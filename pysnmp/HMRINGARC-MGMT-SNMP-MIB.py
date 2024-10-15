# SNMP MIB module (HMRINGARC-MGMT-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HMRINGARC-MGMT-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:43 2024
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

(hmRingRedundancy,) = mibBuilder.importSymbols(
    "HMRING-MGMT-SNMP-MIB",
    "hmRingRedundancy")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hmARC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7)
)
hmARC.setRevisions(
        ("2010-09-01 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmArcManagerConfig_ObjectIdentity = ObjectIdentity
hmArcManagerConfig = _HmArcManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1)
)


class _HmArcManagerAdminStatus_Type(Integer32):
    """Custom type hmArcManagerAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HmArcManagerAdminStatus_Type.__name__ = "Integer32"
_HmArcManagerAdminStatus_Object = MibScalar
hmArcManagerAdminStatus = _HmArcManagerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 1),
    _HmArcManagerAdminStatus_Type()
)
hmArcManagerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmArcManagerAdminStatus.setStatus("current")


class _HmArcManagerRedProtocol_Type(Integer32):
    """Custom type hmArcManagerRedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mrp", 1)
    )


_HmArcManagerRedProtocol_Type.__name__ = "Integer32"
_HmArcManagerRedProtocol_Object = MibScalar
hmArcManagerRedProtocol = _HmArcManagerRedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 2),
    _HmArcManagerRedProtocol_Type()
)
hmArcManagerRedProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmArcManagerRedProtocol.setStatus("current")
_HmArcManagerPrimGroupID_Type = Integer32
_HmArcManagerPrimGroupID_Object = MibScalar
hmArcManagerPrimGroupID = _HmArcManagerPrimGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 3),
    _HmArcManagerPrimGroupID_Type()
)
hmArcManagerPrimGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcManagerPrimGroupID.setStatus("current")
_HmArcManagerPrimIfIndex_Type = Integer32
_HmArcManagerPrimIfIndex_Object = MibScalar
hmArcManagerPrimIfIndex = _HmArcManagerPrimIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 4),
    _HmArcManagerPrimIfIndex_Type()
)
hmArcManagerPrimIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcManagerPrimIfIndex.setStatus("current")
_HmArcManagerRedGroupID_Type = Integer32
_HmArcManagerRedGroupID_Object = MibScalar
hmArcManagerRedGroupID = _HmArcManagerRedGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 5),
    _HmArcManagerRedGroupID_Type()
)
hmArcManagerRedGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcManagerRedGroupID.setStatus("current")
_HmArcManagerRedIfIndex_Type = Integer32
_HmArcManagerRedIfIndex_Object = MibScalar
hmArcManagerRedIfIndex = _HmArcManagerRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 6),
    _HmArcManagerRedIfIndex_Type()
)
hmArcManagerRedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcManagerRedIfIndex.setStatus("current")
_HmArcManagerVlanID_Type = Integer32
_HmArcManagerVlanID_Object = MibScalar
hmArcManagerVlanID = _HmArcManagerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 7),
    _HmArcManagerVlanID_Type()
)
hmArcManagerVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcManagerVlanID.setStatus("current")


class _HmArcManagerAction_Type(Integer32):
    """Custom type hmArcManagerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkTopology", 2),
          ("configureRing", 3),
          ("noAction", 1))
    )


_HmArcManagerAction_Type.__name__ = "Integer32"
_HmArcManagerAction_Object = MibScalar
hmArcManagerAction = _HmArcManagerAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 8),
    _HmArcManagerAction_Type()
)
hmArcManagerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmArcManagerAction.setStatus("current")


class _HmArcManagerActionResult_Type(Integer32):
    """Custom type hmArcManagerActionResult based on Integer32"""
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
        *(("closedRing", 3),
          ("configFailed", 7),
          ("configSuccessful", 8),
          ("configuredRing", 4),
          ("invalidTopology", 6),
          ("noAction", 1),
          ("openRing", 5),
          ("pending", 2))
    )


_HmArcManagerActionResult_Type.__name__ = "Integer32"
_HmArcManagerActionResult_Object = MibScalar
hmArcManagerActionResult = _HmArcManagerActionResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 9),
    _HmArcManagerActionResult_Type()
)
hmArcManagerActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcManagerActionResult.setStatus("current")
_HmArcManagerStatus_ObjectIdentity = ObjectIdentity
hmArcManagerStatus = _HmArcManagerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2)
)
_HmArcCheckResultTable_Object = MibTable
hmArcCheckResultTable = _HmArcCheckResultTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hmArcCheckResultTable.setStatus("current")
_HmArcCheckResultEntry_Object = MibTableRow
hmArcCheckResultEntry = _HmArcCheckResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1)
)
hmArcCheckResultEntry.setIndexNames(
    (0, "HMRINGARC-MGMT-SNMP-MIB", "hmArcCheckStatusIndex"),
    (0, "HMRINGARC-MGMT-SNMP-MIB", "hmArcCheckStatusDeviceMac"),
)
if mibBuilder.loadTexts:
    hmArcCheckResultEntry.setStatus("current")
_HmArcCheckStatusIndex_Type = Integer32
_HmArcCheckStatusIndex_Object = MibTableColumn
hmArcCheckStatusIndex = _HmArcCheckStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 1),
    _HmArcCheckStatusIndex_Type()
)
hmArcCheckStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcCheckStatusIndex.setStatus("current")


class _HmArcCheckStatusDeviceMac_Type(OctetString):
    """Custom type hmArcCheckStatusDeviceMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HmArcCheckStatusDeviceMac_Type.__name__ = "OctetString"
_HmArcCheckStatusDeviceMac_Object = MibTableColumn
hmArcCheckStatusDeviceMac = _HmArcCheckStatusDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 2),
    _HmArcCheckStatusDeviceMac_Type()
)
hmArcCheckStatusDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcCheckStatusDeviceMac.setStatus("current")
_HmArcCheckStatusDeviceIp_Type = IpAddress
_HmArcCheckStatusDeviceIp_Object = MibTableColumn
hmArcCheckStatusDeviceIp = _HmArcCheckStatusDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 3),
    _HmArcCheckStatusDeviceIp_Type()
)
hmArcCheckStatusDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcCheckStatusDeviceIp.setStatus("current")


class _HmArcCheckStatusType_Type(Integer32):
    """Custom type hmArcCheckStatusType based on Integer32"""
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
        *(("alreadyConfigured", 3),
          ("configFailed", 6),
          ("duplexMode", 7),
          ("info", 10),
          ("loop", 2),
          ("noArcDevices", 8),
          ("openRing", 5),
          ("otherRm", 1),
          ("portState", 9),
          ("unsupportedOption", 4))
    )


_HmArcCheckStatusType_Type.__name__ = "Integer32"
_HmArcCheckStatusType_Object = MibTableColumn
hmArcCheckStatusType = _HmArcCheckStatusType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 4),
    _HmArcCheckStatusType_Type()
)
hmArcCheckStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcCheckStatusType.setStatus("current")
_HmArcCheckStatusInfo_Type = DisplayString
_HmArcCheckStatusInfo_Object = MibTableColumn
hmArcCheckStatusInfo = _HmArcCheckStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 5),
    _HmArcCheckStatusInfo_Type()
)
hmArcCheckStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcCheckStatusInfo.setStatus("current")


class _HmArcCheckStatusClassification_Type(Integer32):
    """Custom type hmArcCheckStatusClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ok", 3),
          ("warning", 2))
    )


_HmArcCheckStatusClassification_Type.__name__ = "Integer32"
_HmArcCheckStatusClassification_Object = MibTableColumn
hmArcCheckStatusClassification = _HmArcCheckStatusClassification_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 6),
    _HmArcCheckStatusClassification_Type()
)
hmArcCheckStatusClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcCheckStatusClassification.setStatus("current")
_HmArcClientConfig_ObjectIdentity = ObjectIdentity
hmArcClientConfig = _HmArcClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 3)
)


class _HmArcClientAdminStatus_Type(Integer32):
    """Custom type hmArcClientAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkOnly", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_HmArcClientAdminStatus_Type.__name__ = "Integer32"
_HmArcClientAdminStatus_Object = MibScalar
hmArcClientAdminStatus = _HmArcClientAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 3, 1),
    _HmArcClientAdminStatus_Type()
)
hmArcClientAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmArcClientAdminStatus.setStatus("current")
_HmArcClientStatus_ObjectIdentity = ObjectIdentity
hmArcClientStatus = _HmArcClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4)
)


class _HmArcClientManagerDeviceMac_Type(OctetString):
    """Custom type hmArcClientManagerDeviceMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HmArcClientManagerDeviceMac_Type.__name__ = "OctetString"
_HmArcClientManagerDeviceMac_Object = MibScalar
hmArcClientManagerDeviceMac = _HmArcClientManagerDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 1),
    _HmArcClientManagerDeviceMac_Type()
)
hmArcClientManagerDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcClientManagerDeviceMac.setStatus("current")
_HmArcClientManagerDeviceIp_Type = IpAddress
_HmArcClientManagerDeviceIp_Object = MibScalar
hmArcClientManagerDeviceIp = _HmArcClientManagerDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 2),
    _HmArcClientManagerDeviceIp_Type()
)
hmArcClientManagerDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcClientManagerDeviceIp.setStatus("current")
_HmArcClientPrimGroupID_Type = Integer32
_HmArcClientPrimGroupID_Object = MibScalar
hmArcClientPrimGroupID = _HmArcClientPrimGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 3),
    _HmArcClientPrimGroupID_Type()
)
hmArcClientPrimGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcClientPrimGroupID.setStatus("current")
_HmArcClientPrimIfIndex_Type = Integer32
_HmArcClientPrimIfIndex_Object = MibScalar
hmArcClientPrimIfIndex = _HmArcClientPrimIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 4),
    _HmArcClientPrimIfIndex_Type()
)
hmArcClientPrimIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcClientPrimIfIndex.setStatus("current")
_HmArcClientRedGroupID_Type = Integer32
_HmArcClientRedGroupID_Object = MibScalar
hmArcClientRedGroupID = _HmArcClientRedGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 5),
    _HmArcClientRedGroupID_Type()
)
hmArcClientRedGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcClientRedGroupID.setStatus("current")
_HmArcClientRedIfIndex_Type = Integer32
_HmArcClientRedIfIndex_Object = MibScalar
hmArcClientRedIfIndex = _HmArcClientRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 6),
    _HmArcClientRedIfIndex_Type()
)
hmArcClientRedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmArcClientRedIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMRINGARC-MGMT-SNMP-MIB",
    **{"hmARC": hmARC,
       "hmArcManagerConfig": hmArcManagerConfig,
       "hmArcManagerAdminStatus": hmArcManagerAdminStatus,
       "hmArcManagerRedProtocol": hmArcManagerRedProtocol,
       "hmArcManagerPrimGroupID": hmArcManagerPrimGroupID,
       "hmArcManagerPrimIfIndex": hmArcManagerPrimIfIndex,
       "hmArcManagerRedGroupID": hmArcManagerRedGroupID,
       "hmArcManagerRedIfIndex": hmArcManagerRedIfIndex,
       "hmArcManagerVlanID": hmArcManagerVlanID,
       "hmArcManagerAction": hmArcManagerAction,
       "hmArcManagerActionResult": hmArcManagerActionResult,
       "hmArcManagerStatus": hmArcManagerStatus,
       "hmArcCheckResultTable": hmArcCheckResultTable,
       "hmArcCheckResultEntry": hmArcCheckResultEntry,
       "hmArcCheckStatusIndex": hmArcCheckStatusIndex,
       "hmArcCheckStatusDeviceMac": hmArcCheckStatusDeviceMac,
       "hmArcCheckStatusDeviceIp": hmArcCheckStatusDeviceIp,
       "hmArcCheckStatusType": hmArcCheckStatusType,
       "hmArcCheckStatusInfo": hmArcCheckStatusInfo,
       "hmArcCheckStatusClassification": hmArcCheckStatusClassification,
       "hmArcClientConfig": hmArcClientConfig,
       "hmArcClientAdminStatus": hmArcClientAdminStatus,
       "hmArcClientStatus": hmArcClientStatus,
       "hmArcClientManagerDeviceMac": hmArcClientManagerDeviceMac,
       "hmArcClientManagerDeviceIp": hmArcClientManagerDeviceIp,
       "hmArcClientPrimGroupID": hmArcClientPrimGroupID,
       "hmArcClientPrimIfIndex": hmArcClientPrimIfIndex,
       "hmArcClientRedGroupID": hmArcClientRedGroupID,
       "hmArcClientRedIfIndex": hmArcClientRedIfIndex}
)
