# SNMP MIB module (OPTIX-SONET-PATH-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-PATH-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:31 2024
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

(optixProvisionSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionSonet")

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

optixsonetPathAttrib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class C2Value(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              18,
              19,
              20,
              21,
              22,
              24,
              27,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              65534)
        )
    )
    namedValues = NamedValues(
        *(("atm", 19),
          ("dqdb", 20),
          ("ds3", 4),
          ("ds4na", 18),
          ("eqpd", 1),
          ("fddi", 21),
          ("gfp", 27),
          ("hdlc-over-sonet", 22),
          ("invalid", 65534),
          ("laps", 24),
          ("lock-vt", 3),
          ("o-181", 254),
          ("pdi-1", 225),
          ("pdi-10", 234),
          ("pdi-11", 235),
          ("pdi-12", 236),
          ("pdi-13", 237),
          ("pdi-14", 238),
          ("pdi-15", 239),
          ("pdi-16", 240),
          ("pdi-17", 241),
          ("pdi-18", 242),
          ("pdi-19", 243),
          ("pdi-2", 226),
          ("pdi-20", 244),
          ("pdi-21", 245),
          ("pdi-22", 246),
          ("pdi-23", 247),
          ("pdi-24", 248),
          ("pdi-26", 250),
          ("pdi-27", 251),
          ("pdi-28", 252),
          ("pdi-29", 249),
          ("pdi-3", 227),
          ("pdi-4", 228),
          ("pdi-5", 229),
          ("pdi-6", 230),
          ("pdi-7", 231),
          ("pdi-8", 232),
          ("pdi-9", 233),
          ("uneq", 253),
          ("vt-sts1", 2))
    )



class LpbkType(Integer32, TextualConvention):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("crs", 3),
          ("ds1feac", 4),
          ("ds3feac", 5),
          ("fac2ni", 6),
          ("facility", 2),
          ("noloop", 255),
          ("terminal", 1))
    )



# MIB Managed Objects in the order of their OIDs

_OptixsonetStsPathTable_Object = MibTable
optixsonetStsPathTable = _OptixsonetStsPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1)
)
if mibBuilder.loadTexts:
    optixsonetStsPathTable.setStatus("current")
_OptixsonetStsPathEntry_Object = MibTableRow
optixsonetStsPathEntry = _OptixsonetStsPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1)
)
optixsonetStsPathEntry.setIndexNames(
    (0, "OPTIX-SONET-PATH-MIB-V2", "stsPathLevel"),
    (0, "OPTIX-SONET-PATH-MIB-V2", "stsPathBid"),
    (0, "OPTIX-SONET-PATH-MIB-V2", "stsPathPid"),
    (0, "OPTIX-SONET-PATH-MIB-V2", "stsPathStsId"),
)
if mibBuilder.loadTexts:
    optixsonetStsPathEntry.setStatus("current")


class _StsPathLevel_Type(Integer32):
    """Custom type stsPathLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("levelSTS1", 9),
          ("levelSTS12c", 13),
          ("levelSTS15c", 14),
          ("levelSTS192c", 17),
          ("levelSTS24c", 15),
          ("levelSTS3c", 10),
          ("levelSTS48c", 16),
          ("levelSTS6c", 11),
          ("levelSTS9c", 12))
    )


_StsPathLevel_Type.__name__ = "Integer32"
_StsPathLevel_Object = MibTableColumn
stsPathLevel = _StsPathLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 1),
    _StsPathLevel_Type()
)
stsPathLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathLevel.setStatus("current")
_StsPathBid_Type = Gauge32
_StsPathBid_Object = MibTableColumn
stsPathBid = _StsPathBid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 2),
    _StsPathBid_Type()
)
stsPathBid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathBid.setStatus("current")
_StsPathPid_Type = Gauge32
_StsPathPid_Object = MibTableColumn
stsPathPid = _StsPathPid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 3),
    _StsPathPid_Type()
)
stsPathPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathPid.setStatus("current")
_StsPathStsId_Type = Gauge32
_StsPathStsId_Object = MibTableColumn
stsPathStsId = _StsPathStsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 4),
    _StsPathStsId_Type()
)
stsPathStsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathStsId.setStatus("current")


class _StsPathRevertiveMode_Type(Integer32):
    """Custom type stsPathRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("null", 254),
          ("yes", 1))
    )


_StsPathRevertiveMode_Type.__name__ = "Integer32"
_StsPathRevertiveMode_Object = MibTableColumn
stsPathRevertiveMode = _StsPathRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 5),
    _StsPathRevertiveMode_Type()
)
stsPathRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathRevertiveMode.setStatus("current")
_StsPathRevertiveTime_Type = Gauge32
_StsPathRevertiveTime_Object = MibTableColumn
stsPathRevertiveTime = _StsPathRevertiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 6),
    _StsPathRevertiveTime_Type()
)
stsPathRevertiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathRevertiveTime.setStatus("current")


class _StsPathSwitchConditon_Type(Integer32):
    """Custom type stsPathSwitchConditon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("null", 255),
          ("yes", 2))
    )


_StsPathSwitchConditon_Type.__name__ = "Integer32"
_StsPathSwitchConditon_Object = MibTableColumn
stsPathSwitchConditon = _StsPathSwitchConditon_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 7),
    _StsPathSwitchConditon_Type()
)
stsPathSwitchConditon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathSwitchConditon.setStatus("current")
_StsPathDelayTime_Type = Gauge32
_StsPathDelayTime_Object = MibTableColumn
stsPathDelayTime = _StsPathDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 8),
    _StsPathDelayTime_Type()
)
stsPathDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathDelayTime.setStatus("current")


class _StsPathSFBER_Type(Integer32):
    """Custom type stsPathSFBER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sf1E-3", 3),
          ("sf1E-4", 4),
          ("sf1E-5", 5))
    )


_StsPathSFBER_Type.__name__ = "Integer32"
_StsPathSFBER_Object = MibTableColumn
stsPathSFBER = _StsPathSFBER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 9),
    _StsPathSFBER_Type()
)
stsPathSFBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathSFBER.setStatus("current")


class _StsPathSDBER_Type(Integer32):
    """Custom type stsPathSDBER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("sd1E-5", 5),
          ("sd1E-6", 6),
          ("sd1E-7", 7),
          ("sd1E-8", 8),
          ("sd1E-9", 9))
    )


_StsPathSDBER_Type.__name__ = "Integer32"
_StsPathSDBER_Object = MibTableColumn
stsPathSDBER = _StsPathSDBER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 10),
    _StsPathSDBER_Type()
)
stsPathSDBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathSDBER.setStatus("current")


class _StsPathJ1TRCMODE_Type(Integer32):
    """Custom type stsPathJ1TRCMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("invalid", 254),
          ("manual", 1),
          ("off", 3))
    )


_StsPathJ1TRCMODE_Type.__name__ = "Integer32"
_StsPathJ1TRCMODE_Object = MibTableColumn
stsPathJ1TRCMODE = _StsPathJ1TRCMODE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 11),
    _StsPathJ1TRCMODE_Type()
)
stsPathJ1TRCMODE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathJ1TRCMODE.setStatus("current")


class _StsPathTRCJ1_Type(OctetString):
    """Custom type stsPathTRCJ1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_StsPathTRCJ1_Type.__name__ = "OctetString"
_StsPathTRCJ1_Object = MibTableColumn
stsPathTRCJ1 = _StsPathTRCJ1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 12),
    _StsPathTRCJ1_Type()
)
stsPathTRCJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathTRCJ1.setStatus("current")


class _StsPathEXPTRCJ1_Type(OctetString):
    """Custom type stsPathEXPTRCJ1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_StsPathEXPTRCJ1_Type.__name__ = "OctetString"
_StsPathEXPTRCJ1_Object = MibTableColumn
stsPathEXPTRCJ1 = _StsPathEXPTRCJ1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 13),
    _StsPathEXPTRCJ1_Type()
)
stsPathEXPTRCJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathEXPTRCJ1.setStatus("current")


class _StsPathINCTRCJ1_Type(OctetString):
    """Custom type stsPathINCTRCJ1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_StsPathINCTRCJ1_Type.__name__ = "OctetString"
_StsPathINCTRCJ1_Object = MibTableColumn
stsPathINCTRCJ1 = _StsPathINCTRCJ1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 14),
    _StsPathINCTRCJ1_Type()
)
stsPathINCTRCJ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathINCTRCJ1.setStatus("current")
_StsPathTRCC2_Type = C2Value
_StsPathTRCC2_Object = MibTableColumn
stsPathTRCC2 = _StsPathTRCC2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 15),
    _StsPathTRCC2_Type()
)
stsPathTRCC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathTRCC2.setStatus("current")
_StsPathEXPTRCC2_Type = C2Value
_StsPathEXPTRCC2_Object = MibTableColumn
stsPathEXPTRCC2 = _StsPathEXPTRCC2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 16),
    _StsPathEXPTRCC2_Type()
)
stsPathEXPTRCC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathEXPTRCC2.setStatus("current")
_StsPathINCTRCC2_Type = C2Value
_StsPathINCTRCC2_Object = MibTableColumn
stsPathINCTRCC2 = _StsPathINCTRCC2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 17),
    _StsPathINCTRCC2_Type()
)
stsPathINCTRCC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathINCTRCC2.setStatus("current")


class _StsPathSQL_Type(Integer32):
    """Custom type stsPathSQL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 254),
          ("no", 2),
          ("yes", 1))
    )


_StsPathSQL_Type.__name__ = "Integer32"
_StsPathSQL_Object = MibTableColumn
stsPathSQL = _StsPathSQL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 18),
    _StsPathSQL_Type()
)
stsPathSQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathSQL.setStatus("current")


class _StsPathSwitchState_Type(Integer32):
    """Custom type stsPathSwitchState based on Integer32"""
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
              253,
              254)
        )
    )
    namedValues = NamedValues(
        *(("autosw", 2),
          ("clear", 8),
          ("frcPtoW", 5),
          ("frcWtoP", 6),
          ("idle", 253),
          ("invalid", 254),
          ("lockout", 7),
          ("manPtoW", 3),
          ("manWtoP", 4),
          ("wtr", 1))
    )


_StsPathSwitchState_Type.__name__ = "Integer32"
_StsPathSwitchState_Object = MibTableColumn
stsPathSwitchState = _StsPathSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 19),
    _StsPathSwitchState_Type()
)
stsPathSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsPathSwitchState.setStatus("current")


class _StsPathPST_Type(OctetString):
    """Custom type stsPathPST based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StsPathPST_Type.__name__ = "OctetString"
_StsPathPST_Object = MibTableColumn
stsPathPST = _StsPathPST_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 20),
    _StsPathPST_Type()
)
stsPathPST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathPST.setStatus("current")


class _StsPathSST_Type(OctetString):
    """Custom type stsPathSST based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StsPathSST_Type.__name__ = "OctetString"
_StsPathSST_Object = MibTableColumn
stsPathSST = _StsPathSST_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 21),
    _StsPathSST_Type()
)
stsPathSST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathSST.setStatus("current")
_StsPathLoopbackStatus_Type = LpbkType
_StsPathLoopbackStatus_Object = MibTableColumn
stsPathLoopbackStatus = _StsPathLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 1, 1, 22),
    _StsPathLoopbackStatus_Type()
)
stsPathLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsPathLoopbackStatus.setStatus("current")
_OptixsonetPathAttribConformance_ObjectIdentity = ObjectIdentity
optixsonetPathAttribConformance = _OptixsonetPathAttribConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 2)
)
_OptixsonetPathAttribGroups_ObjectIdentity = ObjectIdentity
optixsonetPathAttribGroups = _OptixsonetPathAttribGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 2, 1)
)
_OptixsonetPathAttribCompliances_ObjectIdentity = ObjectIdentity
optixsonetPathAttribCompliances = _OptixsonetPathAttribCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 2, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 2, 1, 1)
)
currentObjectGroup.setObjects(
      *(("OPTIX-SONET-PATH-MIB-V2", "stsPathLevel"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathBid"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathPid"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathStsId"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathRevertiveMode"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathRevertiveTime"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathSwitchConditon"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathDelayTime"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathSFBER"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathSDBER"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathJ1TRCMODE"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathTRCJ1"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathEXPTRCJ1"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathINCTRCJ1"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathTRCC2"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathEXPTRCC2"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathINCTRCC2"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathSQL"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathSwitchState"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathPST"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathSST"),
        ("OPTIX-SONET-PATH-MIB-V2", "stsPathLoopbackStatus"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-PATH-MIB-V2",
    **{"C2Value": C2Value,
       "LpbkType": LpbkType,
       "optixsonetPathAttrib": optixsonetPathAttrib,
       "optixsonetStsPathTable": optixsonetStsPathTable,
       "optixsonetStsPathEntry": optixsonetStsPathEntry,
       "stsPathLevel": stsPathLevel,
       "stsPathBid": stsPathBid,
       "stsPathPid": stsPathPid,
       "stsPathStsId": stsPathStsId,
       "stsPathRevertiveMode": stsPathRevertiveMode,
       "stsPathRevertiveTime": stsPathRevertiveTime,
       "stsPathSwitchConditon": stsPathSwitchConditon,
       "stsPathDelayTime": stsPathDelayTime,
       "stsPathSFBER": stsPathSFBER,
       "stsPathSDBER": stsPathSDBER,
       "stsPathJ1TRCMODE": stsPathJ1TRCMODE,
       "stsPathTRCJ1": stsPathTRCJ1,
       "stsPathEXPTRCJ1": stsPathEXPTRCJ1,
       "stsPathINCTRCJ1": stsPathINCTRCJ1,
       "stsPathTRCC2": stsPathTRCC2,
       "stsPathEXPTRCC2": stsPathEXPTRCC2,
       "stsPathINCTRCC2": stsPathINCTRCC2,
       "stsPathSQL": stsPathSQL,
       "stsPathSwitchState": stsPathSwitchState,
       "stsPathPST": stsPathPST,
       "stsPathSST": stsPathSST,
       "stsPathLoopbackStatus": stsPathLoopbackStatus,
       "optixsonetPathAttribConformance": optixsonetPathAttribConformance,
       "optixsonetPathAttribGroups": optixsonetPathAttribGroups,
       "currentObjectGroup": currentObjectGroup,
       "optixsonetPathAttribCompliances": optixsonetPathAttribCompliances,
       "basicCompliance": basicCompliance}
)
