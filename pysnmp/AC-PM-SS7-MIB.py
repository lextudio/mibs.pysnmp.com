# SNMP MIB module (AC-PM-SS7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-SS7-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:35 2024
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

(acBoardMibs,
 acGeneric,
 acPerformance,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acPerformance",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acPMSS7 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMSS7Configuration_ObjectIdentity = ObjectIdentity
acPMSS7Configuration = _AcPMSS7Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 1)
)


class _AcPMSS7ConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMSS7ConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMSS7ConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMSS7ConfigurationPeriodLength_Object = MibScalar
acPMSS7ConfigurationPeriodLength = _AcPMSS7ConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 1, 1),
    _AcPMSS7ConfigurationPeriodLength_Type()
)
acPMSS7ConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSS7ConfigurationPeriodLength.setStatus("current")


class _AcPMSS7ConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMSS7ConfigurationResetTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetCountersDone", 1),
          ("resetTotalCounters", 2))
    )


_AcPMSS7ConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMSS7ConfigurationResetTotalCounters_Object = MibScalar
acPMSS7ConfigurationResetTotalCounters = _AcPMSS7ConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 1, 2),
    _AcPMSS7ConfigurationResetTotalCounters_Type()
)
acPMSS7ConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSS7ConfigurationResetTotalCounters.setStatus("current")
_AcPMSS7Data_ObjectIdentity = ObjectIdentity
acPMSS7Data = _AcPMSS7Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2)
)


class _AcPMSS7DataTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMSS7DataTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSS7DataTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMSS7DataTimeFromStartOfInterval_Object = MibScalar
acPMSS7DataTimeFromStartOfInterval = _AcPMSS7DataTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 1),
    _AcPMSS7DataTimeFromStartOfInterval_Type()
)
acPMSS7DataTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7DataTimeFromStartOfInterval.setStatus("current")
_AcPMSS7Links_ObjectIdentity = ObjectIdentity
acPMSS7Links = _AcPMSS7Links_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31)
)
_AcPMSS7TxMSUTable_Object = MibTable
acPMSS7TxMSUTable = _AcPMSS7TxMSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 1)
)
if mibBuilder.loadTexts:
    acPMSS7TxMSUTable.setStatus("current")
_AcPMSS7TxMSUEntry_Object = MibTableRow
acPMSS7TxMSUEntry = _AcPMSS7TxMSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 1, 1)
)
acPMSS7TxMSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMSULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxMSUEntry.setStatus("current")


class _AcPMSS7TxMSULink_Type(Unsigned32):
    """Custom type acPMSS7TxMSULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7TxMSULink_Type.__name__ = "Unsigned32"
_AcPMSS7TxMSULink_Object = MibTableColumn
acPMSS7TxMSULink = _AcPMSS7TxMSULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 1, 1, 1),
    _AcPMSS7TxMSULink_Type()
)
acPMSS7TxMSULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMSULink.setStatus("current")


class _AcPMSS7TxMSUInterval_Type(Unsigned32):
    """Custom type acPMSS7TxMSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxMSUInterval_Object = MibTableColumn
acPMSS7TxMSUInterval = _AcPMSS7TxMSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 1, 1, 2),
    _AcPMSS7TxMSUInterval_Type()
)
acPMSS7TxMSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMSUInterval.setStatus("current")
_AcPMSS7TxMSUVal_Type = Counter32
_AcPMSS7TxMSUVal_Object = MibTableColumn
acPMSS7TxMSUVal = _AcPMSS7TxMSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 1, 1, 3),
    _AcPMSS7TxMSUVal_Type()
)
acPMSS7TxMSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMSUVal.setStatus("current")


class _AcPMSS7TxMSUTotal_Type(Integer32):
    """Custom type acPMSS7TxMSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxMSUTotal_Type.__name__ = "Integer32"
_AcPMSS7TxMSUTotal_Object = MibTableColumn
acPMSS7TxMSUTotal = _AcPMSS7TxMSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 1, 1, 4),
    _AcPMSS7TxMSUTotal_Type()
)
acPMSS7TxMSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMSUTotal.setStatus("current")
_AcPMSS7RxMSUTable_Object = MibTable
acPMSS7RxMSUTable = _AcPMSS7RxMSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 2)
)
if mibBuilder.loadTexts:
    acPMSS7RxMSUTable.setStatus("current")
_AcPMSS7RxMSUEntry_Object = MibTableRow
acPMSS7RxMSUEntry = _AcPMSS7RxMSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 2, 1)
)
acPMSS7RxMSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMSULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxMSUEntry.setStatus("current")


class _AcPMSS7RxMSULink_Type(Unsigned32):
    """Custom type acPMSS7RxMSULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7RxMSULink_Type.__name__ = "Unsigned32"
_AcPMSS7RxMSULink_Object = MibTableColumn
acPMSS7RxMSULink = _AcPMSS7RxMSULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 2, 1, 1),
    _AcPMSS7RxMSULink_Type()
)
acPMSS7RxMSULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMSULink.setStatus("current")


class _AcPMSS7RxMSUInterval_Type(Unsigned32):
    """Custom type acPMSS7RxMSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxMSUInterval_Object = MibTableColumn
acPMSS7RxMSUInterval = _AcPMSS7RxMSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 2, 1, 2),
    _AcPMSS7RxMSUInterval_Type()
)
acPMSS7RxMSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMSUInterval.setStatus("current")
_AcPMSS7RxMSUVal_Type = Counter32
_AcPMSS7RxMSUVal_Object = MibTableColumn
acPMSS7RxMSUVal = _AcPMSS7RxMSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 2, 1, 3),
    _AcPMSS7RxMSUVal_Type()
)
acPMSS7RxMSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMSUVal.setStatus("current")


class _AcPMSS7RxMSUTotal_Type(Integer32):
    """Custom type acPMSS7RxMSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxMSUTotal_Type.__name__ = "Integer32"
_AcPMSS7RxMSUTotal_Object = MibTableColumn
acPMSS7RxMSUTotal = _AcPMSS7RxMSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 2, 1, 4),
    _AcPMSS7RxMSUTotal_Type()
)
acPMSS7RxMSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMSUTotal.setStatus("current")
_AcPMSS7TxLSSUTable_Object = MibTable
acPMSS7TxLSSUTable = _AcPMSS7TxLSSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 3)
)
if mibBuilder.loadTexts:
    acPMSS7TxLSSUTable.setStatus("current")
_AcPMSS7TxLSSUEntry_Object = MibTableRow
acPMSS7TxLSSUEntry = _AcPMSS7TxLSSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 3, 1)
)
acPMSS7TxLSSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxLSSULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxLSSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxLSSUEntry.setStatus("current")


class _AcPMSS7TxLSSULink_Type(Unsigned32):
    """Custom type acPMSS7TxLSSULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7TxLSSULink_Type.__name__ = "Unsigned32"
_AcPMSS7TxLSSULink_Object = MibTableColumn
acPMSS7TxLSSULink = _AcPMSS7TxLSSULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 3, 1, 1),
    _AcPMSS7TxLSSULink_Type()
)
acPMSS7TxLSSULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxLSSULink.setStatus("current")


class _AcPMSS7TxLSSUInterval_Type(Unsigned32):
    """Custom type acPMSS7TxLSSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxLSSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxLSSUInterval_Object = MibTableColumn
acPMSS7TxLSSUInterval = _AcPMSS7TxLSSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 3, 1, 2),
    _AcPMSS7TxLSSUInterval_Type()
)
acPMSS7TxLSSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxLSSUInterval.setStatus("current")
_AcPMSS7TxLSSUVal_Type = Counter32
_AcPMSS7TxLSSUVal_Object = MibTableColumn
acPMSS7TxLSSUVal = _AcPMSS7TxLSSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 3, 1, 3),
    _AcPMSS7TxLSSUVal_Type()
)
acPMSS7TxLSSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxLSSUVal.setStatus("current")


class _AcPMSS7TxLSSUTotal_Type(Integer32):
    """Custom type acPMSS7TxLSSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxLSSUTotal_Type.__name__ = "Integer32"
_AcPMSS7TxLSSUTotal_Object = MibTableColumn
acPMSS7TxLSSUTotal = _AcPMSS7TxLSSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 3, 1, 4),
    _AcPMSS7TxLSSUTotal_Type()
)
acPMSS7TxLSSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxLSSUTotal.setStatus("current")
_AcPMSS7RxLSSUTable_Object = MibTable
acPMSS7RxLSSUTable = _AcPMSS7RxLSSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 4)
)
if mibBuilder.loadTexts:
    acPMSS7RxLSSUTable.setStatus("current")
_AcPMSS7RxLSSUEntry_Object = MibTableRow
acPMSS7RxLSSUEntry = _AcPMSS7RxLSSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 4, 1)
)
acPMSS7RxLSSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxLSSULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxLSSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxLSSUEntry.setStatus("current")


class _AcPMSS7RxLSSULink_Type(Unsigned32):
    """Custom type acPMSS7RxLSSULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7RxLSSULink_Type.__name__ = "Unsigned32"
_AcPMSS7RxLSSULink_Object = MibTableColumn
acPMSS7RxLSSULink = _AcPMSS7RxLSSULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 4, 1, 1),
    _AcPMSS7RxLSSULink_Type()
)
acPMSS7RxLSSULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxLSSULink.setStatus("current")


class _AcPMSS7RxLSSUInterval_Type(Unsigned32):
    """Custom type acPMSS7RxLSSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxLSSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxLSSUInterval_Object = MibTableColumn
acPMSS7RxLSSUInterval = _AcPMSS7RxLSSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 4, 1, 2),
    _AcPMSS7RxLSSUInterval_Type()
)
acPMSS7RxLSSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxLSSUInterval.setStatus("current")
_AcPMSS7RxLSSUVal_Type = Counter32
_AcPMSS7RxLSSUVal_Object = MibTableColumn
acPMSS7RxLSSUVal = _AcPMSS7RxLSSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 4, 1, 3),
    _AcPMSS7RxLSSUVal_Type()
)
acPMSS7RxLSSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxLSSUVal.setStatus("current")


class _AcPMSS7RxLSSUTotal_Type(Integer32):
    """Custom type acPMSS7RxLSSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxLSSUTotal_Type.__name__ = "Integer32"
_AcPMSS7RxLSSUTotal_Object = MibTableColumn
acPMSS7RxLSSUTotal = _AcPMSS7RxLSSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 4, 1, 4),
    _AcPMSS7RxLSSUTotal_Type()
)
acPMSS7RxLSSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxLSSUTotal.setStatus("current")
_AcPMSS7TxFISUTable_Object = MibTable
acPMSS7TxFISUTable = _AcPMSS7TxFISUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 5)
)
if mibBuilder.loadTexts:
    acPMSS7TxFISUTable.setStatus("current")
_AcPMSS7TxFISUEntry_Object = MibTableRow
acPMSS7TxFISUEntry = _AcPMSS7TxFISUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 5, 1)
)
acPMSS7TxFISUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxFISULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxFISUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxFISUEntry.setStatus("current")


class _AcPMSS7TxFISULink_Type(Unsigned32):
    """Custom type acPMSS7TxFISULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7TxFISULink_Type.__name__ = "Unsigned32"
_AcPMSS7TxFISULink_Object = MibTableColumn
acPMSS7TxFISULink = _AcPMSS7TxFISULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 5, 1, 1),
    _AcPMSS7TxFISULink_Type()
)
acPMSS7TxFISULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxFISULink.setStatus("current")


class _AcPMSS7TxFISUInterval_Type(Unsigned32):
    """Custom type acPMSS7TxFISUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxFISUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxFISUInterval_Object = MibTableColumn
acPMSS7TxFISUInterval = _AcPMSS7TxFISUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 5, 1, 2),
    _AcPMSS7TxFISUInterval_Type()
)
acPMSS7TxFISUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxFISUInterval.setStatus("current")
_AcPMSS7TxFISUVal_Type = Counter32
_AcPMSS7TxFISUVal_Object = MibTableColumn
acPMSS7TxFISUVal = _AcPMSS7TxFISUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 5, 1, 3),
    _AcPMSS7TxFISUVal_Type()
)
acPMSS7TxFISUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxFISUVal.setStatus("current")


class _AcPMSS7TxFISUTotal_Type(Integer32):
    """Custom type acPMSS7TxFISUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxFISUTotal_Type.__name__ = "Integer32"
_AcPMSS7TxFISUTotal_Object = MibTableColumn
acPMSS7TxFISUTotal = _AcPMSS7TxFISUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 5, 1, 4),
    _AcPMSS7TxFISUTotal_Type()
)
acPMSS7TxFISUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxFISUTotal.setStatus("current")
_AcPMSS7RxFISUTable_Object = MibTable
acPMSS7RxFISUTable = _AcPMSS7RxFISUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 6)
)
if mibBuilder.loadTexts:
    acPMSS7RxFISUTable.setStatus("current")
_AcPMSS7RxFISUEntry_Object = MibTableRow
acPMSS7RxFISUEntry = _AcPMSS7RxFISUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 6, 1)
)
acPMSS7RxFISUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxFISULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxFISUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxFISUEntry.setStatus("current")


class _AcPMSS7RxFISULink_Type(Unsigned32):
    """Custom type acPMSS7RxFISULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7RxFISULink_Type.__name__ = "Unsigned32"
_AcPMSS7RxFISULink_Object = MibTableColumn
acPMSS7RxFISULink = _AcPMSS7RxFISULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 6, 1, 1),
    _AcPMSS7RxFISULink_Type()
)
acPMSS7RxFISULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxFISULink.setStatus("current")


class _AcPMSS7RxFISUInterval_Type(Unsigned32):
    """Custom type acPMSS7RxFISUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxFISUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxFISUInterval_Object = MibTableColumn
acPMSS7RxFISUInterval = _AcPMSS7RxFISUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 6, 1, 2),
    _AcPMSS7RxFISUInterval_Type()
)
acPMSS7RxFISUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxFISUInterval.setStatus("current")
_AcPMSS7RxFISUVal_Type = Counter32
_AcPMSS7RxFISUVal_Object = MibTableColumn
acPMSS7RxFISUVal = _AcPMSS7RxFISUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 6, 1, 3),
    _AcPMSS7RxFISUVal_Type()
)
acPMSS7RxFISUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxFISUVal.setStatus("current")


class _AcPMSS7RxFISUTotal_Type(Integer32):
    """Custom type acPMSS7RxFISUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxFISUTotal_Type.__name__ = "Integer32"
_AcPMSS7RxFISUTotal_Object = MibTableColumn
acPMSS7RxFISUTotal = _AcPMSS7RxFISUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 6, 1, 4),
    _AcPMSS7RxFISUTotal_Type()
)
acPMSS7RxFISUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxFISUTotal.setStatus("current")
_AcPMSS7TxSignalUnitsTable_Object = MibTable
acPMSS7TxSignalUnitsTable = _AcPMSS7TxSignalUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 7)
)
if mibBuilder.loadTexts:
    acPMSS7TxSignalUnitsTable.setStatus("current")
_AcPMSS7TxSignalUnitsEntry_Object = MibTableRow
acPMSS7TxSignalUnitsEntry = _AcPMSS7TxSignalUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 7, 1)
)
acPMSS7TxSignalUnitsEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxSignalUnitsLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxSignalUnitsInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxSignalUnitsEntry.setStatus("current")


class _AcPMSS7TxSignalUnitsLink_Type(Unsigned32):
    """Custom type acPMSS7TxSignalUnitsLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7TxSignalUnitsLink_Type.__name__ = "Unsigned32"
_AcPMSS7TxSignalUnitsLink_Object = MibTableColumn
acPMSS7TxSignalUnitsLink = _AcPMSS7TxSignalUnitsLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 7, 1, 1),
    _AcPMSS7TxSignalUnitsLink_Type()
)
acPMSS7TxSignalUnitsLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxSignalUnitsLink.setStatus("current")


class _AcPMSS7TxSignalUnitsInterval_Type(Unsigned32):
    """Custom type acPMSS7TxSignalUnitsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxSignalUnitsInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxSignalUnitsInterval_Object = MibTableColumn
acPMSS7TxSignalUnitsInterval = _AcPMSS7TxSignalUnitsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 7, 1, 2),
    _AcPMSS7TxSignalUnitsInterval_Type()
)
acPMSS7TxSignalUnitsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxSignalUnitsInterval.setStatus("current")
_AcPMSS7TxSignalUnitsVal_Type = Counter32
_AcPMSS7TxSignalUnitsVal_Object = MibTableColumn
acPMSS7TxSignalUnitsVal = _AcPMSS7TxSignalUnitsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 7, 1, 3),
    _AcPMSS7TxSignalUnitsVal_Type()
)
acPMSS7TxSignalUnitsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxSignalUnitsVal.setStatus("current")


class _AcPMSS7TxSignalUnitsTotal_Type(Integer32):
    """Custom type acPMSS7TxSignalUnitsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxSignalUnitsTotal_Type.__name__ = "Integer32"
_AcPMSS7TxSignalUnitsTotal_Object = MibTableColumn
acPMSS7TxSignalUnitsTotal = _AcPMSS7TxSignalUnitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 7, 1, 4),
    _AcPMSS7TxSignalUnitsTotal_Type()
)
acPMSS7TxSignalUnitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxSignalUnitsTotal.setStatus("current")
_AcPMSS7RxSignalUnitsTable_Object = MibTable
acPMSS7RxSignalUnitsTable = _AcPMSS7RxSignalUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 8)
)
if mibBuilder.loadTexts:
    acPMSS7RxSignalUnitsTable.setStatus("current")
_AcPMSS7RxSignalUnitsEntry_Object = MibTableRow
acPMSS7RxSignalUnitsEntry = _AcPMSS7RxSignalUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 8, 1)
)
acPMSS7RxSignalUnitsEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxSignalUnitsLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxSignalUnitsInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxSignalUnitsEntry.setStatus("current")


class _AcPMSS7RxSignalUnitsLink_Type(Unsigned32):
    """Custom type acPMSS7RxSignalUnitsLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7RxSignalUnitsLink_Type.__name__ = "Unsigned32"
_AcPMSS7RxSignalUnitsLink_Object = MibTableColumn
acPMSS7RxSignalUnitsLink = _AcPMSS7RxSignalUnitsLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 8, 1, 1),
    _AcPMSS7RxSignalUnitsLink_Type()
)
acPMSS7RxSignalUnitsLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxSignalUnitsLink.setStatus("current")


class _AcPMSS7RxSignalUnitsInterval_Type(Unsigned32):
    """Custom type acPMSS7RxSignalUnitsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxSignalUnitsInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxSignalUnitsInterval_Object = MibTableColumn
acPMSS7RxSignalUnitsInterval = _AcPMSS7RxSignalUnitsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 8, 1, 2),
    _AcPMSS7RxSignalUnitsInterval_Type()
)
acPMSS7RxSignalUnitsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxSignalUnitsInterval.setStatus("current")
_AcPMSS7RxSignalUnitsVal_Type = Counter32
_AcPMSS7RxSignalUnitsVal_Object = MibTableColumn
acPMSS7RxSignalUnitsVal = _AcPMSS7RxSignalUnitsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 8, 1, 3),
    _AcPMSS7RxSignalUnitsVal_Type()
)
acPMSS7RxSignalUnitsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxSignalUnitsVal.setStatus("current")


class _AcPMSS7RxSignalUnitsTotal_Type(Integer32):
    """Custom type acPMSS7RxSignalUnitsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxSignalUnitsTotal_Type.__name__ = "Integer32"
_AcPMSS7RxSignalUnitsTotal_Object = MibTableColumn
acPMSS7RxSignalUnitsTotal = _AcPMSS7RxSignalUnitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 8, 1, 4),
    _AcPMSS7RxSignalUnitsTotal_Type()
)
acPMSS7RxSignalUnitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxSignalUnitsTotal.setStatus("current")
_AcPMSS7TxOctetsTable_Object = MibTable
acPMSS7TxOctetsTable = _AcPMSS7TxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 9)
)
if mibBuilder.loadTexts:
    acPMSS7TxOctetsTable.setStatus("current")
_AcPMSS7TxOctetsEntry_Object = MibTableRow
acPMSS7TxOctetsEntry = _AcPMSS7TxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 9, 1)
)
acPMSS7TxOctetsEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxOctetsLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxOctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxOctetsEntry.setStatus("current")


class _AcPMSS7TxOctetsLink_Type(Unsigned32):
    """Custom type acPMSS7TxOctetsLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7TxOctetsLink_Type.__name__ = "Unsigned32"
_AcPMSS7TxOctetsLink_Object = MibTableColumn
acPMSS7TxOctetsLink = _AcPMSS7TxOctetsLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 9, 1, 1),
    _AcPMSS7TxOctetsLink_Type()
)
acPMSS7TxOctetsLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxOctetsLink.setStatus("current")


class _AcPMSS7TxOctetsInterval_Type(Unsigned32):
    """Custom type acPMSS7TxOctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxOctetsInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxOctetsInterval_Object = MibTableColumn
acPMSS7TxOctetsInterval = _AcPMSS7TxOctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 9, 1, 2),
    _AcPMSS7TxOctetsInterval_Type()
)
acPMSS7TxOctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxOctetsInterval.setStatus("current")
_AcPMSS7TxOctetsVal_Type = Counter32
_AcPMSS7TxOctetsVal_Object = MibTableColumn
acPMSS7TxOctetsVal = _AcPMSS7TxOctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 9, 1, 3),
    _AcPMSS7TxOctetsVal_Type()
)
acPMSS7TxOctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxOctetsVal.setStatus("current")


class _AcPMSS7TxOctetsTotal_Type(Integer32):
    """Custom type acPMSS7TxOctetsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxOctetsTotal_Type.__name__ = "Integer32"
_AcPMSS7TxOctetsTotal_Object = MibTableColumn
acPMSS7TxOctetsTotal = _AcPMSS7TxOctetsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 9, 1, 4),
    _AcPMSS7TxOctetsTotal_Type()
)
acPMSS7TxOctetsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxOctetsTotal.setStatus("current")
_AcPMSS7RxOctetsTable_Object = MibTable
acPMSS7RxOctetsTable = _AcPMSS7RxOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 10)
)
if mibBuilder.loadTexts:
    acPMSS7RxOctetsTable.setStatus("current")
_AcPMSS7RxOctetsEntry_Object = MibTableRow
acPMSS7RxOctetsEntry = _AcPMSS7RxOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 10, 1)
)
acPMSS7RxOctetsEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxOctetsLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxOctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxOctetsEntry.setStatus("current")


class _AcPMSS7RxOctetsLink_Type(Unsigned32):
    """Custom type acPMSS7RxOctetsLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7RxOctetsLink_Type.__name__ = "Unsigned32"
_AcPMSS7RxOctetsLink_Object = MibTableColumn
acPMSS7RxOctetsLink = _AcPMSS7RxOctetsLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 10, 1, 1),
    _AcPMSS7RxOctetsLink_Type()
)
acPMSS7RxOctetsLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxOctetsLink.setStatus("current")


class _AcPMSS7RxOctetsInterval_Type(Unsigned32):
    """Custom type acPMSS7RxOctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxOctetsInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxOctetsInterval_Object = MibTableColumn
acPMSS7RxOctetsInterval = _AcPMSS7RxOctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 10, 1, 2),
    _AcPMSS7RxOctetsInterval_Type()
)
acPMSS7RxOctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxOctetsInterval.setStatus("current")
_AcPMSS7RxOctetsVal_Type = Counter32
_AcPMSS7RxOctetsVal_Object = MibTableColumn
acPMSS7RxOctetsVal = _AcPMSS7RxOctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 10, 1, 3),
    _AcPMSS7RxOctetsVal_Type()
)
acPMSS7RxOctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxOctetsVal.setStatus("current")


class _AcPMSS7RxOctetsTotal_Type(Integer32):
    """Custom type acPMSS7RxOctetsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxOctetsTotal_Type.__name__ = "Integer32"
_AcPMSS7RxOctetsTotal_Object = MibTableColumn
acPMSS7RxOctetsTotal = _AcPMSS7RxOctetsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 10, 1, 4),
    _AcPMSS7RxOctetsTotal_Type()
)
acPMSS7RxOctetsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxOctetsTotal.setStatus("current")
_AcPMSS7MTP2NoAckRxTable_Object = MibTable
acPMSS7MTP2NoAckRxTable = _AcPMSS7MTP2NoAckRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 11)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2NoAckRxTable.setStatus("current")
_AcPMSS7MTP2NoAckRxEntry_Object = MibTableRow
acPMSS7MTP2NoAckRxEntry = _AcPMSS7MTP2NoAckRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 11, 1)
)
acPMSS7MTP2NoAckRxEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2NoAckRxLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2NoAckRxInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2NoAckRxEntry.setStatus("current")


class _AcPMSS7MTP2NoAckRxLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2NoAckRxLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2NoAckRxLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2NoAckRxLink_Object = MibTableColumn
acPMSS7MTP2NoAckRxLink = _AcPMSS7MTP2NoAckRxLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 11, 1, 1),
    _AcPMSS7MTP2NoAckRxLink_Type()
)
acPMSS7MTP2NoAckRxLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2NoAckRxLink.setStatus("current")


class _AcPMSS7MTP2NoAckRxInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2NoAckRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2NoAckRxInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2NoAckRxInterval_Object = MibTableColumn
acPMSS7MTP2NoAckRxInterval = _AcPMSS7MTP2NoAckRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 11, 1, 2),
    _AcPMSS7MTP2NoAckRxInterval_Type()
)
acPMSS7MTP2NoAckRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2NoAckRxInterval.setStatus("current")
_AcPMSS7MTP2NoAckRxVal_Type = Counter32
_AcPMSS7MTP2NoAckRxVal_Object = MibTableColumn
acPMSS7MTP2NoAckRxVal = _AcPMSS7MTP2NoAckRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 11, 1, 3),
    _AcPMSS7MTP2NoAckRxVal_Type()
)
acPMSS7MTP2NoAckRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2NoAckRxVal.setStatus("current")


class _AcPMSS7MTP2NoAckRxTotal_Type(Integer32):
    """Custom type acPMSS7MTP2NoAckRxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2NoAckRxTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2NoAckRxTotal_Object = MibTableColumn
acPMSS7MTP2NoAckRxTotal = _AcPMSS7MTP2NoAckRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 11, 1, 4),
    _AcPMSS7MTP2NoAckRxTotal_Type()
)
acPMSS7MTP2NoAckRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2NoAckRxTotal.setStatus("current")
_AcPMSS7DiscMSUTable_Object = MibTable
acPMSS7DiscMSUTable = _AcPMSS7DiscMSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 12)
)
if mibBuilder.loadTexts:
    acPMSS7DiscMSUTable.setStatus("current")
_AcPMSS7DiscMSUEntry_Object = MibTableRow
acPMSS7DiscMSUEntry = _AcPMSS7DiscMSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 12, 1)
)
acPMSS7DiscMSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7DiscMSULink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7DiscMSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7DiscMSUEntry.setStatus("current")


class _AcPMSS7DiscMSULink_Type(Unsigned32):
    """Custom type acPMSS7DiscMSULink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7DiscMSULink_Type.__name__ = "Unsigned32"
_AcPMSS7DiscMSULink_Object = MibTableColumn
acPMSS7DiscMSULink = _AcPMSS7DiscMSULink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 12, 1, 1),
    _AcPMSS7DiscMSULink_Type()
)
acPMSS7DiscMSULink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7DiscMSULink.setStatus("current")


class _AcPMSS7DiscMSUInterval_Type(Unsigned32):
    """Custom type acPMSS7DiscMSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7DiscMSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7DiscMSUInterval_Object = MibTableColumn
acPMSS7DiscMSUInterval = _AcPMSS7DiscMSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 12, 1, 2),
    _AcPMSS7DiscMSUInterval_Type()
)
acPMSS7DiscMSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7DiscMSUInterval.setStatus("current")
_AcPMSS7DiscMSUVal_Type = Counter32
_AcPMSS7DiscMSUVal_Object = MibTableColumn
acPMSS7DiscMSUVal = _AcPMSS7DiscMSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 12, 1, 3),
    _AcPMSS7DiscMSUVal_Type()
)
acPMSS7DiscMSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7DiscMSUVal.setStatus("current")


class _AcPMSS7DiscMSUTotal_Type(Integer32):
    """Custom type acPMSS7DiscMSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7DiscMSUTotal_Type.__name__ = "Integer32"
_AcPMSS7DiscMSUTotal_Object = MibTableColumn
acPMSS7DiscMSUTotal = _AcPMSS7DiscMSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 12, 1, 4),
    _AcPMSS7DiscMSUTotal_Type()
)
acPMSS7DiscMSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7DiscMSUTotal.setStatus("current")
_AcPMSS7InServiceTable_Object = MibTable
acPMSS7InServiceTable = _AcPMSS7InServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13)
)
if mibBuilder.loadTexts:
    acPMSS7InServiceTable.setStatus("current")
_AcPMSS7InServiceEntry_Object = MibTableRow
acPMSS7InServiceEntry = _AcPMSS7InServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13, 1)
)
acPMSS7InServiceEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7InServiceLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7InServiceInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7InServiceEntry.setStatus("current")


class _AcPMSS7InServiceLink_Type(Unsigned32):
    """Custom type acPMSS7InServiceLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7InServiceLink_Type.__name__ = "Unsigned32"
_AcPMSS7InServiceLink_Object = MibTableColumn
acPMSS7InServiceLink = _AcPMSS7InServiceLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13, 1, 1),
    _AcPMSS7InServiceLink_Type()
)
acPMSS7InServiceLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7InServiceLink.setStatus("current")


class _AcPMSS7InServiceInterval_Type(Unsigned32):
    """Custom type acPMSS7InServiceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7InServiceInterval_Type.__name__ = "Unsigned32"
_AcPMSS7InServiceInterval_Object = MibTableColumn
acPMSS7InServiceInterval = _AcPMSS7InServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13, 1, 2),
    _AcPMSS7InServiceInterval_Type()
)
acPMSS7InServiceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7InServiceInterval.setStatus("current")
_AcPMSS7InServiceVal_Type = Gauge32
_AcPMSS7InServiceVal_Object = MibTableColumn
acPMSS7InServiceVal = _AcPMSS7InServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13, 1, 3),
    _AcPMSS7InServiceVal_Type()
)
acPMSS7InServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7InServiceVal.setStatus("current")


class _AcPMSS7InServiceTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMSS7InServiceTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7InServiceTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMSS7InServiceTimeAboveHighThreshold_Object = MibTableColumn
acPMSS7InServiceTimeAboveHighThreshold = _AcPMSS7InServiceTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13, 1, 4),
    _AcPMSS7InServiceTimeAboveHighThreshold_Type()
)
acPMSS7InServiceTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7InServiceTimeAboveHighThreshold.setStatus("current")


class _AcPMSS7InServiceTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMSS7InServiceTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7InServiceTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMSS7InServiceTimeBetweenThresholds_Object = MibTableColumn
acPMSS7InServiceTimeBetweenThresholds = _AcPMSS7InServiceTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 13, 1, 5),
    _AcPMSS7InServiceTimeBetweenThresholds_Type()
)
acPMSS7InServiceTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7InServiceTimeBetweenThresholds.setStatus("current")
_AcPMSS7OutOfServiceTable_Object = MibTable
acPMSS7OutOfServiceTable = _AcPMSS7OutOfServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14)
)
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceTable.setStatus("current")
_AcPMSS7OutOfServiceEntry_Object = MibTableRow
acPMSS7OutOfServiceEntry = _AcPMSS7OutOfServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14, 1)
)
acPMSS7OutOfServiceEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7OutOfServiceLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7OutOfServiceInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceEntry.setStatus("current")


class _AcPMSS7OutOfServiceLink_Type(Unsigned32):
    """Custom type acPMSS7OutOfServiceLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7OutOfServiceLink_Type.__name__ = "Unsigned32"
_AcPMSS7OutOfServiceLink_Object = MibTableColumn
acPMSS7OutOfServiceLink = _AcPMSS7OutOfServiceLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14, 1, 1),
    _AcPMSS7OutOfServiceLink_Type()
)
acPMSS7OutOfServiceLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceLink.setStatus("current")


class _AcPMSS7OutOfServiceInterval_Type(Unsigned32):
    """Custom type acPMSS7OutOfServiceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7OutOfServiceInterval_Type.__name__ = "Unsigned32"
_AcPMSS7OutOfServiceInterval_Object = MibTableColumn
acPMSS7OutOfServiceInterval = _AcPMSS7OutOfServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14, 1, 2),
    _AcPMSS7OutOfServiceInterval_Type()
)
acPMSS7OutOfServiceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceInterval.setStatus("current")
_AcPMSS7OutOfServiceVal_Type = Gauge32
_AcPMSS7OutOfServiceVal_Object = MibTableColumn
acPMSS7OutOfServiceVal = _AcPMSS7OutOfServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14, 1, 3),
    _AcPMSS7OutOfServiceVal_Type()
)
acPMSS7OutOfServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceVal.setStatus("current")


class _AcPMSS7OutOfServiceTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMSS7OutOfServiceTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7OutOfServiceTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMSS7OutOfServiceTimeAboveHighThreshold_Object = MibTableColumn
acPMSS7OutOfServiceTimeAboveHighThreshold = _AcPMSS7OutOfServiceTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14, 1, 4),
    _AcPMSS7OutOfServiceTimeAboveHighThreshold_Type()
)
acPMSS7OutOfServiceTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceTimeAboveHighThreshold.setStatus("current")


class _AcPMSS7OutOfServiceTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMSS7OutOfServiceTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7OutOfServiceTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMSS7OutOfServiceTimeBetweenThresholds_Object = MibTableColumn
acPMSS7OutOfServiceTimeBetweenThresholds = _AcPMSS7OutOfServiceTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 31, 14, 1, 5),
    _AcPMSS7OutOfServiceTimeBetweenThresholds_Type()
)
acPMSS7OutOfServiceTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7OutOfServiceTimeBetweenThresholds.setStatus("current")
_AcPMSS7LinkSets_ObjectIdentity = ObjectIdentity
acPMSS7LinkSets = _AcPMSS7LinkSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41)
)
_AcPMSS7SN0LSOutOfServiceTable_Object = MibTable
acPMSS7SN0LSOutOfServiceTable = _AcPMSS7SN0LSOutOfServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1)
)
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceTable.setStatus("current")
_AcPMSS7SN0LSOutOfServiceEntry_Object = MibTableRow
acPMSS7SN0LSOutOfServiceEntry = _AcPMSS7SN0LSOutOfServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1, 1)
)
acPMSS7SN0LSOutOfServiceEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7SN0LSOutOfServiceLinkSet"),
    (0, "AC-PM-SS7-MIB", "acPMSS7SN0LSOutOfServiceInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceEntry.setStatus("current")


class _AcPMSS7SN0LSOutOfServiceLinkSet_Type(Unsigned32):
    """Custom type acPMSS7SN0LSOutOfServiceLinkSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AcPMSS7SN0LSOutOfServiceLinkSet_Type.__name__ = "Unsigned32"
_AcPMSS7SN0LSOutOfServiceLinkSet_Object = MibTableColumn
acPMSS7SN0LSOutOfServiceLinkSet = _AcPMSS7SN0LSOutOfServiceLinkSet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1, 1, 1),
    _AcPMSS7SN0LSOutOfServiceLinkSet_Type()
)
acPMSS7SN0LSOutOfServiceLinkSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceLinkSet.setStatus("current")


class _AcPMSS7SN0LSOutOfServiceInterval_Type(Unsigned32):
    """Custom type acPMSS7SN0LSOutOfServiceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7SN0LSOutOfServiceInterval_Type.__name__ = "Unsigned32"
_AcPMSS7SN0LSOutOfServiceInterval_Object = MibTableColumn
acPMSS7SN0LSOutOfServiceInterval = _AcPMSS7SN0LSOutOfServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1, 1, 2),
    _AcPMSS7SN0LSOutOfServiceInterval_Type()
)
acPMSS7SN0LSOutOfServiceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceInterval.setStatus("current")
_AcPMSS7SN0LSOutOfServiceVal_Type = Gauge32
_AcPMSS7SN0LSOutOfServiceVal_Object = MibTableColumn
acPMSS7SN0LSOutOfServiceVal = _AcPMSS7SN0LSOutOfServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1, 1, 3),
    _AcPMSS7SN0LSOutOfServiceVal_Type()
)
acPMSS7SN0LSOutOfServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceVal.setStatus("current")


class _AcPMSS7SN0LSOutOfServiceTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMSS7SN0LSOutOfServiceTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7SN0LSOutOfServiceTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMSS7SN0LSOutOfServiceTimeAboveHighThreshold_Object = MibTableColumn
acPMSS7SN0LSOutOfServiceTimeAboveHighThreshold = _AcPMSS7SN0LSOutOfServiceTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1, 1, 4),
    _AcPMSS7SN0LSOutOfServiceTimeAboveHighThreshold_Type()
)
acPMSS7SN0LSOutOfServiceTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceTimeAboveHighThreshold.setStatus("current")


class _AcPMSS7SN0LSOutOfServiceTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMSS7SN0LSOutOfServiceTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7SN0LSOutOfServiceTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMSS7SN0LSOutOfServiceTimeBetweenThresholds_Object = MibTableColumn
acPMSS7SN0LSOutOfServiceTimeBetweenThresholds = _AcPMSS7SN0LSOutOfServiceTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 1, 1, 5),
    _AcPMSS7SN0LSOutOfServiceTimeBetweenThresholds_Type()
)
acPMSS7SN0LSOutOfServiceTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7SN0LSOutOfServiceTimeBetweenThresholds.setStatus("current")
_AcPMSS7SN1LSOutOfServiceTable_Object = MibTable
acPMSS7SN1LSOutOfServiceTable = _AcPMSS7SN1LSOutOfServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2)
)
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceTable.setStatus("current")
_AcPMSS7SN1LSOutOfServiceEntry_Object = MibTableRow
acPMSS7SN1LSOutOfServiceEntry = _AcPMSS7SN1LSOutOfServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2, 1)
)
acPMSS7SN1LSOutOfServiceEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7SN1LSOutOfServiceLinkSet"),
    (0, "AC-PM-SS7-MIB", "acPMSS7SN1LSOutOfServiceInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceEntry.setStatus("current")


class _AcPMSS7SN1LSOutOfServiceLinkSet_Type(Unsigned32):
    """Custom type acPMSS7SN1LSOutOfServiceLinkSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AcPMSS7SN1LSOutOfServiceLinkSet_Type.__name__ = "Unsigned32"
_AcPMSS7SN1LSOutOfServiceLinkSet_Object = MibTableColumn
acPMSS7SN1LSOutOfServiceLinkSet = _AcPMSS7SN1LSOutOfServiceLinkSet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2, 1, 1),
    _AcPMSS7SN1LSOutOfServiceLinkSet_Type()
)
acPMSS7SN1LSOutOfServiceLinkSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceLinkSet.setStatus("current")


class _AcPMSS7SN1LSOutOfServiceInterval_Type(Unsigned32):
    """Custom type acPMSS7SN1LSOutOfServiceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7SN1LSOutOfServiceInterval_Type.__name__ = "Unsigned32"
_AcPMSS7SN1LSOutOfServiceInterval_Object = MibTableColumn
acPMSS7SN1LSOutOfServiceInterval = _AcPMSS7SN1LSOutOfServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2, 1, 2),
    _AcPMSS7SN1LSOutOfServiceInterval_Type()
)
acPMSS7SN1LSOutOfServiceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceInterval.setStatus("current")
_AcPMSS7SN1LSOutOfServiceVal_Type = Gauge32
_AcPMSS7SN1LSOutOfServiceVal_Object = MibTableColumn
acPMSS7SN1LSOutOfServiceVal = _AcPMSS7SN1LSOutOfServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2, 1, 3),
    _AcPMSS7SN1LSOutOfServiceVal_Type()
)
acPMSS7SN1LSOutOfServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceVal.setStatus("current")


class _AcPMSS7SN1LSOutOfServiceTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMSS7SN1LSOutOfServiceTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7SN1LSOutOfServiceTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMSS7SN1LSOutOfServiceTimeAboveHighThreshold_Object = MibTableColumn
acPMSS7SN1LSOutOfServiceTimeAboveHighThreshold = _AcPMSS7SN1LSOutOfServiceTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2, 1, 4),
    _AcPMSS7SN1LSOutOfServiceTimeAboveHighThreshold_Type()
)
acPMSS7SN1LSOutOfServiceTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceTimeAboveHighThreshold.setStatus("current")


class _AcPMSS7SN1LSOutOfServiceTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMSS7SN1LSOutOfServiceTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSS7SN1LSOutOfServiceTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMSS7SN1LSOutOfServiceTimeBetweenThresholds_Object = MibTableColumn
acPMSS7SN1LSOutOfServiceTimeBetweenThresholds = _AcPMSS7SN1LSOutOfServiceTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 41, 2, 1, 5),
    _AcPMSS7SN1LSOutOfServiceTimeBetweenThresholds_Type()
)
acPMSS7SN1LSOutOfServiceTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7SN1LSOutOfServiceTimeBetweenThresholds.setStatus("current")
_AcPMSS7SignalingNodes_ObjectIdentity = ObjectIdentity
acPMSS7SignalingNodes = _AcPMSS7SignalingNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51)
)
_AcPMSS7TxMTP3OctetsTable_Object = MibTable
acPMSS7TxMTP3OctetsTable = _AcPMSS7TxMTP3OctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 1)
)
if mibBuilder.loadTexts:
    acPMSS7TxMTP3OctetsTable.setStatus("current")
_AcPMSS7TxMTP3OctetsEntry_Object = MibTableRow
acPMSS7TxMTP3OctetsEntry = _AcPMSS7TxMTP3OctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 1, 1)
)
acPMSS7TxMTP3OctetsEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMTP3OctetsSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMTP3OctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxMTP3OctetsEntry.setStatus("current")


class _AcPMSS7TxMTP3OctetsSN_Type(Unsigned32):
    """Custom type acPMSS7TxMTP3OctetsSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMTP3OctetsSN_Type.__name__ = "Unsigned32"
_AcPMSS7TxMTP3OctetsSN_Object = MibTableColumn
acPMSS7TxMTP3OctetsSN = _AcPMSS7TxMTP3OctetsSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 1, 1, 1),
    _AcPMSS7TxMTP3OctetsSN_Type()
)
acPMSS7TxMTP3OctetsSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3OctetsSN.setStatus("current")


class _AcPMSS7TxMTP3OctetsInterval_Type(Unsigned32):
    """Custom type acPMSS7TxMTP3OctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMTP3OctetsInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxMTP3OctetsInterval_Object = MibTableColumn
acPMSS7TxMTP3OctetsInterval = _AcPMSS7TxMTP3OctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 1, 1, 2),
    _AcPMSS7TxMTP3OctetsInterval_Type()
)
acPMSS7TxMTP3OctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3OctetsInterval.setStatus("current")
_AcPMSS7TxMTP3OctetsVal_Type = Counter32
_AcPMSS7TxMTP3OctetsVal_Object = MibTableColumn
acPMSS7TxMTP3OctetsVal = _AcPMSS7TxMTP3OctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 1, 1, 3),
    _AcPMSS7TxMTP3OctetsVal_Type()
)
acPMSS7TxMTP3OctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3OctetsVal.setStatus("current")


class _AcPMSS7TxMTP3OctetsTotal_Type(Integer32):
    """Custom type acPMSS7TxMTP3OctetsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxMTP3OctetsTotal_Type.__name__ = "Integer32"
_AcPMSS7TxMTP3OctetsTotal_Object = MibTableColumn
acPMSS7TxMTP3OctetsTotal = _AcPMSS7TxMTP3OctetsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 1, 1, 4),
    _AcPMSS7TxMTP3OctetsTotal_Type()
)
acPMSS7TxMTP3OctetsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3OctetsTotal.setStatus("current")
_AcPMSS7RxMTP3OctetsTable_Object = MibTable
acPMSS7RxMTP3OctetsTable = _AcPMSS7RxMTP3OctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 2)
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3OctetsTable.setStatus("current")
_AcPMSS7RxMTP3OctetsEntry_Object = MibTableRow
acPMSS7RxMTP3OctetsEntry = _AcPMSS7RxMTP3OctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 2, 1)
)
acPMSS7RxMTP3OctetsEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3OctetsSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3OctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3OctetsEntry.setStatus("current")


class _AcPMSS7RxMTP3OctetsSN_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3OctetsSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3OctetsSN_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3OctetsSN_Object = MibTableColumn
acPMSS7RxMTP3OctetsSN = _AcPMSS7RxMTP3OctetsSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 2, 1, 1),
    _AcPMSS7RxMTP3OctetsSN_Type()
)
acPMSS7RxMTP3OctetsSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3OctetsSN.setStatus("current")


class _AcPMSS7RxMTP3OctetsInterval_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3OctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3OctetsInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3OctetsInterval_Object = MibTableColumn
acPMSS7RxMTP3OctetsInterval = _AcPMSS7RxMTP3OctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 2, 1, 2),
    _AcPMSS7RxMTP3OctetsInterval_Type()
)
acPMSS7RxMTP3OctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3OctetsInterval.setStatus("current")
_AcPMSS7RxMTP3OctetsVal_Type = Counter32
_AcPMSS7RxMTP3OctetsVal_Object = MibTableColumn
acPMSS7RxMTP3OctetsVal = _AcPMSS7RxMTP3OctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 2, 1, 3),
    _AcPMSS7RxMTP3OctetsVal_Type()
)
acPMSS7RxMTP3OctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3OctetsVal.setStatus("current")


class _AcPMSS7RxMTP3OctetsTotal_Type(Integer32):
    """Custom type acPMSS7RxMTP3OctetsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxMTP3OctetsTotal_Type.__name__ = "Integer32"
_AcPMSS7RxMTP3OctetsTotal_Object = MibTableColumn
acPMSS7RxMTP3OctetsTotal = _AcPMSS7RxMTP3OctetsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 2, 1, 4),
    _AcPMSS7RxMTP3OctetsTotal_Type()
)
acPMSS7RxMTP3OctetsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3OctetsTotal.setStatus("current")
_AcPMSS7TxMTP3MSUTable_Object = MibTable
acPMSS7TxMTP3MSUTable = _AcPMSS7TxMTP3MSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 3)
)
if mibBuilder.loadTexts:
    acPMSS7TxMTP3MSUTable.setStatus("current")
_AcPMSS7TxMTP3MSUEntry_Object = MibTableRow
acPMSS7TxMTP3MSUEntry = _AcPMSS7TxMTP3MSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 3, 1)
)
acPMSS7TxMTP3MSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMTP3MSUSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMTP3MSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxMTP3MSUEntry.setStatus("current")


class _AcPMSS7TxMTP3MSUSN_Type(Unsigned32):
    """Custom type acPMSS7TxMTP3MSUSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMTP3MSUSN_Type.__name__ = "Unsigned32"
_AcPMSS7TxMTP3MSUSN_Object = MibTableColumn
acPMSS7TxMTP3MSUSN = _AcPMSS7TxMTP3MSUSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 3, 1, 1),
    _AcPMSS7TxMTP3MSUSN_Type()
)
acPMSS7TxMTP3MSUSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3MSUSN.setStatus("current")


class _AcPMSS7TxMTP3MSUInterval_Type(Unsigned32):
    """Custom type acPMSS7TxMTP3MSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMTP3MSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxMTP3MSUInterval_Object = MibTableColumn
acPMSS7TxMTP3MSUInterval = _AcPMSS7TxMTP3MSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 3, 1, 2),
    _AcPMSS7TxMTP3MSUInterval_Type()
)
acPMSS7TxMTP3MSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3MSUInterval.setStatus("current")
_AcPMSS7TxMTP3MSUVal_Type = Counter32
_AcPMSS7TxMTP3MSUVal_Object = MibTableColumn
acPMSS7TxMTP3MSUVal = _AcPMSS7TxMTP3MSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 3, 1, 3),
    _AcPMSS7TxMTP3MSUVal_Type()
)
acPMSS7TxMTP3MSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3MSUVal.setStatus("current")


class _AcPMSS7TxMTP3MSUTotal_Type(Integer32):
    """Custom type acPMSS7TxMTP3MSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxMTP3MSUTotal_Type.__name__ = "Integer32"
_AcPMSS7TxMTP3MSUTotal_Object = MibTableColumn
acPMSS7TxMTP3MSUTotal = _AcPMSS7TxMTP3MSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 3, 1, 4),
    _AcPMSS7TxMTP3MSUTotal_Type()
)
acPMSS7TxMTP3MSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3MSUTotal.setStatus("current")
_AcPMSS7RxMTP3MSUTable_Object = MibTable
acPMSS7RxMTP3MSUTable = _AcPMSS7RxMTP3MSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 4)
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3MSUTable.setStatus("current")
_AcPMSS7RxMTP3MSUEntry_Object = MibTableRow
acPMSS7RxMTP3MSUEntry = _AcPMSS7RxMTP3MSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 4, 1)
)
acPMSS7RxMTP3MSUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3MSUSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3MSUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3MSUEntry.setStatus("current")


class _AcPMSS7RxMTP3MSUSN_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3MSUSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3MSUSN_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3MSUSN_Object = MibTableColumn
acPMSS7RxMTP3MSUSN = _AcPMSS7RxMTP3MSUSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 4, 1, 1),
    _AcPMSS7RxMTP3MSUSN_Type()
)
acPMSS7RxMTP3MSUSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3MSUSN.setStatus("current")


class _AcPMSS7RxMTP3MSUInterval_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3MSUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3MSUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3MSUInterval_Object = MibTableColumn
acPMSS7RxMTP3MSUInterval = _AcPMSS7RxMTP3MSUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 4, 1, 2),
    _AcPMSS7RxMTP3MSUInterval_Type()
)
acPMSS7RxMTP3MSUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3MSUInterval.setStatus("current")
_AcPMSS7RxMTP3MSUVal_Type = Counter32
_AcPMSS7RxMTP3MSUVal_Object = MibTableColumn
acPMSS7RxMTP3MSUVal = _AcPMSS7RxMTP3MSUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 4, 1, 3),
    _AcPMSS7RxMTP3MSUVal_Type()
)
acPMSS7RxMTP3MSUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3MSUVal.setStatus("current")


class _AcPMSS7RxMTP3MSUTotal_Type(Integer32):
    """Custom type acPMSS7RxMTP3MSUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxMTP3MSUTotal_Type.__name__ = "Integer32"
_AcPMSS7RxMTP3MSUTotal_Object = MibTableColumn
acPMSS7RxMTP3MSUTotal = _AcPMSS7RxMTP3MSUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 4, 1, 4),
    _AcPMSS7RxMTP3MSUTotal_Type()
)
acPMSS7RxMTP3MSUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3MSUTotal.setStatus("current")
_AcPMSS7TxMTP3UPUTable_Object = MibTable
acPMSS7TxMTP3UPUTable = _AcPMSS7TxMTP3UPUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 5)
)
if mibBuilder.loadTexts:
    acPMSS7TxMTP3UPUTable.setStatus("current")
_AcPMSS7TxMTP3UPUEntry_Object = MibTableRow
acPMSS7TxMTP3UPUEntry = _AcPMSS7TxMTP3UPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 5, 1)
)
acPMSS7TxMTP3UPUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMTP3UPUSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7TxMTP3UPUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7TxMTP3UPUEntry.setStatus("current")


class _AcPMSS7TxMTP3UPUSN_Type(Unsigned32):
    """Custom type acPMSS7TxMTP3UPUSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMTP3UPUSN_Type.__name__ = "Unsigned32"
_AcPMSS7TxMTP3UPUSN_Object = MibTableColumn
acPMSS7TxMTP3UPUSN = _AcPMSS7TxMTP3UPUSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 5, 1, 1),
    _AcPMSS7TxMTP3UPUSN_Type()
)
acPMSS7TxMTP3UPUSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3UPUSN.setStatus("current")


class _AcPMSS7TxMTP3UPUInterval_Type(Unsigned32):
    """Custom type acPMSS7TxMTP3UPUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7TxMTP3UPUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7TxMTP3UPUInterval_Object = MibTableColumn
acPMSS7TxMTP3UPUInterval = _AcPMSS7TxMTP3UPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 5, 1, 2),
    _AcPMSS7TxMTP3UPUInterval_Type()
)
acPMSS7TxMTP3UPUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3UPUInterval.setStatus("current")
_AcPMSS7TxMTP3UPUVal_Type = Counter32
_AcPMSS7TxMTP3UPUVal_Object = MibTableColumn
acPMSS7TxMTP3UPUVal = _AcPMSS7TxMTP3UPUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 5, 1, 3),
    _AcPMSS7TxMTP3UPUVal_Type()
)
acPMSS7TxMTP3UPUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3UPUVal.setStatus("current")


class _AcPMSS7TxMTP3UPUTotal_Type(Integer32):
    """Custom type acPMSS7TxMTP3UPUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7TxMTP3UPUTotal_Type.__name__ = "Integer32"
_AcPMSS7TxMTP3UPUTotal_Object = MibTableColumn
acPMSS7TxMTP3UPUTotal = _AcPMSS7TxMTP3UPUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 5, 1, 4),
    _AcPMSS7TxMTP3UPUTotal_Type()
)
acPMSS7TxMTP3UPUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7TxMTP3UPUTotal.setStatus("current")
_AcPMSS7RxMTP3UPUTable_Object = MibTable
acPMSS7RxMTP3UPUTable = _AcPMSS7RxMTP3UPUTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 6)
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3UPUTable.setStatus("current")
_AcPMSS7RxMTP3UPUEntry_Object = MibTableRow
acPMSS7RxMTP3UPUEntry = _AcPMSS7RxMTP3UPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 6, 1)
)
acPMSS7RxMTP3UPUEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3UPUSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3UPUInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3UPUEntry.setStatus("current")


class _AcPMSS7RxMTP3UPUSN_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3UPUSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3UPUSN_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3UPUSN_Object = MibTableColumn
acPMSS7RxMTP3UPUSN = _AcPMSS7RxMTP3UPUSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 6, 1, 1),
    _AcPMSS7RxMTP3UPUSN_Type()
)
acPMSS7RxMTP3UPUSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3UPUSN.setStatus("current")


class _AcPMSS7RxMTP3UPUInterval_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3UPUInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3UPUInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3UPUInterval_Object = MibTableColumn
acPMSS7RxMTP3UPUInterval = _AcPMSS7RxMTP3UPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 6, 1, 2),
    _AcPMSS7RxMTP3UPUInterval_Type()
)
acPMSS7RxMTP3UPUInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3UPUInterval.setStatus("current")
_AcPMSS7RxMTP3UPUVal_Type = Counter32
_AcPMSS7RxMTP3UPUVal_Object = MibTableColumn
acPMSS7RxMTP3UPUVal = _AcPMSS7RxMTP3UPUVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 6, 1, 3),
    _AcPMSS7RxMTP3UPUVal_Type()
)
acPMSS7RxMTP3UPUVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3UPUVal.setStatus("current")


class _AcPMSS7RxMTP3UPUTotal_Type(Integer32):
    """Custom type acPMSS7RxMTP3UPUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxMTP3UPUTotal_Type.__name__ = "Integer32"
_AcPMSS7RxMTP3UPUTotal_Object = MibTableColumn
acPMSS7RxMTP3UPUTotal = _AcPMSS7RxMTP3UPUTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 6, 1, 4),
    _AcPMSS7RxMTP3UPUTotal_Type()
)
acPMSS7RxMTP3UPUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3UPUTotal.setStatus("current")
_AcPMSS7MTP3MSUDiscardedTable_Object = MibTable
acPMSS7MTP3MSUDiscardedTable = _AcPMSS7MTP3MSUDiscardedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 7)
)
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedTable.setStatus("current")
_AcPMSS7MTP3MSUDiscardedEntry_Object = MibTableRow
acPMSS7MTP3MSUDiscardedEntry = _AcPMSS7MTP3MSUDiscardedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 7, 1)
)
acPMSS7MTP3MSUDiscardedEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP3MSUDiscardedSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP3MSUDiscardedInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedEntry.setStatus("current")


class _AcPMSS7MTP3MSUDiscardedSN_Type(Unsigned32):
    """Custom type acPMSS7MTP3MSUDiscardedSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP3MSUDiscardedSN_Type.__name__ = "Unsigned32"
_AcPMSS7MTP3MSUDiscardedSN_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedSN = _AcPMSS7MTP3MSUDiscardedSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 7, 1, 1),
    _AcPMSS7MTP3MSUDiscardedSN_Type()
)
acPMSS7MTP3MSUDiscardedSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedSN.setStatus("current")


class _AcPMSS7MTP3MSUDiscardedInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP3MSUDiscardedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP3MSUDiscardedInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP3MSUDiscardedInterval_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedInterval = _AcPMSS7MTP3MSUDiscardedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 7, 1, 2),
    _AcPMSS7MTP3MSUDiscardedInterval_Type()
)
acPMSS7MTP3MSUDiscardedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedInterval.setStatus("current")
_AcPMSS7MTP3MSUDiscardedVal_Type = Counter32
_AcPMSS7MTP3MSUDiscardedVal_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedVal = _AcPMSS7MTP3MSUDiscardedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 7, 1, 3),
    _AcPMSS7MTP3MSUDiscardedVal_Type()
)
acPMSS7MTP3MSUDiscardedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedVal.setStatus("current")


class _AcPMSS7MTP3MSUDiscardedTotal_Type(Integer32):
    """Custom type acPMSS7MTP3MSUDiscardedTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP3MSUDiscardedTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP3MSUDiscardedTotal_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedTotal = _AcPMSS7MTP3MSUDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 7, 1, 4),
    _AcPMSS7MTP3MSUDiscardedTotal_Type()
)
acPMSS7MTP3MSUDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedTotal.setStatus("current")
_AcPMSS7MTP3MSUDiscardedRtDataErrTable_Object = MibTable
acPMSS7MTP3MSUDiscardedRtDataErrTable = _AcPMSS7MTP3MSUDiscardedRtDataErrTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 8)
)
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedRtDataErrTable.setStatus("current")
_AcPMSS7MTP3MSUDiscardedRtDataErrEntry_Object = MibTableRow
acPMSS7MTP3MSUDiscardedRtDataErrEntry = _AcPMSS7MTP3MSUDiscardedRtDataErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 8, 1)
)
acPMSS7MTP3MSUDiscardedRtDataErrEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP3MSUDiscardedRtDataErrSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP3MSUDiscardedRtDataErrInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedRtDataErrEntry.setStatus("current")


class _AcPMSS7MTP3MSUDiscardedRtDataErrSN_Type(Unsigned32):
    """Custom type acPMSS7MTP3MSUDiscardedRtDataErrSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP3MSUDiscardedRtDataErrSN_Type.__name__ = "Unsigned32"
_AcPMSS7MTP3MSUDiscardedRtDataErrSN_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedRtDataErrSN = _AcPMSS7MTP3MSUDiscardedRtDataErrSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 8, 1, 1),
    _AcPMSS7MTP3MSUDiscardedRtDataErrSN_Type()
)
acPMSS7MTP3MSUDiscardedRtDataErrSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedRtDataErrSN.setStatus("current")


class _AcPMSS7MTP3MSUDiscardedRtDataErrInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP3MSUDiscardedRtDataErrInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP3MSUDiscardedRtDataErrInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP3MSUDiscardedRtDataErrInterval_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedRtDataErrInterval = _AcPMSS7MTP3MSUDiscardedRtDataErrInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 8, 1, 2),
    _AcPMSS7MTP3MSUDiscardedRtDataErrInterval_Type()
)
acPMSS7MTP3MSUDiscardedRtDataErrInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedRtDataErrInterval.setStatus("current")
_AcPMSS7MTP3MSUDiscardedRtDataErrVal_Type = Counter32
_AcPMSS7MTP3MSUDiscardedRtDataErrVal_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedRtDataErrVal = _AcPMSS7MTP3MSUDiscardedRtDataErrVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 8, 1, 3),
    _AcPMSS7MTP3MSUDiscardedRtDataErrVal_Type()
)
acPMSS7MTP3MSUDiscardedRtDataErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedRtDataErrVal.setStatus("current")


class _AcPMSS7MTP3MSUDiscardedRtDataErrTotal_Type(Integer32):
    """Custom type acPMSS7MTP3MSUDiscardedRtDataErrTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP3MSUDiscardedRtDataErrTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP3MSUDiscardedRtDataErrTotal_Object = MibTableColumn
acPMSS7MTP3MSUDiscardedRtDataErrTotal = _AcPMSS7MTP3MSUDiscardedRtDataErrTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 8, 1, 4),
    _AcPMSS7MTP3MSUDiscardedRtDataErrTotal_Type()
)
acPMSS7MTP3MSUDiscardedRtDataErrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP3MSUDiscardedRtDataErrTotal.setStatus("current")
_AcPMSS7RxMTP3TFCMsgTable_Object = MibTable
acPMSS7RxMTP3TFCMsgTable = _AcPMSS7RxMTP3TFCMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 9)
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3TFCMsgTable.setStatus("current")
_AcPMSS7RxMTP3TFCMsgEntry_Object = MibTableRow
acPMSS7RxMTP3TFCMsgEntry = _AcPMSS7RxMTP3TFCMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 9, 1)
)
acPMSS7RxMTP3TFCMsgEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3TFCMsgSN"),
    (0, "AC-PM-SS7-MIB", "acPMSS7RxMTP3TFCMsgInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7RxMTP3TFCMsgEntry.setStatus("current")


class _AcPMSS7RxMTP3TFCMsgSN_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3TFCMsgSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3TFCMsgSN_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3TFCMsgSN_Object = MibTableColumn
acPMSS7RxMTP3TFCMsgSN = _AcPMSS7RxMTP3TFCMsgSN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 9, 1, 1),
    _AcPMSS7RxMTP3TFCMsgSN_Type()
)
acPMSS7RxMTP3TFCMsgSN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3TFCMsgSN.setStatus("current")


class _AcPMSS7RxMTP3TFCMsgInterval_Type(Unsigned32):
    """Custom type acPMSS7RxMTP3TFCMsgInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7RxMTP3TFCMsgInterval_Type.__name__ = "Unsigned32"
_AcPMSS7RxMTP3TFCMsgInterval_Object = MibTableColumn
acPMSS7RxMTP3TFCMsgInterval = _AcPMSS7RxMTP3TFCMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 9, 1, 2),
    _AcPMSS7RxMTP3TFCMsgInterval_Type()
)
acPMSS7RxMTP3TFCMsgInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3TFCMsgInterval.setStatus("current")
_AcPMSS7RxMTP3TFCMsgVal_Type = Counter32
_AcPMSS7RxMTP3TFCMsgVal_Object = MibTableColumn
acPMSS7RxMTP3TFCMsgVal = _AcPMSS7RxMTP3TFCMsgVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 9, 1, 3),
    _AcPMSS7RxMTP3TFCMsgVal_Type()
)
acPMSS7RxMTP3TFCMsgVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3TFCMsgVal.setStatus("current")


class _AcPMSS7RxMTP3TFCMsgTotal_Type(Integer32):
    """Custom type acPMSS7RxMTP3TFCMsgTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7RxMTP3TFCMsgTotal_Type.__name__ = "Integer32"
_AcPMSS7RxMTP3TFCMsgTotal_Object = MibTableColumn
acPMSS7RxMTP3TFCMsgTotal = _AcPMSS7RxMTP3TFCMsgTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 51, 9, 1, 4),
    _AcPMSS7RxMTP3TFCMsgTotal_Type()
)
acPMSS7RxMTP3TFCMsgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7RxMTP3TFCMsgTotal.setStatus("current")
_AcPMSS7MPT2Timers_ObjectIdentity = ObjectIdentity
acPMSS7MPT2Timers = _AcPMSS7MPT2Timers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61)
)
_AcPMSS7MTP2T1ExpiryTable_Object = MibTable
acPMSS7MTP2T1ExpiryTable = _AcPMSS7MTP2T1ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 1)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T1ExpiryTable.setStatus("current")
_AcPMSS7MTP2T1ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T1ExpiryEntry = _AcPMSS7MTP2T1ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 1, 1)
)
acPMSS7MTP2T1ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T1ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T1ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T1ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T1ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T1ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T1ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T1ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T1ExpiryLink = _AcPMSS7MTP2T1ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 1, 1, 1),
    _AcPMSS7MTP2T1ExpiryLink_Type()
)
acPMSS7MTP2T1ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T1ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T1ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T1ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T1ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T1ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T1ExpiryInterval = _AcPMSS7MTP2T1ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 1, 1, 2),
    _AcPMSS7MTP2T1ExpiryInterval_Type()
)
acPMSS7MTP2T1ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T1ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T1ExpiryVal_Type = Counter32
_AcPMSS7MTP2T1ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T1ExpiryVal = _AcPMSS7MTP2T1ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 1, 1, 3),
    _AcPMSS7MTP2T1ExpiryVal_Type()
)
acPMSS7MTP2T1ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T1ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T1ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T1ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T1ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T1ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T1ExpiryTotal = _AcPMSS7MTP2T1ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 1, 1, 4),
    _AcPMSS7MTP2T1ExpiryTotal_Type()
)
acPMSS7MTP2T1ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T1ExpiryTotal.setStatus("current")
_AcPMSS7MTP2T2ExpiryTable_Object = MibTable
acPMSS7MTP2T2ExpiryTable = _AcPMSS7MTP2T2ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 2)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T2ExpiryTable.setStatus("current")
_AcPMSS7MTP2T2ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T2ExpiryEntry = _AcPMSS7MTP2T2ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 2, 1)
)
acPMSS7MTP2T2ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T2ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T2ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T2ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T2ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T2ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2T2ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T2ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T2ExpiryLink = _AcPMSS7MTP2T2ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 2, 1, 1),
    _AcPMSS7MTP2T2ExpiryLink_Type()
)
acPMSS7MTP2T2ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T2ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T2ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T2ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T2ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T2ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T2ExpiryInterval = _AcPMSS7MTP2T2ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 2, 1, 2),
    _AcPMSS7MTP2T2ExpiryInterval_Type()
)
acPMSS7MTP2T2ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T2ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T2ExpiryVal_Type = Counter32
_AcPMSS7MTP2T2ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T2ExpiryVal = _AcPMSS7MTP2T2ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 2, 1, 3),
    _AcPMSS7MTP2T2ExpiryVal_Type()
)
acPMSS7MTP2T2ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T2ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T2ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T2ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T2ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T2ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T2ExpiryTotal = _AcPMSS7MTP2T2ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 2, 1, 4),
    _AcPMSS7MTP2T2ExpiryTotal_Type()
)
acPMSS7MTP2T2ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T2ExpiryTotal.setStatus("current")
_AcPMSS7MTP2T3ExpiryTable_Object = MibTable
acPMSS7MTP2T3ExpiryTable = _AcPMSS7MTP2T3ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 3)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T3ExpiryTable.setStatus("current")
_AcPMSS7MTP2T3ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T3ExpiryEntry = _AcPMSS7MTP2T3ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 3, 1)
)
acPMSS7MTP2T3ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T3ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T3ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T3ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T3ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T3ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2T3ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T3ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T3ExpiryLink = _AcPMSS7MTP2T3ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 3, 1, 1),
    _AcPMSS7MTP2T3ExpiryLink_Type()
)
acPMSS7MTP2T3ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T3ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T3ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T3ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T3ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T3ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T3ExpiryInterval = _AcPMSS7MTP2T3ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 3, 1, 2),
    _AcPMSS7MTP2T3ExpiryInterval_Type()
)
acPMSS7MTP2T3ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T3ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T3ExpiryVal_Type = Counter32
_AcPMSS7MTP2T3ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T3ExpiryVal = _AcPMSS7MTP2T3ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 3, 1, 3),
    _AcPMSS7MTP2T3ExpiryVal_Type()
)
acPMSS7MTP2T3ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T3ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T3ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T3ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T3ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T3ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T3ExpiryTotal = _AcPMSS7MTP2T3ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 3, 1, 4),
    _AcPMSS7MTP2T3ExpiryTotal_Type()
)
acPMSS7MTP2T3ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T3ExpiryTotal.setStatus("current")
_AcPMSS7MTP2T4ExpiryTable_Object = MibTable
acPMSS7MTP2T4ExpiryTable = _AcPMSS7MTP2T4ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 4)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T4ExpiryTable.setStatus("current")
_AcPMSS7MTP2T4ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T4ExpiryEntry = _AcPMSS7MTP2T4ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 4, 1)
)
acPMSS7MTP2T4ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T4ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T4ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T4ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T4ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T4ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2T4ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T4ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T4ExpiryLink = _AcPMSS7MTP2T4ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 4, 1, 1),
    _AcPMSS7MTP2T4ExpiryLink_Type()
)
acPMSS7MTP2T4ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T4ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T4ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T4ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T4ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T4ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T4ExpiryInterval = _AcPMSS7MTP2T4ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 4, 1, 2),
    _AcPMSS7MTP2T4ExpiryInterval_Type()
)
acPMSS7MTP2T4ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T4ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T4ExpiryVal_Type = Counter32
_AcPMSS7MTP2T4ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T4ExpiryVal = _AcPMSS7MTP2T4ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 4, 1, 3),
    _AcPMSS7MTP2T4ExpiryVal_Type()
)
acPMSS7MTP2T4ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T4ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T4ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T4ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T4ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T4ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T4ExpiryTotal = _AcPMSS7MTP2T4ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 4, 1, 4),
    _AcPMSS7MTP2T4ExpiryTotal_Type()
)
acPMSS7MTP2T4ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T4ExpiryTotal.setStatus("current")
_AcPMSS7MTP2T5ExpiryTable_Object = MibTable
acPMSS7MTP2T5ExpiryTable = _AcPMSS7MTP2T5ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 5)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T5ExpiryTable.setStatus("current")
_AcPMSS7MTP2T5ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T5ExpiryEntry = _AcPMSS7MTP2T5ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 5, 1)
)
acPMSS7MTP2T5ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T5ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T5ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T5ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T5ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T5ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2T5ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T5ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T5ExpiryLink = _AcPMSS7MTP2T5ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 5, 1, 1),
    _AcPMSS7MTP2T5ExpiryLink_Type()
)
acPMSS7MTP2T5ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T5ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T5ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T5ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T5ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T5ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T5ExpiryInterval = _AcPMSS7MTP2T5ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 5, 1, 2),
    _AcPMSS7MTP2T5ExpiryInterval_Type()
)
acPMSS7MTP2T5ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T5ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T5ExpiryVal_Type = Counter32
_AcPMSS7MTP2T5ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T5ExpiryVal = _AcPMSS7MTP2T5ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 5, 1, 3),
    _AcPMSS7MTP2T5ExpiryVal_Type()
)
acPMSS7MTP2T5ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T5ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T5ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T5ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T5ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T5ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T5ExpiryTotal = _AcPMSS7MTP2T5ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 5, 1, 4),
    _AcPMSS7MTP2T5ExpiryTotal_Type()
)
acPMSS7MTP2T5ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T5ExpiryTotal.setStatus("current")
_AcPMSS7MTP2T6ExpiryTable_Object = MibTable
acPMSS7MTP2T6ExpiryTable = _AcPMSS7MTP2T6ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 6)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T6ExpiryTable.setStatus("current")
_AcPMSS7MTP2T6ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T6ExpiryEntry = _AcPMSS7MTP2T6ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 6, 1)
)
acPMSS7MTP2T6ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T6ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T6ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T6ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T6ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T6ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2T6ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T6ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T6ExpiryLink = _AcPMSS7MTP2T6ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 6, 1, 1),
    _AcPMSS7MTP2T6ExpiryLink_Type()
)
acPMSS7MTP2T6ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T6ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T6ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T6ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T6ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T6ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T6ExpiryInterval = _AcPMSS7MTP2T6ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 6, 1, 2),
    _AcPMSS7MTP2T6ExpiryInterval_Type()
)
acPMSS7MTP2T6ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T6ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T6ExpiryVal_Type = Counter32
_AcPMSS7MTP2T6ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T6ExpiryVal = _AcPMSS7MTP2T6ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 6, 1, 3),
    _AcPMSS7MTP2T6ExpiryVal_Type()
)
acPMSS7MTP2T6ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T6ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T6ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T6ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T6ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T6ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T6ExpiryTotal = _AcPMSS7MTP2T6ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 6, 1, 4),
    _AcPMSS7MTP2T6ExpiryTotal_Type()
)
acPMSS7MTP2T6ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T6ExpiryTotal.setStatus("current")
_AcPMSS7MTP2T7ExpiryTable_Object = MibTable
acPMSS7MTP2T7ExpiryTable = _AcPMSS7MTP2T7ExpiryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 7)
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T7ExpiryTable.setStatus("current")
_AcPMSS7MTP2T7ExpiryEntry_Object = MibTableRow
acPMSS7MTP2T7ExpiryEntry = _AcPMSS7MTP2T7ExpiryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 7, 1)
)
acPMSS7MTP2T7ExpiryEntry.setIndexNames(
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T7ExpiryLink"),
    (0, "AC-PM-SS7-MIB", "acPMSS7MTP2T7ExpiryInterval"),
)
if mibBuilder.loadTexts:
    acPMSS7MTP2T7ExpiryEntry.setStatus("current")


class _AcPMSS7MTP2T7ExpiryLink_Type(Unsigned32):
    """Custom type acPMSS7MTP2T7ExpiryLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMSS7MTP2T7ExpiryLink_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T7ExpiryLink_Object = MibTableColumn
acPMSS7MTP2T7ExpiryLink = _AcPMSS7MTP2T7ExpiryLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 7, 1, 1),
    _AcPMSS7MTP2T7ExpiryLink_Type()
)
acPMSS7MTP2T7ExpiryLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T7ExpiryLink.setStatus("current")


class _AcPMSS7MTP2T7ExpiryInterval_Type(Unsigned32):
    """Custom type acPMSS7MTP2T7ExpiryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSS7MTP2T7ExpiryInterval_Type.__name__ = "Unsigned32"
_AcPMSS7MTP2T7ExpiryInterval_Object = MibTableColumn
acPMSS7MTP2T7ExpiryInterval = _AcPMSS7MTP2T7ExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 7, 1, 2),
    _AcPMSS7MTP2T7ExpiryInterval_Type()
)
acPMSS7MTP2T7ExpiryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSS7MTP2T7ExpiryInterval.setStatus("current")
_AcPMSS7MTP2T7ExpiryVal_Type = Counter32
_AcPMSS7MTP2T7ExpiryVal_Object = MibTableColumn
acPMSS7MTP2T7ExpiryVal = _AcPMSS7MTP2T7ExpiryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 7, 1, 3),
    _AcPMSS7MTP2T7ExpiryVal_Type()
)
acPMSS7MTP2T7ExpiryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T7ExpiryVal.setStatus("current")


class _AcPMSS7MTP2T7ExpiryTotal_Type(Integer32):
    """Custom type acPMSS7MTP2T7ExpiryTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSS7MTP2T7ExpiryTotal_Type.__name__ = "Integer32"
_AcPMSS7MTP2T7ExpiryTotal_Object = MibTableColumn
acPMSS7MTP2T7ExpiryTotal = _AcPMSS7MTP2T7ExpiryTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 13, 2, 61, 7, 1, 4),
    _AcPMSS7MTP2T7ExpiryTotal_Type()
)
acPMSS7MTP2T7ExpiryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSS7MTP2T7ExpiryTotal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-SS7-MIB",
    **{"acPMSS7": acPMSS7,
       "acPMSS7Configuration": acPMSS7Configuration,
       "acPMSS7ConfigurationPeriodLength": acPMSS7ConfigurationPeriodLength,
       "acPMSS7ConfigurationResetTotalCounters": acPMSS7ConfigurationResetTotalCounters,
       "acPMSS7Data": acPMSS7Data,
       "acPMSS7DataTimeFromStartOfInterval": acPMSS7DataTimeFromStartOfInterval,
       "acPMSS7Links": acPMSS7Links,
       "acPMSS7TxMSUTable": acPMSS7TxMSUTable,
       "acPMSS7TxMSUEntry": acPMSS7TxMSUEntry,
       "acPMSS7TxMSULink": acPMSS7TxMSULink,
       "acPMSS7TxMSUInterval": acPMSS7TxMSUInterval,
       "acPMSS7TxMSUVal": acPMSS7TxMSUVal,
       "acPMSS7TxMSUTotal": acPMSS7TxMSUTotal,
       "acPMSS7RxMSUTable": acPMSS7RxMSUTable,
       "acPMSS7RxMSUEntry": acPMSS7RxMSUEntry,
       "acPMSS7RxMSULink": acPMSS7RxMSULink,
       "acPMSS7RxMSUInterval": acPMSS7RxMSUInterval,
       "acPMSS7RxMSUVal": acPMSS7RxMSUVal,
       "acPMSS7RxMSUTotal": acPMSS7RxMSUTotal,
       "acPMSS7TxLSSUTable": acPMSS7TxLSSUTable,
       "acPMSS7TxLSSUEntry": acPMSS7TxLSSUEntry,
       "acPMSS7TxLSSULink": acPMSS7TxLSSULink,
       "acPMSS7TxLSSUInterval": acPMSS7TxLSSUInterval,
       "acPMSS7TxLSSUVal": acPMSS7TxLSSUVal,
       "acPMSS7TxLSSUTotal": acPMSS7TxLSSUTotal,
       "acPMSS7RxLSSUTable": acPMSS7RxLSSUTable,
       "acPMSS7RxLSSUEntry": acPMSS7RxLSSUEntry,
       "acPMSS7RxLSSULink": acPMSS7RxLSSULink,
       "acPMSS7RxLSSUInterval": acPMSS7RxLSSUInterval,
       "acPMSS7RxLSSUVal": acPMSS7RxLSSUVal,
       "acPMSS7RxLSSUTotal": acPMSS7RxLSSUTotal,
       "acPMSS7TxFISUTable": acPMSS7TxFISUTable,
       "acPMSS7TxFISUEntry": acPMSS7TxFISUEntry,
       "acPMSS7TxFISULink": acPMSS7TxFISULink,
       "acPMSS7TxFISUInterval": acPMSS7TxFISUInterval,
       "acPMSS7TxFISUVal": acPMSS7TxFISUVal,
       "acPMSS7TxFISUTotal": acPMSS7TxFISUTotal,
       "acPMSS7RxFISUTable": acPMSS7RxFISUTable,
       "acPMSS7RxFISUEntry": acPMSS7RxFISUEntry,
       "acPMSS7RxFISULink": acPMSS7RxFISULink,
       "acPMSS7RxFISUInterval": acPMSS7RxFISUInterval,
       "acPMSS7RxFISUVal": acPMSS7RxFISUVal,
       "acPMSS7RxFISUTotal": acPMSS7RxFISUTotal,
       "acPMSS7TxSignalUnitsTable": acPMSS7TxSignalUnitsTable,
       "acPMSS7TxSignalUnitsEntry": acPMSS7TxSignalUnitsEntry,
       "acPMSS7TxSignalUnitsLink": acPMSS7TxSignalUnitsLink,
       "acPMSS7TxSignalUnitsInterval": acPMSS7TxSignalUnitsInterval,
       "acPMSS7TxSignalUnitsVal": acPMSS7TxSignalUnitsVal,
       "acPMSS7TxSignalUnitsTotal": acPMSS7TxSignalUnitsTotal,
       "acPMSS7RxSignalUnitsTable": acPMSS7RxSignalUnitsTable,
       "acPMSS7RxSignalUnitsEntry": acPMSS7RxSignalUnitsEntry,
       "acPMSS7RxSignalUnitsLink": acPMSS7RxSignalUnitsLink,
       "acPMSS7RxSignalUnitsInterval": acPMSS7RxSignalUnitsInterval,
       "acPMSS7RxSignalUnitsVal": acPMSS7RxSignalUnitsVal,
       "acPMSS7RxSignalUnitsTotal": acPMSS7RxSignalUnitsTotal,
       "acPMSS7TxOctetsTable": acPMSS7TxOctetsTable,
       "acPMSS7TxOctetsEntry": acPMSS7TxOctetsEntry,
       "acPMSS7TxOctetsLink": acPMSS7TxOctetsLink,
       "acPMSS7TxOctetsInterval": acPMSS7TxOctetsInterval,
       "acPMSS7TxOctetsVal": acPMSS7TxOctetsVal,
       "acPMSS7TxOctetsTotal": acPMSS7TxOctetsTotal,
       "acPMSS7RxOctetsTable": acPMSS7RxOctetsTable,
       "acPMSS7RxOctetsEntry": acPMSS7RxOctetsEntry,
       "acPMSS7RxOctetsLink": acPMSS7RxOctetsLink,
       "acPMSS7RxOctetsInterval": acPMSS7RxOctetsInterval,
       "acPMSS7RxOctetsVal": acPMSS7RxOctetsVal,
       "acPMSS7RxOctetsTotal": acPMSS7RxOctetsTotal,
       "acPMSS7MTP2NoAckRxTable": acPMSS7MTP2NoAckRxTable,
       "acPMSS7MTP2NoAckRxEntry": acPMSS7MTP2NoAckRxEntry,
       "acPMSS7MTP2NoAckRxLink": acPMSS7MTP2NoAckRxLink,
       "acPMSS7MTP2NoAckRxInterval": acPMSS7MTP2NoAckRxInterval,
       "acPMSS7MTP2NoAckRxVal": acPMSS7MTP2NoAckRxVal,
       "acPMSS7MTP2NoAckRxTotal": acPMSS7MTP2NoAckRxTotal,
       "acPMSS7DiscMSUTable": acPMSS7DiscMSUTable,
       "acPMSS7DiscMSUEntry": acPMSS7DiscMSUEntry,
       "acPMSS7DiscMSULink": acPMSS7DiscMSULink,
       "acPMSS7DiscMSUInterval": acPMSS7DiscMSUInterval,
       "acPMSS7DiscMSUVal": acPMSS7DiscMSUVal,
       "acPMSS7DiscMSUTotal": acPMSS7DiscMSUTotal,
       "acPMSS7InServiceTable": acPMSS7InServiceTable,
       "acPMSS7InServiceEntry": acPMSS7InServiceEntry,
       "acPMSS7InServiceLink": acPMSS7InServiceLink,
       "acPMSS7InServiceInterval": acPMSS7InServiceInterval,
       "acPMSS7InServiceVal": acPMSS7InServiceVal,
       "acPMSS7InServiceTimeAboveHighThreshold": acPMSS7InServiceTimeAboveHighThreshold,
       "acPMSS7InServiceTimeBetweenThresholds": acPMSS7InServiceTimeBetweenThresholds,
       "acPMSS7OutOfServiceTable": acPMSS7OutOfServiceTable,
       "acPMSS7OutOfServiceEntry": acPMSS7OutOfServiceEntry,
       "acPMSS7OutOfServiceLink": acPMSS7OutOfServiceLink,
       "acPMSS7OutOfServiceInterval": acPMSS7OutOfServiceInterval,
       "acPMSS7OutOfServiceVal": acPMSS7OutOfServiceVal,
       "acPMSS7OutOfServiceTimeAboveHighThreshold": acPMSS7OutOfServiceTimeAboveHighThreshold,
       "acPMSS7OutOfServiceTimeBetweenThresholds": acPMSS7OutOfServiceTimeBetweenThresholds,
       "acPMSS7LinkSets": acPMSS7LinkSets,
       "acPMSS7SN0LSOutOfServiceTable": acPMSS7SN0LSOutOfServiceTable,
       "acPMSS7SN0LSOutOfServiceEntry": acPMSS7SN0LSOutOfServiceEntry,
       "acPMSS7SN0LSOutOfServiceLinkSet": acPMSS7SN0LSOutOfServiceLinkSet,
       "acPMSS7SN0LSOutOfServiceInterval": acPMSS7SN0LSOutOfServiceInterval,
       "acPMSS7SN0LSOutOfServiceVal": acPMSS7SN0LSOutOfServiceVal,
       "acPMSS7SN0LSOutOfServiceTimeAboveHighThreshold": acPMSS7SN0LSOutOfServiceTimeAboveHighThreshold,
       "acPMSS7SN0LSOutOfServiceTimeBetweenThresholds": acPMSS7SN0LSOutOfServiceTimeBetweenThresholds,
       "acPMSS7SN1LSOutOfServiceTable": acPMSS7SN1LSOutOfServiceTable,
       "acPMSS7SN1LSOutOfServiceEntry": acPMSS7SN1LSOutOfServiceEntry,
       "acPMSS7SN1LSOutOfServiceLinkSet": acPMSS7SN1LSOutOfServiceLinkSet,
       "acPMSS7SN1LSOutOfServiceInterval": acPMSS7SN1LSOutOfServiceInterval,
       "acPMSS7SN1LSOutOfServiceVal": acPMSS7SN1LSOutOfServiceVal,
       "acPMSS7SN1LSOutOfServiceTimeAboveHighThreshold": acPMSS7SN1LSOutOfServiceTimeAboveHighThreshold,
       "acPMSS7SN1LSOutOfServiceTimeBetweenThresholds": acPMSS7SN1LSOutOfServiceTimeBetweenThresholds,
       "acPMSS7SignalingNodes": acPMSS7SignalingNodes,
       "acPMSS7TxMTP3OctetsTable": acPMSS7TxMTP3OctetsTable,
       "acPMSS7TxMTP3OctetsEntry": acPMSS7TxMTP3OctetsEntry,
       "acPMSS7TxMTP3OctetsSN": acPMSS7TxMTP3OctetsSN,
       "acPMSS7TxMTP3OctetsInterval": acPMSS7TxMTP3OctetsInterval,
       "acPMSS7TxMTP3OctetsVal": acPMSS7TxMTP3OctetsVal,
       "acPMSS7TxMTP3OctetsTotal": acPMSS7TxMTP3OctetsTotal,
       "acPMSS7RxMTP3OctetsTable": acPMSS7RxMTP3OctetsTable,
       "acPMSS7RxMTP3OctetsEntry": acPMSS7RxMTP3OctetsEntry,
       "acPMSS7RxMTP3OctetsSN": acPMSS7RxMTP3OctetsSN,
       "acPMSS7RxMTP3OctetsInterval": acPMSS7RxMTP3OctetsInterval,
       "acPMSS7RxMTP3OctetsVal": acPMSS7RxMTP3OctetsVal,
       "acPMSS7RxMTP3OctetsTotal": acPMSS7RxMTP3OctetsTotal,
       "acPMSS7TxMTP3MSUTable": acPMSS7TxMTP3MSUTable,
       "acPMSS7TxMTP3MSUEntry": acPMSS7TxMTP3MSUEntry,
       "acPMSS7TxMTP3MSUSN": acPMSS7TxMTP3MSUSN,
       "acPMSS7TxMTP3MSUInterval": acPMSS7TxMTP3MSUInterval,
       "acPMSS7TxMTP3MSUVal": acPMSS7TxMTP3MSUVal,
       "acPMSS7TxMTP3MSUTotal": acPMSS7TxMTP3MSUTotal,
       "acPMSS7RxMTP3MSUTable": acPMSS7RxMTP3MSUTable,
       "acPMSS7RxMTP3MSUEntry": acPMSS7RxMTP3MSUEntry,
       "acPMSS7RxMTP3MSUSN": acPMSS7RxMTP3MSUSN,
       "acPMSS7RxMTP3MSUInterval": acPMSS7RxMTP3MSUInterval,
       "acPMSS7RxMTP3MSUVal": acPMSS7RxMTP3MSUVal,
       "acPMSS7RxMTP3MSUTotal": acPMSS7RxMTP3MSUTotal,
       "acPMSS7TxMTP3UPUTable": acPMSS7TxMTP3UPUTable,
       "acPMSS7TxMTP3UPUEntry": acPMSS7TxMTP3UPUEntry,
       "acPMSS7TxMTP3UPUSN": acPMSS7TxMTP3UPUSN,
       "acPMSS7TxMTP3UPUInterval": acPMSS7TxMTP3UPUInterval,
       "acPMSS7TxMTP3UPUVal": acPMSS7TxMTP3UPUVal,
       "acPMSS7TxMTP3UPUTotal": acPMSS7TxMTP3UPUTotal,
       "acPMSS7RxMTP3UPUTable": acPMSS7RxMTP3UPUTable,
       "acPMSS7RxMTP3UPUEntry": acPMSS7RxMTP3UPUEntry,
       "acPMSS7RxMTP3UPUSN": acPMSS7RxMTP3UPUSN,
       "acPMSS7RxMTP3UPUInterval": acPMSS7RxMTP3UPUInterval,
       "acPMSS7RxMTP3UPUVal": acPMSS7RxMTP3UPUVal,
       "acPMSS7RxMTP3UPUTotal": acPMSS7RxMTP3UPUTotal,
       "acPMSS7MTP3MSUDiscardedTable": acPMSS7MTP3MSUDiscardedTable,
       "acPMSS7MTP3MSUDiscardedEntry": acPMSS7MTP3MSUDiscardedEntry,
       "acPMSS7MTP3MSUDiscardedSN": acPMSS7MTP3MSUDiscardedSN,
       "acPMSS7MTP3MSUDiscardedInterval": acPMSS7MTP3MSUDiscardedInterval,
       "acPMSS7MTP3MSUDiscardedVal": acPMSS7MTP3MSUDiscardedVal,
       "acPMSS7MTP3MSUDiscardedTotal": acPMSS7MTP3MSUDiscardedTotal,
       "acPMSS7MTP3MSUDiscardedRtDataErrTable": acPMSS7MTP3MSUDiscardedRtDataErrTable,
       "acPMSS7MTP3MSUDiscardedRtDataErrEntry": acPMSS7MTP3MSUDiscardedRtDataErrEntry,
       "acPMSS7MTP3MSUDiscardedRtDataErrSN": acPMSS7MTP3MSUDiscardedRtDataErrSN,
       "acPMSS7MTP3MSUDiscardedRtDataErrInterval": acPMSS7MTP3MSUDiscardedRtDataErrInterval,
       "acPMSS7MTP3MSUDiscardedRtDataErrVal": acPMSS7MTP3MSUDiscardedRtDataErrVal,
       "acPMSS7MTP3MSUDiscardedRtDataErrTotal": acPMSS7MTP3MSUDiscardedRtDataErrTotal,
       "acPMSS7RxMTP3TFCMsgTable": acPMSS7RxMTP3TFCMsgTable,
       "acPMSS7RxMTP3TFCMsgEntry": acPMSS7RxMTP3TFCMsgEntry,
       "acPMSS7RxMTP3TFCMsgSN": acPMSS7RxMTP3TFCMsgSN,
       "acPMSS7RxMTP3TFCMsgInterval": acPMSS7RxMTP3TFCMsgInterval,
       "acPMSS7RxMTP3TFCMsgVal": acPMSS7RxMTP3TFCMsgVal,
       "acPMSS7RxMTP3TFCMsgTotal": acPMSS7RxMTP3TFCMsgTotal,
       "acPMSS7MPT2Timers": acPMSS7MPT2Timers,
       "acPMSS7MTP2T1ExpiryTable": acPMSS7MTP2T1ExpiryTable,
       "acPMSS7MTP2T1ExpiryEntry": acPMSS7MTP2T1ExpiryEntry,
       "acPMSS7MTP2T1ExpiryLink": acPMSS7MTP2T1ExpiryLink,
       "acPMSS7MTP2T1ExpiryInterval": acPMSS7MTP2T1ExpiryInterval,
       "acPMSS7MTP2T1ExpiryVal": acPMSS7MTP2T1ExpiryVal,
       "acPMSS7MTP2T1ExpiryTotal": acPMSS7MTP2T1ExpiryTotal,
       "acPMSS7MTP2T2ExpiryTable": acPMSS7MTP2T2ExpiryTable,
       "acPMSS7MTP2T2ExpiryEntry": acPMSS7MTP2T2ExpiryEntry,
       "acPMSS7MTP2T2ExpiryLink": acPMSS7MTP2T2ExpiryLink,
       "acPMSS7MTP2T2ExpiryInterval": acPMSS7MTP2T2ExpiryInterval,
       "acPMSS7MTP2T2ExpiryVal": acPMSS7MTP2T2ExpiryVal,
       "acPMSS7MTP2T2ExpiryTotal": acPMSS7MTP2T2ExpiryTotal,
       "acPMSS7MTP2T3ExpiryTable": acPMSS7MTP2T3ExpiryTable,
       "acPMSS7MTP2T3ExpiryEntry": acPMSS7MTP2T3ExpiryEntry,
       "acPMSS7MTP2T3ExpiryLink": acPMSS7MTP2T3ExpiryLink,
       "acPMSS7MTP2T3ExpiryInterval": acPMSS7MTP2T3ExpiryInterval,
       "acPMSS7MTP2T3ExpiryVal": acPMSS7MTP2T3ExpiryVal,
       "acPMSS7MTP2T3ExpiryTotal": acPMSS7MTP2T3ExpiryTotal,
       "acPMSS7MTP2T4ExpiryTable": acPMSS7MTP2T4ExpiryTable,
       "acPMSS7MTP2T4ExpiryEntry": acPMSS7MTP2T4ExpiryEntry,
       "acPMSS7MTP2T4ExpiryLink": acPMSS7MTP2T4ExpiryLink,
       "acPMSS7MTP2T4ExpiryInterval": acPMSS7MTP2T4ExpiryInterval,
       "acPMSS7MTP2T4ExpiryVal": acPMSS7MTP2T4ExpiryVal,
       "acPMSS7MTP2T4ExpiryTotal": acPMSS7MTP2T4ExpiryTotal,
       "acPMSS7MTP2T5ExpiryTable": acPMSS7MTP2T5ExpiryTable,
       "acPMSS7MTP2T5ExpiryEntry": acPMSS7MTP2T5ExpiryEntry,
       "acPMSS7MTP2T5ExpiryLink": acPMSS7MTP2T5ExpiryLink,
       "acPMSS7MTP2T5ExpiryInterval": acPMSS7MTP2T5ExpiryInterval,
       "acPMSS7MTP2T5ExpiryVal": acPMSS7MTP2T5ExpiryVal,
       "acPMSS7MTP2T5ExpiryTotal": acPMSS7MTP2T5ExpiryTotal,
       "acPMSS7MTP2T6ExpiryTable": acPMSS7MTP2T6ExpiryTable,
       "acPMSS7MTP2T6ExpiryEntry": acPMSS7MTP2T6ExpiryEntry,
       "acPMSS7MTP2T6ExpiryLink": acPMSS7MTP2T6ExpiryLink,
       "acPMSS7MTP2T6ExpiryInterval": acPMSS7MTP2T6ExpiryInterval,
       "acPMSS7MTP2T6ExpiryVal": acPMSS7MTP2T6ExpiryVal,
       "acPMSS7MTP2T6ExpiryTotal": acPMSS7MTP2T6ExpiryTotal,
       "acPMSS7MTP2T7ExpiryTable": acPMSS7MTP2T7ExpiryTable,
       "acPMSS7MTP2T7ExpiryEntry": acPMSS7MTP2T7ExpiryEntry,
       "acPMSS7MTP2T7ExpiryLink": acPMSS7MTP2T7ExpiryLink,
       "acPMSS7MTP2T7ExpiryInterval": acPMSS7MTP2T7ExpiryInterval,
       "acPMSS7MTP2T7ExpiryVal": acPMSS7MTP2T7ExpiryVal,
       "acPMSS7MTP2T7ExpiryTotal": acPMSS7MTP2T7ExpiryTotal}
)
