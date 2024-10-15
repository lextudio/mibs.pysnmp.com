# SNMP MIB module (ZHONE-COM-IP-RD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-RD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:10 2024
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

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpRd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 53)
)
comIpRd.setRevisions(
        ("2000-09-12 10:02",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneRDIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Rd_ObjectIdentity = ObjectIdentity
rd = _Rd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 3)
)
if mibBuilder.loadTexts:
    rd.setStatus("current")
_RdTable_Object = MibTable
rdTable = _RdTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rdTable.setStatus("current")
_RdEntry_Object = MibTableRow
rdEntry = _RdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1)
)
rdEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
)
if mibBuilder.loadTexts:
    rdEntry.setStatus("current")
_RdIndex_Type = ZhoneRDIndex
_RdIndex_Object = MibTableColumn
rdIndex = _RdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1, 1),
    _RdIndex_Type()
)
rdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdIndex.setStatus("current")
_RdRowStatus_Type = ZhoneRowStatus
_RdRowStatus_Object = MibTableColumn
rdRowStatus = _RdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1, 2),
    _RdRowStatus_Type()
)
rdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-RD-MIB",
    **{"ZhoneRDIndex": ZhoneRDIndex,
       "rd": rd,
       "rdTable": rdTable,
       "rdEntry": rdEntry,
       "rdIndex": rdIndex,
       "rdRowStatus": rdRowStatus,
       "comIpRd": comIpRd}
)
