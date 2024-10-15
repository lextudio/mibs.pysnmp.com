# SNMP MIB module (Vct-Loopdetect-59-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Vct-Loopdetect-59-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:24 2024
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
 enterprises,
 experimental,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10switch_ObjectIdentity = ObjectIdentity
zxr10switch = _Zxr10switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102)
)
_Switch59vct_ObjectIdentity = ObjectIdentity
switch59vct = _Switch59vct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24)
)
_VctTable_Object = MibTable
vctTable = _VctTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1)
)
if mibBuilder.loadTexts:
    vctTable.setStatus("current")
_VctEntry_Object = MibTableRow
vctEntry = _VctEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1)
)
vctEntry.setIndexNames(
    (0, "Vct-Loopdetect-59-MIB", "vctIfindex"),
)
if mibBuilder.loadTexts:
    vctEntry.setStatus("current")
_VctIfindex_Type = Integer32
_VctIfindex_Object = MibTableColumn
vctIfindex = _VctIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 1),
    _VctIfindex_Type()
)
vctIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctIfindex.setStatus("current")


class _VctSetIfindex_Type(Integer32):
    """Custom type vctSetIfindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VctSetIfindex_Type.__name__ = "Integer32"
_VctSetIfindex_Object = MibTableColumn
vctSetIfindex = _VctSetIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 2),
    _VctSetIfindex_Type()
)
vctSetIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctSetIfindex.setStatus("current")


class _CableStatus_Type(Integer32):
    """Custom type cableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 0),
          ("good", 1))
    )


_CableStatus_Type.__name__ = "Integer32"
_CableStatus_Object = MibTableColumn
cableStatus = _CableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 3),
    _CableStatus_Type()
)
cableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableStatus.setStatus("current")


class _DoubleCableStatus1_2_Type(Integer32):
    """Custom type doubleCableStatus1_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus1_2_Type.__name__ = "Integer32"
_DoubleCableStatus1_2_Object = MibScalar
doubleCableStatus1_2 = _DoubleCableStatus1_2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 4),
    _DoubleCableStatus1_2_Type()
)
doubleCableStatus1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus1_2.setStatus("current")


class _DoubleCableStatus3_6_Type(Integer32):
    """Custom type doubleCableStatus3_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus3_6_Type.__name__ = "Integer32"
_DoubleCableStatus3_6_Object = MibScalar
doubleCableStatus3_6 = _DoubleCableStatus3_6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 5),
    _DoubleCableStatus3_6_Type()
)
doubleCableStatus3_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus3_6.setStatus("current")


class _DoubleCableStatus4_5_Type(Integer32):
    """Custom type doubleCableStatus4_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus4_5_Type.__name__ = "Integer32"
_DoubleCableStatus4_5_Object = MibScalar
doubleCableStatus4_5 = _DoubleCableStatus4_5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 6),
    _DoubleCableStatus4_5_Type()
)
doubleCableStatus4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus4_5.setStatus("current")


class _DoubleCableStatus7_8_Type(Integer32):
    """Custom type doubleCableStatus7_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus7_8_Type.__name__ = "Integer32"
_DoubleCableStatus7_8_Object = MibScalar
doubleCableStatus7_8 = _DoubleCableStatus7_8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 7),
    _DoubleCableStatus7_8_Type()
)
doubleCableStatus7_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus7_8.setStatus("current")


class _DoubleCableLength1_2_Type(Integer32):
    """Custom type doubleCableLength1_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength1_2_Type.__name__ = "Integer32"
_DoubleCableLength1_2_Object = MibScalar
doubleCableLength1_2 = _DoubleCableLength1_2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 8),
    _DoubleCableLength1_2_Type()
)
doubleCableLength1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength1_2.setStatus("current")


class _DoubleCableLength3_6_Type(Integer32):
    """Custom type doubleCableLength3_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength3_6_Type.__name__ = "Integer32"
_DoubleCableLength3_6_Object = MibScalar
doubleCableLength3_6 = _DoubleCableLength3_6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 9),
    _DoubleCableLength3_6_Type()
)
doubleCableLength3_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength3_6.setStatus("current")


class _DoubleCableLength4_5_Type(Integer32):
    """Custom type doubleCableLength4_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength4_5_Type.__name__ = "Integer32"
_DoubleCableLength4_5_Object = MibScalar
doubleCableLength4_5 = _DoubleCableLength4_5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 10),
    _DoubleCableLength4_5_Type()
)
doubleCableLength4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength4_5.setStatus("current")


class _DoubleCableLength7_8_Type(Integer32):
    """Custom type doubleCableLength7_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength7_8_Type.__name__ = "Integer32"
_DoubleCableLength7_8_Object = MibScalar
doubleCableLength7_8 = _DoubleCableLength7_8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 24, 1, 1, 11),
    _DoubleCableLength7_8_Type()
)
doubleCableLength7_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength7_8.setStatus("current")
_Switch59loopdetect_ObjectIdentity = ObjectIdentity
switch59loopdetect = _Switch59loopdetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25)
)


class _LoopdetectReopenTime_Type(Integer32):
    """Custom type loopdetectReopenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777216),
    )


_LoopdetectReopenTime_Type.__name__ = "Integer32"
_LoopdetectReopenTime_Object = MibScalar
loopdetectReopenTime = _LoopdetectReopenTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 1),
    _LoopdetectReopenTime_Type()
)
loopdetectReopenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopdetectReopenTime.setStatus("current")
_LoopdetectTable_Object = MibTable
loopdetectTable = _LoopdetectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2)
)
if mibBuilder.loadTexts:
    loopdetectTable.setStatus("current")
_LoopdetectEntry_Object = MibTableRow
loopdetectEntry = _LoopdetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1)
)
loopdetectEntry.setIndexNames(
    (0, "Vct-Loopdetect-59-MIB", "loopdetectPortIfindex"),
)
if mibBuilder.loadTexts:
    loopdetectEntry.setStatus("current")
_LoopdetectPortIfindex_Type = Integer32
_LoopdetectPortIfindex_Object = MibTableColumn
loopdetectPortIfindex = _LoopdetectPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 1),
    _LoopdetectPortIfindex_Type()
)
loopdetectPortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loopdetectPortIfindex.setStatus("current")


class _LoopdetectPortOperStatus_Type(Integer32):
    """Custom type loopdetectPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_LoopdetectPortOperStatus_Type.__name__ = "Integer32"
_LoopdetectPortOperStatus_Object = MibTableColumn
loopdetectPortOperStatus = _LoopdetectPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 2),
    _LoopdetectPortOperStatus_Type()
)
loopdetectPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectPortOperStatus.setStatus("current")


class _LoopdetectPortControl_Type(Integer32):
    """Custom type loopdetectPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LoopdetectPortControl_Type.__name__ = "Integer32"
_LoopdetectPortControl_Object = MibTableColumn
loopdetectPortControl = _LoopdetectPortControl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 3),
    _LoopdetectPortControl_Type()
)
loopdetectPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopdetectPortControl.setStatus("current")


class _LoopdetectPortVid_Type(OctetString):
    """Custom type loopdetectPortVid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoopdetectPortVid_Type.__name__ = "OctetString"
_LoopdetectPortVid_Object = MibTableColumn
loopdetectPortVid = _LoopdetectPortVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 4),
    _LoopdetectPortVid_Type()
)
loopdetectPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopdetectPortVid.setStatus("current")


class _LoopdetectPortFlag_Type(Integer32):
    """Custom type loopdetectPortFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LoopdetectPortFlag_Type.__name__ = "Integer32"
_LoopdetectPortFlag_Object = MibTableColumn
loopdetectPortFlag = _LoopdetectPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 5),
    _LoopdetectPortFlag_Type()
)
loopdetectPortFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectPortFlag.setStatus("current")


class _LoopdetectPortProtectFlag_Type(Integer32):
    """Custom type loopdetectPortProtectFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LoopdetectPortProtectFlag_Type.__name__ = "Integer32"
_LoopdetectPortProtectFlag_Object = MibTableColumn
loopdetectPortProtectFlag = _LoopdetectPortProtectFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 6),
    _LoopdetectPortProtectFlag_Type()
)
loopdetectPortProtectFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopdetectPortProtectFlag.setStatus("current")
_LoopdetectPortReopenTime_Type = Integer32
_LoopdetectPortReopenTime_Object = MibTableColumn
loopdetectPortReopenTime = _LoopdetectPortReopenTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 7),
    _LoopdetectPortReopenTime_Type()
)
loopdetectPortReopenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectPortReopenTime.setStatus("current")


class _LoopdetectVlan_Type(Integer32):
    """Custom type loopdetectVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_LoopdetectVlan_Type.__name__ = "Integer32"
_LoopdetectVlan_Object = MibTableColumn
loopdetectVlan = _LoopdetectVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 25, 2, 1, 8),
    _LoopdetectVlan_Type()
)
loopdetectVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectVlan.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Vct-Loopdetect-59-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10switch": zxr10switch,
       "switch59vct": switch59vct,
       "vctTable": vctTable,
       "vctEntry": vctEntry,
       "vctIfindex": vctIfindex,
       "vctSetIfindex": vctSetIfindex,
       "cableStatus": cableStatus,
       "doubleCableStatus1-2": doubleCableStatus1_2,
       "doubleCableStatus3-6": doubleCableStatus3_6,
       "doubleCableStatus4-5": doubleCableStatus4_5,
       "doubleCableStatus7-8": doubleCableStatus7_8,
       "doubleCableLength1-2": doubleCableLength1_2,
       "doubleCableLength3-6": doubleCableLength3_6,
       "doubleCableLength4-5": doubleCableLength4_5,
       "doubleCableLength7-8": doubleCableLength7_8,
       "switch59loopdetect": switch59loopdetect,
       "loopdetectReopenTime": loopdetectReopenTime,
       "loopdetectTable": loopdetectTable,
       "loopdetectEntry": loopdetectEntry,
       "loopdetectPortIfindex": loopdetectPortIfindex,
       "loopdetectPortOperStatus": loopdetectPortOperStatus,
       "loopdetectPortControl": loopdetectPortControl,
       "loopdetectPortVid": loopdetectPortVid,
       "loopdetectPortFlag": loopdetectPortFlag,
       "loopdetectPortProtectFlag": loopdetectPortProtectFlag,
       "loopdetectPortReopenTime": loopdetectPortReopenTime,
       "loopdetectVlan": loopdetectVlan}
)
