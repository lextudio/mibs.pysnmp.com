# SNMP MIB module (PAIRGAIN-ETSI-HDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-ETSI-HDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:22 2024
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

(pgainHDSL,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainHDSL")

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



class Byte(Integer32):
    """Custom type Byte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Short(Integer32):
    """Custom type Short based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class PgTimeStamp(OctetString):
    """Custom type PgTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class PgAlarmSeverityMode(Integer32):
    """Custom type PgAlarmSeverityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("major", 3),
          ("minor", 2),
          ("notAvailable", 4))
    )





class PgAlarmSeverityProtectionSwitchMode(Integer32):
    """Custom type PgAlarmSeverityProtectionSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("major", 3),
          ("minor", 2),
          ("notAvailable", 5),
          ("protectionSwitchMajor", 4))
    )





class PgBERThreshold(Integer32):
    """Custom type PgBERThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HdslSpan15mPerformanceTable_Object = MibTable
hdslSpan15mPerformanceTable = _HdslSpan15mPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hdslSpan15mPerformanceTable.setStatus("mandatory")
_HdslSpan15mPerformanceEntry_Object = MibTableRow
hdslSpan15mPerformanceEntry = _HdslSpan15mPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1)
)
hdslSpan15mPerformanceEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpan15mSlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpan15mSpanId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpan15mHistoryId"),
)
if mibBuilder.loadTexts:
    hdslSpan15mPerformanceEntry.setStatus("mandatory")
_HdslSpan15mSlotId_Type = Integer32
_HdslSpan15mSlotId_Object = MibTableColumn
hdslSpan15mSlotId = _HdslSpan15mSlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 1),
    _HdslSpan15mSlotId_Type()
)
hdslSpan15mSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpan15mSlotId.setStatus("mandatory")
_HdslSpan15mSpanId_Type = Integer32
_HdslSpan15mSpanId_Object = MibTableColumn
hdslSpan15mSpanId = _HdslSpan15mSpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 2),
    _HdslSpan15mSpanId_Type()
)
hdslSpan15mSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpan15mSpanId.setStatus("mandatory")
_HdslSpan15mHistoryId_Type = Integer32
_HdslSpan15mHistoryId_Object = MibTableColumn
hdslSpan15mHistoryId = _HdslSpan15mHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 3),
    _HdslSpan15mHistoryId_Type()
)
hdslSpan15mHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpan15mHistoryId.setStatus("mandatory")
_Hdsl15mESLoopANet_Type = Short
_Hdsl15mESLoopANet_Object = MibTableColumn
hdsl15mESLoopANet = _Hdsl15mESLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 4),
    _Hdsl15mESLoopANet_Type()
)
hdsl15mESLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mESLoopANet.setStatus("mandatory")
_Hdsl15mESLoopBNet_Type = Short
_Hdsl15mESLoopBNet_Object = MibTableColumn
hdsl15mESLoopBNet = _Hdsl15mESLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 5),
    _Hdsl15mESLoopBNet_Type()
)
hdsl15mESLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mESLoopBNet.setStatus("mandatory")
_Hdsl15mUASLoopANet_Type = Short
_Hdsl15mUASLoopANet_Object = MibTableColumn
hdsl15mUASLoopANet = _Hdsl15mUASLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 6),
    _Hdsl15mUASLoopANet_Type()
)
hdsl15mUASLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mUASLoopANet.setStatus("mandatory")
_Hdsl15mUASLoopBNet_Type = Short
_Hdsl15mUASLoopBNet_Object = MibTableColumn
hdsl15mUASLoopBNet = _Hdsl15mUASLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 7),
    _Hdsl15mUASLoopBNet_Type()
)
hdsl15mUASLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mUASLoopBNet.setStatus("mandatory")
_Hdsl15mSESLoopANet_Type = Short
_Hdsl15mSESLoopANet_Object = MibTableColumn
hdsl15mSESLoopANet = _Hdsl15mSESLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 8),
    _Hdsl15mSESLoopANet_Type()
)
hdsl15mSESLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mSESLoopANet.setStatus("mandatory")
_Hdsl15mSESLoopBNet_Type = Short
_Hdsl15mSESLoopBNet_Object = MibTableColumn
hdsl15mSESLoopBNet = _Hdsl15mSESLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 9),
    _Hdsl15mSESLoopBNet_Type()
)
hdsl15mSESLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mSESLoopBNet.setStatus("mandatory")
_Hdsl15mESLoopACust_Type = Short
_Hdsl15mESLoopACust_Object = MibTableColumn
hdsl15mESLoopACust = _Hdsl15mESLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 10),
    _Hdsl15mESLoopACust_Type()
)
hdsl15mESLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mESLoopACust.setStatus("mandatory")
_Hdsl15mESLoopBCust_Type = Short
_Hdsl15mESLoopBCust_Object = MibTableColumn
hdsl15mESLoopBCust = _Hdsl15mESLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 11),
    _Hdsl15mESLoopBCust_Type()
)
hdsl15mESLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mESLoopBCust.setStatus("mandatory")
_Hdsl15mUASLoopACust_Type = Short
_Hdsl15mUASLoopACust_Object = MibTableColumn
hdsl15mUASLoopACust = _Hdsl15mUASLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 12),
    _Hdsl15mUASLoopACust_Type()
)
hdsl15mUASLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mUASLoopACust.setStatus("mandatory")
_Hdsl15mUASLoopBCust_Type = Short
_Hdsl15mUASLoopBCust_Object = MibTableColumn
hdsl15mUASLoopBCust = _Hdsl15mUASLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 13),
    _Hdsl15mUASLoopBCust_Type()
)
hdsl15mUASLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mUASLoopBCust.setStatus("mandatory")
_Hdsl15mSESLoopACust_Type = Short
_Hdsl15mSESLoopACust_Object = MibTableColumn
hdsl15mSESLoopACust = _Hdsl15mSESLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 14),
    _Hdsl15mSESLoopACust_Type()
)
hdsl15mSESLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mSESLoopACust.setStatus("mandatory")
_Hdsl15mSESLoopBCust_Type = Short
_Hdsl15mSESLoopBCust_Object = MibTableColumn
hdsl15mSESLoopBCust = _Hdsl15mSESLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 1, 1, 15),
    _Hdsl15mSESLoopBCust_Type()
)
hdsl15mSESLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl15mSESLoopBCust.setStatus("mandatory")
_HdslSpan24hPerformanceTable_Object = MibTable
hdslSpan24hPerformanceTable = _HdslSpan24hPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hdslSpan24hPerformanceTable.setStatus("mandatory")
_HdslSpan24hPerformanceEntry_Object = MibTableRow
hdslSpan24hPerformanceEntry = _HdslSpan24hPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1)
)
hdslSpan24hPerformanceEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpan24hSlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpan24hSpanId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpan24hHistoryId"),
)
if mibBuilder.loadTexts:
    hdslSpan24hPerformanceEntry.setStatus("mandatory")
_HdslSpan24hSlotId_Type = Integer32
_HdslSpan24hSlotId_Object = MibTableColumn
hdslSpan24hSlotId = _HdslSpan24hSlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 1),
    _HdslSpan24hSlotId_Type()
)
hdslSpan24hSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpan24hSlotId.setStatus("mandatory")
_HdslSpan24hSpanId_Type = Integer32
_HdslSpan24hSpanId_Object = MibTableColumn
hdslSpan24hSpanId = _HdslSpan24hSpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 2),
    _HdslSpan24hSpanId_Type()
)
hdslSpan24hSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpan24hSpanId.setStatus("mandatory")
_HdslSpan24hHistoryId_Type = Integer32
_HdslSpan24hHistoryId_Object = MibTableColumn
hdslSpan24hHistoryId = _HdslSpan24hHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 3),
    _HdslSpan24hHistoryId_Type()
)
hdslSpan24hHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpan24hHistoryId.setStatus("mandatory")
_Hdsl24hESLoopANet_Type = Integer32
_Hdsl24hESLoopANet_Object = MibTableColumn
hdsl24hESLoopANet = _Hdsl24hESLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 4),
    _Hdsl24hESLoopANet_Type()
)
hdsl24hESLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hESLoopANet.setStatus("mandatory")
_Hdsl24hESLoopBNet_Type = Integer32
_Hdsl24hESLoopBNet_Object = MibTableColumn
hdsl24hESLoopBNet = _Hdsl24hESLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 5),
    _Hdsl24hESLoopBNet_Type()
)
hdsl24hESLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hESLoopBNet.setStatus("mandatory")
_Hdsl24hUASLoopANet_Type = Integer32
_Hdsl24hUASLoopANet_Object = MibTableColumn
hdsl24hUASLoopANet = _Hdsl24hUASLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 6),
    _Hdsl24hUASLoopANet_Type()
)
hdsl24hUASLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hUASLoopANet.setStatus("mandatory")
_Hdsl24hUASLoopBNet_Type = Integer32
_Hdsl24hUASLoopBNet_Object = MibTableColumn
hdsl24hUASLoopBNet = _Hdsl24hUASLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 7),
    _Hdsl24hUASLoopBNet_Type()
)
hdsl24hUASLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hUASLoopBNet.setStatus("mandatory")
_Hdsl24hSESLoopANet_Type = Integer32
_Hdsl24hSESLoopANet_Object = MibTableColumn
hdsl24hSESLoopANet = _Hdsl24hSESLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 8),
    _Hdsl24hSESLoopANet_Type()
)
hdsl24hSESLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hSESLoopANet.setStatus("mandatory")
_Hdsl24hSESLoopBNet_Type = Integer32
_Hdsl24hSESLoopBNet_Object = MibTableColumn
hdsl24hSESLoopBNet = _Hdsl24hSESLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 9),
    _Hdsl24hSESLoopBNet_Type()
)
hdsl24hSESLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hSESLoopBNet.setStatus("mandatory")
_Hdsl24hESLoopACust_Type = Integer32
_Hdsl24hESLoopACust_Object = MibTableColumn
hdsl24hESLoopACust = _Hdsl24hESLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 10),
    _Hdsl24hESLoopACust_Type()
)
hdsl24hESLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hESLoopACust.setStatus("mandatory")
_Hdsl24hESLoopBCust_Type = Integer32
_Hdsl24hESLoopBCust_Object = MibTableColumn
hdsl24hESLoopBCust = _Hdsl24hESLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 11),
    _Hdsl24hESLoopBCust_Type()
)
hdsl24hESLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hESLoopBCust.setStatus("mandatory")
_Hdsl24hUASLoopACust_Type = Integer32
_Hdsl24hUASLoopACust_Object = MibTableColumn
hdsl24hUASLoopACust = _Hdsl24hUASLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 12),
    _Hdsl24hUASLoopACust_Type()
)
hdsl24hUASLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hUASLoopACust.setStatus("mandatory")
_Hdsl24hUASLoopBCust_Type = Integer32
_Hdsl24hUASLoopBCust_Object = MibTableColumn
hdsl24hUASLoopBCust = _Hdsl24hUASLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 13),
    _Hdsl24hUASLoopBCust_Type()
)
hdsl24hUASLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hUASLoopBCust.setStatus("mandatory")
_Hdsl24hSESLoopACust_Type = Integer32
_Hdsl24hSESLoopACust_Object = MibTableColumn
hdsl24hSESLoopACust = _Hdsl24hSESLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 14),
    _Hdsl24hSESLoopACust_Type()
)
hdsl24hSESLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hSESLoopACust.setStatus("mandatory")
_Hdsl24hSESLoopBCust_Type = Integer32
_Hdsl24hSESLoopBCust_Object = MibTableColumn
hdsl24hSESLoopBCust = _Hdsl24hSESLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 2, 1, 15),
    _Hdsl24hSESLoopBCust_Type()
)
hdsl24hSESLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl24hSESLoopBCust.setStatus("mandatory")
_HdslSpanCurr24hPerformanceTable_Object = MibTable
hdslSpanCurr24hPerformanceTable = _HdslSpanCurr24hPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hdslSpanCurr24hPerformanceTable.setStatus("mandatory")
_HdslSpanCurr24hPerformanceEntry_Object = MibTableRow
hdslSpanCurr24hPerformanceEntry = _HdslSpanCurr24hPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1)
)
hdslSpanCurr24hPerformanceEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanCurr24hSlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanCurr24hSpanId"),
)
if mibBuilder.loadTexts:
    hdslSpanCurr24hPerformanceEntry.setStatus("mandatory")
_HdslSpanCurr24hSlotId_Type = Integer32
_HdslSpanCurr24hSlotId_Object = MibTableColumn
hdslSpanCurr24hSlotId = _HdslSpanCurr24hSlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 1),
    _HdslSpanCurr24hSlotId_Type()
)
hdslSpanCurr24hSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanCurr24hSlotId.setStatus("mandatory")
_HdslSpanCurr24hSpanId_Type = Integer32
_HdslSpanCurr24hSpanId_Object = MibTableColumn
hdslSpanCurr24hSpanId = _HdslSpanCurr24hSpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 2),
    _HdslSpanCurr24hSpanId_Type()
)
hdslSpanCurr24hSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanCurr24hSpanId.setStatus("mandatory")
_HdslCurr24hESLoopANet_Type = Integer32
_HdslCurr24hESLoopANet_Object = MibTableColumn
hdslCurr24hESLoopANet = _HdslCurr24hESLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 3),
    _HdslCurr24hESLoopANet_Type()
)
hdslCurr24hESLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hESLoopANet.setStatus("mandatory")
_HdslCurr24hESLoopBNet_Type = Integer32
_HdslCurr24hESLoopBNet_Object = MibTableColumn
hdslCurr24hESLoopBNet = _HdslCurr24hESLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 4),
    _HdslCurr24hESLoopBNet_Type()
)
hdslCurr24hESLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hESLoopBNet.setStatus("mandatory")
_HdslCurr24hUASLoopANet_Type = Integer32
_HdslCurr24hUASLoopANet_Object = MibTableColumn
hdslCurr24hUASLoopANet = _HdslCurr24hUASLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 5),
    _HdslCurr24hUASLoopANet_Type()
)
hdslCurr24hUASLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hUASLoopANet.setStatus("mandatory")
_HdslCurr24hUASLoopBNet_Type = Integer32
_HdslCurr24hUASLoopBNet_Object = MibTableColumn
hdslCurr24hUASLoopBNet = _HdslCurr24hUASLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 6),
    _HdslCurr24hUASLoopBNet_Type()
)
hdslCurr24hUASLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hUASLoopBNet.setStatus("mandatory")
_HdslCurr24hSESLoopANet_Type = Integer32
_HdslCurr24hSESLoopANet_Object = MibTableColumn
hdslCurr24hSESLoopANet = _HdslCurr24hSESLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 7),
    _HdslCurr24hSESLoopANet_Type()
)
hdslCurr24hSESLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hSESLoopANet.setStatus("mandatory")
_HdslCurr24hSESLoopBNet_Type = Integer32
_HdslCurr24hSESLoopBNet_Object = MibTableColumn
hdslCurr24hSESLoopBNet = _HdslCurr24hSESLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 8),
    _HdslCurr24hSESLoopBNet_Type()
)
hdslCurr24hSESLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hSESLoopBNet.setStatus("mandatory")
_HdslCurr24hESLoopACust_Type = Integer32
_HdslCurr24hESLoopACust_Object = MibTableColumn
hdslCurr24hESLoopACust = _HdslCurr24hESLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 9),
    _HdslCurr24hESLoopACust_Type()
)
hdslCurr24hESLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hESLoopACust.setStatus("mandatory")
_HdslCurr24hESLoopBCust_Type = Integer32
_HdslCurr24hESLoopBCust_Object = MibTableColumn
hdslCurr24hESLoopBCust = _HdslCurr24hESLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 10),
    _HdslCurr24hESLoopBCust_Type()
)
hdslCurr24hESLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hESLoopBCust.setStatus("mandatory")
_HdslCurr24hUASLoopACust_Type = Integer32
_HdslCurr24hUASLoopACust_Object = MibTableColumn
hdslCurr24hUASLoopACust = _HdslCurr24hUASLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 11),
    _HdslCurr24hUASLoopACust_Type()
)
hdslCurr24hUASLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hUASLoopACust.setStatus("mandatory")
_HdslCurr24hUASLoopBCust_Type = Integer32
_HdslCurr24hUASLoopBCust_Object = MibTableColumn
hdslCurr24hUASLoopBCust = _HdslCurr24hUASLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 12),
    _HdslCurr24hUASLoopBCust_Type()
)
hdslCurr24hUASLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hUASLoopBCust.setStatus("mandatory")
_HdslCurr24hSESLoopACust_Type = Integer32
_HdslCurr24hSESLoopACust_Object = MibTableColumn
hdslCurr24hSESLoopACust = _HdslCurr24hSESLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 13),
    _HdslCurr24hSESLoopACust_Type()
)
hdslCurr24hSESLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hSESLoopACust.setStatus("mandatory")
_HdslCurr24hSESLoopBCust_Type = Integer32
_HdslCurr24hSESLoopBCust_Object = MibTableColumn
hdslCurr24hSESLoopBCust = _HdslCurr24hSESLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 3, 1, 14),
    _HdslCurr24hSESLoopBCust_Type()
)
hdslCurr24hSESLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslCurr24hSESLoopBCust.setStatus("mandatory")
_HdslSpanStatisticsTable_Object = MibTable
hdslSpanStatisticsTable = _HdslSpanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4)
)
if mibBuilder.loadTexts:
    hdslSpanStatisticsTable.setStatus("mandatory")
_HdslSpanStatisticsEntry_Object = MibTableRow
hdslSpanStatisticsEntry = _HdslSpanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1)
)
hdslSpanStatisticsEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslStatisticsSlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslStatisticsSpanId"),
)
if mibBuilder.loadTexts:
    hdslSpanStatisticsEntry.setStatus("mandatory")
_HdslStatisticsSlotId_Type = Integer32
_HdslStatisticsSlotId_Object = MibTableColumn
hdslStatisticsSlotId = _HdslStatisticsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 1),
    _HdslStatisticsSlotId_Type()
)
hdslStatisticsSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslStatisticsSlotId.setStatus("mandatory")
_HdslStatisticsSpanId_Type = Integer32
_HdslStatisticsSpanId_Object = MibTableColumn
hdslStatisticsSpanId = _HdslStatisticsSpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 2),
    _HdslStatisticsSpanId_Type()
)
hdslStatisticsSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslStatisticsSpanId.setStatus("mandatory")
_HdslLoopPairState_Type = Byte
_HdslLoopPairState_Object = MibTableColumn
hdslLoopPairState = _HdslLoopPairState_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 3),
    _HdslLoopPairState_Type()
)
hdslLoopPairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLoopPairState.setStatus("mandatory")
_HdslLoopATipRingReversal_Type = Byte
_HdslLoopATipRingReversal_Object = MibTableColumn
hdslLoopATipRingReversal = _HdslLoopATipRingReversal_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 4),
    _HdslLoopATipRingReversal_Type()
)
hdslLoopATipRingReversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLoopATipRingReversal.setStatus("mandatory")
_HdslLoopBTipRingReversal_Type = Byte
_HdslLoopBTipRingReversal_Object = MibTableColumn
hdslLoopBTipRingReversal = _HdslLoopBTipRingReversal_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 5),
    _HdslLoopBTipRingReversal_Type()
)
hdslLoopBTipRingReversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLoopBTipRingReversal.setStatus("mandatory")
_HdslLoopAUpState_Type = Byte
_HdslLoopAUpState_Object = MibTableColumn
hdslLoopAUpState = _HdslLoopAUpState_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 6),
    _HdslLoopAUpState_Type()
)
hdslLoopAUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLoopAUpState.setStatus("mandatory")
_HdslLoopBUpState_Type = Byte
_HdslLoopBUpState_Object = MibTableColumn
hdslLoopBUpState = _HdslLoopBUpState_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 7),
    _HdslLoopBUpState_Type()
)
hdslLoopBUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLoopBUpState.setStatus("mandatory")
_HdslMarginLoopANet_Type = Byte
_HdslMarginLoopANet_Object = MibTableColumn
hdslMarginLoopANet = _HdslMarginLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 8),
    _HdslMarginLoopANet_Type()
)
hdslMarginLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLoopANet.setStatus("mandatory")
_HdslMarginHighLoopANet_Type = Byte
_HdslMarginHighLoopANet_Object = MibTableColumn
hdslMarginHighLoopANet = _HdslMarginHighLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 9),
    _HdslMarginHighLoopANet_Type()
)
hdslMarginHighLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginHighLoopANet.setStatus("mandatory")
_HdslMarginLowLoopANet_Type = Byte
_HdslMarginLowLoopANet_Object = MibTableColumn
hdslMarginLowLoopANet = _HdslMarginLowLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 10),
    _HdslMarginLowLoopANet_Type()
)
hdslMarginLowLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLowLoopANet.setStatus("mandatory")
_HdslMarginLoopBNet_Type = Byte
_HdslMarginLoopBNet_Object = MibTableColumn
hdslMarginLoopBNet = _HdslMarginLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 11),
    _HdslMarginLoopBNet_Type()
)
hdslMarginLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLoopBNet.setStatus("mandatory")
_HdslMarginHighLoopBNet_Type = Byte
_HdslMarginHighLoopBNet_Object = MibTableColumn
hdslMarginHighLoopBNet = _HdslMarginHighLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 12),
    _HdslMarginHighLoopBNet_Type()
)
hdslMarginHighLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginHighLoopBNet.setStatus("mandatory")
_HdslMarginLowLoopBNet_Type = Byte
_HdslMarginLowLoopBNet_Object = MibTableColumn
hdslMarginLowLoopBNet = _HdslMarginLowLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 13),
    _HdslMarginLowLoopBNet_Type()
)
hdslMarginLowLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLowLoopBNet.setStatus("mandatory")
_HdslPulseAttenuationLoopANet_Type = Byte
_HdslPulseAttenuationLoopANet_Object = MibTableColumn
hdslPulseAttenuationLoopANet = _HdslPulseAttenuationLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 14),
    _HdslPulseAttenuationLoopANet_Type()
)
hdslPulseAttenuationLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPulseAttenuationLoopANet.setStatus("mandatory")
_HdslPulseAttenuationLoopBNet_Type = Byte
_HdslPulseAttenuationLoopBNet_Object = MibTableColumn
hdslPulseAttenuationLoopBNet = _HdslPulseAttenuationLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 15),
    _HdslPulseAttenuationLoopBNet_Type()
)
hdslPulseAttenuationLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPulseAttenuationLoopBNet.setStatus("mandatory")
_HdslMarginLoopACust_Type = Byte
_HdslMarginLoopACust_Object = MibTableColumn
hdslMarginLoopACust = _HdslMarginLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 16),
    _HdslMarginLoopACust_Type()
)
hdslMarginLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLoopACust.setStatus("mandatory")
_HdslMarginHighLoopACust_Type = Byte
_HdslMarginHighLoopACust_Object = MibTableColumn
hdslMarginHighLoopACust = _HdslMarginHighLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 17),
    _HdslMarginHighLoopACust_Type()
)
hdslMarginHighLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginHighLoopACust.setStatus("mandatory")
_HdslMarginLowLoopACust_Type = Byte
_HdslMarginLowLoopACust_Object = MibTableColumn
hdslMarginLowLoopACust = _HdslMarginLowLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 18),
    _HdslMarginLowLoopACust_Type()
)
hdslMarginLowLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLowLoopACust.setStatus("mandatory")
_HdslMarginLoopBCust_Type = Byte
_HdslMarginLoopBCust_Object = MibTableColumn
hdslMarginLoopBCust = _HdslMarginLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 19),
    _HdslMarginLoopBCust_Type()
)
hdslMarginLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLoopBCust.setStatus("mandatory")
_HdslMarginHighLoopBCust_Type = Byte
_HdslMarginHighLoopBCust_Object = MibTableColumn
hdslMarginHighLoopBCust = _HdslMarginHighLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 20),
    _HdslMarginHighLoopBCust_Type()
)
hdslMarginHighLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginHighLoopBCust.setStatus("mandatory")
_HdslMarginLowLoopBCust_Type = Byte
_HdslMarginLowLoopBCust_Object = MibTableColumn
hdslMarginLowLoopBCust = _HdslMarginLowLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 21),
    _HdslMarginLowLoopBCust_Type()
)
hdslMarginLowLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginLowLoopBCust.setStatus("mandatory")
_HdslPulseAttenuationLoopACust_Type = Byte
_HdslPulseAttenuationLoopACust_Object = MibTableColumn
hdslPulseAttenuationLoopACust = _HdslPulseAttenuationLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 22),
    _HdslPulseAttenuationLoopACust_Type()
)
hdslPulseAttenuationLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPulseAttenuationLoopACust.setStatus("mandatory")
_HdslPulseAttenuationLoopBCust_Type = Byte
_HdslPulseAttenuationLoopBCust_Object = MibTableColumn
hdslPulseAttenuationLoopBCust = _HdslPulseAttenuationLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 4, 1, 23),
    _HdslPulseAttenuationLoopBCust_Type()
)
hdslPulseAttenuationLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPulseAttenuationLoopBCust.setStatus("mandatory")
_HdslSpanAlarmTable_Object = MibTable
hdslSpanAlarmTable = _HdslSpanAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5)
)
if mibBuilder.loadTexts:
    hdslSpanAlarmTable.setStatus("mandatory")
_HdslSpanAlarmEntry_Object = MibTableRow
hdslSpanAlarmEntry = _HdslSpanAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1)
)
hdslSpanAlarmEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanAlarmSlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanAlarmSpanId"),
)
if mibBuilder.loadTexts:
    hdslSpanAlarmEntry.setStatus("mandatory")
_HdslSpanAlarmSlotId_Type = Integer32
_HdslSpanAlarmSlotId_Object = MibTableColumn
hdslSpanAlarmSlotId = _HdslSpanAlarmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 1),
    _HdslSpanAlarmSlotId_Type()
)
hdslSpanAlarmSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanAlarmSlotId.setStatus("mandatory")
_HdslSpanAlarmSpanId_Type = Integer32
_HdslSpanAlarmSpanId_Object = MibTableColumn
hdslSpanAlarmSpanId = _HdslSpanAlarmSpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 2),
    _HdslSpanAlarmSpanId_Type()
)
hdslSpanAlarmSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanAlarmSpanId.setStatus("mandatory")
_HdslMarginAlarmLoopANet_Type = Byte
_HdslMarginAlarmLoopANet_Object = MibTableColumn
hdslMarginAlarmLoopANet = _HdslMarginAlarmLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 3),
    _HdslMarginAlarmLoopANet_Type()
)
hdslMarginAlarmLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmLoopANet.setStatus("mandatory")
_HdslMarginAlarmLoopBNet_Type = Byte
_HdslMarginAlarmLoopBNet_Object = MibTableColumn
hdslMarginAlarmLoopBNet = _HdslMarginAlarmLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 4),
    _HdslMarginAlarmLoopBNet_Type()
)
hdslMarginAlarmLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmLoopBNet.setStatus("mandatory")
_HdslESAlarmLoopANet_Type = Byte
_HdslESAlarmLoopANet_Object = MibTableColumn
hdslESAlarmLoopANet = _HdslESAlarmLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 5),
    _HdslESAlarmLoopANet_Type()
)
hdslESAlarmLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmLoopANet.setStatus("mandatory")
_HdslESAlarmLoopBNet_Type = Byte
_HdslESAlarmLoopBNet_Object = MibTableColumn
hdslESAlarmLoopBNet = _HdslESAlarmLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 6),
    _HdslESAlarmLoopBNet_Type()
)
hdslESAlarmLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmLoopBNet.setStatus("mandatory")
_HdslUASAlarmLoopANet_Type = Byte
_HdslUASAlarmLoopANet_Object = MibTableColumn
hdslUASAlarmLoopANet = _HdslUASAlarmLoopANet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 7),
    _HdslUASAlarmLoopANet_Type()
)
hdslUASAlarmLoopANet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmLoopANet.setStatus("mandatory")
_HdslUASAlarmLoopBNet_Type = Byte
_HdslUASAlarmLoopBNet_Object = MibTableColumn
hdslUASAlarmLoopBNet = _HdslUASAlarmLoopBNet_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 8),
    _HdslUASAlarmLoopBNet_Type()
)
hdslUASAlarmLoopBNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmLoopBNet.setStatus("mandatory")
_HdslMarginAlarmLoopACust_Type = Byte
_HdslMarginAlarmLoopACust_Object = MibTableColumn
hdslMarginAlarmLoopACust = _HdslMarginAlarmLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 9),
    _HdslMarginAlarmLoopACust_Type()
)
hdslMarginAlarmLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmLoopACust.setStatus("mandatory")
_HdslMarginAlarmLoopBCust_Type = Byte
_HdslMarginAlarmLoopBCust_Object = MibTableColumn
hdslMarginAlarmLoopBCust = _HdslMarginAlarmLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 10),
    _HdslMarginAlarmLoopBCust_Type()
)
hdslMarginAlarmLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmLoopBCust.setStatus("mandatory")
_HdslESAlarmLoopACust_Type = Byte
_HdslESAlarmLoopACust_Object = MibTableColumn
hdslESAlarmLoopACust = _HdslESAlarmLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 11),
    _HdslESAlarmLoopACust_Type()
)
hdslESAlarmLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmLoopACust.setStatus("mandatory")
_HdslESAlarmLoopBCust_Type = Byte
_HdslESAlarmLoopBCust_Object = MibTableColumn
hdslESAlarmLoopBCust = _HdslESAlarmLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 12),
    _HdslESAlarmLoopBCust_Type()
)
hdslESAlarmLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmLoopBCust.setStatus("mandatory")
_HdslUASAlarmLoopACust_Type = Byte
_HdslUASAlarmLoopACust_Object = MibTableColumn
hdslUASAlarmLoopACust = _HdslUASAlarmLoopACust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 13),
    _HdslUASAlarmLoopACust_Type()
)
hdslUASAlarmLoopACust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmLoopACust.setStatus("mandatory")
_HdslUASAlarmLoopBCust_Type = Byte
_HdslUASAlarmLoopBCust_Object = MibTableColumn
hdslUASAlarmLoopBCust = _HdslUASAlarmLoopBCust_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 14),
    _HdslUASAlarmLoopBCust_Type()
)
hdslUASAlarmLoopBCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmLoopBCust.setStatus("mandatory")
_HdslLOSWAlarmLoopA_Type = Byte
_HdslLOSWAlarmLoopA_Object = MibTableColumn
hdslLOSWAlarmLoopA = _HdslLOSWAlarmLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 15),
    _HdslLOSWAlarmLoopA_Type()
)
hdslLOSWAlarmLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmLoopA.setStatus("mandatory")
_HdslLOSWAlarmLoopB_Type = Byte
_HdslLOSWAlarmLoopB_Object = MibTableColumn
hdslLOSWAlarmLoopB = _HdslLOSWAlarmLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 16),
    _HdslLOSWAlarmLoopB_Type()
)
hdslLOSWAlarmLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmLoopB.setStatus("mandatory")
_HdslPFOAlarmLoopA_Type = Byte
_HdslPFOAlarmLoopA_Object = MibTableColumn
hdslPFOAlarmLoopA = _HdslPFOAlarmLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 17),
    _HdslPFOAlarmLoopA_Type()
)
hdslPFOAlarmLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmLoopA.setStatus("mandatory")
_HdslPFOAlarmLoopB_Type = Byte
_HdslPFOAlarmLoopB_Object = MibTableColumn
hdslPFOAlarmLoopB = _HdslPFOAlarmLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 18),
    _HdslPFOAlarmLoopB_Type()
)
hdslPFOAlarmLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmLoopB.setStatus("mandatory")
_HdslPFSAlarmLoopA_Type = Byte
_HdslPFSAlarmLoopA_Object = MibTableColumn
hdslPFSAlarmLoopA = _HdslPFSAlarmLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 19),
    _HdslPFSAlarmLoopA_Type()
)
hdslPFSAlarmLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmLoopA.setStatus("mandatory")
_HdslPFSAlarmLoopB_Type = Byte
_HdslPFSAlarmLoopB_Object = MibTableColumn
hdslPFSAlarmLoopB = _HdslPFSAlarmLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 20),
    _HdslPFSAlarmLoopB_Type()
)
hdslPFSAlarmLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmLoopB.setStatus("mandatory")
_HdslBERAlarmLoopA_Type = Byte
_HdslBERAlarmLoopA_Object = MibTableColumn
hdslBERAlarmLoopA = _HdslBERAlarmLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 21),
    _HdslBERAlarmLoopA_Type()
)
hdslBERAlarmLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmLoopA.setStatus("mandatory")
_HdslBERAlarmLoopB_Type = Byte
_HdslBERAlarmLoopB_Object = MibTableColumn
hdslBERAlarmLoopB = _HdslBERAlarmLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 5, 1, 22),
    _HdslBERAlarmLoopB_Type()
)
hdslBERAlarmLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmLoopB.setStatus("mandatory")
_HdslSpanAlarmHistoryTable_Object = MibTable
hdslSpanAlarmHistoryTable = _HdslSpanAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6)
)
if mibBuilder.loadTexts:
    hdslSpanAlarmHistoryTable.setStatus("mandatory")
_HdslSpanAlarmHistoryEntry_Object = MibTableRow
hdslSpanAlarmHistoryEntry = _HdslSpanAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1)
)
hdslSpanAlarmHistoryEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanAlarmHistorySlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanAlarmHistorySpanId"),
)
if mibBuilder.loadTexts:
    hdslSpanAlarmHistoryEntry.setStatus("mandatory")
_HdslSpanAlarmHistorySlotId_Type = Integer32
_HdslSpanAlarmHistorySlotId_Object = MibTableColumn
hdslSpanAlarmHistorySlotId = _HdslSpanAlarmHistorySlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 1),
    _HdslSpanAlarmHistorySlotId_Type()
)
hdslSpanAlarmHistorySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanAlarmHistorySlotId.setStatus("mandatory")
_HdslSpanAlarmHistorySpanId_Type = Integer32
_HdslSpanAlarmHistorySpanId_Object = MibTableColumn
hdslSpanAlarmHistorySpanId = _HdslSpanAlarmHistorySpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 2),
    _HdslSpanAlarmHistorySpanId_Type()
)
hdslSpanAlarmHistorySpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanAlarmHistorySpanId.setStatus("mandatory")
_HdslMarginAlarmFirstLoopA_Type = PgTimeStamp
_HdslMarginAlarmFirstLoopA_Object = MibTableColumn
hdslMarginAlarmFirstLoopA = _HdslMarginAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 3),
    _HdslMarginAlarmFirstLoopA_Type()
)
hdslMarginAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmFirstLoopA.setStatus("mandatory")
_HdslMarginAlarmLastLoopA_Type = PgTimeStamp
_HdslMarginAlarmLastLoopA_Object = MibTableColumn
hdslMarginAlarmLastLoopA = _HdslMarginAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 4),
    _HdslMarginAlarmLastLoopA_Type()
)
hdslMarginAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmLastLoopA.setStatus("mandatory")
_HdslMarginAlarmCountLoopA_Type = Integer32
_HdslMarginAlarmCountLoopA_Object = MibTableColumn
hdslMarginAlarmCountLoopA = _HdslMarginAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 5),
    _HdslMarginAlarmCountLoopA_Type()
)
hdslMarginAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmCountLoopA.setStatus("mandatory")
_HdslMarginAlarmFirstLoopB_Type = PgTimeStamp
_HdslMarginAlarmFirstLoopB_Object = MibTableColumn
hdslMarginAlarmFirstLoopB = _HdslMarginAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 6),
    _HdslMarginAlarmFirstLoopB_Type()
)
hdslMarginAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmFirstLoopB.setStatus("mandatory")
_HdslMarginAlarmLastLoopB_Type = PgTimeStamp
_HdslMarginAlarmLastLoopB_Object = MibTableColumn
hdslMarginAlarmLastLoopB = _HdslMarginAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 7),
    _HdslMarginAlarmLastLoopB_Type()
)
hdslMarginAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmLastLoopB.setStatus("mandatory")
_HdslMarginAlarmCountLoopB_Type = Integer32
_HdslMarginAlarmCountLoopB_Object = MibTableColumn
hdslMarginAlarmCountLoopB = _HdslMarginAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 8),
    _HdslMarginAlarmCountLoopB_Type()
)
hdslMarginAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslMarginAlarmCountLoopB.setStatus("mandatory")
_HdslESAlarmFirstLoopA_Type = PgTimeStamp
_HdslESAlarmFirstLoopA_Object = MibTableColumn
hdslESAlarmFirstLoopA = _HdslESAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 9),
    _HdslESAlarmFirstLoopA_Type()
)
hdslESAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmFirstLoopA.setStatus("mandatory")
_HdslESAlarmLastLoopA_Type = PgTimeStamp
_HdslESAlarmLastLoopA_Object = MibTableColumn
hdslESAlarmLastLoopA = _HdslESAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 10),
    _HdslESAlarmLastLoopA_Type()
)
hdslESAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmLastLoopA.setStatus("mandatory")
_HdslESAlarmCountLoopA_Type = Integer32
_HdslESAlarmCountLoopA_Object = MibTableColumn
hdslESAlarmCountLoopA = _HdslESAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 11),
    _HdslESAlarmCountLoopA_Type()
)
hdslESAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmCountLoopA.setStatus("mandatory")
_HdslESAlarmFirstLoopB_Type = PgTimeStamp
_HdslESAlarmFirstLoopB_Object = MibTableColumn
hdslESAlarmFirstLoopB = _HdslESAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 12),
    _HdslESAlarmFirstLoopB_Type()
)
hdslESAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmFirstLoopB.setStatus("mandatory")
_HdslESAlarmLastLoopB_Type = PgTimeStamp
_HdslESAlarmLastLoopB_Object = MibTableColumn
hdslESAlarmLastLoopB = _HdslESAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 13),
    _HdslESAlarmLastLoopB_Type()
)
hdslESAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmLastLoopB.setStatus("mandatory")
_HdslESAlarmCountLoopB_Type = Integer32
_HdslESAlarmCountLoopB_Object = MibTableColumn
hdslESAlarmCountLoopB = _HdslESAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 14),
    _HdslESAlarmCountLoopB_Type()
)
hdslESAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslESAlarmCountLoopB.setStatus("mandatory")
_HdslUASAlarmFirstLoopA_Type = PgTimeStamp
_HdslUASAlarmFirstLoopA_Object = MibTableColumn
hdslUASAlarmFirstLoopA = _HdslUASAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 15),
    _HdslUASAlarmFirstLoopA_Type()
)
hdslUASAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmFirstLoopA.setStatus("mandatory")
_HdslUASAlarmLastLoopA_Type = PgTimeStamp
_HdslUASAlarmLastLoopA_Object = MibTableColumn
hdslUASAlarmLastLoopA = _HdslUASAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 16),
    _HdslUASAlarmLastLoopA_Type()
)
hdslUASAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmLastLoopA.setStatus("mandatory")
_HdslUASAlarmCountLoopA_Type = Integer32
_HdslUASAlarmCountLoopA_Object = MibTableColumn
hdslUASAlarmCountLoopA = _HdslUASAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 17),
    _HdslUASAlarmCountLoopA_Type()
)
hdslUASAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmCountLoopA.setStatus("mandatory")
_HdslUASAlarmFirstLoopB_Type = PgTimeStamp
_HdslUASAlarmFirstLoopB_Object = MibTableColumn
hdslUASAlarmFirstLoopB = _HdslUASAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 18),
    _HdslUASAlarmFirstLoopB_Type()
)
hdslUASAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmFirstLoopB.setStatus("mandatory")
_HdslUASAlarmLastLoopB_Type = PgTimeStamp
_HdslUASAlarmLastLoopB_Object = MibTableColumn
hdslUASAlarmLastLoopB = _HdslUASAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 19),
    _HdslUASAlarmLastLoopB_Type()
)
hdslUASAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmLastLoopB.setStatus("mandatory")
_HdslUASAlarmCountLoopB_Type = Integer32
_HdslUASAlarmCountLoopB_Object = MibTableColumn
hdslUASAlarmCountLoopB = _HdslUASAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 20),
    _HdslUASAlarmCountLoopB_Type()
)
hdslUASAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslUASAlarmCountLoopB.setStatus("mandatory")
_HdslLOSWAlarmFirstLoopA_Type = PgTimeStamp
_HdslLOSWAlarmFirstLoopA_Object = MibTableColumn
hdslLOSWAlarmFirstLoopA = _HdslLOSWAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 21),
    _HdslLOSWAlarmFirstLoopA_Type()
)
hdslLOSWAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmFirstLoopA.setStatus("mandatory")
_HdslLOSWAlarmLastLoopA_Type = PgTimeStamp
_HdslLOSWAlarmLastLoopA_Object = MibTableColumn
hdslLOSWAlarmLastLoopA = _HdslLOSWAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 22),
    _HdslLOSWAlarmLastLoopA_Type()
)
hdslLOSWAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmLastLoopA.setStatus("mandatory")
_HdslLOSWAlarmCountLoopA_Type = Integer32
_HdslLOSWAlarmCountLoopA_Object = MibTableColumn
hdslLOSWAlarmCountLoopA = _HdslLOSWAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 23),
    _HdslLOSWAlarmCountLoopA_Type()
)
hdslLOSWAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmCountLoopA.setStatus("mandatory")
_HdslLOSWAlarmFirstLoopB_Type = PgTimeStamp
_HdslLOSWAlarmFirstLoopB_Object = MibTableColumn
hdslLOSWAlarmFirstLoopB = _HdslLOSWAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 24),
    _HdslLOSWAlarmFirstLoopB_Type()
)
hdslLOSWAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmFirstLoopB.setStatus("mandatory")
_HdslLOSWAlarmLastLoopB_Type = PgTimeStamp
_HdslLOSWAlarmLastLoopB_Object = MibTableColumn
hdslLOSWAlarmLastLoopB = _HdslLOSWAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 25),
    _HdslLOSWAlarmLastLoopB_Type()
)
hdslLOSWAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmLastLoopB.setStatus("mandatory")
_HdslLOSWAlarmCountLoopB_Type = Integer32
_HdslLOSWAlarmCountLoopB_Object = MibTableColumn
hdslLOSWAlarmCountLoopB = _HdslLOSWAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 26),
    _HdslLOSWAlarmCountLoopB_Type()
)
hdslLOSWAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslLOSWAlarmCountLoopB.setStatus("mandatory")
_HdslPFOAlarmFirstLoopA_Type = PgTimeStamp
_HdslPFOAlarmFirstLoopA_Object = MibTableColumn
hdslPFOAlarmFirstLoopA = _HdslPFOAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 27),
    _HdslPFOAlarmFirstLoopA_Type()
)
hdslPFOAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmFirstLoopA.setStatus("mandatory")
_HdslPFOAlarmLastLoopA_Type = PgTimeStamp
_HdslPFOAlarmLastLoopA_Object = MibTableColumn
hdslPFOAlarmLastLoopA = _HdslPFOAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 28),
    _HdslPFOAlarmLastLoopA_Type()
)
hdslPFOAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmLastLoopA.setStatus("mandatory")
_HdslPFOAlarmCountLoopA_Type = Integer32
_HdslPFOAlarmCountLoopA_Object = MibTableColumn
hdslPFOAlarmCountLoopA = _HdslPFOAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 29),
    _HdslPFOAlarmCountLoopA_Type()
)
hdslPFOAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmCountLoopA.setStatus("mandatory")
_HdslPFOAlarmFirstLoopB_Type = PgTimeStamp
_HdslPFOAlarmFirstLoopB_Object = MibTableColumn
hdslPFOAlarmFirstLoopB = _HdslPFOAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 30),
    _HdslPFOAlarmFirstLoopB_Type()
)
hdslPFOAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmFirstLoopB.setStatus("mandatory")
_HdslPFOAlarmLastLoopB_Type = PgTimeStamp
_HdslPFOAlarmLastLoopB_Object = MibTableColumn
hdslPFOAlarmLastLoopB = _HdslPFOAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 31),
    _HdslPFOAlarmLastLoopB_Type()
)
hdslPFOAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmLastLoopB.setStatus("mandatory")
_HdslPFOAlarmCountLoopB_Type = Integer32
_HdslPFOAlarmCountLoopB_Object = MibTableColumn
hdslPFOAlarmCountLoopB = _HdslPFOAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 32),
    _HdslPFOAlarmCountLoopB_Type()
)
hdslPFOAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFOAlarmCountLoopB.setStatus("mandatory")
_HdslPFSAlarmFirstLoopA_Type = PgTimeStamp
_HdslPFSAlarmFirstLoopA_Object = MibTableColumn
hdslPFSAlarmFirstLoopA = _HdslPFSAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 33),
    _HdslPFSAlarmFirstLoopA_Type()
)
hdslPFSAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmFirstLoopA.setStatus("mandatory")
_HdslPFSAlarmLastLoopA_Type = PgTimeStamp
_HdslPFSAlarmLastLoopA_Object = MibTableColumn
hdslPFSAlarmLastLoopA = _HdslPFSAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 34),
    _HdslPFSAlarmLastLoopA_Type()
)
hdslPFSAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmLastLoopA.setStatus("mandatory")
_HdslPFSAlarmCountLoopA_Type = Integer32
_HdslPFSAlarmCountLoopA_Object = MibTableColumn
hdslPFSAlarmCountLoopA = _HdslPFSAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 35),
    _HdslPFSAlarmCountLoopA_Type()
)
hdslPFSAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmCountLoopA.setStatus("mandatory")
_HdslPFSAlarmFirstLoopB_Type = PgTimeStamp
_HdslPFSAlarmFirstLoopB_Object = MibTableColumn
hdslPFSAlarmFirstLoopB = _HdslPFSAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 36),
    _HdslPFSAlarmFirstLoopB_Type()
)
hdslPFSAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmFirstLoopB.setStatus("mandatory")
_HdslPFSAlarmLastLoopB_Type = PgTimeStamp
_HdslPFSAlarmLastLoopB_Object = MibTableColumn
hdslPFSAlarmLastLoopB = _HdslPFSAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 37),
    _HdslPFSAlarmLastLoopB_Type()
)
hdslPFSAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmLastLoopB.setStatus("mandatory")
_HdslPFSAlarmCountLoopB_Type = Integer32
_HdslPFSAlarmCountLoopB_Object = MibTableColumn
hdslPFSAlarmCountLoopB = _HdslPFSAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 38),
    _HdslPFSAlarmCountLoopB_Type()
)
hdslPFSAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslPFSAlarmCountLoopB.setStatus("mandatory")
_HdslBERAlarmFirstLoopA_Type = PgTimeStamp
_HdslBERAlarmFirstLoopA_Object = MibTableColumn
hdslBERAlarmFirstLoopA = _HdslBERAlarmFirstLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 39),
    _HdslBERAlarmFirstLoopA_Type()
)
hdslBERAlarmFirstLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmFirstLoopA.setStatus("mandatory")
_HdslBERAlarmLastLoopA_Type = PgTimeStamp
_HdslBERAlarmLastLoopA_Object = MibTableColumn
hdslBERAlarmLastLoopA = _HdslBERAlarmLastLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 40),
    _HdslBERAlarmLastLoopA_Type()
)
hdslBERAlarmLastLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmLastLoopA.setStatus("mandatory")
_HdslBERAlarmCountLoopA_Type = Integer32
_HdslBERAlarmCountLoopA_Object = MibTableColumn
hdslBERAlarmCountLoopA = _HdslBERAlarmCountLoopA_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 41),
    _HdslBERAlarmCountLoopA_Type()
)
hdslBERAlarmCountLoopA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmCountLoopA.setStatus("mandatory")
_HdslBERAlarmFirstLoopB_Type = PgTimeStamp
_HdslBERAlarmFirstLoopB_Object = MibTableColumn
hdslBERAlarmFirstLoopB = _HdslBERAlarmFirstLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 42),
    _HdslBERAlarmFirstLoopB_Type()
)
hdslBERAlarmFirstLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmFirstLoopB.setStatus("mandatory")
_HdslBERAlarmLastLoopB_Type = PgTimeStamp
_HdslBERAlarmLastLoopB_Object = MibTableColumn
hdslBERAlarmLastLoopB = _HdslBERAlarmLastLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 43),
    _HdslBERAlarmLastLoopB_Type()
)
hdslBERAlarmLastLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmLastLoopB.setStatus("mandatory")
_HdslBERAlarmCountLoopB_Type = Integer32
_HdslBERAlarmCountLoopB_Object = MibTableColumn
hdslBERAlarmCountLoopB = _HdslBERAlarmCountLoopB_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 6, 1, 44),
    _HdslBERAlarmCountLoopB_Type()
)
hdslBERAlarmCountLoopB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslBERAlarmCountLoopB.setStatus("mandatory")
_HdslSpanAlarmSeverityTable_Object = MibTable
hdslSpanAlarmSeverityTable = _HdslSpanAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7)
)
if mibBuilder.loadTexts:
    hdslSpanAlarmSeverityTable.setStatus("mandatory")
_HdslSpanAlarmSeverityEntry_Object = MibTableRow
hdslSpanAlarmSeverityEntry = _HdslSpanAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1)
)
hdslSpanAlarmSeverityEntry.setIndexNames(
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanAlarmSeveritySlotId"),
    (0, "PAIRGAIN-ETSI-HDSL-MIB", "hdslSpanAlarmSeveritySpanId"),
)
if mibBuilder.loadTexts:
    hdslSpanAlarmSeverityEntry.setStatus("mandatory")
_HdslSpanAlarmSeveritySlotId_Type = Integer32
_HdslSpanAlarmSeveritySlotId_Object = MibTableColumn
hdslSpanAlarmSeveritySlotId = _HdslSpanAlarmSeveritySlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 1),
    _HdslSpanAlarmSeveritySlotId_Type()
)
hdslSpanAlarmSeveritySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanAlarmSeveritySlotId.setStatus("mandatory")
_HdslSpanAlarmSeveritySpanId_Type = Integer32
_HdslSpanAlarmSeveritySpanId_Object = MibTableColumn
hdslSpanAlarmSeveritySpanId = _HdslSpanAlarmSeveritySpanId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 2),
    _HdslSpanAlarmSeveritySpanId_Type()
)
hdslSpanAlarmSeveritySpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslSpanAlarmSeveritySpanId.setStatus("mandatory")
_HdslSpanLOSWAlarmSetting_Type = PgAlarmSeverityProtectionSwitchMode
_HdslSpanLOSWAlarmSetting_Object = MibTableColumn
hdslSpanLOSWAlarmSetting = _HdslSpanLOSWAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 3),
    _HdslSpanLOSWAlarmSetting_Type()
)
hdslSpanLOSWAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanLOSWAlarmSetting.setStatus("mandatory")
_HdslSpanPFOAlarmSetting_Type = PgAlarmSeverityMode
_HdslSpanPFOAlarmSetting_Object = MibTableColumn
hdslSpanPFOAlarmSetting = _HdslSpanPFOAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 4),
    _HdslSpanPFOAlarmSetting_Type()
)
hdslSpanPFOAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanPFOAlarmSetting.setStatus("mandatory")
_HdslSpanPFSAlarmSetting_Type = PgAlarmSeverityMode
_HdslSpanPFSAlarmSetting_Object = MibTableColumn
hdslSpanPFSAlarmSetting = _HdslSpanPFSAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 5),
    _HdslSpanPFSAlarmSetting_Type()
)
hdslSpanPFSAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanPFSAlarmSetting.setStatus("mandatory")
_HdslSpanMarginThreshold_Type = Byte
_HdslSpanMarginThreshold_Object = MibTableColumn
hdslSpanMarginThreshold = _HdslSpanMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 6),
    _HdslSpanMarginThreshold_Type()
)
hdslSpanMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanMarginThreshold.setStatus("mandatory")
_HdslSpanMarginAlarmSetting_Type = PgAlarmSeverityProtectionSwitchMode
_HdslSpanMarginAlarmSetting_Object = MibTableColumn
hdslSpanMarginAlarmSetting = _HdslSpanMarginAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 7),
    _HdslSpanMarginAlarmSetting_Type()
)
hdslSpanMarginAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanMarginAlarmSetting.setStatus("mandatory")
_HdslSpanESThreshold_Type = Byte
_HdslSpanESThreshold_Object = MibTableColumn
hdslSpanESThreshold = _HdslSpanESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 8),
    _HdslSpanESThreshold_Type()
)
hdslSpanESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanESThreshold.setStatus("mandatory")
_HdslSpanESAlarmSetting_Type = PgAlarmSeverityProtectionSwitchMode
_HdslSpanESAlarmSetting_Object = MibTableColumn
hdslSpanESAlarmSetting = _HdslSpanESAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 9),
    _HdslSpanESAlarmSetting_Type()
)
hdslSpanESAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanESAlarmSetting.setStatus("mandatory")
_HdslSpanUASThreshold_Type = Byte
_HdslSpanUASThreshold_Object = MibTableColumn
hdslSpanUASThreshold = _HdslSpanUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 10),
    _HdslSpanUASThreshold_Type()
)
hdslSpanUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanUASThreshold.setStatus("mandatory")
_HdslSpanUASAlarmSetting_Type = PgAlarmSeverityMode
_HdslSpanUASAlarmSetting_Object = MibTableColumn
hdslSpanUASAlarmSetting = _HdslSpanUASAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 11),
    _HdslSpanUASAlarmSetting_Type()
)
hdslSpanUASAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanUASAlarmSetting.setStatus("mandatory")
_HdslSpanBERThreshold_Type = PgBERThreshold
_HdslSpanBERThreshold_Object = MibTableColumn
hdslSpanBERThreshold = _HdslSpanBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 12),
    _HdslSpanBERThreshold_Type()
)
hdslSpanBERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanBERThreshold.setStatus("mandatory")
_HdslSpanBERAlarmSetting_Type = PgAlarmSeverityMode
_HdslSpanBERAlarmSetting_Object = MibTableColumn
hdslSpanBERAlarmSetting = _HdslSpanBERAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 7, 7, 1, 13),
    _HdslSpanBERAlarmSetting_Type()
)
hdslSpanBERAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslSpanBERAlarmSetting.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-ETSI-HDSL-MIB",
    **{"Byte": Byte,
       "Short": Short,
       "PgTimeStamp": PgTimeStamp,
       "PgAlarmSeverityMode": PgAlarmSeverityMode,
       "PgAlarmSeverityProtectionSwitchMode": PgAlarmSeverityProtectionSwitchMode,
       "PgBERThreshold": PgBERThreshold,
       "hdslSpan15mPerformanceTable": hdslSpan15mPerformanceTable,
       "hdslSpan15mPerformanceEntry": hdslSpan15mPerformanceEntry,
       "hdslSpan15mSlotId": hdslSpan15mSlotId,
       "hdslSpan15mSpanId": hdslSpan15mSpanId,
       "hdslSpan15mHistoryId": hdslSpan15mHistoryId,
       "hdsl15mESLoopANet": hdsl15mESLoopANet,
       "hdsl15mESLoopBNet": hdsl15mESLoopBNet,
       "hdsl15mUASLoopANet": hdsl15mUASLoopANet,
       "hdsl15mUASLoopBNet": hdsl15mUASLoopBNet,
       "hdsl15mSESLoopANet": hdsl15mSESLoopANet,
       "hdsl15mSESLoopBNet": hdsl15mSESLoopBNet,
       "hdsl15mESLoopACust": hdsl15mESLoopACust,
       "hdsl15mESLoopBCust": hdsl15mESLoopBCust,
       "hdsl15mUASLoopACust": hdsl15mUASLoopACust,
       "hdsl15mUASLoopBCust": hdsl15mUASLoopBCust,
       "hdsl15mSESLoopACust": hdsl15mSESLoopACust,
       "hdsl15mSESLoopBCust": hdsl15mSESLoopBCust,
       "hdslSpan24hPerformanceTable": hdslSpan24hPerformanceTable,
       "hdslSpan24hPerformanceEntry": hdslSpan24hPerformanceEntry,
       "hdslSpan24hSlotId": hdslSpan24hSlotId,
       "hdslSpan24hSpanId": hdslSpan24hSpanId,
       "hdslSpan24hHistoryId": hdslSpan24hHistoryId,
       "hdsl24hESLoopANet": hdsl24hESLoopANet,
       "hdsl24hESLoopBNet": hdsl24hESLoopBNet,
       "hdsl24hUASLoopANet": hdsl24hUASLoopANet,
       "hdsl24hUASLoopBNet": hdsl24hUASLoopBNet,
       "hdsl24hSESLoopANet": hdsl24hSESLoopANet,
       "hdsl24hSESLoopBNet": hdsl24hSESLoopBNet,
       "hdsl24hESLoopACust": hdsl24hESLoopACust,
       "hdsl24hESLoopBCust": hdsl24hESLoopBCust,
       "hdsl24hUASLoopACust": hdsl24hUASLoopACust,
       "hdsl24hUASLoopBCust": hdsl24hUASLoopBCust,
       "hdsl24hSESLoopACust": hdsl24hSESLoopACust,
       "hdsl24hSESLoopBCust": hdsl24hSESLoopBCust,
       "hdslSpanCurr24hPerformanceTable": hdslSpanCurr24hPerformanceTable,
       "hdslSpanCurr24hPerformanceEntry": hdslSpanCurr24hPerformanceEntry,
       "hdslSpanCurr24hSlotId": hdslSpanCurr24hSlotId,
       "hdslSpanCurr24hSpanId": hdslSpanCurr24hSpanId,
       "hdslCurr24hESLoopANet": hdslCurr24hESLoopANet,
       "hdslCurr24hESLoopBNet": hdslCurr24hESLoopBNet,
       "hdslCurr24hUASLoopANet": hdslCurr24hUASLoopANet,
       "hdslCurr24hUASLoopBNet": hdslCurr24hUASLoopBNet,
       "hdslCurr24hSESLoopANet": hdslCurr24hSESLoopANet,
       "hdslCurr24hSESLoopBNet": hdslCurr24hSESLoopBNet,
       "hdslCurr24hESLoopACust": hdslCurr24hESLoopACust,
       "hdslCurr24hESLoopBCust": hdslCurr24hESLoopBCust,
       "hdslCurr24hUASLoopACust": hdslCurr24hUASLoopACust,
       "hdslCurr24hUASLoopBCust": hdslCurr24hUASLoopBCust,
       "hdslCurr24hSESLoopACust": hdslCurr24hSESLoopACust,
       "hdslCurr24hSESLoopBCust": hdslCurr24hSESLoopBCust,
       "hdslSpanStatisticsTable": hdslSpanStatisticsTable,
       "hdslSpanStatisticsEntry": hdslSpanStatisticsEntry,
       "hdslStatisticsSlotId": hdslStatisticsSlotId,
       "hdslStatisticsSpanId": hdslStatisticsSpanId,
       "hdslLoopPairState": hdslLoopPairState,
       "hdslLoopATipRingReversal": hdslLoopATipRingReversal,
       "hdslLoopBTipRingReversal": hdslLoopBTipRingReversal,
       "hdslLoopAUpState": hdslLoopAUpState,
       "hdslLoopBUpState": hdslLoopBUpState,
       "hdslMarginLoopANet": hdslMarginLoopANet,
       "hdslMarginHighLoopANet": hdslMarginHighLoopANet,
       "hdslMarginLowLoopANet": hdslMarginLowLoopANet,
       "hdslMarginLoopBNet": hdslMarginLoopBNet,
       "hdslMarginHighLoopBNet": hdslMarginHighLoopBNet,
       "hdslMarginLowLoopBNet": hdslMarginLowLoopBNet,
       "hdslPulseAttenuationLoopANet": hdslPulseAttenuationLoopANet,
       "hdslPulseAttenuationLoopBNet": hdslPulseAttenuationLoopBNet,
       "hdslMarginLoopACust": hdslMarginLoopACust,
       "hdslMarginHighLoopACust": hdslMarginHighLoopACust,
       "hdslMarginLowLoopACust": hdslMarginLowLoopACust,
       "hdslMarginLoopBCust": hdslMarginLoopBCust,
       "hdslMarginHighLoopBCust": hdslMarginHighLoopBCust,
       "hdslMarginLowLoopBCust": hdslMarginLowLoopBCust,
       "hdslPulseAttenuationLoopACust": hdslPulseAttenuationLoopACust,
       "hdslPulseAttenuationLoopBCust": hdslPulseAttenuationLoopBCust,
       "hdslSpanAlarmTable": hdslSpanAlarmTable,
       "hdslSpanAlarmEntry": hdslSpanAlarmEntry,
       "hdslSpanAlarmSlotId": hdslSpanAlarmSlotId,
       "hdslSpanAlarmSpanId": hdslSpanAlarmSpanId,
       "hdslMarginAlarmLoopANet": hdslMarginAlarmLoopANet,
       "hdslMarginAlarmLoopBNet": hdslMarginAlarmLoopBNet,
       "hdslESAlarmLoopANet": hdslESAlarmLoopANet,
       "hdslESAlarmLoopBNet": hdslESAlarmLoopBNet,
       "hdslUASAlarmLoopANet": hdslUASAlarmLoopANet,
       "hdslUASAlarmLoopBNet": hdslUASAlarmLoopBNet,
       "hdslMarginAlarmLoopACust": hdslMarginAlarmLoopACust,
       "hdslMarginAlarmLoopBCust": hdslMarginAlarmLoopBCust,
       "hdslESAlarmLoopACust": hdslESAlarmLoopACust,
       "hdslESAlarmLoopBCust": hdslESAlarmLoopBCust,
       "hdslUASAlarmLoopACust": hdslUASAlarmLoopACust,
       "hdslUASAlarmLoopBCust": hdslUASAlarmLoopBCust,
       "hdslLOSWAlarmLoopA": hdslLOSWAlarmLoopA,
       "hdslLOSWAlarmLoopB": hdslLOSWAlarmLoopB,
       "hdslPFOAlarmLoopA": hdslPFOAlarmLoopA,
       "hdslPFOAlarmLoopB": hdslPFOAlarmLoopB,
       "hdslPFSAlarmLoopA": hdslPFSAlarmLoopA,
       "hdslPFSAlarmLoopB": hdslPFSAlarmLoopB,
       "hdslBERAlarmLoopA": hdslBERAlarmLoopA,
       "hdslBERAlarmLoopB": hdslBERAlarmLoopB,
       "hdslSpanAlarmHistoryTable": hdslSpanAlarmHistoryTable,
       "hdslSpanAlarmHistoryEntry": hdslSpanAlarmHistoryEntry,
       "hdslSpanAlarmHistorySlotId": hdslSpanAlarmHistorySlotId,
       "hdslSpanAlarmHistorySpanId": hdslSpanAlarmHistorySpanId,
       "hdslMarginAlarmFirstLoopA": hdslMarginAlarmFirstLoopA,
       "hdslMarginAlarmLastLoopA": hdslMarginAlarmLastLoopA,
       "hdslMarginAlarmCountLoopA": hdslMarginAlarmCountLoopA,
       "hdslMarginAlarmFirstLoopB": hdslMarginAlarmFirstLoopB,
       "hdslMarginAlarmLastLoopB": hdslMarginAlarmLastLoopB,
       "hdslMarginAlarmCountLoopB": hdslMarginAlarmCountLoopB,
       "hdslESAlarmFirstLoopA": hdslESAlarmFirstLoopA,
       "hdslESAlarmLastLoopA": hdslESAlarmLastLoopA,
       "hdslESAlarmCountLoopA": hdslESAlarmCountLoopA,
       "hdslESAlarmFirstLoopB": hdslESAlarmFirstLoopB,
       "hdslESAlarmLastLoopB": hdslESAlarmLastLoopB,
       "hdslESAlarmCountLoopB": hdslESAlarmCountLoopB,
       "hdslUASAlarmFirstLoopA": hdslUASAlarmFirstLoopA,
       "hdslUASAlarmLastLoopA": hdslUASAlarmLastLoopA,
       "hdslUASAlarmCountLoopA": hdslUASAlarmCountLoopA,
       "hdslUASAlarmFirstLoopB": hdslUASAlarmFirstLoopB,
       "hdslUASAlarmLastLoopB": hdslUASAlarmLastLoopB,
       "hdslUASAlarmCountLoopB": hdslUASAlarmCountLoopB,
       "hdslLOSWAlarmFirstLoopA": hdslLOSWAlarmFirstLoopA,
       "hdslLOSWAlarmLastLoopA": hdslLOSWAlarmLastLoopA,
       "hdslLOSWAlarmCountLoopA": hdslLOSWAlarmCountLoopA,
       "hdslLOSWAlarmFirstLoopB": hdslLOSWAlarmFirstLoopB,
       "hdslLOSWAlarmLastLoopB": hdslLOSWAlarmLastLoopB,
       "hdslLOSWAlarmCountLoopB": hdslLOSWAlarmCountLoopB,
       "hdslPFOAlarmFirstLoopA": hdslPFOAlarmFirstLoopA,
       "hdslPFOAlarmLastLoopA": hdslPFOAlarmLastLoopA,
       "hdslPFOAlarmCountLoopA": hdslPFOAlarmCountLoopA,
       "hdslPFOAlarmFirstLoopB": hdslPFOAlarmFirstLoopB,
       "hdslPFOAlarmLastLoopB": hdslPFOAlarmLastLoopB,
       "hdslPFOAlarmCountLoopB": hdslPFOAlarmCountLoopB,
       "hdslPFSAlarmFirstLoopA": hdslPFSAlarmFirstLoopA,
       "hdslPFSAlarmLastLoopA": hdslPFSAlarmLastLoopA,
       "hdslPFSAlarmCountLoopA": hdslPFSAlarmCountLoopA,
       "hdslPFSAlarmFirstLoopB": hdslPFSAlarmFirstLoopB,
       "hdslPFSAlarmLastLoopB": hdslPFSAlarmLastLoopB,
       "hdslPFSAlarmCountLoopB": hdslPFSAlarmCountLoopB,
       "hdslBERAlarmFirstLoopA": hdslBERAlarmFirstLoopA,
       "hdslBERAlarmLastLoopA": hdslBERAlarmLastLoopA,
       "hdslBERAlarmCountLoopA": hdslBERAlarmCountLoopA,
       "hdslBERAlarmFirstLoopB": hdslBERAlarmFirstLoopB,
       "hdslBERAlarmLastLoopB": hdslBERAlarmLastLoopB,
       "hdslBERAlarmCountLoopB": hdslBERAlarmCountLoopB,
       "hdslSpanAlarmSeverityTable": hdslSpanAlarmSeverityTable,
       "hdslSpanAlarmSeverityEntry": hdslSpanAlarmSeverityEntry,
       "hdslSpanAlarmSeveritySlotId": hdslSpanAlarmSeveritySlotId,
       "hdslSpanAlarmSeveritySpanId": hdslSpanAlarmSeveritySpanId,
       "hdslSpanLOSWAlarmSetting": hdslSpanLOSWAlarmSetting,
       "hdslSpanPFOAlarmSetting": hdslSpanPFOAlarmSetting,
       "hdslSpanPFSAlarmSetting": hdslSpanPFSAlarmSetting,
       "hdslSpanMarginThreshold": hdslSpanMarginThreshold,
       "hdslSpanMarginAlarmSetting": hdslSpanMarginAlarmSetting,
       "hdslSpanESThreshold": hdslSpanESThreshold,
       "hdslSpanESAlarmSetting": hdslSpanESAlarmSetting,
       "hdslSpanUASThreshold": hdslSpanUASThreshold,
       "hdslSpanUASAlarmSetting": hdslSpanUASAlarmSetting,
       "hdslSpanBERThreshold": hdslSpanBERThreshold,
       "hdslSpanBERAlarmSetting": hdslSpanBERAlarmSetting}
)
