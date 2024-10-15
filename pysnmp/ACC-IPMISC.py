# SNMP MIB module (ACC-IPMISC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-IPMISC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:20 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccIpMisc_ObjectIdentity = ObjectIdentity
accIpMisc = _AccIpMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45)
)
_AccIpAssign_ObjectIdentity = ObjectIdentity
accIpAssign = _AccIpAssign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1)
)
_AccIpAssignRangeTable_Object = MibTable
accIpAssignRangeTable = _AccIpAssignRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 1)
)
if mibBuilder.loadTexts:
    accIpAssignRangeTable.setStatus("mandatory")
_AccIpAssignRangeEntry_Object = MibTableRow
accIpAssignRangeEntry = _AccIpAssignRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 1, 1)
)
accIpAssignRangeEntry.setIndexNames(
    (0, "ACC-IPMISC", "accIpAssignStartAddr"),
)
if mibBuilder.loadTexts:
    accIpAssignRangeEntry.setStatus("mandatory")
_AccIpAssignStartAddr_Type = IpAddress
_AccIpAssignStartAddr_Object = MibTableColumn
accIpAssignStartAddr = _AccIpAssignStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 1, 1, 1),
    _AccIpAssignStartAddr_Type()
)
accIpAssignStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAssignStartAddr.setStatus("mandatory")
_AccIpAssignEndAddr_Type = IpAddress
_AccIpAssignEndAddr_Object = MibTableColumn
accIpAssignEndAddr = _AccIpAssignEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 1, 1, 2),
    _AccIpAssignEndAddr_Type()
)
accIpAssignEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAssignEndAddr.setStatus("mandatory")
_AccIpAssignAccessPartition_Type = DisplayString
_AccIpAssignAccessPartition_Object = MibTableColumn
accIpAssignAccessPartition = _AccIpAssignAccessPartition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 1, 1, 3),
    _AccIpAssignAccessPartition_Type()
)
accIpAssignAccessPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAssignAccessPartition.setStatus("obsolete")
_AccIpAssignCurrent_Type = Gauge32
_AccIpAssignCurrent_Object = MibScalar
accIpAssignCurrent = _AccIpAssignCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 3),
    _AccIpAssignCurrent_Type()
)
accIpAssignCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignCurrent.setStatus("mandatory")
_AccIpAssignAvail_Type = Gauge32
_AccIpAssignAvail_Object = MibScalar
accIpAssignAvail = _AccIpAssignAvail_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 4),
    _AccIpAssignAvail_Type()
)
accIpAssignAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignAvail.setStatus("mandatory")
_AccIpAssignTotals_Type = Integer32
_AccIpAssignTotals_Object = MibScalar
accIpAssignTotals = _AccIpAssignTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 5),
    _AccIpAssignTotals_Type()
)
accIpAssignTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignTotals.setStatus("mandatory")
_AccIpAssignReleases_Type = Counter32
_AccIpAssignReleases_Object = MibScalar
accIpAssignReleases = _AccIpAssignReleases_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 6),
    _AccIpAssignReleases_Type()
)
accIpAssignReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignReleases.setStatus("mandatory")
_AccIpAssignFailures_Type = Counter32
_AccIpAssignFailures_Object = MibScalar
accIpAssignFailures = _AccIpAssignFailures_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 7),
    _AccIpAssignFailures_Type()
)
accIpAssignFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignFailures.setStatus("mandatory")
_AccIpAssignAssignments_Type = Counter32
_AccIpAssignAssignments_Object = MibScalar
accIpAssignAssignments = _AccIpAssignAssignments_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 8),
    _AccIpAssignAssignments_Type()
)
accIpAssignAssignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignAssignments.setStatus("mandatory")
_AccIpAssignLasts_Type = IpAddress
_AccIpAssignLasts_Object = MibScalar
accIpAssignLasts = _AccIpAssignLasts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 1, 9),
    _AccIpAssignLasts_Type()
)
accIpAssignLasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpAssignLasts.setStatus("mandatory")
_AccIpNegAddrTable_Object = MibTable
accIpNegAddrTable = _AccIpNegAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 2)
)
if mibBuilder.loadTexts:
    accIpNegAddrTable.setStatus("mandatory")
_AccIpNegAddrEntry_Object = MibTableRow
accIpNegAddrEntry = _AccIpNegAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 2, 1)
)
accIpNegAddrEntry.setIndexNames(
    (0, "ACC-IPMISC", "accIpNegIfIndex"),
)
if mibBuilder.loadTexts:
    accIpNegAddrEntry.setStatus("mandatory")
_AccIpNegIfIndex_Type = Integer32
_AccIpNegIfIndex_Object = MibTableColumn
accIpNegIfIndex = _AccIpNegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 2, 1, 1),
    _AccIpNegIfIndex_Type()
)
accIpNegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNegIfIndex.setStatus("mandatory")


class _AccIpNegType_Type(Integer32):
    """Custom type accIpNegType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 2),
          ("configured", 1),
          ("user", 3))
    )


_AccIpNegType_Type.__name__ = "Integer32"
_AccIpNegType_Object = MibTableColumn
accIpNegType = _AccIpNegType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 2, 1, 2),
    _AccIpNegType_Type()
)
accIpNegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNegType.setStatus("mandatory")
_AccIpNegAddr_Type = IpAddress
_AccIpNegAddr_Object = MibTableColumn
accIpNegAddr = _AccIpNegAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 2, 1, 3),
    _AccIpNegAddr_Type()
)
accIpNegAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNegAddr.setStatus("mandatory")
_AccIpNegAccessPartition_Type = DisplayString
_AccIpNegAccessPartition_Object = MibTableColumn
accIpNegAccessPartition = _AccIpNegAccessPartition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 45, 2, 1, 4),
    _AccIpNegAccessPartition_Type()
)
accIpNegAccessPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpNegAccessPartition.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-IPMISC",
    **{"accIpMisc": accIpMisc,
       "accIpAssign": accIpAssign,
       "accIpAssignRangeTable": accIpAssignRangeTable,
       "accIpAssignRangeEntry": accIpAssignRangeEntry,
       "accIpAssignStartAddr": accIpAssignStartAddr,
       "accIpAssignEndAddr": accIpAssignEndAddr,
       "accIpAssignAccessPartition": accIpAssignAccessPartition,
       "accIpAssignCurrent": accIpAssignCurrent,
       "accIpAssignAvail": accIpAssignAvail,
       "accIpAssignTotals": accIpAssignTotals,
       "accIpAssignReleases": accIpAssignReleases,
       "accIpAssignFailures": accIpAssignFailures,
       "accIpAssignAssignments": accIpAssignAssignments,
       "accIpAssignLasts": accIpAssignLasts,
       "accIpNegAddrTable": accIpNegAddrTable,
       "accIpNegAddrEntry": accIpNegAddrEntry,
       "accIpNegIfIndex": accIpNegIfIndex,
       "accIpNegType": accIpNegType,
       "accIpNegAddr": accIpNegAddr,
       "accIpNegAccessPartition": accIpNegAccessPartition}
)
