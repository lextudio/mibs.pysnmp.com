# SNMP MIB module (FCMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FCMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:31 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 experimental,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class FcNameId(OctetString):
    """Custom type FcNameId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class FcGlobalId(OctetString):
    """Custom type FcGlobalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )





class FcAddressId(OctetString):
    """Custom type FcAddressId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class FcEventSeverity(Integer32):
    """Custom type FcEventSeverity based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("critical", 4),
          ("debug", 9),
          ("emergency", 2),
          ("error", 5),
          ("info", 8),
          ("mark", 10),
          ("notify", 7),
          ("unknown", 1),
          ("warning", 6))
    )





class FcUnitType(Integer32):
    """Custom type FcUnitType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("converter", 6),
          ("gateway", 5),
          ("hba", 7),
          ("host", 10),
          ("hub", 3),
          ("module", 12),
          ("other", 2),
          ("proxy-agent", 8),
          ("storage-access-device", 14),
          ("storage-device", 9),
          ("storage-subsystem", 11),
          ("swdriver", 13),
          ("switch", 4),
          ("unknown", 1),
          ("ups", 16),
          ("wdm", 15))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fcmgmt_ObjectIdentity = ObjectIdentity
fcmgmt = _Fcmgmt_ObjectIdentity(
    (1, 3, 6, 1, 3, 94)
)
_ConnSet_ObjectIdentity = ObjectIdentity
connSet = _ConnSet_ObjectIdentity(
    (1, 3, 6, 1, 3, 94, 1)
)


class _UNumber_Type(Integer32):
    """Custom type uNumber based on Integer32"""
    defaultValue = 1


_UNumber_Object = MibScalar
uNumber = _UNumber_Object(
    (1, 3, 6, 1, 3, 94, 1, 1),
    _UNumber_Type()
)
uNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uNumber.setStatus("mandatory")
_SystemURL_Type = DisplayString
_SystemURL_Object = MibScalar
systemURL = _SystemURL_Object(
    (1, 3, 6, 1, 3, 94, 1, 2),
    _SystemURL_Type()
)
systemURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemURL.setStatus("mandatory")
_StatusChangeTime_Type = TimeTicks
_StatusChangeTime_Object = MibScalar
statusChangeTime = _StatusChangeTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 3),
    _StatusChangeTime_Type()
)
statusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusChangeTime.setStatus("obsolete")
_ConfigurationChangeTime_Type = TimeTicks
_ConfigurationChangeTime_Object = MibScalar
configurationChangeTime = _ConfigurationChangeTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 4),
    _ConfigurationChangeTime_Type()
)
configurationChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationChangeTime.setStatus("obsolete")
_ConnUnitTableChangeTime_Type = TimeTicks
_ConnUnitTableChangeTime_Object = MibScalar
connUnitTableChangeTime = _ConnUnitTableChangeTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 5),
    _ConnUnitTableChangeTime_Type()
)
connUnitTableChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitTableChangeTime.setStatus("obsolete")
_ConnUnitTable_Object = MibTable
connUnitTable = _ConnUnitTable_Object(
    (1, 3, 6, 1, 3, 94, 1, 6)
)
if mibBuilder.loadTexts:
    connUnitTable.setStatus("mandatory")
_ConnUnitEntry_Object = MibTableRow
connUnitEntry = _ConnUnitEntry_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1)
)
connUnitEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitId"),
)
if mibBuilder.loadTexts:
    connUnitEntry.setStatus("mandatory")


class _ConnUnitId_Type(OctetString):
    """Custom type connUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitId_Type.__name__ = "OctetString"
_ConnUnitId_Object = MibTableColumn
connUnitId = _ConnUnitId_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 1),
    _ConnUnitId_Type()
)
connUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitId.setStatus("mandatory")
_ConnUnitGlobalId_Type = FcGlobalId
_ConnUnitGlobalId_Object = MibTableColumn
connUnitGlobalId = _ConnUnitGlobalId_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 2),
    _ConnUnitGlobalId_Type()
)
connUnitGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitGlobalId.setStatus("mandatory")
_ConnUnitType_Type = FcUnitType
_ConnUnitType_Object = MibTableColumn
connUnitType = _ConnUnitType_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 3),
    _ConnUnitType_Type()
)
connUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitType.setStatus("mandatory")
_ConnUnitNumports_Type = Integer32
_ConnUnitNumports_Object = MibTableColumn
connUnitNumports = _ConnUnitNumports_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 4),
    _ConnUnitNumports_Type()
)
connUnitNumports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitNumports.setStatus("mandatory")


class _ConnUnitState_Type(Integer32):
    """Custom type connUnitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 3),
          ("online", 2),
          ("unknown", 1))
    )


_ConnUnitState_Type.__name__ = "Integer32"
_ConnUnitState_Object = MibTableColumn
connUnitState = _ConnUnitState_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 5),
    _ConnUnitState_Type()
)
connUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitState.setStatus("mandatory")


class _ConnUnitStatus_Type(Integer32):
    """Custom type connUnitStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_ConnUnitStatus_Type.__name__ = "Integer32"
_ConnUnitStatus_Object = MibTableColumn
connUnitStatus = _ConnUnitStatus_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 6),
    _ConnUnitStatus_Type()
)
connUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitStatus.setStatus("mandatory")


class _ConnUnitProduct_Type(DisplayString):
    """Custom type connUnitProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitProduct_Type.__name__ = "DisplayString"
_ConnUnitProduct_Object = MibTableColumn
connUnitProduct = _ConnUnitProduct_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 7),
    _ConnUnitProduct_Type()
)
connUnitProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitProduct.setStatus("mandatory")


class _ConnUnitSn_Type(DisplayString):
    """Custom type connUnitSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitSn_Type.__name__ = "DisplayString"
_ConnUnitSn_Object = MibTableColumn
connUnitSn = _ConnUnitSn_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 8),
    _ConnUnitSn_Type()
)
connUnitSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSn.setStatus("mandatory")
_ConnUnitUpTime_Type = TimeTicks
_ConnUnitUpTime_Object = MibTableColumn
connUnitUpTime = _ConnUnitUpTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 9),
    _ConnUnitUpTime_Type()
)
connUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitUpTime.setStatus("mandatory")
_ConnUnitUrl_Type = DisplayString
_ConnUnitUrl_Object = MibTableColumn
connUnitUrl = _ConnUnitUrl_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 10),
    _ConnUnitUrl_Type()
)
connUnitUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitUrl.setStatus("mandatory")


class _ConnUnitDomainId_Type(OctetString):
    """Custom type connUnitDomainId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_ConnUnitDomainId_Type.__name__ = "OctetString"
_ConnUnitDomainId_Object = MibTableColumn
connUnitDomainId = _ConnUnitDomainId_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 11),
    _ConnUnitDomainId_Type()
)
connUnitDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitDomainId.setStatus("mandatory")


class _ConnUnitProxyMaster_Type(Integer32):
    """Custom type connUnitProxyMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 1),
          ("yes", 3))
    )


_ConnUnitProxyMaster_Type.__name__ = "Integer32"
_ConnUnitProxyMaster_Object = MibTableColumn
connUnitProxyMaster = _ConnUnitProxyMaster_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 12),
    _ConnUnitProxyMaster_Type()
)
connUnitProxyMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitProxyMaster.setStatus("mandatory")


class _ConnUnitPrincipal_Type(Integer32):
    """Custom type connUnitPrincipal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 1),
          ("yes", 3))
    )


_ConnUnitPrincipal_Type.__name__ = "Integer32"
_ConnUnitPrincipal_Object = MibTableColumn
connUnitPrincipal = _ConnUnitPrincipal_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 13),
    _ConnUnitPrincipal_Type()
)
connUnitPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPrincipal.setStatus("mandatory")
_ConnUnitNumSensors_Type = Integer32
_ConnUnitNumSensors_Object = MibTableColumn
connUnitNumSensors = _ConnUnitNumSensors_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 14),
    _ConnUnitNumSensors_Type()
)
connUnitNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitNumSensors.setStatus("mandatory")
_ConnUnitStatusChangeTime_Type = TimeTicks
_ConnUnitStatusChangeTime_Object = MibTableColumn
connUnitStatusChangeTime = _ConnUnitStatusChangeTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 15),
    _ConnUnitStatusChangeTime_Type()
)
connUnitStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitStatusChangeTime.setStatus("obsolete")
_ConnUnitConfigurationChangeTime_Type = TimeTicks
_ConnUnitConfigurationChangeTime_Object = MibTableColumn
connUnitConfigurationChangeTime = _ConnUnitConfigurationChangeTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 16),
    _ConnUnitConfigurationChangeTime_Type()
)
connUnitConfigurationChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitConfigurationChangeTime.setStatus("obsolete")


class _ConnUnitNumRevs_Type(Integer32):
    """Custom type connUnitNumRevs based on Integer32"""
    defaultValue = 1


_ConnUnitNumRevs_Object = MibTableColumn
connUnitNumRevs = _ConnUnitNumRevs_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 17),
    _ConnUnitNumRevs_Type()
)
connUnitNumRevs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitNumRevs.setStatus("mandatory")
_ConnUnitNumZones_Type = Integer32
_ConnUnitNumZones_Object = MibTableColumn
connUnitNumZones = _ConnUnitNumZones_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 18),
    _ConnUnitNumZones_Type()
)
connUnitNumZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitNumZones.setStatus("obsolete")


class _ConnUnitModuleId_Type(OctetString):
    """Custom type connUnitModuleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitModuleId_Type.__name__ = "OctetString"
_ConnUnitModuleId_Object = MibTableColumn
connUnitModuleId = _ConnUnitModuleId_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 19),
    _ConnUnitModuleId_Type()
)
connUnitModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitModuleId.setStatus("mandatory")


class _ConnUnitName_Type(DisplayString):
    """Custom type connUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitName_Type.__name__ = "DisplayString"
_ConnUnitName_Object = MibTableColumn
connUnitName = _ConnUnitName_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 20),
    _ConnUnitName_Type()
)
connUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitName.setStatus("mandatory")
_ConnUnitInfo_Type = DisplayString
_ConnUnitInfo_Object = MibTableColumn
connUnitInfo = _ConnUnitInfo_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 21),
    _ConnUnitInfo_Type()
)
connUnitInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitInfo.setStatus("mandatory")


class _ConnUnitControl_Type(Integer32):
    """Custom type connUnitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("offlineConnUnit", 5),
          ("onlineConnUnit", 6),
          ("resetConnUnitColdStart", 3),
          ("resetConnUnitWarmStart", 4),
          ("unknown", 1))
    )


_ConnUnitControl_Type.__name__ = "Integer32"
_ConnUnitControl_Object = MibTableColumn
connUnitControl = _ConnUnitControl_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 22),
    _ConnUnitControl_Type()
)
connUnitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitControl.setStatus("mandatory")


class _ConnUnitContact_Type(DisplayString):
    """Custom type connUnitContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitContact_Type.__name__ = "DisplayString"
_ConnUnitContact_Object = MibTableColumn
connUnitContact = _ConnUnitContact_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 23),
    _ConnUnitContact_Type()
)
connUnitContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitContact.setStatus("mandatory")


class _ConnUnitLocation_Type(DisplayString):
    """Custom type connUnitLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitLocation_Type.__name__ = "DisplayString"
_ConnUnitLocation_Object = MibTableColumn
connUnitLocation = _ConnUnitLocation_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 24),
    _ConnUnitLocation_Type()
)
connUnitLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitLocation.setStatus("mandatory")
_ConnUnitEventFilter_Type = FcEventSeverity
_ConnUnitEventFilter_Object = MibTableColumn
connUnitEventFilter = _ConnUnitEventFilter_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 25),
    _ConnUnitEventFilter_Type()
)
connUnitEventFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventFilter.setStatus("mandatory")
_ConnUnitNumEvents_Type = Integer32
_ConnUnitNumEvents_Object = MibTableColumn
connUnitNumEvents = _ConnUnitNumEvents_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 26),
    _ConnUnitNumEvents_Type()
)
connUnitNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitNumEvents.setStatus("mandatory")
_ConnUnitMaxEvents_Type = Integer32
_ConnUnitMaxEvents_Object = MibTableColumn
connUnitMaxEvents = _ConnUnitMaxEvents_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 27),
    _ConnUnitMaxEvents_Type()
)
connUnitMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitMaxEvents.setStatus("mandatory")
_ConnUnitEventCurrID_Type = Integer32
_ConnUnitEventCurrID_Object = MibTableColumn
connUnitEventCurrID = _ConnUnitEventCurrID_Object(
    (1, 3, 6, 1, 3, 94, 1, 6, 1, 28),
    _ConnUnitEventCurrID_Type()
)
connUnitEventCurrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventCurrID.setStatus("mandatory")
_ConnUnitRevsTable_Object = MibTable
connUnitRevsTable = _ConnUnitRevsTable_Object(
    (1, 3, 6, 1, 3, 94, 1, 7)
)
if mibBuilder.loadTexts:
    connUnitRevsTable.setStatus("mandatory")
_ConnUnitRevsEntry_Object = MibTableRow
connUnitRevsEntry = _ConnUnitRevsEntry_Object(
    (1, 3, 6, 1, 3, 94, 1, 7, 1)
)
connUnitRevsEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitRevsUnitId"),
    (0, "FCMGMT-MIB", "connUnitRevsIndex"),
)
if mibBuilder.loadTexts:
    connUnitRevsEntry.setStatus("mandatory")


class _ConnUnitRevsUnitId_Type(OctetString):
    """Custom type connUnitRevsUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitRevsUnitId_Type.__name__ = "OctetString"
_ConnUnitRevsUnitId_Object = MibTableColumn
connUnitRevsUnitId = _ConnUnitRevsUnitId_Object(
    (1, 3, 6, 1, 3, 94, 1, 7, 1, 1),
    _ConnUnitRevsUnitId_Type()
)
connUnitRevsUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitRevsUnitId.setStatus("mandatory")


class _ConnUnitRevsIndex_Type(Integer32):
    """Custom type connUnitRevsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConnUnitRevsIndex_Type.__name__ = "Integer32"
_ConnUnitRevsIndex_Object = MibTableColumn
connUnitRevsIndex = _ConnUnitRevsIndex_Object(
    (1, 3, 6, 1, 3, 94, 1, 7, 1, 2),
    _ConnUnitRevsIndex_Type()
)
connUnitRevsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitRevsIndex.setStatus("mandatory")
_ConnUnitRevsRevId_Type = DisplayString
_ConnUnitRevsRevId_Object = MibTableColumn
connUnitRevsRevId = _ConnUnitRevsRevId_Object(
    (1, 3, 6, 1, 3, 94, 1, 7, 1, 3),
    _ConnUnitRevsRevId_Type()
)
connUnitRevsRevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitRevsRevId.setStatus("mandatory")
_ConnUnitRevsDescription_Type = DisplayString
_ConnUnitRevsDescription_Object = MibTableColumn
connUnitRevsDescription = _ConnUnitRevsDescription_Object(
    (1, 3, 6, 1, 3, 94, 1, 7, 1, 4),
    _ConnUnitRevsDescription_Type()
)
connUnitRevsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitRevsDescription.setStatus("mandatory")
_ConnUnitSensorTable_Object = MibTable
connUnitSensorTable = _ConnUnitSensorTable_Object(
    (1, 3, 6, 1, 3, 94, 1, 8)
)
if mibBuilder.loadTexts:
    connUnitSensorTable.setStatus("mandatory")
_ConnUnitSensorEntry_Object = MibTableRow
connUnitSensorEntry = _ConnUnitSensorEntry_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1)
)
connUnitSensorEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitSensorUnitId"),
    (0, "FCMGMT-MIB", "connUnitSensorIndex"),
)
if mibBuilder.loadTexts:
    connUnitSensorEntry.setStatus("mandatory")


class _ConnUnitSensorUnitId_Type(OctetString):
    """Custom type connUnitSensorUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitSensorUnitId_Type.__name__ = "OctetString"
_ConnUnitSensorUnitId_Object = MibTableColumn
connUnitSensorUnitId = _ConnUnitSensorUnitId_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 1),
    _ConnUnitSensorUnitId_Type()
)
connUnitSensorUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorUnitId.setStatus("mandatory")


class _ConnUnitSensorIndex_Type(Integer32):
    """Custom type connUnitSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConnUnitSensorIndex_Type.__name__ = "Integer32"
_ConnUnitSensorIndex_Object = MibTableColumn
connUnitSensorIndex = _ConnUnitSensorIndex_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 2),
    _ConnUnitSensorIndex_Type()
)
connUnitSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorIndex.setStatus("mandatory")
_ConnUnitSensorName_Type = DisplayString
_ConnUnitSensorName_Object = MibTableColumn
connUnitSensorName = _ConnUnitSensorName_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 3),
    _ConnUnitSensorName_Type()
)
connUnitSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorName.setStatus("mandatory")


class _ConnUnitSensorStatus_Type(Integer32):
    """Custom type connUnitSensorStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("other", 2),
          ("unknown", 1),
          ("warning", 4))
    )


_ConnUnitSensorStatus_Type.__name__ = "Integer32"
_ConnUnitSensorStatus_Object = MibTableColumn
connUnitSensorStatus = _ConnUnitSensorStatus_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 4),
    _ConnUnitSensorStatus_Type()
)
connUnitSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorStatus.setStatus("mandatory")
_ConnUnitSensorInfo_Type = DisplayString
_ConnUnitSensorInfo_Object = MibTableColumn
connUnitSensorInfo = _ConnUnitSensorInfo_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 5),
    _ConnUnitSensorInfo_Type()
)
connUnitSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorInfo.setStatus("mandatory")
_ConnUnitSensorMessage_Type = DisplayString
_ConnUnitSensorMessage_Object = MibTableColumn
connUnitSensorMessage = _ConnUnitSensorMessage_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 6),
    _ConnUnitSensorMessage_Type()
)
connUnitSensorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorMessage.setStatus("mandatory")


class _ConnUnitSensorType_Type(Integer32):
    """Custom type connUnitSensorType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("battery", 3),
          ("board", 8),
          ("enclosure", 7),
          ("fan", 4),
          ("other", 2),
          ("power-supply", 5),
          ("receiver", 9),
          ("transmitter", 6),
          ("unknown", 1))
    )


_ConnUnitSensorType_Type.__name__ = "Integer32"
_ConnUnitSensorType_Object = MibTableColumn
connUnitSensorType = _ConnUnitSensorType_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 7),
    _ConnUnitSensorType_Type()
)
connUnitSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorType.setStatus("mandatory")


class _ConnUnitSensorCharacteristic_Type(Integer32):
    """Custom type connUnitSensorCharacteristic based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("airflow", 7),
          ("currentValue", 6),
          ("door", 10),
          ("emf", 5),
          ("frequency", 8),
          ("other", 2),
          ("power", 9),
          ("pressure", 4),
          ("temperature", 3),
          ("unknown", 1))
    )


_ConnUnitSensorCharacteristic_Type.__name__ = "Integer32"
_ConnUnitSensorCharacteristic_Object = MibTableColumn
connUnitSensorCharacteristic = _ConnUnitSensorCharacteristic_Object(
    (1, 3, 6, 1, 3, 94, 1, 8, 1, 8),
    _ConnUnitSensorCharacteristic_Type()
)
connUnitSensorCharacteristic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSensorCharacteristic.setStatus("mandatory")
_ConnUnitPortTable_Object = MibTable
connUnitPortTable = _ConnUnitPortTable_Object(
    (1, 3, 6, 1, 3, 94, 1, 10)
)
if mibBuilder.loadTexts:
    connUnitPortTable.setStatus("mandatory")
_ConnUnitPortEntry_Object = MibTableRow
connUnitPortEntry = _ConnUnitPortEntry_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1)
)
connUnitPortEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitPortUnitId"),
    (0, "FCMGMT-MIB", "connUnitPortIndex"),
)
if mibBuilder.loadTexts:
    connUnitPortEntry.setStatus("mandatory")


class _ConnUnitPortUnitId_Type(OctetString):
    """Custom type connUnitPortUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitPortUnitId_Type.__name__ = "OctetString"
_ConnUnitPortUnitId_Object = MibTableColumn
connUnitPortUnitId = _ConnUnitPortUnitId_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 1),
    _ConnUnitPortUnitId_Type()
)
connUnitPortUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortUnitId.setStatus("mandatory")


class _ConnUnitPortIndex_Type(Integer32):
    """Custom type connUnitPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConnUnitPortIndex_Type.__name__ = "Integer32"
_ConnUnitPortIndex_Object = MibTableColumn
connUnitPortIndex = _ConnUnitPortIndex_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 2),
    _ConnUnitPortIndex_Type()
)
connUnitPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortIndex.setStatus("mandatory")


class _ConnUnitPortType_Type(Integer32):
    """Custom type connUnitPortType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ac", 17),
          ("dc", 18),
          ("domain-ctl", 11),
          ("e-port", 9),
          ("escon", 14),
          ("f-port", 8),
          ("fl-port", 7),
          ("g-port", 10),
          ("hub-controller", 12),
          ("hub-port", 4),
          ("l-port", 6),
          ("lan", 15),
          ("n-port", 5),
          ("not-present", 3),
          ("other", 2),
          ("scsi", 13),
          ("ssa", 19),
          ("unknown", 1),
          ("wan", 16))
    )


_ConnUnitPortType_Type.__name__ = "Integer32"
_ConnUnitPortType_Object = MibTableColumn
connUnitPortType = _ConnUnitPortType_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 3),
    _ConnUnitPortType_Type()
)
connUnitPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortType.setStatus("mandatory")


class _ConnUnitPortFCClassCap_Type(OctetString):
    """Custom type connUnitPortFCClassCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ConnUnitPortFCClassCap_Type.__name__ = "OctetString"
_ConnUnitPortFCClassCap_Object = MibTableColumn
connUnitPortFCClassCap = _ConnUnitPortFCClassCap_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 4),
    _ConnUnitPortFCClassCap_Type()
)
connUnitPortFCClassCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortFCClassCap.setStatus("mandatory")


class _ConnUnitPortFCClassOp_Type(OctetString):
    """Custom type connUnitPortFCClassOp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ConnUnitPortFCClassOp_Type.__name__ = "OctetString"
_ConnUnitPortFCClassOp_Object = MibTableColumn
connUnitPortFCClassOp = _ConnUnitPortFCClassOp_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 5),
    _ConnUnitPortFCClassOp_Type()
)
connUnitPortFCClassOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortFCClassOp.setStatus("mandatory")


class _ConnUnitPortState_Type(Integer32):
    """Custom type connUnitPortState based on Integer32"""
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
        *(("bypassed", 4),
          ("diagnostics", 5),
          ("offline", 3),
          ("online", 2),
          ("unknown", 1))
    )


_ConnUnitPortState_Type.__name__ = "Integer32"
_ConnUnitPortState_Object = MibTableColumn
connUnitPortState = _ConnUnitPortState_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 6),
    _ConnUnitPortState_Type()
)
connUnitPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortState.setStatus("mandatory")


class _ConnUnitPortStatus_Type(Integer32):
    """Custom type connUnitPortStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 8),
          ("failure", 5),
          ("initializing", 7),
          ("notparticipating", 6),
          ("ols", 9),
          ("ready", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_ConnUnitPortStatus_Type.__name__ = "Integer32"
_ConnUnitPortStatus_Object = MibTableColumn
connUnitPortStatus = _ConnUnitPortStatus_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 7),
    _ConnUnitPortStatus_Type()
)
connUnitPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatus.setStatus("mandatory")


class _ConnUnitPortTransmitterType_Type(Integer32):
    """Custom type connUnitPortTransmitterType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("copper", 6),
          ("longwave", 5),
          ("longwaveLED", 10),
          ("longwaveNoOFC", 8),
          ("other", 2),
          ("scsi", 7),
          ("shortwave", 4),
          ("shortwaveNoOFC", 9),
          ("ssa", 11),
          ("unknown", 1),
          ("unused", 3))
    )


_ConnUnitPortTransmitterType_Type.__name__ = "Integer32"
_ConnUnitPortTransmitterType_Object = MibTableColumn
connUnitPortTransmitterType = _ConnUnitPortTransmitterType_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 8),
    _ConnUnitPortTransmitterType_Type()
)
connUnitPortTransmitterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortTransmitterType.setStatus("mandatory")


class _ConnUnitPortModuleType_Type(Integer32):
    """Custom type connUnitPortModuleType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("embedded", 4),
          ("gbic", 3),
          ("gbicNoSerialId", 7),
          ("gbicNotInstalled", 8),
          ("gbicSerialId", 6),
          ("glm", 5),
          ("other", 2),
          ("smallFormFactor", 9),
          ("unknown", 1))
    )


_ConnUnitPortModuleType_Type.__name__ = "Integer32"
_ConnUnitPortModuleType_Object = MibTableColumn
connUnitPortModuleType = _ConnUnitPortModuleType_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 9),
    _ConnUnitPortModuleType_Type()
)
connUnitPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortModuleType.setStatus("mandatory")
_ConnUnitPortWwn_Type = FcNameId
_ConnUnitPortWwn_Object = MibTableColumn
connUnitPortWwn = _ConnUnitPortWwn_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 10),
    _ConnUnitPortWwn_Type()
)
connUnitPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortWwn.setStatus("mandatory")


class _ConnUnitPortFCId_Type(OctetString):
    """Custom type connUnitPortFCId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_ConnUnitPortFCId_Type.__name__ = "OctetString"
_ConnUnitPortFCId_Object = MibTableColumn
connUnitPortFCId = _ConnUnitPortFCId_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 11),
    _ConnUnitPortFCId_Type()
)
connUnitPortFCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortFCId.setStatus("mandatory")


class _ConnUnitPortSn_Type(DisplayString):
    """Custom type connUnitPortSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitPortSn_Type.__name__ = "DisplayString"
_ConnUnitPortSn_Object = MibTableColumn
connUnitPortSn = _ConnUnitPortSn_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 12),
    _ConnUnitPortSn_Type()
)
connUnitPortSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortSn.setStatus("mandatory")


class _ConnUnitPortRevision_Type(DisplayString):
    """Custom type connUnitPortRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitPortRevision_Type.__name__ = "DisplayString"
_ConnUnitPortRevision_Object = MibTableColumn
connUnitPortRevision = _ConnUnitPortRevision_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 13),
    _ConnUnitPortRevision_Type()
)
connUnitPortRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortRevision.setStatus("mandatory")


class _ConnUnitPortVendor_Type(DisplayString):
    """Custom type connUnitPortVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitPortVendor_Type.__name__ = "DisplayString"
_ConnUnitPortVendor_Object = MibTableColumn
connUnitPortVendor = _ConnUnitPortVendor_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 14),
    _ConnUnitPortVendor_Type()
)
connUnitPortVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortVendor.setStatus("mandatory")
_ConnUnitPortSpeed_Type = Integer32
_ConnUnitPortSpeed_Object = MibTableColumn
connUnitPortSpeed = _ConnUnitPortSpeed_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 15),
    _ConnUnitPortSpeed_Type()
)
connUnitPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortSpeed.setStatus("mandatory")


class _ConnUnitPortControl_Type(Integer32):
    """Custom type connUnitPortControl based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bypassConnUnitPort", 4),
          ("invalid", 2),
          ("offlineConnUnitPort", 6),
          ("onlineConnUnitPort", 7),
          ("resetConnUnitPort", 3),
          ("resetConnUnitPortCounters", 8),
          ("unbypassConnUnitPort", 5),
          ("unknown", 1))
    )


_ConnUnitPortControl_Type.__name__ = "Integer32"
_ConnUnitPortControl_Object = MibTableColumn
connUnitPortControl = _ConnUnitPortControl_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 16),
    _ConnUnitPortControl_Type()
)
connUnitPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitPortControl.setStatus("mandatory")
_ConnUnitPortName_Type = DisplayString
_ConnUnitPortName_Object = MibTableColumn
connUnitPortName = _ConnUnitPortName_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 17),
    _ConnUnitPortName_Type()
)
connUnitPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connUnitPortName.setStatus("mandatory")
_ConnUnitPortPhysicalNumber_Type = Integer32
_ConnUnitPortPhysicalNumber_Object = MibTableColumn
connUnitPortPhysicalNumber = _ConnUnitPortPhysicalNumber_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 18),
    _ConnUnitPortPhysicalNumber_Type()
)
connUnitPortPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortPhysicalNumber.setStatus("mandatory")
_ConnUnitPortStatObject_Type = ObjectIdentifier
_ConnUnitPortStatObject_Object = MibTableColumn
connUnitPortStatObject = _ConnUnitPortStatObject_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 19),
    _ConnUnitPortStatObject_Type()
)
connUnitPortStatObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatObject.setStatus("deprecated")


class _ConnUnitPortProtocolCap_Type(OctetString):
    """Custom type connUnitPortProtocolCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ConnUnitPortProtocolCap_Type.__name__ = "OctetString"
_ConnUnitPortProtocolCap_Object = MibTableColumn
connUnitPortProtocolCap = _ConnUnitPortProtocolCap_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 20),
    _ConnUnitPortProtocolCap_Type()
)
connUnitPortProtocolCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortProtocolCap.setStatus("mandatory")


class _ConnUnitPortProtocolOp_Type(OctetString):
    """Custom type connUnitPortProtocolOp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ConnUnitPortProtocolOp_Type.__name__ = "OctetString"
_ConnUnitPortProtocolOp_Object = MibTableColumn
connUnitPortProtocolOp = _ConnUnitPortProtocolOp_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 21),
    _ConnUnitPortProtocolOp_Type()
)
connUnitPortProtocolOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortProtocolOp.setStatus("mandatory")
_ConnUnitPortNodeWwn_Type = FcNameId
_ConnUnitPortNodeWwn_Object = MibTableColumn
connUnitPortNodeWwn = _ConnUnitPortNodeWwn_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 22),
    _ConnUnitPortNodeWwn_Type()
)
connUnitPortNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortNodeWwn.setStatus("mandatory")


class _ConnUnitPortHWState_Type(Integer32):
    """Custom type connUnitPortHWState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("bypassed", 3),
          ("failed", 2),
          ("linkDown", 8),
          ("loopback", 5),
          ("noMedia", 7),
          ("txfault", 6),
          ("unknown", 1))
    )


_ConnUnitPortHWState_Type.__name__ = "Integer32"
_ConnUnitPortHWState_Object = MibTableColumn
connUnitPortHWState = _ConnUnitPortHWState_Object(
    (1, 3, 6, 1, 3, 94, 1, 10, 1, 23),
    _ConnUnitPortHWState_Type()
)
connUnitPortHWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortHWState.setStatus("mandatory")
_ConnUnitEventTable_Object = MibTable
connUnitEventTable = _ConnUnitEventTable_Object(
    (1, 3, 6, 1, 3, 94, 1, 11)
)
if mibBuilder.loadTexts:
    connUnitEventTable.setStatus("mandatory")
_ConnUnitEventEntry_Object = MibTableRow
connUnitEventEntry = _ConnUnitEventEntry_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1)
)
connUnitEventEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitEventUnitId"),
    (0, "FCMGMT-MIB", "connUnitEventIndex"),
)
if mibBuilder.loadTexts:
    connUnitEventEntry.setStatus("mandatory")


class _ConnUnitEventUnitId_Type(OctetString):
    """Custom type connUnitEventUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitEventUnitId_Type.__name__ = "OctetString"
_ConnUnitEventUnitId_Object = MibTableColumn
connUnitEventUnitId = _ConnUnitEventUnitId_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 1),
    _ConnUnitEventUnitId_Type()
)
connUnitEventUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventUnitId.setStatus("mandatory")


class _ConnUnitEventIndex_Type(Integer32):
    """Custom type connUnitEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConnUnitEventIndex_Type.__name__ = "Integer32"
_ConnUnitEventIndex_Object = MibTableColumn
connUnitEventIndex = _ConnUnitEventIndex_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 2),
    _ConnUnitEventIndex_Type()
)
connUnitEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventIndex.setStatus("mandatory")
_ConnUnitEventId_Type = Integer32
_ConnUnitEventId_Object = MibTableColumn
connUnitEventId = _ConnUnitEventId_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 3),
    _ConnUnitEventId_Type()
)
connUnitEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventId.setStatus("obsolete")


class _ConnUnitREventTime_Type(DisplayString):
    """Custom type connUnitREventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_ConnUnitREventTime_Type.__name__ = "DisplayString"
_ConnUnitREventTime_Object = MibTableColumn
connUnitREventTime = _ConnUnitREventTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 4),
    _ConnUnitREventTime_Type()
)
connUnitREventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitREventTime.setStatus("mandatory")
_ConnUnitSEventTime_Type = TimeTicks
_ConnUnitSEventTime_Object = MibTableColumn
connUnitSEventTime = _ConnUnitSEventTime_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 5),
    _ConnUnitSEventTime_Type()
)
connUnitSEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSEventTime.setStatus("mandatory")
_ConnUnitEventSeverity_Type = FcEventSeverity
_ConnUnitEventSeverity_Object = MibTableColumn
connUnitEventSeverity = _ConnUnitEventSeverity_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 6),
    _ConnUnitEventSeverity_Type()
)
connUnitEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventSeverity.setStatus("mandatory")


class _ConnUnitEventType_Type(Integer32):
    """Custom type connUnitEventType based on Integer32"""
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
        *(("configuration", 4),
          ("other", 2),
          ("status", 3),
          ("topology", 5),
          ("unknown", 1))
    )


_ConnUnitEventType_Type.__name__ = "Integer32"
_ConnUnitEventType_Object = MibTableColumn
connUnitEventType = _ConnUnitEventType_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 7),
    _ConnUnitEventType_Type()
)
connUnitEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventType.setStatus("mandatory")
_ConnUnitEventObject_Type = ObjectIdentifier
_ConnUnitEventObject_Object = MibTableColumn
connUnitEventObject = _ConnUnitEventObject_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 8),
    _ConnUnitEventObject_Type()
)
connUnitEventObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventObject.setStatus("mandatory")
_ConnUnitEventDescr_Type = DisplayString
_ConnUnitEventDescr_Object = MibTableColumn
connUnitEventDescr = _ConnUnitEventDescr_Object(
    (1, 3, 6, 1, 3, 94, 1, 11, 1, 9),
    _ConnUnitEventDescr_Type()
)
connUnitEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitEventDescr.setStatus("mandatory")
_ConnUnitLinkTable_Object = MibTable
connUnitLinkTable = _ConnUnitLinkTable_Object(
    (1, 3, 6, 1, 3, 94, 1, 12)
)
if mibBuilder.loadTexts:
    connUnitLinkTable.setStatus("mandatory")
_ConnUnitLinkEntry_Object = MibTableRow
connUnitLinkEntry = _ConnUnitLinkEntry_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1)
)
connUnitLinkEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitLinkUnitId"),
    (0, "FCMGMT-MIB", "connUnitLinkIndex"),
)
if mibBuilder.loadTexts:
    connUnitLinkEntry.setStatus("mandatory")


class _ConnUnitLinkUnitId_Type(OctetString):
    """Custom type connUnitLinkUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitLinkUnitId_Type.__name__ = "OctetString"
_ConnUnitLinkUnitId_Object = MibTableColumn
connUnitLinkUnitId = _ConnUnitLinkUnitId_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 1),
    _ConnUnitLinkUnitId_Type()
)
connUnitLinkUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkUnitId.setStatus("mandatory")


class _ConnUnitLinkIndex_Type(Integer32):
    """Custom type connUnitLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnUnitLinkIndex_Type.__name__ = "Integer32"
_ConnUnitLinkIndex_Object = MibTableColumn
connUnitLinkIndex = _ConnUnitLinkIndex_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 2),
    _ConnUnitLinkIndex_Type()
)
connUnitLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkIndex.setStatus("mandatory")


class _ConnUnitLinkNodeIdX_Type(OctetString):
    """Custom type connUnitLinkNodeIdX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ConnUnitLinkNodeIdX_Type.__name__ = "OctetString"
_ConnUnitLinkNodeIdX_Object = MibTableColumn
connUnitLinkNodeIdX = _ConnUnitLinkNodeIdX_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 3),
    _ConnUnitLinkNodeIdX_Type()
)
connUnitLinkNodeIdX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkNodeIdX.setStatus("mandatory")
_ConnUnitLinkPortNumberX_Type = Integer32
_ConnUnitLinkPortNumberX_Object = MibTableColumn
connUnitLinkPortNumberX = _ConnUnitLinkPortNumberX_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 4),
    _ConnUnitLinkPortNumberX_Type()
)
connUnitLinkPortNumberX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkPortNumberX.setStatus("mandatory")


class _ConnUnitLinkPortWwnX_Type(OctetString):
    """Custom type connUnitLinkPortWwnX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitLinkPortWwnX_Type.__name__ = "OctetString"
_ConnUnitLinkPortWwnX_Object = MibTableColumn
connUnitLinkPortWwnX = _ConnUnitLinkPortWwnX_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 5),
    _ConnUnitLinkPortWwnX_Type()
)
connUnitLinkPortWwnX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkPortWwnX.setStatus("mandatory")


class _ConnUnitLinkNodeIdY_Type(OctetString):
    """Custom type connUnitLinkNodeIdY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ConnUnitLinkNodeIdY_Type.__name__ = "OctetString"
_ConnUnitLinkNodeIdY_Object = MibTableColumn
connUnitLinkNodeIdY = _ConnUnitLinkNodeIdY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 6),
    _ConnUnitLinkNodeIdY_Type()
)
connUnitLinkNodeIdY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkNodeIdY.setStatus("mandatory")
_ConnUnitLinkPortNumberY_Type = Integer32
_ConnUnitLinkPortNumberY_Object = MibTableColumn
connUnitLinkPortNumberY = _ConnUnitLinkPortNumberY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 7),
    _ConnUnitLinkPortNumberY_Type()
)
connUnitLinkPortNumberY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkPortNumberY.setStatus("mandatory")


class _ConnUnitLinkPortWwnY_Type(OctetString):
    """Custom type connUnitLinkPortWwnY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitLinkPortWwnY_Type.__name__ = "OctetString"
_ConnUnitLinkPortWwnY_Object = MibTableColumn
connUnitLinkPortWwnY = _ConnUnitLinkPortWwnY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 8),
    _ConnUnitLinkPortWwnY_Type()
)
connUnitLinkPortWwnY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkPortWwnY.setStatus("mandatory")


class _ConnUnitLinkAgentAddressY_Type(OctetString):
    """Custom type connUnitLinkAgentAddressY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitLinkAgentAddressY_Type.__name__ = "OctetString"
_ConnUnitLinkAgentAddressY_Object = MibTableColumn
connUnitLinkAgentAddressY = _ConnUnitLinkAgentAddressY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 9),
    _ConnUnitLinkAgentAddressY_Type()
)
connUnitLinkAgentAddressY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkAgentAddressY.setStatus("mandatory")
_ConnUnitLinkAgentAddressTypeY_Type = Integer32
_ConnUnitLinkAgentAddressTypeY_Object = MibTableColumn
connUnitLinkAgentAddressTypeY = _ConnUnitLinkAgentAddressTypeY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 10),
    _ConnUnitLinkAgentAddressTypeY_Type()
)
connUnitLinkAgentAddressTypeY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkAgentAddressTypeY.setStatus("mandatory")
_ConnUnitLinkAgentPortY_Type = Integer32
_ConnUnitLinkAgentPortY_Object = MibTableColumn
connUnitLinkAgentPortY = _ConnUnitLinkAgentPortY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 11),
    _ConnUnitLinkAgentPortY_Type()
)
connUnitLinkAgentPortY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkAgentPortY.setStatus("mandatory")
_ConnUnitLinkUnitTypeY_Type = FcUnitType
_ConnUnitLinkUnitTypeY_Object = MibTableColumn
connUnitLinkUnitTypeY = _ConnUnitLinkUnitTypeY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 12),
    _ConnUnitLinkUnitTypeY_Type()
)
connUnitLinkUnitTypeY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkUnitTypeY.setStatus("mandatory")


class _ConnUnitLinkConnIdY_Type(OctetString):
    """Custom type connUnitLinkConnIdY based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_ConnUnitLinkConnIdY_Type.__name__ = "OctetString"
_ConnUnitLinkConnIdY_Object = MibTableColumn
connUnitLinkConnIdY = _ConnUnitLinkConnIdY_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 13),
    _ConnUnitLinkConnIdY_Type()
)
connUnitLinkConnIdY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkConnIdY.setStatus("mandatory")
_ConnUnitLinkCurrIndex_Type = Integer32
_ConnUnitLinkCurrIndex_Object = MibTableColumn
connUnitLinkCurrIndex = _ConnUnitLinkCurrIndex_Object(
    (1, 3, 6, 1, 3, 94, 1, 12, 1, 14),
    _ConnUnitLinkCurrIndex_Type()
)
connUnitLinkCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitLinkCurrIndex.setStatus("mandatory")
_TrapReg_ObjectIdentity = ObjectIdentity
trapReg = _TrapReg_ObjectIdentity(
    (1, 3, 6, 1, 3, 94, 2)
)
_TrapMaxClients_Type = Integer32
_TrapMaxClients_Object = MibScalar
trapMaxClients = _TrapMaxClients_Object(
    (1, 3, 6, 1, 3, 94, 2, 1),
    _TrapMaxClients_Type()
)
trapMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMaxClients.setStatus("mandatory")
_TrapClientCount_Type = Integer32
_TrapClientCount_Object = MibScalar
trapClientCount = _TrapClientCount_Object(
    (1, 3, 6, 1, 3, 94, 2, 2),
    _TrapClientCount_Type()
)
trapClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientCount.setStatus("mandatory")
_TrapRegTable_Object = MibTable
trapRegTable = _TrapRegTable_Object(
    (1, 3, 6, 1, 3, 94, 2, 3)
)
if mibBuilder.loadTexts:
    trapRegTable.setStatus("mandatory")
_TrapRegEntry_Object = MibTableRow
trapRegEntry = _TrapRegEntry_Object(
    (1, 3, 6, 1, 3, 94, 2, 3, 1)
)
trapRegEntry.setIndexNames(
    (0, "FCMGMT-MIB", "trapRegIpAddress"),
    (0, "FCMGMT-MIB", "trapRegPort"),
)
if mibBuilder.loadTexts:
    trapRegEntry.setStatus("mandatory")
_TrapRegIpAddress_Type = IpAddress
_TrapRegIpAddress_Object = MibTableColumn
trapRegIpAddress = _TrapRegIpAddress_Object(
    (1, 3, 6, 1, 3, 94, 2, 3, 1, 1),
    _TrapRegIpAddress_Type()
)
trapRegIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRegIpAddress.setStatus("mandatory")


class _TrapRegPort_Type(Integer32):
    """Custom type trapRegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapRegPort_Type.__name__ = "Integer32"
_TrapRegPort_Object = MibTableColumn
trapRegPort = _TrapRegPort_Object(
    (1, 3, 6, 1, 3, 94, 2, 3, 1, 2),
    _TrapRegPort_Type()
)
trapRegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRegPort.setStatus("mandatory")
_TrapRegFilter_Type = FcEventSeverity
_TrapRegFilter_Object = MibTableColumn
trapRegFilter = _TrapRegFilter_Object(
    (1, 3, 6, 1, 3, 94, 2, 3, 1, 3),
    _TrapRegFilter_Type()
)
trapRegFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRegFilter.setStatus("mandatory")


class _TrapRegRowState_Type(Integer32):
    """Custom type trapRegRowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rowActive", 3),
          ("rowDestroy", 1),
          ("rowInactive", 2))
    )


_TrapRegRowState_Type.__name__ = "Integer32"
_TrapRegRowState_Object = MibTableColumn
trapRegRowState = _TrapRegRowState_Object(
    (1, 3, 6, 1, 3, 94, 2, 3, 1, 4),
    _TrapRegRowState_Type()
)
trapRegRowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRegRowState.setStatus("mandatory")


class _RevisionNumber_Type(DisplayString):
    """Custom type revisionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RevisionNumber_Type.__name__ = "DisplayString"
_RevisionNumber_Object = MibScalar
revisionNumber = _RevisionNumber_Object(
    (1, 3, 6, 1, 3, 94, 3),
    _RevisionNumber_Type()
)
revisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revisionNumber.setStatus("mandatory")
_StatSet_ObjectIdentity = ObjectIdentity
statSet = _StatSet_ObjectIdentity(
    (1, 3, 6, 1, 3, 94, 4)
)
_ConnUnitPortStatTable_Object = MibTable
connUnitPortStatTable = _ConnUnitPortStatTable_Object(
    (1, 3, 6, 1, 3, 94, 4, 5)
)
if mibBuilder.loadTexts:
    connUnitPortStatTable.setStatus("mandatory")
_ConnUnitPortStatEntry_Object = MibTableRow
connUnitPortStatEntry = _ConnUnitPortStatEntry_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1)
)
connUnitPortStatEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitPortStatUnitId"),
    (0, "FCMGMT-MIB", "connUnitPortStatIndex"),
)
if mibBuilder.loadTexts:
    connUnitPortStatEntry.setStatus("mandatory")
_ConnUnitPortStatUnitId_Type = FcGlobalId
_ConnUnitPortStatUnitId_Object = MibTableColumn
connUnitPortStatUnitId = _ConnUnitPortStatUnitId_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 1),
    _ConnUnitPortStatUnitId_Type()
)
connUnitPortStatUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatUnitId.setStatus("mandatory")


class _ConnUnitPortStatIndex_Type(Integer32):
    """Custom type connUnitPortStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnUnitPortStatIndex_Type.__name__ = "Integer32"
_ConnUnitPortStatIndex_Object = MibTableColumn
connUnitPortStatIndex = _ConnUnitPortStatIndex_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 2),
    _ConnUnitPortStatIndex_Type()
)
connUnitPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatIndex.setStatus("mandatory")


class _ConnUnitPortStatCountError_Type(OctetString):
    """Custom type connUnitPortStatCountError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountError_Type.__name__ = "OctetString"
_ConnUnitPortStatCountError_Object = MibTableColumn
connUnitPortStatCountError = _ConnUnitPortStatCountError_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 3),
    _ConnUnitPortStatCountError_Type()
)
connUnitPortStatCountError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountError.setStatus("mandatory")


class _ConnUnitPortStatCountTxObjects_Type(OctetString):
    """Custom type connUnitPortStatCountTxObjects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountTxObjects_Type.__name__ = "OctetString"
_ConnUnitPortStatCountTxObjects_Object = MibTableColumn
connUnitPortStatCountTxObjects = _ConnUnitPortStatCountTxObjects_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 4),
    _ConnUnitPortStatCountTxObjects_Type()
)
connUnitPortStatCountTxObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountTxObjects.setStatus("mandatory")


class _ConnUnitPortStatCountRxObjects_Type(OctetString):
    """Custom type connUnitPortStatCountRxObjects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountRxObjects_Type.__name__ = "OctetString"
_ConnUnitPortStatCountRxObjects_Object = MibTableColumn
connUnitPortStatCountRxObjects = _ConnUnitPortStatCountRxObjects_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 5),
    _ConnUnitPortStatCountRxObjects_Type()
)
connUnitPortStatCountRxObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountRxObjects.setStatus("mandatory")


class _ConnUnitPortStatCountTxElements_Type(OctetString):
    """Custom type connUnitPortStatCountTxElements based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountTxElements_Type.__name__ = "OctetString"
_ConnUnitPortStatCountTxElements_Object = MibTableColumn
connUnitPortStatCountTxElements = _ConnUnitPortStatCountTxElements_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 6),
    _ConnUnitPortStatCountTxElements_Type()
)
connUnitPortStatCountTxElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountTxElements.setStatus("mandatory")


class _ConnUnitPortStatCountRxElements_Type(OctetString):
    """Custom type connUnitPortStatCountRxElements based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountRxElements_Type.__name__ = "OctetString"
_ConnUnitPortStatCountRxElements_Object = MibTableColumn
connUnitPortStatCountRxElements = _ConnUnitPortStatCountRxElements_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 7),
    _ConnUnitPortStatCountRxElements_Type()
)
connUnitPortStatCountRxElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountRxElements.setStatus("mandatory")


class _ConnUnitPortStatCountBBCreditZero_Type(OctetString):
    """Custom type connUnitPortStatCountBBCreditZero based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountBBCreditZero_Type.__name__ = "OctetString"
_ConnUnitPortStatCountBBCreditZero_Object = MibTableColumn
connUnitPortStatCountBBCreditZero = _ConnUnitPortStatCountBBCreditZero_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 8),
    _ConnUnitPortStatCountBBCreditZero_Type()
)
connUnitPortStatCountBBCreditZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountBBCreditZero.setStatus("mandatory")


class _ConnUnitPortStatCountInputBuffersFull_Type(OctetString):
    """Custom type connUnitPortStatCountInputBuffersFull based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountInputBuffersFull_Type.__name__ = "OctetString"
_ConnUnitPortStatCountInputBuffersFull_Object = MibTableColumn
connUnitPortStatCountInputBuffersFull = _ConnUnitPortStatCountInputBuffersFull_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 9),
    _ConnUnitPortStatCountInputBuffersFull_Type()
)
connUnitPortStatCountInputBuffersFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountInputBuffersFull.setStatus("mandatory")


class _ConnUnitPortStatCountFBSYFrames_Type(OctetString):
    """Custom type connUnitPortStatCountFBSYFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountFBSYFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountFBSYFrames_Object = MibTableColumn
connUnitPortStatCountFBSYFrames = _ConnUnitPortStatCountFBSYFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 10),
    _ConnUnitPortStatCountFBSYFrames_Type()
)
connUnitPortStatCountFBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountFBSYFrames.setStatus("mandatory")


class _ConnUnitPortStatCountPBSYFrames_Type(OctetString):
    """Custom type connUnitPortStatCountPBSYFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountPBSYFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountPBSYFrames_Object = MibTableColumn
connUnitPortStatCountPBSYFrames = _ConnUnitPortStatCountPBSYFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 11),
    _ConnUnitPortStatCountPBSYFrames_Type()
)
connUnitPortStatCountPBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountPBSYFrames.setStatus("mandatory")


class _ConnUnitPortStatCountFRJTFrames_Type(OctetString):
    """Custom type connUnitPortStatCountFRJTFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountFRJTFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountFRJTFrames_Object = MibTableColumn
connUnitPortStatCountFRJTFrames = _ConnUnitPortStatCountFRJTFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 12),
    _ConnUnitPortStatCountFRJTFrames_Type()
)
connUnitPortStatCountFRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountFRJTFrames.setStatus("mandatory")


class _ConnUnitPortStatCountPRJTFrames_Type(OctetString):
    """Custom type connUnitPortStatCountPRJTFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountPRJTFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountPRJTFrames_Object = MibTableColumn
connUnitPortStatCountPRJTFrames = _ConnUnitPortStatCountPRJTFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 13),
    _ConnUnitPortStatCountPRJTFrames_Type()
)
connUnitPortStatCountPRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountPRJTFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass1RxFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass1RxFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass1RxFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass1RxFrames_Object = MibTableColumn
connUnitPortStatCountClass1RxFrames = _ConnUnitPortStatCountClass1RxFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 14),
    _ConnUnitPortStatCountClass1RxFrames_Type()
)
connUnitPortStatCountClass1RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass1RxFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass1TxFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass1TxFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass1TxFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass1TxFrames_Object = MibTableColumn
connUnitPortStatCountClass1TxFrames = _ConnUnitPortStatCountClass1TxFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 15),
    _ConnUnitPortStatCountClass1TxFrames_Type()
)
connUnitPortStatCountClass1TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass1TxFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass1FBSYFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass1FBSYFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass1FBSYFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass1FBSYFrames_Object = MibTableColumn
connUnitPortStatCountClass1FBSYFrames = _ConnUnitPortStatCountClass1FBSYFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 16),
    _ConnUnitPortStatCountClass1FBSYFrames_Type()
)
connUnitPortStatCountClass1FBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass1FBSYFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass1PBSYFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass1PBSYFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass1PBSYFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass1PBSYFrames_Object = MibTableColumn
connUnitPortStatCountClass1PBSYFrames = _ConnUnitPortStatCountClass1PBSYFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 17),
    _ConnUnitPortStatCountClass1PBSYFrames_Type()
)
connUnitPortStatCountClass1PBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass1PBSYFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass1FRJTFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass1FRJTFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass1FRJTFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass1FRJTFrames_Object = MibTableColumn
connUnitPortStatCountClass1FRJTFrames = _ConnUnitPortStatCountClass1FRJTFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 18),
    _ConnUnitPortStatCountClass1FRJTFrames_Type()
)
connUnitPortStatCountClass1FRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass1FRJTFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass1PRJTFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass1PRJTFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass1PRJTFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass1PRJTFrames_Object = MibTableColumn
connUnitPortStatCountClass1PRJTFrames = _ConnUnitPortStatCountClass1PRJTFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 19),
    _ConnUnitPortStatCountClass1PRJTFrames_Type()
)
connUnitPortStatCountClass1PRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass1PRJTFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass2RxFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass2RxFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass2RxFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass2RxFrames_Object = MibTableColumn
connUnitPortStatCountClass2RxFrames = _ConnUnitPortStatCountClass2RxFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 20),
    _ConnUnitPortStatCountClass2RxFrames_Type()
)
connUnitPortStatCountClass2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass2RxFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass2TxFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass2TxFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass2TxFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass2TxFrames_Object = MibTableColumn
connUnitPortStatCountClass2TxFrames = _ConnUnitPortStatCountClass2TxFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 21),
    _ConnUnitPortStatCountClass2TxFrames_Type()
)
connUnitPortStatCountClass2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass2TxFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass2FBSYFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass2FBSYFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass2FBSYFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass2FBSYFrames_Object = MibTableColumn
connUnitPortStatCountClass2FBSYFrames = _ConnUnitPortStatCountClass2FBSYFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 22),
    _ConnUnitPortStatCountClass2FBSYFrames_Type()
)
connUnitPortStatCountClass2FBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass2FBSYFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass2PBSYFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass2PBSYFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass2PBSYFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass2PBSYFrames_Object = MibTableColumn
connUnitPortStatCountClass2PBSYFrames = _ConnUnitPortStatCountClass2PBSYFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 23),
    _ConnUnitPortStatCountClass2PBSYFrames_Type()
)
connUnitPortStatCountClass2PBSYFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass2PBSYFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass2FRJTFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass2FRJTFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass2FRJTFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass2FRJTFrames_Object = MibTableColumn
connUnitPortStatCountClass2FRJTFrames = _ConnUnitPortStatCountClass2FRJTFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 24),
    _ConnUnitPortStatCountClass2FRJTFrames_Type()
)
connUnitPortStatCountClass2FRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass2FRJTFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass2PRJTFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass2PRJTFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass2PRJTFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass2PRJTFrames_Object = MibTableColumn
connUnitPortStatCountClass2PRJTFrames = _ConnUnitPortStatCountClass2PRJTFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 25),
    _ConnUnitPortStatCountClass2PRJTFrames_Type()
)
connUnitPortStatCountClass2PRJTFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass2PRJTFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass3RxFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass3RxFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass3RxFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass3RxFrames_Object = MibTableColumn
connUnitPortStatCountClass3RxFrames = _ConnUnitPortStatCountClass3RxFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 26),
    _ConnUnitPortStatCountClass3RxFrames_Type()
)
connUnitPortStatCountClass3RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass3RxFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass3TxFrames_Type(OctetString):
    """Custom type connUnitPortStatCountClass3TxFrames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass3TxFrames_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass3TxFrames_Object = MibTableColumn
connUnitPortStatCountClass3TxFrames = _ConnUnitPortStatCountClass3TxFrames_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 27),
    _ConnUnitPortStatCountClass3TxFrames_Type()
)
connUnitPortStatCountClass3TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass3TxFrames.setStatus("mandatory")


class _ConnUnitPortStatCountClass3Discards_Type(OctetString):
    """Custom type connUnitPortStatCountClass3Discards based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountClass3Discards_Type.__name__ = "OctetString"
_ConnUnitPortStatCountClass3Discards_Object = MibTableColumn
connUnitPortStatCountClass3Discards = _ConnUnitPortStatCountClass3Discards_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 28),
    _ConnUnitPortStatCountClass3Discards_Type()
)
connUnitPortStatCountClass3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountClass3Discards.setStatus("mandatory")


class _ConnUnitPortStatCountRxMulticastObjects_Type(OctetString):
    """Custom type connUnitPortStatCountRxMulticastObjects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountRxMulticastObjects_Type.__name__ = "OctetString"
_ConnUnitPortStatCountRxMulticastObjects_Object = MibTableColumn
connUnitPortStatCountRxMulticastObjects = _ConnUnitPortStatCountRxMulticastObjects_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 29),
    _ConnUnitPortStatCountRxMulticastObjects_Type()
)
connUnitPortStatCountRxMulticastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountRxMulticastObjects.setStatus("mandatory")


class _ConnUnitPortStatCountTxMulticastObjects_Type(OctetString):
    """Custom type connUnitPortStatCountTxMulticastObjects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountTxMulticastObjects_Type.__name__ = "OctetString"
_ConnUnitPortStatCountTxMulticastObjects_Object = MibTableColumn
connUnitPortStatCountTxMulticastObjects = _ConnUnitPortStatCountTxMulticastObjects_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 30),
    _ConnUnitPortStatCountTxMulticastObjects_Type()
)
connUnitPortStatCountTxMulticastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountTxMulticastObjects.setStatus("mandatory")


class _ConnUnitPortStatCountRxBroadcastObjects_Type(OctetString):
    """Custom type connUnitPortStatCountRxBroadcastObjects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountRxBroadcastObjects_Type.__name__ = "OctetString"
_ConnUnitPortStatCountRxBroadcastObjects_Object = MibTableColumn
connUnitPortStatCountRxBroadcastObjects = _ConnUnitPortStatCountRxBroadcastObjects_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 31),
    _ConnUnitPortStatCountRxBroadcastObjects_Type()
)
connUnitPortStatCountRxBroadcastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountRxBroadcastObjects.setStatus("mandatory")


class _ConnUnitPortStatCountTxBroadcastObjects_Type(OctetString):
    """Custom type connUnitPortStatCountTxBroadcastObjects based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountTxBroadcastObjects_Type.__name__ = "OctetString"
_ConnUnitPortStatCountTxBroadcastObjects_Object = MibTableColumn
connUnitPortStatCountTxBroadcastObjects = _ConnUnitPortStatCountTxBroadcastObjects_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 32),
    _ConnUnitPortStatCountTxBroadcastObjects_Type()
)
connUnitPortStatCountTxBroadcastObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountTxBroadcastObjects.setStatus("mandatory")


class _ConnUnitPortStatCountRxLinkResets_Type(OctetString):
    """Custom type connUnitPortStatCountRxLinkResets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountRxLinkResets_Type.__name__ = "OctetString"
_ConnUnitPortStatCountRxLinkResets_Object = MibTableColumn
connUnitPortStatCountRxLinkResets = _ConnUnitPortStatCountRxLinkResets_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 33),
    _ConnUnitPortStatCountRxLinkResets_Type()
)
connUnitPortStatCountRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountRxLinkResets.setStatus("mandatory")


class _ConnUnitPortStatCountTxLinkResets_Type(OctetString):
    """Custom type connUnitPortStatCountTxLinkResets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountTxLinkResets_Type.__name__ = "OctetString"
_ConnUnitPortStatCountTxLinkResets_Object = MibTableColumn
connUnitPortStatCountTxLinkResets = _ConnUnitPortStatCountTxLinkResets_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 34),
    _ConnUnitPortStatCountTxLinkResets_Type()
)
connUnitPortStatCountTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountTxLinkResets.setStatus("mandatory")


class _ConnUnitPortStatCountNumberLinkResets_Type(OctetString):
    """Custom type connUnitPortStatCountNumberLinkResets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountNumberLinkResets_Type.__name__ = "OctetString"
_ConnUnitPortStatCountNumberLinkResets_Object = MibTableColumn
connUnitPortStatCountNumberLinkResets = _ConnUnitPortStatCountNumberLinkResets_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 35),
    _ConnUnitPortStatCountNumberLinkResets_Type()
)
connUnitPortStatCountNumberLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountNumberLinkResets.setStatus("mandatory")


class _ConnUnitPortStatCountRxOfflineSequences_Type(OctetString):
    """Custom type connUnitPortStatCountRxOfflineSequences based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountRxOfflineSequences_Type.__name__ = "OctetString"
_ConnUnitPortStatCountRxOfflineSequences_Object = MibTableColumn
connUnitPortStatCountRxOfflineSequences = _ConnUnitPortStatCountRxOfflineSequences_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 36),
    _ConnUnitPortStatCountRxOfflineSequences_Type()
)
connUnitPortStatCountRxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountRxOfflineSequences.setStatus("mandatory")


class _ConnUnitPortStatCountTxOfflineSequences_Type(OctetString):
    """Custom type connUnitPortStatCountTxOfflineSequences based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountTxOfflineSequences_Type.__name__ = "OctetString"
_ConnUnitPortStatCountTxOfflineSequences_Object = MibTableColumn
connUnitPortStatCountTxOfflineSequences = _ConnUnitPortStatCountTxOfflineSequences_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 37),
    _ConnUnitPortStatCountTxOfflineSequences_Type()
)
connUnitPortStatCountTxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountTxOfflineSequences.setStatus("mandatory")


class _ConnUnitPortStatCountNumberOfflineSequences_Type(OctetString):
    """Custom type connUnitPortStatCountNumberOfflineSequences based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountNumberOfflineSequences_Type.__name__ = "OctetString"
_ConnUnitPortStatCountNumberOfflineSequences_Object = MibTableColumn
connUnitPortStatCountNumberOfflineSequences = _ConnUnitPortStatCountNumberOfflineSequences_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 38),
    _ConnUnitPortStatCountNumberOfflineSequences_Type()
)
connUnitPortStatCountNumberOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountNumberOfflineSequences.setStatus("mandatory")


class _ConnUnitPortStatCountLinkFailures_Type(OctetString):
    """Custom type connUnitPortStatCountLinkFailures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountLinkFailures_Type.__name__ = "OctetString"
_ConnUnitPortStatCountLinkFailures_Object = MibTableColumn
connUnitPortStatCountLinkFailures = _ConnUnitPortStatCountLinkFailures_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 39),
    _ConnUnitPortStatCountLinkFailures_Type()
)
connUnitPortStatCountLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountLinkFailures.setStatus("mandatory")


class _ConnUnitPortStatCountInvalidCRC_Type(OctetString):
    """Custom type connUnitPortStatCountInvalidCRC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountInvalidCRC_Type.__name__ = "OctetString"
_ConnUnitPortStatCountInvalidCRC_Object = MibTableColumn
connUnitPortStatCountInvalidCRC = _ConnUnitPortStatCountInvalidCRC_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 40),
    _ConnUnitPortStatCountInvalidCRC_Type()
)
connUnitPortStatCountInvalidCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountInvalidCRC.setStatus("mandatory")


class _ConnUnitPortStatCountInvalidTxWords_Type(OctetString):
    """Custom type connUnitPortStatCountInvalidTxWords based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountInvalidTxWords_Type.__name__ = "OctetString"
_ConnUnitPortStatCountInvalidTxWords_Object = MibTableColumn
connUnitPortStatCountInvalidTxWords = _ConnUnitPortStatCountInvalidTxWords_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 41),
    _ConnUnitPortStatCountInvalidTxWords_Type()
)
connUnitPortStatCountInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountInvalidTxWords.setStatus("mandatory")


class _ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Type(OctetString):
    """Custom type connUnitPortStatCountPrimitiveSequenceProtocolErrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Type.__name__ = "OctetString"
_ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Object = MibTableColumn
connUnitPortStatCountPrimitiveSequenceProtocolErrors = _ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 42),
    _ConnUnitPortStatCountPrimitiveSequenceProtocolErrors_Type()
)
connUnitPortStatCountPrimitiveSequenceProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountPrimitiveSequenceProtocolErrors.setStatus("mandatory")


class _ConnUnitPortStatCountLossofSignal_Type(OctetString):
    """Custom type connUnitPortStatCountLossofSignal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountLossofSignal_Type.__name__ = "OctetString"
_ConnUnitPortStatCountLossofSignal_Object = MibTableColumn
connUnitPortStatCountLossofSignal = _ConnUnitPortStatCountLossofSignal_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 43),
    _ConnUnitPortStatCountLossofSignal_Type()
)
connUnitPortStatCountLossofSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountLossofSignal.setStatus("mandatory")


class _ConnUnitPortStatCountLossofSynchronization_Type(OctetString):
    """Custom type connUnitPortStatCountLossofSynchronization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountLossofSynchronization_Type.__name__ = "OctetString"
_ConnUnitPortStatCountLossofSynchronization_Object = MibTableColumn
connUnitPortStatCountLossofSynchronization = _ConnUnitPortStatCountLossofSynchronization_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 44),
    _ConnUnitPortStatCountLossofSynchronization_Type()
)
connUnitPortStatCountLossofSynchronization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountLossofSynchronization.setStatus("mandatory")


class _ConnUnitPortStatCountInvalidOrderedSets_Type(OctetString):
    """Custom type connUnitPortStatCountInvalidOrderedSets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountInvalidOrderedSets_Type.__name__ = "OctetString"
_ConnUnitPortStatCountInvalidOrderedSets_Object = MibTableColumn
connUnitPortStatCountInvalidOrderedSets = _ConnUnitPortStatCountInvalidOrderedSets_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 45),
    _ConnUnitPortStatCountInvalidOrderedSets_Type()
)
connUnitPortStatCountInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountInvalidOrderedSets.setStatus("mandatory")


class _ConnUnitPortStatCountFramesTooLong_Type(OctetString):
    """Custom type connUnitPortStatCountFramesTooLong based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountFramesTooLong_Type.__name__ = "OctetString"
_ConnUnitPortStatCountFramesTooLong_Object = MibTableColumn
connUnitPortStatCountFramesTooLong = _ConnUnitPortStatCountFramesTooLong_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 46),
    _ConnUnitPortStatCountFramesTooLong_Type()
)
connUnitPortStatCountFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountFramesTooLong.setStatus("mandatory")


class _ConnUnitPortStatCountFramesTruncated_Type(OctetString):
    """Custom type connUnitPortStatCountFramesTruncated based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountFramesTruncated_Type.__name__ = "OctetString"
_ConnUnitPortStatCountFramesTruncated_Object = MibTableColumn
connUnitPortStatCountFramesTruncated = _ConnUnitPortStatCountFramesTruncated_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 47),
    _ConnUnitPortStatCountFramesTruncated_Type()
)
connUnitPortStatCountFramesTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountFramesTruncated.setStatus("mandatory")


class _ConnUnitPortStatCountAddressErrors_Type(OctetString):
    """Custom type connUnitPortStatCountAddressErrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountAddressErrors_Type.__name__ = "OctetString"
_ConnUnitPortStatCountAddressErrors_Object = MibTableColumn
connUnitPortStatCountAddressErrors = _ConnUnitPortStatCountAddressErrors_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 48),
    _ConnUnitPortStatCountAddressErrors_Type()
)
connUnitPortStatCountAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountAddressErrors.setStatus("mandatory")


class _ConnUnitPortStatCountDelimiterErrors_Type(OctetString):
    """Custom type connUnitPortStatCountDelimiterErrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountDelimiterErrors_Type.__name__ = "OctetString"
_ConnUnitPortStatCountDelimiterErrors_Object = MibTableColumn
connUnitPortStatCountDelimiterErrors = _ConnUnitPortStatCountDelimiterErrors_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 49),
    _ConnUnitPortStatCountDelimiterErrors_Type()
)
connUnitPortStatCountDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountDelimiterErrors.setStatus("mandatory")


class _ConnUnitPortStatCountEncodingDisparityErrors_Type(OctetString):
    """Custom type connUnitPortStatCountEncodingDisparityErrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConnUnitPortStatCountEncodingDisparityErrors_Type.__name__ = "OctetString"
_ConnUnitPortStatCountEncodingDisparityErrors_Object = MibTableColumn
connUnitPortStatCountEncodingDisparityErrors = _ConnUnitPortStatCountEncodingDisparityErrors_Object(
    (1, 3, 6, 1, 3, 94, 4, 5, 1, 50),
    _ConnUnitPortStatCountEncodingDisparityErrors_Type()
)
connUnitPortStatCountEncodingDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitPortStatCountEncodingDisparityErrors.setStatus("mandatory")
_ConnUnitServiceSet_ObjectIdentity = ObjectIdentity
connUnitServiceSet = _ConnUnitServiceSet_ObjectIdentity(
    (1, 3, 6, 1, 3, 94, 5)
)
_ConnUnitServiceScalars_ObjectIdentity = ObjectIdentity
connUnitServiceScalars = _ConnUnitServiceScalars_ObjectIdentity(
    (1, 3, 6, 1, 3, 94, 5, 1)
)
_ConnUnitSnsMaxEntry_Type = Integer32
_ConnUnitSnsMaxEntry_Object = MibScalar
connUnitSnsMaxEntry = _ConnUnitSnsMaxEntry_Object(
    (1, 3, 6, 1, 3, 94, 5, 1, 1),
    _ConnUnitSnsMaxEntry_Type()
)
connUnitSnsMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsMaxEntry.setStatus("mandatory")
_ConnUnitServiceTables_ObjectIdentity = ObjectIdentity
connUnitServiceTables = _ConnUnitServiceTables_ObjectIdentity(
    (1, 3, 6, 1, 3, 94, 5, 2)
)
_ConnUnitSnsTable_Object = MibTable
connUnitSnsTable = _ConnUnitSnsTable_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1)
)
if mibBuilder.loadTexts:
    connUnitSnsTable.setStatus("mandatory")
_ConnUnitSnsEntry_Object = MibTableRow
connUnitSnsEntry = _ConnUnitSnsEntry_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1)
)
connUnitSnsEntry.setIndexNames(
    (0, "FCMGMT-MIB", "connUnitSnsId"),
    (0, "FCMGMT-MIB", "connUnitSnsPortIndex"),
    (0, "FCMGMT-MIB", "connUnitSnsPortIdentifier"),
)
if mibBuilder.loadTexts:
    connUnitSnsEntry.setStatus("mandatory")


class _ConnUnitSnsId_Type(OctetString):
    """Custom type connUnitSnsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitSnsId_Type.__name__ = "OctetString"
_ConnUnitSnsId_Object = MibTableColumn
connUnitSnsId = _ConnUnitSnsId_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 1),
    _ConnUnitSnsId_Type()
)
connUnitSnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsId.setStatus("mandatory")
_ConnUnitSnsPortIndex_Type = Integer32
_ConnUnitSnsPortIndex_Object = MibTableColumn
connUnitSnsPortIndex = _ConnUnitSnsPortIndex_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 2),
    _ConnUnitSnsPortIndex_Type()
)
connUnitSnsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsPortIndex.setStatus("mandatory")
_ConnUnitSnsPortIdentifier_Type = FcAddressId
_ConnUnitSnsPortIdentifier_Object = MibTableColumn
connUnitSnsPortIdentifier = _ConnUnitSnsPortIdentifier_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 3),
    _ConnUnitSnsPortIdentifier_Type()
)
connUnitSnsPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsPortIdentifier.setStatus("mandatory")
_ConnUnitSnsPortName_Type = FcNameId
_ConnUnitSnsPortName_Object = MibTableColumn
connUnitSnsPortName = _ConnUnitSnsPortName_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 4),
    _ConnUnitSnsPortName_Type()
)
connUnitSnsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsPortName.setStatus("mandatory")
_ConnUnitSnsNodeName_Type = FcNameId
_ConnUnitSnsNodeName_Object = MibTableColumn
connUnitSnsNodeName = _ConnUnitSnsNodeName_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 5),
    _ConnUnitSnsNodeName_Type()
)
connUnitSnsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsNodeName.setStatus("mandatory")


class _ConnUnitSnsClassOfSvc_Type(OctetString):
    """Custom type connUnitSnsClassOfSvc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ConnUnitSnsClassOfSvc_Type.__name__ = "OctetString"
_ConnUnitSnsClassOfSvc_Object = MibTableColumn
connUnitSnsClassOfSvc = _ConnUnitSnsClassOfSvc_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 6),
    _ConnUnitSnsClassOfSvc_Type()
)
connUnitSnsClassOfSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsClassOfSvc.setStatus("mandatory")


class _ConnUnitSnsNodeIPAddress_Type(OctetString):
    """Custom type connUnitSnsNodeIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitSnsNodeIPAddress_Type.__name__ = "OctetString"
_ConnUnitSnsNodeIPAddress_Object = MibTableColumn
connUnitSnsNodeIPAddress = _ConnUnitSnsNodeIPAddress_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 7),
    _ConnUnitSnsNodeIPAddress_Type()
)
connUnitSnsNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsNodeIPAddress.setStatus("mandatory")


class _ConnUnitSnsProcAssoc_Type(OctetString):
    """Custom type connUnitSnsProcAssoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ConnUnitSnsProcAssoc_Type.__name__ = "OctetString"
_ConnUnitSnsProcAssoc_Object = MibTableColumn
connUnitSnsProcAssoc = _ConnUnitSnsProcAssoc_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 8),
    _ConnUnitSnsProcAssoc_Type()
)
connUnitSnsProcAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsProcAssoc.setStatus("mandatory")


class _ConnUnitSnsFC4Type_Type(OctetString):
    """Custom type connUnitSnsFC4Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ConnUnitSnsFC4Type_Type.__name__ = "OctetString"
_ConnUnitSnsFC4Type_Object = MibTableColumn
connUnitSnsFC4Type = _ConnUnitSnsFC4Type_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 9),
    _ConnUnitSnsFC4Type_Type()
)
connUnitSnsFC4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsFC4Type.setStatus("mandatory")


class _ConnUnitSnsPortType_Type(OctetString):
    """Custom type connUnitSnsPortType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ConnUnitSnsPortType_Type.__name__ = "OctetString"
_ConnUnitSnsPortType_Object = MibTableColumn
connUnitSnsPortType = _ConnUnitSnsPortType_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 10),
    _ConnUnitSnsPortType_Type()
)
connUnitSnsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsPortType.setStatus("mandatory")


class _ConnUnitSnsPortIPAddress_Type(OctetString):
    """Custom type connUnitSnsPortIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ConnUnitSnsPortIPAddress_Type.__name__ = "OctetString"
_ConnUnitSnsPortIPAddress_Object = MibTableColumn
connUnitSnsPortIPAddress = _ConnUnitSnsPortIPAddress_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 11),
    _ConnUnitSnsPortIPAddress_Type()
)
connUnitSnsPortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsPortIPAddress.setStatus("mandatory")
_ConnUnitSnsFabricPortName_Type = FcNameId
_ConnUnitSnsFabricPortName_Object = MibTableColumn
connUnitSnsFabricPortName = _ConnUnitSnsFabricPortName_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 12),
    _ConnUnitSnsFabricPortName_Type()
)
connUnitSnsFabricPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsFabricPortName.setStatus("mandatory")
_ConnUnitSnsHardAddress_Type = FcAddressId
_ConnUnitSnsHardAddress_Object = MibTableColumn
connUnitSnsHardAddress = _ConnUnitSnsHardAddress_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 13),
    _ConnUnitSnsHardAddress_Type()
)
connUnitSnsHardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsHardAddress.setStatus("mandatory")


class _ConnUnitSnsSymbolicPortName_Type(DisplayString):
    """Custom type connUnitSnsSymbolicPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitSnsSymbolicPortName_Type.__name__ = "DisplayString"
_ConnUnitSnsSymbolicPortName_Object = MibTableColumn
connUnitSnsSymbolicPortName = _ConnUnitSnsSymbolicPortName_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 14),
    _ConnUnitSnsSymbolicPortName_Type()
)
connUnitSnsSymbolicPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsSymbolicPortName.setStatus("mandatory")


class _ConnUnitSnsSymbolicNodeName_Type(DisplayString):
    """Custom type connUnitSnsSymbolicNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ConnUnitSnsSymbolicNodeName_Type.__name__ = "DisplayString"
_ConnUnitSnsSymbolicNodeName_Object = MibTableColumn
connUnitSnsSymbolicNodeName = _ConnUnitSnsSymbolicNodeName_Object(
    (1, 3, 6, 1, 3, 94, 5, 2, 1, 1, 15),
    _ConnUnitSnsSymbolicNodeName_Type()
)
connUnitSnsSymbolicNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connUnitSnsSymbolicNodeName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

connUnitStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 94, 0, 1)
)
connUnitStatusChange.setObjects(
      *(("FCMGMT-MIB", "connUnitStatus"),
        ("FCMGMT-MIB", "connUnitState"))
)
if mibBuilder.loadTexts:
    connUnitStatusChange.setStatus(
        ""
    )

connUnitDeletedTrap = NotificationType(
    (1, 3, 6, 1, 3, 94, 0, 3)
)
connUnitDeletedTrap.setObjects(
    ("FCMGMT-MIB", "connUnitId")
)
if mibBuilder.loadTexts:
    connUnitDeletedTrap.setStatus(
        ""
    )

connUnitEventTrap = NotificationType(
    (1, 3, 6, 1, 3, 94, 0, 4)
)
connUnitEventTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventObject"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    connUnitEventTrap.setStatus(
        ""
    )

connUnitSensorStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 94, 0, 5)
)
connUnitSensorStatusChange.setObjects(
    ("FCMGMT-MIB", "connUnitSensorStatus")
)
if mibBuilder.loadTexts:
    connUnitSensorStatusChange.setStatus(
        ""
    )

connUnitPortStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 94, 0, 6)
)
connUnitPortStatusChange.setObjects(
      *(("FCMGMT-MIB", "connUnitPortStatus"),
        ("FCMGMT-MIB", "connUnitPortState"))
)
if mibBuilder.loadTexts:
    connUnitPortStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FCMGMT-MIB",
    **{"FcNameId": FcNameId,
       "FcGlobalId": FcGlobalId,
       "FcAddressId": FcAddressId,
       "FcEventSeverity": FcEventSeverity,
       "FcUnitType": FcUnitType,
       "fcmgmt": fcmgmt,
       "connUnitStatusChange": connUnitStatusChange,
       "connUnitDeletedTrap": connUnitDeletedTrap,
       "connUnitEventTrap": connUnitEventTrap,
       "connUnitSensorStatusChange": connUnitSensorStatusChange,
       "connUnitPortStatusChange": connUnitPortStatusChange,
       "connSet": connSet,
       "uNumber": uNumber,
       "systemURL": systemURL,
       "statusChangeTime": statusChangeTime,
       "configurationChangeTime": configurationChangeTime,
       "connUnitTableChangeTime": connUnitTableChangeTime,
       "connUnitTable": connUnitTable,
       "connUnitEntry": connUnitEntry,
       "connUnitId": connUnitId,
       "connUnitGlobalId": connUnitGlobalId,
       "connUnitType": connUnitType,
       "connUnitNumports": connUnitNumports,
       "connUnitState": connUnitState,
       "connUnitStatus": connUnitStatus,
       "connUnitProduct": connUnitProduct,
       "connUnitSn": connUnitSn,
       "connUnitUpTime": connUnitUpTime,
       "connUnitUrl": connUnitUrl,
       "connUnitDomainId": connUnitDomainId,
       "connUnitProxyMaster": connUnitProxyMaster,
       "connUnitPrincipal": connUnitPrincipal,
       "connUnitNumSensors": connUnitNumSensors,
       "connUnitStatusChangeTime": connUnitStatusChangeTime,
       "connUnitConfigurationChangeTime": connUnitConfigurationChangeTime,
       "connUnitNumRevs": connUnitNumRevs,
       "connUnitNumZones": connUnitNumZones,
       "connUnitModuleId": connUnitModuleId,
       "connUnitName": connUnitName,
       "connUnitInfo": connUnitInfo,
       "connUnitControl": connUnitControl,
       "connUnitContact": connUnitContact,
       "connUnitLocation": connUnitLocation,
       "connUnitEventFilter": connUnitEventFilter,
       "connUnitNumEvents": connUnitNumEvents,
       "connUnitMaxEvents": connUnitMaxEvents,
       "connUnitEventCurrID": connUnitEventCurrID,
       "connUnitRevsTable": connUnitRevsTable,
       "connUnitRevsEntry": connUnitRevsEntry,
       "connUnitRevsUnitId": connUnitRevsUnitId,
       "connUnitRevsIndex": connUnitRevsIndex,
       "connUnitRevsRevId": connUnitRevsRevId,
       "connUnitRevsDescription": connUnitRevsDescription,
       "connUnitSensorTable": connUnitSensorTable,
       "connUnitSensorEntry": connUnitSensorEntry,
       "connUnitSensorUnitId": connUnitSensorUnitId,
       "connUnitSensorIndex": connUnitSensorIndex,
       "connUnitSensorName": connUnitSensorName,
       "connUnitSensorStatus": connUnitSensorStatus,
       "connUnitSensorInfo": connUnitSensorInfo,
       "connUnitSensorMessage": connUnitSensorMessage,
       "connUnitSensorType": connUnitSensorType,
       "connUnitSensorCharacteristic": connUnitSensorCharacteristic,
       "connUnitPortTable": connUnitPortTable,
       "connUnitPortEntry": connUnitPortEntry,
       "connUnitPortUnitId": connUnitPortUnitId,
       "connUnitPortIndex": connUnitPortIndex,
       "connUnitPortType": connUnitPortType,
       "connUnitPortFCClassCap": connUnitPortFCClassCap,
       "connUnitPortFCClassOp": connUnitPortFCClassOp,
       "connUnitPortState": connUnitPortState,
       "connUnitPortStatus": connUnitPortStatus,
       "connUnitPortTransmitterType": connUnitPortTransmitterType,
       "connUnitPortModuleType": connUnitPortModuleType,
       "connUnitPortWwn": connUnitPortWwn,
       "connUnitPortFCId": connUnitPortFCId,
       "connUnitPortSn": connUnitPortSn,
       "connUnitPortRevision": connUnitPortRevision,
       "connUnitPortVendor": connUnitPortVendor,
       "connUnitPortSpeed": connUnitPortSpeed,
       "connUnitPortControl": connUnitPortControl,
       "connUnitPortName": connUnitPortName,
       "connUnitPortPhysicalNumber": connUnitPortPhysicalNumber,
       "connUnitPortStatObject": connUnitPortStatObject,
       "connUnitPortProtocolCap": connUnitPortProtocolCap,
       "connUnitPortProtocolOp": connUnitPortProtocolOp,
       "connUnitPortNodeWwn": connUnitPortNodeWwn,
       "connUnitPortHWState": connUnitPortHWState,
       "connUnitEventTable": connUnitEventTable,
       "connUnitEventEntry": connUnitEventEntry,
       "connUnitEventUnitId": connUnitEventUnitId,
       "connUnitEventIndex": connUnitEventIndex,
       "connUnitEventId": connUnitEventId,
       "connUnitREventTime": connUnitREventTime,
       "connUnitSEventTime": connUnitSEventTime,
       "connUnitEventSeverity": connUnitEventSeverity,
       "connUnitEventType": connUnitEventType,
       "connUnitEventObject": connUnitEventObject,
       "connUnitEventDescr": connUnitEventDescr,
       "connUnitLinkTable": connUnitLinkTable,
       "connUnitLinkEntry": connUnitLinkEntry,
       "connUnitLinkUnitId": connUnitLinkUnitId,
       "connUnitLinkIndex": connUnitLinkIndex,
       "connUnitLinkNodeIdX": connUnitLinkNodeIdX,
       "connUnitLinkPortNumberX": connUnitLinkPortNumberX,
       "connUnitLinkPortWwnX": connUnitLinkPortWwnX,
       "connUnitLinkNodeIdY": connUnitLinkNodeIdY,
       "connUnitLinkPortNumberY": connUnitLinkPortNumberY,
       "connUnitLinkPortWwnY": connUnitLinkPortWwnY,
       "connUnitLinkAgentAddressY": connUnitLinkAgentAddressY,
       "connUnitLinkAgentAddressTypeY": connUnitLinkAgentAddressTypeY,
       "connUnitLinkAgentPortY": connUnitLinkAgentPortY,
       "connUnitLinkUnitTypeY": connUnitLinkUnitTypeY,
       "connUnitLinkConnIdY": connUnitLinkConnIdY,
       "connUnitLinkCurrIndex": connUnitLinkCurrIndex,
       "trapReg": trapReg,
       "trapMaxClients": trapMaxClients,
       "trapClientCount": trapClientCount,
       "trapRegTable": trapRegTable,
       "trapRegEntry": trapRegEntry,
       "trapRegIpAddress": trapRegIpAddress,
       "trapRegPort": trapRegPort,
       "trapRegFilter": trapRegFilter,
       "trapRegRowState": trapRegRowState,
       "revisionNumber": revisionNumber,
       "statSet": statSet,
       "connUnitPortStatTable": connUnitPortStatTable,
       "connUnitPortStatEntry": connUnitPortStatEntry,
       "connUnitPortStatUnitId": connUnitPortStatUnitId,
       "connUnitPortStatIndex": connUnitPortStatIndex,
       "connUnitPortStatCountError": connUnitPortStatCountError,
       "connUnitPortStatCountTxObjects": connUnitPortStatCountTxObjects,
       "connUnitPortStatCountRxObjects": connUnitPortStatCountRxObjects,
       "connUnitPortStatCountTxElements": connUnitPortStatCountTxElements,
       "connUnitPortStatCountRxElements": connUnitPortStatCountRxElements,
       "connUnitPortStatCountBBCreditZero": connUnitPortStatCountBBCreditZero,
       "connUnitPortStatCountInputBuffersFull": connUnitPortStatCountInputBuffersFull,
       "connUnitPortStatCountFBSYFrames": connUnitPortStatCountFBSYFrames,
       "connUnitPortStatCountPBSYFrames": connUnitPortStatCountPBSYFrames,
       "connUnitPortStatCountFRJTFrames": connUnitPortStatCountFRJTFrames,
       "connUnitPortStatCountPRJTFrames": connUnitPortStatCountPRJTFrames,
       "connUnitPortStatCountClass1RxFrames": connUnitPortStatCountClass1RxFrames,
       "connUnitPortStatCountClass1TxFrames": connUnitPortStatCountClass1TxFrames,
       "connUnitPortStatCountClass1FBSYFrames": connUnitPortStatCountClass1FBSYFrames,
       "connUnitPortStatCountClass1PBSYFrames": connUnitPortStatCountClass1PBSYFrames,
       "connUnitPortStatCountClass1FRJTFrames": connUnitPortStatCountClass1FRJTFrames,
       "connUnitPortStatCountClass1PRJTFrames": connUnitPortStatCountClass1PRJTFrames,
       "connUnitPortStatCountClass2RxFrames": connUnitPortStatCountClass2RxFrames,
       "connUnitPortStatCountClass2TxFrames": connUnitPortStatCountClass2TxFrames,
       "connUnitPortStatCountClass2FBSYFrames": connUnitPortStatCountClass2FBSYFrames,
       "connUnitPortStatCountClass2PBSYFrames": connUnitPortStatCountClass2PBSYFrames,
       "connUnitPortStatCountClass2FRJTFrames": connUnitPortStatCountClass2FRJTFrames,
       "connUnitPortStatCountClass2PRJTFrames": connUnitPortStatCountClass2PRJTFrames,
       "connUnitPortStatCountClass3RxFrames": connUnitPortStatCountClass3RxFrames,
       "connUnitPortStatCountClass3TxFrames": connUnitPortStatCountClass3TxFrames,
       "connUnitPortStatCountClass3Discards": connUnitPortStatCountClass3Discards,
       "connUnitPortStatCountRxMulticastObjects": connUnitPortStatCountRxMulticastObjects,
       "connUnitPortStatCountTxMulticastObjects": connUnitPortStatCountTxMulticastObjects,
       "connUnitPortStatCountRxBroadcastObjects": connUnitPortStatCountRxBroadcastObjects,
       "connUnitPortStatCountTxBroadcastObjects": connUnitPortStatCountTxBroadcastObjects,
       "connUnitPortStatCountRxLinkResets": connUnitPortStatCountRxLinkResets,
       "connUnitPortStatCountTxLinkResets": connUnitPortStatCountTxLinkResets,
       "connUnitPortStatCountNumberLinkResets": connUnitPortStatCountNumberLinkResets,
       "connUnitPortStatCountRxOfflineSequences": connUnitPortStatCountRxOfflineSequences,
       "connUnitPortStatCountTxOfflineSequences": connUnitPortStatCountTxOfflineSequences,
       "connUnitPortStatCountNumberOfflineSequences": connUnitPortStatCountNumberOfflineSequences,
       "connUnitPortStatCountLinkFailures": connUnitPortStatCountLinkFailures,
       "connUnitPortStatCountInvalidCRC": connUnitPortStatCountInvalidCRC,
       "connUnitPortStatCountInvalidTxWords": connUnitPortStatCountInvalidTxWords,
       "connUnitPortStatCountPrimitiveSequenceProtocolErrors": connUnitPortStatCountPrimitiveSequenceProtocolErrors,
       "connUnitPortStatCountLossofSignal": connUnitPortStatCountLossofSignal,
       "connUnitPortStatCountLossofSynchronization": connUnitPortStatCountLossofSynchronization,
       "connUnitPortStatCountInvalidOrderedSets": connUnitPortStatCountInvalidOrderedSets,
       "connUnitPortStatCountFramesTooLong": connUnitPortStatCountFramesTooLong,
       "connUnitPortStatCountFramesTruncated": connUnitPortStatCountFramesTruncated,
       "connUnitPortStatCountAddressErrors": connUnitPortStatCountAddressErrors,
       "connUnitPortStatCountDelimiterErrors": connUnitPortStatCountDelimiterErrors,
       "connUnitPortStatCountEncodingDisparityErrors": connUnitPortStatCountEncodingDisparityErrors,
       "connUnitServiceSet": connUnitServiceSet,
       "connUnitServiceScalars": connUnitServiceScalars,
       "connUnitSnsMaxEntry": connUnitSnsMaxEntry,
       "connUnitServiceTables": connUnitServiceTables,
       "connUnitSnsTable": connUnitSnsTable,
       "connUnitSnsEntry": connUnitSnsEntry,
       "connUnitSnsId": connUnitSnsId,
       "connUnitSnsPortIndex": connUnitSnsPortIndex,
       "connUnitSnsPortIdentifier": connUnitSnsPortIdentifier,
       "connUnitSnsPortName": connUnitSnsPortName,
       "connUnitSnsNodeName": connUnitSnsNodeName,
       "connUnitSnsClassOfSvc": connUnitSnsClassOfSvc,
       "connUnitSnsNodeIPAddress": connUnitSnsNodeIPAddress,
       "connUnitSnsProcAssoc": connUnitSnsProcAssoc,
       "connUnitSnsFC4Type": connUnitSnsFC4Type,
       "connUnitSnsPortType": connUnitSnsPortType,
       "connUnitSnsPortIPAddress": connUnitSnsPortIPAddress,
       "connUnitSnsFabricPortName": connUnitSnsFabricPortName,
       "connUnitSnsHardAddress": connUnitSnsHardAddress,
       "connUnitSnsSymbolicPortName": connUnitSnsSymbolicPortName,
       "connUnitSnsSymbolicNodeName": connUnitSnsSymbolicNodeName}
)
