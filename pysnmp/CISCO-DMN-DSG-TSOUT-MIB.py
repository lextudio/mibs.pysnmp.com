# SNMP MIB module (CISCO-DMN-DSG-TSOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-TSOUT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:36 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGTSOUT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34)
)
ciscoDSGTSOUT.setRevisions(
        ("2012-03-20 11:00",
         "2010-08-24 07:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TsoutTable_Object = MibTable
tsoutTable = _TsoutTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1)
)
if mibBuilder.loadTexts:
    tsoutTable.setStatus("current")
_TsoutEntry_Object = MibTableRow
tsoutEntry = _TsoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1)
)
tsoutEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TSOUT-MIB", "tsoutID"),
)
if mibBuilder.loadTexts:
    tsoutEntry.setStatus("current")


class _TsoutID_Type(Integer32):
    """Custom type tsoutID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TsoutID_Type.__name__ = "Integer32"
_TsoutID_Object = MibTableColumn
tsoutID = _TsoutID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 1),
    _TsoutID_Type()
)
tsoutID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsoutID.setStatus("current")


class _TsoutInstanceName_Type(DisplayString):
    """Custom type tsoutInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TsoutInstanceName_Type.__name__ = "DisplayString"
_TsoutInstanceName_Object = MibTableColumn
tsoutInstanceName = _TsoutInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 2),
    _TsoutInstanceName_Type()
)
tsoutInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsoutInstanceName.setStatus("current")


class _TsoutOutputMode_Type(Integer32):
    """Custom type tsoutOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fullDpmControl", 6),
          ("mapPassthrough", 4),
          ("mapserviceChannelOnly", 5),
          ("noOutput", 1),
          ("passThrough", 2),
          ("serviceChannelOnly", 3),
          ("transcoding", 7))
    )


_TsoutOutputMode_Type.__name__ = "Integer32"
_TsoutOutputMode_Object = MibTableColumn
tsoutOutputMode = _TsoutOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 3),
    _TsoutOutputMode_Type()
)
tsoutOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsoutOutputMode.setStatus("current")


class _TsoutDescrambleMode_Type(Integer32):
    """Custom type tsoutDescrambleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deScrambled", 1),
          ("scrambled", 2))
    )


_TsoutDescrambleMode_Type.__name__ = "Integer32"
_TsoutDescrambleMode_Object = MibTableColumn
tsoutDescrambleMode = _TsoutDescrambleMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 4),
    _TsoutDescrambleMode_Type()
)
tsoutDescrambleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsoutDescrambleMode.setStatus("current")


class _TsoutRateControl_Type(Integer32):
    """Custom type tsoutRateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("user", 2))
    )


_TsoutRateControl_Type.__name__ = "Integer32"
_TsoutRateControl_Object = MibTableColumn
tsoutRateControl = _TsoutRateControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 5),
    _TsoutRateControl_Type()
)
tsoutRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsoutRateControl.setStatus("current")


class _TsoutOutputRate_Type(Integer32):
    """Custom type tsoutOutputRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 206000000),
    )


_TsoutOutputRate_Type.__name__ = "Integer32"
_TsoutOutputRate_Object = MibTableColumn
tsoutOutputRate = _TsoutOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 6),
    _TsoutOutputRate_Type()
)
tsoutOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsoutOutputRate.setStatus("current")


class _TsoutInsertNullPkt_Type(Integer32):
    """Custom type tsoutInsertNullPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TsoutInsertNullPkt_Type.__name__ = "Integer32"
_TsoutInsertNullPkt_Object = MibTableColumn
tsoutInsertNullPkt = _TsoutInsertNullPkt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 7),
    _TsoutInsertNullPkt_Type()
)
tsoutInsertNullPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsoutInsertNullPkt.setStatus("current")


class _TsoutMOIPOutputMode_Type(Integer32):
    """Custom type tsoutMOIPOutputMode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fullDpmControl", 6),
          ("mapPassthrough", 4),
          ("mapServiceChannelsOnly", 5),
          ("noOutput", 1),
          ("passThrough", 2),
          ("serviceChannelsOnly", 3),
          ("sptsFullDpmControl", 10),
          ("sptsMapServiceChannelsOnly", 9),
          ("sptsServiceChannelsOnly", 8),
          ("transcoding", 7))
    )


_TsoutMOIPOutputMode_Type.__name__ = "Integer32"
_TsoutMOIPOutputMode_Object = MibTableColumn
tsoutMOIPOutputMode = _TsoutMOIPOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 8),
    _TsoutMOIPOutputMode_Type()
)
tsoutMOIPOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsoutMOIPOutputMode.setStatus("current")
_TsoutStatusTable_Object = MibTable
tsoutStatusTable = _TsoutStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2)
)
if mibBuilder.loadTexts:
    tsoutStatusTable.setStatus("current")
_TsoutStatusEntry_Object = MibTableRow
tsoutStatusEntry = _TsoutStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1)
)
tsoutStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TSOUT-MIB", "tsoutStatusID"),
)
if mibBuilder.loadTexts:
    tsoutStatusEntry.setStatus("current")


class _TsoutStatusID_Type(Integer32):
    """Custom type tsoutStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TsoutStatusID_Type.__name__ = "Integer32"
_TsoutStatusID_Object = MibTableColumn
tsoutStatusID = _TsoutStatusID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 1),
    _TsoutStatusID_Type()
)
tsoutStatusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsoutStatusID.setStatus("current")


class _TsoutStatusInstanceName_Type(DisplayString):
    """Custom type tsoutStatusInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TsoutStatusInstanceName_Type.__name__ = "DisplayString"
_TsoutStatusInstanceName_Object = MibTableColumn
tsoutStatusInstanceName = _TsoutStatusInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 2),
    _TsoutStatusInstanceName_Type()
)
tsoutStatusInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsoutStatusInstanceName.setStatus("current")


class _TsoutStatusRate_Type(Integer32):
    """Custom type tsoutStatusRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TsoutStatusRate_Type.__name__ = "Integer32"
_TsoutStatusRate_Object = MibTableColumn
tsoutStatusRate = _TsoutStatusRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 3),
    _TsoutStatusRate_Type()
)
tsoutStatusRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsoutStatusRate.setStatus("current")


class _TsoutStatusFree_Type(Integer32):
    """Custom type tsoutStatusFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TsoutStatusFree_Type.__name__ = "Integer32"
_TsoutStatusFree_Object = MibTableColumn
tsoutStatusFree = _TsoutStatusFree_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 4),
    _TsoutStatusFree_Type()
)
tsoutStatusFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsoutStatusFree.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-TSOUT-MIB",
    **{"ciscoDSGTSOUT": ciscoDSGTSOUT,
       "tsoutTable": tsoutTable,
       "tsoutEntry": tsoutEntry,
       "tsoutID": tsoutID,
       "tsoutInstanceName": tsoutInstanceName,
       "tsoutOutputMode": tsoutOutputMode,
       "tsoutDescrambleMode": tsoutDescrambleMode,
       "tsoutRateControl": tsoutRateControl,
       "tsoutOutputRate": tsoutOutputRate,
       "tsoutInsertNullPkt": tsoutInsertNullPkt,
       "tsoutMOIPOutputMode": tsoutMOIPOutputMode,
       "tsoutStatusTable": tsoutStatusTable,
       "tsoutStatusEntry": tsoutStatusEntry,
       "tsoutStatusID": tsoutStatusID,
       "tsoutStatusInstanceName": tsoutStatusInstanceName,
       "tsoutStatusRate": tsoutStatusRate,
       "tsoutStatusFree": tsoutStatusFree}
)
