# SNMP MIB module (BROCADE-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-FABRIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:20 2024
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

(snAgentBrdIndex,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "snAgentBrdIndex")

(brcdFabric,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "brcdFabric")

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

brcdFabricMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1)
)
brcdFabricMIB.setRevisions(
        ("2012-05-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdFabricNotifications_ObjectIdentity = ObjectIdentity
brcdFabricNotifications = _BrcdFabricNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 0)
)
_BrcdFabricObjects_ObjectIdentity = ObjectIdentity
brcdFabricObjects = _BrcdFabricObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1)
)
_BrcdFabricStatsTable_Object = MibTable
brcdFabricStatsTable = _BrcdFabricStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    brcdFabricStatsTable.setStatus("current")
_BrcdFabricStatsEntry_Object = MibTableRow
brcdFabricStatsEntry = _BrcdFabricStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1)
)
brcdFabricStatsEntry.setIndexNames(
    (0, "BROCADE-FABRIC-MIB", "brcdFabricSfmId"),
    (0, "BROCADE-FABRIC-MIB", "brcdFabricSfmFeId"),
)
if mibBuilder.loadTexts:
    brcdFabricStatsEntry.setStatus("current")
_BrcdFabricSfmId_Type = Unsigned32
_BrcdFabricSfmId_Object = MibTableColumn
brcdFabricSfmId = _BrcdFabricSfmId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1, 1),
    _BrcdFabricSfmId_Type()
)
brcdFabricSfmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdFabricSfmId.setStatus("current")
_BrcdFabricSfmFeId_Type = Unsigned32
_BrcdFabricSfmFeId_Object = MibTableColumn
brcdFabricSfmFeId = _BrcdFabricSfmFeId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1, 2),
    _BrcdFabricSfmFeId_Type()
)
brcdFabricSfmFeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdFabricSfmFeId.setStatus("current")
_BrcdFabricDropMAC0Count_Type = Counter32
_BrcdFabricDropMAC0Count_Object = MibTableColumn
brcdFabricDropMAC0Count = _BrcdFabricDropMAC0Count_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1, 3),
    _BrcdFabricDropMAC0Count_Type()
)
brcdFabricDropMAC0Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdFabricDropMAC0Count.setStatus("current")
_BrcdFabricDropMAC1Count_Type = Counter32
_BrcdFabricDropMAC1Count_Object = MibTableColumn
brcdFabricDropMAC1Count = _BrcdFabricDropMAC1Count_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1, 4),
    _BrcdFabricDropMAC1Count_Type()
)
brcdFabricDropMAC1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdFabricDropMAC1Count.setStatus("current")
_BrcdFabricDropMAC2Count_Type = Counter32
_BrcdFabricDropMAC2Count_Object = MibTableColumn
brcdFabricDropMAC2Count = _BrcdFabricDropMAC2Count_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1, 5),
    _BrcdFabricDropMAC2Count_Type()
)
brcdFabricDropMAC2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdFabricDropMAC2Count.setStatus("current")
_BrcdFabricDropMAC3Count_Type = Counter32
_BrcdFabricDropMAC3Count_Object = MibTableColumn
brcdFabricDropMAC3Count = _BrcdFabricDropMAC3Count_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 1, 1, 1, 6),
    _BrcdFabricDropMAC3Count_Type()
)
brcdFabricDropMAC3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdFabricDropMAC3Count.setStatus("current")

# Managed Objects groups


# Notification objects

brcdFabricAutoSFMWalkInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 0, 1)
)
brcdFabricAutoSFMWalkInitiated.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    brcdFabricAutoSFMWalkInitiated.setStatus(
        "current"
    )

brcdFabricSFMRemovedFromDatapath = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13, 1, 0, 2)
)
brcdFabricSFMRemovedFromDatapath.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    brcdFabricSFMRemovedFromDatapath.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-FABRIC-MIB",
    **{"brcdFabricMIB": brcdFabricMIB,
       "brcdFabricNotifications": brcdFabricNotifications,
       "brcdFabricAutoSFMWalkInitiated": brcdFabricAutoSFMWalkInitiated,
       "brcdFabricSFMRemovedFromDatapath": brcdFabricSFMRemovedFromDatapath,
       "brcdFabricObjects": brcdFabricObjects,
       "brcdFabricStatsTable": brcdFabricStatsTable,
       "brcdFabricStatsEntry": brcdFabricStatsEntry,
       "brcdFabricSfmId": brcdFabricSfmId,
       "brcdFabricSfmFeId": brcdFabricSfmFeId,
       "brcdFabricDropMAC0Count": brcdFabricDropMAC0Count,
       "brcdFabricDropMAC1Count": brcdFabricDropMAC1Count,
       "brcdFabricDropMAC2Count": brcdFabricDropMAC2Count,
       "brcdFabricDropMAC3Count": brcdFabricDropMAC3Count}
)
