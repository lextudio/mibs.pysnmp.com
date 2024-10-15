# SNMP MIB module (BAS-ANALYZER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ANALYZER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:19 2024
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

(basAnalyzer,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basAnalyzer")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basAnalyzerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasAnalyzerTable_Object = MibTable
basAnalyzerTable = _BasAnalyzerTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    basAnalyzerTable.setStatus("current")
_BasAnalyzerEntry_Object = MibTableRow
basAnalyzerEntry = _BasAnalyzerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1, 1)
)
basAnalyzerEntry.setIndexNames(
    (0, "BAS-ANALYZER-MIB", "basAnalyzerIndex"),
)
if mibBuilder.loadTexts:
    basAnalyzerEntry.setStatus("current")
_BasAnalyzerIndex_Type = InterfaceIndex
_BasAnalyzerIndex_Object = MibTableColumn
basAnalyzerIndex = _BasAnalyzerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1, 1, 1),
    _BasAnalyzerIndex_Type()
)
basAnalyzerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAnalyzerIndex.setStatus("current")
_BasAnalyzerClient_Type = InterfaceIndex
_BasAnalyzerClient_Object = MibTableColumn
basAnalyzerClient = _BasAnalyzerClient_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1, 1, 2),
    _BasAnalyzerClient_Type()
)
basAnalyzerClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAnalyzerClient.setStatus("current")


class _BasAnalyzerAdminStatus_Type(TruthValue):
    """Custom type basAnalyzerAdminStatus based on TruthValue"""


_BasAnalyzerAdminStatus_Object = MibTableColumn
basAnalyzerAdminStatus = _BasAnalyzerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1, 1, 3),
    _BasAnalyzerAdminStatus_Type()
)
basAnalyzerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAnalyzerAdminStatus.setStatus("current")
_BasAnalyzerMacAddress_Type = MacAddress
_BasAnalyzerMacAddress_Object = MibTableColumn
basAnalyzerMacAddress = _BasAnalyzerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1, 1, 4),
    _BasAnalyzerMacAddress_Type()
)
basAnalyzerMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAnalyzerMacAddress.setStatus("current")
_BasAnalyzerMacAddressMask_Type = MacAddress
_BasAnalyzerMacAddressMask_Object = MibTableColumn
basAnalyzerMacAddressMask = _BasAnalyzerMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17, 1, 1, 1, 5),
    _BasAnalyzerMacAddressMask_Type()
)
basAnalyzerMacAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basAnalyzerMacAddressMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ANALYZER-MIB",
    **{"basAnalyzerMib": basAnalyzerMib,
       "basAnalyzerTable": basAnalyzerTable,
       "basAnalyzerEntry": basAnalyzerEntry,
       "basAnalyzerIndex": basAnalyzerIndex,
       "basAnalyzerClient": basAnalyzerClient,
       "basAnalyzerAdminStatus": basAnalyzerAdminStatus,
       "basAnalyzerMacAddress": basAnalyzerMacAddress,
       "basAnalyzerMacAddressMask": basAnalyzerMacAddressMask}
)
