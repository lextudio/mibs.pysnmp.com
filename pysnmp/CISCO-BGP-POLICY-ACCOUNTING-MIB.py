# SNMP MIB module (CISCO-BGP-POLICY-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BGP-POLICY-ACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

ciscoBgpPolAcctMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 148)
)
ciscoBgpPolAcctMIB.setRevisions(
        ("2002-07-26 00:00",
         "1999-12-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBgpPolAcctMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBgpPolAcctMIBObjects = _CiscoBgpPolAcctMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1)
)
_CbpAcctTable_Object = MibTable
cbpAcctTable = _CbpAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1)
)
if mibBuilder.loadTexts:
    cbpAcctTable.setStatus("current")
_CbpAcctEntry_Object = MibTableRow
cbpAcctEntry = _CbpAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1)
)
cbpAcctEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"),
)
if mibBuilder.loadTexts:
    cbpAcctEntry.setStatus("current")


class _CbpAcctTrafficIndex_Type(Integer32):
    """Custom type cbpAcctTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CbpAcctTrafficIndex_Type.__name__ = "Integer32"
_CbpAcctTrafficIndex_Object = MibTableColumn
cbpAcctTrafficIndex = _CbpAcctTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 1),
    _CbpAcctTrafficIndex_Type()
)
cbpAcctTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbpAcctTrafficIndex.setStatus("current")
_CbpAcctInPacketCount_Type = Counter64
_CbpAcctInPacketCount_Object = MibTableColumn
cbpAcctInPacketCount = _CbpAcctInPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 2),
    _CbpAcctInPacketCount_Type()
)
cbpAcctInPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbpAcctInPacketCount.setStatus("current")
_CbpAcctInOctetCount_Type = Counter64
_CbpAcctInOctetCount_Object = MibTableColumn
cbpAcctInOctetCount = _CbpAcctInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 3),
    _CbpAcctInOctetCount_Type()
)
cbpAcctInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbpAcctInOctetCount.setStatus("current")
_CbpAcctOutPacketCount_Type = Counter64
_CbpAcctOutPacketCount_Object = MibTableColumn
cbpAcctOutPacketCount = _CbpAcctOutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 4),
    _CbpAcctOutPacketCount_Type()
)
cbpAcctOutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbpAcctOutPacketCount.setStatus("current")
_CbpAcctOutOctetCount_Type = Counter64
_CbpAcctOutOctetCount_Object = MibTableColumn
cbpAcctOutOctetCount = _CbpAcctOutOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 5),
    _CbpAcctOutOctetCount_Type()
)
cbpAcctOutOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbpAcctOutOctetCount.setStatus("current")
_CiscoBgpPolAcctMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBgpPolAcctMIBConformance = _CiscoBgpPolAcctMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3)
)
_CiscoBgpPolAcctMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBgpPolAcctMIBCompliances = _CiscoBgpPolAcctMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1)
)
_CiscoBgpPolAcctMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBgpPolAcctMIBGroups = _CiscoBgpPolAcctMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2)
)

# Managed Objects groups

cbpAcctTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 1)
)
cbpAcctTableGroup.setObjects(
      *(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"),
        ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"),
        ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"))
)
if mibBuilder.loadTexts:
    cbpAcctTableGroup.setStatus("deprecated")

cbpAcctTableGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 2)
)
cbpAcctTableGroupRev1.setObjects(
      *(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"),
        ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"),
        ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"),
        ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutPacketCount"),
        ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutOctetCount"))
)
if mibBuilder.loadTexts:
    cbpAcctTableGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoBgpPolAcctMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBgpPolAcctMIBCompliance.setStatus(
        "deprecated"
    )

ciscoBgpPolAcctMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoBgpPolAcctMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BGP-POLICY-ACCOUNTING-MIB",
    **{"ciscoBgpPolAcctMIB": ciscoBgpPolAcctMIB,
       "ciscoBgpPolAcctMIBObjects": ciscoBgpPolAcctMIBObjects,
       "cbpAcctTable": cbpAcctTable,
       "cbpAcctEntry": cbpAcctEntry,
       "cbpAcctTrafficIndex": cbpAcctTrafficIndex,
       "cbpAcctInPacketCount": cbpAcctInPacketCount,
       "cbpAcctInOctetCount": cbpAcctInOctetCount,
       "cbpAcctOutPacketCount": cbpAcctOutPacketCount,
       "cbpAcctOutOctetCount": cbpAcctOutOctetCount,
       "ciscoBgpPolAcctMIBConformance": ciscoBgpPolAcctMIBConformance,
       "ciscoBgpPolAcctMIBCompliances": ciscoBgpPolAcctMIBCompliances,
       "ciscoBgpPolAcctMIBCompliance": ciscoBgpPolAcctMIBCompliance,
       "ciscoBgpPolAcctMIBComplianceRev1": ciscoBgpPolAcctMIBComplianceRev1,
       "ciscoBgpPolAcctMIBGroups": ciscoBgpPolAcctMIBGroups,
       "cbpAcctTableGroup": cbpAcctTableGroup,
       "cbpAcctTableGroupRev1": cbpAcctTableGroupRev1}
)
