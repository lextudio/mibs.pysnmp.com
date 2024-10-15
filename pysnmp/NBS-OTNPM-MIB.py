# SNMP MIB module (NBS-OTNPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-OTNPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:56 2024
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

(InterfaceIndex,
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias")

(Unsigned64,
 WritableU64,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "Unsigned64",
    "WritableU64",
    "nbs")

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

nbsOtnpmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NbsOtnAlarmId(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("aBwdSD", 51),
          ("aBwdSF", 50),
          ("aCSF", 53),
          ("aFwdSD", 49),
          ("aFwdSF", 48),
          ("aLOF", 2),
          ("aLOM", 4),
          ("aLOS", 1),
          ("aOOF", 3),
          ("aOOM", 5),
          ("aOduAIS", 13),
          ("aOduLCK", 15),
          ("aOduOCI", 14),
          ("aOtuAIS", 8),
          ("aPTM", 52),
          ("aPathBDI", 16),
          ("aPathTIM", 17),
          ("aRxLOL", 6),
          ("aSectBDI", 9),
          ("aSectBIAE", 10),
          ("aSectIAE", 11),
          ("aSectTIM", 12),
          ("aTcm1BDI", 18),
          ("aTcm1BIAE", 24),
          ("aTcm1IAE", 30),
          ("aTcm1LTC", 36),
          ("aTcm1TIM", 42),
          ("aTcm2BDI", 19),
          ("aTcm2BIAE", 25),
          ("aTcm2IAE", 31),
          ("aTcm2LTC", 37),
          ("aTcm2TIM", 43),
          ("aTcm3BDI", 20),
          ("aTcm3BIAE", 26),
          ("aTcm3IAE", 32),
          ("aTcm3LTC", 38),
          ("aTcm3TIM", 44),
          ("aTcm4BDI", 21),
          ("aTcm4BIAE", 27),
          ("aTcm4IAE", 33),
          ("aTcm4LTC", 39),
          ("aTcm4TIM", 45),
          ("aTcm5BDI", 22),
          ("aTcm5BIAE", 28),
          ("aTcm5IAE", 34),
          ("aTcm5LTC", 40),
          ("aTcm5TIM", 46),
          ("aTcm6BDI", 23),
          ("aTcm6BIAE", 29),
          ("aTcm6IAE", 35),
          ("aTcm6LTC", 41),
          ("aTcm6TIM", 47),
          ("aTxLOL", 7))
    )



class NbsOtnAlarmMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_NbsOtnpmThresholdsGrp_ObjectIdentity = ObjectIdentity
nbsOtnpmThresholdsGrp = _NbsOtnpmThresholdsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 1)
)
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsGrp.setStatus("current")
_NbsOtnpmThresholdsTable_Object = MibTable
nbsOtnpmThresholdsTable = _NbsOtnpmThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1)
)
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsTable.setStatus("current")
_NbsOtnpmThresholdsEntry_Object = MibTableRow
nbsOtnpmThresholdsEntry = _NbsOtnpmThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1)
)
nbsOtnpmThresholdsEntry.setIndexNames(
    (0, "NBS-OTNPM-MIB", "nbsOtnpmThresholdsIfIndex"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmThresholdsInterval"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmThresholdsScope"),
)
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsEntry.setStatus("current")
_NbsOtnpmThresholdsIfIndex_Type = InterfaceIndex
_NbsOtnpmThresholdsIfIndex_Object = MibTableColumn
nbsOtnpmThresholdsIfIndex = _NbsOtnpmThresholdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 1),
    _NbsOtnpmThresholdsIfIndex_Type()
)
nbsOtnpmThresholdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsIfIndex.setStatus("current")


class _NbsOtnpmThresholdsInterval_Type(Integer32):
    """Custom type nbsOtnpmThresholdsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsOtnpmThresholdsInterval_Type.__name__ = "Integer32"
_NbsOtnpmThresholdsInterval_Object = MibTableColumn
nbsOtnpmThresholdsInterval = _NbsOtnpmThresholdsInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 2),
    _NbsOtnpmThresholdsInterval_Type()
)
nbsOtnpmThresholdsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsInterval.setStatus("current")


class _NbsOtnpmThresholdsScope_Type(Integer32):
    """Custom type nbsOtnpmThresholdsScope based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("path", 8),
          ("section", 7),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6))
    )


_NbsOtnpmThresholdsScope_Type.__name__ = "Integer32"
_NbsOtnpmThresholdsScope_Object = MibTableColumn
nbsOtnpmThresholdsScope = _NbsOtnpmThresholdsScope_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 3),
    _NbsOtnpmThresholdsScope_Type()
)
nbsOtnpmThresholdsScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsScope.setStatus("current")
_NbsOtnpmThresholdsEs_Type = Unsigned32
_NbsOtnpmThresholdsEs_Object = MibTableColumn
nbsOtnpmThresholdsEs = _NbsOtnpmThresholdsEs_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 10),
    _NbsOtnpmThresholdsEs_Type()
)
nbsOtnpmThresholdsEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsEs.setStatus("current")


class _NbsOtnpmThresholdsEsrSig_Type(Integer32):
    """Custom type nbsOtnpmThresholdsEsrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmThresholdsEsrSig_Object = MibTableColumn
nbsOtnpmThresholdsEsrSig = _NbsOtnpmThresholdsEsrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 11),
    _NbsOtnpmThresholdsEsrSig_Type()
)
nbsOtnpmThresholdsEsrSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsEsrSig.setStatus("current")


class _NbsOtnpmThresholdsEsrExp_Type(Integer32):
    """Custom type nbsOtnpmThresholdsEsrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmThresholdsEsrExp_Type.__name__ = "Integer32"
_NbsOtnpmThresholdsEsrExp_Object = MibTableColumn
nbsOtnpmThresholdsEsrExp = _NbsOtnpmThresholdsEsrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 12),
    _NbsOtnpmThresholdsEsrExp_Type()
)
nbsOtnpmThresholdsEsrExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsEsrExp.setStatus("current")
_NbsOtnpmThresholdsSes_Type = Unsigned32
_NbsOtnpmThresholdsSes_Object = MibTableColumn
nbsOtnpmThresholdsSes = _NbsOtnpmThresholdsSes_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 13),
    _NbsOtnpmThresholdsSes_Type()
)
nbsOtnpmThresholdsSes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsSes.setStatus("current")


class _NbsOtnpmThresholdsSesrSig_Type(Integer32):
    """Custom type nbsOtnpmThresholdsSesrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmThresholdsSesrSig_Object = MibTableColumn
nbsOtnpmThresholdsSesrSig = _NbsOtnpmThresholdsSesrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 14),
    _NbsOtnpmThresholdsSesrSig_Type()
)
nbsOtnpmThresholdsSesrSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsSesrSig.setStatus("current")


class _NbsOtnpmThresholdsSesrExp_Type(Integer32):
    """Custom type nbsOtnpmThresholdsSesrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmThresholdsSesrExp_Type.__name__ = "Integer32"
_NbsOtnpmThresholdsSesrExp_Object = MibTableColumn
nbsOtnpmThresholdsSesrExp = _NbsOtnpmThresholdsSesrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 15),
    _NbsOtnpmThresholdsSesrExp_Type()
)
nbsOtnpmThresholdsSesrExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsSesrExp.setStatus("current")
_NbsOtnpmThresholdsBbe_Type = WritableU64
_NbsOtnpmThresholdsBbe_Object = MibTableColumn
nbsOtnpmThresholdsBbe = _NbsOtnpmThresholdsBbe_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 16),
    _NbsOtnpmThresholdsBbe_Type()
)
nbsOtnpmThresholdsBbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsBbe.setStatus("current")


class _NbsOtnpmThresholdsBberSig_Type(Integer32):
    """Custom type nbsOtnpmThresholdsBberSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmThresholdsBberSig_Object = MibTableColumn
nbsOtnpmThresholdsBberSig = _NbsOtnpmThresholdsBberSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 17),
    _NbsOtnpmThresholdsBberSig_Type()
)
nbsOtnpmThresholdsBberSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsBberSig.setStatus("current")


class _NbsOtnpmThresholdsBberExp_Type(Integer32):
    """Custom type nbsOtnpmThresholdsBberExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmThresholdsBberExp_Type.__name__ = "Integer32"
_NbsOtnpmThresholdsBberExp_Object = MibTableColumn
nbsOtnpmThresholdsBberExp = _NbsOtnpmThresholdsBberExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 18),
    _NbsOtnpmThresholdsBberExp_Type()
)
nbsOtnpmThresholdsBberExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsBberExp.setStatus("current")
_NbsOtnpmThresholdsUas_Type = Unsigned32
_NbsOtnpmThresholdsUas_Object = MibTableColumn
nbsOtnpmThresholdsUas = _NbsOtnpmThresholdsUas_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 19),
    _NbsOtnpmThresholdsUas_Type()
)
nbsOtnpmThresholdsUas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsUas.setStatus("current")
_NbsOtnpmThresholdsFc_Type = WritableU64
_NbsOtnpmThresholdsFc_Object = MibTableColumn
nbsOtnpmThresholdsFc = _NbsOtnpmThresholdsFc_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 1, 1, 1, 20),
    _NbsOtnpmThresholdsFc_Type()
)
nbsOtnpmThresholdsFc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnpmThresholdsFc.setStatus("current")
_NbsOtnpmCurrentGrp_ObjectIdentity = ObjectIdentity
nbsOtnpmCurrentGrp = _NbsOtnpmCurrentGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 2)
)
if mibBuilder.loadTexts:
    nbsOtnpmCurrentGrp.setStatus("current")
_NbsOtnpmCurrentTable_Object = MibTable
nbsOtnpmCurrentTable = _NbsOtnpmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3)
)
if mibBuilder.loadTexts:
    nbsOtnpmCurrentTable.setStatus("current")
_NbsOtnpmCurrentEntry_Object = MibTableRow
nbsOtnpmCurrentEntry = _NbsOtnpmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1)
)
nbsOtnpmCurrentEntry.setIndexNames(
    (0, "NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
)
if mibBuilder.loadTexts:
    nbsOtnpmCurrentEntry.setStatus("current")
_NbsOtnpmCurrentIfIndex_Type = InterfaceIndex
_NbsOtnpmCurrentIfIndex_Object = MibTableColumn
nbsOtnpmCurrentIfIndex = _NbsOtnpmCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 1),
    _NbsOtnpmCurrentIfIndex_Type()
)
nbsOtnpmCurrentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentIfIndex.setStatus("current")


class _NbsOtnpmCurrentInterval_Type(Integer32):
    """Custom type nbsOtnpmCurrentInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsOtnpmCurrentInterval_Type.__name__ = "Integer32"
_NbsOtnpmCurrentInterval_Object = MibTableColumn
nbsOtnpmCurrentInterval = _NbsOtnpmCurrentInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 2),
    _NbsOtnpmCurrentInterval_Type()
)
nbsOtnpmCurrentInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentInterval.setStatus("current")


class _NbsOtnpmCurrentScope_Type(Integer32):
    """Custom type nbsOtnpmCurrentScope based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("path", 8),
          ("section", 7),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6))
    )


_NbsOtnpmCurrentScope_Type.__name__ = "Integer32"
_NbsOtnpmCurrentScope_Object = MibTableColumn
nbsOtnpmCurrentScope = _NbsOtnpmCurrentScope_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 3),
    _NbsOtnpmCurrentScope_Type()
)
nbsOtnpmCurrentScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentScope.setStatus("current")
_NbsOtnpmCurrentDate_Type = Integer32
_NbsOtnpmCurrentDate_Object = MibTableColumn
nbsOtnpmCurrentDate = _NbsOtnpmCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 5),
    _NbsOtnpmCurrentDate_Type()
)
nbsOtnpmCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentDate.setStatus("current")
_NbsOtnpmCurrentTime_Type = Integer32
_NbsOtnpmCurrentTime_Object = MibTableColumn
nbsOtnpmCurrentTime = _NbsOtnpmCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 6),
    _NbsOtnpmCurrentTime_Type()
)
nbsOtnpmCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentTime.setStatus("current")
_NbsOtnpmCurrentEs_Type = Unsigned32
_NbsOtnpmCurrentEs_Object = MibTableColumn
nbsOtnpmCurrentEs = _NbsOtnpmCurrentEs_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 10),
    _NbsOtnpmCurrentEs_Type()
)
nbsOtnpmCurrentEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentEs.setStatus("current")


class _NbsOtnpmCurrentEsrSig_Type(Integer32):
    """Custom type nbsOtnpmCurrentEsrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmCurrentEsrSig_Object = MibTableColumn
nbsOtnpmCurrentEsrSig = _NbsOtnpmCurrentEsrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 11),
    _NbsOtnpmCurrentEsrSig_Type()
)
nbsOtnpmCurrentEsrSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentEsrSig.setStatus("current")


class _NbsOtnpmCurrentEsrExp_Type(Integer32):
    """Custom type nbsOtnpmCurrentEsrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmCurrentEsrExp_Type.__name__ = "Integer32"
_NbsOtnpmCurrentEsrExp_Object = MibTableColumn
nbsOtnpmCurrentEsrExp = _NbsOtnpmCurrentEsrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 12),
    _NbsOtnpmCurrentEsrExp_Type()
)
nbsOtnpmCurrentEsrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentEsrExp.setStatus("current")
_NbsOtnpmCurrentSes_Type = Unsigned32
_NbsOtnpmCurrentSes_Object = MibTableColumn
nbsOtnpmCurrentSes = _NbsOtnpmCurrentSes_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 13),
    _NbsOtnpmCurrentSes_Type()
)
nbsOtnpmCurrentSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentSes.setStatus("current")


class _NbsOtnpmCurrentSesrSig_Type(Integer32):
    """Custom type nbsOtnpmCurrentSesrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmCurrentSesrSig_Object = MibTableColumn
nbsOtnpmCurrentSesrSig = _NbsOtnpmCurrentSesrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 14),
    _NbsOtnpmCurrentSesrSig_Type()
)
nbsOtnpmCurrentSesrSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentSesrSig.setStatus("current")


class _NbsOtnpmCurrentSesrExp_Type(Integer32):
    """Custom type nbsOtnpmCurrentSesrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmCurrentSesrExp_Type.__name__ = "Integer32"
_NbsOtnpmCurrentSesrExp_Object = MibTableColumn
nbsOtnpmCurrentSesrExp = _NbsOtnpmCurrentSesrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 15),
    _NbsOtnpmCurrentSesrExp_Type()
)
nbsOtnpmCurrentSesrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentSesrExp.setStatus("current")
_NbsOtnpmCurrentBbe_Type = Unsigned64
_NbsOtnpmCurrentBbe_Object = MibTableColumn
nbsOtnpmCurrentBbe = _NbsOtnpmCurrentBbe_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 16),
    _NbsOtnpmCurrentBbe_Type()
)
nbsOtnpmCurrentBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentBbe.setStatus("current")


class _NbsOtnpmCurrentBberSig_Type(Integer32):
    """Custom type nbsOtnpmCurrentBberSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmCurrentBberSig_Object = MibTableColumn
nbsOtnpmCurrentBberSig = _NbsOtnpmCurrentBberSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 17),
    _NbsOtnpmCurrentBberSig_Type()
)
nbsOtnpmCurrentBberSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentBberSig.setStatus("current")


class _NbsOtnpmCurrentBberExp_Type(Integer32):
    """Custom type nbsOtnpmCurrentBberExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmCurrentBberExp_Type.__name__ = "Integer32"
_NbsOtnpmCurrentBberExp_Object = MibTableColumn
nbsOtnpmCurrentBberExp = _NbsOtnpmCurrentBberExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 18),
    _NbsOtnpmCurrentBberExp_Type()
)
nbsOtnpmCurrentBberExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentBberExp.setStatus("current")
_NbsOtnpmCurrentUas_Type = Unsigned32
_NbsOtnpmCurrentUas_Object = MibTableColumn
nbsOtnpmCurrentUas = _NbsOtnpmCurrentUas_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 19),
    _NbsOtnpmCurrentUas_Type()
)
nbsOtnpmCurrentUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentUas.setStatus("current")
_NbsOtnpmCurrentFc_Type = Unsigned64
_NbsOtnpmCurrentFc_Object = MibTableColumn
nbsOtnpmCurrentFc = _NbsOtnpmCurrentFc_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 20),
    _NbsOtnpmCurrentFc_Type()
)
nbsOtnpmCurrentFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentFc.setStatus("current")
_NbsOtnpmCurrentAlarmsSupported_Type = NbsOtnAlarmMask
_NbsOtnpmCurrentAlarmsSupported_Object = MibTableColumn
nbsOtnpmCurrentAlarmsSupported = _NbsOtnpmCurrentAlarmsSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 100),
    _NbsOtnpmCurrentAlarmsSupported_Type()
)
nbsOtnpmCurrentAlarmsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentAlarmsSupported.setStatus("current")
_NbsOtnpmCurrentAlarmsRaised_Type = NbsOtnAlarmMask
_NbsOtnpmCurrentAlarmsRaised_Object = MibTableColumn
nbsOtnpmCurrentAlarmsRaised = _NbsOtnpmCurrentAlarmsRaised_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 101),
    _NbsOtnpmCurrentAlarmsRaised_Type()
)
nbsOtnpmCurrentAlarmsRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentAlarmsRaised.setStatus("current")
_NbsOtnpmCurrentAlarmsChanged_Type = NbsOtnAlarmMask
_NbsOtnpmCurrentAlarmsChanged_Object = MibTableColumn
nbsOtnpmCurrentAlarmsChanged = _NbsOtnpmCurrentAlarmsChanged_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 2, 3, 1, 102),
    _NbsOtnpmCurrentAlarmsChanged_Type()
)
nbsOtnpmCurrentAlarmsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmCurrentAlarmsChanged.setStatus("current")
_NbsOtnpmHistoricGrp_ObjectIdentity = ObjectIdentity
nbsOtnpmHistoricGrp = _NbsOtnpmHistoricGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 3)
)
if mibBuilder.loadTexts:
    nbsOtnpmHistoricGrp.setStatus("current")
_NbsOtnpmHistoricTable_Object = MibTable
nbsOtnpmHistoricTable = _NbsOtnpmHistoricTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3)
)
if mibBuilder.loadTexts:
    nbsOtnpmHistoricTable.setStatus("current")
_NbsOtnpmHistoricEntry_Object = MibTableRow
nbsOtnpmHistoricEntry = _NbsOtnpmHistoricEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1)
)
nbsOtnpmHistoricEntry.setIndexNames(
    (0, "NBS-OTNPM-MIB", "nbsOtnpmHistoricIfIndex"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmHistoricInterval"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmHistoricScope"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmHistoricSample"),
)
if mibBuilder.loadTexts:
    nbsOtnpmHistoricEntry.setStatus("current")
_NbsOtnpmHistoricIfIndex_Type = InterfaceIndex
_NbsOtnpmHistoricIfIndex_Object = MibTableColumn
nbsOtnpmHistoricIfIndex = _NbsOtnpmHistoricIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 1),
    _NbsOtnpmHistoricIfIndex_Type()
)
nbsOtnpmHistoricIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricIfIndex.setStatus("current")


class _NbsOtnpmHistoricInterval_Type(Integer32):
    """Custom type nbsOtnpmHistoricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsOtnpmHistoricInterval_Type.__name__ = "Integer32"
_NbsOtnpmHistoricInterval_Object = MibTableColumn
nbsOtnpmHistoricInterval = _NbsOtnpmHistoricInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 2),
    _NbsOtnpmHistoricInterval_Type()
)
nbsOtnpmHistoricInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricInterval.setStatus("current")


class _NbsOtnpmHistoricScope_Type(Integer32):
    """Custom type nbsOtnpmHistoricScope based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("path", 8),
          ("section", 7),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6))
    )


_NbsOtnpmHistoricScope_Type.__name__ = "Integer32"
_NbsOtnpmHistoricScope_Object = MibTableColumn
nbsOtnpmHistoricScope = _NbsOtnpmHistoricScope_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 3),
    _NbsOtnpmHistoricScope_Type()
)
nbsOtnpmHistoricScope.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricScope.setStatus("current")
_NbsOtnpmHistoricSample_Type = Integer32
_NbsOtnpmHistoricSample_Object = MibTableColumn
nbsOtnpmHistoricSample = _NbsOtnpmHistoricSample_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 4),
    _NbsOtnpmHistoricSample_Type()
)
nbsOtnpmHistoricSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricSample.setStatus("current")
_NbsOtnpmHistoricDate_Type = Integer32
_NbsOtnpmHistoricDate_Object = MibTableColumn
nbsOtnpmHistoricDate = _NbsOtnpmHistoricDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 5),
    _NbsOtnpmHistoricDate_Type()
)
nbsOtnpmHistoricDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricDate.setStatus("current")
_NbsOtnpmHistoricTime_Type = Integer32
_NbsOtnpmHistoricTime_Object = MibTableColumn
nbsOtnpmHistoricTime = _NbsOtnpmHistoricTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 6),
    _NbsOtnpmHistoricTime_Type()
)
nbsOtnpmHistoricTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricTime.setStatus("current")
_NbsOtnpmHistoricEs_Type = Unsigned32
_NbsOtnpmHistoricEs_Object = MibTableColumn
nbsOtnpmHistoricEs = _NbsOtnpmHistoricEs_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 10),
    _NbsOtnpmHistoricEs_Type()
)
nbsOtnpmHistoricEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricEs.setStatus("current")


class _NbsOtnpmHistoricEsrSig_Type(Integer32):
    """Custom type nbsOtnpmHistoricEsrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmHistoricEsrSig_Object = MibTableColumn
nbsOtnpmHistoricEsrSig = _NbsOtnpmHistoricEsrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 11),
    _NbsOtnpmHistoricEsrSig_Type()
)
nbsOtnpmHistoricEsrSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricEsrSig.setStatus("current")


class _NbsOtnpmHistoricEsrExp_Type(Integer32):
    """Custom type nbsOtnpmHistoricEsrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmHistoricEsrExp_Type.__name__ = "Integer32"
_NbsOtnpmHistoricEsrExp_Object = MibTableColumn
nbsOtnpmHistoricEsrExp = _NbsOtnpmHistoricEsrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 12),
    _NbsOtnpmHistoricEsrExp_Type()
)
nbsOtnpmHistoricEsrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricEsrExp.setStatus("current")
_NbsOtnpmHistoricSes_Type = Unsigned32
_NbsOtnpmHistoricSes_Object = MibTableColumn
nbsOtnpmHistoricSes = _NbsOtnpmHistoricSes_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 13),
    _NbsOtnpmHistoricSes_Type()
)
nbsOtnpmHistoricSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricSes.setStatus("current")


class _NbsOtnpmHistoricSesrSig_Type(Integer32):
    """Custom type nbsOtnpmHistoricSesrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmHistoricSesrSig_Object = MibTableColumn
nbsOtnpmHistoricSesrSig = _NbsOtnpmHistoricSesrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 14),
    _NbsOtnpmHistoricSesrSig_Type()
)
nbsOtnpmHistoricSesrSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricSesrSig.setStatus("current")


class _NbsOtnpmHistoricSesrExp_Type(Integer32):
    """Custom type nbsOtnpmHistoricSesrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmHistoricSesrExp_Type.__name__ = "Integer32"
_NbsOtnpmHistoricSesrExp_Object = MibTableColumn
nbsOtnpmHistoricSesrExp = _NbsOtnpmHistoricSesrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 15),
    _NbsOtnpmHistoricSesrExp_Type()
)
nbsOtnpmHistoricSesrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricSesrExp.setStatus("current")
_NbsOtnpmHistoricBbe_Type = Unsigned64
_NbsOtnpmHistoricBbe_Object = MibTableColumn
nbsOtnpmHistoricBbe = _NbsOtnpmHistoricBbe_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 16),
    _NbsOtnpmHistoricBbe_Type()
)
nbsOtnpmHistoricBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricBbe.setStatus("current")


class _NbsOtnpmHistoricBberSig_Type(Integer32):
    """Custom type nbsOtnpmHistoricBberSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmHistoricBberSig_Object = MibTableColumn
nbsOtnpmHistoricBberSig = _NbsOtnpmHistoricBberSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 17),
    _NbsOtnpmHistoricBberSig_Type()
)
nbsOtnpmHistoricBberSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricBberSig.setStatus("current")


class _NbsOtnpmHistoricBberExp_Type(Integer32):
    """Custom type nbsOtnpmHistoricBberExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmHistoricBberExp_Type.__name__ = "Integer32"
_NbsOtnpmHistoricBberExp_Object = MibTableColumn
nbsOtnpmHistoricBberExp = _NbsOtnpmHistoricBberExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 18),
    _NbsOtnpmHistoricBberExp_Type()
)
nbsOtnpmHistoricBberExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricBberExp.setStatus("current")
_NbsOtnpmHistoricUas_Type = Unsigned32
_NbsOtnpmHistoricUas_Object = MibTableColumn
nbsOtnpmHistoricUas = _NbsOtnpmHistoricUas_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 19),
    _NbsOtnpmHistoricUas_Type()
)
nbsOtnpmHistoricUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricUas.setStatus("current")
_NbsOtnpmHistoricFc_Type = Unsigned64
_NbsOtnpmHistoricFc_Object = MibTableColumn
nbsOtnpmHistoricFc = _NbsOtnpmHistoricFc_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 20),
    _NbsOtnpmHistoricFc_Type()
)
nbsOtnpmHistoricFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricFc.setStatus("current")
_NbsOtnpmHistoricAlarmsSupported_Type = NbsOtnAlarmMask
_NbsOtnpmHistoricAlarmsSupported_Object = MibTableColumn
nbsOtnpmHistoricAlarmsSupported = _NbsOtnpmHistoricAlarmsSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 100),
    _NbsOtnpmHistoricAlarmsSupported_Type()
)
nbsOtnpmHistoricAlarmsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricAlarmsSupported.setStatus("current")
_NbsOtnpmHistoricAlarmsRaised_Type = NbsOtnAlarmMask
_NbsOtnpmHistoricAlarmsRaised_Object = MibTableColumn
nbsOtnpmHistoricAlarmsRaised = _NbsOtnpmHistoricAlarmsRaised_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 101),
    _NbsOtnpmHistoricAlarmsRaised_Type()
)
nbsOtnpmHistoricAlarmsRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricAlarmsRaised.setStatus("current")
_NbsOtnpmHistoricAlarmsChanged_Type = NbsOtnAlarmMask
_NbsOtnpmHistoricAlarmsChanged_Object = MibTableColumn
nbsOtnpmHistoricAlarmsChanged = _NbsOtnpmHistoricAlarmsChanged_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 3, 3, 1, 102),
    _NbsOtnpmHistoricAlarmsChanged_Type()
)
nbsOtnpmHistoricAlarmsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmHistoricAlarmsChanged.setStatus("current")
_NbsOtnpmRunningGrp_ObjectIdentity = ObjectIdentity
nbsOtnpmRunningGrp = _NbsOtnpmRunningGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 4)
)
if mibBuilder.loadTexts:
    nbsOtnpmRunningGrp.setStatus("current")
_NbsOtnpmRunningTable_Object = MibTable
nbsOtnpmRunningTable = _NbsOtnpmRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3)
)
if mibBuilder.loadTexts:
    nbsOtnpmRunningTable.setStatus("current")
_NbsOtnpmRunningEntry_Object = MibTableRow
nbsOtnpmRunningEntry = _NbsOtnpmRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1)
)
nbsOtnpmRunningEntry.setIndexNames(
    (0, "NBS-OTNPM-MIB", "nbsOtnpmRunningIfIndex"),
    (0, "NBS-OTNPM-MIB", "nbsOtnpmRunningScope"),
)
if mibBuilder.loadTexts:
    nbsOtnpmRunningEntry.setStatus("current")
_NbsOtnpmRunningIfIndex_Type = InterfaceIndex
_NbsOtnpmRunningIfIndex_Object = MibTableColumn
nbsOtnpmRunningIfIndex = _NbsOtnpmRunningIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 1),
    _NbsOtnpmRunningIfIndex_Type()
)
nbsOtnpmRunningIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningIfIndex.setStatus("current")


class _NbsOtnpmRunningScope_Type(Integer32):
    """Custom type nbsOtnpmRunningScope based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("path", 8),
          ("section", 7),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6))
    )


_NbsOtnpmRunningScope_Type.__name__ = "Integer32"
_NbsOtnpmRunningScope_Object = MibTableColumn
nbsOtnpmRunningScope = _NbsOtnpmRunningScope_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 3),
    _NbsOtnpmRunningScope_Type()
)
nbsOtnpmRunningScope.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOtnpmRunningScope.setStatus("current")
_NbsOtnpmRunningDate_Type = Integer32
_NbsOtnpmRunningDate_Object = MibTableColumn
nbsOtnpmRunningDate = _NbsOtnpmRunningDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 5),
    _NbsOtnpmRunningDate_Type()
)
nbsOtnpmRunningDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningDate.setStatus("current")
_NbsOtnpmRunningTime_Type = Integer32
_NbsOtnpmRunningTime_Object = MibTableColumn
nbsOtnpmRunningTime = _NbsOtnpmRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 6),
    _NbsOtnpmRunningTime_Type()
)
nbsOtnpmRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningTime.setStatus("current")
_NbsOtnpmRunningEs_Type = Counter32
_NbsOtnpmRunningEs_Object = MibTableColumn
nbsOtnpmRunningEs = _NbsOtnpmRunningEs_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 10),
    _NbsOtnpmRunningEs_Type()
)
nbsOtnpmRunningEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningEs.setStatus("current")


class _NbsOtnpmRunningEsrSig_Type(Integer32):
    """Custom type nbsOtnpmRunningEsrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmRunningEsrSig_Object = MibTableColumn
nbsOtnpmRunningEsrSig = _NbsOtnpmRunningEsrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 11),
    _NbsOtnpmRunningEsrSig_Type()
)
nbsOtnpmRunningEsrSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningEsrSig.setStatus("current")


class _NbsOtnpmRunningEsrExp_Type(Integer32):
    """Custom type nbsOtnpmRunningEsrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmRunningEsrExp_Type.__name__ = "Integer32"
_NbsOtnpmRunningEsrExp_Object = MibTableColumn
nbsOtnpmRunningEsrExp = _NbsOtnpmRunningEsrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 12),
    _NbsOtnpmRunningEsrExp_Type()
)
nbsOtnpmRunningEsrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningEsrExp.setStatus("current")
_NbsOtnpmRunningSes_Type = Counter32
_NbsOtnpmRunningSes_Object = MibTableColumn
nbsOtnpmRunningSes = _NbsOtnpmRunningSes_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 13),
    _NbsOtnpmRunningSes_Type()
)
nbsOtnpmRunningSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningSes.setStatus("current")


class _NbsOtnpmRunningSesrSig_Type(Integer32):
    """Custom type nbsOtnpmRunningSesrSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmRunningSesrSig_Object = MibTableColumn
nbsOtnpmRunningSesrSig = _NbsOtnpmRunningSesrSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 14),
    _NbsOtnpmRunningSesrSig_Type()
)
nbsOtnpmRunningSesrSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningSesrSig.setStatus("current")


class _NbsOtnpmRunningSesrExp_Type(Integer32):
    """Custom type nbsOtnpmRunningSesrExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmRunningSesrExp_Type.__name__ = "Integer32"
_NbsOtnpmRunningSesrExp_Object = MibTableColumn
nbsOtnpmRunningSesrExp = _NbsOtnpmRunningSesrExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 15),
    _NbsOtnpmRunningSesrExp_Type()
)
nbsOtnpmRunningSesrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningSesrExp.setStatus("current")
_NbsOtnpmRunningBbe_Type = Counter64
_NbsOtnpmRunningBbe_Object = MibTableColumn
nbsOtnpmRunningBbe = _NbsOtnpmRunningBbe_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 16),
    _NbsOtnpmRunningBbe_Type()
)
nbsOtnpmRunningBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningBbe.setStatus("current")


class _NbsOtnpmRunningBberSig_Type(Integer32):
    """Custom type nbsOtnpmRunningBberSig based on Integer32"""
    defaultValue = 0


_NbsOtnpmRunningBberSig_Object = MibTableColumn
nbsOtnpmRunningBberSig = _NbsOtnpmRunningBberSig_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 17),
    _NbsOtnpmRunningBberSig_Type()
)
nbsOtnpmRunningBberSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningBberSig.setStatus("current")


class _NbsOtnpmRunningBberExp_Type(Integer32):
    """Custom type nbsOtnpmRunningBberExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsOtnpmRunningBberExp_Type.__name__ = "Integer32"
_NbsOtnpmRunningBberExp_Object = MibTableColumn
nbsOtnpmRunningBberExp = _NbsOtnpmRunningBberExp_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 18),
    _NbsOtnpmRunningBberExp_Type()
)
nbsOtnpmRunningBberExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningBberExp.setStatus("current")
_NbsOtnpmRunningUas_Type = Counter32
_NbsOtnpmRunningUas_Object = MibTableColumn
nbsOtnpmRunningUas = _NbsOtnpmRunningUas_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 19),
    _NbsOtnpmRunningUas_Type()
)
nbsOtnpmRunningUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningUas.setStatus("current")
_NbsOtnpmRunningFc_Type = Counter64
_NbsOtnpmRunningFc_Object = MibTableColumn
nbsOtnpmRunningFc = _NbsOtnpmRunningFc_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 20),
    _NbsOtnpmRunningFc_Type()
)
nbsOtnpmRunningFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningFc.setStatus("current")
_NbsOtnpmRunningAlarmsSupported_Type = NbsOtnAlarmMask
_NbsOtnpmRunningAlarmsSupported_Object = MibTableColumn
nbsOtnpmRunningAlarmsSupported = _NbsOtnpmRunningAlarmsSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 100),
    _NbsOtnpmRunningAlarmsSupported_Type()
)
nbsOtnpmRunningAlarmsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningAlarmsSupported.setStatus("current")
_NbsOtnpmRunningAlarmsRaised_Type = NbsOtnAlarmMask
_NbsOtnpmRunningAlarmsRaised_Object = MibTableColumn
nbsOtnpmRunningAlarmsRaised = _NbsOtnpmRunningAlarmsRaised_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 101),
    _NbsOtnpmRunningAlarmsRaised_Type()
)
nbsOtnpmRunningAlarmsRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningAlarmsRaised.setStatus("current")
_NbsOtnpmRunningAlarmsChanged_Type = NbsOtnAlarmMask
_NbsOtnpmRunningAlarmsChanged_Object = MibTableColumn
nbsOtnpmRunningAlarmsChanged = _NbsOtnpmRunningAlarmsChanged_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 4, 3, 1, 102),
    _NbsOtnpmRunningAlarmsChanged_Type()
)
nbsOtnpmRunningAlarmsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnpmRunningAlarmsChanged.setStatus("current")
_NbsOtnAlarmsGrp_ObjectIdentity = ObjectIdentity
nbsOtnAlarmsGrp = _NbsOtnAlarmsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 80)
)
if mibBuilder.loadTexts:
    nbsOtnAlarmsGrp.setStatus("current")
_NbsOtnAlarmsTable_Object = MibTable
nbsOtnAlarmsTable = _NbsOtnAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3)
)
if mibBuilder.loadTexts:
    nbsOtnAlarmsTable.setStatus("current")
_NbsOtnAlarmsEntry_Object = MibTableRow
nbsOtnAlarmsEntry = _NbsOtnAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1)
)
nbsOtnAlarmsEntry.setIndexNames(
    (0, "NBS-OTNPM-MIB", "nbsOtnAlarmsIfIndex"),
)
if mibBuilder.loadTexts:
    nbsOtnAlarmsEntry.setStatus("current")
_NbsOtnAlarmsIfIndex_Type = InterfaceIndex
_NbsOtnAlarmsIfIndex_Object = MibTableColumn
nbsOtnAlarmsIfIndex = _NbsOtnAlarmsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 1),
    _NbsOtnAlarmsIfIndex_Type()
)
nbsOtnAlarmsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsIfIndex.setStatus("current")
_NbsOtnAlarmsDate_Type = Integer32
_NbsOtnAlarmsDate_Object = MibTableColumn
nbsOtnAlarmsDate = _NbsOtnAlarmsDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 5),
    _NbsOtnAlarmsDate_Type()
)
nbsOtnAlarmsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsDate.setStatus("current")
_NbsOtnAlarmsTime_Type = Integer32
_NbsOtnAlarmsTime_Object = MibTableColumn
nbsOtnAlarmsTime = _NbsOtnAlarmsTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 6),
    _NbsOtnAlarmsTime_Type()
)
nbsOtnAlarmsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsTime.setStatus("current")
_NbsOtnAlarmsSpan_Type = Integer32
_NbsOtnAlarmsSpan_Object = MibTableColumn
nbsOtnAlarmsSpan = _NbsOtnAlarmsSpan_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 7),
    _NbsOtnAlarmsSpan_Type()
)
nbsOtnAlarmsSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsSpan.setStatus("current")


class _NbsOtnAlarmsState_Type(Integer32):
    """Custom type nbsOtnAlarmsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("monitoring", 2),
          ("notSupported", 1))
    )


_NbsOtnAlarmsState_Type.__name__ = "Integer32"
_NbsOtnAlarmsState_Object = MibTableColumn
nbsOtnAlarmsState = _NbsOtnAlarmsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 8),
    _NbsOtnAlarmsState_Type()
)
nbsOtnAlarmsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnAlarmsState.setStatus("current")
_NbsOtnAlarmsSupported_Type = NbsOtnAlarmMask
_NbsOtnAlarmsSupported_Object = MibTableColumn
nbsOtnAlarmsSupported = _NbsOtnAlarmsSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 100),
    _NbsOtnAlarmsSupported_Type()
)
nbsOtnAlarmsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsSupported.setStatus("current")
_NbsOtnAlarmsRaised_Type = NbsOtnAlarmMask
_NbsOtnAlarmsRaised_Object = MibTableColumn
nbsOtnAlarmsRaised = _NbsOtnAlarmsRaised_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 101),
    _NbsOtnAlarmsRaised_Type()
)
nbsOtnAlarmsRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsRaised.setStatus("current")
_NbsOtnAlarmsChanged_Type = NbsOtnAlarmMask
_NbsOtnAlarmsChanged_Object = MibTableColumn
nbsOtnAlarmsChanged = _NbsOtnAlarmsChanged_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 102),
    _NbsOtnAlarmsChanged_Type()
)
nbsOtnAlarmsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsChanged.setStatus("current")


class _NbsOtnAlarmsRcvdFTFL_Type(OctetString):
    """Custom type nbsOtnAlarmsRcvdFTFL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NbsOtnAlarmsRcvdFTFL_Type.__name__ = "OctetString"
_NbsOtnAlarmsRcvdFTFL_Object = MibTableColumn
nbsOtnAlarmsRcvdFTFL = _NbsOtnAlarmsRcvdFTFL_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 80, 3, 1, 110),
    _NbsOtnAlarmsRcvdFTFL_Type()
)
nbsOtnAlarmsRcvdFTFL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnAlarmsRcvdFTFL.setStatus("current")
_NbsOtnStatsGrp_ObjectIdentity = ObjectIdentity
nbsOtnStatsGrp = _NbsOtnStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 90)
)
if mibBuilder.loadTexts:
    nbsOtnStatsGrp.setStatus("current")
_NbsOtnStatsTable_Object = MibTable
nbsOtnStatsTable = _NbsOtnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3)
)
if mibBuilder.loadTexts:
    nbsOtnStatsTable.setStatus("current")
_NbsOtnStatsEntry_Object = MibTableRow
nbsOtnStatsEntry = _NbsOtnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1)
)
nbsOtnStatsEntry.setIndexNames(
    (0, "NBS-OTNPM-MIB", "nbsOtnStatsIfIndex"),
)
if mibBuilder.loadTexts:
    nbsOtnStatsEntry.setStatus("current")
_NbsOtnStatsIfIndex_Type = InterfaceIndex
_NbsOtnStatsIfIndex_Object = MibTableColumn
nbsOtnStatsIfIndex = _NbsOtnStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 1),
    _NbsOtnStatsIfIndex_Type()
)
nbsOtnStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsIfIndex.setStatus("current")
_NbsOtnStatsDate_Type = Integer32
_NbsOtnStatsDate_Object = MibTableColumn
nbsOtnStatsDate = _NbsOtnStatsDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 5),
    _NbsOtnStatsDate_Type()
)
nbsOtnStatsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsDate.setStatus("current")
_NbsOtnStatsTime_Type = Integer32
_NbsOtnStatsTime_Object = MibTableColumn
nbsOtnStatsTime = _NbsOtnStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 6),
    _NbsOtnStatsTime_Type()
)
nbsOtnStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsTime.setStatus("current")
_NbsOtnStatsSpan_Type = Integer32
_NbsOtnStatsSpan_Object = MibTableColumn
nbsOtnStatsSpan = _NbsOtnStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 7),
    _NbsOtnStatsSpan_Type()
)
nbsOtnStatsSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsSpan.setStatus("current")


class _NbsOtnStatsState_Type(Integer32):
    """Custom type nbsOtnStatsState based on Integer32"""
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
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1),
          ("stopped", 4))
    )


_NbsOtnStatsState_Type.__name__ = "Integer32"
_NbsOtnStatsState_Object = MibTableColumn
nbsOtnStatsState = _NbsOtnStatsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 8),
    _NbsOtnStatsState_Type()
)
nbsOtnStatsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOtnStatsState.setStatus("current")
_NbsOtnStatsErrCntSectBEI_Type = Counter64
_NbsOtnStatsErrCntSectBEI_Object = MibTableColumn
nbsOtnStatsErrCntSectBEI = _NbsOtnStatsErrCntSectBEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 21),
    _NbsOtnStatsErrCntSectBEI_Type()
)
nbsOtnStatsErrCntSectBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntSectBEI.setStatus("current")
_NbsOtnStatsErrCntPathBEI_Type = Counter64
_NbsOtnStatsErrCntPathBEI_Object = MibTableColumn
nbsOtnStatsErrCntPathBEI = _NbsOtnStatsErrCntPathBEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 22),
    _NbsOtnStatsErrCntPathBEI_Type()
)
nbsOtnStatsErrCntPathBEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntPathBEI.setStatus("current")
_NbsOtnStatsErrCntTcm1BEI_Type = Counter64
_NbsOtnStatsErrCntTcm1BEI_Object = MibTableColumn
nbsOtnStatsErrCntTcm1BEI = _NbsOtnStatsErrCntTcm1BEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 23),
    _NbsOtnStatsErrCntTcm1BEI_Type()
)
nbsOtnStatsErrCntTcm1BEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm1BEI.setStatus("current")
_NbsOtnStatsErrCntTcm2BEI_Type = Counter64
_NbsOtnStatsErrCntTcm2BEI_Object = MibTableColumn
nbsOtnStatsErrCntTcm2BEI = _NbsOtnStatsErrCntTcm2BEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 24),
    _NbsOtnStatsErrCntTcm2BEI_Type()
)
nbsOtnStatsErrCntTcm2BEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm2BEI.setStatus("current")
_NbsOtnStatsErrCntTcm3BEI_Type = Counter64
_NbsOtnStatsErrCntTcm3BEI_Object = MibTableColumn
nbsOtnStatsErrCntTcm3BEI = _NbsOtnStatsErrCntTcm3BEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 25),
    _NbsOtnStatsErrCntTcm3BEI_Type()
)
nbsOtnStatsErrCntTcm3BEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm3BEI.setStatus("current")
_NbsOtnStatsErrCntTcm4BEI_Type = Counter64
_NbsOtnStatsErrCntTcm4BEI_Object = MibTableColumn
nbsOtnStatsErrCntTcm4BEI = _NbsOtnStatsErrCntTcm4BEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 26),
    _NbsOtnStatsErrCntTcm4BEI_Type()
)
nbsOtnStatsErrCntTcm4BEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm4BEI.setStatus("current")
_NbsOtnStatsErrCntTcm5BEI_Type = Counter64
_NbsOtnStatsErrCntTcm5BEI_Object = MibTableColumn
nbsOtnStatsErrCntTcm5BEI = _NbsOtnStatsErrCntTcm5BEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 27),
    _NbsOtnStatsErrCntTcm5BEI_Type()
)
nbsOtnStatsErrCntTcm5BEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm5BEI.setStatus("current")
_NbsOtnStatsErrCntTcm6BEI_Type = Counter64
_NbsOtnStatsErrCntTcm6BEI_Object = MibTableColumn
nbsOtnStatsErrCntTcm6BEI = _NbsOtnStatsErrCntTcm6BEI_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 28),
    _NbsOtnStatsErrCntTcm6BEI_Type()
)
nbsOtnStatsErrCntTcm6BEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm6BEI.setStatus("current")
_NbsOtnStatsErrCntSectBIP8_Type = Counter64
_NbsOtnStatsErrCntSectBIP8_Object = MibTableColumn
nbsOtnStatsErrCntSectBIP8 = _NbsOtnStatsErrCntSectBIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 31),
    _NbsOtnStatsErrCntSectBIP8_Type()
)
nbsOtnStatsErrCntSectBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntSectBIP8.setStatus("current")
_NbsOtnStatsErrCntPathBIP8_Type = Counter64
_NbsOtnStatsErrCntPathBIP8_Object = MibTableColumn
nbsOtnStatsErrCntPathBIP8 = _NbsOtnStatsErrCntPathBIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 32),
    _NbsOtnStatsErrCntPathBIP8_Type()
)
nbsOtnStatsErrCntPathBIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntPathBIP8.setStatus("current")
_NbsOtnStatsErrCntTcm1BIP8_Type = Counter64
_NbsOtnStatsErrCntTcm1BIP8_Object = MibTableColumn
nbsOtnStatsErrCntTcm1BIP8 = _NbsOtnStatsErrCntTcm1BIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 33),
    _NbsOtnStatsErrCntTcm1BIP8_Type()
)
nbsOtnStatsErrCntTcm1BIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm1BIP8.setStatus("current")
_NbsOtnStatsErrCntTcm2BIP8_Type = Counter64
_NbsOtnStatsErrCntTcm2BIP8_Object = MibTableColumn
nbsOtnStatsErrCntTcm2BIP8 = _NbsOtnStatsErrCntTcm2BIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 34),
    _NbsOtnStatsErrCntTcm2BIP8_Type()
)
nbsOtnStatsErrCntTcm2BIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm2BIP8.setStatus("current")
_NbsOtnStatsErrCntTcm3BIP8_Type = Counter64
_NbsOtnStatsErrCntTcm3BIP8_Object = MibTableColumn
nbsOtnStatsErrCntTcm3BIP8 = _NbsOtnStatsErrCntTcm3BIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 35),
    _NbsOtnStatsErrCntTcm3BIP8_Type()
)
nbsOtnStatsErrCntTcm3BIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm3BIP8.setStatus("current")
_NbsOtnStatsErrCntTcm4BIP8_Type = Counter64
_NbsOtnStatsErrCntTcm4BIP8_Object = MibTableColumn
nbsOtnStatsErrCntTcm4BIP8 = _NbsOtnStatsErrCntTcm4BIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 36),
    _NbsOtnStatsErrCntTcm4BIP8_Type()
)
nbsOtnStatsErrCntTcm4BIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm4BIP8.setStatus("current")
_NbsOtnStatsErrCntTcm5BIP8_Type = Counter64
_NbsOtnStatsErrCntTcm5BIP8_Object = MibTableColumn
nbsOtnStatsErrCntTcm5BIP8 = _NbsOtnStatsErrCntTcm5BIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 37),
    _NbsOtnStatsErrCntTcm5BIP8_Type()
)
nbsOtnStatsErrCntTcm5BIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm5BIP8.setStatus("current")
_NbsOtnStatsErrCntTcm6BIP8_Type = Counter64
_NbsOtnStatsErrCntTcm6BIP8_Object = MibTableColumn
nbsOtnStatsErrCntTcm6BIP8 = _NbsOtnStatsErrCntTcm6BIP8_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 38),
    _NbsOtnStatsErrCntTcm6BIP8_Type()
)
nbsOtnStatsErrCntTcm6BIP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsErrCntTcm6BIP8.setStatus("current")
_NbsOtnStatsAlarmsSupported_Type = NbsOtnAlarmMask
_NbsOtnStatsAlarmsSupported_Object = MibTableColumn
nbsOtnStatsAlarmsSupported = _NbsOtnStatsAlarmsSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 100),
    _NbsOtnStatsAlarmsSupported_Type()
)
nbsOtnStatsAlarmsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsAlarmsSupported.setStatus("current")
_NbsOtnStatsAlarmsRaised_Type = NbsOtnAlarmMask
_NbsOtnStatsAlarmsRaised_Object = MibTableColumn
nbsOtnStatsAlarmsRaised = _NbsOtnStatsAlarmsRaised_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 101),
    _NbsOtnStatsAlarmsRaised_Type()
)
nbsOtnStatsAlarmsRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsAlarmsRaised.setStatus("current")
_NbsOtnStatsAlarmsChanged_Type = NbsOtnAlarmMask
_NbsOtnStatsAlarmsChanged_Object = MibTableColumn
nbsOtnStatsAlarmsChanged = _NbsOtnStatsAlarmsChanged_Object(
    (1, 3, 6, 1, 4, 1, 629, 222, 90, 3, 1, 102),
    _NbsOtnStatsAlarmsChanged_Type()
)
nbsOtnStatsAlarmsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOtnStatsAlarmsChanged.setStatus("current")
_NbsOtnpmEventsGrp_ObjectIdentity = ObjectIdentity
nbsOtnpmEventsGrp = _NbsOtnpmEventsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 100)
)
if mibBuilder.loadTexts:
    nbsOtnpmEventsGrp.setStatus("current")
_NbsOtnpmTraps_ObjectIdentity = ObjectIdentity
nbsOtnpmTraps = _NbsOtnpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0)
)
if mibBuilder.loadTexts:
    nbsOtnpmTraps.setStatus("current")

# Managed Objects groups


# Notification objects

nbsOtnpmTrapsEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 10)
)
nbsOtnpmTrapsEs.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentEs"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsEs.setStatus(
        "current"
    )

nbsOtnpmTrapsEsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 11)
)
nbsOtnpmTrapsEsr.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentEsrSig"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentEsrExp"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsEsr.setStatus(
        "current"
    )

nbsOtnpmTrapsSes = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 12)
)
nbsOtnpmTrapsSes.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentSes"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsSes.setStatus(
        "current"
    )

nbsOtnpmTrapsSesr = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 13)
)
nbsOtnpmTrapsSesr.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentSesrSig"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentSesrExp"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsSesr.setStatus(
        "current"
    )

nbsOtnpmTrapsBbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 14)
)
nbsOtnpmTrapsBbe.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentBbe"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsBbe.setStatus(
        "current"
    )

nbsOtnpmTrapsBber = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 15)
)
nbsOtnpmTrapsBber.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentBberSig"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentBberExp"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsBber.setStatus(
        "current"
    )

nbsOtnpmTrapsUas = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 16)
)
nbsOtnpmTrapsUas.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentUas"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsUas.setStatus(
        "current"
    )

nbsOtnpmTrapsFc = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 222, 100, 0, 17)
)
nbsOtnpmTrapsFc.setObjects(
      *(("NBS-OTNPM-MIB", "nbsOtnpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentInterval"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentScope"),
        ("NBS-OTNPM-MIB", "nbsOtnpmCurrentFc"))
)
if mibBuilder.loadTexts:
    nbsOtnpmTrapsFc.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-OTNPM-MIB",
    **{"NbsOtnAlarmId": NbsOtnAlarmId,
       "NbsOtnAlarmMask": NbsOtnAlarmMask,
       "nbsOtnpmMib": nbsOtnpmMib,
       "nbsOtnpmThresholdsGrp": nbsOtnpmThresholdsGrp,
       "nbsOtnpmThresholdsTable": nbsOtnpmThresholdsTable,
       "nbsOtnpmThresholdsEntry": nbsOtnpmThresholdsEntry,
       "nbsOtnpmThresholdsIfIndex": nbsOtnpmThresholdsIfIndex,
       "nbsOtnpmThresholdsInterval": nbsOtnpmThresholdsInterval,
       "nbsOtnpmThresholdsScope": nbsOtnpmThresholdsScope,
       "nbsOtnpmThresholdsEs": nbsOtnpmThresholdsEs,
       "nbsOtnpmThresholdsEsrSig": nbsOtnpmThresholdsEsrSig,
       "nbsOtnpmThresholdsEsrExp": nbsOtnpmThresholdsEsrExp,
       "nbsOtnpmThresholdsSes": nbsOtnpmThresholdsSes,
       "nbsOtnpmThresholdsSesrSig": nbsOtnpmThresholdsSesrSig,
       "nbsOtnpmThresholdsSesrExp": nbsOtnpmThresholdsSesrExp,
       "nbsOtnpmThresholdsBbe": nbsOtnpmThresholdsBbe,
       "nbsOtnpmThresholdsBberSig": nbsOtnpmThresholdsBberSig,
       "nbsOtnpmThresholdsBberExp": nbsOtnpmThresholdsBberExp,
       "nbsOtnpmThresholdsUas": nbsOtnpmThresholdsUas,
       "nbsOtnpmThresholdsFc": nbsOtnpmThresholdsFc,
       "nbsOtnpmCurrentGrp": nbsOtnpmCurrentGrp,
       "nbsOtnpmCurrentTable": nbsOtnpmCurrentTable,
       "nbsOtnpmCurrentEntry": nbsOtnpmCurrentEntry,
       "nbsOtnpmCurrentIfIndex": nbsOtnpmCurrentIfIndex,
       "nbsOtnpmCurrentInterval": nbsOtnpmCurrentInterval,
       "nbsOtnpmCurrentScope": nbsOtnpmCurrentScope,
       "nbsOtnpmCurrentDate": nbsOtnpmCurrentDate,
       "nbsOtnpmCurrentTime": nbsOtnpmCurrentTime,
       "nbsOtnpmCurrentEs": nbsOtnpmCurrentEs,
       "nbsOtnpmCurrentEsrSig": nbsOtnpmCurrentEsrSig,
       "nbsOtnpmCurrentEsrExp": nbsOtnpmCurrentEsrExp,
       "nbsOtnpmCurrentSes": nbsOtnpmCurrentSes,
       "nbsOtnpmCurrentSesrSig": nbsOtnpmCurrentSesrSig,
       "nbsOtnpmCurrentSesrExp": nbsOtnpmCurrentSesrExp,
       "nbsOtnpmCurrentBbe": nbsOtnpmCurrentBbe,
       "nbsOtnpmCurrentBberSig": nbsOtnpmCurrentBberSig,
       "nbsOtnpmCurrentBberExp": nbsOtnpmCurrentBberExp,
       "nbsOtnpmCurrentUas": nbsOtnpmCurrentUas,
       "nbsOtnpmCurrentFc": nbsOtnpmCurrentFc,
       "nbsOtnpmCurrentAlarmsSupported": nbsOtnpmCurrentAlarmsSupported,
       "nbsOtnpmCurrentAlarmsRaised": nbsOtnpmCurrentAlarmsRaised,
       "nbsOtnpmCurrentAlarmsChanged": nbsOtnpmCurrentAlarmsChanged,
       "nbsOtnpmHistoricGrp": nbsOtnpmHistoricGrp,
       "nbsOtnpmHistoricTable": nbsOtnpmHistoricTable,
       "nbsOtnpmHistoricEntry": nbsOtnpmHistoricEntry,
       "nbsOtnpmHistoricIfIndex": nbsOtnpmHistoricIfIndex,
       "nbsOtnpmHistoricInterval": nbsOtnpmHistoricInterval,
       "nbsOtnpmHistoricScope": nbsOtnpmHistoricScope,
       "nbsOtnpmHistoricSample": nbsOtnpmHistoricSample,
       "nbsOtnpmHistoricDate": nbsOtnpmHistoricDate,
       "nbsOtnpmHistoricTime": nbsOtnpmHistoricTime,
       "nbsOtnpmHistoricEs": nbsOtnpmHistoricEs,
       "nbsOtnpmHistoricEsrSig": nbsOtnpmHistoricEsrSig,
       "nbsOtnpmHistoricEsrExp": nbsOtnpmHistoricEsrExp,
       "nbsOtnpmHistoricSes": nbsOtnpmHistoricSes,
       "nbsOtnpmHistoricSesrSig": nbsOtnpmHistoricSesrSig,
       "nbsOtnpmHistoricSesrExp": nbsOtnpmHistoricSesrExp,
       "nbsOtnpmHistoricBbe": nbsOtnpmHistoricBbe,
       "nbsOtnpmHistoricBberSig": nbsOtnpmHistoricBberSig,
       "nbsOtnpmHistoricBberExp": nbsOtnpmHistoricBberExp,
       "nbsOtnpmHistoricUas": nbsOtnpmHistoricUas,
       "nbsOtnpmHistoricFc": nbsOtnpmHistoricFc,
       "nbsOtnpmHistoricAlarmsSupported": nbsOtnpmHistoricAlarmsSupported,
       "nbsOtnpmHistoricAlarmsRaised": nbsOtnpmHistoricAlarmsRaised,
       "nbsOtnpmHistoricAlarmsChanged": nbsOtnpmHistoricAlarmsChanged,
       "nbsOtnpmRunningGrp": nbsOtnpmRunningGrp,
       "nbsOtnpmRunningTable": nbsOtnpmRunningTable,
       "nbsOtnpmRunningEntry": nbsOtnpmRunningEntry,
       "nbsOtnpmRunningIfIndex": nbsOtnpmRunningIfIndex,
       "nbsOtnpmRunningScope": nbsOtnpmRunningScope,
       "nbsOtnpmRunningDate": nbsOtnpmRunningDate,
       "nbsOtnpmRunningTime": nbsOtnpmRunningTime,
       "nbsOtnpmRunningEs": nbsOtnpmRunningEs,
       "nbsOtnpmRunningEsrSig": nbsOtnpmRunningEsrSig,
       "nbsOtnpmRunningEsrExp": nbsOtnpmRunningEsrExp,
       "nbsOtnpmRunningSes": nbsOtnpmRunningSes,
       "nbsOtnpmRunningSesrSig": nbsOtnpmRunningSesrSig,
       "nbsOtnpmRunningSesrExp": nbsOtnpmRunningSesrExp,
       "nbsOtnpmRunningBbe": nbsOtnpmRunningBbe,
       "nbsOtnpmRunningBberSig": nbsOtnpmRunningBberSig,
       "nbsOtnpmRunningBberExp": nbsOtnpmRunningBberExp,
       "nbsOtnpmRunningUas": nbsOtnpmRunningUas,
       "nbsOtnpmRunningFc": nbsOtnpmRunningFc,
       "nbsOtnpmRunningAlarmsSupported": nbsOtnpmRunningAlarmsSupported,
       "nbsOtnpmRunningAlarmsRaised": nbsOtnpmRunningAlarmsRaised,
       "nbsOtnpmRunningAlarmsChanged": nbsOtnpmRunningAlarmsChanged,
       "nbsOtnAlarmsGrp": nbsOtnAlarmsGrp,
       "nbsOtnAlarmsTable": nbsOtnAlarmsTable,
       "nbsOtnAlarmsEntry": nbsOtnAlarmsEntry,
       "nbsOtnAlarmsIfIndex": nbsOtnAlarmsIfIndex,
       "nbsOtnAlarmsDate": nbsOtnAlarmsDate,
       "nbsOtnAlarmsTime": nbsOtnAlarmsTime,
       "nbsOtnAlarmsSpan": nbsOtnAlarmsSpan,
       "nbsOtnAlarmsState": nbsOtnAlarmsState,
       "nbsOtnAlarmsSupported": nbsOtnAlarmsSupported,
       "nbsOtnAlarmsRaised": nbsOtnAlarmsRaised,
       "nbsOtnAlarmsChanged": nbsOtnAlarmsChanged,
       "nbsOtnAlarmsRcvdFTFL": nbsOtnAlarmsRcvdFTFL,
       "nbsOtnStatsGrp": nbsOtnStatsGrp,
       "nbsOtnStatsTable": nbsOtnStatsTable,
       "nbsOtnStatsEntry": nbsOtnStatsEntry,
       "nbsOtnStatsIfIndex": nbsOtnStatsIfIndex,
       "nbsOtnStatsDate": nbsOtnStatsDate,
       "nbsOtnStatsTime": nbsOtnStatsTime,
       "nbsOtnStatsSpan": nbsOtnStatsSpan,
       "nbsOtnStatsState": nbsOtnStatsState,
       "nbsOtnStatsErrCntSectBEI": nbsOtnStatsErrCntSectBEI,
       "nbsOtnStatsErrCntPathBEI": nbsOtnStatsErrCntPathBEI,
       "nbsOtnStatsErrCntTcm1BEI": nbsOtnStatsErrCntTcm1BEI,
       "nbsOtnStatsErrCntTcm2BEI": nbsOtnStatsErrCntTcm2BEI,
       "nbsOtnStatsErrCntTcm3BEI": nbsOtnStatsErrCntTcm3BEI,
       "nbsOtnStatsErrCntTcm4BEI": nbsOtnStatsErrCntTcm4BEI,
       "nbsOtnStatsErrCntTcm5BEI": nbsOtnStatsErrCntTcm5BEI,
       "nbsOtnStatsErrCntTcm6BEI": nbsOtnStatsErrCntTcm6BEI,
       "nbsOtnStatsErrCntSectBIP8": nbsOtnStatsErrCntSectBIP8,
       "nbsOtnStatsErrCntPathBIP8": nbsOtnStatsErrCntPathBIP8,
       "nbsOtnStatsErrCntTcm1BIP8": nbsOtnStatsErrCntTcm1BIP8,
       "nbsOtnStatsErrCntTcm2BIP8": nbsOtnStatsErrCntTcm2BIP8,
       "nbsOtnStatsErrCntTcm3BIP8": nbsOtnStatsErrCntTcm3BIP8,
       "nbsOtnStatsErrCntTcm4BIP8": nbsOtnStatsErrCntTcm4BIP8,
       "nbsOtnStatsErrCntTcm5BIP8": nbsOtnStatsErrCntTcm5BIP8,
       "nbsOtnStatsErrCntTcm6BIP8": nbsOtnStatsErrCntTcm6BIP8,
       "nbsOtnStatsAlarmsSupported": nbsOtnStatsAlarmsSupported,
       "nbsOtnStatsAlarmsRaised": nbsOtnStatsAlarmsRaised,
       "nbsOtnStatsAlarmsChanged": nbsOtnStatsAlarmsChanged,
       "nbsOtnpmEventsGrp": nbsOtnpmEventsGrp,
       "nbsOtnpmTraps": nbsOtnpmTraps,
       "nbsOtnpmTrapsEs": nbsOtnpmTrapsEs,
       "nbsOtnpmTrapsEsr": nbsOtnpmTrapsEsr,
       "nbsOtnpmTrapsSes": nbsOtnpmTrapsSes,
       "nbsOtnpmTrapsSesr": nbsOtnpmTrapsSesr,
       "nbsOtnpmTrapsBbe": nbsOtnpmTrapsBbe,
       "nbsOtnpmTrapsBber": nbsOtnpmTrapsBber,
       "nbsOtnpmTrapsUas": nbsOtnpmTrapsUas,
       "nbsOtnpmTrapsFc": nbsOtnpmTrapsFc}
)
