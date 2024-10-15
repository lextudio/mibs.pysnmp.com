# SNMP MIB module (CAPWAP-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAPWAP-DOT11-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:32 2024
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

(CapwapBaseMacTypeTC,
 CapwapBaseTunnelModeTC) = mibBuilder.importSymbols(
    "CAPWAP-BASE-MIB",
    "CapwapBaseMacTypeTC",
    "CapwapBaseTunnelModeTC")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

capwapDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 195)
)
capwapDot11MIB.setRevisions(
        ("2010-04-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CapwapDot11WlanIdTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class CapwapDot11WlanIdProfileTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )



# MIB Managed Objects in the order of their OIDs

_CapwapDot11Objects_ObjectIdentity = ObjectIdentity
capwapDot11Objects = _CapwapDot11Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 195, 1)
)
_CapwapDot11WlanTable_Object = MibTable
capwapDot11WlanTable = _CapwapDot11WlanTable_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1)
)
if mibBuilder.loadTexts:
    capwapDot11WlanTable.setStatus("current")
_CapwapDot11WlanEntry_Object = MibTableRow
capwapDot11WlanEntry = _CapwapDot11WlanEntry_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1, 1)
)
capwapDot11WlanEntry.setIndexNames(
    (0, "CAPWAP-DOT11-MIB", "capwapDot11WlanProfileId"),
)
if mibBuilder.loadTexts:
    capwapDot11WlanEntry.setStatus("current")
_CapwapDot11WlanProfileId_Type = CapwapDot11WlanIdProfileTC
_CapwapDot11WlanProfileId_Object = MibTableColumn
capwapDot11WlanProfileId = _CapwapDot11WlanProfileId_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 1),
    _CapwapDot11WlanProfileId_Type()
)
capwapDot11WlanProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapDot11WlanProfileId.setStatus("current")
_CapwapDot11WlanProfileIfIndex_Type = InterfaceIndex
_CapwapDot11WlanProfileIfIndex_Object = MibTableColumn
capwapDot11WlanProfileIfIndex = _CapwapDot11WlanProfileIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 2),
    _CapwapDot11WlanProfileIfIndex_Type()
)
capwapDot11WlanProfileIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapDot11WlanProfileIfIndex.setStatus("current")
_CapwapDot11WlanMacType_Type = CapwapBaseMacTypeTC
_CapwapDot11WlanMacType_Object = MibTableColumn
capwapDot11WlanMacType = _CapwapDot11WlanMacType_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 3),
    _CapwapDot11WlanMacType_Type()
)
capwapDot11WlanMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapDot11WlanMacType.setStatus("current")
_CapwapDot11WlanTunnelMode_Type = CapwapBaseTunnelModeTC
_CapwapDot11WlanTunnelMode_Object = MibTableColumn
capwapDot11WlanTunnelMode = _CapwapDot11WlanTunnelMode_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 4),
    _CapwapDot11WlanTunnelMode_Type()
)
capwapDot11WlanTunnelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapDot11WlanTunnelMode.setStatus("current")
_CapwapDot11WlanRowStatus_Type = RowStatus
_CapwapDot11WlanRowStatus_Object = MibTableColumn
capwapDot11WlanRowStatus = _CapwapDot11WlanRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 5),
    _CapwapDot11WlanRowStatus_Type()
)
capwapDot11WlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapDot11WlanRowStatus.setStatus("current")
_CapwapDot11WlanBindTable_Object = MibTable
capwapDot11WlanBindTable = _CapwapDot11WlanBindTable_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 2)
)
if mibBuilder.loadTexts:
    capwapDot11WlanBindTable.setStatus("current")
_CapwapDot11WlanBindEntry_Object = MibTableRow
capwapDot11WlanBindEntry = _CapwapDot11WlanBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 2, 1)
)
capwapDot11WlanBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CAPWAP-DOT11-MIB", "capwapDot11WlanProfileId"),
)
if mibBuilder.loadTexts:
    capwapDot11WlanBindEntry.setStatus("current")
_CapwapDot11WlanBindWlanId_Type = CapwapDot11WlanIdTC
_CapwapDot11WlanBindWlanId_Object = MibTableColumn
capwapDot11WlanBindWlanId = _CapwapDot11WlanBindWlanId_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 1),
    _CapwapDot11WlanBindWlanId_Type()
)
capwapDot11WlanBindWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapDot11WlanBindWlanId.setStatus("current")
_CapwapDot11WlanBindBssIfIndex_Type = InterfaceIndex
_CapwapDot11WlanBindBssIfIndex_Object = MibTableColumn
capwapDot11WlanBindBssIfIndex = _CapwapDot11WlanBindBssIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 2),
    _CapwapDot11WlanBindBssIfIndex_Type()
)
capwapDot11WlanBindBssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapDot11WlanBindBssIfIndex.setStatus("current")
_CapwapDot11WlanBindRowStatus_Type = RowStatus
_CapwapDot11WlanBindRowStatus_Object = MibTableColumn
capwapDot11WlanBindRowStatus = _CapwapDot11WlanBindRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 3),
    _CapwapDot11WlanBindRowStatus_Type()
)
capwapDot11WlanBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapDot11WlanBindRowStatus.setStatus("current")
_CapwapDot11Conformance_ObjectIdentity = ObjectIdentity
capwapDot11Conformance = _CapwapDot11Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 195, 2)
)
_CapwapDot11Groups_ObjectIdentity = ObjectIdentity
capwapDot11Groups = _CapwapDot11Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 195, 2, 1)
)
_CapwapDot11Compliances_ObjectIdentity = ObjectIdentity
capwapDot11Compliances = _CapwapDot11Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 195, 2, 2)
)

# Managed Objects groups

capwapDot11WlanGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 195, 2, 1, 1)
)
capwapDot11WlanGroup.setObjects(
      *(("CAPWAP-DOT11-MIB", "capwapDot11WlanProfileIfIndex"),
        ("CAPWAP-DOT11-MIB", "capwapDot11WlanMacType"),
        ("CAPWAP-DOT11-MIB", "capwapDot11WlanTunnelMode"),
        ("CAPWAP-DOT11-MIB", "capwapDot11WlanRowStatus"))
)
if mibBuilder.loadTexts:
    capwapDot11WlanGroup.setStatus("current")

capwapDot11WlanBindGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 195, 2, 1, 2)
)
capwapDot11WlanBindGroup.setObjects(
      *(("CAPWAP-DOT11-MIB", "capwapDot11WlanBindWlanId"),
        ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindBssIfIndex"),
        ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindRowStatus"))
)
if mibBuilder.loadTexts:
    capwapDot11WlanBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

capwapDot11Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 195, 2, 2, 1)
)
if mibBuilder.loadTexts:
    capwapDot11Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAPWAP-DOT11-MIB",
    **{"CapwapDot11WlanIdTC": CapwapDot11WlanIdTC,
       "CapwapDot11WlanIdProfileTC": CapwapDot11WlanIdProfileTC,
       "capwapDot11MIB": capwapDot11MIB,
       "capwapDot11Objects": capwapDot11Objects,
       "capwapDot11WlanTable": capwapDot11WlanTable,
       "capwapDot11WlanEntry": capwapDot11WlanEntry,
       "capwapDot11WlanProfileId": capwapDot11WlanProfileId,
       "capwapDot11WlanProfileIfIndex": capwapDot11WlanProfileIfIndex,
       "capwapDot11WlanMacType": capwapDot11WlanMacType,
       "capwapDot11WlanTunnelMode": capwapDot11WlanTunnelMode,
       "capwapDot11WlanRowStatus": capwapDot11WlanRowStatus,
       "capwapDot11WlanBindTable": capwapDot11WlanBindTable,
       "capwapDot11WlanBindEntry": capwapDot11WlanBindEntry,
       "capwapDot11WlanBindWlanId": capwapDot11WlanBindWlanId,
       "capwapDot11WlanBindBssIfIndex": capwapDot11WlanBindBssIfIndex,
       "capwapDot11WlanBindRowStatus": capwapDot11WlanBindRowStatus,
       "capwapDot11Conformance": capwapDot11Conformance,
       "capwapDot11Groups": capwapDot11Groups,
       "capwapDot11WlanGroup": capwapDot11WlanGroup,
       "capwapDot11WlanBindGroup": capwapDot11WlanBindGroup,
       "capwapDot11Compliances": capwapDot11Compliances,
       "capwapDot11Compliance": capwapDot11Compliance}
)
