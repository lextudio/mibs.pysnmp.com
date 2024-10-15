# SNMP MIB module (ADTRAN-ATLAS-BRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-BRI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:21 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLASBRImg_ObjectIdentity = ObjectIdentity
adATLASBRImg = _AdATLASBRImg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8)
)
_AdATLASBRIIfNumber_Type = Integer32
_AdATLASBRIIfNumber_Object = MibScalar
adATLASBRIIfNumber = _AdATLASBRIIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 1),
    _AdATLASBRIIfNumber_Type()
)
adATLASBRIIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfNumber.setStatus("mandatory")
_AdATLASBRIIfTable_Object = MibTable
adATLASBRIIfTable = _AdATLASBRIIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2)
)
if mibBuilder.loadTexts:
    adATLASBRIIfTable.setStatus("mandatory")
_AdATLASBRIIfEntry_Object = MibTableRow
adATLASBRIIfEntry = _AdATLASBRIIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1)
)
adATLASBRIIfEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfIndex"),
)
if mibBuilder.loadTexts:
    adATLASBRIIfEntry.setStatus("mandatory")
_AdATLASBRIIfIndex_Type = Integer32
_AdATLASBRIIfIndex_Object = MibTableColumn
adATLASBRIIfIndex = _AdATLASBRIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 1),
    _AdATLASBRIIfIndex_Type()
)
adATLASBRIIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfIndex.setStatus("mandatory")
_AdATLASBRIIfSlotNum_Type = Integer32
_AdATLASBRIIfSlotNum_Object = MibTableColumn
adATLASBRIIfSlotNum = _AdATLASBRIIfSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 2),
    _AdATLASBRIIfSlotNum_Type()
)
adATLASBRIIfSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfSlotNum.setStatus("mandatory")
_AdATLASBRIIfPortNum_Type = Integer32
_AdATLASBRIIfPortNum_Object = MibTableColumn
adATLASBRIIfPortNum = _AdATLASBRIIfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 3),
    _AdATLASBRIIfPortNum_Type()
)
adATLASBRIIfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfPortNum.setStatus("mandatory")


class _AdATLASBRIIfAlarmStatus_Type(Integer32):
    """Custom type adATLASBRIIfAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer1down", 2),
          ("layer1up", 1))
    )


_AdATLASBRIIfAlarmStatus_Type.__name__ = "Integer32"
_AdATLASBRIIfAlarmStatus_Object = MibTableColumn
adATLASBRIIfAlarmStatus = _AdATLASBRIIfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 4),
    _AdATLASBRIIfAlarmStatus_Type()
)
adATLASBRIIfAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfAlarmStatus.setStatus("mandatory")
_AdATLASBRIIfChanStatTable_Object = MibTable
adATLASBRIIfChanStatTable = _AdATLASBRIIfChanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3)
)
if mibBuilder.loadTexts:
    adATLASBRIIfChanStatTable.setStatus("mandatory")
_AdATLASBRIIfChanStatEntry_Object = MibTableRow
adATLASBRIIfChanStatEntry = _AdATLASBRIIfChanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1)
)
adATLASBRIIfChanStatEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfChanStatIndex"),
)
if mibBuilder.loadTexts:
    adATLASBRIIfChanStatEntry.setStatus("mandatory")
_AdATLASBRIIfChanStatIndex_Type = Integer32
_AdATLASBRIIfChanStatIndex_Object = MibTableColumn
adATLASBRIIfChanStatIndex = _AdATLASBRIIfChanStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 1),
    _AdATLASBRIIfChanStatIndex_Type()
)
adATLASBRIIfChanStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfChanStatIndex.setStatus("mandatory")


class _AdATLASBRIIfChanStatB1_Type(Integer32):
    """Custom type adATLASBRIIfChanStatB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("unallocated", 1))
    )


_AdATLASBRIIfChanStatB1_Type.__name__ = "Integer32"
_AdATLASBRIIfChanStatB1_Object = MibTableColumn
adATLASBRIIfChanStatB1 = _AdATLASBRIIfChanStatB1_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 2),
    _AdATLASBRIIfChanStatB1_Type()
)
adATLASBRIIfChanStatB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfChanStatB1.setStatus("mandatory")


class _AdATLASBRIIfChanStatB2_Type(Integer32):
    """Custom type adATLASBRIIfChanStatB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("unallocated", 1))
    )


_AdATLASBRIIfChanStatB2_Type.__name__ = "Integer32"
_AdATLASBRIIfChanStatB2_Object = MibTableColumn
adATLASBRIIfChanStatB2 = _AdATLASBRIIfChanStatB2_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 3),
    _AdATLASBRIIfChanStatB2_Type()
)
adATLASBRIIfChanStatB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfChanStatB2.setStatus("mandatory")


class _AdATLASBRIIfChanStatD_Type(Integer32):
    """Custom type adATLASBRIIfChanStatD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 2),
          ("unallocated", 1))
    )


_AdATLASBRIIfChanStatD_Type.__name__ = "Integer32"
_AdATLASBRIIfChanStatD_Object = MibTableColumn
adATLASBRIIfChanStatD = _AdATLASBRIIfChanStatD_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 4),
    _AdATLASBRIIfChanStatD_Type()
)
adATLASBRIIfChanStatD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRIIfChanStatD.setStatus("mandatory")
_AdATLASBRITstTable_Object = MibTable
adATLASBRITstTable = _AdATLASBRITstTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4)
)
if mibBuilder.loadTexts:
    adATLASBRITstTable.setStatus("mandatory")
_AdATLASBRITstEntry_Object = MibTableRow
adATLASBRITstEntry = _AdATLASBRITstEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1)
)
adATLASBRITstEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRITstIndex"),
)
if mibBuilder.loadTexts:
    adATLASBRITstEntry.setStatus("mandatory")
_AdATLASBRITstIndex_Type = Integer32
_AdATLASBRITstIndex_Object = MibTableColumn
adATLASBRITstIndex = _AdATLASBRITstIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1, 1),
    _AdATLASBRITstIndex_Type()
)
adATLASBRITstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASBRITstIndex.setStatus("mandatory")


class _AdATLASBRITstLLB_Type(Integer32):
    """Custom type adATLASBRITstLLB based on Integer32"""
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
        *(("lpBkAll", 5),
          ("lpBkB1", 2),
          ("lpBkB1B2", 4),
          ("lpBkB2", 3),
          ("none", 1))
    )


_AdATLASBRITstLLB_Type.__name__ = "Integer32"
_AdATLASBRITstLLB_Object = MibTableColumn
adATLASBRITstLLB = _AdATLASBRITstLLB_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1, 2),
    _AdATLASBRITstLLB_Type()
)
adATLASBRITstLLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASBRITstLLB.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-BRI-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adGenATLASmg": adGenATLASmg,
       "adATLASBRImg": adATLASBRImg,
       "adATLASBRIIfNumber": adATLASBRIIfNumber,
       "adATLASBRIIfTable": adATLASBRIIfTable,
       "adATLASBRIIfEntry": adATLASBRIIfEntry,
       "adATLASBRIIfIndex": adATLASBRIIfIndex,
       "adATLASBRIIfSlotNum": adATLASBRIIfSlotNum,
       "adATLASBRIIfPortNum": adATLASBRIIfPortNum,
       "adATLASBRIIfAlarmStatus": adATLASBRIIfAlarmStatus,
       "adATLASBRIIfChanStatTable": adATLASBRIIfChanStatTable,
       "adATLASBRIIfChanStatEntry": adATLASBRIIfChanStatEntry,
       "adATLASBRIIfChanStatIndex": adATLASBRIIfChanStatIndex,
       "adATLASBRIIfChanStatB1": adATLASBRIIfChanStatB1,
       "adATLASBRIIfChanStatB2": adATLASBRIIfChanStatB2,
       "adATLASBRIIfChanStatD": adATLASBRIIfChanStatD,
       "adATLASBRITstTable": adATLASBRITstTable,
       "adATLASBRITstEntry": adATLASBRITstEntry,
       "adATLASBRITstIndex": adATLASBRITstIndex,
       "adATLASBRITstLLB": adATLASBRITstLLB}
)
