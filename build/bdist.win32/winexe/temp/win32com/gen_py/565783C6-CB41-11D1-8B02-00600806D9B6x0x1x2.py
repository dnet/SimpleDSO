# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.6.4 (r264:75708, Oct 26 2009, 08:23:19) [MSC v.1500 32 bit (Intel)]
# From type library '{565783C6-CB41-11D1-8B02-00600806D9B6}'
# On Sat Nov 06 11:24:42 2010
"""Microsoft WMI Scripting V1.2 Library"""
makepy_version = '0.5.00'
python_version = 0x20604f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{565783C6-CB41-11D1-8B02-00600806D9B6}')
MajorVersion = 1
MinorVersion = 2
LibraryFlags = 8
LCID = 0x0

class constants:
	wbemAuthenticationLevelCall   =3          # from enum WbemAuthenticationLevelEnum
	wbemAuthenticationLevelConnect=2          # from enum WbemAuthenticationLevelEnum
	wbemAuthenticationLevelDefault=0          # from enum WbemAuthenticationLevelEnum
	wbemAuthenticationLevelNone   =1          # from enum WbemAuthenticationLevelEnum
	wbemAuthenticationLevelPkt    =4          # from enum WbemAuthenticationLevelEnum
	wbemAuthenticationLevelPktIntegrity=5          # from enum WbemAuthenticationLevelEnum
	wbemAuthenticationLevelPktPrivacy=6          # from enum WbemAuthenticationLevelEnum
	wbemChangeFlagAdvisory        =65536      # from enum WbemChangeFlagEnum
	wbemChangeFlagCreateOnly      =2          # from enum WbemChangeFlagEnum
	wbemChangeFlagCreateOrUpdate  =0          # from enum WbemChangeFlagEnum
	wbemChangeFlagStrongValidation=128        # from enum WbemChangeFlagEnum
	wbemChangeFlagUpdateCompatible=0          # from enum WbemChangeFlagEnum
	wbemChangeFlagUpdateForceMode =64         # from enum WbemChangeFlagEnum
	wbemChangeFlagUpdateOnly      =1          # from enum WbemChangeFlagEnum
	wbemChangeFlagUpdateSafeMode  =32         # from enum WbemChangeFlagEnum
	wbemCimtypeBoolean            =11         # from enum WbemCimtypeEnum
	wbemCimtypeChar16             =103        # from enum WbemCimtypeEnum
	wbemCimtypeDatetime           =101        # from enum WbemCimtypeEnum
	wbemCimtypeObject             =13         # from enum WbemCimtypeEnum
	wbemCimtypeReal32             =4          # from enum WbemCimtypeEnum
	wbemCimtypeReal64             =5          # from enum WbemCimtypeEnum
	wbemCimtypeReference          =102        # from enum WbemCimtypeEnum
	wbemCimtypeSint16             =2          # from enum WbemCimtypeEnum
	wbemCimtypeSint32             =3          # from enum WbemCimtypeEnum
	wbemCimtypeSint64             =20         # from enum WbemCimtypeEnum
	wbemCimtypeSint8              =16         # from enum WbemCimtypeEnum
	wbemCimtypeString             =8          # from enum WbemCimtypeEnum
	wbemCimtypeUint16             =18         # from enum WbemCimtypeEnum
	wbemCimtypeUint32             =19         # from enum WbemCimtypeEnum
	wbemCimtypeUint64             =21         # from enum WbemCimtypeEnum
	wbemCimtypeUint8              =17         # from enum WbemCimtypeEnum
	wbemComparisonFlagIgnoreCase  =16         # from enum WbemComparisonFlagEnum
	wbemComparisonFlagIgnoreClass =8          # from enum WbemComparisonFlagEnum
	wbemComparisonFlagIgnoreDefaultValues=4          # from enum WbemComparisonFlagEnum
	wbemComparisonFlagIgnoreFlavor=32         # from enum WbemComparisonFlagEnum
	wbemComparisonFlagIgnoreObjectSource=2          # from enum WbemComparisonFlagEnum
	wbemComparisonFlagIgnoreQualifiers=1          # from enum WbemComparisonFlagEnum
	wbemComparisonFlagIncludeAll  =0          # from enum WbemComparisonFlagEnum
	wbemConnectFlagUseMaxWait     =128        # from enum WbemConnectOptionsEnum
	wbemErrAccessDenied           =-2147217405 # from enum WbemErrorEnum
	wbemErrAggregatingByObject    =-2147217315 # from enum WbemErrorEnum
	wbemErrAlreadyExists          =-2147217383 # from enum WbemErrorEnum
	wbemErrAmbiguousOperation     =-2147217301 # from enum WbemErrorEnum
	wbemErrAmendedObject          =-2147217306 # from enum WbemErrorEnum
	wbemErrBackupRestoreWinmgmtRunning=-2147217312 # from enum WbemErrorEnum
	wbemErrBufferTooSmall         =-2147217348 # from enum WbemErrorEnum
	wbemErrCallCancelled          =-2147217358 # from enum WbemErrorEnum
	wbemErrCannotBeAbstract       =-2147217307 # from enum WbemErrorEnum
	wbemErrCannotBeKey            =-2147217377 # from enum WbemErrorEnum
	wbemErrCannotBeSingleton      =-2147217364 # from enum WbemErrorEnum
	wbemErrCannotChangeIndexInheritance=-2147217328 # from enum WbemErrorEnum
	wbemErrCannotChangeKeyInheritance=-2147217335 # from enum WbemErrorEnum
	wbemErrCircularReference      =-2147217337 # from enum WbemErrorEnum
	wbemErrClassHasChildren       =-2147217371 # from enum WbemErrorEnum
	wbemErrClassHasInstances      =-2147217370 # from enum WbemErrorEnum
	wbemErrClassNameTooWide       =-2147217292 # from enum WbemErrorEnum
	wbemErrClientTooSlow          =-2147217305 # from enum WbemErrorEnum
	wbemErrConnectionFailed       =-2147217295 # from enum WbemErrorEnum
	wbemErrCriticalError          =-2147217398 # from enum WbemErrorEnum
	wbemErrDatabaseVerMismatch    =-2147217288 # from enum WbemErrorEnum
	wbemErrEncryptedConnectionRequired=-2147217273 # from enum WbemErrorEnum
	wbemErrFailed                 =-2147217407 # from enum WbemErrorEnum
	wbemErrFatalTransportError    =-2147217274 # from enum WbemErrorEnum
	wbemErrForcedRollback         =-2147217298 # from enum WbemErrorEnum
	wbemErrHandleOutOfDate        =-2147217296 # from enum WbemErrorEnum
	wbemErrIllegalNull            =-2147217368 # from enum WbemErrorEnum
	wbemErrIllegalOperation       =-2147217378 # from enum WbemErrorEnum
	wbemErrIncompleteClass        =-2147217376 # from enum WbemErrorEnum
	wbemErrInitializationFailure  =-2147217388 # from enum WbemErrorEnum
	wbemErrInvalidAssociation     =-2147217302 # from enum WbemErrorEnum
	wbemErrInvalidCimType         =-2147217363 # from enum WbemErrorEnum
	wbemErrInvalidClass           =-2147217392 # from enum WbemErrorEnum
	wbemErrInvalidContext         =-2147217401 # from enum WbemErrorEnum
	wbemErrInvalidDuplicateParameter=-2147217341 # from enum WbemErrorEnum
	wbemErrInvalidFlavor          =-2147217338 # from enum WbemErrorEnum
	wbemErrInvalidHandleRequest   =-2147217294 # from enum WbemErrorEnum
	wbemErrInvalidLocale          =-2147217280 # from enum WbemErrorEnum
	wbemErrInvalidMethod          =-2147217362 # from enum WbemErrorEnum
	wbemErrInvalidMethodParameters=-2147217361 # from enum WbemErrorEnum
	wbemErrInvalidNamespace       =-2147217394 # from enum WbemErrorEnum
	wbemErrInvalidObject          =-2147217393 # from enum WbemErrorEnum
	wbemErrInvalidObjectPath      =-2147217350 # from enum WbemErrorEnum
	wbemErrInvalidOperation       =-2147217386 # from enum WbemErrorEnum
	wbemErrInvalidOperator        =-2147217309 # from enum WbemErrorEnum
	wbemErrInvalidParameter       =-2147217400 # from enum WbemErrorEnum
	wbemErrInvalidParameterId     =-2147217353 # from enum WbemErrorEnum
	wbemErrInvalidProperty        =-2147217359 # from enum WbemErrorEnum
	wbemErrInvalidPropertyType    =-2147217366 # from enum WbemErrorEnum
	wbemErrInvalidProviderRegistration=-2147217390 # from enum WbemErrorEnum
	wbemErrInvalidQualifier       =-2147217342 # from enum WbemErrorEnum
	wbemErrInvalidQualifierType   =-2147217367 # from enum WbemErrorEnum
	wbemErrInvalidQuery           =-2147217385 # from enum WbemErrorEnum
	wbemErrInvalidQueryType       =-2147217384 # from enum WbemErrorEnum
	wbemErrInvalidStream          =-2147217397 # from enum WbemErrorEnum
	wbemErrInvalidSuperclass      =-2147217395 # from enum WbemErrorEnum
	wbemErrInvalidSyntax          =-2147217375 # from enum WbemErrorEnum
	wbemErrLocalCredentials       =-2147217308 # from enum WbemErrorEnum
	wbemErrMarshalInvalidSignature=-2147217343 # from enum WbemErrorEnum
	wbemErrMarshalVersionMismatch =-2147217344 # from enum WbemErrorEnum
	wbemErrMethodDisabled         =-2147217322 # from enum WbemErrorEnum
	wbemErrMethodNameTooWide      =-2147217291 # from enum WbemErrorEnum
	wbemErrMethodNotImplemented   =-2147217323 # from enum WbemErrorEnum
	wbemErrMissingAggregationList =-2147217317 # from enum WbemErrorEnum
	wbemErrMissingGroupWithin     =-2147217318 # from enum WbemErrorEnum
	wbemErrMissingParameter       =-2147217354 # from enum WbemErrorEnum
	wbemErrNoSchema               =-2147217277 # from enum WbemErrorEnum
	wbemErrNonConsecutiveParameterIds=-2147217352 # from enum WbemErrorEnum
	wbemErrNondecoratedObject     =-2147217374 # from enum WbemErrorEnum
	wbemErrNotAvailable           =-2147217399 # from enum WbemErrorEnum
	wbemErrNotEventClass          =-2147217319 # from enum WbemErrorEnum
	wbemErrNotFound               =-2147217406 # from enum WbemErrorEnum
	wbemErrNotSupported           =-2147217396 # from enum WbemErrorEnum
	wbemErrNullSecurityDescriptor =-2147217304 # from enum WbemErrorEnum
	wbemErrOutOfDiskSpace         =-2147217349 # from enum WbemErrorEnum
	wbemErrOutOfMemory            =-2147217402 # from enum WbemErrorEnum
	wbemErrOverrideNotAllowed     =-2147217382 # from enum WbemErrorEnum
	wbemErrParameterIdOnRetval    =-2147217351 # from enum WbemErrorEnum
	wbemErrPrivilegeNotHeld       =-2147217310 # from enum WbemErrorEnum
	wbemErrPropagatedMethod       =-2147217356 # from enum WbemErrorEnum
	wbemErrPropagatedProperty     =-2147217380 # from enum WbemErrorEnum
	wbemErrPropagatedQualifier    =-2147217381 # from enum WbemErrorEnum
	wbemErrPropertyNameTooWide    =-2147217293 # from enum WbemErrorEnum
	wbemErrPropertyNotAnObject    =-2147217316 # from enum WbemErrorEnum
	wbemErrProviderAlreadyRegistered=-2147217276 # from enum WbemErrorEnum
	wbemErrProviderFailure        =-2147217404 # from enum WbemErrorEnum
	wbemErrProviderLoadFailure    =-2147217389 # from enum WbemErrorEnum
	wbemErrProviderNotCapable     =-2147217372 # from enum WbemErrorEnum
	wbemErrProviderNotFound       =-2147217391 # from enum WbemErrorEnum
	wbemErrProviderNotRegistered  =-2147217275 # from enum WbemErrorEnum
	wbemErrProviderSuspended      =-2147217279 # from enum WbemErrorEnum
	wbemErrQualifierNameTooWide   =-2147217290 # from enum WbemErrorEnum
	wbemErrQueryNotImplemented    =-2147217369 # from enum WbemErrorEnum
	wbemErrQueueOverflow          =-2147217311 # from enum WbemErrorEnum
	wbemErrQuotaViolation         =-2147217300 # from enum WbemErrorEnum
	wbemErrReadOnly               =-2147217373 # from enum WbemErrorEnum
	wbemErrRefresherBusy          =-2147217321 # from enum WbemErrorEnum
	wbemErrRegistrationTooBroad   =-2147213311 # from enum WbemErrorEnum
	wbemErrRegistrationTooPrecise =-2147213310 # from enum WbemErrorEnum
	wbemErrRerunCommand           =-2147217289 # from enum WbemErrorEnum
	wbemErrResetToDefault         =-2147209214 # from enum WbemErrorEnum
	wbemErrServerTooBusy          =-2147217339 # from enum WbemErrorEnum
	wbemErrShuttingDown           =-2147217357 # from enum WbemErrorEnum
	wbemErrSynchronizationRequired=-2147217278 # from enum WbemErrorEnum
	wbemErrSystemProperty         =-2147217360 # from enum WbemErrorEnum
	wbemErrTimedout               =-2147209215 # from enum WbemErrorEnum
	wbemErrTimeout                =-2147217303 # from enum WbemErrorEnum
	wbemErrTooManyProperties      =-2147217327 # from enum WbemErrorEnum
	wbemErrTooMuchData            =-2147217340 # from enum WbemErrorEnum
	wbemErrTransactionConflict    =-2147217299 # from enum WbemErrorEnum
	wbemErrTransportFailure       =-2147217387 # from enum WbemErrorEnum
	wbemErrTypeMismatch           =-2147217403 # from enum WbemErrorEnum
	wbemErrUnexpected             =-2147217379 # from enum WbemErrorEnum
	wbemErrUninterpretableProviderQuery=-2147217313 # from enum WbemErrorEnum
	wbemErrUnknownObjectType      =-2147217346 # from enum WbemErrorEnum
	wbemErrUnknownPacketType      =-2147217345 # from enum WbemErrorEnum
	wbemErrUnparsableQuery        =-2147217320 # from enum WbemErrorEnum
	wbemErrUnsupportedClassUpdate =-2147217336 # from enum WbemErrorEnum
	wbemErrUnsupportedLocale      =-2147217297 # from enum WbemErrorEnum
	wbemErrUnsupportedParameter   =-2147217355 # from enum WbemErrorEnum
	wbemErrUnsupportedPutExtension=-2147217347 # from enum WbemErrorEnum
	wbemErrUpdateOverrideNotAllowed=-2147217325 # from enum WbemErrorEnum
	wbemErrUpdatePropagatedMethod =-2147217324 # from enum WbemErrorEnum
	wbemErrUpdateTypeMismatch     =-2147217326 # from enum WbemErrorEnum
	wbemErrValueOutOfRange        =-2147217365 # from enum WbemErrorEnum
	wbemErrVetoDelete             =-2147217286 # from enum WbemErrorEnum
	wbemErrVetoPut                =-2147217287 # from enum WbemErrorEnum
	wbemNoErr                     =0          # from enum WbemErrorEnum
	wbemFlagBidirectional         =0          # from enum WbemFlagEnum
	wbemFlagDirectRead            =512        # from enum WbemFlagEnum
	wbemFlagDontSendStatus        =0          # from enum WbemFlagEnum
	wbemFlagEnsureLocatable       =256        # from enum WbemFlagEnum
	wbemFlagForwardOnly           =32         # from enum WbemFlagEnum
	wbemFlagGetDefault            =0          # from enum WbemFlagEnum
	wbemFlagNoErrorObject         =64         # from enum WbemFlagEnum
	wbemFlagReturnErrorObject     =0          # from enum WbemFlagEnum
	wbemFlagReturnImmediately     =16         # from enum WbemFlagEnum
	wbemFlagReturnWhenComplete    =0          # from enum WbemFlagEnum
	wbemFlagSendOnlySelected      =0          # from enum WbemFlagEnum
	wbemFlagSendStatus            =128        # from enum WbemFlagEnum
	wbemFlagSpawnInstance         =1          # from enum WbemFlagEnum
	wbemFlagUseAmendedQualifiers  =131072     # from enum WbemFlagEnum
	wbemFlagUseCurrentTime        =1          # from enum WbemFlagEnum
	wbemImpersonationLevelAnonymous=1          # from enum WbemImpersonationLevelEnum
	wbemImpersonationLevelDelegate=4          # from enum WbemImpersonationLevelEnum
	wbemImpersonationLevelIdentify=2          # from enum WbemImpersonationLevelEnum
	wbemImpersonationLevelImpersonate=3          # from enum WbemImpersonationLevelEnum
	wbemObjectTextFormatCIMDTD20  =1          # from enum WbemObjectTextFormatEnum
	wbemObjectTextFormatWMIDTD20  =2          # from enum WbemObjectTextFormatEnum
	wbemPrivilegeAudit            =20         # from enum WbemPrivilegeEnum
	wbemPrivilegeBackup           =16         # from enum WbemPrivilegeEnum
	wbemPrivilegeChangeNotify     =22         # from enum WbemPrivilegeEnum
	wbemPrivilegeCreatePagefile   =14         # from enum WbemPrivilegeEnum
	wbemPrivilegeCreatePermanent  =15         # from enum WbemPrivilegeEnum
	wbemPrivilegeCreateToken      =1          # from enum WbemPrivilegeEnum
	wbemPrivilegeDebug            =19         # from enum WbemPrivilegeEnum
	wbemPrivilegeEnableDelegation =26         # from enum WbemPrivilegeEnum
	wbemPrivilegeIncreaseBasePriority=13         # from enum WbemPrivilegeEnum
	wbemPrivilegeIncreaseQuota    =4          # from enum WbemPrivilegeEnum
	wbemPrivilegeLoadDriver       =9          # from enum WbemPrivilegeEnum
	wbemPrivilegeLockMemory       =3          # from enum WbemPrivilegeEnum
	wbemPrivilegeMachineAccount   =5          # from enum WbemPrivilegeEnum
	wbemPrivilegeManageVolume     =27         # from enum WbemPrivilegeEnum
	wbemPrivilegePrimaryToken     =2          # from enum WbemPrivilegeEnum
	wbemPrivilegeProfileSingleProcess=12         # from enum WbemPrivilegeEnum
	wbemPrivilegeRemoteShutdown   =23         # from enum WbemPrivilegeEnum
	wbemPrivilegeRestore          =17         # from enum WbemPrivilegeEnum
	wbemPrivilegeSecurity         =7          # from enum WbemPrivilegeEnum
	wbemPrivilegeShutdown         =18         # from enum WbemPrivilegeEnum
	wbemPrivilegeSyncAgent        =25         # from enum WbemPrivilegeEnum
	wbemPrivilegeSystemEnvironment=21         # from enum WbemPrivilegeEnum
	wbemPrivilegeSystemProfile    =10         # from enum WbemPrivilegeEnum
	wbemPrivilegeSystemtime       =11         # from enum WbemPrivilegeEnum
	wbemPrivilegeTakeOwnership    =8          # from enum WbemPrivilegeEnum
	wbemPrivilegeTcb              =6          # from enum WbemPrivilegeEnum
	wbemPrivilegeUndock           =24         # from enum WbemPrivilegeEnum
	wbemQueryFlagDeep             =0          # from enum WbemQueryFlagEnum
	wbemQueryFlagPrototype        =2          # from enum WbemQueryFlagEnum
	wbemQueryFlagShallow          =1          # from enum WbemQueryFlagEnum
	wbemTextFlagNoFlavors         =1          # from enum WbemTextFlagEnum
	wbemTimeoutInfinite           =-1         # from enum WbemTimeout

from win32com.client import DispatchBaseClass
class ISWbemDateTime(DispatchBaseClass):
	"""A Datetime"""
	CLSID = IID('{5E97458A-CF77-11D3-B38F-00105A1F473A}')
	coclass_clsid = IID('{47DFBE54-CF76-11D3-B38F-00105A1F473A}')

	def GetFileTime(self, bIsLocal=True):
		"""Retrieve value in FILETIME compatible string representation"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(20, LCID, 1, (8, 0), ((11, 49),),bIsLocal
			)

	def GetVarDate(self, bIsLocal=True):
		"""Retrieve value in Variant compatible (VT_DATE) format"""
		return self._oleobj_.InvokeTypes(18, LCID, 1, (7, 0), ((11, 49),),bIsLocal
			)

	def SetFileTime(self, strFileTime=defaultNamedNotOptArg, bIsLocal=True):
		"""Set the value using FILETIME compatible string representation"""
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((8, 1), (11, 49)),strFileTime
			, bIsLocal)

	def SetVarDate(self, dVarDate=defaultNamedNotOptArg, bIsLocal=True):
		"""Set the value using Variant compatible (VT_DATE) format"""
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((7, 1), (11, 49)),dVarDate
			, bIsLocal)

	_prop_map_get_ = {
		"Day": (5, 2, (3, 0), (), "Day", None),
		"DaySpecified": (6, 2, (11, 0), (), "DaySpecified", None),
		"Hours": (7, 2, (3, 0), (), "Hours", None),
		"HoursSpecified": (8, 2, (11, 0), (), "HoursSpecified", None),
		"IsInterval": (17, 2, (11, 0), (), "IsInterval", None),
		"Microseconds": (13, 2, (3, 0), (), "Microseconds", None),
		"MicrosecondsSpecified": (14, 2, (11, 0), (), "MicrosecondsSpecified", None),
		"Minutes": (9, 2, (3, 0), (), "Minutes", None),
		"MinutesSpecified": (10, 2, (11, 0), (), "MinutesSpecified", None),
		"Month": (3, 2, (3, 0), (), "Month", None),
		"MonthSpecified": (4, 2, (11, 0), (), "MonthSpecified", None),
		"Seconds": (11, 2, (3, 0), (), "Seconds", None),
		"SecondsSpecified": (12, 2, (11, 0), (), "SecondsSpecified", None),
		"UTC": (15, 2, (3, 0), (), "UTC", None),
		"UTCSpecified": (16, 2, (11, 0), (), "UTCSpecified", None),
		"Value": (0, 2, (8, 0), (), "Value", None),
		"Year": (1, 2, (3, 0), (), "Year", None),
		"YearSpecified": (2, 2, (11, 0), (), "YearSpecified", None),
	}
	_prop_map_put_ = {
		"Day": ((5, LCID, 4, 0),()),
		"DaySpecified": ((6, LCID, 4, 0),()),
		"Hours": ((7, LCID, 4, 0),()),
		"HoursSpecified": ((8, LCID, 4, 0),()),
		"IsInterval": ((17, LCID, 4, 0),()),
		"Microseconds": ((13, LCID, 4, 0),()),
		"MicrosecondsSpecified": ((14, LCID, 4, 0),()),
		"Minutes": ((9, LCID, 4, 0),()),
		"MinutesSpecified": ((10, LCID, 4, 0),()),
		"Month": ((3, LCID, 4, 0),()),
		"MonthSpecified": ((4, LCID, 4, 0),()),
		"Seconds": ((11, LCID, 4, 0),()),
		"SecondsSpecified": ((12, LCID, 4, 0),()),
		"UTC": ((15, LCID, 4, 0),()),
		"UTCSpecified": ((16, LCID, 4, 0),()),
		"Value": ((0, LCID, 4, 0),()),
		"Year": ((1, LCID, 4, 0),()),
		"YearSpecified": ((2, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Value", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ISWbemEventSource(DispatchBaseClass):
	"""An Event source"""
	CLSID = IID('{27D54D92-0EBE-11D2-8B22-00600806D9B6}')
	coclass_clsid = IID('{04B83D58-21AE-11D2-8B33-00600806D9B6}')

	# Result is of type ISWbemObject
	def NextEvent(self, iTimeoutMs=-1):
		"""Retrieve the next event within a specified time period. The timeout is specified in milliseconds."""
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((3, 49),),iTimeoutMs
			)
		if ret is not None:
			ret = Dispatch(ret, u'NextEvent', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	_prop_map_get_ = {
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (2, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemLastError(DispatchBaseClass):
	"""The last error on the current thread"""
	CLSID = IID('{D962DB84-D4BB-11D1-8B09-00600806D9B6}')
	coclass_clsid = IID('{C2FEEEAC-CFCD-11D1-8B05-00600806D9B6}')

	def AssociatorsAsync_(self, objWbemSink=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u'', strResultRole=u''
			, strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u''
			, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the Associators of this Object asynchronously"""
		return self._ApplyTypes_(10, 1, (24, 32), ((9, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'AssociatorsAsync_', None,objWbemSink
			, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly
			, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet
			, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Associators_(self, strAssocClass=u'', strResultClass=u'', strResultRole=u'', strRole=u''
			, bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u'', iFlags=16
			, objWbemNamedValueSet=None):
		"""Get the Associators of this Object"""
		return self._ApplyTypes_(9, 1, (9, 32), ((8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49)), u'Associators_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strAssocClass
			, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly
			, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet)

	# Result is of type ISWbemObject
	def Clone_(self):
		"""Clone this Object"""
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'Clone_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def CompareTo_(self, objWbemObject=defaultNamedNotOptArg, iFlags=0):
		"""Compare this Object with another"""
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((9, 1), (3, 49)),objWbemObject
			, iFlags)

	def DeleteAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Delete this Object asynchronously"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	def Delete_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Delete this Object"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)

	def ExecMethodAsync_(self, objWbemSink=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute a Method of this Object asynchronously"""
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((9, 1), (8, 1), (9, 49), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObject
	def ExecMethod_(self, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0, objWbemNamedValueSet=None):
		"""Execute a Method of this Object"""
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((8, 1), (9, 49), (3, 49), (9, 49)),strMethodName
			, objWbemInParameters, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'ExecMethod_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def GetObjectText_(self, iFlags=0):
		"""Get the MOF text of this Object"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(16, LCID, 1, (8, 0), ((3, 49),),iFlags
			)

	def InstancesAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Return all instances of this Class asynchronously"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Instances_(self, iFlags=16, objWbemNamedValueSet=None):
		"""Return all instances of this Class"""
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Instances_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def PutAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Save this Object asynchronously"""
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectPath
	def Put_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Save this Object"""
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Put_', '{5791BC27-CE9C-11D1-97BF-0000F81E849C}')
		return ret

	def ReferencesAsync_(self, objWbemSink=defaultNamedNotOptArg, strResultClass=u'', strRole=u'', bClassesOnly=False
			, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the References to this Object asynchronously"""
		return self._ApplyTypes_(12, 1, (24, 32), ((9, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'ReferencesAsync_', None,objWbemSink
			, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def References_(self, strResultClass=u'', strRole=u'', bClassesOnly=False, bSchemaOnly=False
			, strRequiredQualifier=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Get the References to this Object"""
		return self._ApplyTypes_(11, 1, (9, 32), ((8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49)), u'References_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strResultClass
			, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags
			, objWbemNamedValueSet)

	# Result is of type ISWbemObject
	def SpawnDerivedClass_(self, iFlags=0):
		"""Create a subclass of this Object"""
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 49),),iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'SpawnDerivedClass_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	# Result is of type ISWbemObject
	def SpawnInstance_(self, iFlags=0):
		"""Create an Instance of this Object"""
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((3, 49),),iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'SpawnInstance_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def SubclassesAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Enumerate subclasses of this Class asynchronously"""
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Subclasses_(self, iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate subclasses of this Class"""
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Subclasses_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	_prop_map_get_ = {
		"Derivation_": (23, 2, (12, 0), (), "Derivation_", None),
		# Method 'Methods_' returns object of type 'ISWbemMethodSet'
		"Methods_": (22, 2, (9, 0), (), "Methods_", '{C93BA292-D955-11D1-8B09-00600806D9B6}'),
		# Method 'Path_' returns object of type 'ISWbemObjectPath'
		"Path_": (24, 2, (9, 0), (), "Path_", '{5791BC27-CE9C-11D1-97BF-0000F81E849C}'),
		# Method 'Properties_' returns object of type 'ISWbemPropertySet'
		"Properties_": (21, 2, (9, 0), (), "Properties_", '{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}'),
		# Method 'Qualifiers_' returns object of type 'ISWbemQualifierSet'
		"Qualifiers_": (20, 2, (9, 0), (), "Qualifiers_", '{9B16ED16-D3DF-11D1-8B08-00600806D9B6}'),
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (25, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemLocator(DispatchBaseClass):
	"""Used to obtain Namespace connections"""
	CLSID = IID('{76A6415B-CB41-11D1-8B02-00600806D9B6}')
	coclass_clsid = IID('{76A64158-CB41-11D1-8B02-00600806D9B6}')

	# Result is of type ISWbemServices
	def ConnectServer(self, strServer=u'.', strNamespace=u'', strUser=u'', strPassword=u''
			, strLocale=u'', strAuthority=u'', iSecurityFlags=0, objWbemNamedValueSet=None):
		"""Connect to a Namespace"""
		return self._ApplyTypes_(1, 1, (9, 32), ((8, 49), (8, 49), (8, 49), (8, 49), (8, 49), (8, 49), (3, 49), (9, 49)), u'ConnectServer', '{76A6415C-CB41-11D1-8B02-00600806D9B6}',strServer
			, strNamespace, strUser, strPassword, strLocale, strAuthority
			, iSecurityFlags, objWbemNamedValueSet)

	_prop_map_get_ = {
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (2, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemMethod(DispatchBaseClass):
	"""A Method"""
	CLSID = IID('{422E8E90-D955-11D1-8B09-00600806D9B6}')
	coclass_clsid = IID('{04B83D5B-21AE-11D2-8B33-00600806D9B6}')

	_prop_map_get_ = {
		# Method 'InParameters' returns object of type 'ISWbemObject'
		"InParameters": (3, 2, (9, 0), (), "InParameters", '{76A6415A-CB41-11D1-8B02-00600806D9B6}'),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Origin": (2, 2, (8, 0), (), "Origin", None),
		# Method 'OutParameters' returns object of type 'ISWbemObject'
		"OutParameters": (4, 2, (9, 0), (), "OutParameters", '{76A6415A-CB41-11D1-8B02-00600806D9B6}'),
		# Method 'Qualifiers_' returns object of type 'ISWbemQualifierSet'
		"Qualifiers_": (5, 2, (9, 0), (), "Qualifiers_", '{9B16ED16-D3DF-11D1-8B08-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemMethodSet(DispatchBaseClass):
	"""A collection of Methods"""
	CLSID = IID('{C93BA292-D955-11D1-8B09-00600806D9B6}')
	coclass_clsid = IID('{04B83D5A-21AE-11D2-8B33-00600806D9B6}')

	# Result is of type ISWbemMethod
	def Item(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Get a named Method from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strName
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{422E8E90-D955-11D1-8B09-00600806D9B6}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Get a named Method from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strName
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{422E8E90-D955-11D1-8B09-00600806D9B6}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{422E8E90-D955-11D1-8B09-00600806D9B6}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{422E8E90-D955-11D1-8B09-00600806D9B6}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemNamedValue(DispatchBaseClass):
	"""A named value"""
	CLSID = IID('{76A64164-CB41-11D1-8B02-00600806D9B6}')
	coclass_clsid = IID('{04B83D60-21AE-11D2-8B33-00600806D9B6}')

	_prop_map_get_ = {
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Value": (0, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (12, 0), (), "Value", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ISWbemNamedValueSet(DispatchBaseClass):
	"""A collection of named values"""
	CLSID = IID('{CF2376EA-CE8C-11D1-8B05-00600806D9B6}')
	coclass_clsid = IID('{9AED384E-CE8B-11D1-8B05-00600806D9B6}')

	# Result is of type ISWbemNamedValue
	def Add(self, strName=defaultNamedNotOptArg, varValue=defaultNamedNotOptArg, iFlags=0):
		"""Add a named value to this collection"""
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1), (16396, 1), (3, 49)),strName
			, varValue, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{76A64164-CB41-11D1-8B02-00600806D9B6}')
		return ret

	# Result is of type ISWbemNamedValueSet
	def Clone(self):
		"""Make a copy of this collection"""
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'Clone', '{CF2376EA-CE8C-11D1-8B05-00600806D9B6}')
		return ret

	def DeleteAll(self):
		"""Delete all items in this collection"""
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	# Result is of type ISWbemNamedValue
	def Item(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Get a named value from this Collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strName
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{76A64164-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def Remove(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Remove a named value from this collection"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (3, 49)),strName
			, iFlags)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Get a named value from this Collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strName
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{76A64164-CB41-11D1-8B02-00600806D9B6}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{76A64164-CB41-11D1-8B02-00600806D9B6}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{76A64164-CB41-11D1-8B02-00600806D9B6}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemObject(DispatchBaseClass):
	"""A Class or Instance"""
	CLSID = IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')
	coclass_clsid = IID('{04B83D62-21AE-11D2-8B33-00600806D9B6}')

	def AssociatorsAsync_(self, objWbemSink=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u'', strResultRole=u''
			, strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u''
			, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the Associators of this Object asynchronously"""
		return self._ApplyTypes_(10, 1, (24, 32), ((9, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'AssociatorsAsync_', None,objWbemSink
			, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly
			, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet
			, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Associators_(self, strAssocClass=u'', strResultClass=u'', strResultRole=u'', strRole=u''
			, bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u'', iFlags=16
			, objWbemNamedValueSet=None):
		"""Get the Associators of this Object"""
		return self._ApplyTypes_(9, 1, (9, 32), ((8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49)), u'Associators_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strAssocClass
			, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly
			, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet)

	# Result is of type ISWbemObject
	def Clone_(self):
		"""Clone this Object"""
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'Clone_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def CompareTo_(self, objWbemObject=defaultNamedNotOptArg, iFlags=0):
		"""Compare this Object with another"""
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((9, 1), (3, 49)),objWbemObject
			, iFlags)

	def DeleteAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Delete this Object asynchronously"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	def Delete_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Delete this Object"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)

	def ExecMethodAsync_(self, objWbemSink=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute a Method of this Object asynchronously"""
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((9, 1), (8, 1), (9, 49), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObject
	def ExecMethod_(self, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0, objWbemNamedValueSet=None):
		"""Execute a Method of this Object"""
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((8, 1), (9, 49), (3, 49), (9, 49)),strMethodName
			, objWbemInParameters, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'ExecMethod_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def GetObjectText_(self, iFlags=0):
		"""Get the MOF text of this Object"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(16, LCID, 1, (8, 0), ((3, 49),),iFlags
			)

	def InstancesAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Return all instances of this Class asynchronously"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Instances_(self, iFlags=16, objWbemNamedValueSet=None):
		"""Return all instances of this Class"""
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Instances_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def PutAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Save this Object asynchronously"""
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectPath
	def Put_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Save this Object"""
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Put_', '{5791BC27-CE9C-11D1-97BF-0000F81E849C}')
		return ret

	def ReferencesAsync_(self, objWbemSink=defaultNamedNotOptArg, strResultClass=u'', strRole=u'', bClassesOnly=False
			, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the References to this Object asynchronously"""
		return self._ApplyTypes_(12, 1, (24, 32), ((9, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'ReferencesAsync_', None,objWbemSink
			, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def References_(self, strResultClass=u'', strRole=u'', bClassesOnly=False, bSchemaOnly=False
			, strRequiredQualifier=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Get the References to this Object"""
		return self._ApplyTypes_(11, 1, (9, 32), ((8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49)), u'References_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strResultClass
			, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags
			, objWbemNamedValueSet)

	# Result is of type ISWbemObject
	def SpawnDerivedClass_(self, iFlags=0):
		"""Create a subclass of this Object"""
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 49),),iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'SpawnDerivedClass_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	# Result is of type ISWbemObject
	def SpawnInstance_(self, iFlags=0):
		"""Create an Instance of this Object"""
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((3, 49),),iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'SpawnInstance_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def SubclassesAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Enumerate subclasses of this Class asynchronously"""
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Subclasses_(self, iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate subclasses of this Class"""
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Subclasses_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	_prop_map_get_ = {
		"Derivation_": (23, 2, (12, 0), (), "Derivation_", None),
		# Method 'Methods_' returns object of type 'ISWbemMethodSet'
		"Methods_": (22, 2, (9, 0), (), "Methods_", '{C93BA292-D955-11D1-8B09-00600806D9B6}'),
		# Method 'Path_' returns object of type 'ISWbemObjectPath'
		"Path_": (24, 2, (9, 0), (), "Path_", '{5791BC27-CE9C-11D1-97BF-0000F81E849C}'),
		# Method 'Properties_' returns object of type 'ISWbemPropertySet'
		"Properties_": (21, 2, (9, 0), (), "Properties_", '{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}'),
		# Method 'Qualifiers_' returns object of type 'ISWbemQualifierSet'
		"Qualifiers_": (20, 2, (9, 0), (), "Qualifiers_", '{9B16ED16-D3DF-11D1-8B08-00600806D9B6}'),
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (25, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemObjectEx(DispatchBaseClass):
	"""A Class or Instance"""
	CLSID = IID('{269AD56A-8A67-4129-BC8C-0506DCFE9880}')
	coclass_clsid = IID('{D6BDAFB2-9435-491F-BB87-6AA0F0BC31A2}')

	def AssociatorsAsync_(self, objWbemSink=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u'', strResultRole=u''
			, strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u''
			, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the Associators of this Object asynchronously"""
		return self._ApplyTypes_(10, 1, (24, 32), ((9, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'AssociatorsAsync_', None,objWbemSink
			, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly
			, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet
			, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Associators_(self, strAssocClass=u'', strResultClass=u'', strResultRole=u'', strRole=u''
			, bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u'', iFlags=16
			, objWbemNamedValueSet=None):
		"""Get the Associators of this Object"""
		return self._ApplyTypes_(9, 1, (9, 32), ((8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49)), u'Associators_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strAssocClass
			, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly
			, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet)

	# Result is of type ISWbemObject
	def Clone_(self):
		"""Clone this Object"""
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'Clone_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def CompareTo_(self, objWbemObject=defaultNamedNotOptArg, iFlags=0):
		"""Compare this Object with another"""
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((9, 1), (3, 49)),objWbemObject
			, iFlags)

	def DeleteAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Delete this Object asynchronously"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	def Delete_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Delete this Object"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)

	def ExecMethodAsync_(self, objWbemSink=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute a Method of this Object asynchronously"""
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((9, 1), (8, 1), (9, 49), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObject
	def ExecMethod_(self, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0, objWbemNamedValueSet=None):
		"""Execute a Method of this Object"""
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((8, 1), (9, 49), (3, 49), (9, 49)),strMethodName
			, objWbemInParameters, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'ExecMethod_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def GetObjectText_(self, iFlags=0):
		"""Get the MOF text of this Object"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(16, LCID, 1, (8, 0), ((3, 49),),iFlags
			)

	def GetText_(self, iObjectTextFormat=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Retrieve a textual representation of this Object"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(28, LCID, 1, (8, 0), ((3, 1), (3, 49), (9, 49)),iObjectTextFormat
			, iFlags, objWbemNamedValueSet)

	def InstancesAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Return all instances of this Class asynchronously"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Instances_(self, iFlags=16, objWbemNamedValueSet=None):
		"""Return all instances of this Class"""
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Instances_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def PutAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Save this Object asynchronously"""
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectPath
	def Put_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Save this Object"""
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Put_', '{5791BC27-CE9C-11D1-97BF-0000F81E849C}')
		return ret

	def ReferencesAsync_(self, objWbemSink=defaultNamedNotOptArg, strResultClass=u'', strRole=u'', bClassesOnly=False
			, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the References to this Object asynchronously"""
		return self._ApplyTypes_(12, 1, (24, 32), ((9, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'ReferencesAsync_', None,objWbemSink
			, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def References_(self, strResultClass=u'', strRole=u'', bClassesOnly=False, bSchemaOnly=False
			, strRequiredQualifier=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Get the References to this Object"""
		return self._ApplyTypes_(11, 1, (9, 32), ((8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49)), u'References_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strResultClass
			, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags
			, objWbemNamedValueSet)

	def Refresh_(self, iFlags=0, objWbemNamedValueSet=None):
		"""Refresh this Object"""
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)

	def SetFromText_(self, bsText=defaultNamedNotOptArg, iObjectTextFormat=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Set this Object using the supplied textual representation"""
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 49), (9, 49)),bsText
			, iObjectTextFormat, iFlags, objWbemNamedValueSet)

	# Result is of type ISWbemObject
	def SpawnDerivedClass_(self, iFlags=0):
		"""Create a subclass of this Object"""
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 49),),iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'SpawnDerivedClass_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	# Result is of type ISWbemObject
	def SpawnInstance_(self, iFlags=0):
		"""Create an Instance of this Object"""
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((3, 49),),iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'SpawnInstance_', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def SubclassesAsync_(self, objWbemSink=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Enumerate subclasses of this Class asynchronously"""
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def Subclasses_(self, iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate subclasses of this Class"""
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 49), (9, 49)),iFlags
			, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Subclasses_', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	_prop_map_get_ = {
		"Derivation_": (23, 2, (12, 0), (), "Derivation_", None),
		# Method 'Methods_' returns object of type 'ISWbemMethodSet'
		"Methods_": (22, 2, (9, 0), (), "Methods_", '{C93BA292-D955-11D1-8B09-00600806D9B6}'),
		# Method 'Path_' returns object of type 'ISWbemObjectPath'
		"Path_": (24, 2, (9, 0), (), "Path_", '{5791BC27-CE9C-11D1-97BF-0000F81E849C}'),
		# Method 'Properties_' returns object of type 'ISWbemPropertySet'
		"Properties_": (21, 2, (9, 0), (), "Properties_", '{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}'),
		# Method 'Qualifiers_' returns object of type 'ISWbemQualifierSet'
		"Qualifiers_": (20, 2, (9, 0), (), "Qualifiers_", '{9B16ED16-D3DF-11D1-8B08-00600806D9B6}'),
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (25, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
		# Method 'SystemProperties_' returns object of type 'ISWbemPropertySet'
		"SystemProperties_": (27, 2, (9, 0), (), "SystemProperties_", '{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemObjectPath(DispatchBaseClass):
	"""An Object path"""
	CLSID = IID('{5791BC27-CE9C-11D1-97BF-0000F81E849C}')
	coclass_clsid = IID('{5791BC26-CE9C-11D1-97BF-0000F81E849C}')

	def SetAsClass(self):
		"""Coerce this path to address a Class"""
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def SetAsSingleton(self):
		"""Coerce this path to address a Singleton Instance"""
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Authority": (14, 2, (8, 0), (), "Authority", None),
		"Class": (6, 2, (8, 0), (), "Class", None),
		"DisplayName": (5, 2, (8, 0), (), "DisplayName", None),
		"IsClass": (7, 2, (11, 0), (), "IsClass", None),
		"IsSingleton": (9, 2, (11, 0), (), "IsSingleton", None),
		# Method 'Keys' returns object of type 'ISWbemNamedValueSet'
		"Keys": (11, 2, (9, 0), (), "Keys", '{CF2376EA-CE8C-11D1-8B05-00600806D9B6}'),
		"Locale": (13, 2, (8, 0), (), "Locale", None),
		"Namespace": (3, 2, (8, 0), (), "Namespace", None),
		"ParentNamespace": (4, 2, (8, 0), (), "ParentNamespace", None),
		"Path": (0, 2, (8, 0), (), "Path", None),
		"RelPath": (1, 2, (8, 0), (), "RelPath", None),
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (12, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
		"Server": (2, 2, (8, 0), (), "Server", None),
	}
	_prop_map_put_ = {
		"Authority": ((14, LCID, 4, 0),()),
		"Class": ((6, LCID, 4, 0),()),
		"DisplayName": ((5, LCID, 4, 0),()),
		"Locale": ((13, LCID, 4, 0),()),
		"Namespace": ((3, LCID, 4, 0),()),
		"Path": ((0, LCID, 4, 0),()),
		"RelPath": ((1, LCID, 4, 0),()),
		"Server": ((2, LCID, 4, 0),()),
	}
	# Default property for this class is 'Path'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Path", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ISWbemObjectSet(DispatchBaseClass):
	"""A collection of Classes or Instances"""
	CLSID = IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')
	coclass_clsid = IID('{04B83D61-21AE-11D2-8B33-00600806D9B6}')

	# Result is of type ISWbemObject
	def Item(self, strObjectPath=defaultNamedNotOptArg, iFlags=0):
		"""Get an Object with a specific path from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strObjectPath
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (4, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, strObjectPath=defaultNamedNotOptArg, iFlags=0):
		"""Get an Object with a specific path from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strObjectPath
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{76A6415A-CB41-11D1-8B02-00600806D9B6}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemPrivilege(DispatchBaseClass):
	"""A Privilege Override"""
	CLSID = IID('{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
	coclass_clsid = IID('{26EE67BC-5804-11D2-8B4A-00600806D9B6}')

	_prop_map_get_ = {
		"DisplayName": (2, 2, (8, 0), (), "DisplayName", None),
		"Identifier": (3, 2, (3, 0), (), "Identifier", None),
		"IsEnabled": (0, 2, (11, 0), (), "IsEnabled", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
		"IsEnabled": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'IsEnabled'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (11, 0), (), "IsEnabled", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ISWbemPrivilegeSet(DispatchBaseClass):
	"""A collection of Privilege Overrides"""
	CLSID = IID('{26EE67BF-5804-11D2-8B4A-00600806D9B6}')
	coclass_clsid = IID('{26EE67BE-5804-11D2-8B4A-00600806D9B6}')

	# Result is of type ISWbemPrivilege
	def Add(self, iPrivilege=defaultNamedNotOptArg, bIsEnabled=True):
		"""Add a Privilege to this collection"""
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((3, 1), (11, 49)),iPrivilege
			, bIsEnabled)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
		return ret

	# Result is of type ISWbemPrivilege
	def AddAsString(self, strPrivilege=defaultNamedNotOptArg, bIsEnabled=True):
		"""Add a named Privilege to this collection"""
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((8, 1), (11, 49)),strPrivilege
			, bIsEnabled)
		if ret is not None:
			ret = Dispatch(ret, u'AddAsString', '{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
		return ret

	def DeleteAll(self):
		"""Delete all items in this collection"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	# Result is of type ISWbemPrivilege
	def Item(self, iPrivilege=defaultNamedNotOptArg):
		"""Get a named Privilege from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),iPrivilege
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
		return ret

	def Remove(self, iPrivilege=defaultNamedNotOptArg):
		"""Remove a Privilege from this collection"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),iPrivilege
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, iPrivilege=defaultNamedNotOptArg):
		"""Get a named Privilege from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),iPrivilege
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemProperty(DispatchBaseClass):
	"""A Property"""
	CLSID = IID('{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
	coclass_clsid = IID('{04B83D5D-21AE-11D2-8B33-00600806D9B6}')

	_prop_map_get_ = {
		"CIMType": (4, 2, (3, 0), (), "CIMType", None),
		"IsArray": (6, 2, (11, 0), (), "IsArray", None),
		"IsLocal": (2, 2, (11, 0), (), "IsLocal", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Origin": (3, 2, (8, 0), (), "Origin", None),
		# Method 'Qualifiers_' returns object of type 'ISWbemQualifierSet'
		"Qualifiers_": (5, 2, (9, 0), (), "Qualifiers_", '{9B16ED16-D3DF-11D1-8B08-00600806D9B6}'),
		"Value": (0, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (12, 0), (), "Value", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ISWbemPropertySet(DispatchBaseClass):
	"""A collection of Properties"""
	CLSID = IID('{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}')
	coclass_clsid = IID('{04B83D5C-21AE-11D2-8B33-00600806D9B6}')

	# Result is of type ISWbemProperty
	def Add(self, strName=defaultNamedNotOptArg, iCimType=defaultNamedNotOptArg, bIsArray=False, iFlags=0):
		"""Add a Property to this collection"""
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1), (3, 1), (11, 49), (3, 49)),strName
			, iCimType, bIsArray, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
		return ret

	# Result is of type ISWbemProperty
	def Item(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Get a named Property from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strName
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
		return ret

	def Remove(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Remove a Property from this collection"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (3, 49)),strName
			, iFlags)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Get a named Property from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),strName
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemQualifier(DispatchBaseClass):
	"""A Qualifier"""
	CLSID = IID('{79B05932-D3B7-11D1-8B06-00600806D9B6}')
	coclass_clsid = IID('{04B83D5F-21AE-11D2-8B33-00600806D9B6}')

	_prop_map_get_ = {
		"IsAmended": (6, 2, (11, 0), (), "IsAmended", None),
		"IsLocal": (2, 2, (11, 0), (), "IsLocal", None),
		"IsOverridable": (5, 2, (11, 0), (), "IsOverridable", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"PropagatesToInstance": (4, 2, (11, 0), (), "PropagatesToInstance", None),
		"PropagatesToSubclass": (3, 2, (11, 0), (), "PropagatesToSubclass", None),
		"Value": (0, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"IsOverridable": ((5, LCID, 4, 0),()),
		"PropagatesToInstance": ((4, LCID, 4, 0),()),
		"PropagatesToSubclass": ((3, LCID, 4, 0),()),
		"Value": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (12, 0), (), "Value", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class ISWbemQualifierSet(DispatchBaseClass):
	"""A collection of Qualifiers"""
	CLSID = IID('{9B16ED16-D3DF-11D1-8B08-00600806D9B6}')
	coclass_clsid = IID('{04B83D5E-21AE-11D2-8B33-00600806D9B6}')

	# Result is of type ISWbemQualifier
	def Add(self, strName=defaultNamedNotOptArg, varVal=defaultNamedNotOptArg, bPropagatesToSubclass=True, bPropagatesToInstance=True
			, bIsOverridable=True, iFlags=0):
		"""Add a Qualifier to this collection"""
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((8, 1), (16396, 1), (11, 49), (11, 49), (11, 49), (3, 49)),strName
			, varVal, bPropagatesToSubclass, bPropagatesToInstance, bIsOverridable, iFlags
			)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{79B05932-D3B7-11D1-8B06-00600806D9B6}')
		return ret

	# Result is of type ISWbemQualifier
	def Item(self, Name=defaultNamedNotOptArg, iFlags=0):
		"""Get a named Qualifier from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),Name
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{79B05932-D3B7-11D1-8B06-00600806D9B6}')
		return ret

	def Remove(self, strName=defaultNamedNotOptArg, iFlags=0):
		"""Remove a Qualifier from this collection"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (3, 49)),strName
			, iFlags)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg, iFlags=0):
		"""Get a named Qualifier from this collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((8, 1), (3, 49)),Name
			, iFlags)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{79B05932-D3B7-11D1-8B06-00600806D9B6}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{79B05932-D3B7-11D1-8B06-00600806D9B6}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{79B05932-D3B7-11D1-8B06-00600806D9B6}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemRefreshableItem(DispatchBaseClass):
	"""A single item in a Refresher"""
	CLSID = IID('{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
	coclass_clsid = IID('{8C6854BC-DE4B-11D3-B390-00105A1F473A}')

	def Remove(self, iFlags=0):
		"""Remove this item from the parent refresher"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 49),),iFlags
			)

	_prop_map_get_ = {
		"Index": (1, 2, (3, 0), (), "Index", None),
		"IsSet": (3, 2, (11, 0), (), "IsSet", None),
		# Method 'Object' returns object of type 'ISWbemObjectEx'
		"Object": (4, 2, (9, 0), (), "Object", '{269AD56A-8A67-4129-BC8C-0506DCFE9880}'),
		# Method 'ObjectSet' returns object of type 'ISWbemObjectSet'
		"ObjectSet": (5, 2, (9, 0), (), "ObjectSet", '{76A6415F-CB41-11D1-8B02-00600806D9B6}'),
		# Method 'Refresher' returns object of type 'ISWbemRefresher'
		"Refresher": (2, 2, (9, 0), (), "Refresher", '{14D8250E-D9C2-11D3-B38F-00105A1F473A}'),
	}
	_prop_map_put_ = {
	}

class ISWbemRefresher(DispatchBaseClass):
	"""A Collection of Refreshable Objects"""
	CLSID = IID('{14D8250E-D9C2-11D3-B38F-00105A1F473A}')
	coclass_clsid = IID('{D269BF5C-D9C1-11D3-B38F-00105A1F473A}')

	# Result is of type ISWbemRefreshableItem
	def Add(self, objWbemServices=defaultNamedNotOptArg, bsInstancePath=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Add a refreshable instance to this refresher"""
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((9, 1), (8, 1), (3, 49), (9, 49)),objWbemServices
			, bsInstancePath, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
		return ret

	# Result is of type ISWbemRefreshableItem
	def AddEnum(self, objWbemServices=defaultNamedNotOptArg, bsClassName=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Add a refreshable enumerator to this refresher"""
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((9, 1), (8, 1), (3, 49), (9, 49)),objWbemServices
			, bsClassName, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'AddEnum', '{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
		return ret

	def DeleteAll(self):
		"""Delete all items in this collection"""
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	# Result is of type ISWbemRefreshableItem
	def Item(self, iIndex=defaultNamedNotOptArg):
		"""Get an item from this refresher"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),iIndex
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
		return ret

	def Refresh(self, iFlags=0):
		"""Refresh all items in this collection"""
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 49),),iFlags
			)

	def Remove(self, iIndex=defaultNamedNotOptArg, iFlags=0):
		"""Remove an item from this refresher"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((3, 1), (3, 49)),iIndex
			, iFlags)

	_prop_map_get_ = {
		"AutoReconnect": (6, 2, (11, 0), (), "AutoReconnect", None),
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
		"AutoReconnect": ((6, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, iIndex=defaultNamedNotOptArg):
		"""Get an item from this refresher"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),iIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISWbemSecurity(DispatchBaseClass):
	"""A Security Configurator"""
	CLSID = IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')
	coclass_clsid = IID('{B54D66E9-2287-11D2-8B33-00600806D9B6}')

	_prop_map_get_ = {
		"AuthenticationLevel": (2, 2, (3, 0), (), "AuthenticationLevel", None),
		"ImpersonationLevel": (1, 2, (3, 0), (), "ImpersonationLevel", None),
		# Method 'Privileges' returns object of type 'ISWbemPrivilegeSet'
		"Privileges": (3, 2, (9, 0), (), "Privileges", '{26EE67BF-5804-11D2-8B4A-00600806D9B6}'),
	}
	_prop_map_put_ = {
		"AuthenticationLevel": ((2, LCID, 4, 0),()),
		"ImpersonationLevel": ((1, LCID, 4, 0),()),
	}

class ISWbemServices(DispatchBaseClass):
	"""A connection to a Namespace"""
	CLSID = IID('{76A6415C-CB41-11D1-8B02-00600806D9B6}')
	coclass_clsid = IID('{04B83D63-21AE-11D2-8B33-00600806D9B6}')

	# Result is of type ISWbemObjectSet
	def AssociatorsOf(self, strObjectPath=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u'', strResultRole=u''
			, strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u''
			, iFlags=16, objWbemNamedValueSet=None):
		"""Get the Associators of a class or instance"""
		return self._ApplyTypes_(11, 1, (9, 32), ((8, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49)), u'AssociatorsOf', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strObjectPath
			, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly
			, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet
			)

	def AssociatorsOfAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u''
			, strResultRole=u'', strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u''
			, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the Associators of a class or instance asynchronously"""
		return self._ApplyTypes_(12, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'AssociatorsOfAsync', None,objWbemSink
			, strObjectPath, strAssocClass, strResultClass, strResultRole, strRole
			, bClassesOnly, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags
			, objWbemNamedValueSet, objWbemAsyncContext)

	def Delete(self, strObjectPath=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Delete a Class or Instance"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (3, 49), (9, 49)),strObjectPath
			, iFlags, objWbemNamedValueSet)

	def DeleteAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Delete a Class or Instance asynchronously"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1), (8, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strObjectPath, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObject
	def ExecMethod(self, strObjectPath=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0
			, objWbemNamedValueSet=None):
		"""Execute a Method"""
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((8, 1), (8, 1), (9, 49), (3, 49), (9, 49)),strObjectPath
			, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'ExecMethod', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def ExecMethodAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None
			, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute a Method asynchronously"""
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((9, 1), (8, 1), (8, 1), (9, 49), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strObjectPath, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet
			, objWbemAsyncContext)

	# Result is of type ISWbemEventSource
	def ExecNotificationQuery(self, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', iFlags=48, objWbemNamedValueSet=None):
		"""Execute a Query to receive Notifications"""
		return self._ApplyTypes_(15, 1, (9, 32), ((8, 1), (8, 49), (3, 49), (9, 49)), u'ExecNotificationQuery', '{27D54D92-0EBE-11D2-8B22-00600806D9B6}',strQuery
			, strQueryLanguage, iFlags, objWbemNamedValueSet)

	def ExecNotificationQueryAsync(self, objWbemSink=defaultNamedNotOptArg, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', iFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute an asynchronous Query to receive Notifications"""
		return self._ApplyTypes_(16, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'ExecNotificationQueryAsync', None,objWbemSink
			, strQuery, strQueryLanguage, iFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObjectSet
	def ExecQuery(self, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', iFlags=16, objWbemNamedValueSet=None):
		"""Execute a Query"""
		return self._ApplyTypes_(9, 1, (9, 32), ((8, 1), (8, 49), (3, 49), (9, 49)), u'ExecQuery', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strQuery
			, strQueryLanguage, iFlags, objWbemNamedValueSet)

	def ExecQueryAsync(self, objWbemSink=defaultNamedNotOptArg, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', lFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute an asynchronous Query"""
		return self._ApplyTypes_(10, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'ExecQueryAsync', None,objWbemSink
			, strQuery, strQueryLanguage, lFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObject
	def Get(self, strObjectPath=u'', iFlags=0, objWbemNamedValueSet=None):
		"""Get a single Class or Instance"""
		return self._ApplyTypes_(1, 1, (9, 32), ((8, 49), (3, 49), (9, 49)), u'Get', '{76A6415A-CB41-11D1-8B02-00600806D9B6}',strObjectPath
			, iFlags, objWbemNamedValueSet)

	def GetAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=u'', iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Get a single Class or Instance asynchronously"""
		return self._ApplyTypes_(2, 1, (24, 32), ((9, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'GetAsync', None,objWbemSink
			, strObjectPath, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def InstancesOf(self, strClass=defaultNamedNotOptArg, iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate the Instances of a Class"""
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((8, 1), (3, 49), (9, 49)),strClass
			, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'InstancesOf', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def InstancesOfAsync(self, objWbemSink=defaultNamedNotOptArg, strClass=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Enumerate the Instances of a Class asynchronously"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1), (8, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strClass, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def ReferencesTo(self, strObjectPath=defaultNamedNotOptArg, strResultClass=u'', strRole=u'', bClassesOnly=False
			, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Get the References to a class or instance"""
		return self._ApplyTypes_(13, 1, (9, 32), ((8, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49)), u'ReferencesTo', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strObjectPath
			, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier
			, iFlags, objWbemNamedValueSet)

	def ReferencesToAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, strResultClass=u'', strRole=u''
			, bClassesOnly=False, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Get the References to a class or instance asynchronously"""
		return self._ApplyTypes_(14, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'ReferencesToAsync', None,objWbemSink
			, strObjectPath, strResultClass, strRole, bClassesOnly, bSchemaOnly
			, strRequiredQualifier, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def SubclassesOf(self, strSuperclass=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate the subclasses of a Class"""
		return self._ApplyTypes_(7, 1, (9, 32), ((8, 49), (3, 49), (9, 49)), u'SubclassesOf', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strSuperclass
			, iFlags, objWbemNamedValueSet)

	def SubclassesOfAsync(self, objWbemSink=defaultNamedNotOptArg, strSuperclass=u'', iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Enumerate the subclasses of a Class asynchronously """
		return self._ApplyTypes_(8, 1, (24, 32), ((9, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'SubclassesOfAsync', None,objWbemSink
			, strSuperclass, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	_prop_map_get_ = {
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (19, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemServicesEx(DispatchBaseClass):
	"""A connection to a Namespace"""
	CLSID = IID('{D2F68443-85DC-427E-91D8-366554CC754C}')
	coclass_clsid = IID('{62E522DC-8CF3-40A8-8B2E-37D595651E40}')

	# Result is of type ISWbemObjectSet
	def AssociatorsOf(self, strObjectPath=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u'', strResultRole=u''
			, strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u'', strRequiredQualifier=u''
			, iFlags=16, objWbemNamedValueSet=None):
		"""Get the Associators of a class or instance"""
		return self._ApplyTypes_(11, 1, (9, 32), ((8, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49)), u'AssociatorsOf', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strObjectPath
			, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly
			, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet
			)

	def AssociatorsOfAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, strAssocClass=u'', strResultClass=u''
			, strResultRole=u'', strRole=u'', bClassesOnly=False, bSchemaOnly=False, strRequiredAssocQualifier=u''
			, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Get the Associators of a class or instance asynchronously"""
		return self._ApplyTypes_(12, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (8, 49), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'AssociatorsOfAsync', None,objWbemSink
			, strObjectPath, strAssocClass, strResultClass, strResultRole, strRole
			, bClassesOnly, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags
			, objWbemNamedValueSet, objWbemAsyncContext)

	def Delete(self, strObjectPath=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Delete a Class or Instance"""
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (3, 49), (9, 49)),strObjectPath
			, iFlags, objWbemNamedValueSet)

	def DeleteAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Delete a Class or Instance asynchronously"""
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1), (8, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strObjectPath, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObject
	def ExecMethod(self, strObjectPath=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None, iFlags=0
			, objWbemNamedValueSet=None):
		"""Execute a Method"""
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((8, 1), (8, 1), (9, 49), (3, 49), (9, 49)),strObjectPath
			, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'ExecMethod', '{76A6415A-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def ExecMethodAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, strMethodName=defaultNamedNotOptArg, objWbemInParameters=None
			, iFlags=0, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute a Method asynchronously"""
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((9, 1), (8, 1), (8, 1), (9, 49), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strObjectPath, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet
			, objWbemAsyncContext)

	# Result is of type ISWbemEventSource
	def ExecNotificationQuery(self, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', iFlags=48, objWbemNamedValueSet=None):
		"""Execute a Query to receive Notifications"""
		return self._ApplyTypes_(15, 1, (9, 32), ((8, 1), (8, 49), (3, 49), (9, 49)), u'ExecNotificationQuery', '{27D54D92-0EBE-11D2-8B22-00600806D9B6}',strQuery
			, strQueryLanguage, iFlags, objWbemNamedValueSet)

	def ExecNotificationQueryAsync(self, objWbemSink=defaultNamedNotOptArg, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', iFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute an asynchronous Query to receive Notifications"""
		return self._ApplyTypes_(16, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'ExecNotificationQueryAsync', None,objWbemSink
			, strQuery, strQueryLanguage, iFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObjectSet
	def ExecQuery(self, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', iFlags=16, objWbemNamedValueSet=None):
		"""Execute a Query"""
		return self._ApplyTypes_(9, 1, (9, 32), ((8, 1), (8, 49), (3, 49), (9, 49)), u'ExecQuery', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strQuery
			, strQueryLanguage, iFlags, objWbemNamedValueSet)

	def ExecQueryAsync(self, objWbemSink=defaultNamedNotOptArg, strQuery=defaultNamedNotOptArg, strQueryLanguage=u'WQL', lFlags=0
			, objWbemNamedValueSet=None, objWbemAsyncContext=None):
		"""Execute an asynchronous Query"""
		return self._ApplyTypes_(10, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'ExecQueryAsync', None,objWbemSink
			, strQuery, strQueryLanguage, lFlags, objWbemNamedValueSet, objWbemAsyncContext
			)

	# Result is of type ISWbemObject
	def Get(self, strObjectPath=u'', iFlags=0, objWbemNamedValueSet=None):
		"""Get a single Class or Instance"""
		return self._ApplyTypes_(1, 1, (9, 32), ((8, 49), (3, 49), (9, 49)), u'Get', '{76A6415A-CB41-11D1-8B02-00600806D9B6}',strObjectPath
			, iFlags, objWbemNamedValueSet)

	def GetAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=u'', iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Get a single Class or Instance asynchronously"""
		return self._ApplyTypes_(2, 1, (24, 32), ((9, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'GetAsync', None,objWbemSink
			, strObjectPath, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def InstancesOf(self, strClass=defaultNamedNotOptArg, iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate the Instances of a Class"""
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((8, 1), (3, 49), (9, 49)),strClass
			, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'InstancesOf', '{76A6415F-CB41-11D1-8B02-00600806D9B6}')
		return ret

	def InstancesOfAsync(self, objWbemSink=defaultNamedNotOptArg, strClass=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Enumerate the Instances of a Class asynchronously"""
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1), (8, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, strClass, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectPath
	def Put(self, objWbemObject=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None):
		"""Save the Object to this Namespace"""
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((9, 1), (3, 49), (9, 49)),objWbemObject
			, iFlags, objWbemNamedValueSet)
		if ret is not None:
			ret = Dispatch(ret, u'Put', '{5791BC27-CE9C-11D1-97BF-0000F81E849C}')
		return ret

	def PutAsync(self, objWbemSink=defaultNamedNotOptArg, objWbemObject=defaultNamedNotOptArg, iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Save the Object to this Namespace asynchronously"""
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((9, 1), (9, 1), (3, 49), (9, 49), (9, 49)),objWbemSink
			, objWbemObject, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def ReferencesTo(self, strObjectPath=defaultNamedNotOptArg, strResultClass=u'', strRole=u'', bClassesOnly=False
			, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Get the References to a class or instance"""
		return self._ApplyTypes_(13, 1, (9, 32), ((8, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49)), u'ReferencesTo', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strObjectPath
			, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier
			, iFlags, objWbemNamedValueSet)

	def ReferencesToAsync(self, objWbemSink=defaultNamedNotOptArg, strObjectPath=defaultNamedNotOptArg, strResultClass=u'', strRole=u''
			, bClassesOnly=False, bSchemaOnly=False, strRequiredQualifier=u'', iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Get the References to a class or instance asynchronously"""
		return self._ApplyTypes_(14, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (8, 49), (11, 49), (11, 49), (8, 49), (3, 49), (9, 49), (9, 49)), u'ReferencesToAsync', None,objWbemSink
			, strObjectPath, strResultClass, strRole, bClassesOnly, bSchemaOnly
			, strRequiredQualifier, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	# Result is of type ISWbemObjectSet
	def SubclassesOf(self, strSuperclass=u'', iFlags=16, objWbemNamedValueSet=None):
		"""Enumerate the subclasses of a Class"""
		return self._ApplyTypes_(7, 1, (9, 32), ((8, 49), (3, 49), (9, 49)), u'SubclassesOf', '{76A6415F-CB41-11D1-8B02-00600806D9B6}',strSuperclass
			, iFlags, objWbemNamedValueSet)

	def SubclassesOfAsync(self, objWbemSink=defaultNamedNotOptArg, strSuperclass=u'', iFlags=0, objWbemNamedValueSet=None
			, objWbemAsyncContext=None):
		"""Enumerate the subclasses of a Class asynchronously """
		return self._ApplyTypes_(8, 1, (24, 32), ((9, 1), (8, 49), (3, 49), (9, 49), (9, 49)), u'SubclassesOfAsync', None,objWbemSink
			, strSuperclass, iFlags, objWbemNamedValueSet, objWbemAsyncContext)

	_prop_map_get_ = {
		# Method 'Security_' returns object of type 'ISWbemSecurity'
		"Security_": (19, 2, (9, 0), (), "Security_", '{B54D66E6-2287-11D2-8B33-00600806D9B6}'),
	}
	_prop_map_put_ = {
	}

class ISWbemSink(DispatchBaseClass):
	"""Asynchronous operation control"""
	CLSID = IID('{75718C9F-F029-11D1-A1AC-00C04FB6C223}')
	coclass_clsid = IID('{75718C9A-F029-11D1-A1AC-00C04FB6C223}')

	def Cancel(self):
		"""Cancel an asynchronous operation"""
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class ISWbemSinkEvents:
	"""A sink for events arising from asynchronous operations"""
	CLSID = CLSID_Sink = IID('{75718CA0-F029-11D1-A1AC-00C04FB6C223}')
	coclass_clsid = IID('{75718C9A-F029-11D1-A1AC-00C04FB6C223}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        2 : "OnCompleted",
		        1 : "OnObjectReady",
		        3 : "OnProgress",
		        4 : "OnObjectPut",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnCompleted(self, iHResult=defaultNamedNotOptArg, objWbemErrorObject=defaultNamedNotOptArg, objWbemAsyncContext=defaultNamedNotOptArg):
#		"""Event triggered when an asynchronous operation is completed"""
#	def OnObjectReady(self, objWbemObject=defaultNamedNotOptArg, objWbemAsyncContext=defaultNamedNotOptArg):
#		"""Event triggered when an Object is available"""
#	def OnProgress(self, iUpperBound=defaultNamedNotOptArg, iCurrent=defaultNamedNotOptArg, strMessage=defaultNamedNotOptArg, objWbemAsyncContext=defaultNamedNotOptArg):
#		"""Event triggered to report the progress of an asynchronous operation"""
#	def OnObjectPut(self, objWbemObjectPath=defaultNamedNotOptArg, objWbemAsyncContext=defaultNamedNotOptArg):
#		"""Event triggered when an object path is available following a Put operation"""


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'WbemScripting.SWbemDateTime.1'
class SWbemDateTime(CoClassBaseClass): # A CoClass
	# Date & Time
	CLSID = IID('{47DFBE54-CF76-11D3-B38F-00105A1F473A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemDateTime,
	]
	default_interface = ISWbemDateTime

class SWbemEventSource(CoClassBaseClass): # A CoClass
	# An Event source
	CLSID = IID('{04B83D58-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemEventSource,
	]
	default_interface = ISWbemEventSource

# This CoClass is known by the name 'WbemScripting.SWbemLastError.1'
class SWbemLastError(CoClassBaseClass): # A CoClass
	# The last error on the current thread
	CLSID = IID('{C2FEEEAC-CFCD-11D1-8B05-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemLastError,
	]
	default_interface = ISWbemLastError

# This CoClass is known by the name 'WbemScripting.SWbemLocator.1'
class SWbemLocator(CoClassBaseClass): # A CoClass
	# Used to obtain Namespace connections
	CLSID = IID('{76A64158-CB41-11D1-8B02-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemLocator,
	]
	default_interface = ISWbemLocator

class SWbemMethod(CoClassBaseClass): # A CoClass
	# A Method
	CLSID = IID('{04B83D5B-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemMethod,
	]
	default_interface = ISWbemMethod

class SWbemMethodSet(CoClassBaseClass): # A CoClass
	# A collection of Methods
	CLSID = IID('{04B83D5A-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemMethodSet,
	]
	default_interface = ISWbemMethodSet

class SWbemNamedValue(CoClassBaseClass): # A CoClass
	# A named value
	CLSID = IID('{04B83D60-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemNamedValue,
	]
	default_interface = ISWbemNamedValue

# This CoClass is known by the name 'WbemScripting.SWbemNamedValueSet.1'
class SWbemNamedValueSet(CoClassBaseClass): # A CoClass
	# A collection of Named Values
	CLSID = IID('{9AED384E-CE8B-11D1-8B05-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemNamedValueSet,
	]
	default_interface = ISWbemNamedValueSet

class SWbemObject(CoClassBaseClass): # A CoClass
	# A Class or Instance
	CLSID = IID('{04B83D62-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemObject,
	]
	default_interface = ISWbemObject

class SWbemObjectEx(CoClassBaseClass): # A CoClass
	# A Class or Instance
	CLSID = IID('{D6BDAFB2-9435-491F-BB87-6AA0F0BC31A2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemObjectEx,
	]
	default_interface = ISWbemObjectEx

# This CoClass is known by the name 'WbemScripting.SWbemObjectPath.1'
class SWbemObjectPath(CoClassBaseClass): # A CoClass
	# Object Path
	CLSID = IID('{5791BC26-CE9C-11D1-97BF-0000F81E849C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemObjectPath,
	]
	default_interface = ISWbemObjectPath

class SWbemObjectSet(CoClassBaseClass): # A CoClass
	# A collection of Classes or Instances
	CLSID = IID('{04B83D61-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemObjectSet,
	]
	default_interface = ISWbemObjectSet

class SWbemPrivilege(CoClassBaseClass): # A CoClass
	# A Privilege Override
	CLSID = IID('{26EE67BC-5804-11D2-8B4A-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemPrivilege,
	]
	default_interface = ISWbemPrivilege

class SWbemPrivilegeSet(CoClassBaseClass): # A CoClass
	# A collection of Privilege Overrides
	CLSID = IID('{26EE67BE-5804-11D2-8B4A-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemPrivilegeSet,
	]
	default_interface = ISWbemPrivilegeSet

class SWbemProperty(CoClassBaseClass): # A CoClass
	# A Property
	CLSID = IID('{04B83D5D-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemProperty,
	]
	default_interface = ISWbemProperty

class SWbemPropertySet(CoClassBaseClass): # A CoClass
	# A collection of Properties
	CLSID = IID('{04B83D5C-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemPropertySet,
	]
	default_interface = ISWbemPropertySet

class SWbemQualifier(CoClassBaseClass): # A CoClass
	# A Qualifier
	CLSID = IID('{04B83D5F-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemQualifier,
	]
	default_interface = ISWbemQualifier

class SWbemQualifierSet(CoClassBaseClass): # A CoClass
	# A collection of Qualifiers
	CLSID = IID('{04B83D5E-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemQualifierSet,
	]
	default_interface = ISWbemQualifierSet

class SWbemRefreshableItem(CoClassBaseClass): # A CoClass
	# A single item from a Refresher
	CLSID = IID('{8C6854BC-DE4B-11D3-B390-00105A1F473A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemRefreshableItem,
	]
	default_interface = ISWbemRefreshableItem

# This CoClass is known by the name 'WbemScripting.SWbemRefresher.1'
class SWbemRefresher(CoClassBaseClass): # A CoClass
	# Refresher
	CLSID = IID('{D269BF5C-D9C1-11D3-B38F-00105A1F473A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemRefresher,
	]
	default_interface = ISWbemRefresher

class SWbemSecurity(CoClassBaseClass): # A CoClass
	# A Security Configurator
	CLSID = IID('{B54D66E9-2287-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemSecurity,
	]
	default_interface = ISWbemSecurity

class SWbemServices(CoClassBaseClass): # A CoClass
	# A connection to a Namespace
	CLSID = IID('{04B83D63-21AE-11D2-8B33-00600806D9B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemServices,
	]
	default_interface = ISWbemServices

class SWbemServicesEx(CoClassBaseClass): # A CoClass
	# A connection to a Namespace
	CLSID = IID('{62E522DC-8CF3-40A8-8B2E-37D595651E40}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISWbemServicesEx,
	]
	default_interface = ISWbemServicesEx

# This CoClass is known by the name 'WbemScripting.SWbemSink.1'
class SWbemSink(CoClassBaseClass): # A CoClass
	# A sink for events arising from asynchronous operations
	CLSID = IID('{75718C9A-F029-11D1-A1AC-00C04FB6C223}')
	coclass_sources = [
		ISWbemSinkEvents,
	]
	default_source = ISWbemSinkEvents
	coclass_interfaces = [
		ISWbemSink,
	]
	default_interface = ISWbemSink

ISWbemDateTime_vtables_dispatch_ = 1
ISWbemDateTime_vtables_ = [
	(( u'Value' , u'strValue' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'strValue' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Year' , u'iYear' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Year' , u'iYear' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'YearSpecified' , u'bYearSpecified' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'YearSpecified' , u'bYearSpecified' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Month' , u'iMonth' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Month' , u'iMonth' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'MonthSpecified' , u'bMonthSpecified' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'MonthSpecified' , u'bMonthSpecified' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Day' , u'iDay' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Day' , u'iDay' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'DaySpecified' , u'bDaySpecified' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'DaySpecified' , u'bDaySpecified' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Hours' , u'iHours' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Hours' , u'iHours' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'HoursSpecified' , u'bHoursSpecified' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'HoursSpecified' , u'bHoursSpecified' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Minutes' , u'iMinutes' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Minutes' , u'iMinutes' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'MinutesSpecified' , u'bMinutesSpecified' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'MinutesSpecified' , u'bMinutesSpecified' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Seconds' , u'iSeconds' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Seconds' , u'iSeconds' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'SecondsSpecified' , u'bSecondsSpecified' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'SecondsSpecified' , u'bSecondsSpecified' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Microseconds' , u'iMicroseconds' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'Microseconds' , u'iMicroseconds' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'MicrosecondsSpecified' , u'bMicrosecondsSpecified' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'MicrosecondsSpecified' , u'bMicrosecondsSpecified' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'UTC' , u'iUTC' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'UTC' , u'iUTC' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'UTCSpecified' , u'bUTCSpecified' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'UTCSpecified' , u'bUTCSpecified' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'IsInterval' , u'bIsInterval' , ), 17, (17, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'IsInterval' , u'bIsInterval' , ), 17, (17, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetVarDate' , u'bIsLocal' , u'dVarDate' , ), 18, (18, (), [ (11, 49, 'True', None) , 
			(16391, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'SetVarDate' , u'dVarDate' , u'bIsLocal' , ), 19, (19, (), [ (7, 1, None, None) , 
			(11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'GetFileTime' , u'bIsLocal' , u'strFileTime' , ), 20, (20, (), [ (11, 49, 'True', None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'SetFileTime' , u'strFileTime' , u'bIsLocal' , ), 21, (21, (), [ (8, 1, None, None) , 
			(11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

ISWbemEventSource_vtables_dispatch_ = 1
ISWbemEventSource_vtables_ = [
	(( u'NextEvent' , u'iTimeoutMs' , u'objWbemObject' , ), 1, (1, (), [ (3, 49, '-1', None) , 
			(16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Security_' , u'objWbemSecurity' , ), 2, (2, (), [ (16393, 10, None, "IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISWbemLastError_vtables_dispatch_ = 1
ISWbemLastError_vtables_ = [
]

ISWbemLocator_vtables_dispatch_ = 1
ISWbemLocator_vtables_ = [
	(( u'ConnectServer' , u'strServer' , u'strNamespace' , u'strUser' , u'strPassword' , 
			u'strLocale' , u'strAuthority' , u'iSecurityFlags' , u'objWbemNamedValueSet' , u'objWbemServices' , 
			), 1, (1, (), [ (8, 49, "u'.'", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (3, 49, '0', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415C-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 28 , (3, 32, None, None) , 0 , )),
	(( u'Security_' , u'objWbemSecurity' , ), 2, (2, (), [ (16393, 10, None, "IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISWbemMethod_vtables_dispatch_ = 1
ISWbemMethod_vtables_ = [
	(( u'Name' , u'strName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Origin' , u'strOrigin' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'InParameters' , u'objWbemInParameters' , ), 3, (3, (), [ (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'OutParameters' , u'objWbemOutParameters' , ), 4, (4, (), [ (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Qualifiers_' , u'objWbemQualifierSet' , ), 5, (5, (), [ (16393, 10, None, "IID('{9B16ED16-D3DF-11D1-8B08-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ISWbemMethodSet_vtables_dispatch_ = 1
ISWbemMethodSet_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'strName' , u'iFlags' , u'objWbemMethod' , ), 0, (0, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{422E8E90-D955-11D1-8B09-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ISWbemNamedValue_vtables_dispatch_ = 1
ISWbemNamedValue_vtables_ = [
	(( u'Value' , u'varValue' , ), 0, (0, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'varValue' , ), 0, (0, (), [ (16396, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'strName' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

ISWbemNamedValueSet_vtables_dispatch_ = 1
ISWbemNamedValueSet_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'strName' , u'iFlags' , u'objWbemNamedValue' , ), 0, (0, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{76A64164-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'strName' , u'varValue' , u'iFlags' , u'objWbemNamedValue' , 
			), 2, (2, (), [ (8, 1, None, None) , (16396, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{76A64164-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'strName' , u'iFlags' , ), 3, (3, (), [ (8, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Clone' , u'objWbemNamedValueSet' , ), 4, (4, (), [ (16393, 10, None, "IID('{CF2376EA-CE8C-11D1-8B05-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAll' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

ISWbemObject_vtables_dispatch_ = 1
ISWbemObject_vtables_ = [
	(( u'Put_' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectPath' , ), 1, (1, (), [ 
			(3, 49, '0', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{5791BC27-CE9C-11D1-97BF-0000F81E849C}')") , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'PutAsync_' , u'objWbemSink' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , 
			), 2, (2, (), [ (9, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Delete_' , u'iFlags' , u'objWbemNamedValueSet' , ), 3, (3, (), [ (3, 49, '0', None) , 
			(9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAsync_' , u'objWbemSink' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , 
			), 4, (4, (), [ (9, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Instances_' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , ), 5, (5, (), [ 
			(3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'InstancesAsync_' , u'objWbemSink' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , 
			), 6, (6, (), [ (9, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Subclasses_' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , ), 7, (7, (), [ 
			(3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'SubclassesAsync_' , u'objWbemSink' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , 
			), 8, (8, (), [ (9, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Associators_' , u'strAssocClass' , u'strResultClass' , u'strResultRole' , u'strRole' , 
			u'bClassesOnly' , u'bSchemaOnly' , u'strRequiredAssocQualifier' , u'strRequiredQualifier' , u'iFlags' , 
			u'objWbemNamedValueSet' , u'objWbemObjectSet' , ), 9, (9, (), [ (8, 49, "u''", None) , (8, 49, "u''", None) , 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , (11, 49, 'False', None) , (8, 49, "u''", None) , 
			(8, 49, "u''", None) , (3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 32, None, None) , 0 , )),
	(( u'AssociatorsAsync_' , u'objWbemSink' , u'strAssocClass' , u'strResultClass' , u'strResultRole' , 
			u'strRole' , u'bClassesOnly' , u'bSchemaOnly' , u'strRequiredAssocQualifier' , u'strRequiredQualifier' , 
			u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , ), 10, (10, (), [ (9, 1, None, None) , 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , 
			(11, 49, 'False', None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (3, 49, '0', None) , (9, 49, 'None', None) , 
			(9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 64 , (3, 32, None, None) , 0 , )),
	(( u'References_' , u'strResultClass' , u'strRole' , u'bClassesOnly' , u'bSchemaOnly' , 
			u'strRequiredQualifier' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , ), 11, (11, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , (11, 49, 'False', None) , (8, 49, "u''", None) , 
			(3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 32, None, None) , 0 , )),
	(( u'ReferencesAsync_' , u'objWbemSink' , u'strResultClass' , u'strRole' , u'bClassesOnly' , 
			u'bSchemaOnly' , u'strRequiredQualifier' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , 
			), 12, (12, (), [ (9, 1, None, None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , 
			(11, 49, 'False', None) , (8, 49, "u''", None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 32, None, None) , 0 , )),
	(( u'ExecMethod_' , u'strMethodName' , u'objWbemInParameters' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemOutParameters' , ), 13, (13, (), [ (8, 1, None, None) , (9, 49, 'None', None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'ExecMethodAsync_' , u'objWbemSink' , u'strMethodName' , u'objWbemInParameters' , u'iFlags' , 
			u'objWbemNamedValueSet' , u'objWbemAsyncContext' , ), 14, (14, (), [ (9, 1, None, None) , (8, 1, None, None) , 
			(9, 49, 'None', None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Clone_' , u'objWbemObject' , ), 15, (15, (), [ (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetObjectText_' , u'iFlags' , u'strObjectText' , ), 16, (16, (), [ (3, 49, '0', None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SpawnDerivedClass_' , u'iFlags' , u'objWbemObject' , ), 17, (17, (), [ (3, 49, '0', None) , 
			(16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'SpawnInstance_' , u'iFlags' , u'objWbemObject' , ), 18, (18, (), [ (3, 49, '0', None) , 
			(16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'CompareTo_' , u'objWbemObject' , u'iFlags' , u'bResult' , ), 19, (19, (), [ 
			(9, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Qualifiers_' , u'objWbemQualifierSet' , ), 20, (20, (), [ (16393, 10, None, "IID('{9B16ED16-D3DF-11D1-8B08-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Properties_' , u'objWbemPropertySet' , ), 21, (21, (), [ (16393, 10, None, "IID('{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Methods_' , u'objWbemMethodSet' , ), 22, (22, (), [ (16393, 10, None, "IID('{C93BA292-D955-11D1-8B09-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Derivation_' , u'strClassNameArray' , ), 23, (23, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Path_' , u'objWbemObjectPath' , ), 24, (24, (), [ (16393, 10, None, "IID('{5791BC27-CE9C-11D1-97BF-0000F81E849C}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Security_' , u'objWbemSecurity' , ), 25, (25, (), [ (16393, 10, None, "IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
]

ISWbemObjectEx_vtables_dispatch_ = 1
ISWbemObjectEx_vtables_ = [
	(( u'Refresh_' , u'iFlags' , u'objWbemNamedValueSet' , ), 26, (26, (), [ (3, 49, '0', None) , 
			(9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'SystemProperties_' , u'objWbemPropertySet' , ), 27, (27, (), [ (16393, 10, None, "IID('{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'GetText_' , u'iObjectTextFormat' , u'iFlags' , u'objWbemNamedValueSet' , u'bsText' , 
			), 28, (28, (), [ (3, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SetFromText_' , u'bsText' , u'iObjectTextFormat' , u'iFlags' , u'objWbemNamedValueSet' , 
			), 29, (29, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
]

ISWbemObjectPath_vtables_dispatch_ = 1
ISWbemObjectPath_vtables_ = [
	(( u'Path' , u'strPath' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Path' , u'strPath' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'RelPath' , u'strRelPath' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'RelPath' , u'strRelPath' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Server' , u'strServer' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Server' , u'strServer' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Namespace' , u'strNamespace' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Namespace' , u'strNamespace' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ParentNamespace' , u'strParentNamespace' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'DisplayName' , u'strDisplayName' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'DisplayName' , u'strDisplayName' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Class' , u'strClass' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Class' , u'strClass' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'IsClass' , u'bIsClass' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SetAsClass' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'IsSingleton' , u'bIsSingleton' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetAsSingleton' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Keys' , u'objWbemNamedValueSet' , ), 11, (11, (), [ (16393, 10, None, "IID('{CF2376EA-CE8C-11D1-8B05-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Security_' , u'objWbemSecurity' , ), 12, (12, (), [ (16393, 10, None, "IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Locale' , u'strLocale' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Locale' , u'strLocale' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Authority' , u'strAuthority' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Authority' , u'strAuthority' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
]

ISWbemObjectSet_vtables_dispatch_ = 1
ISWbemObjectSet_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'strObjectPath' , u'iFlags' , u'objWbemObject' , ), 0, (0, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Security_' , u'objWbemSecurity' , ), 4, (4, (), [ (16393, 10, None, "IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ISWbemPrivilege_vtables_dispatch_ = 1
ISWbemPrivilege_vtables_ = [
	(( u'IsEnabled' , u'bIsEnabled' , ), 0, (0, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'IsEnabled' , u'bIsEnabled' , ), 0, (0, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'strDisplayName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'DisplayName' , u'strDisplayName' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Identifier' , u'iPrivilege' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ISWbemPrivilegeSet_vtables_dispatch_ = 1
ISWbemPrivilegeSet_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'iPrivilege' , u'objWbemPrivilege' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{26EE67BD-5804-11D2-8B4A-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'iPrivilege' , u'bIsEnabled' , u'objWbemPrivilege' , ), 2, (2, (), [ 
			(3, 1, None, None) , (11, 49, 'True', None) , (16393, 10, None, "IID('{26EE67BD-5804-11D2-8B4A-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'iPrivilege' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAll' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'AddAsString' , u'strPrivilege' , u'bIsEnabled' , u'objWbemPrivilege' , ), 5, (5, (), [ 
			(8, 1, None, None) , (11, 49, 'True', None) , (16393, 10, None, "IID('{26EE67BD-5804-11D2-8B4A-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

ISWbemProperty_vtables_dispatch_ = 1
ISWbemProperty_vtables_ = [
	(( u'Value' , u'varValue' , ), 0, (0, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'varValue' , ), 0, (0, (), [ (16396, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'strName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'IsLocal' , u'bIsLocal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Origin' , u'strOrigin' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'CIMType' , u'iCimType' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Qualifiers_' , u'objWbemQualifierSet' , ), 5, (5, (), [ (16393, 10, None, "IID('{9B16ED16-D3DF-11D1-8B08-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'IsArray' , u'bIsArray' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

ISWbemPropertySet_vtables_dispatch_ = 1
ISWbemPropertySet_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'strName' , u'iFlags' , u'objWbemProperty' , ), 0, (0, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{1A388F98-D4BA-11D1-8B09-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'strName' , u'iCimType' , u'bIsArray' , u'iFlags' , 
			u'objWbemProperty' , ), 2, (2, (), [ (8, 1, None, None) , (3, 1, None, None) , (11, 49, 'False', None) , 
			(3, 49, '0', None) , (16393, 10, None, "IID('{1A388F98-D4BA-11D1-8B09-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'strName' , u'iFlags' , ), 3, (3, (), [ (8, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ISWbemQualifier_vtables_dispatch_ = 1
ISWbemQualifier_vtables_ = [
	(( u'Value' , u'varValue' , ), 0, (0, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'varValue' , ), 0, (0, (), [ (16396, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'strName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'IsLocal' , u'bIsLocal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'PropagatesToSubclass' , u'bPropagatesToSubclass' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'PropagatesToSubclass' , u'bPropagatesToSubclass' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'PropagatesToInstance' , u'bPropagatesToInstance' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'PropagatesToInstance' , u'bPropagatesToInstance' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'IsOverridable' , u'bIsOverridable' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'IsOverridable' , u'bIsOverridable' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'IsAmended' , u'bIsAmended' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
]

ISWbemQualifierSet_vtables_dispatch_ = 1
ISWbemQualifierSet_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'Name' , u'iFlags' , u'objWbemQualifier' , ), 0, (0, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{79B05932-D3B7-11D1-8B06-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'strName' , u'varVal' , u'bPropagatesToSubclass' , u'bPropagatesToInstance' , 
			u'bIsOverridable' , u'iFlags' , u'objWbemQualifier' , ), 2, (2, (), [ (8, 1, None, None) , 
			(16396, 1, None, None) , (11, 49, 'True', None) , (11, 49, 'True', None) , (11, 49, 'True', None) , (3, 49, '0', None) , 
			(16393, 10, None, "IID('{79B05932-D3B7-11D1-8B06-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'strName' , u'iFlags' , ), 3, (3, (), [ (8, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ISWbemRefreshableItem_vtables_dispatch_ = 1
ISWbemRefreshableItem_vtables_ = [
	(( u'Index' , u'iIndex' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Refresher' , u'objWbemRefresher' , ), 2, (2, (), [ (16393, 10, None, "IID('{14D8250E-D9C2-11D3-B38F-00105A1F473A}')") , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'IsSet' , u'bIsSet' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Object' , u'objWbemObject' , ), 4, (4, (), [ (16393, 10, None, "IID('{269AD56A-8A67-4129-BC8C-0506DCFE9880}')") , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ObjectSet' , u'objWbemObjectSet' , ), 5, (5, (), [ (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'iFlags' , ), 6, (6, (), [ (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ISWbemRefresher_vtables_dispatch_ = 1
ISWbemRefresher_vtables_ = [
	(( u'_NewEnum' , u'pUnk' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 1 , )),
	(( u'Item' , u'iIndex' , u'objWbemRefreshableItem' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'iCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'objWbemServices' , u'bsInstancePath' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemRefreshableItem' , ), 2, (2, (), [ (9, 1, None, "IID('{D2F68443-85DC-427E-91D8-366554CC754C}')") , (8, 1, None, None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (16393, 10, None, "IID('{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'AddEnum' , u'objWbemServices' , u'bsClassName' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemRefreshableItem' , ), 3, (3, (), [ (9, 1, None, "IID('{D2F68443-85DC-427E-91D8-366554CC754C}')") , (8, 1, None, None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (16393, 10, None, "IID('{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'iIndex' , u'iFlags' , ), 4, (4, (), [ (3, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Refresh' , u'iFlags' , ), 5, (5, (), [ (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'AutoReconnect' , u'bCount' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AutoReconnect' , u'bCount' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAll' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISWbemSecurity_vtables_dispatch_ = 1
ISWbemSecurity_vtables_ = [
	(( u'ImpersonationLevel' , u'iImpersonationLevel' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ImpersonationLevel' , u'iImpersonationLevel' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'AuthenticationLevel' , u'iAuthenticationLevel' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'AuthenticationLevel' , u'iAuthenticationLevel' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Privileges' , u'objWbemPrivilegeSet' , ), 3, (3, (), [ (16393, 10, None, "IID('{26EE67BF-5804-11D2-8B4A-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
]

ISWbemServices_vtables_dispatch_ = 1
ISWbemServices_vtables_ = [
	(( u'Get' , u'strObjectPath' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObject' , 
			), 1, (1, (), [ (8, 49, "u''", None) , (3, 49, '0', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 28 , (3, 32, None, None) , 0 , )),
	(( u'GetAsync' , u'objWbemSink' , u'strObjectPath' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemAsyncContext' , ), 2, (2, (), [ (9, 1, None, None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 32 , (3, 32, None, None) , 0 , )),
	(( u'Delete' , u'strObjectPath' , u'iFlags' , u'objWbemNamedValueSet' , ), 3, (3, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAsync' , u'objWbemSink' , u'strObjectPath' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemAsyncContext' , ), 4, (4, (), [ (9, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'InstancesOf' , u'strClass' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , 
			), 5, (5, (), [ (8, 1, None, None) , (3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'InstancesOfAsync' , u'objWbemSink' , u'strClass' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemAsyncContext' , ), 6, (6, (), [ (9, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SubclassesOf' , u'strSuperclass' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , 
			), 7, (7, (), [ (8, 49, "u''", None) , (3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 32, None, None) , 0 , )),
	(( u'SubclassesOfAsync' , u'objWbemSink' , u'strSuperclass' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemAsyncContext' , ), 8, (8, (), [ (9, 1, None, None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 56 , (3, 32, None, None) , 0 , )),
	(( u'ExecQuery' , u'strQuery' , u'strQueryLanguage' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemObjectSet' , ), 9, (9, (), [ (8, 1, None, None) , (8, 49, "u'WQL'", None) , (3, 49, '16', None) , 
			(9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 32, None, None) , 0 , )),
	(( u'ExecQueryAsync' , u'objWbemSink' , u'strQuery' , u'strQueryLanguage' , u'lFlags' , 
			u'objWbemNamedValueSet' , u'objWbemAsyncContext' , ), 10, (10, (), [ (9, 1, None, None) , (8, 1, None, None) , 
			(8, 49, "u'WQL'", None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 64 , (3, 32, None, None) , 0 , )),
	(( u'AssociatorsOf' , u'strObjectPath' , u'strAssocClass' , u'strResultClass' , u'strResultRole' , 
			u'strRole' , u'bClassesOnly' , u'bSchemaOnly' , u'strRequiredAssocQualifier' , u'strRequiredQualifier' , 
			u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , ), 11, (11, (), [ (8, 1, None, None) , 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , 
			(11, 49, 'False', None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (3, 49, '16', None) , (9, 49, 'None', None) , 
			(16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 68 , (3, 32, None, None) , 0 , )),
	(( u'AssociatorsOfAsync' , u'objWbemSink' , u'strObjectPath' , u'strAssocClass' , u'strResultClass' , 
			u'strResultRole' , u'strRole' , u'bClassesOnly' , u'bSchemaOnly' , u'strRequiredAssocQualifier' , 
			u'strRequiredQualifier' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , ), 12, (12, (), [ 
			(9, 1, None, None) , (8, 1, None, None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (8, 49, "u''", None) , 
			(8, 49, "u''", None) , (11, 49, 'False', None) , (11, 49, 'False', None) , (8, 49, "u''", None) , (8, 49, "u''", None) , 
			(3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 32, None, None) , 0 , )),
	(( u'ReferencesTo' , u'strObjectPath' , u'strResultClass' , u'strRole' , u'bClassesOnly' , 
			u'bSchemaOnly' , u'strRequiredQualifier' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectSet' , 
			), 13, (13, (), [ (8, 1, None, None) , (8, 49, "u''", None) , (8, 49, "u''", None) , (11, 49, 'False', None) , 
			(11, 49, 'False', None) , (8, 49, "u''", None) , (3, 49, '16', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 76 , (3, 32, None, None) , 0 , )),
	(( u'ReferencesToAsync' , u'objWbemSink' , u'strObjectPath' , u'strResultClass' , u'strRole' , 
			u'bClassesOnly' , u'bSchemaOnly' , u'strRequiredQualifier' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemAsyncContext' , ), 14, (14, (), [ (9, 1, None, None) , (8, 1, None, None) , (8, 49, "u''", None) , 
			(8, 49, "u''", None) , (11, 49, 'False', None) , (11, 49, 'False', None) , (8, 49, "u''", None) , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 32, None, None) , 0 , )),
	(( u'ExecNotificationQuery' , u'strQuery' , u'strQueryLanguage' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemEventSource' , ), 15, (15, (), [ (8, 1, None, None) , (8, 49, "u'WQL'", None) , (3, 49, '48', None) , 
			(9, 49, 'None', None) , (16393, 10, None, "IID('{27D54D92-0EBE-11D2-8B22-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 84 , (3, 32, None, None) , 0 , )),
	(( u'ExecNotificationQueryAsync' , u'objWbemSink' , u'strQuery' , u'strQueryLanguage' , u'iFlags' , 
			u'objWbemNamedValueSet' , u'objWbemAsyncContext' , ), 16, (16, (), [ (9, 1, None, None) , (8, 1, None, None) , 
			(8, 49, "u'WQL'", None) , (3, 49, '0', None) , (9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 32, None, None) , 0 , )),
	(( u'ExecMethod' , u'strObjectPath' , u'strMethodName' , u'objWbemInParameters' , u'iFlags' , 
			u'objWbemNamedValueSet' , u'objWbemOutParameters' , ), 17, (17, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			(9, 49, 'None', None) , (3, 49, '0', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')") , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'ExecMethodAsync' , u'objWbemSink' , u'strObjectPath' , u'strMethodName' , u'objWbemInParameters' , 
			u'iFlags' , u'objWbemNamedValueSet' , u'objWbemAsyncContext' , ), 18, (18, (), [ (9, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (9, 49, 'None', None) , (3, 49, '0', None) , (9, 49, 'None', None) , 
			(9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Security_' , u'objWbemSecurity' , ), 19, (19, (), [ (16393, 10, None, "IID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')") , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

ISWbemServicesEx_vtables_dispatch_ = 1
ISWbemServicesEx_vtables_ = [
	(( u'Put' , u'objWbemObject' , u'iFlags' , u'objWbemNamedValueSet' , u'objWbemObjectPath' , 
			), 20, (20, (), [ (9, 1, None, "IID('{269AD56A-8A67-4129-BC8C-0506DCFE9880}')") , (3, 49, '0', None) , (9, 49, 'None', None) , (16393, 10, None, "IID('{5791BC27-CE9C-11D1-97BF-0000F81E849C}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'PutAsync' , u'objWbemSink' , u'objWbemObject' , u'iFlags' , u'objWbemNamedValueSet' , 
			u'objWbemAsyncContext' , ), 21, (21, (), [ (9, 1, None, "IID('{75718C9F-F029-11D1-A1AC-00C04FB6C223}')") , (9, 1, None, "IID('{269AD56A-8A67-4129-BC8C-0506DCFE9880}')") , (3, 49, '0', None) , 
			(9, 49, 'None', None) , (9, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
]

ISWbemSink_vtables_dispatch_ = 1
ISWbemSink_vtables_ = [
	(( u'Cancel' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{B54D66E6-2287-11D2-8B33-00600806D9B6}' : ISWbemSecurity,
	'{B54D66E9-2287-11D2-8B33-00600806D9B6}' : SWbemSecurity,
	'{D2F68443-85DC-427E-91D8-366554CC754C}' : ISWbemServicesEx,
	'{9B16ED16-D3DF-11D1-8B08-00600806D9B6}' : ISWbemQualifierSet,
	'{CF2376EA-CE8C-11D1-8B05-00600806D9B6}' : ISWbemNamedValueSet,
	'{C2FEEEAC-CFCD-11D1-8B05-00600806D9B6}' : SWbemLastError,
	'{5E97458A-CF77-11D3-B38F-00105A1F473A}' : ISWbemDateTime,
	'{D6BDAFB2-9435-491F-BB87-6AA0F0BC31A2}' : SWbemObjectEx,
	'{8C6854BC-DE4B-11D3-B390-00105A1F473A}' : SWbemRefreshableItem,
	'{04B83D58-21AE-11D2-8B33-00600806D9B6}' : SWbemEventSource,
	'{04B83D5A-21AE-11D2-8B33-00600806D9B6}' : SWbemMethodSet,
	'{04B83D5B-21AE-11D2-8B33-00600806D9B6}' : SWbemMethod,
	'{04B83D5C-21AE-11D2-8B33-00600806D9B6}' : SWbemPropertySet,
	'{04B83D5D-21AE-11D2-8B33-00600806D9B6}' : SWbemProperty,
	'{04B83D5E-21AE-11D2-8B33-00600806D9B6}' : SWbemQualifierSet,
	'{04B83D5F-21AE-11D2-8B33-00600806D9B6}' : SWbemQualifier,
	'{04B83D60-21AE-11D2-8B33-00600806D9B6}' : SWbemNamedValue,
	'{04B83D61-21AE-11D2-8B33-00600806D9B6}' : SWbemObjectSet,
	'{04B83D62-21AE-11D2-8B33-00600806D9B6}' : SWbemObject,
	'{04B83D63-21AE-11D2-8B33-00600806D9B6}' : SWbemServices,
	'{D269BF5C-D9C1-11D3-B38F-00105A1F473A}' : SWbemRefresher,
	'{76A64158-CB41-11D1-8B02-00600806D9B6}' : SWbemLocator,
	'{76A6415A-CB41-11D1-8B02-00600806D9B6}' : ISWbemObject,
	'{76A6415B-CB41-11D1-8B02-00600806D9B6}' : ISWbemLocator,
	'{76A6415C-CB41-11D1-8B02-00600806D9B6}' : ISWbemServices,
	'{76A6415F-CB41-11D1-8B02-00600806D9B6}' : ISWbemObjectSet,
	'{75718C9F-F029-11D1-A1AC-00C04FB6C223}' : ISWbemSink,
	'{75718CA0-F029-11D1-A1AC-00C04FB6C223}' : ISWbemSinkEvents,
	'{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}' : ISWbemRefreshableItem,
	'{76A64164-CB41-11D1-8B02-00600806D9B6}' : ISWbemNamedValue,
	'{D962DB84-D4BB-11D1-8B09-00600806D9B6}' : ISWbemLastError,
	'{26EE67BC-5804-11D2-8B4A-00600806D9B6}' : SWbemPrivilege,
	'{26EE67BD-5804-11D2-8B4A-00600806D9B6}' : ISWbemPrivilege,
	'{26EE67BE-5804-11D2-8B4A-00600806D9B6}' : SWbemPrivilegeSet,
	'{26EE67BF-5804-11D2-8B4A-00600806D9B6}' : ISWbemPrivilegeSet,
	'{47DFBE54-CF76-11D3-B38F-00105A1F473A}' : SWbemDateTime,
	'{14D8250E-D9C2-11D3-B38F-00105A1F473A}' : ISWbemRefresher,
	'{27D54D92-0EBE-11D2-8B22-00600806D9B6}' : ISWbemEventSource,
	'{1A388F98-D4BA-11D1-8B09-00600806D9B6}' : ISWbemProperty,
	'{5791BC26-CE9C-11D1-97BF-0000F81E849C}' : SWbemObjectPath,
	'{269AD56A-8A67-4129-BC8C-0506DCFE9880}' : ISWbemObjectEx,
	'{9AED384E-CE8B-11D1-8B05-00600806D9B6}' : SWbemNamedValueSet,
	'{5791BC27-CE9C-11D1-97BF-0000F81E849C}' : ISWbemObjectPath,
	'{62E522DC-8CF3-40A8-8B2E-37D595651E40}' : SWbemServicesEx,
	'{422E8E90-D955-11D1-8B09-00600806D9B6}' : ISWbemMethod,
	'{C93BA292-D955-11D1-8B09-00600806D9B6}' : ISWbemMethodSet,
	'{79B05932-D3B7-11D1-8B06-00600806D9B6}' : ISWbemQualifier,
	'{75718C9A-F029-11D1-A1AC-00C04FB6C223}' : SWbemSink,
	'{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}' : ISWbemPropertySet,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{B54D66E6-2287-11D2-8B33-00600806D9B6}' : 'ISWbemSecurity',
	'{D2F68443-85DC-427E-91D8-366554CC754C}' : 'ISWbemServicesEx',
	'{9B16ED16-D3DF-11D1-8B08-00600806D9B6}' : 'ISWbemQualifierSet',
	'{CF2376EA-CE8C-11D1-8B05-00600806D9B6}' : 'ISWbemNamedValueSet',
	'{5E97458A-CF77-11D3-B38F-00105A1F473A}' : 'ISWbemDateTime',
	'{76A6415A-CB41-11D1-8B02-00600806D9B6}' : 'ISWbemObject',
	'{76A6415B-CB41-11D1-8B02-00600806D9B6}' : 'ISWbemLocator',
	'{76A6415C-CB41-11D1-8B02-00600806D9B6}' : 'ISWbemServices',
	'{76A6415F-CB41-11D1-8B02-00600806D9B6}' : 'ISWbemObjectSet',
	'{75718C9F-F029-11D1-A1AC-00C04FB6C223}' : 'ISWbemSink',
	'{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}' : 'ISWbemRefreshableItem',
	'{76A64164-CB41-11D1-8B02-00600806D9B6}' : 'ISWbemNamedValue',
	'{D962DB84-D4BB-11D1-8B09-00600806D9B6}' : 'ISWbemLastError',
	'{26EE67BD-5804-11D2-8B4A-00600806D9B6}' : 'ISWbemPrivilege',
	'{26EE67BF-5804-11D2-8B4A-00600806D9B6}' : 'ISWbemPrivilegeSet',
	'{14D8250E-D9C2-11D3-B38F-00105A1F473A}' : 'ISWbemRefresher',
	'{27D54D92-0EBE-11D2-8B22-00600806D9B6}' : 'ISWbemEventSource',
	'{1A388F98-D4BA-11D1-8B09-00600806D9B6}' : 'ISWbemProperty',
	'{269AD56A-8A67-4129-BC8C-0506DCFE9880}' : 'ISWbemObjectEx',
	'{5791BC27-CE9C-11D1-97BF-0000F81E849C}' : 'ISWbemObjectPath',
	'{422E8E90-D955-11D1-8B09-00600806D9B6}' : 'ISWbemMethod',
	'{C93BA292-D955-11D1-8B09-00600806D9B6}' : 'ISWbemMethodSet',
	'{79B05932-D3B7-11D1-8B06-00600806D9B6}' : 'ISWbemQualifier',
	'{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}' : 'ISWbemPropertySet',
}


NamesToIIDMap = {
	'ISWbemProperty' : '{1A388F98-D4BA-11D1-8B09-00600806D9B6}',
	'ISWbemNamedValueSet' : '{CF2376EA-CE8C-11D1-8B05-00600806D9B6}',
	'ISWbemNamedValue' : '{76A64164-CB41-11D1-8B02-00600806D9B6}',
	'ISWbemServicesEx' : '{D2F68443-85DC-427E-91D8-366554CC754C}',
	'ISWbemRefreshableItem' : '{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}',
	'ISWbemLocator' : '{76A6415B-CB41-11D1-8B02-00600806D9B6}',
	'ISWbemMethodSet' : '{C93BA292-D955-11D1-8B09-00600806D9B6}',
	'ISWbemLastError' : '{D962DB84-D4BB-11D1-8B09-00600806D9B6}',
	'ISWbemPropertySet' : '{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}',
	'ISWbemObject' : '{76A6415A-CB41-11D1-8B02-00600806D9B6}',
	'ISWbemObjectSet' : '{76A6415F-CB41-11D1-8B02-00600806D9B6}',
	'ISWbemPrivilegeSet' : '{26EE67BF-5804-11D2-8B4A-00600806D9B6}',
	'ISWbemSink' : '{75718C9F-F029-11D1-A1AC-00C04FB6C223}',
	'ISWbemSinkEvents' : '{75718CA0-F029-11D1-A1AC-00C04FB6C223}',
	'ISWbemDateTime' : '{5E97458A-CF77-11D3-B38F-00105A1F473A}',
	'ISWbemObjectEx' : '{269AD56A-8A67-4129-BC8C-0506DCFE9880}',
	'ISWbemQualifier' : '{79B05932-D3B7-11D1-8B06-00600806D9B6}',
	'ISWbemObjectPath' : '{5791BC27-CE9C-11D1-97BF-0000F81E849C}',
	'ISWbemPrivilege' : '{26EE67BD-5804-11D2-8B4A-00600806D9B6}',
	'ISWbemServices' : '{76A6415C-CB41-11D1-8B02-00600806D9B6}',
	'ISWbemEventSource' : '{27D54D92-0EBE-11D2-8B22-00600806D9B6}',
	'ISWbemRefresher' : '{14D8250E-D9C2-11D3-B38F-00105A1F473A}',
	'ISWbemSecurity' : '{B54D66E6-2287-11D2-8B33-00600806D9B6}',
	'ISWbemMethod' : '{422E8E90-D955-11D1-8B09-00600806D9B6}',
	'ISWbemQualifierSet' : '{9B16ED16-D3DF-11D1-8B08-00600806D9B6}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

