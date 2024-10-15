# SNMP MIB module (CADANT-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:03 2024
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

(cadLicense,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLicense")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadLicenseMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1)
)
cadLicenseMib.setRevisions(
        ("2015-06-17 00:00",
         "2015-06-09 00:00",
         "2014-08-20 00:00",
         "2014-08-14 00:00",
         "2014-07-17 00:00",
         "2014-07-10 00:00",
         "2014-06-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadChassisLicenseIndexType(Integer32, TextualConvention):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("docsisDownstream30A", 12),
          ("docsisDownstream30B", 11),
          ("docsisDownstreamOfdm", 13),
          ("docsisUpstream30", 10),
          ("docsisUpstreamOfdma", 14),
          ("reserved", 1),
          ("videoBroadcastA", 8),
          ("videoBroadcastB", 4),
          ("videoNarrowcastA", 6),
          ("videoNarrowcastB", 2),
          ("videoReplicaBroadcastA", 9),
          ("videoReplicaBroadcastB", 5),
          ("videoReplicaNarrowcastA", 7),
          ("videoReplicaNarrowcastB", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CadChassisLicenseTable_Object = MibTable
cadChassisLicenseTable = _CadChassisLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1)
)
if mibBuilder.loadTexts:
    cadChassisLicenseTable.setStatus("current")
_CadChassisLicenseEntry_Object = MibTableRow
cadChassisLicenseEntry = _CadChassisLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1)
)
cadChassisLicenseEntry.setIndexNames(
    (0, "CADANT-LICENSE-MIB", "cadLicenseIndex"),
)
if mibBuilder.loadTexts:
    cadChassisLicenseEntry.setStatus("current")
_CadLicenseIndex_Type = CadChassisLicenseIndexType
_CadLicenseIndex_Object = MibTableColumn
cadLicenseIndex = _CadLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 1),
    _CadLicenseIndex_Type()
)
cadLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadLicenseIndex.setStatus("current")


class _CadLicenseKey_Type(OctetString):
    """Custom type cadLicenseKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CadLicenseKey_Type.__name__ = "OctetString"
_CadLicenseKey_Object = MibTableColumn
cadLicenseKey = _CadLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 2),
    _CadLicenseKey_Type()
)
cadLicenseKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadLicenseKey.setStatus("current")


class _CadLicenseChannelCount_Type(Unsigned32):
    """Custom type cadLicenseChannelCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_CadLicenseChannelCount_Type.__name__ = "Unsigned32"
_CadLicenseChannelCount_Object = MibTableColumn
cadLicenseChannelCount = _CadLicenseChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 3),
    _CadLicenseChannelCount_Type()
)
cadLicenseChannelCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadLicenseChannelCount.setStatus("current")


class _CadLicenseSpareChannelCount_Type(Unsigned32):
    """Custom type cadLicenseSpareChannelCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )


_CadLicenseSpareChannelCount_Type.__name__ = "Unsigned32"
_CadLicenseSpareChannelCount_Object = MibTableColumn
cadLicenseSpareChannelCount = _CadLicenseSpareChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 4),
    _CadLicenseSpareChannelCount_Type()
)
cadLicenseSpareChannelCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadLicenseSpareChannelCount.setStatus("current")
_CadLicenseRowStatus_Type = RowStatus
_CadLicenseRowStatus_Object = MibTableColumn
cadLicenseRowStatus = _CadLicenseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 5),
    _CadLicenseRowStatus_Type()
)
cadLicenseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadLicenseRowStatus.setStatus("current")
_CadChassisLicenseStatusTable_Object = MibTable
cadChassisLicenseStatusTable = _CadChassisLicenseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2)
)
if mibBuilder.loadTexts:
    cadChassisLicenseStatusTable.setStatus("current")
_CadChassisLicenseStatusEntry_Object = MibTableRow
cadChassisLicenseStatusEntry = _CadChassisLicenseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1)
)
cadChassisLicenseStatusEntry.setIndexNames(
    (0, "CADANT-LICENSE-MIB", "cadChassisLicenseStatusType"),
)
if mibBuilder.loadTexts:
    cadChassisLicenseStatusEntry.setStatus("current")
_CadChassisLicenseStatusType_Type = CadChassisLicenseIndexType
_CadChassisLicenseStatusType_Object = MibTableColumn
cadChassisLicenseStatusType = _CadChassisLicenseStatusType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 1),
    _CadChassisLicenseStatusType_Type()
)
cadChassisLicenseStatusType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadChassisLicenseStatusType.setStatus("current")
_CadChassisLicensesUsed_Type = Unsigned32
_CadChassisLicensesUsed_Object = MibTableColumn
cadChassisLicensesUsed = _CadChassisLicensesUsed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 2),
    _CadChassisLicensesUsed_Type()
)
cadChassisLicensesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChassisLicensesUsed.setStatus("current")
_CadChassisLicensesRequested_Type = Unsigned32
_CadChassisLicensesRequested_Object = MibTableColumn
cadChassisLicensesRequested = _CadChassisLicensesRequested_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 3),
    _CadChassisLicensesRequested_Type()
)
cadChassisLicensesRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChassisLicensesRequested.setStatus("current")
_CadChassisLicensesApplied_Type = Unsigned32
_CadChassisLicensesApplied_Object = MibTableColumn
cadChassisLicensesApplied = _CadChassisLicensesApplied_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 4),
    _CadChassisLicensesApplied_Type()
)
cadChassisLicensesApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChassisLicensesApplied.setStatus("current")
_CadChassisLicensesValid_Type = TruthValue
_CadChassisLicensesValid_Object = MibTableColumn
cadChassisLicensesValid = _CadChassisLicensesValid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 5),
    _CadChassisLicensesValid_Type()
)
cadChassisLicensesValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChassisLicensesValid.setStatus("current")
_CerCardDataLicenseStatusTable_Object = MibTable
cerCardDataLicenseStatusTable = _CerCardDataLicenseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3)
)
if mibBuilder.loadTexts:
    cerCardDataLicenseStatusTable.setStatus("current")
_CerCardDataLicenseStatusEntry_Object = MibTableRow
cerCardDataLicenseStatusEntry = _CerCardDataLicenseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1)
)
cerCardDataLicenseStatusEntry.setIndexNames(
    (0, "CADANT-LICENSE-MIB", "cerCardDataLicenseSlot"),
    (0, "CADANT-LICENSE-MIB", "cerCardDataLicenseType"),
)
if mibBuilder.loadTexts:
    cerCardDataLicenseStatusEntry.setStatus("current")


class _CerCardDataLicenseSlot_Type(Unsigned32):
    """Custom type cerCardDataLicenseSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
        ValueRangeConstraint(9, 14),
    )


_CerCardDataLicenseSlot_Type.__name__ = "Unsigned32"
_CerCardDataLicenseSlot_Object = MibTableColumn
cerCardDataLicenseSlot = _CerCardDataLicenseSlot_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 1),
    _CerCardDataLicenseSlot_Type()
)
cerCardDataLicenseSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerCardDataLicenseSlot.setStatus("current")
_CerCardDataLicenseType_Type = CadChassisLicenseIndexType
_CerCardDataLicenseType_Object = MibTableColumn
cerCardDataLicenseType = _CerCardDataLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 2),
    _CerCardDataLicenseType_Type()
)
cerCardDataLicenseType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerCardDataLicenseType.setStatus("current")
_CerCardDataLicensesUsed_Type = Unsigned32
_CerCardDataLicensesUsed_Object = MibTableColumn
cerCardDataLicensesUsed = _CerCardDataLicensesUsed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 3),
    _CerCardDataLicensesUsed_Type()
)
cerCardDataLicensesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLicensesUsed.setStatus("current")
_CerCardDataLicensesRequested_Type = Unsigned32
_CerCardDataLicensesRequested_Object = MibTableColumn
cerCardDataLicensesRequested = _CerCardDataLicensesRequested_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 4),
    _CerCardDataLicensesRequested_Type()
)
cerCardDataLicensesRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLicensesRequested.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-LICENSE-MIB",
    **{"CadChassisLicenseIndexType": CadChassisLicenseIndexType,
       "cadLicenseMib": cadLicenseMib,
       "cadChassisLicenseTable": cadChassisLicenseTable,
       "cadChassisLicenseEntry": cadChassisLicenseEntry,
       "cadLicenseIndex": cadLicenseIndex,
       "cadLicenseKey": cadLicenseKey,
       "cadLicenseChannelCount": cadLicenseChannelCount,
       "cadLicenseSpareChannelCount": cadLicenseSpareChannelCount,
       "cadLicenseRowStatus": cadLicenseRowStatus,
       "cadChassisLicenseStatusTable": cadChassisLicenseStatusTable,
       "cadChassisLicenseStatusEntry": cadChassisLicenseStatusEntry,
       "cadChassisLicenseStatusType": cadChassisLicenseStatusType,
       "cadChassisLicensesUsed": cadChassisLicensesUsed,
       "cadChassisLicensesRequested": cadChassisLicensesRequested,
       "cadChassisLicensesApplied": cadChassisLicensesApplied,
       "cadChassisLicensesValid": cadChassisLicensesValid,
       "cerCardDataLicenseStatusTable": cerCardDataLicenseStatusTable,
       "cerCardDataLicenseStatusEntry": cerCardDataLicenseStatusEntry,
       "cerCardDataLicenseSlot": cerCardDataLicenseSlot,
       "cerCardDataLicenseType": cerCardDataLicenseType,
       "cerCardDataLicensesUsed": cerCardDataLicensesUsed,
       "cerCardDataLicensesRequested": cerCardDataLicensesRequested}
)
