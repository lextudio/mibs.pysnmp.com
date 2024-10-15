# SNMP MIB module (MPOA-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPOA-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:31 2024
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

(Boolean,
 extensions) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "Boolean",
    "extensions")

(mpcIndex,) = mibBuilder.importSymbols(
    "MPOA-MIB",
    "mpcIndex")

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

(RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "RowStatus",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnMpoaExt_ObjectIdentity = ObjectIdentity
cnMpoaExt = _CnMpoaExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 7)
)
_CnMpcConfigTable_Object = MibTable
cnMpcConfigTable = _CnMpcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 2)
)
if mibBuilder.loadTexts:
    cnMpcConfigTable.setStatus("mandatory")
_CnMpcConfigEntry_Object = MibTableRow
cnMpcConfigEntry = _CnMpcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1)
)
cnMpcConfigEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
)
if mibBuilder.loadTexts:
    cnMpcConfigEntry.setStatus("mandatory")
_CnMpcShareControlVccs_Type = TruthValue
_CnMpcShareControlVccs_Object = MibTableColumn
cnMpcShareControlVccs = _CnMpcShareControlVccs_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 1),
    _CnMpcShareControlVccs_Type()
)
cnMpcShareControlVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpcShareControlVccs.setStatus("mandatory")
_CnMpcShareDataVccs_Type = TruthValue
_CnMpcShareDataVccs_Object = MibTableColumn
cnMpcShareDataVccs = _CnMpcShareDataVccs_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 2),
    _CnMpcShareDataVccs_Type()
)
cnMpcShareDataVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpcShareDataVccs.setStatus("mandatory")


class _CnMpcValidEntryCheckInterval_Type(Integer32):
    """Custom type cnMpcValidEntryCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnMpcValidEntryCheckInterval_Type.__name__ = "Integer32"
_CnMpcValidEntryCheckInterval_Object = MibTableColumn
cnMpcValidEntryCheckInterval = _CnMpcValidEntryCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 3),
    _CnMpcValidEntryCheckInterval_Type()
)
cnMpcValidEntryCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpcValidEntryCheckInterval.setStatus("mandatory")
_CnMpcMinFlowPacketCount_Type = Integer32
_CnMpcMinFlowPacketCount_Object = MibTableColumn
cnMpcMinFlowPacketCount = _CnMpcMinFlowPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 4),
    _CnMpcMinFlowPacketCount_Type()
)
cnMpcMinFlowPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpcMinFlowPacketCount.setStatus("mandatory")
_CnMpoaIpVerification_ObjectIdentity = ObjectIdentity
cnMpoaIpVerification = _CnMpoaIpVerification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3)
)


class _CnMpoaIpVerificationTableType_Type(Integer32):
    """Custom type cnMpoaIpVerificationTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclusion", 2),
          ("inclusion", 3),
          ("unknown", 1))
    )


_CnMpoaIpVerificationTableType_Type.__name__ = "Integer32"
_CnMpoaIpVerificationTableType_Object = MibScalar
cnMpoaIpVerificationTableType = _CnMpoaIpVerificationTableType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 1),
    _CnMpoaIpVerificationTableType_Type()
)
cnMpoaIpVerificationTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpoaIpVerificationTableType.setStatus("mandatory")


class _CnMpoaIpVerificationTableStatus_Type(Integer32):
    """Custom type cnMpoaIpVerificationTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("disable", 1),
          ("enable", 2))
    )


_CnMpoaIpVerificationTableStatus_Type.__name__ = "Integer32"
_CnMpoaIpVerificationTableStatus_Object = MibScalar
cnMpoaIpVerificationTableStatus = _CnMpoaIpVerificationTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 2),
    _CnMpoaIpVerificationTableStatus_Type()
)
cnMpoaIpVerificationTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpoaIpVerificationTableStatus.setStatus("mandatory")
_CnMpoaIpVerificationTableDownload_Type = Boolean
_CnMpoaIpVerificationTableDownload_Object = MibScalar
cnMpoaIpVerificationTableDownload = _CnMpoaIpVerificationTableDownload_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 3),
    _CnMpoaIpVerificationTableDownload_Type()
)
cnMpoaIpVerificationTableDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpoaIpVerificationTableDownload.setStatus("mandatory")
_CnMpoaIpVerificationTable_Object = MibTable
cnMpoaIpVerificationTable = _CnMpoaIpVerificationTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4)
)
if mibBuilder.loadTexts:
    cnMpoaIpVerificationTable.setStatus("mandatory")
_CnMpoaIpVerificationEntry_Object = MibTableRow
cnMpoaIpVerificationEntry = _CnMpoaIpVerificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1)
)
cnMpoaIpVerificationEntry.setIndexNames(
    (0, "MPOA-EXT-MIB", "cnMpoaIpVerificationAddress"),
    (0, "MPOA-EXT-MIB", "cnMpoaIpVerificationMask"),
)
if mibBuilder.loadTexts:
    cnMpoaIpVerificationEntry.setStatus("mandatory")
_CnMpoaIpVerificationAddress_Type = IpAddress
_CnMpoaIpVerificationAddress_Object = MibTableColumn
cnMpoaIpVerificationAddress = _CnMpoaIpVerificationAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1, 1),
    _CnMpoaIpVerificationAddress_Type()
)
cnMpoaIpVerificationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMpoaIpVerificationAddress.setStatus("mandatory")
_CnMpoaIpVerificationMask_Type = IpAddress
_CnMpoaIpVerificationMask_Object = MibTableColumn
cnMpoaIpVerificationMask = _CnMpoaIpVerificationMask_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1, 2),
    _CnMpoaIpVerificationMask_Type()
)
cnMpoaIpVerificationMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMpoaIpVerificationMask.setStatus("mandatory")
_CnMpoaIpVerificationStatus_Type = RowStatus
_CnMpoaIpVerificationStatus_Object = MibTableColumn
cnMpoaIpVerificationStatus = _CnMpoaIpVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1, 3),
    _CnMpoaIpVerificationStatus_Type()
)
cnMpoaIpVerificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMpoaIpVerificationStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPOA-EXT-MIB",
    **{"cnMpoaExt": cnMpoaExt,
       "cnMpcConfigTable": cnMpcConfigTable,
       "cnMpcConfigEntry": cnMpcConfigEntry,
       "cnMpcShareControlVccs": cnMpcShareControlVccs,
       "cnMpcShareDataVccs": cnMpcShareDataVccs,
       "cnMpcValidEntryCheckInterval": cnMpcValidEntryCheckInterval,
       "cnMpcMinFlowPacketCount": cnMpcMinFlowPacketCount,
       "cnMpoaIpVerification": cnMpoaIpVerification,
       "cnMpoaIpVerificationTableType": cnMpoaIpVerificationTableType,
       "cnMpoaIpVerificationTableStatus": cnMpoaIpVerificationTableStatus,
       "cnMpoaIpVerificationTableDownload": cnMpoaIpVerificationTableDownload,
       "cnMpoaIpVerificationTable": cnMpoaIpVerificationTable,
       "cnMpoaIpVerificationEntry": cnMpoaIpVerificationEntry,
       "cnMpoaIpVerificationAddress": cnMpoaIpVerificationAddress,
       "cnMpoaIpVerificationMask": cnMpoaIpVerificationMask,
       "cnMpoaIpVerificationStatus": cnMpoaIpVerificationStatus}
)
