# SNMP MIB module (CISCO-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:34 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(tcpConnEntry,) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnEntry")


# MODULE-IDENTITY

ciscoTcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 6)
)
ciscoTcpMIB.setRevisions(
        ("2001-11-12 00:00",
         "1996-12-03 00:00",
         "1994-07-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTcpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTcpMIBObjects = _CiscoTcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1)
)
_CiscoTcpConnTable_Object = MibTable
ciscoTcpConnTable = _CiscoTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTcpConnTable.setStatus("current")
_CiscoTcpConnEntry_Object = MibTableRow
ciscoTcpConnEntry = _CiscoTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTcpConnEntry.setStatus("current")
_CiscoTcpConnInBytes_Type = Counter32
_CiscoTcpConnInBytes_Object = MibTableColumn
ciscoTcpConnInBytes = _CiscoTcpConnInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 1),
    _CiscoTcpConnInBytes_Type()
)
ciscoTcpConnInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnInBytes.setStatus("current")
_CiscoTcpConnOutBytes_Type = Counter32
_CiscoTcpConnOutBytes_Object = MibTableColumn
ciscoTcpConnOutBytes = _CiscoTcpConnOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 2),
    _CiscoTcpConnOutBytes_Type()
)
ciscoTcpConnOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnOutBytes.setStatus("current")
_CiscoTcpConnInPkts_Type = Counter32
_CiscoTcpConnInPkts_Object = MibTableColumn
ciscoTcpConnInPkts = _CiscoTcpConnInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 3),
    _CiscoTcpConnInPkts_Type()
)
ciscoTcpConnInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnInPkts.setStatus("current")
_CiscoTcpConnOutPkts_Type = Counter32
_CiscoTcpConnOutPkts_Object = MibTableColumn
ciscoTcpConnOutPkts = _CiscoTcpConnOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 4),
    _CiscoTcpConnOutPkts_Type()
)
ciscoTcpConnOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnOutPkts.setStatus("current")
_CiscoTcpConnElapsed_Type = TimeTicks
_CiscoTcpConnElapsed_Object = MibTableColumn
ciscoTcpConnElapsed = _CiscoTcpConnElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 5),
    _CiscoTcpConnElapsed_Type()
)
ciscoTcpConnElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnElapsed.setStatus("current")
_CiscoTcpConnSRTT_Type = Integer32
_CiscoTcpConnSRTT_Object = MibTableColumn
ciscoTcpConnSRTT = _CiscoTcpConnSRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 6),
    _CiscoTcpConnSRTT_Type()
)
ciscoTcpConnSRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnSRTT.setStatus("current")
if mibBuilder.loadTexts:
    ciscoTcpConnSRTT.setUnits("milliseconds")
_CiscoTcpConnRetransPkts_Type = Counter32
_CiscoTcpConnRetransPkts_Object = MibTableColumn
ciscoTcpConnRetransPkts = _CiscoTcpConnRetransPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 7),
    _CiscoTcpConnRetransPkts_Type()
)
ciscoTcpConnRetransPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnRetransPkts.setStatus("current")
_CiscoTcpConnFastRetransPkts_Type = Counter32
_CiscoTcpConnFastRetransPkts_Object = MibTableColumn
ciscoTcpConnFastRetransPkts = _CiscoTcpConnFastRetransPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 8),
    _CiscoTcpConnFastRetransPkts_Type()
)
ciscoTcpConnFastRetransPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnFastRetransPkts.setStatus("current")
_CiscoTcpConnRto_Type = Integer32
_CiscoTcpConnRto_Object = MibTableColumn
ciscoTcpConnRto = _CiscoTcpConnRto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 9),
    _CiscoTcpConnRto_Type()
)
ciscoTcpConnRto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTcpConnRto.setStatus("current")
if mibBuilder.loadTexts:
    ciscoTcpConnRto.setUnits("milliseconds")
_CiscoTcpMIBTraps_ObjectIdentity = ObjectIdentity
ciscoTcpMIBTraps = _CiscoTcpMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 2)
)
_CiscoTcpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoTcpMIBConformance = _CiscoTcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3)
)
_CiscoTcpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTcpMIBCompliances = _CiscoTcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1)
)
_CiscoTcpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTcpMIBGroups = _CiscoTcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2)
)
tcpConnEntry.registerAugmentions(
    ("CISCO-TCP-MIB",
     "ciscoTcpConnEntry")
)
ciscoTcpConnEntry.setIndexNames(*tcpConnEntry.getIndexNames())

# Managed Objects groups

ciscoTcpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 1)
)
ciscoTcpMIBGroup.setObjects(
      *(("CISCO-TCP-MIB", "ciscoTcpConnInBytes"),
        ("CISCO-TCP-MIB", "ciscoTcpConnOutBytes"),
        ("CISCO-TCP-MIB", "ciscoTcpConnInPkts"),
        ("CISCO-TCP-MIB", "ciscoTcpConnOutPkts"),
        ("CISCO-TCP-MIB", "ciscoTcpConnElapsed"),
        ("CISCO-TCP-MIB", "ciscoTcpConnSRTT"))
)
if mibBuilder.loadTexts:
    ciscoTcpMIBGroup.setStatus("deprecated")

ciscoTcpMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 2)
)
ciscoTcpMIBGroupRev1.setObjects(
      *(("CISCO-TCP-MIB", "ciscoTcpConnInBytes"),
        ("CISCO-TCP-MIB", "ciscoTcpConnOutBytes"),
        ("CISCO-TCP-MIB", "ciscoTcpConnInPkts"),
        ("CISCO-TCP-MIB", "ciscoTcpConnOutPkts"),
        ("CISCO-TCP-MIB", "ciscoTcpConnElapsed"),
        ("CISCO-TCP-MIB", "ciscoTcpConnSRTT"),
        ("CISCO-TCP-MIB", "ciscoTcpConnRto"),
        ("CISCO-TCP-MIB", "ciscoTcpConnRetransPkts"),
        ("CISCO-TCP-MIB", "ciscoTcpConnFastRetransPkts"))
)
if mibBuilder.loadTexts:
    ciscoTcpMIBGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTcpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTcpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTcpMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TCP-MIB",
    **{"ciscoTcpMIB": ciscoTcpMIB,
       "ciscoTcpMIBObjects": ciscoTcpMIBObjects,
       "ciscoTcpConnTable": ciscoTcpConnTable,
       "ciscoTcpConnEntry": ciscoTcpConnEntry,
       "ciscoTcpConnInBytes": ciscoTcpConnInBytes,
       "ciscoTcpConnOutBytes": ciscoTcpConnOutBytes,
       "ciscoTcpConnInPkts": ciscoTcpConnInPkts,
       "ciscoTcpConnOutPkts": ciscoTcpConnOutPkts,
       "ciscoTcpConnElapsed": ciscoTcpConnElapsed,
       "ciscoTcpConnSRTT": ciscoTcpConnSRTT,
       "ciscoTcpConnRetransPkts": ciscoTcpConnRetransPkts,
       "ciscoTcpConnFastRetransPkts": ciscoTcpConnFastRetransPkts,
       "ciscoTcpConnRto": ciscoTcpConnRto,
       "ciscoTcpMIBTraps": ciscoTcpMIBTraps,
       "ciscoTcpMIBConformance": ciscoTcpMIBConformance,
       "ciscoTcpMIBCompliances": ciscoTcpMIBCompliances,
       "ciscoTcpMIBCompliance": ciscoTcpMIBCompliance,
       "ciscoTcpMIBComplianceRev1": ciscoTcpMIBComplianceRev1,
       "ciscoTcpMIBGroups": ciscoTcpMIBGroups,
       "ciscoTcpMIBGroup": ciscoTcpMIBGroup,
       "ciscoTcpMIBGroupRev1": ciscoTcpMIBGroupRev1}
)
