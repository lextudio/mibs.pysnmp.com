# SNMP MIB module (FSC-HSMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSC-HSMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:29 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_FscHSMS_ObjectIdentity = ObjectIdentity
fscHSMS = _FscHSMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 40)
)
_FscHSMSGlobalData_ObjectIdentity = ObjectIdentity
fscHSMSGlobalData = _FscHSMSGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1)
)


class _HsmsGDVersion_Type(DisplayString):
    """Custom type hsmsGDVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HsmsGDVersion_Type.__name__ = "DisplayString"
_HsmsGDVersion_Object = MibScalar
hsmsGDVersion = _HsmsGDVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 1),
    _HsmsGDVersion_Type()
)
hsmsGDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDVersion.setStatus("mandatory")


class _HsmsGDOpmode_Type(Integer32):
    """Custom type hsmsGDOpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("defineshow", 1),
          ("operation", 3),
          ("simulation", 2),
          ("unknown", 255))
    )


_HsmsGDOpmode_Type.__name__ = "Integer32"
_HsmsGDOpmode_Object = MibScalar
hsmsGDOpmode = _HsmsGDOpmode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 2),
    _HsmsGDOpmode_Type()
)
hsmsGDOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsmsGDOpmode.setStatus("mandatory")


class _HsmsGDServertask_Type(Integer32):
    """Custom type hsmsGDServertask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HsmsGDServertask_Type.__name__ = "Integer32"
_HsmsGDServertask_Object = MibScalar
hsmsGDServertask = _HsmsGDServertask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 3),
    _HsmsGDServertask_Type()
)
hsmsGDServertask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsmsGDServertask.setStatus("mandatory")
_HsmsGDSysMigrate_Type = DisplayString
_HsmsGDSysMigrate_Object = MibScalar
hsmsGDSysMigrate = _HsmsGDSysMigrate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 4),
    _HsmsGDSysMigrate_Type()
)
hsmsGDSysMigrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDSysMigrate.setStatus("mandatory")
_HsmsGDSysBackup_Type = DisplayString
_HsmsGDSysBackup_Object = MibScalar
hsmsGDSysBackup = _HsmsGDSysBackup_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 5),
    _HsmsGDSysBackup_Type()
)
hsmsGDSysBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDSysBackup.setStatus("mandatory")
_HsmsGDSysArchive_Type = DisplayString
_HsmsGDSysArchive_Object = MibScalar
hsmsGDSysArchive = _HsmsGDSysArchive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 6),
    _HsmsGDSysArchive_Type()
)
hsmsGDSysArchive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDSysArchive.setStatus("mandatory")
_HsmsGDSysNodeBackup_Type = DisplayString
_HsmsGDSysNodeBackup_Object = MibScalar
hsmsGDSysNodeBackup = _HsmsGDSysNodeBackup_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 7),
    _HsmsGDSysNodeBackup_Type()
)
hsmsGDSysNodeBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDSysNodeBackup.setStatus("mandatory")
_HsmsGDSysNodeArchive_Type = DisplayString
_HsmsGDSysNodeArchive_Object = MibScalar
hsmsGDSysNodeArchive = _HsmsGDSysNodeArchive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 8),
    _HsmsGDSysNodeArchive_Type()
)
hsmsGDSysNodeArchive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDSysNodeArchive.setStatus("mandatory")
_HsmsGDS1Pubset_Type = DisplayString
_HsmsGDS1Pubset_Object = MibScalar
hsmsGDS1Pubset = _HsmsGDS1Pubset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 9),
    _HsmsGDS1Pubset_Type()
)
hsmsGDS1Pubset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsGDS1Pubset.setStatus("mandatory")
_FscHSMSInstances_ObjectIdentity = ObjectIdentity
fscHSMSInstances = _FscHSMSInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2)
)
_HsmsInSubTabNum_Type = Integer32
_HsmsInSubTabNum_Object = MibScalar
hsmsInSubTabNum = _HsmsInSubTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 1),
    _HsmsInSubTabNum_Type()
)
hsmsInSubTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsInSubTabNum.setStatus("mandatory")
_HsmsInSubTable_Object = MibTable
hsmsInSubTable = _HsmsInSubTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2)
)
if mibBuilder.loadTexts:
    hsmsInSubTable.setStatus("mandatory")
_HsmsInSubEntry_Object = MibTableRow
hsmsInSubEntry = _HsmsInSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1)
)
hsmsInSubEntry.setIndexNames(
    (0, "FSC-HSMS-MIB", "hsmsInSubIndex"),
)
if mibBuilder.loadTexts:
    hsmsInSubEntry.setStatus("mandatory")
_HsmsInSubIndex_Type = Integer32
_HsmsInSubIndex_Object = MibTableColumn
hsmsInSubIndex = _HsmsInSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 1),
    _HsmsInSubIndex_Type()
)
hsmsInSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsInSubIndex.setStatus("mandatory")
_HsmsInSubName_Type = DisplayString
_HsmsInSubName_Object = MibTableColumn
hsmsInSubName = _HsmsInSubName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 2),
    _HsmsInSubName_Type()
)
hsmsInSubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsInSubName.setStatus("mandatory")
_HsmsInSubVersion_Type = DisplayString
_HsmsInSubVersion_Object = MibTableColumn
hsmsInSubVersion = _HsmsInSubVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 3),
    _HsmsInSubVersion_Type()
)
hsmsInSubVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsInSubVersion.setStatus("mandatory")


class _HsmsInSubState_Type(Integer32):
    """Custom type hsmsInSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("in-create", 4),
          ("in-delete", 3),
          ("in-hold", 6),
          ("in-resume", 5),
          ("locked", 8),
          ("not-created", 2),
          ("not-installed", 255),
          ("not-resumed", 7))
    )


_HsmsInSubState_Type.__name__ = "Integer32"
_HsmsInSubState_Object = MibTableColumn
hsmsInSubState = _HsmsInSubState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 4),
    _HsmsInSubState_Type()
)
hsmsInSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsInSubState.setStatus("mandatory")
_FscHSMSRequests_ObjectIdentity = ObjectIdentity
fscHSMSRequests = _FscHSMSRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3)
)


class _HsmsRequestTabState_Type(Integer32):
    """Custom type hsmsRequestTabState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 3),
          ("any", 1),
          ("completed", 2),
          ("interrupted", 5),
          ("started", 4))
    )


_HsmsRequestTabState_Type.__name__ = "Integer32"
_HsmsRequestTabState_Object = MibScalar
hsmsRequestTabState = _HsmsRequestTabState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 1),
    _HsmsRequestTabState_Type()
)
hsmsRequestTabState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsmsRequestTabState.setStatus("mandatory")


class _HsmsRequestTabOrigin_Type(Integer32):
    """Custom type hsmsRequestTabOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bs2000", 1),
          ("node-cl", 2))
    )


_HsmsRequestTabOrigin_Type.__name__ = "Integer32"
_HsmsRequestTabOrigin_Object = MibScalar
hsmsRequestTabOrigin = _HsmsRequestTabOrigin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 2),
    _HsmsRequestTabOrigin_Type()
)
hsmsRequestTabOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsmsRequestTabOrigin.setStatus("mandatory")


class _HsmsRequestTabNodeID_Type(DisplayString):
    """Custom type hsmsRequestTabNodeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_HsmsRequestTabNodeID_Type.__name__ = "DisplayString"
_HsmsRequestTabNodeID_Object = MibScalar
hsmsRequestTabNodeID = _HsmsRequestTabNodeID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 3),
    _HsmsRequestTabNodeID_Type()
)
hsmsRequestTabNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsmsRequestTabNodeID.setStatus("mandatory")
_HsmsRequestTable_Object = MibTable
hsmsRequestTable = _HsmsRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10)
)
if mibBuilder.loadTexts:
    hsmsRequestTable.setStatus("mandatory")
_HsmsRequestEntry_Object = MibTableRow
hsmsRequestEntry = _HsmsRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1)
)
hsmsRequestEntry.setIndexNames(
    (0, "FSC-HSMS-MIB", "hsmsRequestIndex"),
)
if mibBuilder.loadTexts:
    hsmsRequestEntry.setStatus("mandatory")
_HsmsRequestIndex_Type = Integer32
_HsmsRequestIndex_Object = MibTableColumn
hsmsRequestIndex = _HsmsRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 1),
    _HsmsRequestIndex_Type()
)
hsmsRequestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestIndex.setStatus("mandatory")


class _HsmsRequestName_Type(DisplayString):
    """Custom type hsmsRequestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HsmsRequestName_Type.__name__ = "DisplayString"
_HsmsRequestName_Object = MibTableColumn
hsmsRequestName = _HsmsRequestName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 2),
    _HsmsRequestName_Type()
)
hsmsRequestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestName.setStatus("mandatory")
_HsmsRequestDateAndTime_Type = DateAndTime
_HsmsRequestDateAndTime_Object = MibTableColumn
hsmsRequestDateAndTime = _HsmsRequestDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 3),
    _HsmsRequestDateAndTime_Type()
)
hsmsRequestDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestDateAndTime.setStatus("mandatory")
_HsmsRequestAction_Type = DisplayString
_HsmsRequestAction_Object = MibTableColumn
hsmsRequestAction = _HsmsRequestAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 4),
    _HsmsRequestAction_Type()
)
hsmsRequestAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestAction.setStatus("mandatory")
_HsmsRequestArchiveName_Type = DisplayString
_HsmsRequestArchiveName_Object = MibTableColumn
hsmsRequestArchiveName = _HsmsRequestArchiveName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 5),
    _HsmsRequestArchiveName_Type()
)
hsmsRequestArchiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestArchiveName.setStatus("mandatory")


class _HsmsRequestSim_Type(Integer32):
    """Custom type hsmsRequestSim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HsmsRequestSim_Type.__name__ = "Integer32"
_HsmsRequestSim_Object = MibTableColumn
hsmsRequestSim = _HsmsRequestSim_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 6),
    _HsmsRequestSim_Type()
)
hsmsRequestSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestSim.setStatus("mandatory")


class _HsmsRequestExp_Type(Integer32):
    """Custom type hsmsRequestExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HsmsRequestExp_Type.__name__ = "Integer32"
_HsmsRequestExp_Object = MibTableColumn
hsmsRequestExp = _HsmsRequestExp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 7),
    _HsmsRequestExp_Type()
)
hsmsRequestExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestExp.setStatus("mandatory")


class _HsmsRequestRestart_Type(Integer32):
    """Custom type hsmsRequestRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HsmsRequestRestart_Type.__name__ = "Integer32"
_HsmsRequestRestart_Object = MibTableColumn
hsmsRequestRestart = _HsmsRequestRestart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 8),
    _HsmsRequestRestart_Type()
)
hsmsRequestRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestRestart.setStatus("mandatory")


class _HsmsRequestRem_Type(Integer32):
    """Custom type hsmsRequestRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HsmsRequestRem_Type.__name__ = "Integer32"
_HsmsRequestRem_Object = MibTableColumn
hsmsRequestRem = _HsmsRequestRem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 9),
    _HsmsRequestRem_Type()
)
hsmsRequestRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestRem.setStatus("mandatory")


class _HsmsRequestState_Type(Integer32):
    """Custom type hsmsRequestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 2),
          ("cancelled", 5),
          ("completed", 4),
          ("incomplete", 1),
          ("interrupted", 6),
          ("started", 3),
          ("unknown", 255))
    )


_HsmsRequestState_Type.__name__ = "Integer32"
_HsmsRequestState_Object = MibTableColumn
hsmsRequestState = _HsmsRequestState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 10),
    _HsmsRequestState_Type()
)
hsmsRequestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestState.setStatus("mandatory")


class _HsmsRequestSubState_Type(Integer32):
    """Custom type hsmsRequestSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              20,
              255)
        )
    )
    namedValues = NamedValues(
        *(("archive-completed", 3),
          ("collected", 1),
          ("in-transmit", 9),
          ("master-no-connect", 8),
          ("master-replied", 6),
          ("master-timeout", 7),
          ("none", 20),
          ("sent-to-master", 5),
          ("start-archive", 2),
          ("start-report", 4),
          ("unknown", 255),
          ("with-errors", 11),
          ("with-warnings", 10))
    )


_HsmsRequestSubState_Type.__name__ = "Integer32"
_HsmsRequestSubState_Object = MibTableColumn
hsmsRequestSubState = _HsmsRequestSubState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 11),
    _HsmsRequestSubState_Type()
)
hsmsRequestSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestSubState.setStatus("mandatory")


class _HsmsRequestProcessor_Type(DisplayString):
    """Custom type hsmsRequestProcessor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HsmsRequestProcessor_Type.__name__ = "DisplayString"
_HsmsRequestProcessor_Object = MibTableColumn
hsmsRequestProcessor = _HsmsRequestProcessor_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 12),
    _HsmsRequestProcessor_Type()
)
hsmsRequestProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestProcessor.setStatus("mandatory")


class _HsmsRequestTSN_Type(DisplayString):
    """Custom type hsmsRequestTSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_HsmsRequestTSN_Type.__name__ = "DisplayString"
_HsmsRequestTSN_Object = MibTableColumn
hsmsRequestTSN = _HsmsRequestTSN_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 13),
    _HsmsRequestTSN_Type()
)
hsmsRequestTSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestTSN.setStatus("mandatory")


class _HsmsRequestUser_Type(DisplayString):
    """Custom type hsmsRequestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HsmsRequestUser_Type.__name__ = "DisplayString"
_HsmsRequestUser_Object = MibTableColumn
hsmsRequestUser = _HsmsRequestUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 14),
    _HsmsRequestUser_Type()
)
hsmsRequestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestUser.setStatus("mandatory")
_HsmsRequestUserNo_Type = Integer32
_HsmsRequestUserNo_Object = MibTableColumn
hsmsRequestUserNo = _HsmsRequestUserNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 15),
    _HsmsRequestUserNo_Type()
)
hsmsRequestUserNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestUserNo.setStatus("mandatory")


class _HsmsRequestNodeId_Type(DisplayString):
    """Custom type hsmsRequestNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HsmsRequestNodeId_Type.__name__ = "DisplayString"
_HsmsRequestNodeId_Object = MibTableColumn
hsmsRequestNodeId = _HsmsRequestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 16),
    _HsmsRequestNodeId_Type()
)
hsmsRequestNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestNodeId.setStatus("mandatory")
_HsmsRequestIPAddr_Type = IpAddress
_HsmsRequestIPAddr_Object = MibTableColumn
hsmsRequestIPAddr = _HsmsRequestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 17),
    _HsmsRequestIPAddr_Type()
)
hsmsRequestIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestIPAddr.setStatus("mandatory")
_HsmsRequestIPPort_Type = Integer32
_HsmsRequestIPPort_Object = MibTableColumn
hsmsRequestIPPort = _HsmsRequestIPPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 18),
    _HsmsRequestIPPort_Type()
)
hsmsRequestIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestIPPort.setStatus("mandatory")


class _HsmsRequestBspiId_Type(DisplayString):
    """Custom type hsmsRequestBspiId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_HsmsRequestBspiId_Type.__name__ = "DisplayString"
_HsmsRequestBspiId_Object = MibTableColumn
hsmsRequestBspiId = _HsmsRequestBspiId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 19),
    _HsmsRequestBspiId_Type()
)
hsmsRequestBspiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmsRequestBspiId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSC-HSMS-MIB",
    **{"DateAndTime": DateAndTime,
       "sni": sni,
       "sniProductMibs": sniProductMibs,
       "fscHSMS": fscHSMS,
       "fscHSMSGlobalData": fscHSMSGlobalData,
       "hsmsGDVersion": hsmsGDVersion,
       "hsmsGDOpmode": hsmsGDOpmode,
       "hsmsGDServertask": hsmsGDServertask,
       "hsmsGDSysMigrate": hsmsGDSysMigrate,
       "hsmsGDSysBackup": hsmsGDSysBackup,
       "hsmsGDSysArchive": hsmsGDSysArchive,
       "hsmsGDSysNodeBackup": hsmsGDSysNodeBackup,
       "hsmsGDSysNodeArchive": hsmsGDSysNodeArchive,
       "hsmsGDS1Pubset": hsmsGDS1Pubset,
       "fscHSMSInstances": fscHSMSInstances,
       "hsmsInSubTabNum": hsmsInSubTabNum,
       "hsmsInSubTable": hsmsInSubTable,
       "hsmsInSubEntry": hsmsInSubEntry,
       "hsmsInSubIndex": hsmsInSubIndex,
       "hsmsInSubName": hsmsInSubName,
       "hsmsInSubVersion": hsmsInSubVersion,
       "hsmsInSubState": hsmsInSubState,
       "fscHSMSRequests": fscHSMSRequests,
       "hsmsRequestTabState": hsmsRequestTabState,
       "hsmsRequestTabOrigin": hsmsRequestTabOrigin,
       "hsmsRequestTabNodeID": hsmsRequestTabNodeID,
       "hsmsRequestTable": hsmsRequestTable,
       "hsmsRequestEntry": hsmsRequestEntry,
       "hsmsRequestIndex": hsmsRequestIndex,
       "hsmsRequestName": hsmsRequestName,
       "hsmsRequestDateAndTime": hsmsRequestDateAndTime,
       "hsmsRequestAction": hsmsRequestAction,
       "hsmsRequestArchiveName": hsmsRequestArchiveName,
       "hsmsRequestSim": hsmsRequestSim,
       "hsmsRequestExp": hsmsRequestExp,
       "hsmsRequestRestart": hsmsRequestRestart,
       "hsmsRequestRem": hsmsRequestRem,
       "hsmsRequestState": hsmsRequestState,
       "hsmsRequestSubState": hsmsRequestSubState,
       "hsmsRequestProcessor": hsmsRequestProcessor,
       "hsmsRequestTSN": hsmsRequestTSN,
       "hsmsRequestUser": hsmsRequestUser,
       "hsmsRequestUserNo": hsmsRequestUserNo,
       "hsmsRequestNodeId": hsmsRequestNodeId,
       "hsmsRequestIPAddr": hsmsRequestIPAddr,
       "hsmsRequestIPPort": hsmsRequestIPPort,
       "hsmsRequestBspiId": hsmsRequestBspiId}
)
