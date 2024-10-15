# SNMP MIB module (BCAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BCAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:26 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniBcam_ObjectIdentity = ObjectIdentity
sniBcam = _SniBcam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17)
)
_BcamTrap_ObjectIdentity = ObjectIdentity
bcamTrap = _BcamTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 1)
)
_BcamTrapString_Type = DisplayString
_BcamTrapString_Object = MibScalar
bcamTrapString = _BcamTrapString_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 1, 1),
    _BcamTrapString_Type()
)
bcamTrapString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcamTrapString.setStatus("mandatory")
_BcamTrapOutPoolOverCurrent_Type = Integer32
_BcamTrapOutPoolOverCurrent_Object = MibScalar
bcamTrapOutPoolOverCurrent = _BcamTrapOutPoolOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 1, 2),
    _BcamTrapOutPoolOverCurrent_Type()
)
bcamTrapOutPoolOverCurrent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcamTrapOutPoolOverCurrent.setStatus("mandatory")
_BcamTrapOutPoolUnderCurrent_Type = Integer32
_BcamTrapOutPoolUnderCurrent_Object = MibScalar
bcamTrapOutPoolUnderCurrent = _BcamTrapOutPoolUnderCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 1, 3),
    _BcamTrapOutPoolUnderCurrent_Type()
)
bcamTrapOutPoolUnderCurrent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcamTrapOutPoolUnderCurrent.setStatus("mandatory")
_BcamTrapInPoolOverCurrent_Type = Integer32
_BcamTrapInPoolOverCurrent_Object = MibScalar
bcamTrapInPoolOverCurrent = _BcamTrapInPoolOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 1, 4),
    _BcamTrapInPoolOverCurrent_Type()
)
bcamTrapInPoolOverCurrent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcamTrapInPoolOverCurrent.setStatus("mandatory")
_BcamTrapInPoolUnderCurrent_Type = Integer32
_BcamTrapInPoolUnderCurrent_Object = MibScalar
bcamTrapInPoolUnderCurrent = _BcamTrapInPoolUnderCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 1, 5),
    _BcamTrapInPoolUnderCurrent_Type()
)
bcamTrapInPoolUnderCurrent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcamTrapInPoolUnderCurrent.setStatus("mandatory")
_BcamGlobal_ObjectIdentity = ObjectIdentity
bcamGlobal = _BcamGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2)
)


class _BcamGlobalBcamVersion_Type(DisplayString):
    """Custom type bcamGlobalBcamVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BcamGlobalBcamVersion_Type.__name__ = "DisplayString"
_BcamGlobalBcamVersion_Object = MibScalar
bcamGlobalBcamVersion = _BcamGlobalBcamVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 1),
    _BcamGlobalBcamVersion_Type()
)
bcamGlobalBcamVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalBcamVersion.setStatus("mandatory")
_BcamGlobalMibVersion_Type = Integer32
_BcamGlobalMibVersion_Object = MibScalar
bcamGlobalMibVersion = _BcamGlobalMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 2),
    _BcamGlobalMibVersion_Type()
)
bcamGlobalMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalMibVersion.setStatus("mandatory")
_BcamGlobalUpTime_Type = Integer32
_BcamGlobalUpTime_Object = MibScalar
bcamGlobalUpTime = _BcamGlobalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 3),
    _BcamGlobalUpTime_Type()
)
bcamGlobalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalUpTime.setStatus("mandatory")
_BcamGlobalPortNonpriv_Type = Integer32
_BcamGlobalPortNonpriv_Object = MibScalar
bcamGlobalPortNonpriv = _BcamGlobalPortNonpriv_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 4),
    _BcamGlobalPortNonpriv_Type()
)
bcamGlobalPortNonpriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalPortNonpriv.setStatus("mandatory")
_BcamGlobalPortFree_Type = Integer32
_BcamGlobalPortFree_Object = MibScalar
bcamGlobalPortFree = _BcamGlobalPortFree_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 5),
    _BcamGlobalPortFree_Type()
)
bcamGlobalPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalPortFree.setStatus("mandatory")
_BcamGlobalNumBitmap_Type = Integer32
_BcamGlobalNumBitmap_Object = MibScalar
bcamGlobalNumBitmap = _BcamGlobalNumBitmap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 6),
    _BcamGlobalNumBitmap_Type()
)
bcamGlobalNumBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalNumBitmap.setStatus("mandatory")
_BcamGlobalMaxRemoteIp_Type = Integer32
_BcamGlobalMaxRemoteIp_Object = MibScalar
bcamGlobalMaxRemoteIp = _BcamGlobalMaxRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 7),
    _BcamGlobalMaxRemoteIp_Type()
)
bcamGlobalMaxRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalMaxRemoteIp.setStatus("mandatory")


class _BcamGlobalEsCreationIp_Type(Integer32):
    """Custom type bcamGlobalEsCreationIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipInData", 2),
          ("ipOff", 1),
          ("ipOutData", 4),
          ("ipRoutingData", 16),
          ("ipRoutingProt", 8))
    )


_BcamGlobalEsCreationIp_Type.__name__ = "Integer32"
_BcamGlobalEsCreationIp_Object = MibScalar
bcamGlobalEsCreationIp = _BcamGlobalEsCreationIp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 8),
    _BcamGlobalEsCreationIp_Type()
)
bcamGlobalEsCreationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalEsCreationIp.setStatus("mandatory")


class _BcamGlobalEsCreationIso_Type(Integer32):
    """Custom type bcamGlobalEsCreationIso based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("isoInData", 2),
          ("isoOff", 1),
          ("isoOutData", 4),
          ("isoRoutingData", 16),
          ("isoRoutingProt", 8))
    )


_BcamGlobalEsCreationIso_Type.__name__ = "Integer32"
_BcamGlobalEsCreationIso_Object = MibScalar
bcamGlobalEsCreationIso = _BcamGlobalEsCreationIso_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 9),
    _BcamGlobalEsCreationIso_Type()
)
bcamGlobalEsCreationIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalEsCreationIso.setStatus("mandatory")


class _BcamGlobalBroadcast_Type(Integer32):
    """Custom type bcamGlobalBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BcamGlobalBroadcast_Type.__name__ = "Integer32"
_BcamGlobalBroadcast_Object = MibScalar
bcamGlobalBroadcast = _BcamGlobalBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 10),
    _BcamGlobalBroadcast_Type()
)
bcamGlobalBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalBroadcast.setStatus("mandatory")


class _BcamGlobalArp_Type(Integer32):
    """Custom type bcamGlobalArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 4),
          ("quiet", 2))
    )


_BcamGlobalArp_Type.__name__ = "Integer32"
_BcamGlobalArp_Object = MibScalar
bcamGlobalArp = _BcamGlobalArp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 11),
    _BcamGlobalArp_Type()
)
bcamGlobalArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalArp.setStatus("mandatory")


class _BcamGlobalRarp_Type(Integer32):
    """Custom type bcamGlobalRarp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BcamGlobalRarp_Type.__name__ = "Integer32"
_BcamGlobalRarp_Object = MibScalar
bcamGlobalRarp = _BcamGlobalRarp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 12),
    _BcamGlobalRarp_Type()
)
bcamGlobalRarp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalRarp.setStatus("mandatory")
_BcamGlobalInWaitLimit1_Type = Integer32
_BcamGlobalInWaitLimit1_Object = MibScalar
bcamGlobalInWaitLimit1 = _BcamGlobalInWaitLimit1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 13),
    _BcamGlobalInWaitLimit1_Type()
)
bcamGlobalInWaitLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInWaitLimit1.setStatus("mandatory")
_BcamGlobalInWaitLimit2_Type = Integer32
_BcamGlobalInWaitLimit2_Object = MibScalar
bcamGlobalInWaitLimit2 = _BcamGlobalInWaitLimit2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 14),
    _BcamGlobalInWaitLimit2_Type()
)
bcamGlobalInWaitLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInWaitLimit2.setStatus("mandatory")
_BcamGlobalInWaitLimit3_Type = Integer32
_BcamGlobalInWaitLimit3_Object = MibScalar
bcamGlobalInWaitLimit3 = _BcamGlobalInWaitLimit3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 15),
    _BcamGlobalInWaitLimit3_Type()
)
bcamGlobalInWaitLimit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInWaitLimit3.setStatus("mandatory")
_BcamGlobalInWaitLimit4_Type = Integer32
_BcamGlobalInWaitLimit4_Object = MibScalar
bcamGlobalInWaitLimit4 = _BcamGlobalInWaitLimit4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 16),
    _BcamGlobalInWaitLimit4_Type()
)
bcamGlobalInWaitLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInWaitLimit4.setStatus("mandatory")


class _BcamGlobalInWaitChange_Type(Integer32):
    """Custom type bcamGlobalInWaitChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcamGlobalInWaitChange_Type.__name__ = "Integer32"
_BcamGlobalInWaitChange_Object = MibScalar
bcamGlobalInWaitChange = _BcamGlobalInWaitChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 17),
    _BcamGlobalInWaitChange_Type()
)
bcamGlobalInWaitChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalInWaitChange.setStatus("mandatory")


class _BcamGlobalInWaitSet_Type(Integer32):
    """Custom type bcamGlobalInWaitSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BcamGlobalInWaitSet_Type.__name__ = "Integer32"
_BcamGlobalInWaitSet_Object = MibScalar
bcamGlobalInWaitSet = _BcamGlobalInWaitSet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 18),
    _BcamGlobalInWaitSet_Type()
)
bcamGlobalInWaitSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInWaitSet.setStatus("mandatory")
_BcamGlobalReactLimit1_Type = Integer32
_BcamGlobalReactLimit1_Object = MibScalar
bcamGlobalReactLimit1 = _BcamGlobalReactLimit1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 19),
    _BcamGlobalReactLimit1_Type()
)
bcamGlobalReactLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalReactLimit1.setStatus("mandatory")
_BcamGlobalReactLimit2_Type = Integer32
_BcamGlobalReactLimit2_Object = MibScalar
bcamGlobalReactLimit2 = _BcamGlobalReactLimit2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 20),
    _BcamGlobalReactLimit2_Type()
)
bcamGlobalReactLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalReactLimit2.setStatus("mandatory")
_BcamGlobalReactLimit3_Type = Integer32
_BcamGlobalReactLimit3_Object = MibScalar
bcamGlobalReactLimit3 = _BcamGlobalReactLimit3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 21),
    _BcamGlobalReactLimit3_Type()
)
bcamGlobalReactLimit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalReactLimit3.setStatus("mandatory")
_BcamGlobalReactLimit4_Type = Integer32
_BcamGlobalReactLimit4_Object = MibScalar
bcamGlobalReactLimit4 = _BcamGlobalReactLimit4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 22),
    _BcamGlobalReactLimit4_Type()
)
bcamGlobalReactLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalReactLimit4.setStatus("mandatory")


class _BcamGlobalReactChange_Type(Integer32):
    """Custom type bcamGlobalReactChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcamGlobalReactChange_Type.__name__ = "Integer32"
_BcamGlobalReactChange_Object = MibScalar
bcamGlobalReactChange = _BcamGlobalReactChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 23),
    _BcamGlobalReactChange_Type()
)
bcamGlobalReactChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalReactChange.setStatus("mandatory")


class _BcamGlobalReactSet_Type(Integer32):
    """Custom type bcamGlobalReactSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BcamGlobalReactSet_Type.__name__ = "Integer32"
_BcamGlobalReactSet_Object = MibScalar
bcamGlobalReactSet = _BcamGlobalReactSet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 24),
    _BcamGlobalReactSet_Type()
)
bcamGlobalReactSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalReactSet.setStatus("mandatory")
_BcamGlobalInProcLimit1_Type = Integer32
_BcamGlobalInProcLimit1_Object = MibScalar
bcamGlobalInProcLimit1 = _BcamGlobalInProcLimit1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 25),
    _BcamGlobalInProcLimit1_Type()
)
bcamGlobalInProcLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInProcLimit1.setStatus("mandatory")
_BcamGlobalInProcLimit2_Type = Integer32
_BcamGlobalInProcLimit2_Object = MibScalar
bcamGlobalInProcLimit2 = _BcamGlobalInProcLimit2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 26),
    _BcamGlobalInProcLimit2_Type()
)
bcamGlobalInProcLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInProcLimit2.setStatus("mandatory")
_BcamGlobalInProcLimit3_Type = Integer32
_BcamGlobalInProcLimit3_Object = MibScalar
bcamGlobalInProcLimit3 = _BcamGlobalInProcLimit3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 27),
    _BcamGlobalInProcLimit3_Type()
)
bcamGlobalInProcLimit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInProcLimit3.setStatus("mandatory")
_BcamGlobalInProcLimit4_Type = Integer32
_BcamGlobalInProcLimit4_Object = MibScalar
bcamGlobalInProcLimit4 = _BcamGlobalInProcLimit4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 28),
    _BcamGlobalInProcLimit4_Type()
)
bcamGlobalInProcLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInProcLimit4.setStatus("mandatory")


class _BcamGlobalInProcChange_Type(Integer32):
    """Custom type bcamGlobalInProcChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcamGlobalInProcChange_Type.__name__ = "Integer32"
_BcamGlobalInProcChange_Object = MibScalar
bcamGlobalInProcChange = _BcamGlobalInProcChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 29),
    _BcamGlobalInProcChange_Type()
)
bcamGlobalInProcChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalInProcChange.setStatus("mandatory")


class _BcamGlobalInProcSet_Type(Integer32):
    """Custom type bcamGlobalInProcSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BcamGlobalInProcSet_Type.__name__ = "Integer32"
_BcamGlobalInProcSet_Object = MibScalar
bcamGlobalInProcSet = _BcamGlobalInProcSet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 30),
    _BcamGlobalInProcSet_Type()
)
bcamGlobalInProcSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalInProcSet.setStatus("mandatory")
_BcamGlobalOutProcLimit1_Type = Integer32
_BcamGlobalOutProcLimit1_Object = MibScalar
bcamGlobalOutProcLimit1 = _BcamGlobalOutProcLimit1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 31),
    _BcamGlobalOutProcLimit1_Type()
)
bcamGlobalOutProcLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalOutProcLimit1.setStatus("mandatory")
_BcamGlobalOutProcLimit2_Type = Integer32
_BcamGlobalOutProcLimit2_Object = MibScalar
bcamGlobalOutProcLimit2 = _BcamGlobalOutProcLimit2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 32),
    _BcamGlobalOutProcLimit2_Type()
)
bcamGlobalOutProcLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalOutProcLimit2.setStatus("mandatory")
_BcamGlobalOutProcLimit3_Type = Integer32
_BcamGlobalOutProcLimit3_Object = MibScalar
bcamGlobalOutProcLimit3 = _BcamGlobalOutProcLimit3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 33),
    _BcamGlobalOutProcLimit3_Type()
)
bcamGlobalOutProcLimit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalOutProcLimit3.setStatus("mandatory")
_BcamGlobalOutProcLimit4_Type = Integer32
_BcamGlobalOutProcLimit4_Object = MibScalar
bcamGlobalOutProcLimit4 = _BcamGlobalOutProcLimit4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 34),
    _BcamGlobalOutProcLimit4_Type()
)
bcamGlobalOutProcLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalOutProcLimit4.setStatus("mandatory")


class _BcamGlobalOutProcChange_Type(Integer32):
    """Custom type bcamGlobalOutProcChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcamGlobalOutProcChange_Type.__name__ = "Integer32"
_BcamGlobalOutProcChange_Object = MibScalar
bcamGlobalOutProcChange = _BcamGlobalOutProcChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 35),
    _BcamGlobalOutProcChange_Type()
)
bcamGlobalOutProcChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalOutProcChange.setStatus("mandatory")


class _BcamGlobalOutProcSet_Type(Integer32):
    """Custom type bcamGlobalOutProcSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BcamGlobalOutProcSet_Type.__name__ = "Integer32"
_BcamGlobalOutProcSet_Object = MibScalar
bcamGlobalOutProcSet = _BcamGlobalOutProcSet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 36),
    _BcamGlobalOutProcSet_Type()
)
bcamGlobalOutProcSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalOutProcSet.setStatus("mandatory")


class _BcamGlobalSnmpRelease_Type(Integer32):
    """Custom type bcamGlobalSnmpRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BcamGlobalSnmpRelease_Type.__name__ = "Integer32"
_BcamGlobalSnmpRelease_Object = MibScalar
bcamGlobalSnmpRelease = _BcamGlobalSnmpRelease_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 37),
    _BcamGlobalSnmpRelease_Type()
)
bcamGlobalSnmpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalSnmpRelease.setStatus("mandatory")


class _BcamGlobalTrapPollInterval_Type(Integer32):
    """Custom type bcamGlobalTrapPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BcamGlobalTrapPollInterval_Type.__name__ = "Integer32"
_BcamGlobalTrapPollInterval_Object = MibScalar
bcamGlobalTrapPollInterval = _BcamGlobalTrapPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 38),
    _BcamGlobalTrapPollInterval_Type()
)
bcamGlobalTrapPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamGlobalTrapPollInterval.setStatus("mandatory")


class _BcamGlobalFileApplTable_Type(DisplayString):
    """Custom type bcamGlobalFileApplTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(54, 54),
    )


_BcamGlobalFileApplTable_Type.__name__ = "DisplayString"
_BcamGlobalFileApplTable_Object = MibScalar
bcamGlobalFileApplTable = _BcamGlobalFileApplTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 39),
    _BcamGlobalFileApplTable_Type()
)
bcamGlobalFileApplTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalFileApplTable.setStatus("mandatory")


class _BcamGlobalFileSocketHostTable_Type(DisplayString):
    """Custom type bcamGlobalFileSocketHostTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(54, 54),
    )


_BcamGlobalFileSocketHostTable_Type.__name__ = "DisplayString"
_BcamGlobalFileSocketHostTable_Object = MibScalar
bcamGlobalFileSocketHostTable = _BcamGlobalFileSocketHostTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 40),
    _BcamGlobalFileSocketHostTable_Type()
)
bcamGlobalFileSocketHostTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalFileSocketHostTable.setStatus("mandatory")


class _BcamGlobalFileProcTable_Type(DisplayString):
    """Custom type bcamGlobalFileProcTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(54, 54),
    )


_BcamGlobalFileProcTable_Type.__name__ = "DisplayString"
_BcamGlobalFileProcTable_Object = MibScalar
bcamGlobalFileProcTable = _BcamGlobalFileProcTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 41),
    _BcamGlobalFileProcTable_Type()
)
bcamGlobalFileProcTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalFileProcTable.setStatus("mandatory")


class _BcamGlobalAccessProcTable_Type(Integer32):
    """Custom type bcamGlobalAccessProcTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("update", 2))
    )


_BcamGlobalAccessProcTable_Type.__name__ = "Integer32"
_BcamGlobalAccessProcTable_Object = MibScalar
bcamGlobalAccessProcTable = _BcamGlobalAccessProcTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 42),
    _BcamGlobalAccessProcTable_Type()
)
bcamGlobalAccessProcTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalAccessProcTable.setStatus("mandatory")


class _BcamGlobalHostName_Type(DisplayString):
    """Custom type bcamGlobalHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamGlobalHostName_Type.__name__ = "DisplayString"
_BcamGlobalHostName_Object = MibScalar
bcamGlobalHostName = _BcamGlobalHostName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 2, 43),
    _BcamGlobalHostName_Type()
)
bcamGlobalHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamGlobalHostName.setStatus("mandatory")
_BcamMemory_ObjectIdentity = ObjectIdentity
bcamMemory = _BcamMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3)
)
_BcamMemoryClass3_Type = Integer32
_BcamMemoryClass3_Object = MibScalar
bcamMemoryClass3 = _BcamMemoryClass3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 1),
    _BcamMemoryClass3_Type()
)
bcamMemoryClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryClass3.setStatus("mandatory")
_BcamMemoryClass4_Type = Integer32
_BcamMemoryClass4_Object = MibScalar
bcamMemoryClass4 = _BcamMemoryClass4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 2),
    _BcamMemoryClass4_Type()
)
bcamMemoryClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryClass4.setStatus("mandatory")
_BcamMemoryLenLongEventSlot_Type = Integer32
_BcamMemoryLenLongEventSlot_Object = MibScalar
bcamMemoryLenLongEventSlot = _BcamMemoryLenLongEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 3),
    _BcamMemoryLenLongEventSlot_Type()
)
bcamMemoryLenLongEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenLongEventSlot.setStatus("mandatory")
_BcamMemoryOccLongEventSlot_Type = Integer32
_BcamMemoryOccLongEventSlot_Object = MibScalar
bcamMemoryOccLongEventSlot = _BcamMemoryOccLongEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 4),
    _BcamMemoryOccLongEventSlot_Type()
)
bcamMemoryOccLongEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccLongEventSlot.setStatus("mandatory")
_BcamMemoryLenShortEventSlot_Type = Integer32
_BcamMemoryLenShortEventSlot_Object = MibScalar
bcamMemoryLenShortEventSlot = _BcamMemoryLenShortEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 5),
    _BcamMemoryLenShortEventSlot_Type()
)
bcamMemoryLenShortEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenShortEventSlot.setStatus("mandatory")
_BcamMemoryOccShortEventSlot_Type = Integer32
_BcamMemoryOccShortEventSlot_Object = MibScalar
bcamMemoryOccShortEventSlot = _BcamMemoryOccShortEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 6),
    _BcamMemoryOccShortEventSlot_Type()
)
bcamMemoryOccShortEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccShortEventSlot.setStatus("mandatory")
_BcamMemoryLenTransParamSlot_Type = Integer32
_BcamMemoryLenTransParamSlot_Object = MibScalar
bcamMemoryLenTransParamSlot = _BcamMemoryLenTransParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 7),
    _BcamMemoryLenTransParamSlot_Type()
)
bcamMemoryLenTransParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenTransParamSlot.setStatus("mandatory")
_BcamMemoryOccTransParamSlot_Type = Integer32
_BcamMemoryOccTransParamSlot_Object = MibScalar
bcamMemoryOccTransParamSlot = _BcamMemoryOccTransParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 8),
    _BcamMemoryOccTransParamSlot_Type()
)
bcamMemoryOccTransParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccTransParamSlot.setStatus("mandatory")
_BcamMemoryLenSnmpParamSlot_Type = Integer32
_BcamMemoryLenSnmpParamSlot_Object = MibScalar
bcamMemoryLenSnmpParamSlot = _BcamMemoryLenSnmpParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 9),
    _BcamMemoryLenSnmpParamSlot_Type()
)
bcamMemoryLenSnmpParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenSnmpParamSlot.setStatus("mandatory")
_BcamMemoryOccSnmpParamSlot_Type = Integer32
_BcamMemoryOccSnmpParamSlot_Object = MibScalar
bcamMemoryOccSnmpParamSlot = _BcamMemoryOccSnmpParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 10),
    _BcamMemoryOccSnmpParamSlot_Type()
)
bcamMemoryOccSnmpParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccSnmpParamSlot.setStatus("mandatory")
_BcamMemoryLenApplCb_Type = Integer32
_BcamMemoryLenApplCb_Object = MibScalar
bcamMemoryLenApplCb = _BcamMemoryLenApplCb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 11),
    _BcamMemoryLenApplCb_Type()
)
bcamMemoryLenApplCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenApplCb.setStatus("mandatory")
_BcamMemoryOccApplCb_Type = Integer32
_BcamMemoryOccApplCb_Object = MibScalar
bcamMemoryOccApplCb = _BcamMemoryOccApplCb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 12),
    _BcamMemoryOccApplCb_Type()
)
bcamMemoryOccApplCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccApplCb.setStatus("mandatory")
_BcamMemoryLenEnaCb_Type = Integer32
_BcamMemoryLenEnaCb_Object = MibScalar
bcamMemoryLenEnaCb = _BcamMemoryLenEnaCb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 13),
    _BcamMemoryLenEnaCb_Type()
)
bcamMemoryLenEnaCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenEnaCb.setStatus("mandatory")
_BcamMemoryOccEnaCb_Type = Integer32
_BcamMemoryOccEnaCb_Object = MibScalar
bcamMemoryOccEnaCb = _BcamMemoryOccEnaCb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 14),
    _BcamMemoryOccEnaCb_Type()
)
bcamMemoryOccEnaCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccEnaCb.setStatus("mandatory")
_BcamMemoryLenExtApplCb_Type = Integer32
_BcamMemoryLenExtApplCb_Object = MibScalar
bcamMemoryLenExtApplCb = _BcamMemoryLenExtApplCb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 15),
    _BcamMemoryLenExtApplCb_Type()
)
bcamMemoryLenExtApplCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenExtApplCb.setStatus("mandatory")
_BcamMemoryOccExtApplCb_Type = Integer32
_BcamMemoryOccExtApplCb_Object = MibScalar
bcamMemoryOccExtApplCb = _BcamMemoryOccExtApplCb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 16),
    _BcamMemoryOccExtApplCb_Type()
)
bcamMemoryOccExtApplCb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccExtApplCb.setStatus("mandatory")
_BcamMemoryLenShortResConn2_Type = Integer32
_BcamMemoryLenShortResConn2_Object = MibScalar
bcamMemoryLenShortResConn2 = _BcamMemoryLenShortResConn2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 17),
    _BcamMemoryLenShortResConn2_Type()
)
bcamMemoryLenShortResConn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenShortResConn2.setStatus("mandatory")
_BcamMemoryOccShortResConn2_Type = Integer32
_BcamMemoryOccShortResConn2_Object = MibScalar
bcamMemoryOccShortResConn2 = _BcamMemoryOccShortResConn2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 18),
    _BcamMemoryOccShortResConn2_Type()
)
bcamMemoryOccShortResConn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccShortResConn2.setStatus("mandatory")
_BcamMemoryLenLongResConn2_Type = Integer32
_BcamMemoryLenLongResConn2_Object = MibScalar
bcamMemoryLenLongResConn2 = _BcamMemoryLenLongResConn2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 19),
    _BcamMemoryLenLongResConn2_Type()
)
bcamMemoryLenLongResConn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenLongResConn2.setStatus("mandatory")
_BcamMemoryOccLongResConn2_Type = Integer32
_BcamMemoryOccLongResConn2_Object = MibScalar
bcamMemoryOccLongResConn2 = _BcamMemoryOccLongResConn2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 20),
    _BcamMemoryOccLongResConn2_Type()
)
bcamMemoryOccLongResConn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccLongResConn2.setStatus("mandatory")
_BcamMemoryLenShortPagConn1_Type = Integer32
_BcamMemoryLenShortPagConn1_Object = MibScalar
bcamMemoryLenShortPagConn1 = _BcamMemoryLenShortPagConn1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 21),
    _BcamMemoryLenShortPagConn1_Type()
)
bcamMemoryLenShortPagConn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenShortPagConn1.setStatus("mandatory")
_BcamMemoryOccShortPagConn1_Type = Integer32
_BcamMemoryOccShortPagConn1_Object = MibScalar
bcamMemoryOccShortPagConn1 = _BcamMemoryOccShortPagConn1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 22),
    _BcamMemoryOccShortPagConn1_Type()
)
bcamMemoryOccShortPagConn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccShortPagConn1.setStatus("mandatory")
_BcamMemoryLenSnmpConn_Type = Integer32
_BcamMemoryLenSnmpConn_Object = MibScalar
bcamMemoryLenSnmpConn = _BcamMemoryLenSnmpConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 23),
    _BcamMemoryLenSnmpConn_Type()
)
bcamMemoryLenSnmpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenSnmpConn.setStatus("mandatory")
_BcamMemoryOccSnmpConn_Type = Integer32
_BcamMemoryOccSnmpConn_Object = MibScalar
bcamMemoryOccSnmpConn = _BcamMemoryOccSnmpConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 24),
    _BcamMemoryOccSnmpConn_Type()
)
bcamMemoryOccSnmpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccSnmpConn.setStatus("mandatory")
_BcamMemoryLenLongPagConn1_Type = Integer32
_BcamMemoryLenLongPagConn1_Object = MibScalar
bcamMemoryLenLongPagConn1 = _BcamMemoryLenLongPagConn1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 25),
    _BcamMemoryLenLongPagConn1_Type()
)
bcamMemoryLenLongPagConn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenLongPagConn1.setStatus("mandatory")
_BcamMemoryOccLongPagConn1_Type = Integer32
_BcamMemoryOccLongPagConn1_Object = MibScalar
bcamMemoryOccLongPagConn1 = _BcamMemoryOccLongPagConn1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 26),
    _BcamMemoryOccLongPagConn1_Type()
)
bcamMemoryOccLongPagConn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccLongPagConn1.setStatus("mandatory")
_BcamMemoryLenShortPagConn2_Type = Integer32
_BcamMemoryLenShortPagConn2_Object = MibScalar
bcamMemoryLenShortPagConn2 = _BcamMemoryLenShortPagConn2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 27),
    _BcamMemoryLenShortPagConn2_Type()
)
bcamMemoryLenShortPagConn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryLenShortPagConn2.setStatus("mandatory")
_BcamMemoryOccShortPagConn2_Type = Integer32
_BcamMemoryOccShortPagConn2_Object = MibScalar
bcamMemoryOccShortPagConn2 = _BcamMemoryOccShortPagConn2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 28),
    _BcamMemoryOccShortPagConn2_Type()
)
bcamMemoryOccShortPagConn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryOccShortPagConn2.setStatus("mandatory")
_BcamMemoryPoolInputCurrent_Type = Integer32
_BcamMemoryPoolInputCurrent_Object = MibScalar
bcamMemoryPoolInputCurrent = _BcamMemoryPoolInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 29),
    _BcamMemoryPoolInputCurrent_Type()
)
bcamMemoryPoolInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputCurrent.setStatus("mandatory")
_BcamMemoryPoolInputResume_Type = Integer32
_BcamMemoryPoolInputResume_Object = MibScalar
bcamMemoryPoolInputResume = _BcamMemoryPoolInputResume_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 30),
    _BcamMemoryPoolInputResume_Type()
)
bcamMemoryPoolInputResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputResume.setStatus("mandatory")
_BcamMemoryPoolInputMonMax_Type = Integer32
_BcamMemoryPoolInputMonMax_Object = MibScalar
bcamMemoryPoolInputMonMax = _BcamMemoryPoolInputMonMax_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 31),
    _BcamMemoryPoolInputMonMax_Type()
)
bcamMemoryPoolInputMonMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputMonMax.setStatus("mandatory")
_BcamMemoryPoolInputMonMin_Type = Integer32
_BcamMemoryPoolInputMonMin_Object = MibScalar
bcamMemoryPoolInputMonMin = _BcamMemoryPoolInputMonMin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 32),
    _BcamMemoryPoolInputMonMin_Type()
)
bcamMemoryPoolInputMonMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputMonMin.setStatus("mandatory")
_BcamMemoryPoolInputLimit_Type = Integer32
_BcamMemoryPoolInputLimit_Object = MibScalar
bcamMemoryPoolInputLimit = _BcamMemoryPoolInputLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 33),
    _BcamMemoryPoolInputLimit_Type()
)
bcamMemoryPoolInputLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputLimit.setStatus("mandatory")
_BcamMemoryPoolInputLimitTrap_Type = Integer32
_BcamMemoryPoolInputLimitTrap_Object = MibScalar
bcamMemoryPoolInputLimitTrap = _BcamMemoryPoolInputLimitTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 34),
    _BcamMemoryPoolInputLimitTrap_Type()
)
bcamMemoryPoolInputLimitTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputLimitTrap.setStatus("mandatory")
_BcamMemoryPoolMaxResident_Type = Integer32
_BcamMemoryPoolMaxResident_Object = MibScalar
bcamMemoryPoolMaxResident = _BcamMemoryPoolMaxResident_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 35),
    _BcamMemoryPoolMaxResident_Type()
)
bcamMemoryPoolMaxResident.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamMemoryPoolMaxResident.setStatus("mandatory")
_BcamMemoryPoolMaxPageable_Type = Integer32
_BcamMemoryPoolMaxPageable_Object = MibScalar
bcamMemoryPoolMaxPageable = _BcamMemoryPoolMaxPageable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 36),
    _BcamMemoryPoolMaxPageable_Type()
)
bcamMemoryPoolMaxPageable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcamMemoryPoolMaxPageable.setStatus("mandatory")
_BcamMemoryPoolInputMaxPageable_Type = Integer32
_BcamMemoryPoolInputMaxPageable_Object = MibScalar
bcamMemoryPoolInputMaxPageable = _BcamMemoryPoolInputMaxPageable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 37),
    _BcamMemoryPoolInputMaxPageable_Type()
)
bcamMemoryPoolInputMaxPageable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolInputMaxPageable.setStatus("mandatory")
_BcamMemoryPoolOutputCurrent_Type = Integer32
_BcamMemoryPoolOutputCurrent_Object = MibScalar
bcamMemoryPoolOutputCurrent = _BcamMemoryPoolOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 38),
    _BcamMemoryPoolOutputCurrent_Type()
)
bcamMemoryPoolOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputCurrent.setStatus("mandatory")
_BcamMemoryPoolOutputResume_Type = Integer32
_BcamMemoryPoolOutputResume_Object = MibScalar
bcamMemoryPoolOutputResume = _BcamMemoryPoolOutputResume_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 39),
    _BcamMemoryPoolOutputResume_Type()
)
bcamMemoryPoolOutputResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputResume.setStatus("mandatory")
_BcamMemoryPoolOutputMonMax_Type = Integer32
_BcamMemoryPoolOutputMonMax_Object = MibScalar
bcamMemoryPoolOutputMonMax = _BcamMemoryPoolOutputMonMax_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 40),
    _BcamMemoryPoolOutputMonMax_Type()
)
bcamMemoryPoolOutputMonMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputMonMax.setStatus("mandatory")
_BcamMemoryPoolOutputMonMin_Type = Integer32
_BcamMemoryPoolOutputMonMin_Object = MibScalar
bcamMemoryPoolOutputMonMin = _BcamMemoryPoolOutputMonMin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 41),
    _BcamMemoryPoolOutputMonMin_Type()
)
bcamMemoryPoolOutputMonMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputMonMin.setStatus("mandatory")
_BcamMemoryPoolOutputLimit_Type = Integer32
_BcamMemoryPoolOutputLimit_Object = MibScalar
bcamMemoryPoolOutputLimit = _BcamMemoryPoolOutputLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 42),
    _BcamMemoryPoolOutputLimit_Type()
)
bcamMemoryPoolOutputLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputLimit.setStatus("mandatory")
_BcamMemoryPoolOutputLimitTrap_Type = Integer32
_BcamMemoryPoolOutputLimitTrap_Object = MibScalar
bcamMemoryPoolOutputLimitTrap = _BcamMemoryPoolOutputLimitTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 43),
    _BcamMemoryPoolOutputLimitTrap_Type()
)
bcamMemoryPoolOutputLimitTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputLimitTrap.setStatus("mandatory")
_BcamMemoryPoolMaxCells_Type = Integer32
_BcamMemoryPoolMaxCells_Object = MibScalar
bcamMemoryPoolMaxCells = _BcamMemoryPoolMaxCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 44),
    _BcamMemoryPoolMaxCells_Type()
)
bcamMemoryPoolMaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolMaxCells.setStatus("mandatory")
_BcamMemoryPoolOutputMaxPageable_Type = Integer32
_BcamMemoryPoolOutputMaxPageable_Object = MibScalar
bcamMemoryPoolOutputMaxPageable = _BcamMemoryPoolOutputMaxPageable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 45),
    _BcamMemoryPoolOutputMaxPageable_Type()
)
bcamMemoryPoolOutputMaxPageable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolOutputMaxPageable.setStatus("mandatory")
_BcamMemoryPoolRoutingCurrent_Type = Integer32
_BcamMemoryPoolRoutingCurrent_Object = MibScalar
bcamMemoryPoolRoutingCurrent = _BcamMemoryPoolRoutingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 46),
    _BcamMemoryPoolRoutingCurrent_Type()
)
bcamMemoryPoolRoutingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolRoutingCurrent.setStatus("mandatory")
_BcamMemoryPoolRoutingLimit_Type = Integer32
_BcamMemoryPoolRoutingLimit_Object = MibScalar
bcamMemoryPoolRoutingLimit = _BcamMemoryPoolRoutingLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 47),
    _BcamMemoryPoolRoutingLimit_Type()
)
bcamMemoryPoolRoutingLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolRoutingLimit.setStatus("mandatory")
_BcamMemoryPoolPageableCurrent_Type = Integer32
_BcamMemoryPoolPageableCurrent_Object = MibScalar
bcamMemoryPoolPageableCurrent = _BcamMemoryPoolPageableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 48),
    _BcamMemoryPoolPageableCurrent_Type()
)
bcamMemoryPoolPageableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolPageableCurrent.setStatus("mandatory")
_BcamMemoryPoolPageableFixed_Type = Integer32
_BcamMemoryPoolPageableFixed_Object = MibScalar
bcamMemoryPoolPageableFixed = _BcamMemoryPoolPageableFixed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 49),
    _BcamMemoryPoolPageableFixed_Type()
)
bcamMemoryPoolPageableFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryPoolPageableFixed.setStatus("mandatory")
_BcamMemoryCellReqSucc_Type = Integer32
_BcamMemoryCellReqSucc_Object = MibScalar
bcamMemoryCellReqSucc = _BcamMemoryCellReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 50),
    _BcamMemoryCellReqSucc_Type()
)
bcamMemoryCellReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqSucc.setStatus("mandatory")
_BcamMemoryCellReqResOutExceed_Type = Integer32
_BcamMemoryCellReqResOutExceed_Object = MibScalar
bcamMemoryCellReqResOutExceed = _BcamMemoryCellReqResOutExceed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 51),
    _BcamMemoryCellReqResOutExceed_Type()
)
bcamMemoryCellReqResOutExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqResOutExceed.setStatus("mandatory")
_BcamMemoryCellReqResInExceed_Type = Integer32
_BcamMemoryCellReqResInExceed_Object = MibScalar
bcamMemoryCellReqResInExceed = _BcamMemoryCellReqResInExceed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 52),
    _BcamMemoryCellReqResInExceed_Type()
)
bcamMemoryCellReqResInExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqResInExceed.setStatus("mandatory")
_BcamMemoryCellReqTempExceed_Type = Integer32
_BcamMemoryCellReqTempExceed_Object = MibScalar
bcamMemoryCellReqTempExceed = _BcamMemoryCellReqTempExceed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 53),
    _BcamMemoryCellReqTempExceed_Type()
)
bcamMemoryCellReqTempExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqTempExceed.setStatus("mandatory")
_BcamMemoryCellReqBitmapFull_Type = Integer32
_BcamMemoryCellReqBitmapFull_Object = MibScalar
bcamMemoryCellReqBitmapFull = _BcamMemoryCellReqBitmapFull_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 54),
    _BcamMemoryCellReqBitmapFull_Type()
)
bcamMemoryCellReqBitmapFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqBitmapFull.setStatus("mandatory")
_BcamMemoryCellReqNoMemory_Type = Integer32
_BcamMemoryCellReqNoMemory_Object = MibScalar
bcamMemoryCellReqNoMemory = _BcamMemoryCellReqNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 55),
    _BcamMemoryCellReqNoMemory_Type()
)
bcamMemoryCellReqNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqNoMemory.setStatus("mandatory")
_BcamMemoryCellReqPagInExceed_Type = Integer32
_BcamMemoryCellReqPagInExceed_Object = MibScalar
bcamMemoryCellReqPagInExceed = _BcamMemoryCellReqPagInExceed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 56),
    _BcamMemoryCellReqPagInExceed_Type()
)
bcamMemoryCellReqPagInExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqPagInExceed.setStatus("mandatory")
_BcamMemoryCellReqPagOutExceed_Type = Integer32
_BcamMemoryCellReqPagOutExceed_Object = MibScalar
bcamMemoryCellReqPagOutExceed = _BcamMemoryCellReqPagOutExceed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 3, 57),
    _BcamMemoryCellReqPagOutExceed_Type()
)
bcamMemoryCellReqPagOutExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamMemoryCellReqPagOutExceed.setStatus("mandatory")
_BcamTrace_ObjectIdentity = ObjectIdentity
bcamTrace = _BcamTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4)
)


class _BcamTraceSavingState_Type(Integer32):
    """Custom type bcamTraceSavingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("initiated", 1),
          ("noSaving", 32),
          ("passive", 8),
          ("shutting", 4),
          ("waiting", 16))
    )


_BcamTraceSavingState_Type.__name__ = "Integer32"
_BcamTraceSavingState_Object = MibScalar
bcamTraceSavingState = _BcamTraceSavingState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 1),
    _BcamTraceSavingState_Type()
)
bcamTraceSavingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceSavingState.setStatus("mandatory")


class _BcamTraceFilename_Type(DisplayString):
    """Custom type bcamTraceFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(54, 54),
    )


_BcamTraceFilename_Type.__name__ = "DisplayString"
_BcamTraceFilename_Object = MibScalar
bcamTraceFilename = _BcamTraceFilename_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 2),
    _BcamTraceFilename_Type()
)
bcamTraceFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceFilename.setStatus("mandatory")
_BcamTraceMaxFilesize_Type = Integer32
_BcamTraceMaxFilesize_Object = MibScalar
bcamTraceMaxFilesize = _BcamTraceMaxFilesize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 3),
    _BcamTraceMaxFilesize_Type()
)
bcamTraceMaxFilesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMaxFilesize.setStatus("mandatory")
_BcamTraceNumberFiles_Type = Integer32
_BcamTraceNumberFiles_Object = MibScalar
bcamTraceNumberFiles = _BcamTraceNumberFiles_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 4),
    _BcamTraceNumberFiles_Type()
)
bcamTraceNumberFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceNumberFiles.setStatus("mandatory")


class _BcamTraceAdmState_Type(Integer32):
    """Custom type bcamTraceAdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceAdmState_Type.__name__ = "Integer32"
_BcamTraceAdmState_Object = MibScalar
bcamTraceAdmState = _BcamTraceAdmState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 5),
    _BcamTraceAdmState_Type()
)
bcamTraceAdmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceAdmState.setStatus("mandatory")


class _BcamTraceAdmNumberBuffer_Type(Integer32):
    """Custom type bcamTraceAdmNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceAdmNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceAdmNumberBuffer_Object = MibScalar
bcamTraceAdmNumberBuffer = _BcamTraceAdmNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 6),
    _BcamTraceAdmNumberBuffer_Type()
)
bcamTraceAdmNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceAdmNumberBuffer.setStatus("mandatory")


class _BcamTraceAdmBufferLen_Type(Integer32):
    """Custom type bcamTraceAdmBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceAdmBufferLen_Type.__name__ = "Integer32"
_BcamTraceAdmBufferLen_Object = MibScalar
bcamTraceAdmBufferLen = _BcamTraceAdmBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 7),
    _BcamTraceAdmBufferLen_Type()
)
bcamTraceAdmBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceAdmBufferLen.setStatus("mandatory")


class _BcamTraceBasicState_Type(Integer32):
    """Custom type bcamTraceBasicState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceBasicState_Type.__name__ = "Integer32"
_BcamTraceBasicState_Object = MibScalar
bcamTraceBasicState = _BcamTraceBasicState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 8),
    _BcamTraceBasicState_Type()
)
bcamTraceBasicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceBasicState.setStatus("mandatory")


class _BcamTraceBasicNumberBuffer_Type(Integer32):
    """Custom type bcamTraceBasicNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceBasicNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceBasicNumberBuffer_Object = MibScalar
bcamTraceBasicNumberBuffer = _BcamTraceBasicNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 9),
    _BcamTraceBasicNumberBuffer_Type()
)
bcamTraceBasicNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceBasicNumberBuffer.setStatus("mandatory")


class _BcamTraceBasicBufferLen_Type(Integer32):
    """Custom type bcamTraceBasicBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceBasicBufferLen_Type.__name__ = "Integer32"
_BcamTraceBasicBufferLen_Object = MibScalar
bcamTraceBasicBufferLen = _BcamTraceBasicBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 10),
    _BcamTraceBasicBufferLen_Type()
)
bcamTraceBasicBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceBasicBufferLen.setStatus("mandatory")


class _BcamTraceConnState_Type(Integer32):
    """Custom type bcamTraceConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceConnState_Type.__name__ = "Integer32"
_BcamTraceConnState_Object = MibScalar
bcamTraceConnState = _BcamTraceConnState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 11),
    _BcamTraceConnState_Type()
)
bcamTraceConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceConnState.setStatus("mandatory")


class _BcamTraceConnNumberBuffer_Type(Integer32):
    """Custom type bcamTraceConnNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceConnNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceConnNumberBuffer_Object = MibScalar
bcamTraceConnNumberBuffer = _BcamTraceConnNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 12),
    _BcamTraceConnNumberBuffer_Type()
)
bcamTraceConnNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceConnNumberBuffer.setStatus("mandatory")


class _BcamTraceConnBufferLen_Type(Integer32):
    """Custom type bcamTraceConnBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceConnBufferLen_Type.__name__ = "Integer32"
_BcamTraceConnBufferLen_Object = MibScalar
bcamTraceConnBufferLen = _BcamTraceConnBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 13),
    _BcamTraceConnBufferLen_Type()
)
bcamTraceConnBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceConnBufferLen.setStatus("mandatory")


class _BcamTraceLocalState_Type(Integer32):
    """Custom type bcamTraceLocalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceLocalState_Type.__name__ = "Integer32"
_BcamTraceLocalState_Object = MibScalar
bcamTraceLocalState = _BcamTraceLocalState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 14),
    _BcamTraceLocalState_Type()
)
bcamTraceLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceLocalState.setStatus("mandatory")


class _BcamTraceLocalNumberBuffer_Type(Integer32):
    """Custom type bcamTraceLocalNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceLocalNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceLocalNumberBuffer_Object = MibScalar
bcamTraceLocalNumberBuffer = _BcamTraceLocalNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 15),
    _BcamTraceLocalNumberBuffer_Type()
)
bcamTraceLocalNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceLocalNumberBuffer.setStatus("mandatory")


class _BcamTraceLocalBufferLen_Type(Integer32):
    """Custom type bcamTraceLocalBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceLocalBufferLen_Type.__name__ = "Integer32"
_BcamTraceLocalBufferLen_Object = MibScalar
bcamTraceLocalBufferLen = _BcamTraceLocalBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 16),
    _BcamTraceLocalBufferLen_Type()
)
bcamTraceLocalBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceLocalBufferLen.setStatus("mandatory")


class _BcamTraceMappingState_Type(Integer32):
    """Custom type bcamTraceMappingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceMappingState_Type.__name__ = "Integer32"
_BcamTraceMappingState_Object = MibScalar
bcamTraceMappingState = _BcamTraceMappingState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 17),
    _BcamTraceMappingState_Type()
)
bcamTraceMappingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMappingState.setStatus("mandatory")


class _BcamTraceMappingNumberBuffer_Type(Integer32):
    """Custom type bcamTraceMappingNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceMappingNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceMappingNumberBuffer_Object = MibScalar
bcamTraceMappingNumberBuffer = _BcamTraceMappingNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 18),
    _BcamTraceMappingNumberBuffer_Type()
)
bcamTraceMappingNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMappingNumberBuffer.setStatus("mandatory")


class _BcamTraceMappingBufferLen_Type(Integer32):
    """Custom type bcamTraceMappingBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceMappingBufferLen_Type.__name__ = "Integer32"
_BcamTraceMappingBufferLen_Object = MibScalar
bcamTraceMappingBufferLen = _BcamTraceMappingBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 19),
    _BcamTraceMappingBufferLen_Type()
)
bcamTraceMappingBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMappingBufferLen.setStatus("mandatory")


class _BcamTraceMgmtState_Type(Integer32):
    """Custom type bcamTraceMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceMgmtState_Type.__name__ = "Integer32"
_BcamTraceMgmtState_Object = MibScalar
bcamTraceMgmtState = _BcamTraceMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 20),
    _BcamTraceMgmtState_Type()
)
bcamTraceMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMgmtState.setStatus("mandatory")


class _BcamTraceMgmtNumberBuffer_Type(Integer32):
    """Custom type bcamTraceMgmtNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceMgmtNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceMgmtNumberBuffer_Object = MibScalar
bcamTraceMgmtNumberBuffer = _BcamTraceMgmtNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 21),
    _BcamTraceMgmtNumberBuffer_Type()
)
bcamTraceMgmtNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMgmtNumberBuffer.setStatus("mandatory")


class _BcamTraceMgmtBufferLen_Type(Integer32):
    """Custom type bcamTraceMgmtBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceMgmtBufferLen_Type.__name__ = "Integer32"
_BcamTraceMgmtBufferLen_Object = MibScalar
bcamTraceMgmtBufferLen = _BcamTraceMgmtBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 22),
    _BcamTraceMgmtBufferLen_Type()
)
bcamTraceMgmtBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceMgmtBufferLen.setStatus("mandatory")


class _BcamTraceNetState_Type(Integer32):
    """Custom type bcamTraceNetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceNetState_Type.__name__ = "Integer32"
_BcamTraceNetState_Object = MibScalar
bcamTraceNetState = _BcamTraceNetState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 23),
    _BcamTraceNetState_Type()
)
bcamTraceNetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceNetState.setStatus("mandatory")


class _BcamTraceNetNumberBuffer_Type(Integer32):
    """Custom type bcamTraceNetNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceNetNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceNetNumberBuffer_Object = MibScalar
bcamTraceNetNumberBuffer = _BcamTraceNetNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 24),
    _BcamTraceNetNumberBuffer_Type()
)
bcamTraceNetNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceNetNumberBuffer.setStatus("mandatory")


class _BcamTraceNetBufferLen_Type(Integer32):
    """Custom type bcamTraceNetBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceNetBufferLen_Type.__name__ = "Integer32"
_BcamTraceNetBufferLen_Object = MibScalar
bcamTraceNetBufferLen = _BcamTraceNetBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 25),
    _BcamTraceNetBufferLen_Type()
)
bcamTraceNetBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceNetBufferLen.setStatus("mandatory")


class _BcamTraceSnmpState_Type(Integer32):
    """Custom type bcamTraceSnmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceSnmpState_Type.__name__ = "Integer32"
_BcamTraceSnmpState_Object = MibScalar
bcamTraceSnmpState = _BcamTraceSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 26),
    _BcamTraceSnmpState_Type()
)
bcamTraceSnmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceSnmpState.setStatus("mandatory")


class _BcamTraceSnmpNumberBuffer_Type(Integer32):
    """Custom type bcamTraceSnmpNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceSnmpNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceSnmpNumberBuffer_Object = MibScalar
bcamTraceSnmpNumberBuffer = _BcamTraceSnmpNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 27),
    _BcamTraceSnmpNumberBuffer_Type()
)
bcamTraceSnmpNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceSnmpNumberBuffer.setStatus("mandatory")


class _BcamTraceSnmpBufferLen_Type(Integer32):
    """Custom type bcamTraceSnmpBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceSnmpBufferLen_Type.__name__ = "Integer32"
_BcamTraceSnmpBufferLen_Object = MibScalar
bcamTraceSnmpBufferLen = _BcamTraceSnmpBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 28),
    _BcamTraceSnmpBufferLen_Type()
)
bcamTraceSnmpBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceSnmpBufferLen.setStatus("mandatory")


class _BcamTraceTransState_Type(Integer32):
    """Custom type bcamTraceTransState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceTransState_Type.__name__ = "Integer32"
_BcamTraceTransState_Object = MibScalar
bcamTraceTransState = _BcamTraceTransState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 29),
    _BcamTraceTransState_Type()
)
bcamTraceTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceTransState.setStatus("mandatory")


class _BcamTraceTransNumberBuffer_Type(Integer32):
    """Custom type bcamTraceTransNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceTransNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceTransNumberBuffer_Object = MibScalar
bcamTraceTransNumberBuffer = _BcamTraceTransNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 30),
    _BcamTraceTransNumberBuffer_Type()
)
bcamTraceTransNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceTransNumberBuffer.setStatus("mandatory")


class _BcamTraceTransBufferLen_Type(Integer32):
    """Custom type bcamTraceTransBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceTransBufferLen_Type.__name__ = "Integer32"
_BcamTraceTransBufferLen_Object = MibScalar
bcamTraceTransBufferLen = _BcamTraceTransBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 31),
    _BcamTraceTransBufferLen_Type()
)
bcamTraceTransBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceTransBufferLen.setStatus("mandatory")


class _BcamTraceInfoState_Type(Integer32):
    """Custom type bcamTraceInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamTraceInfoState_Type.__name__ = "Integer32"
_BcamTraceInfoState_Object = MibScalar
bcamTraceInfoState = _BcamTraceInfoState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 32),
    _BcamTraceInfoState_Type()
)
bcamTraceInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceInfoState.setStatus("mandatory")


class _BcamTraceInfoNumberBuffer_Type(Integer32):
    """Custom type bcamTraceInfoNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamTraceInfoNumberBuffer_Type.__name__ = "Integer32"
_BcamTraceInfoNumberBuffer_Object = MibScalar
bcamTraceInfoNumberBuffer = _BcamTraceInfoNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 33),
    _BcamTraceInfoNumberBuffer_Type()
)
bcamTraceInfoNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceInfoNumberBuffer.setStatus("mandatory")


class _BcamTraceInfoBufferLen_Type(Integer32):
    """Custom type bcamTraceInfoBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamTraceInfoBufferLen_Type.__name__ = "Integer32"
_BcamTraceInfoBufferLen_Object = MibScalar
bcamTraceInfoBufferLen = _BcamTraceInfoBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 4, 34),
    _BcamTraceInfoBufferLen_Type()
)
bcamTraceInfoBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTraceInfoBufferLen.setStatus("mandatory")
_BcamTsap_ObjectIdentity = ObjectIdentity
bcamTsap = _BcamTsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5)
)
_BcamTsapCurrOpen_Type = Integer32
_BcamTsapCurrOpen_Object = MibScalar
bcamTsapCurrOpen = _BcamTsapCurrOpen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 1),
    _BcamTsapCurrOpen_Type()
)
bcamTsapCurrOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapCurrOpen.setStatus("mandatory")
_BcamTsapTotOpen_Type = Integer32
_BcamTsapTotOpen_Object = MibScalar
bcamTsapTotOpen = _BcamTsapTotOpen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 2),
    _BcamTsapTotOpen_Type()
)
bcamTsapTotOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTotOpen.setStatus("mandatory")
_BcamTsapSendCall_Type = Integer32
_BcamTsapSendCall_Object = MibScalar
bcamTsapSendCall = _BcamTsapSendCall_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 3),
    _BcamTsapSendCall_Type()
)
bcamTsapSendCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapSendCall.setStatus("mandatory")
_BcamTsapSendByteHigh_Type = Integer32
_BcamTsapSendByteHigh_Object = MibScalar
bcamTsapSendByteHigh = _BcamTsapSendByteHigh_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 4),
    _BcamTsapSendByteHigh_Type()
)
bcamTsapSendByteHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapSendByteHigh.setStatus("mandatory")
_BcamTsapSendByteLow_Type = Integer32
_BcamTsapSendByteLow_Object = MibScalar
bcamTsapSendByteLow = _BcamTsapSendByteLow_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 5),
    _BcamTsapSendByteLow_Type()
)
bcamTsapSendByteLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapSendByteLow.setStatus("mandatory")
_BcamTsapRecvCall_Type = Integer32
_BcamTsapRecvCall_Object = MibScalar
bcamTsapRecvCall = _BcamTsapRecvCall_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 6),
    _BcamTsapRecvCall_Type()
)
bcamTsapRecvCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRecvCall.setStatus("mandatory")
_BcamTsapRecvByteHigh_Type = Integer32
_BcamTsapRecvByteHigh_Object = MibScalar
bcamTsapRecvByteHigh = _BcamTsapRecvByteHigh_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 7),
    _BcamTsapRecvByteHigh_Type()
)
bcamTsapRecvByteHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRecvByteHigh.setStatus("mandatory")
_BcamTsapRecvByteLow_Type = Integer32
_BcamTsapRecvByteLow_Object = MibScalar
bcamTsapRecvByteLow = _BcamTsapRecvByteLow_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 8),
    _BcamTsapRecvByteLow_Type()
)
bcamTsapRecvByteLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRecvByteLow.setStatus("mandatory")
_BcamTsapSendCallCless_Type = Integer32
_BcamTsapSendCallCless_Object = MibScalar
bcamTsapSendCallCless = _BcamTsapSendCallCless_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 9),
    _BcamTsapSendCallCless_Type()
)
bcamTsapSendCallCless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapSendCallCless.setStatus("mandatory")
_BcamTsapSendByteClessHigh_Type = Integer32
_BcamTsapSendByteClessHigh_Object = MibScalar
bcamTsapSendByteClessHigh = _BcamTsapSendByteClessHigh_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 10),
    _BcamTsapSendByteClessHigh_Type()
)
bcamTsapSendByteClessHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapSendByteClessHigh.setStatus("mandatory")
_BcamTsapSendByteClessLow_Type = Integer32
_BcamTsapSendByteClessLow_Object = MibScalar
bcamTsapSendByteClessLow = _BcamTsapSendByteClessLow_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 11),
    _BcamTsapSendByteClessLow_Type()
)
bcamTsapSendByteClessLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapSendByteClessLow.setStatus("mandatory")
_BcamTsapRecvCallCless_Type = Integer32
_BcamTsapRecvCallCless_Object = MibScalar
bcamTsapRecvCallCless = _BcamTsapRecvCallCless_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 12),
    _BcamTsapRecvCallCless_Type()
)
bcamTsapRecvCallCless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRecvCallCless.setStatus("mandatory")
_BcamTsapRecvByteClessHigh_Type = Integer32
_BcamTsapRecvByteClessHigh_Object = MibScalar
bcamTsapRecvByteClessHigh = _BcamTsapRecvByteClessHigh_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 13),
    _BcamTsapRecvByteClessHigh_Type()
)
bcamTsapRecvByteClessHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRecvByteClessHigh.setStatus("mandatory")
_BcamTsapRecvByteClessLow_Type = Integer32
_BcamTsapRecvByteClessLow_Object = MibScalar
bcamTsapRecvByteClessLow = _BcamTsapRecvByteClessLow_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 14),
    _BcamTsapRecvByteClessLow_Type()
)
bcamTsapRecvByteClessLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRecvByteClessLow.setStatus("mandatory")
_BcamTsapNumTable_Type = Integer32
_BcamTsapNumTable_Object = MibScalar
bcamTsapNumTable = _BcamTsapNumTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 15),
    _BcamTsapNumTable_Type()
)
bcamTsapNumTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapNumTable.setStatus("mandatory")
_BcamTsapMaxTsap_Type = Integer32
_BcamTsapMaxTsap_Object = MibScalar
bcamTsapMaxTsap = _BcamTsapMaxTsap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 16),
    _BcamTsapMaxTsap_Type()
)
bcamTsapMaxTsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapMaxTsap.setStatus("mandatory")
_BcamTsapMaxTsapTask_Type = Integer32
_BcamTsapMaxTsapTask_Object = MibScalar
bcamTsapMaxTsapTask = _BcamTsapMaxTsapTask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 17),
    _BcamTsapMaxTsapTask_Type()
)
bcamTsapMaxTsapTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapMaxTsapTask.setStatus("mandatory")
_BcamTsapMaxCepTsap_Type = Integer32
_BcamTsapMaxCepTsap_Object = MibScalar
bcamTsapMaxCepTsap = _BcamTsapMaxCepTsap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 18),
    _BcamTsapMaxCepTsap_Type()
)
bcamTsapMaxCepTsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapMaxCepTsap.setStatus("mandatory")
_BcamTsapRejTsap_Type = Integer32
_BcamTsapRejTsap_Object = MibScalar
bcamTsapRejTsap = _BcamTsapRejTsap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 19),
    _BcamTsapRejTsap_Type()
)
bcamTsapRejTsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRejTsap.setStatus("mandatory")
_BcamTsapRejTsapTask_Type = Integer32
_BcamTsapRejTsapTask_Object = MibScalar
bcamTsapRejTsapTask = _BcamTsapRejTsapTask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 20),
    _BcamTsapRejTsapTask_Type()
)
bcamTsapRejTsapTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRejTsapTask.setStatus("mandatory")
_BcamTsapRejCepTsap_Type = Integer32
_BcamTsapRejCepTsap_Object = MibScalar
bcamTsapRejCepTsap = _BcamTsapRejCepTsap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 21),
    _BcamTsapRejCepTsap_Type()
)
bcamTsapRejCepTsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapRejCepTsap.setStatus("mandatory")
_BcamTsapTab_Object = MibTable
bcamTsapTab = _BcamTsapTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22)
)
if mibBuilder.loadTexts:
    bcamTsapTab.setStatus("mandatory")
_BcamTsapTabEntry_Object = MibTableRow
bcamTsapTabEntry = _BcamTsapTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1)
)
bcamTsapTabEntry.setIndexNames(
    (0, "BCAM-MIB", "bcamTsapTabNumbers"),
)
if mibBuilder.loadTexts:
    bcamTsapTabEntry.setStatus("mandatory")
_BcamTsapTabNumbers_Type = Counter32
_BcamTsapTabNumbers_Object = MibTableColumn
bcamTsapTabNumbers = _BcamTsapTabNumbers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 1),
    _BcamTsapTabNumbers_Type()
)
bcamTsapTabNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabNumbers.setStatus("mandatory")


class _BcamTsapTabState_Type(Integer32):
    """Custom type bcamTsapTabState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("closed", 4),
          ("closing", 3),
          ("open", 2),
          ("opening", 1),
          ("stopped", 8))
    )


_BcamTsapTabState_Type.__name__ = "Integer32"
_BcamTsapTabState_Object = MibTableColumn
bcamTsapTabState = _BcamTsapTabState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 2),
    _BcamTsapTabState_Type()
)
bcamTsapTabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabState.setStatus("mandatory")
_BcamTsapTabDuration_Type = Gauge32
_BcamTsapTabDuration_Object = MibTableColumn
bcamTsapTabDuration = _BcamTsapTabDuration_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 3),
    _BcamTsapTabDuration_Type()
)
bcamTsapTabDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabDuration.setStatus("mandatory")


class _BcamTsapTabDateApplEnable_Type(DisplayString):
    """Custom type bcamTsapTabDateApplEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamTsapTabDateApplEnable_Type.__name__ = "DisplayString"
_BcamTsapTabDateApplEnable_Object = MibTableColumn
bcamTsapTabDateApplEnable = _BcamTsapTabDateApplEnable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 4),
    _BcamTsapTabDateApplEnable_Type()
)
bcamTsapTabDateApplEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabDateApplEnable.setStatus("mandatory")


class _BcamTsapTabTimeApplEnable_Type(DisplayString):
    """Custom type bcamTsapTabTimeApplEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BcamTsapTabTimeApplEnable_Type.__name__ = "DisplayString"
_BcamTsapTabTimeApplEnable_Object = MibTableColumn
bcamTsapTabTimeApplEnable = _BcamTsapTabTimeApplEnable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 5),
    _BcamTsapTabTimeApplEnable_Type()
)
bcamTsapTabTimeApplEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabTimeApplEnable.setStatus("mandatory")


class _BcamTsapTabTypName_Type(Integer32):
    """Custom type bcamTsapTabTypName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isoName", 3),
          ("neaName", 1),
          ("socketName", 2))
    )


_BcamTsapTabTypName_Type.__name__ = "Integer32"
_BcamTsapTabTypName_Object = MibTableColumn
bcamTsapTabTypName = _BcamTsapTabTypName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 6),
    _BcamTsapTabTypName_Type()
)
bcamTsapTabTypName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabTypName.setStatus("mandatory")


class _BcamTsapTabName_Type(DisplayString):
    """Custom type bcamTsapTabName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_BcamTsapTabName_Type.__name__ = "DisplayString"
_BcamTsapTabName_Object = MibTableColumn
bcamTsapTabName = _BcamTsapTabName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 7),
    _BcamTsapTabName_Type()
)
bcamTsapTabName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabName.setStatus("mandatory")


class _BcamTsapTabPortnumber_Type(Integer32):
    """Custom type bcamTsapTabPortnumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabPortnumber_Type.__name__ = "Integer32"
_BcamTsapTabPortnumber_Object = MibTableColumn
bcamTsapTabPortnumber = _BcamTsapTabPortnumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 8),
    _BcamTsapTabPortnumber_Type()
)
bcamTsapTabPortnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabPortnumber.setStatus("mandatory")


class _BcamTsapTabOsiTsel_Type(OctetString):
    """Custom type bcamTsapTabOsiTsel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcamTsapTabOsiTsel_Type.__name__ = "OctetString"
_BcamTsapTabOsiTsel_Object = MibTableColumn
bcamTsapTabOsiTsel = _BcamTsapTabOsiTsel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 9),
    _BcamTsapTabOsiTsel_Type()
)
bcamTsapTabOsiTsel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabOsiTsel.setStatus("mandatory")


class _BcamTsapTabNeaTsel_Type(OctetString):
    """Custom type bcamTsapTabNeaTsel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamTsapTabNeaTsel_Type.__name__ = "OctetString"
_BcamTsapTabNeaTsel_Object = MibTableColumn
bcamTsapTabNeaTsel = _BcamTsapTabNeaTsel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 10),
    _BcamTsapTabNeaTsel_Type()
)
bcamTsapTabNeaTsel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabNeaTsel.setStatus("mandatory")


class _BcamTsapTabHost_Type(DisplayString):
    """Custom type bcamTsapTabHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamTsapTabHost_Type.__name__ = "DisplayString"
_BcamTsapTabHost_Object = MibTableColumn
bcamTsapTabHost = _BcamTsapTabHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 11),
    _BcamTsapTabHost_Type()
)
bcamTsapTabHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabHost.setStatus("mandatory")


class _BcamTsapTabDiagnostic_Type(OctetString):
    """Custom type bcamTsapTabDiagnostic based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BcamTsapTabDiagnostic_Type.__name__ = "OctetString"
_BcamTsapTabDiagnostic_Object = MibTableColumn
bcamTsapTabDiagnostic = _BcamTsapTabDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 12),
    _BcamTsapTabDiagnostic_Type()
)
bcamTsapTabDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabDiagnostic.setStatus("mandatory")
_BcamTsapTabTsduSends_Type = Counter32
_BcamTsapTabTsduSends_Object = MibTableColumn
bcamTsapTabTsduSends = _BcamTsapTabTsduSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 13),
    _BcamTsapTabTsduSends_Type()
)
bcamTsapTabTsduSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabTsduSends.setStatus("mandatory")
_BcamTsapTabByteSends_Type = Counter32
_BcamTsapTabByteSends_Object = MibTableColumn
bcamTsapTabByteSends = _BcamTsapTabByteSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 14),
    _BcamTsapTabByteSends_Type()
)
bcamTsapTabByteSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabByteSends.setStatus("mandatory")
_BcamTsapTabTsduReceiveds_Type = Counter32
_BcamTsapTabTsduReceiveds_Object = MibTableColumn
bcamTsapTabTsduReceiveds = _BcamTsapTabTsduReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 15),
    _BcamTsapTabTsduReceiveds_Type()
)
bcamTsapTabTsduReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabTsduReceiveds.setStatus("mandatory")
_BcamTsapTabByteReceiveds_Type = Counter32
_BcamTsapTabByteReceiveds_Object = MibTableColumn
bcamTsapTabByteReceiveds = _BcamTsapTabByteReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 16),
    _BcamTsapTabByteReceiveds_Type()
)
bcamTsapTabByteReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabByteReceiveds.setStatus("mandatory")
_BcamTsapTabSendCallOverMaxs_Type = Counter32
_BcamTsapTabSendCallOverMaxs_Object = MibTableColumn
bcamTsapTabSendCallOverMaxs = _BcamTsapTabSendCallOverMaxs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 17),
    _BcamTsapTabSendCallOverMaxs_Type()
)
bcamTsapTabSendCallOverMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabSendCallOverMaxs.setStatus("mandatory")
_BcamTsapTabLetterTimeouts_Type = Counter32
_BcamTsapTabLetterTimeouts_Object = MibTableColumn
bcamTsapTabLetterTimeouts = _BcamTsapTabLetterTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 18),
    _BcamTsapTabLetterTimeouts_Type()
)
bcamTsapTabLetterTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabLetterTimeouts.setStatus("mandatory")


class _BcamTsapTabInWaitBuck1Hist_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck1Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck1Hist_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck1Hist_Object = MibTableColumn
bcamTsapTabInWaitBuck1Hist = _BcamTsapTabInWaitBuck1Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 19),
    _BcamTsapTabInWaitBuck1Hist_Type()
)
bcamTsapTabInWaitBuck1Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck1Hist.setStatus("mandatory")


class _BcamTsapTabInWaitBuck2Hist_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck2Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck2Hist_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck2Hist_Object = MibTableColumn
bcamTsapTabInWaitBuck2Hist = _BcamTsapTabInWaitBuck2Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 20),
    _BcamTsapTabInWaitBuck2Hist_Type()
)
bcamTsapTabInWaitBuck2Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck2Hist.setStatus("mandatory")


class _BcamTsapTabInWaitBuck3Hist_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck3Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck3Hist_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck3Hist_Object = MibTableColumn
bcamTsapTabInWaitBuck3Hist = _BcamTsapTabInWaitBuck3Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 21),
    _BcamTsapTabInWaitBuck3Hist_Type()
)
bcamTsapTabInWaitBuck3Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck3Hist.setStatus("mandatory")


class _BcamTsapTabInWaitBuck4Hist_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck4Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck4Hist_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck4Hist_Object = MibTableColumn
bcamTsapTabInWaitBuck4Hist = _BcamTsapTabInWaitBuck4Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 22),
    _BcamTsapTabInWaitBuck4Hist_Type()
)
bcamTsapTabInWaitBuck4Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck4Hist.setStatus("mandatory")


class _BcamTsapTabInWaitBuck5Hist_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck5Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck5Hist_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck5Hist_Object = MibTableColumn
bcamTsapTabInWaitBuck5Hist = _BcamTsapTabInWaitBuck5Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 23),
    _BcamTsapTabInWaitBuck5Hist_Type()
)
bcamTsapTabInWaitBuck5Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck5Hist.setStatus("mandatory")


class _BcamTsapTabReactBuck1Hist_Type(Integer32):
    """Custom type bcamTsapTabReactBuck1Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck1Hist_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck1Hist_Object = MibTableColumn
bcamTsapTabReactBuck1Hist = _BcamTsapTabReactBuck1Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 24),
    _BcamTsapTabReactBuck1Hist_Type()
)
bcamTsapTabReactBuck1Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck1Hist.setStatus("mandatory")


class _BcamTsapTabReactBuck2Hist_Type(Integer32):
    """Custom type bcamTsapTabReactBuck2Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck2Hist_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck2Hist_Object = MibTableColumn
bcamTsapTabReactBuck2Hist = _BcamTsapTabReactBuck2Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 25),
    _BcamTsapTabReactBuck2Hist_Type()
)
bcamTsapTabReactBuck2Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck2Hist.setStatus("mandatory")


class _BcamTsapTabReactBuck3Hist_Type(Integer32):
    """Custom type bcamTsapTabReactBuck3Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck3Hist_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck3Hist_Object = MibTableColumn
bcamTsapTabReactBuck3Hist = _BcamTsapTabReactBuck3Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 26),
    _BcamTsapTabReactBuck3Hist_Type()
)
bcamTsapTabReactBuck3Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck3Hist.setStatus("mandatory")


class _BcamTsapTabReactBuck4Hist_Type(Integer32):
    """Custom type bcamTsapTabReactBuck4Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck4Hist_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck4Hist_Object = MibTableColumn
bcamTsapTabReactBuck4Hist = _BcamTsapTabReactBuck4Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 27),
    _BcamTsapTabReactBuck4Hist_Type()
)
bcamTsapTabReactBuck4Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck4Hist.setStatus("mandatory")


class _BcamTsapTabReactBuck5Hist_Type(Integer32):
    """Custom type bcamTsapTabReactBuck5Hist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck5Hist_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck5Hist_Object = MibTableColumn
bcamTsapTabReactBuck5Hist = _BcamTsapTabReactBuck5Hist_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 28),
    _BcamTsapTabReactBuck5Hist_Type()
)
bcamTsapTabReactBuck5Hist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck5Hist.setStatus("mandatory")


class _BcamTsapTabInWaitBuck1_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck1_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck1_Object = MibTableColumn
bcamTsapTabInWaitBuck1 = _BcamTsapTabInWaitBuck1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 29),
    _BcamTsapTabInWaitBuck1_Type()
)
bcamTsapTabInWaitBuck1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck1.setStatus("mandatory")


class _BcamTsapTabInWaitBuck2_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck2_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck2_Object = MibTableColumn
bcamTsapTabInWaitBuck2 = _BcamTsapTabInWaitBuck2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 30),
    _BcamTsapTabInWaitBuck2_Type()
)
bcamTsapTabInWaitBuck2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck2.setStatus("mandatory")


class _BcamTsapTabInWaitBuck3_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck3_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck3_Object = MibTableColumn
bcamTsapTabInWaitBuck3 = _BcamTsapTabInWaitBuck3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 31),
    _BcamTsapTabInWaitBuck3_Type()
)
bcamTsapTabInWaitBuck3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck3.setStatus("mandatory")


class _BcamTsapTabInWaitBuck4_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck4_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck4_Object = MibTableColumn
bcamTsapTabInWaitBuck4 = _BcamTsapTabInWaitBuck4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 32),
    _BcamTsapTabInWaitBuck4_Type()
)
bcamTsapTabInWaitBuck4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck4.setStatus("mandatory")


class _BcamTsapTabInWaitBuck5_Type(Integer32):
    """Custom type bcamTsapTabInWaitBuck5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabInWaitBuck5_Type.__name__ = "Integer32"
_BcamTsapTabInWaitBuck5_Object = MibTableColumn
bcamTsapTabInWaitBuck5 = _BcamTsapTabInWaitBuck5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 33),
    _BcamTsapTabInWaitBuck5_Type()
)
bcamTsapTabInWaitBuck5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInWaitBuck5.setStatus("mandatory")


class _BcamTsapTabReactBuck1_Type(Integer32):
    """Custom type bcamTsapTabReactBuck1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck1_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck1_Object = MibTableColumn
bcamTsapTabReactBuck1 = _BcamTsapTabReactBuck1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 34),
    _BcamTsapTabReactBuck1_Type()
)
bcamTsapTabReactBuck1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck1.setStatus("mandatory")


class _BcamTsapTabReactBuck2_Type(Integer32):
    """Custom type bcamTsapTabReactBuck2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck2_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck2_Object = MibTableColumn
bcamTsapTabReactBuck2 = _BcamTsapTabReactBuck2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 35),
    _BcamTsapTabReactBuck2_Type()
)
bcamTsapTabReactBuck2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck2.setStatus("mandatory")


class _BcamTsapTabReactBuck3_Type(Integer32):
    """Custom type bcamTsapTabReactBuck3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck3_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck3_Object = MibTableColumn
bcamTsapTabReactBuck3 = _BcamTsapTabReactBuck3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 36),
    _BcamTsapTabReactBuck3_Type()
)
bcamTsapTabReactBuck3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck3.setStatus("mandatory")


class _BcamTsapTabReactBuck4_Type(Integer32):
    """Custom type bcamTsapTabReactBuck4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck4_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck4_Object = MibTableColumn
bcamTsapTabReactBuck4 = _BcamTsapTabReactBuck4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 37),
    _BcamTsapTabReactBuck4_Type()
)
bcamTsapTabReactBuck4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck4.setStatus("mandatory")


class _BcamTsapTabReactBuck5_Type(Integer32):
    """Custom type bcamTsapTabReactBuck5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamTsapTabReactBuck5_Type.__name__ = "Integer32"
_BcamTsapTabReactBuck5_Object = MibTableColumn
bcamTsapTabReactBuck5 = _BcamTsapTabReactBuck5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 38),
    _BcamTsapTabReactBuck5_Type()
)
bcamTsapTabReactBuck5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabReactBuck5.setStatus("mandatory")
_BcamTsapTabTsduSendHists_Type = Counter32
_BcamTsapTabTsduSendHists_Object = MibTableColumn
bcamTsapTabTsduSendHists = _BcamTsapTabTsduSendHists_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 39),
    _BcamTsapTabTsduSendHists_Type()
)
bcamTsapTabTsduSendHists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabTsduSendHists.setStatus("mandatory")
_BcamTsapTabByteSendHists_Type = Counter32
_BcamTsapTabByteSendHists_Object = MibTableColumn
bcamTsapTabByteSendHists = _BcamTsapTabByteSendHists_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 40),
    _BcamTsapTabByteSendHists_Type()
)
bcamTsapTabByteSendHists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabByteSendHists.setStatus("mandatory")
_BcamTsapTabTsduReceivedHists_Type = Counter32
_BcamTsapTabTsduReceivedHists_Object = MibTableColumn
bcamTsapTabTsduReceivedHists = _BcamTsapTabTsduReceivedHists_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 41),
    _BcamTsapTabTsduReceivedHists_Type()
)
bcamTsapTabTsduReceivedHists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabTsduReceivedHists.setStatus("mandatory")
_BcamTsapTabByteReceivedHists_Type = Counter32
_BcamTsapTabByteReceivedHists_Object = MibTableColumn
bcamTsapTabByteReceivedHists = _BcamTsapTabByteReceivedHists_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 42),
    _BcamTsapTabByteReceivedHists_Type()
)
bcamTsapTabByteReceivedHists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabByteReceivedHists.setStatus("mandatory")
_BcamTsapTabSendCallOverMaxHists_Type = Counter32
_BcamTsapTabSendCallOverMaxHists_Object = MibTableColumn
bcamTsapTabSendCallOverMaxHists = _BcamTsapTabSendCallOverMaxHists_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 43),
    _BcamTsapTabSendCallOverMaxHists_Type()
)
bcamTsapTabSendCallOverMaxHists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabSendCallOverMaxHists.setStatus("mandatory")
_BcamTsapTabLetterTimeoutHists_Type = Counter32
_BcamTsapTabLetterTimeoutHists_Object = MibTableColumn
bcamTsapTabLetterTimeoutHists = _BcamTsapTabLetterTimeoutHists_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 44),
    _BcamTsapTabLetterTimeoutHists_Type()
)
bcamTsapTabLetterTimeoutHists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabLetterTimeoutHists.setStatus("mandatory")


class _BcamTsapTabFunction_Type(Integer32):
    """Custom type bcamTsapTabFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iso", 2),
          ("nea", 1),
          ("streams", 3))
    )


_BcamTsapTabFunction_Type.__name__ = "Integer32"
_BcamTsapTabFunction_Object = MibTableColumn
bcamTsapTabFunction = _BcamTsapTabFunction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 45),
    _BcamTsapTabFunction_Type()
)
bcamTsapTabFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabFunction.setStatus("mandatory")
_BcamTsapTabCurrConn_Type = Gauge32
_BcamTsapTabCurrConn_Object = MibTableColumn
bcamTsapTabCurrConn = _BcamTsapTabCurrConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 46),
    _BcamTsapTabCurrConn_Type()
)
bcamTsapTabCurrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabCurrConn.setStatus("mandatory")
_BcamTsapTabCloseConns_Type = Counter32
_BcamTsapTabCloseConns_Object = MibTableColumn
bcamTsapTabCloseConns = _BcamTsapTabCloseConns_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 47),
    _BcamTsapTabCloseConns_Type()
)
bcamTsapTabCloseConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabCloseConns.setStatus("mandatory")
_BcamTsapTabClessSendBytes_Type = Counter32
_BcamTsapTabClessSendBytes_Object = MibTableColumn
bcamTsapTabClessSendBytes = _BcamTsapTabClessSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 48),
    _BcamTsapTabClessSendBytes_Type()
)
bcamTsapTabClessSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabClessSendBytes.setStatus("mandatory")
_BcamTsapTabClessRecvBytes_Type = Counter32
_BcamTsapTabClessRecvBytes_Object = MibTableColumn
bcamTsapTabClessRecvBytes = _BcamTsapTabClessRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 49),
    _BcamTsapTabClessRecvBytes_Type()
)
bcamTsapTabClessRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabClessRecvBytes.setStatus("mandatory")
_BcamTsapTabClessSendCalls_Type = Counter32
_BcamTsapTabClessSendCalls_Object = MibTableColumn
bcamTsapTabClessSendCalls = _BcamTsapTabClessSendCalls_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 50),
    _BcamTsapTabClessSendCalls_Type()
)
bcamTsapTabClessSendCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabClessSendCalls.setStatus("mandatory")
_BcamTsapTabClessRecvCalls_Type = Counter32
_BcamTsapTabClessRecvCalls_Object = MibTableColumn
bcamTsapTabClessRecvCalls = _BcamTsapTabClessRecvCalls_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 51),
    _BcamTsapTabClessRecvCalls_Type()
)
bcamTsapTabClessRecvCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabClessRecvCalls.setStatus("mandatory")
_BcamTsapTabOutbufTsdu_Type = Gauge32
_BcamTsapTabOutbufTsdu_Object = MibTableColumn
bcamTsapTabOutbufTsdu = _BcamTsapTabOutbufTsdu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 52),
    _BcamTsapTabOutbufTsdu_Type()
)
bcamTsapTabOutbufTsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabOutbufTsdu.setStatus("mandatory")
_BcamTsapTabOutbufByte_Type = Gauge32
_BcamTsapTabOutbufByte_Object = MibTableColumn
bcamTsapTabOutbufByte = _BcamTsapTabOutbufByte_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 53),
    _BcamTsapTabOutbufByte_Type()
)
bcamTsapTabOutbufByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabOutbufByte.setStatus("mandatory")
_BcamTsapTabInbufTsdu_Type = Gauge32
_BcamTsapTabInbufTsdu_Object = MibTableColumn
bcamTsapTabInbufTsdu = _BcamTsapTabInbufTsdu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 54),
    _BcamTsapTabInbufTsdu_Type()
)
bcamTsapTabInbufTsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInbufTsdu.setStatus("mandatory")
_BcamTsapTabInbufByte_Type = Gauge32
_BcamTsapTabInbufByte_Object = MibTableColumn
bcamTsapTabInbufByte = _BcamTsapTabInbufByte_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 55),
    _BcamTsapTabInbufByte_Type()
)
bcamTsapTabInbufByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInbufByte.setStatus("mandatory")
_BcamTsapTabOutbufTsduCless_Type = Gauge32
_BcamTsapTabOutbufTsduCless_Object = MibTableColumn
bcamTsapTabOutbufTsduCless = _BcamTsapTabOutbufTsduCless_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 56),
    _BcamTsapTabOutbufTsduCless_Type()
)
bcamTsapTabOutbufTsduCless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabOutbufTsduCless.setStatus("mandatory")
_BcamTsapTabOutbufByteCless_Type = Gauge32
_BcamTsapTabOutbufByteCless_Object = MibTableColumn
bcamTsapTabOutbufByteCless = _BcamTsapTabOutbufByteCless_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 57),
    _BcamTsapTabOutbufByteCless_Type()
)
bcamTsapTabOutbufByteCless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabOutbufByteCless.setStatus("mandatory")
_BcamTsapTabInbufTsduCless_Type = Gauge32
_BcamTsapTabInbufTsduCless_Object = MibTableColumn
bcamTsapTabInbufTsduCless = _BcamTsapTabInbufTsduCless_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 58),
    _BcamTsapTabInbufTsduCless_Type()
)
bcamTsapTabInbufTsduCless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInbufTsduCless.setStatus("mandatory")
_BcamTsapTabInbufByteCless_Type = Gauge32
_BcamTsapTabInbufByteCless_Object = MibTableColumn
bcamTsapTabInbufByteCless = _BcamTsapTabInbufByteCless_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 59),
    _BcamTsapTabInbufByteCless_Type()
)
bcamTsapTabInbufByteCless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabInbufByteCless.setStatus("mandatory")
_BcamTsapTabClessTimeout_Type = Integer32
_BcamTsapTabClessTimeout_Object = MibTableColumn
bcamTsapTabClessTimeout = _BcamTsapTabClessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 5, 22, 1, 60),
    _BcamTsapTabClessTimeout_Type()
)
bcamTsapTabClessTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamTsapTabClessTimeout.setStatus("mandatory")
_BcamCep_ObjectIdentity = ObjectIdentity
bcamCep = _BcamCep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6)
)
_BcamCepCurrent_Type = Integer32
_BcamCepCurrent_Object = MibScalar
bcamCepCurrent = _BcamCepCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 1),
    _BcamCepCurrent_Type()
)
bcamCepCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepCurrent.setStatus("mandatory")
_BcamCepClosed_Type = Integer32
_BcamCepClosed_Object = MibScalar
bcamCepClosed = _BcamCepClosed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 2),
    _BcamCepClosed_Type()
)
bcamCepClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepClosed.setStatus("mandatory")
_BcamCepNotClosed_Type = Integer32
_BcamCepNotClosed_Object = MibScalar
bcamCepNotClosed = _BcamCepNotClosed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 3),
    _BcamCepNotClosed_Type()
)
bcamCepNotClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepNotClosed.setStatus("mandatory")
_BcamCepRerouting_Type = Integer32
_BcamCepRerouting_Object = MibScalar
bcamCepRerouting = _BcamCepRerouting_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 4),
    _BcamCepRerouting_Type()
)
bcamCepRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepRerouting.setStatus("mandatory")
_BcamCepActiveTrials_Type = Counter32
_BcamCepActiveTrials_Object = MibScalar
bcamCepActiveTrials = _BcamCepActiveTrials_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 5),
    _BcamCepActiveTrials_Type()
)
bcamCepActiveTrials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepActiveTrials.setStatus("mandatory")
_BcamCepActiveTrialFailures_Type = Counter32
_BcamCepActiveTrialFailures_Object = MibScalar
bcamCepActiveTrialFailures = _BcamCepActiveTrialFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 6),
    _BcamCepActiveTrialFailures_Type()
)
bcamCepActiveTrialFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepActiveTrialFailures.setStatus("mandatory")
_BcamCepPassiveTrials_Type = Counter32
_BcamCepPassiveTrials_Object = MibScalar
bcamCepPassiveTrials = _BcamCepPassiveTrials_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 7),
    _BcamCepPassiveTrials_Type()
)
bcamCepPassiveTrials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepPassiveTrials.setStatus("mandatory")
_BcamCepPassiveTrialFailures_Type = Counter32
_BcamCepPassiveTrialFailures_Object = MibScalar
bcamCepPassiveTrialFailures = _BcamCepPassiveTrialFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 8),
    _BcamCepPassiveTrialFailures_Type()
)
bcamCepPassiveTrialFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepPassiveTrialFailures.setStatus("mandatory")
_BcamCepNumTable_Type = Integer32
_BcamCepNumTable_Object = MibScalar
bcamCepNumTable = _BcamCepNumTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 9),
    _BcamCepNumTable_Type()
)
bcamCepNumTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepNumTable.setStatus("mandatory")
_BcamCepTab_Object = MibTable
bcamCepTab = _BcamCepTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10)
)
if mibBuilder.loadTexts:
    bcamCepTab.setStatus("mandatory")
_BcamCepTabEntry_Object = MibTableRow
bcamCepTabEntry = _BcamCepTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1)
)
bcamCepTabEntry.setIndexNames(
    (0, "BCAM-MIB", "bcamCepTabConnectionNumbers"),
)
if mibBuilder.loadTexts:
    bcamCepTabEntry.setStatus("mandatory")


class _BcamCepTabProtocolClass_Type(Integer32):
    """Custom type bcamCepTabProtocolClass based on Integer32"""
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
        *(("iso", 3),
          ("local", 1),
          ("nea", 2),
          ("tcp", 4))
    )


_BcamCepTabProtocolClass_Type.__name__ = "Integer32"
_BcamCepTabProtocolClass_Object = MibTableColumn
bcamCepTabProtocolClass = _BcamCepTabProtocolClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 1),
    _BcamCepTabProtocolClass_Type()
)
bcamCepTabProtocolClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabProtocolClass.setStatus("mandatory")
_BcamCepTabConnectionNumbers_Type = Counter32
_BcamCepTabConnectionNumbers_Object = MibTableColumn
bcamCepTabConnectionNumbers = _BcamCepTabConnectionNumbers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 2),
    _BcamCepTabConnectionNumbers_Type()
)
bcamCepTabConnectionNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabConnectionNumbers.setStatus("mandatory")


class _BcamCepTabDisconCommand_Type(OctetString):
    """Custom type bcamCepTabDisconCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BcamCepTabDisconCommand_Type.__name__ = "OctetString"
_BcamCepTabDisconCommand_Object = MibTableColumn
bcamCepTabDisconCommand = _BcamCepTabDisconCommand_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 3),
    _BcamCepTabDisconCommand_Type()
)
bcamCepTabDisconCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabDisconCommand.setStatus("mandatory")


class _BcamCepTabDisconInfoWord_Type(OctetString):
    """Custom type bcamCepTabDisconInfoWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BcamCepTabDisconInfoWord_Type.__name__ = "OctetString"
_BcamCepTabDisconInfoWord_Object = MibTableColumn
bcamCepTabDisconInfoWord = _BcamCepTabDisconInfoWord_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 4),
    _BcamCepTabDisconInfoWord_Type()
)
bcamCepTabDisconInfoWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabDisconInfoWord.setStatus("mandatory")
_BcamCepTabTsduSends_Type = Counter32
_BcamCepTabTsduSends_Object = MibTableColumn
bcamCepTabTsduSends = _BcamCepTabTsduSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 5),
    _BcamCepTabTsduSends_Type()
)
bcamCepTabTsduSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabTsduSends.setStatus("mandatory")
_BcamCepTabByteSends_Type = Counter32
_BcamCepTabByteSends_Object = MibTableColumn
bcamCepTabByteSends = _BcamCepTabByteSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 6),
    _BcamCepTabByteSends_Type()
)
bcamCepTabByteSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabByteSends.setStatus("mandatory")
_BcamCepTabTsduReceiveds_Type = Counter32
_BcamCepTabTsduReceiveds_Object = MibTableColumn
bcamCepTabTsduReceiveds = _BcamCepTabTsduReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 7),
    _BcamCepTabTsduReceiveds_Type()
)
bcamCepTabTsduReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabTsduReceiveds.setStatus("mandatory")
_BcamCepTabByteReceiveds_Type = Counter32
_BcamCepTabByteReceiveds_Object = MibTableColumn
bcamCepTabByteReceiveds = _BcamCepTabByteReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 8),
    _BcamCepTabByteReceiveds_Type()
)
bcamCepTabByteReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabByteReceiveds.setStatus("mandatory")
_BcamCepTabSendCallOverMaxs_Type = Counter32
_BcamCepTabSendCallOverMaxs_Object = MibTableColumn
bcamCepTabSendCallOverMaxs = _BcamCepTabSendCallOverMaxs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 9),
    _BcamCepTabSendCallOverMaxs_Type()
)
bcamCepTabSendCallOverMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabSendCallOverMaxs.setStatus("mandatory")
_BcamCepTabLetterTimeouts_Type = Counter32
_BcamCepTabLetterTimeouts_Object = MibTableColumn
bcamCepTabLetterTimeouts = _BcamCepTabLetterTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 10),
    _BcamCepTabLetterTimeouts_Type()
)
bcamCepTabLetterTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabLetterTimeouts.setStatus("mandatory")
_BcamCepTabOutbufTsduSend_Type = Gauge32
_BcamCepTabOutbufTsduSend_Object = MibTableColumn
bcamCepTabOutbufTsduSend = _BcamCepTabOutbufTsduSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 11),
    _BcamCepTabOutbufTsduSend_Type()
)
bcamCepTabOutbufTsduSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutbufTsduSend.setStatus("mandatory")
_BcamCepTabOutbufByteSend_Type = Gauge32
_BcamCepTabOutbufByteSend_Object = MibTableColumn
bcamCepTabOutbufByteSend = _BcamCepTabOutbufByteSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 12),
    _BcamCepTabOutbufByteSend_Type()
)
bcamCepTabOutbufByteSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutbufByteSend.setStatus("mandatory")
_BcamCepTabOutbufMaxTsduSend_Type = Gauge32
_BcamCepTabOutbufMaxTsduSend_Object = MibTableColumn
bcamCepTabOutbufMaxTsduSend = _BcamCepTabOutbufMaxTsduSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 13),
    _BcamCepTabOutbufMaxTsduSend_Type()
)
bcamCepTabOutbufMaxTsduSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutbufMaxTsduSend.setStatus("mandatory")
_BcamCepTabOutbufMaxByteSend_Type = Gauge32
_BcamCepTabOutbufMaxByteSend_Object = MibTableColumn
bcamCepTabOutbufMaxByteSend = _BcamCepTabOutbufMaxByteSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 14),
    _BcamCepTabOutbufMaxByteSend_Type()
)
bcamCepTabOutbufMaxByteSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutbufMaxByteSend.setStatus("mandatory")
_BcamCepTabInbufTsdu_Type = Gauge32
_BcamCepTabInbufTsdu_Object = MibTableColumn
bcamCepTabInbufTsdu = _BcamCepTabInbufTsdu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 15),
    _BcamCepTabInbufTsdu_Type()
)
bcamCepTabInbufTsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInbufTsdu.setStatus("mandatory")
_BcamCepTabInbufByte_Type = Gauge32
_BcamCepTabInbufByte_Object = MibTableColumn
bcamCepTabInbufByte = _BcamCepTabInbufByte_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 16),
    _BcamCepTabInbufByte_Type()
)
bcamCepTabInbufByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInbufByte.setStatus("mandatory")
_BcamCepTabInbufMaxTsduReceived_Type = Gauge32
_BcamCepTabInbufMaxTsduReceived_Object = MibTableColumn
bcamCepTabInbufMaxTsduReceived = _BcamCepTabInbufMaxTsduReceived_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 17),
    _BcamCepTabInbufMaxTsduReceived_Type()
)
bcamCepTabInbufMaxTsduReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInbufMaxTsduReceived.setStatus("mandatory")
_BcamCepTabInbufMaxByteReceived_Type = Gauge32
_BcamCepTabInbufMaxByteReceived_Object = MibTableColumn
bcamCepTabInbufMaxByteReceived = _BcamCepTabInbufMaxByteReceived_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 18),
    _BcamCepTabInbufMaxByteReceived_Type()
)
bcamCepTabInbufMaxByteReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInbufMaxByteReceived.setStatus("mandatory")
_BcamCepTabPacketsDataSends_Type = Counter32
_BcamCepTabPacketsDataSends_Object = MibTableColumn
bcamCepTabPacketsDataSends = _BcamCepTabPacketsDataSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 19),
    _BcamCepTabPacketsDataSends_Type()
)
bcamCepTabPacketsDataSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabPacketsDataSends.setStatus("mandatory")
_BcamCepTabPacketsWindowSends_Type = Counter32
_BcamCepTabPacketsWindowSends_Object = MibTableColumn
bcamCepTabPacketsWindowSends = _BcamCepTabPacketsWindowSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 20),
    _BcamCepTabPacketsWindowSends_Type()
)
bcamCepTabPacketsWindowSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabPacketsWindowSends.setStatus("mandatory")
_BcamCepTabPacketsDataReceiveds_Type = Counter32
_BcamCepTabPacketsDataReceiveds_Object = MibTableColumn
bcamCepTabPacketsDataReceiveds = _BcamCepTabPacketsDataReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 21),
    _BcamCepTabPacketsDataReceiveds_Type()
)
bcamCepTabPacketsDataReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabPacketsDataReceiveds.setStatus("mandatory")
_BcamCepTabPacketsWindowReceiveds_Type = Counter32
_BcamCepTabPacketsWindowReceiveds_Object = MibTableColumn
bcamCepTabPacketsWindowReceiveds = _BcamCepTabPacketsWindowReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 22),
    _BcamCepTabPacketsWindowReceiveds_Type()
)
bcamCepTabPacketsWindowReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabPacketsWindowReceiveds.setStatus("mandatory")
_BcamCepTabGlobalZeroWindowSends_Type = Counter32
_BcamCepTabGlobalZeroWindowSends_Object = MibTableColumn
bcamCepTabGlobalZeroWindowSends = _BcamCepTabGlobalZeroWindowSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 23),
    _BcamCepTabGlobalZeroWindowSends_Type()
)
bcamCepTabGlobalZeroWindowSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabGlobalZeroWindowSends.setStatus("mandatory")
_BcamCepTabConnectionZeroWindowSends_Type = Counter32
_BcamCepTabConnectionZeroWindowSends_Object = MibTableColumn
bcamCepTabConnectionZeroWindowSends = _BcamCepTabConnectionZeroWindowSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 24),
    _BcamCepTabConnectionZeroWindowSends_Type()
)
bcamCepTabConnectionZeroWindowSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabConnectionZeroWindowSends.setStatus("mandatory")
_BcamCepTabZeroWindowReceiveds_Type = Counter32
_BcamCepTabZeroWindowReceiveds_Object = MibTableColumn
bcamCepTabZeroWindowReceiveds = _BcamCepTabZeroWindowReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 25),
    _BcamCepTabZeroWindowReceiveds_Type()
)
bcamCepTabZeroWindowReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabZeroWindowReceiveds.setStatus("mandatory")


class _BcamCepTabRoundTripTime_Type(Integer32):
    """Custom type bcamCepTabRoundTripTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabRoundTripTime_Type.__name__ = "Integer32"
_BcamCepTabRoundTripTime_Object = MibTableColumn
bcamCepTabRoundTripTime = _BcamCepTabRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 26),
    _BcamCepTabRoundTripTime_Type()
)
bcamCepTabRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabRoundTripTime.setStatus("mandatory")
_BcamCepTabRetransmitPacketsSends_Type = Counter32
_BcamCepTabRetransmitPacketsSends_Object = MibTableColumn
bcamCepTabRetransmitPacketsSends = _BcamCepTabRetransmitPacketsSends_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 27),
    _BcamCepTabRetransmitPacketsSends_Type()
)
bcamCepTabRetransmitPacketsSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabRetransmitPacketsSends.setStatus("mandatory")
_BcamCepTabDetectedGapsReceiveds_Type = Counter32
_BcamCepTabDetectedGapsReceiveds_Object = MibTableColumn
bcamCepTabDetectedGapsReceiveds = _BcamCepTabDetectedGapsReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 28),
    _BcamCepTabDetectedGapsReceiveds_Type()
)
bcamCepTabDetectedGapsReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabDetectedGapsReceiveds.setStatus("mandatory")
_BcamCepTabDuplicatePacketsReceiveds_Type = Counter32
_BcamCepTabDuplicatePacketsReceiveds_Object = MibTableColumn
bcamCepTabDuplicatePacketsReceiveds = _BcamCepTabDuplicatePacketsReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 29),
    _BcamCepTabDuplicatePacketsReceiveds_Type()
)
bcamCepTabDuplicatePacketsReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabDuplicatePacketsReceiveds.setStatus("mandatory")
_BcamCepTabErrorPacketsReceiveds_Type = Counter32
_BcamCepTabErrorPacketsReceiveds_Object = MibTableColumn
bcamCepTabErrorPacketsReceiveds = _BcamCepTabErrorPacketsReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 30),
    _BcamCepTabErrorPacketsReceiveds_Type()
)
bcamCepTabErrorPacketsReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabErrorPacketsReceiveds.setStatus("mandatory")


class _BcamCepTabConnectionState_Type(Integer32):
    """Custom type bcamCepTabConnectionState based on Integer32"""
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
        *(("closed", 4),
          ("closing", 3),
          ("open", 2),
          ("opening", 1))
    )


_BcamCepTabConnectionState_Type.__name__ = "Integer32"
_BcamCepTabConnectionState_Object = MibTableColumn
bcamCepTabConnectionState = _BcamCepTabConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 31),
    _BcamCepTabConnectionState_Type()
)
bcamCepTabConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabConnectionState.setStatus("mandatory")
_BcamCepTabApplicationNumber_Type = Integer32
_BcamCepTabApplicationNumber_Object = MibTableColumn
bcamCepTabApplicationNumber = _BcamCepTabApplicationNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 32),
    _BcamCepTabApplicationNumber_Type()
)
bcamCepTabApplicationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabApplicationNumber.setStatus("mandatory")
_BcamCepTabRouteNumber_Type = Integer32
_BcamCepTabRouteNumber_Object = MibTableColumn
bcamCepTabRouteNumber = _BcamCepTabRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 33),
    _BcamCepTabRouteNumber_Type()
)
bcamCepTabRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabRouteNumber.setStatus("mandatory")
_BcamCepTabDuration_Type = Gauge32
_BcamCepTabDuration_Object = MibTableColumn
bcamCepTabDuration = _BcamCepTabDuration_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 34),
    _BcamCepTabDuration_Type()
)
bcamCepTabDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabDuration.setStatus("mandatory")


class _BcamCepTabDateConnectionEstablishment_Type(DisplayString):
    """Custom type bcamCepTabDateConnectionEstablishment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamCepTabDateConnectionEstablishment_Type.__name__ = "DisplayString"
_BcamCepTabDateConnectionEstablishment_Object = MibTableColumn
bcamCepTabDateConnectionEstablishment = _BcamCepTabDateConnectionEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 35),
    _BcamCepTabDateConnectionEstablishment_Type()
)
bcamCepTabDateConnectionEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabDateConnectionEstablishment.setStatus("mandatory")


class _BcamCepTabTimeConnectionEstablishment_Type(DisplayString):
    """Custom type bcamCepTabTimeConnectionEstablishment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BcamCepTabTimeConnectionEstablishment_Type.__name__ = "DisplayString"
_BcamCepTabTimeConnectionEstablishment_Object = MibTableColumn
bcamCepTabTimeConnectionEstablishment = _BcamCepTabTimeConnectionEstablishment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 36),
    _BcamCepTabTimeConnectionEstablishment_Type()
)
bcamCepTabTimeConnectionEstablishment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabTimeConnectionEstablishment.setStatus("mandatory")


class _BcamCepTabTypPartnerName_Type(Integer32):
    """Custom type bcamCepTabTypPartnerName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isoName", 3),
          ("neaName", 1),
          ("socketName", 2))
    )


_BcamCepTabTypPartnerName_Type.__name__ = "Integer32"
_BcamCepTabTypPartnerName_Object = MibTableColumn
bcamCepTabTypPartnerName = _BcamCepTabTypPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 37),
    _BcamCepTabTypPartnerName_Type()
)
bcamCepTabTypPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabTypPartnerName.setStatus("mandatory")


class _BcamCepTabPartnerName_Type(DisplayString):
    """Custom type bcamCepTabPartnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_BcamCepTabPartnerName_Type.__name__ = "DisplayString"
_BcamCepTabPartnerName_Object = MibTableColumn
bcamCepTabPartnerName = _BcamCepTabPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 38),
    _BcamCepTabPartnerName_Type()
)
bcamCepTabPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabPartnerName.setStatus("mandatory")


class _BcamCepTabLocalName_Type(DisplayString):
    """Custom type bcamCepTabLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_BcamCepTabLocalName_Type.__name__ = "DisplayString"
_BcamCepTabLocalName_Object = MibTableColumn
bcamCepTabLocalName = _BcamCepTabLocalName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 39),
    _BcamCepTabLocalName_Type()
)
bcamCepTabLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabLocalName.setStatus("mandatory")


class _BcamCepTabTypeL4Addr_Type(Integer32):
    """Custom type bcamCepTabTypeL4Addr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neaTsel", 2),
          ("osiTsel", 3),
          ("portNumber", 1))
    )


_BcamCepTabTypeL4Addr_Type.__name__ = "Integer32"
_BcamCepTabTypeL4Addr_Object = MibTableColumn
bcamCepTabTypeL4Addr = _BcamCepTabTypeL4Addr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 40),
    _BcamCepTabTypeL4Addr_Type()
)
bcamCepTabTypeL4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabTypeL4Addr.setStatus("mandatory")


class _BcamCepTabL4AddrPartner_Type(OctetString):
    """Custom type bcamCepTabL4AddrPartner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcamCepTabL4AddrPartner_Type.__name__ = "OctetString"
_BcamCepTabL4AddrPartner_Object = MibTableColumn
bcamCepTabL4AddrPartner = _BcamCepTabL4AddrPartner_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 41),
    _BcamCepTabL4AddrPartner_Type()
)
bcamCepTabL4AddrPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabL4AddrPartner.setStatus("mandatory")


class _BcamCepTabL4AddrLocal_Type(OctetString):
    """Custom type bcamCepTabL4AddrLocal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcamCepTabL4AddrLocal_Type.__name__ = "OctetString"
_BcamCepTabL4AddrLocal_Object = MibTableColumn
bcamCepTabL4AddrLocal = _BcamCepTabL4AddrLocal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 42),
    _BcamCepTabL4AddrLocal_Type()
)
bcamCepTabL4AddrLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabL4AddrLocal.setStatus("mandatory")


class _BcamCepTabPartnerEndsystem_Type(DisplayString):
    """Custom type bcamCepTabPartnerEndsystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamCepTabPartnerEndsystem_Type.__name__ = "DisplayString"
_BcamCepTabPartnerEndsystem_Object = MibTableColumn
bcamCepTabPartnerEndsystem = _BcamCepTabPartnerEndsystem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 43),
    _BcamCepTabPartnerEndsystem_Type()
)
bcamCepTabPartnerEndsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabPartnerEndsystem.setStatus("mandatory")


class _BcamCepTabInWaitBuck1_Type(Integer32):
    """Custom type bcamCepTabInWaitBuck1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInWaitBuck1_Type.__name__ = "Integer32"
_BcamCepTabInWaitBuck1_Object = MibTableColumn
bcamCepTabInWaitBuck1 = _BcamCepTabInWaitBuck1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 44),
    _BcamCepTabInWaitBuck1_Type()
)
bcamCepTabInWaitBuck1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInWaitBuck1.setStatus("mandatory")


class _BcamCepTabInWaitBuck2_Type(Integer32):
    """Custom type bcamCepTabInWaitBuck2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInWaitBuck2_Type.__name__ = "Integer32"
_BcamCepTabInWaitBuck2_Object = MibTableColumn
bcamCepTabInWaitBuck2 = _BcamCepTabInWaitBuck2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 45),
    _BcamCepTabInWaitBuck2_Type()
)
bcamCepTabInWaitBuck2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInWaitBuck2.setStatus("mandatory")


class _BcamCepTabInWaitBuck3_Type(Integer32):
    """Custom type bcamCepTabInWaitBuck3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInWaitBuck3_Type.__name__ = "Integer32"
_BcamCepTabInWaitBuck3_Object = MibTableColumn
bcamCepTabInWaitBuck3 = _BcamCepTabInWaitBuck3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 46),
    _BcamCepTabInWaitBuck3_Type()
)
bcamCepTabInWaitBuck3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInWaitBuck3.setStatus("mandatory")


class _BcamCepTabInWaitBuck4_Type(Integer32):
    """Custom type bcamCepTabInWaitBuck4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInWaitBuck4_Type.__name__ = "Integer32"
_BcamCepTabInWaitBuck4_Object = MibTableColumn
bcamCepTabInWaitBuck4 = _BcamCepTabInWaitBuck4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 47),
    _BcamCepTabInWaitBuck4_Type()
)
bcamCepTabInWaitBuck4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInWaitBuck4.setStatus("mandatory")


class _BcamCepTabInWaitBuck5_Type(Integer32):
    """Custom type bcamCepTabInWaitBuck5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInWaitBuck5_Type.__name__ = "Integer32"
_BcamCepTabInWaitBuck5_Object = MibTableColumn
bcamCepTabInWaitBuck5 = _BcamCepTabInWaitBuck5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 48),
    _BcamCepTabInWaitBuck5_Type()
)
bcamCepTabInWaitBuck5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInWaitBuck5.setStatus("mandatory")


class _BcamCepTabReactBuck1_Type(Integer32):
    """Custom type bcamCepTabReactBuck1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabReactBuck1_Type.__name__ = "Integer32"
_BcamCepTabReactBuck1_Object = MibTableColumn
bcamCepTabReactBuck1 = _BcamCepTabReactBuck1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 49),
    _BcamCepTabReactBuck1_Type()
)
bcamCepTabReactBuck1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabReactBuck1.setStatus("mandatory")


class _BcamCepTabReactBuck2_Type(Integer32):
    """Custom type bcamCepTabReactBuck2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabReactBuck2_Type.__name__ = "Integer32"
_BcamCepTabReactBuck2_Object = MibTableColumn
bcamCepTabReactBuck2 = _BcamCepTabReactBuck2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 50),
    _BcamCepTabReactBuck2_Type()
)
bcamCepTabReactBuck2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabReactBuck2.setStatus("mandatory")


class _BcamCepTabReactBuck3_Type(Integer32):
    """Custom type bcamCepTabReactBuck3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabReactBuck3_Type.__name__ = "Integer32"
_BcamCepTabReactBuck3_Object = MibTableColumn
bcamCepTabReactBuck3 = _BcamCepTabReactBuck3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 51),
    _BcamCepTabReactBuck3_Type()
)
bcamCepTabReactBuck3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabReactBuck3.setStatus("mandatory")


class _BcamCepTabReactBuck4_Type(Integer32):
    """Custom type bcamCepTabReactBuck4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabReactBuck4_Type.__name__ = "Integer32"
_BcamCepTabReactBuck4_Object = MibTableColumn
bcamCepTabReactBuck4 = _BcamCepTabReactBuck4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 52),
    _BcamCepTabReactBuck4_Type()
)
bcamCepTabReactBuck4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabReactBuck4.setStatus("mandatory")


class _BcamCepTabReactBuck5_Type(Integer32):
    """Custom type bcamCepTabReactBuck5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabReactBuck5_Type.__name__ = "Integer32"
_BcamCepTabReactBuck5_Object = MibTableColumn
bcamCepTabReactBuck5 = _BcamCepTabReactBuck5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 53),
    _BcamCepTabReactBuck5_Type()
)
bcamCepTabReactBuck5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabReactBuck5.setStatus("mandatory")


class _BcamCepTabOutProcBuck1_Type(Integer32):
    """Custom type bcamCepTabOutProcBuck1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabOutProcBuck1_Type.__name__ = "Integer32"
_BcamCepTabOutProcBuck1_Object = MibTableColumn
bcamCepTabOutProcBuck1 = _BcamCepTabOutProcBuck1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 54),
    _BcamCepTabOutProcBuck1_Type()
)
bcamCepTabOutProcBuck1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutProcBuck1.setStatus("mandatory")


class _BcamCepTabOutProcBuck2_Type(Integer32):
    """Custom type bcamCepTabOutProcBuck2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabOutProcBuck2_Type.__name__ = "Integer32"
_BcamCepTabOutProcBuck2_Object = MibTableColumn
bcamCepTabOutProcBuck2 = _BcamCepTabOutProcBuck2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 55),
    _BcamCepTabOutProcBuck2_Type()
)
bcamCepTabOutProcBuck2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutProcBuck2.setStatus("mandatory")


class _BcamCepTabOutProcBuck3_Type(Integer32):
    """Custom type bcamCepTabOutProcBuck3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabOutProcBuck3_Type.__name__ = "Integer32"
_BcamCepTabOutProcBuck3_Object = MibTableColumn
bcamCepTabOutProcBuck3 = _BcamCepTabOutProcBuck3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 56),
    _BcamCepTabOutProcBuck3_Type()
)
bcamCepTabOutProcBuck3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutProcBuck3.setStatus("mandatory")


class _BcamCepTabOutProcBuck4_Type(Integer32):
    """Custom type bcamCepTabOutProcBuck4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabOutProcBuck4_Type.__name__ = "Integer32"
_BcamCepTabOutProcBuck4_Object = MibTableColumn
bcamCepTabOutProcBuck4 = _BcamCepTabOutProcBuck4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 57),
    _BcamCepTabOutProcBuck4_Type()
)
bcamCepTabOutProcBuck4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutProcBuck4.setStatus("mandatory")


class _BcamCepTabOutProcBuck5_Type(Integer32):
    """Custom type bcamCepTabOutProcBuck5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabOutProcBuck5_Type.__name__ = "Integer32"
_BcamCepTabOutProcBuck5_Object = MibTableColumn
bcamCepTabOutProcBuck5 = _BcamCepTabOutProcBuck5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 58),
    _BcamCepTabOutProcBuck5_Type()
)
bcamCepTabOutProcBuck5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabOutProcBuck5.setStatus("mandatory")


class _BcamCepTabInProcBuck1_Type(Integer32):
    """Custom type bcamCepTabInProcBuck1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInProcBuck1_Type.__name__ = "Integer32"
_BcamCepTabInProcBuck1_Object = MibTableColumn
bcamCepTabInProcBuck1 = _BcamCepTabInProcBuck1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 59),
    _BcamCepTabInProcBuck1_Type()
)
bcamCepTabInProcBuck1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInProcBuck1.setStatus("mandatory")


class _BcamCepTabInProcBuck2_Type(Integer32):
    """Custom type bcamCepTabInProcBuck2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInProcBuck2_Type.__name__ = "Integer32"
_BcamCepTabInProcBuck2_Object = MibTableColumn
bcamCepTabInProcBuck2 = _BcamCepTabInProcBuck2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 60),
    _BcamCepTabInProcBuck2_Type()
)
bcamCepTabInProcBuck2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInProcBuck2.setStatus("mandatory")


class _BcamCepTabInProcBuck3_Type(Integer32):
    """Custom type bcamCepTabInProcBuck3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInProcBuck3_Type.__name__ = "Integer32"
_BcamCepTabInProcBuck3_Object = MibTableColumn
bcamCepTabInProcBuck3 = _BcamCepTabInProcBuck3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 61),
    _BcamCepTabInProcBuck3_Type()
)
bcamCepTabInProcBuck3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInProcBuck3.setStatus("mandatory")


class _BcamCepTabInProcBuck4_Type(Integer32):
    """Custom type bcamCepTabInProcBuck4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInProcBuck4_Type.__name__ = "Integer32"
_BcamCepTabInProcBuck4_Object = MibTableColumn
bcamCepTabInProcBuck4 = _BcamCepTabInProcBuck4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 62),
    _BcamCepTabInProcBuck4_Type()
)
bcamCepTabInProcBuck4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInProcBuck4.setStatus("mandatory")


class _BcamCepTabInProcBuck5_Type(Integer32):
    """Custom type bcamCepTabInProcBuck5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamCepTabInProcBuck5_Type.__name__ = "Integer32"
_BcamCepTabInProcBuck5_Object = MibTableColumn
bcamCepTabInProcBuck5 = _BcamCepTabInProcBuck5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 63),
    _BcamCepTabInProcBuck5_Type()
)
bcamCepTabInProcBuck5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabInProcBuck5.setStatus("mandatory")
_BcamCepTabMaxSendLen_Type = Integer32
_BcamCepTabMaxSendLen_Object = MibTableColumn
bcamCepTabMaxSendLen = _BcamCepTabMaxSendLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 64),
    _BcamCepTabMaxSendLen_Type()
)
bcamCepTabMaxSendLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabMaxSendLen.setStatus("mandatory")
_BcamCepTabMaxIndLen_Type = Integer32
_BcamCepTabMaxIndLen_Object = MibTableColumn
bcamCepTabMaxIndLen = _BcamCepTabMaxIndLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 65),
    _BcamCepTabMaxIndLen_Type()
)
bcamCepTabMaxIndLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabMaxIndLen.setStatus("mandatory")


class _BcamCepTabLocalEndsystem_Type(DisplayString):
    """Custom type bcamCepTabLocalEndsystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamCepTabLocalEndsystem_Type.__name__ = "DisplayString"
_BcamCepTabLocalEndsystem_Object = MibTableColumn
bcamCepTabLocalEndsystem = _BcamCepTabLocalEndsystem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 6, 10, 1, 66),
    _BcamCepTabLocalEndsystem_Type()
)
bcamCepTabLocalEndsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamCepTabLocalEndsystem.setStatus("mandatory")
_BcamRoute_ObjectIdentity = ObjectIdentity
bcamRoute = _BcamRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7)
)
_BcamRouteNumTable_Type = Integer32
_BcamRouteNumTable_Object = MibScalar
bcamRouteNumTable = _BcamRouteNumTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 1),
    _BcamRouteNumTable_Type()
)
bcamRouteNumTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteNumTable.setStatus("mandatory")
_BcamRouteActive_Type = Integer32
_BcamRouteActive_Object = MibScalar
bcamRouteActive = _BcamRouteActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 2),
    _BcamRouteActive_Type()
)
bcamRouteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteActive.setStatus("mandatory")


class _BcamRouteArpDefault_Type(Integer32):
    """Custom type bcamRouteArpDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("quiet", 4))
    )


_BcamRouteArpDefault_Type.__name__ = "Integer32"
_BcamRouteArpDefault_Object = MibScalar
bcamRouteArpDefault = _BcamRouteArpDefault_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 3),
    _BcamRouteArpDefault_Type()
)
bcamRouteArpDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteArpDefault.setStatus("mandatory")
_BcamRouteRoutingReqIp_Type = Integer32
_BcamRouteRoutingReqIp_Object = MibScalar
bcamRouteRoutingReqIp = _BcamRouteRoutingReqIp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 4),
    _BcamRouteRoutingReqIp_Type()
)
bcamRouteRoutingReqIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteRoutingReqIp.setStatus("mandatory")
_BcamRouteRoutingReqIso_Type = Integer32
_BcamRouteRoutingReqIso_Object = MibScalar
bcamRouteRoutingReqIso = _BcamRouteRoutingReqIso_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 5),
    _BcamRouteRoutingReqIso_Type()
)
bcamRouteRoutingReqIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteRoutingReqIso.setStatus("mandatory")
_BcamRouteRoutingReqNea_Type = Integer32
_BcamRouteRoutingReqNea_Object = MibScalar
bcamRouteRoutingReqNea = _BcamRouteRoutingReqNea_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 6),
    _BcamRouteRoutingReqNea_Type()
)
bcamRouteRoutingReqNea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteRoutingReqNea.setStatus("mandatory")
_BcamRouteSuccRoutingReqIp_Type = Integer32
_BcamRouteSuccRoutingReqIp_Object = MibScalar
bcamRouteSuccRoutingReqIp = _BcamRouteSuccRoutingReqIp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 7),
    _BcamRouteSuccRoutingReqIp_Type()
)
bcamRouteSuccRoutingReqIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteSuccRoutingReqIp.setStatus("mandatory")
_BcamRouteSuccRoutingReqIso_Type = Integer32
_BcamRouteSuccRoutingReqIso_Object = MibScalar
bcamRouteSuccRoutingReqIso = _BcamRouteSuccRoutingReqIso_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 8),
    _BcamRouteSuccRoutingReqIso_Type()
)
bcamRouteSuccRoutingReqIso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteSuccRoutingReqIso.setStatus("mandatory")
_BcamRouteSuccRoutingReqNea_Type = Integer32
_BcamRouteSuccRoutingReqNea_Object = MibScalar
bcamRouteSuccRoutingReqNea = _BcamRouteSuccRoutingReqNea_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 9),
    _BcamRouteSuccRoutingReqNea_Type()
)
bcamRouteSuccRoutingReqNea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteSuccRoutingReqNea.setStatus("mandatory")
_BcamRouteTab_Object = MibTable
bcamRouteTab = _BcamRouteTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10)
)
if mibBuilder.loadTexts:
    bcamRouteTab.setStatus("mandatory")
_BcamRouteTabEntry_Object = MibTableRow
bcamRouteTabEntry = _BcamRouteTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1)
)
bcamRouteTabEntry.setIndexNames(
    (0, "BCAM-MIB", "bcamRouteTabNumbers"),
)
if mibBuilder.loadTexts:
    bcamRouteTabEntry.setStatus("mandatory")
_BcamRouteTabNumbers_Type = Counter32
_BcamRouteTabNumbers_Object = MibTableColumn
bcamRouteTabNumbers = _BcamRouteTabNumbers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 1),
    _BcamRouteTabNumbers_Type()
)
bcamRouteTabNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumbers.setStatus("mandatory")


class _BcamRouteTabName_Type(DisplayString):
    """Custom type bcamRouteTabName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamRouteTabName_Type.__name__ = "DisplayString"
_BcamRouteTabName_Object = MibTableColumn
bcamRouteTabName = _BcamRouteTabName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 2),
    _BcamRouteTabName_Type()
)
bcamRouteTabName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabName.setStatus("mandatory")
_BcamRouteTabNumNeaConn_Type = Gauge32
_BcamRouteTabNumNeaConn_Object = MibTableColumn
bcamRouteTabNumNeaConn = _BcamRouteTabNumNeaConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 3),
    _BcamRouteTabNumNeaConn_Type()
)
bcamRouteTabNumNeaConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumNeaConn.setStatus("mandatory")
_BcamRouteTabNumIsoConn_Type = Gauge32
_BcamRouteTabNumIsoConn_Object = MibTableColumn
bcamRouteTabNumIsoConn = _BcamRouteTabNumIsoConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 4),
    _BcamRouteTabNumIsoConn_Type()
)
bcamRouteTabNumIsoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumIsoConn.setStatus("mandatory")
_BcamRouteTabMaxNeaConn_Type = Gauge32
_BcamRouteTabMaxNeaConn_Object = MibTableColumn
bcamRouteTabMaxNeaConn = _BcamRouteTabMaxNeaConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 5),
    _BcamRouteTabMaxNeaConn_Type()
)
bcamRouteTabMaxNeaConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxNeaConn.setStatus("mandatory")
_BcamRouteTabMaxIsoConn_Type = Gauge32
_BcamRouteTabMaxIsoConn_Object = MibTableColumn
bcamRouteTabMaxIsoConn = _BcamRouteTabMaxIsoConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 6),
    _BcamRouteTabMaxIsoConn_Type()
)
bcamRouteTabMaxIsoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxIsoConn.setStatus("mandatory")
_BcamRouteTabBadNeaElems_Type = Counter32
_BcamRouteTabBadNeaElems_Object = MibTableColumn
bcamRouteTabBadNeaElems = _BcamRouteTabBadNeaElems_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 7),
    _BcamRouteTabBadNeaElems_Type()
)
bcamRouteTabBadNeaElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabBadNeaElems.setStatus("mandatory")
_BcamRouteTabBadIsoElems_Type = Counter32
_BcamRouteTabBadIsoElems_Object = MibTableColumn
bcamRouteTabBadIsoElems = _BcamRouteTabBadIsoElems_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 8),
    _BcamRouteTabBadIsoElems_Type()
)
bcamRouteTabBadIsoElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabBadIsoElems.setStatus("mandatory")
_BcamRouteTabMaxL4Conn_Type = Gauge32
_BcamRouteTabMaxL4Conn_Object = MibTableColumn
bcamRouteTabMaxL4Conn = _BcamRouteTabMaxL4Conn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 9),
    _BcamRouteTabMaxL4Conn_Type()
)
bcamRouteTabMaxL4Conn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxL4Conn.setStatus("mandatory")
_BcamRouteTabMaxUnackTpdu_Type = Gauge32
_BcamRouteTabMaxUnackTpdu_Object = MibTableColumn
bcamRouteTabMaxUnackTpdu = _BcamRouteTabMaxUnackTpdu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 10),
    _BcamRouteTabMaxUnackTpdu_Type()
)
bcamRouteTabMaxUnackTpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxUnackTpdu.setStatus("mandatory")


class _BcamRouteTabRouteNetTyp_Type(Integer32):
    """Custom type bcamRouteTabRouteNetTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("gatewayRouter", 1),
          ("int0Router", 8),
          ("intfIpRouter", 4),
          ("neaRouter", 2))
    )


_BcamRouteTabRouteNetTyp_Type.__name__ = "Integer32"
_BcamRouteTabRouteNetTyp_Object = MibTableColumn
bcamRouteTabRouteNetTyp = _BcamRouteTabRouteNetTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 11),
    _BcamRouteTabRouteNetTyp_Type()
)
bcamRouteTabRouteNetTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabRouteNetTyp.setStatus("mandatory")
_BcamRouteTabNumberIsoIpRouter_Type = Integer32
_BcamRouteTabNumberIsoIpRouter_Object = MibTableColumn
bcamRouteTabNumberIsoIpRouter = _BcamRouteTabNumberIsoIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 12),
    _BcamRouteTabNumberIsoIpRouter_Type()
)
bcamRouteTabNumberIsoIpRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumberIsoIpRouter.setStatus("mandatory")
_BcamRouteTabNumberNeaRouter_Type = Integer32
_BcamRouteTabNumberNeaRouter_Object = MibTableColumn
bcamRouteTabNumberNeaRouter = _BcamRouteTabNumberNeaRouter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 13),
    _BcamRouteTabNumberNeaRouter_Type()
)
bcamRouteTabNumberNeaRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumberNeaRouter.setStatus("mandatory")
_BcamRouteTabNumberGateway_Type = Integer32
_BcamRouteTabNumberGateway_Object = MibTableColumn
bcamRouteTabNumberGateway = _BcamRouteTabNumberGateway_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 14),
    _BcamRouteTabNumberGateway_Type()
)
bcamRouteTabNumberGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumberGateway.setStatus("mandatory")


class _BcamRouteTabFunction_Type(Integer32):
    """Custom type bcamRouteTabFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onlyServerAccess", 1),
          ("transportRoute", 2))
    )


_BcamRouteTabFunction_Type.__name__ = "Integer32"
_BcamRouteTabFunction_Object = MibTableColumn
bcamRouteTabFunction = _BcamRouteTabFunction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 15),
    _BcamRouteTabFunction_Type()
)
bcamRouteTabFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabFunction.setStatus("mandatory")


class _BcamRouteTabProcNetTyp_Type(Integer32):
    """Custom type bcamRouteTabProcNetTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gatewayProc", 1),
          ("isoIpProc", 4),
          ("neaProc", 2))
    )


_BcamRouteTabProcNetTyp_Type.__name__ = "Integer32"
_BcamRouteTabProcNetTyp_Object = MibTableColumn
bcamRouteTabProcNetTyp = _BcamRouteTabProcNetTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 16),
    _BcamRouteTabProcNetTyp_Type()
)
bcamRouteTabProcNetTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabProcNetTyp.setStatus("mandatory")
_BcamRouteTabMaxTsduLen_Type = Gauge32
_BcamRouteTabMaxTsduLen_Object = MibTableColumn
bcamRouteTabMaxTsduLen = _BcamRouteTabMaxTsduLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 17),
    _BcamRouteTabMaxTsduLen_Type()
)
bcamRouteTabMaxTsduLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxTsduLen.setStatus("mandatory")


class _BcamRouteTabNameEndsystem_Type(DisplayString):
    """Custom type bcamRouteTabNameEndsystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamRouteTabNameEndsystem_Type.__name__ = "DisplayString"
_BcamRouteTabNameEndsystem_Object = MibTableColumn
bcamRouteTabNameEndsystem = _BcamRouteTabNameEndsystem_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 18),
    _BcamRouteTabNameEndsystem_Type()
)
bcamRouteTabNameEndsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNameEndsystem.setStatus("mandatory")
_BcamRouteTabIso4WindowTimer_Type = Gauge32
_BcamRouteTabIso4WindowTimer_Object = MibTableColumn
bcamRouteTabIso4WindowTimer = _BcamRouteTabIso4WindowTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 19),
    _BcamRouteTabIso4WindowTimer_Type()
)
bcamRouteTabIso4WindowTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabIso4WindowTimer.setStatus("mandatory")
_BcamRouteTabIso4RetransTimer_Type = Gauge32
_BcamRouteTabIso4RetransTimer_Object = MibTableColumn
bcamRouteTabIso4RetransTimer = _BcamRouteTabIso4RetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 20),
    _BcamRouteTabIso4RetransTimer_Type()
)
bcamRouteTabIso4RetransTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabIso4RetransTimer.setStatus("mandatory")
_BcamRouteTabAckTimer_Type = Gauge32
_BcamRouteTabAckTimer_Object = MibTableColumn
bcamRouteTabAckTimer = _BcamRouteTabAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 21),
    _BcamRouteTabAckTimer_Type()
)
bcamRouteTabAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabAckTimer.setStatus("mandatory")
_BcamRouteTabErrorRecovTimer_Type = Gauge32
_BcamRouteTabErrorRecovTimer_Object = MibTableColumn
bcamRouteTabErrorRecovTimer = _BcamRouteTabErrorRecovTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 22),
    _BcamRouteTabErrorRecovTimer_Type()
)
bcamRouteTabErrorRecovTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabErrorRecovTimer.setStatus("mandatory")
_BcamRouteTabRejectTimer_Type = Gauge32
_BcamRouteTabRejectTimer_Object = MibTableColumn
bcamRouteTabRejectTimer = _BcamRouteTabRejectTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 23),
    _BcamRouteTabRejectTimer_Type()
)
bcamRouteTabRejectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabRejectTimer.setStatus("mandatory")
_BcamRouteTabExpedRetransTimer_Type = Gauge32
_BcamRouteTabExpedRetransTimer_Object = MibTableColumn
bcamRouteTabExpedRetransTimer = _BcamRouteTabExpedRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 24),
    _BcamRouteTabExpedRetransTimer_Type()
)
bcamRouteTabExpedRetransTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabExpedRetransTimer.setStatus("mandatory")


class _BcamRouteTabNameGateway_Type(DisplayString):
    """Custom type bcamRouteTabNameGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamRouteTabNameGateway_Type.__name__ = "DisplayString"
_BcamRouteTabNameGateway_Object = MibTableColumn
bcamRouteTabNameGateway = _BcamRouteTabNameGateway_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 25),
    _BcamRouteTabNameGateway_Type()
)
bcamRouteTabNameGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNameGateway.setStatus("mandatory")


class _BcamRouteTabNameX25Station_Type(DisplayString):
    """Custom type bcamRouteTabNameX25Station based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamRouteTabNameX25Station_Type.__name__ = "DisplayString"
_BcamRouteTabNameX25Station_Object = MibTableColumn
bcamRouteTabNameX25Station = _BcamRouteTabNameX25Station_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 26),
    _BcamRouteTabNameX25Station_Type()
)
bcamRouteTabNameX25Station.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNameX25Station.setStatus("mandatory")


class _BcamRouteTabL3InputProfil_Type(Integer32):
    """Custom type bcamRouteTabL3InputProfil based on Integer32"""
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
        *(("gateway", 4),
          ("int0", 2),
          ("intf", 3),
          ("ip", 5),
          ("nea", 1))
    )


_BcamRouteTabL3InputProfil_Type.__name__ = "Integer32"
_BcamRouteTabL3InputProfil_Object = MibTableColumn
bcamRouteTabL3InputProfil = _BcamRouteTabL3InputProfil_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 27),
    _BcamRouteTabL3InputProfil_Type()
)
bcamRouteTabL3InputProfil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabL3InputProfil.setStatus("mandatory")


class _BcamRouteTabTransState_Type(Integer32):
    """Custom type bcamRouteTabTransState based on Integer32"""
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
        *(("notReady", 4),
          ("ready", 3),
          ("waitForReadyToTransfer", 2),
          ("waitForTransferInit", 1))
    )


_BcamRouteTabTransState_Type.__name__ = "Integer32"
_BcamRouteTabTransState_Object = MibTableColumn
bcamRouteTabTransState = _BcamRouteTabTransState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 28),
    _BcamRouteTabTransState_Type()
)
bcamRouteTabTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabTransState.setStatus("mandatory")


class _BcamRouteTabOption_Type(Integer32):
    """Custom type bcamRouteTabOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delayedAckAllowed", 1),
          ("optimalSegmentSizeOn", 2))
    )


_BcamRouteTabOption_Type.__name__ = "Integer32"
_BcamRouteTabOption_Object = MibTableColumn
bcamRouteTabOption = _BcamRouteTabOption_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 29),
    _BcamRouteTabOption_Type()
)
bcamRouteTabOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabOption.setStatus("mandatory")


class _BcamRouteTabTyp_Type(Integer32):
    """Custom type bcamRouteTabTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("node", 3),
          ("remote", 2))
    )


_BcamRouteTabTyp_Type.__name__ = "Integer32"
_BcamRouteTabTyp_Object = MibTableColumn
bcamRouteTabTyp = _BcamRouteTabTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 30),
    _BcamRouteTabTyp_Type()
)
bcamRouteTabTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabTyp.setStatus("mandatory")


class _BcamRouteTabUsage_Type(Integer32):
    """Custom type bcamRouteTabUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("gatewayRoute", 1),
          ("int0Router", 8),
          ("intfIpRouter", 2),
          ("neaRouter", 4),
          ("noIntermediate", 16))
    )


_BcamRouteTabUsage_Type.__name__ = "Integer32"
_BcamRouteTabUsage_Object = MibTableColumn
bcamRouteTabUsage = _BcamRouteTabUsage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 31),
    _BcamRouteTabUsage_Type()
)
bcamRouteTabUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabUsage.setStatus("mandatory")


class _BcamRouteTabL3Subprofile_Type(Integer32):
    """Custom type bcamRouteTabL3Subprofile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("neaNetConn", 4),
          ("neattNetConn", 8),
          ("netConnLess", 2),
          ("rfc1042", 1))
    )


_BcamRouteTabL3Subprofile_Type.__name__ = "Integer32"
_BcamRouteTabL3Subprofile_Object = MibTableColumn
bcamRouteTabL3Subprofile = _BcamRouteTabL3Subprofile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 32),
    _BcamRouteTabL3Subprofile_Type()
)
bcamRouteTabL3Subprofile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabL3Subprofile.setStatus("mandatory")


class _BcamRouteTabCommandState_Type(Integer32):
    """Custom type bcamRouteTabCommandState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("included", 1))
    )


_BcamRouteTabCommandState_Type.__name__ = "Integer32"
_BcamRouteTabCommandState_Object = MibTableColumn
bcamRouteTabCommandState = _BcamRouteTabCommandState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 33),
    _BcamRouteTabCommandState_Type()
)
bcamRouteTabCommandState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabCommandState.setStatus("mandatory")


class _BcamRouteTabChangeState_Type(Integer32):
    """Custom type bcamRouteTabChangeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("changed", 8),
          ("defByProtocol", 2),
          ("dynamic", 1),
          ("generated", 16),
          ("switchByProtocol", 4))
    )


_BcamRouteTabChangeState_Type.__name__ = "Integer32"
_BcamRouteTabChangeState_Object = MibTableColumn
bcamRouteTabChangeState = _BcamRouteTabChangeState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 34),
    _BcamRouteTabChangeState_Type()
)
bcamRouteTabChangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabChangeState.setStatus("mandatory")


class _BcamRouteTabIso9542_Type(Integer32):
    """Custom type bcamRouteTabIso9542 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eshReceived", 1),
          ("ishReceived", 2),
          ("iso8473QueryReceived", 4),
          ("refreshRequired", 8))
    )


_BcamRouteTabIso9542_Type.__name__ = "Integer32"
_BcamRouteTabIso9542_Object = MibTableColumn
bcamRouteTabIso9542 = _BcamRouteTabIso9542_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 35),
    _BcamRouteTabIso9542_Type()
)
bcamRouteTabIso9542.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabIso9542.setStatus("mandatory")


class _BcamRouteTabMaxNetLength_Type(Integer32):
    """Custom type bcamRouteTabMaxNetLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 2))
    )


_BcamRouteTabMaxNetLength_Type.__name__ = "Integer32"
_BcamRouteTabMaxNetLength_Object = MibTableColumn
bcamRouteTabMaxNetLength = _BcamRouteTabMaxNetLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 36),
    _BcamRouteTabMaxNetLength_Type()
)
bcamRouteTabMaxNetLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxNetLength.setStatus("mandatory")


class _BcamRouteTabState2_Type(Integer32):
    """Custom type bcamRouteTabState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("lifeSupervisionFailed", 8),
          ("silent", 16),
          ("testing", 1),
          ("waitAddrResolution", 4),
          ("working", 2))
    )


_BcamRouteTabState2_Type.__name__ = "Integer32"
_BcamRouteTabState2_Object = MibTableColumn
bcamRouteTabState2 = _BcamRouteTabState2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 37),
    _BcamRouteTabState2_Type()
)
bcamRouteTabState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabState2.setStatus("mandatory")


class _BcamRouteTabDeactReason_Type(Integer32):
    """Custom type bcamRouteTabDeactReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("flush", 1),
          ("noArpReply", 4),
          ("supposedDown", 2))
    )


_BcamRouteTabDeactReason_Type.__name__ = "Integer32"
_BcamRouteTabDeactReason_Object = MibTableColumn
bcamRouteTabDeactReason = _BcamRouteTabDeactReason_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 38),
    _BcamRouteTabDeactReason_Type()
)
bcamRouteTabDeactReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabDeactReason.setStatus("mandatory")


class _BcamRouteTabSwitchType_Type(Integer32):
    """Custom type bcamRouteTabSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("lanAddrChanged", 16),
          ("localRemote", 1),
          ("lsapChanged", 8),
          ("remoteLocal", 2),
          ("remoteRemote", 4))
    )


_BcamRouteTabSwitchType_Type.__name__ = "Integer32"
_BcamRouteTabSwitchType_Object = MibTableColumn
bcamRouteTabSwitchType = _BcamRouteTabSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 39),
    _BcamRouteTabSwitchType_Type()
)
bcamRouteTabSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabSwitchType.setStatus("mandatory")


class _BcamRouteTabReasonCreation_Type(Integer32):
    """Custom type bcamRouteTabReasonCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("incomingData", 1),
          ("outgoingData", 2),
          ("routingData", 8),
          ("routingProtocol", 4))
    )


_BcamRouteTabReasonCreation_Type.__name__ = "Integer32"
_BcamRouteTabReasonCreation_Object = MibTableColumn
bcamRouteTabReasonCreation = _BcamRouteTabReasonCreation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 40),
    _BcamRouteTabReasonCreation_Type()
)
bcamRouteTabReasonCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabReasonCreation.setStatus("mandatory")
_BcamRouteTabOrigLanAddress_Type = PhysAddress
_BcamRouteTabOrigLanAddress_Object = MibTableColumn
bcamRouteTabOrigLanAddress = _BcamRouteTabOrigLanAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 41),
    _BcamRouteTabOrigLanAddress_Type()
)
bcamRouteTabOrigLanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabOrigLanAddress.setStatus("mandatory")
_BcamRouteTabLanAddress_Type = PhysAddress
_BcamRouteTabLanAddress_Object = MibTableColumn
bcamRouteTabLanAddress = _BcamRouteTabLanAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 42),
    _BcamRouteTabLanAddress_Type()
)
bcamRouteTabLanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabLanAddress.setStatus("mandatory")


class _BcamRouteTabTypAddress_Type(Integer32):
    """Custom type bcamRouteTabTypAddress based on Integer32"""
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
        *(("int0", 4),
          ("intf", 2),
          ("nea", 1),
          ("streams", 3))
    )


_BcamRouteTabTypAddress_Type.__name__ = "Integer32"
_BcamRouteTabTypAddress_Object = MibTableColumn
bcamRouteTabTypAddress = _BcamRouteTabTypAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 43),
    _BcamRouteTabTypAddress_Type()
)
bcamRouteTabTypAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabTypAddress.setStatus("mandatory")


class _BcamRouteTabLocalAddr_Type(OctetString):
    """Custom type bcamRouteTabLocalAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamRouteTabLocalAddr_Type.__name__ = "OctetString"
_BcamRouteTabLocalAddr_Object = MibTableColumn
bcamRouteTabLocalAddr = _BcamRouteTabLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 44),
    _BcamRouteTabLocalAddr_Type()
)
bcamRouteTabLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabLocalAddr.setStatus("mandatory")


class _BcamRouteTabRemoteAddr_Type(OctetString):
    """Custom type bcamRouteTabRemoteAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamRouteTabRemoteAddr_Type.__name__ = "OctetString"
_BcamRouteTabRemoteAddr_Object = MibTableColumn
bcamRouteTabRemoteAddr = _BcamRouteTabRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 45),
    _BcamRouteTabRemoteAddr_Type()
)
bcamRouteTabRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabRemoteAddr.setStatus("mandatory")
_BcamRouteTabOutPacketsDatas_Type = Counter32
_BcamRouteTabOutPacketsDatas_Object = MibTableColumn
bcamRouteTabOutPacketsDatas = _BcamRouteTabOutPacketsDatas_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 46),
    _BcamRouteTabOutPacketsDatas_Type()
)
bcamRouteTabOutPacketsDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabOutPacketsDatas.setStatus("mandatory")
_BcamRouteTabOutPacketsFlowControls_Type = Counter32
_BcamRouteTabOutPacketsFlowControls_Object = MibTableColumn
bcamRouteTabOutPacketsFlowControls = _BcamRouteTabOutPacketsFlowControls_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 47),
    _BcamRouteTabOutPacketsFlowControls_Type()
)
bcamRouteTabOutPacketsFlowControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabOutPacketsFlowControls.setStatus("mandatory")
_BcamRouteTabInPacketsDatas_Type = Counter32
_BcamRouteTabInPacketsDatas_Object = MibTableColumn
bcamRouteTabInPacketsDatas = _BcamRouteTabInPacketsDatas_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 48),
    _BcamRouteTabInPacketsDatas_Type()
)
bcamRouteTabInPacketsDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabInPacketsDatas.setStatus("mandatory")
_BcamRouteTabInPacketsFlowControls_Type = Counter32
_BcamRouteTabInPacketsFlowControls_Object = MibTableColumn
bcamRouteTabInPacketsFlowControls = _BcamRouteTabInPacketsFlowControls_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 49),
    _BcamRouteTabInPacketsFlowControls_Type()
)
bcamRouteTabInPacketsFlowControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabInPacketsFlowControls.setStatus("mandatory")
_BcamRouteTabOutRetransPackets_Type = Counter32
_BcamRouteTabOutRetransPackets_Object = MibTableColumn
bcamRouteTabOutRetransPackets = _BcamRouteTabOutRetransPackets_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 50),
    _BcamRouteTabOutRetransPackets_Type()
)
bcamRouteTabOutRetransPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabOutRetransPackets.setStatus("mandatory")
_BcamRouteTabInDetectedGaps_Type = Counter32
_BcamRouteTabInDetectedGaps_Object = MibTableColumn
bcamRouteTabInDetectedGaps = _BcamRouteTabInDetectedGaps_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 51),
    _BcamRouteTabInDetectedGaps_Type()
)
bcamRouteTabInDetectedGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabInDetectedGaps.setStatus("mandatory")
_BcamRouteTabInDuplicatedPackets_Type = Counter32
_BcamRouteTabInDuplicatedPackets_Object = MibTableColumn
bcamRouteTabInDuplicatedPackets = _BcamRouteTabInDuplicatedPackets_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 52),
    _BcamRouteTabInDuplicatedPackets_Type()
)
bcamRouteTabInDuplicatedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabInDuplicatedPackets.setStatus("mandatory")
_BcamRouteTabInIncorrectPackets_Type = Counter32
_BcamRouteTabInIncorrectPackets_Object = MibTableColumn
bcamRouteTabInIncorrectPackets = _BcamRouteTabInIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 53),
    _BcamRouteTabInIncorrectPackets_Type()
)
bcamRouteTabInIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabInIncorrectPackets.setStatus("mandatory")


class _BcamRouteTabRoundTripTimeClosed_Type(Integer32):
    """Custom type bcamRouteTabRoundTripTimeClosed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabRoundTripTimeClosed_Type.__name__ = "Integer32"
_BcamRouteTabRoundTripTimeClosed_Object = MibTableColumn
bcamRouteTabRoundTripTimeClosed = _BcamRouteTabRoundTripTimeClosed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 54),
    _BcamRouteTabRoundTripTimeClosed_Type()
)
bcamRouteTabRoundTripTimeClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabRoundTripTimeClosed.setStatus("mandatory")


class _BcamRouteTabRoundTripTimeCurrent_Type(Integer32):
    """Custom type bcamRouteTabRoundTripTimeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabRoundTripTimeCurrent_Type.__name__ = "Integer32"
_BcamRouteTabRoundTripTimeCurrent_Object = MibTableColumn
bcamRouteTabRoundTripTimeCurrent = _BcamRouteTabRoundTripTimeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 55),
    _BcamRouteTabRoundTripTimeCurrent_Type()
)
bcamRouteTabRoundTripTimeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabRoundTripTimeCurrent.setStatus("mandatory")
_BcamRouteTabArpReqSend_Type = Integer32
_BcamRouteTabArpReqSend_Object = MibTableColumn
bcamRouteTabArpReqSend = _BcamRouteTabArpReqSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 56),
    _BcamRouteTabArpReqSend_Type()
)
bcamRouteTabArpReqSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabArpReqSend.setStatus("mandatory")
_BcamRouteTabArpRepSend_Type = Integer32
_BcamRouteTabArpRepSend_Object = MibTableColumn
bcamRouteTabArpRepSend = _BcamRouteTabArpRepSend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 57),
    _BcamRouteTabArpRepSend_Type()
)
bcamRouteTabArpRepSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabArpRepSend.setStatus("mandatory")
_BcamRouteTabArpReqRec_Type = Integer32
_BcamRouteTabArpReqRec_Object = MibTableColumn
bcamRouteTabArpReqRec = _BcamRouteTabArpReqRec_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 58),
    _BcamRouteTabArpReqRec_Type()
)
bcamRouteTabArpReqRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabArpReqRec.setStatus("mandatory")
_BcamRouteTabArpRepRec_Type = Integer32
_BcamRouteTabArpRepRec_Object = MibTableColumn
bcamRouteTabArpRepRec = _BcamRouteTabArpRepRec_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 59),
    _BcamRouteTabArpRepRec_Type()
)
bcamRouteTabArpRepRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabArpRepRec.setStatus("mandatory")
_BcamRouteTabIcmpReq_Type = Integer32
_BcamRouteTabIcmpReq_Object = MibTableColumn
bcamRouteTabIcmpReq = _BcamRouteTabIcmpReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 60),
    _BcamRouteTabIcmpReq_Type()
)
bcamRouteTabIcmpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabIcmpReq.setStatus("mandatory")
_BcamRouteTabIcmpReply_Type = Integer32
_BcamRouteTabIcmpReply_Object = MibTableColumn
bcamRouteTabIcmpReply = _BcamRouteTabIcmpReply_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 61),
    _BcamRouteTabIcmpReply_Type()
)
bcamRouteTabIcmpReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabIcmpReply.setStatus("mandatory")
_BcamRouteTabIcmpRedirect_Type = Integer32
_BcamRouteTabIcmpRedirect_Object = MibTableColumn
bcamRouteTabIcmpRedirect = _BcamRouteTabIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 62),
    _BcamRouteTabIcmpRedirect_Type()
)
bcamRouteTabIcmpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabIcmpRedirect.setStatus("mandatory")
_BcamRouteTabSwitched_Type = Integer32
_BcamRouteTabSwitched_Object = MibTableColumn
bcamRouteTabSwitched = _BcamRouteTabSwitched_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 63),
    _BcamRouteTabSwitched_Type()
)
bcamRouteTabSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabSwitched.setStatus("mandatory")
_BcamRouteTabDown_Type = Integer32
_BcamRouteTabDown_Object = MibTableColumn
bcamRouteTabDown = _BcamRouteTabDown_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 64),
    _BcamRouteTabDown_Type()
)
bcamRouteTabDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabDown.setStatus("mandatory")
_BcamRouteTabOspfHello_Type = Integer32
_BcamRouteTabOspfHello_Object = MibTableColumn
bcamRouteTabOspfHello = _BcamRouteTabOspfHello_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 65),
    _BcamRouteTabOspfHello_Type()
)
bcamRouteTabOspfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabOspfHello.setStatus("mandatory")


class _BcamRouteTabPacketNoConn_Type(Integer32):
    """Custom type bcamRouteTabPacketNoConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabPacketNoConn_Type.__name__ = "Integer32"
_BcamRouteTabPacketNoConn_Object = MibTableColumn
bcamRouteTabPacketNoConn = _BcamRouteTabPacketNoConn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 66),
    _BcamRouteTabPacketNoConn_Type()
)
bcamRouteTabPacketNoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabPacketNoConn.setStatus("mandatory")


class _BcamRouteTabPacketInternDiscon_Type(Integer32):
    """Custom type bcamRouteTabPacketInternDiscon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabPacketInternDiscon_Type.__name__ = "Integer32"
_BcamRouteTabPacketInternDiscon_Object = MibTableColumn
bcamRouteTabPacketInternDiscon = _BcamRouteTabPacketInternDiscon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 67),
    _BcamRouteTabPacketInternDiscon_Type()
)
bcamRouteTabPacketInternDiscon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabPacketInternDiscon.setStatus("mandatory")


class _BcamRouteTabPacketBadProtocol_Type(Integer32):
    """Custom type bcamRouteTabPacketBadProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabPacketBadProtocol_Type.__name__ = "Integer32"
_BcamRouteTabPacketBadProtocol_Object = MibTableColumn
bcamRouteTabPacketBadProtocol = _BcamRouteTabPacketBadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 68),
    _BcamRouteTabPacketBadProtocol_Type()
)
bcamRouteTabPacketBadProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabPacketBadProtocol.setStatus("mandatory")


class _BcamRouteTabConnReqOut_Type(Integer32):
    """Custom type bcamRouteTabConnReqOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabConnReqOut_Type.__name__ = "Integer32"
_BcamRouteTabConnReqOut_Object = MibTableColumn
bcamRouteTabConnReqOut = _BcamRouteTabConnReqOut_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 69),
    _BcamRouteTabConnReqOut_Type()
)
bcamRouteTabConnReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabConnReqOut.setStatus("mandatory")


class _BcamRouteTabConnReqOutAck_Type(Integer32):
    """Custom type bcamRouteTabConnReqOutAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabConnReqOutAck_Type.__name__ = "Integer32"
_BcamRouteTabConnReqOutAck_Object = MibTableColumn
bcamRouteTabConnReqOutAck = _BcamRouteTabConnReqOutAck_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 70),
    _BcamRouteTabConnReqOutAck_Type()
)
bcamRouteTabConnReqOutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabConnReqOutAck.setStatus("mandatory")


class _BcamRouteTabConnReqOutRej_Type(Integer32):
    """Custom type bcamRouteTabConnReqOutRej based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabConnReqOutRej_Type.__name__ = "Integer32"
_BcamRouteTabConnReqOutRej_Object = MibTableColumn
bcamRouteTabConnReqOutRej = _BcamRouteTabConnReqOutRej_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 71),
    _BcamRouteTabConnReqOutRej_Type()
)
bcamRouteTabConnReqOutRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabConnReqOutRej.setStatus("mandatory")


class _BcamRouteTabConnReqIn_Type(Integer32):
    """Custom type bcamRouteTabConnReqIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabConnReqIn_Type.__name__ = "Integer32"
_BcamRouteTabConnReqIn_Object = MibTableColumn
bcamRouteTabConnReqIn = _BcamRouteTabConnReqIn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 72),
    _BcamRouteTabConnReqIn_Type()
)
bcamRouteTabConnReqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabConnReqIn.setStatus("mandatory")


class _BcamRouteTabConnReqInAck_Type(Integer32):
    """Custom type bcamRouteTabConnReqInAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabConnReqInAck_Type.__name__ = "Integer32"
_BcamRouteTabConnReqInAck_Object = MibTableColumn
bcamRouteTabConnReqInAck = _BcamRouteTabConnReqInAck_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 73),
    _BcamRouteTabConnReqInAck_Type()
)
bcamRouteTabConnReqInAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabConnReqInAck.setStatus("mandatory")


class _BcamRouteTabConnReqInRej_Type(Integer32):
    """Custom type bcamRouteTabConnReqInRej based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabConnReqInRej_Type.__name__ = "Integer32"
_BcamRouteTabConnReqInRej_Object = MibTableColumn
bcamRouteTabConnReqInRej = _BcamRouteTabConnReqInRej_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 74),
    _BcamRouteTabConnReqInRej_Type()
)
bcamRouteTabConnReqInRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabConnReqInRej.setStatus("mandatory")


class _BcamRouteTabDisconnOut_Type(Integer32):
    """Custom type bcamRouteTabDisconnOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabDisconnOut_Type.__name__ = "Integer32"
_BcamRouteTabDisconnOut_Object = MibTableColumn
bcamRouteTabDisconnOut = _BcamRouteTabDisconnOut_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 75),
    _BcamRouteTabDisconnOut_Type()
)
bcamRouteTabDisconnOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabDisconnOut.setStatus("mandatory")


class _BcamRouteTabDisconnOutAck_Type(Integer32):
    """Custom type bcamRouteTabDisconnOutAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabDisconnOutAck_Type.__name__ = "Integer32"
_BcamRouteTabDisconnOutAck_Object = MibTableColumn
bcamRouteTabDisconnOutAck = _BcamRouteTabDisconnOutAck_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 76),
    _BcamRouteTabDisconnOutAck_Type()
)
bcamRouteTabDisconnOutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabDisconnOutAck.setStatus("mandatory")


class _BcamRouteTabDisconnIn_Type(Integer32):
    """Custom type bcamRouteTabDisconnIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabDisconnIn_Type.__name__ = "Integer32"
_BcamRouteTabDisconnIn_Object = MibTableColumn
bcamRouteTabDisconnIn = _BcamRouteTabDisconnIn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 77),
    _BcamRouteTabDisconnIn_Type()
)
bcamRouteTabDisconnIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabDisconnIn.setStatus("mandatory")


class _BcamRouteTabDisconnInAck_Type(Integer32):
    """Custom type bcamRouteTabDisconnInAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcamRouteTabDisconnInAck_Type.__name__ = "Integer32"
_BcamRouteTabDisconnInAck_Object = MibTableColumn
bcamRouteTabDisconnInAck = _BcamRouteTabDisconnInAck_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 78),
    _BcamRouteTabDisconnInAck_Type()
)
bcamRouteTabDisconnInAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabDisconnInAck.setStatus("mandatory")
_BcamRouteTabNumberLink_Type = Integer32
_BcamRouteTabNumberLink_Object = MibTableColumn
bcamRouteTabNumberLink = _BcamRouteTabNumberLink_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 79),
    _BcamRouteTabNumberLink_Type()
)
bcamRouteTabNumberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNumberLink.setStatus("mandatory")


class _BcamRouteTabArpFlag_Type(Integer32):
    """Custom type bcamRouteTabArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("quiet", 4))
    )


_BcamRouteTabArpFlag_Type.__name__ = "Integer32"
_BcamRouteTabArpFlag_Object = MibTableColumn
bcamRouteTabArpFlag = _BcamRouteTabArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 80),
    _BcamRouteTabArpFlag_Type()
)
bcamRouteTabArpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabArpFlag.setStatus("mandatory")
_BcamRouteTabNsduLen_Type = Integer32
_BcamRouteTabNsduLen_Object = MibTableColumn
bcamRouteTabNsduLen = _BcamRouteTabNsduLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 81),
    _BcamRouteTabNsduLen_Type()
)
bcamRouteTabNsduLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabNsduLen.setStatus("mandatory")
_BcamRouteTabMinNsduLen_Type = Integer32
_BcamRouteTabMinNsduLen_Object = MibTableColumn
bcamRouteTabMinNsduLen = _BcamRouteTabMinNsduLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 82),
    _BcamRouteTabMinNsduLen_Type()
)
bcamRouteTabMinNsduLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMinNsduLen.setStatus("mandatory")
_BcamRouteTabMaxNsduLen_Type = Integer32
_BcamRouteTabMaxNsduLen_Object = MibTableColumn
bcamRouteTabMaxNsduLen = _BcamRouteTabMaxNsduLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 7, 10, 1, 83),
    _BcamRouteTabMaxNsduLen_Type()
)
bcamRouteTabMaxNsduLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouteTabMaxNsduLen.setStatus("mandatory")
_BcamIf_ObjectIdentity = ObjectIdentity
bcamIf = _BcamIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8)
)
_BcamIfNumTable_Type = Integer32
_BcamIfNumTable_Object = MibScalar
bcamIfNumTable = _BcamIfNumTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 1),
    _BcamIfNumTable_Type()
)
bcamIfNumTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfNumTable.setStatus("mandatory")
_BcamIfTab_Object = MibTable
bcamIfTab = _BcamIfTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2)
)
if mibBuilder.loadTexts:
    bcamIfTab.setStatus("mandatory")
_BcamIfTabEntry_Object = MibTableRow
bcamIfTabEntry = _BcamIfTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1)
)
bcamIfTabEntry.setIndexNames(
    (0, "BCAM-MIB", "bcamIfTabNumbers"),
)
if mibBuilder.loadTexts:
    bcamIfTabEntry.setStatus("mandatory")
_BcamIfTabNumbers_Type = Integer32
_BcamIfTabNumbers_Object = MibTableColumn
bcamIfTabNumbers = _BcamIfTabNumbers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 1),
    _BcamIfTabNumbers_Type()
)
bcamIfTabNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumbers.setStatus("mandatory")


class _BcamIfTabName_Type(DisplayString):
    """Custom type bcamIfTabName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamIfTabName_Type.__name__ = "DisplayString"
_BcamIfTabName_Object = MibTableColumn
bcamIfTabName = _BcamIfTabName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 2),
    _BcamIfTabName_Type()
)
bcamIfTabName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabName.setStatus("mandatory")


class _BcamIfTabProfile_Type(Integer32):
    """Custom type bcamIfTabProfile based on Integer32"""
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
        *(("fddi", 7),
          ("llc1", 5),
          ("nealke", 2),
          ("nealkeS", 3),
          ("nealkh", 4),
          ("nealkp", 1),
          ("sinix", 6))
    )


_BcamIfTabProfile_Type.__name__ = "Integer32"
_BcamIfTabProfile_Object = MibTableColumn
bcamIfTabProfile = _BcamIfTabProfile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 3),
    _BcamIfTabProfile_Type()
)
bcamIfTabProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabProfile.setStatus("mandatory")


class _BcamIfTabMnemonicWrite_Type(DisplayString):
    """Custom type bcamIfTabMnemonicWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BcamIfTabMnemonicWrite_Type.__name__ = "DisplayString"
_BcamIfTabMnemonicWrite_Object = MibTableColumn
bcamIfTabMnemonicWrite = _BcamIfTabMnemonicWrite_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 4),
    _BcamIfTabMnemonicWrite_Type()
)
bcamIfTabMnemonicWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMnemonicWrite.setStatus("mandatory")


class _BcamIfTabMnemonicRead_Type(DisplayString):
    """Custom type bcamIfTabMnemonicRead based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BcamIfTabMnemonicRead_Type.__name__ = "DisplayString"
_BcamIfTabMnemonicRead_Object = MibTableColumn
bcamIfTabMnemonicRead = _BcamIfTabMnemonicRead_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 5),
    _BcamIfTabMnemonicRead_Type()
)
bcamIfTabMnemonicRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMnemonicRead.setStatus("mandatory")
_BcamIfTabLanAddress_Type = PhysAddress
_BcamIfTabLanAddress_Object = MibTableColumn
bcamIfTabLanAddress = _BcamIfTabLanAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 6),
    _BcamIfTabLanAddress_Type()
)
bcamIfTabLanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabLanAddress.setStatus("mandatory")


class _BcamIfTabConfigUpdate_Type(Integer32):
    """Custom type bcamIfTabConfigUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("primaryRequested", 2),
          ("updateAllowed", 4),
          ("updateForbidden", 1))
    )


_BcamIfTabConfigUpdate_Type.__name__ = "Integer32"
_BcamIfTabConfigUpdate_Object = MibTableColumn
bcamIfTabConfigUpdate = _BcamIfTabConfigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 7),
    _BcamIfTabConfigUpdate_Type()
)
bcamIfTabConfigUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabConfigUpdate.setStatus("mandatory")


class _BcamIfTabMaxLpdu_Type(Integer32):
    """Custom type bcamIfTabMaxLpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1514,
              4113,
              4494,
              16392,
              65535,
              65549)
        )
    )
    namedValues = NamedValues(
        *(("atm", 65535),
          ("ethernet", 1514),
          ("fddi", 4494),
          ("maxReass", 16392),
          ("nealkh", 65549),
          ("nealkp", 4113))
    )


_BcamIfTabMaxLpdu_Type.__name__ = "Integer32"
_BcamIfTabMaxLpdu_Object = MibTableColumn
bcamIfTabMaxLpdu = _BcamIfTabMaxLpdu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 8),
    _BcamIfTabMaxLpdu_Type()
)
bcamIfTabMaxLpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMaxLpdu.setStatus("mandatory")


class _BcamIfTabL2Monitoring_Type(Integer32):
    """Custom type bcamIfTabL2Monitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BcamIfTabL2Monitoring_Type.__name__ = "Integer32"
_BcamIfTabL2Monitoring_Object = MibTableColumn
bcamIfTabL2Monitoring = _BcamIfTabL2Monitoring_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 9),
    _BcamIfTabL2Monitoring_Type()
)
bcamIfTabL2Monitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabL2Monitoring.setStatus("mandatory")


class _BcamIfTabDevice_Type(Integer32):
    """Custom type bcamIfTabDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("esconCtc", 1)
    )


_BcamIfTabDevice_Type.__name__ = "Integer32"
_BcamIfTabDevice_Object = MibTableColumn
bcamIfTabDevice = _BcamIfTabDevice_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 10),
    _BcamIfTabDevice_Type()
)
bcamIfTabDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabDevice.setStatus("mandatory")


class _BcamIfTabAdminState_Type(Integer32):
    """Custom type bcamIfTabAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("excluded", 4),
          ("included", 1))
    )


_BcamIfTabAdminState_Type.__name__ = "Integer32"
_BcamIfTabAdminState_Object = MibTableColumn
bcamIfTabAdminState = _BcamIfTabAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 11),
    _BcamIfTabAdminState_Type()
)
bcamIfTabAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabAdminState.setStatus("mandatory")


class _BcamIfTabCurrentState_Type(Integer32):
    """Custom type bcamIfTabCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 8),
          ("waitForAct", 1),
          ("waitForDeact", 4),
          ("working", 2))
    )


_BcamIfTabCurrentState_Type.__name__ = "Integer32"
_BcamIfTabCurrentState_Object = MibTableColumn
bcamIfTabCurrentState = _BcamIfTabCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 12),
    _BcamIfTabCurrentState_Type()
)
bcamIfTabCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabCurrentState.setStatus("mandatory")


class _BcamIfTabMode_Type(Integer32):
    """Custom type bcamIfTabMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("broadcastOn", 1),
          ("multicastOn", 2),
          ("shortWaitOn", 4),
          ("slowPollOn", 8),
          ("stopModeOn", 16))
    )


_BcamIfTabMode_Type.__name__ = "Integer32"
_BcamIfTabMode_Object = MibTableColumn
bcamIfTabMode = _BcamIfTabMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 13),
    _BcamIfTabMode_Type()
)
bcamIfTabMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMode.setStatus("mandatory")


class _BcamIfTabPortName_Type(DisplayString):
    """Custom type bcamIfTabPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamIfTabPortName_Type.__name__ = "DisplayString"
_BcamIfTabPortName_Object = MibTableColumn
bcamIfTabPortName = _BcamIfTabPortName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 14),
    _BcamIfTabPortName_Type()
)
bcamIfTabPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabPortName.setStatus("mandatory")


class _BcamIfTabLenTraceOut_Type(Integer32):
    """Custom type bcamIfTabLenTraceOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_BcamIfTabLenTraceOut_Type.__name__ = "Integer32"
_BcamIfTabLenTraceOut_Object = MibTableColumn
bcamIfTabLenTraceOut = _BcamIfTabLenTraceOut_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 15),
    _BcamIfTabLenTraceOut_Type()
)
bcamIfTabLenTraceOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabLenTraceOut.setStatus("mandatory")


class _BcamIfTabLenTraceIn_Type(Integer32):
    """Custom type bcamIfTabLenTraceIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_BcamIfTabLenTraceIn_Type.__name__ = "Integer32"
_BcamIfTabLenTraceIn_Object = MibTableColumn
bcamIfTabLenTraceIn = _BcamIfTabLenTraceIn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 16),
    _BcamIfTabLenTraceIn_Type()
)
bcamIfTabLenTraceIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabLenTraceIn.setStatus("mandatory")
_BcamIfTabNumRouteSwitchings_Type = Integer32
_BcamIfTabNumRouteSwitchings_Object = MibTableColumn
bcamIfTabNumRouteSwitchings = _BcamIfTabNumRouteSwitchings_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 17),
    _BcamIfTabNumRouteSwitchings_Type()
)
bcamIfTabNumRouteSwitchings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumRouteSwitchings.setStatus("mandatory")
_BcamIfTabTimeLastChange_Type = Integer32
_BcamIfTabTimeLastChange_Object = MibTableColumn
bcamIfTabTimeLastChange = _BcamIfTabTimeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 18),
    _BcamIfTabTimeLastChange_Type()
)
bcamIfTabTimeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabTimeLastChange.setStatus("mandatory")


class _BcamIfTabMnemonicDiag_Type(DisplayString):
    """Custom type bcamIfTabMnemonicDiag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BcamIfTabMnemonicDiag_Type.__name__ = "DisplayString"
_BcamIfTabMnemonicDiag_Object = MibTableColumn
bcamIfTabMnemonicDiag = _BcamIfTabMnemonicDiag_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 19),
    _BcamIfTabMnemonicDiag_Type()
)
bcamIfTabMnemonicDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMnemonicDiag.setStatus("mandatory")
_BcamIfTabNumMulticastAddr_Type = Integer32
_BcamIfTabNumMulticastAddr_Object = MibTableColumn
bcamIfTabNumMulticastAddr = _BcamIfTabNumMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 20),
    _BcamIfTabNumMulticastAddr_Type()
)
bcamIfTabNumMulticastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumMulticastAddr.setStatus("mandatory")
_BcamIfTabMulticastAddr1_Type = PhysAddress
_BcamIfTabMulticastAddr1_Object = MibTableColumn
bcamIfTabMulticastAddr1 = _BcamIfTabMulticastAddr1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 21),
    _BcamIfTabMulticastAddr1_Type()
)
bcamIfTabMulticastAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr1.setStatus("mandatory")
_BcamIfTabMulticastAddr2_Type = PhysAddress
_BcamIfTabMulticastAddr2_Object = MibTableColumn
bcamIfTabMulticastAddr2 = _BcamIfTabMulticastAddr2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 22),
    _BcamIfTabMulticastAddr2_Type()
)
bcamIfTabMulticastAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr2.setStatus("mandatory")
_BcamIfTabMulticastAddr3_Type = PhysAddress
_BcamIfTabMulticastAddr3_Object = MibTableColumn
bcamIfTabMulticastAddr3 = _BcamIfTabMulticastAddr3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 23),
    _BcamIfTabMulticastAddr3_Type()
)
bcamIfTabMulticastAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr3.setStatus("mandatory")
_BcamIfTabMulticastAddr4_Type = PhysAddress
_BcamIfTabMulticastAddr4_Object = MibTableColumn
bcamIfTabMulticastAddr4 = _BcamIfTabMulticastAddr4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 24),
    _BcamIfTabMulticastAddr4_Type()
)
bcamIfTabMulticastAddr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr4.setStatus("mandatory")
_BcamIfTabMulticastAddr5_Type = PhysAddress
_BcamIfTabMulticastAddr5_Object = MibTableColumn
bcamIfTabMulticastAddr5 = _BcamIfTabMulticastAddr5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 25),
    _BcamIfTabMulticastAddr5_Type()
)
bcamIfTabMulticastAddr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr5.setStatus("mandatory")
_BcamIfTabMulticastAddr6_Type = PhysAddress
_BcamIfTabMulticastAddr6_Object = MibTableColumn
bcamIfTabMulticastAddr6 = _BcamIfTabMulticastAddr6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 26),
    _BcamIfTabMulticastAddr6_Type()
)
bcamIfTabMulticastAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr6.setStatus("mandatory")
_BcamIfTabMulticastAddr7_Type = PhysAddress
_BcamIfTabMulticastAddr7_Object = MibTableColumn
bcamIfTabMulticastAddr7 = _BcamIfTabMulticastAddr7_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 27),
    _BcamIfTabMulticastAddr7_Type()
)
bcamIfTabMulticastAddr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr7.setStatus("mandatory")
_BcamIfTabMulticastAddr8_Type = PhysAddress
_BcamIfTabMulticastAddr8_Object = MibTableColumn
bcamIfTabMulticastAddr8 = _BcamIfTabMulticastAddr8_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 28),
    _BcamIfTabMulticastAddr8_Type()
)
bcamIfTabMulticastAddr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr8.setStatus("mandatory")
_BcamIfTabMulticastAddr9_Type = PhysAddress
_BcamIfTabMulticastAddr9_Object = MibTableColumn
bcamIfTabMulticastAddr9 = _BcamIfTabMulticastAddr9_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 29),
    _BcamIfTabMulticastAddr9_Type()
)
bcamIfTabMulticastAddr9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr9.setStatus("mandatory")
_BcamIfTabMulticastAddr10_Type = PhysAddress
_BcamIfTabMulticastAddr10_Object = MibTableColumn
bcamIfTabMulticastAddr10 = _BcamIfTabMulticastAddr10_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 30),
    _BcamIfTabMulticastAddr10_Type()
)
bcamIfTabMulticastAddr10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastAddr10.setStatus("mandatory")
_BcamIfTabNumNeaAddress_Type = Integer32
_BcamIfTabNumNeaAddress_Object = MibTableColumn
bcamIfTabNumNeaAddress = _BcamIfTabNumNeaAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 31),
    _BcamIfTabNumNeaAddress_Type()
)
bcamIfTabNumNeaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumNeaAddress.setStatus("mandatory")


class _BcamIfTabNeaAddress1_Type(OctetString):
    """Custom type bcamIfTabNeaAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BcamIfTabNeaAddress1_Type.__name__ = "OctetString"
_BcamIfTabNeaAddress1_Object = MibTableColumn
bcamIfTabNeaAddress1 = _BcamIfTabNeaAddress1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 32),
    _BcamIfTabNeaAddress1_Type()
)
bcamIfTabNeaAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNeaAddress1.setStatus("mandatory")


class _BcamIfTabNeaAddress2_Type(OctetString):
    """Custom type bcamIfTabNeaAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BcamIfTabNeaAddress2_Type.__name__ = "OctetString"
_BcamIfTabNeaAddress2_Object = MibTableColumn
bcamIfTabNeaAddress2 = _BcamIfTabNeaAddress2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 33),
    _BcamIfTabNeaAddress2_Type()
)
bcamIfTabNeaAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNeaAddress2.setStatus("mandatory")


class _BcamIfTabNeaAddress3_Type(OctetString):
    """Custom type bcamIfTabNeaAddress3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BcamIfTabNeaAddress3_Type.__name__ = "OctetString"
_BcamIfTabNeaAddress3_Object = MibTableColumn
bcamIfTabNeaAddress3 = _BcamIfTabNeaAddress3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 34),
    _BcamIfTabNeaAddress3_Type()
)
bcamIfTabNeaAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNeaAddress3.setStatus("mandatory")


class _BcamIfTabNeaAddress4_Type(OctetString):
    """Custom type bcamIfTabNeaAddress4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BcamIfTabNeaAddress4_Type.__name__ = "OctetString"
_BcamIfTabNeaAddress4_Object = MibTableColumn
bcamIfTabNeaAddress4 = _BcamIfTabNeaAddress4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 35),
    _BcamIfTabNeaAddress4_Type()
)
bcamIfTabNeaAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNeaAddress4.setStatus("mandatory")


class _BcamIfTabNeaAddress5_Type(OctetString):
    """Custom type bcamIfTabNeaAddress5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BcamIfTabNeaAddress5_Type.__name__ = "OctetString"
_BcamIfTabNeaAddress5_Object = MibTableColumn
bcamIfTabNeaAddress5 = _BcamIfTabNeaAddress5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 36),
    _BcamIfTabNeaAddress5_Type()
)
bcamIfTabNeaAddress5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNeaAddress5.setStatus("mandatory")


class _BcamIfTabNeaAddress6_Type(OctetString):
    """Custom type bcamIfTabNeaAddress6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BcamIfTabNeaAddress6_Type.__name__ = "OctetString"
_BcamIfTabNeaAddress6_Object = MibTableColumn
bcamIfTabNeaAddress6 = _BcamIfTabNeaAddress6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 37),
    _BcamIfTabNeaAddress6_Type()
)
bcamIfTabNeaAddress6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNeaAddress6.setStatus("mandatory")
_BcamIfTabNumIpAddress_Type = Integer32
_BcamIfTabNumIpAddress_Object = MibTableColumn
bcamIfTabNumIpAddress = _BcamIfTabNumIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 38),
    _BcamIfTabNumIpAddress_Type()
)
bcamIfTabNumIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumIpAddress.setStatus("mandatory")
_BcamIfTabIpAddress1_Type = IpAddress
_BcamIfTabIpAddress1_Object = MibTableColumn
bcamIfTabIpAddress1 = _BcamIfTabIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 39),
    _BcamIfTabIpAddress1_Type()
)
bcamIfTabIpAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIpAddress1.setStatus("mandatory")
_BcamIfTabIpAddress2_Type = IpAddress
_BcamIfTabIpAddress2_Object = MibTableColumn
bcamIfTabIpAddress2 = _BcamIfTabIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 40),
    _BcamIfTabIpAddress2_Type()
)
bcamIfTabIpAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIpAddress2.setStatus("mandatory")
_BcamIfTabIpAddress3_Type = IpAddress
_BcamIfTabIpAddress3_Object = MibTableColumn
bcamIfTabIpAddress3 = _BcamIfTabIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 41),
    _BcamIfTabIpAddress3_Type()
)
bcamIfTabIpAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIpAddress3.setStatus("mandatory")
_BcamIfTabIpAddress4_Type = IpAddress
_BcamIfTabIpAddress4_Object = MibTableColumn
bcamIfTabIpAddress4 = _BcamIfTabIpAddress4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 42),
    _BcamIfTabIpAddress4_Type()
)
bcamIfTabIpAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIpAddress4.setStatus("mandatory")
_BcamIfTabIpAddress5_Type = IpAddress
_BcamIfTabIpAddress5_Object = MibTableColumn
bcamIfTabIpAddress5 = _BcamIfTabIpAddress5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 43),
    _BcamIfTabIpAddress5_Type()
)
bcamIfTabIpAddress5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIpAddress5.setStatus("mandatory")
_BcamIfTabIpAddress6_Type = IpAddress
_BcamIfTabIpAddress6_Object = MibTableColumn
bcamIfTabIpAddress6 = _BcamIfTabIpAddress6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 44),
    _BcamIfTabIpAddress6_Type()
)
bcamIfTabIpAddress6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIpAddress6.setStatus("mandatory")
_BcamIfTabNumInt0Address_Type = Integer32
_BcamIfTabNumInt0Address_Object = MibTableColumn
bcamIfTabNumInt0Address = _BcamIfTabNumInt0Address_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 45),
    _BcamIfTabNumInt0Address_Type()
)
bcamIfTabNumInt0Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumInt0Address.setStatus("mandatory")
_BcamIfTabInt0Address1_Type = PhysAddress
_BcamIfTabInt0Address1_Object = MibTableColumn
bcamIfTabInt0Address1 = _BcamIfTabInt0Address1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 46),
    _BcamIfTabInt0Address1_Type()
)
bcamIfTabInt0Address1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInt0Address1.setStatus("mandatory")
_BcamIfTabInt0Address2_Type = PhysAddress
_BcamIfTabInt0Address2_Object = MibTableColumn
bcamIfTabInt0Address2 = _BcamIfTabInt0Address2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 47),
    _BcamIfTabInt0Address2_Type()
)
bcamIfTabInt0Address2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInt0Address2.setStatus("mandatory")
_BcamIfTabInt0Address3_Type = PhysAddress
_BcamIfTabInt0Address3_Object = MibTableColumn
bcamIfTabInt0Address3 = _BcamIfTabInt0Address3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 48),
    _BcamIfTabInt0Address3_Type()
)
bcamIfTabInt0Address3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInt0Address3.setStatus("mandatory")
_BcamIfTabInt0Address4_Type = PhysAddress
_BcamIfTabInt0Address4_Object = MibTableColumn
bcamIfTabInt0Address4 = _BcamIfTabInt0Address4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 49),
    _BcamIfTabInt0Address4_Type()
)
bcamIfTabInt0Address4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInt0Address4.setStatus("mandatory")
_BcamIfTabInt0Address5_Type = PhysAddress
_BcamIfTabInt0Address5_Object = MibTableColumn
bcamIfTabInt0Address5 = _BcamIfTabInt0Address5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 50),
    _BcamIfTabInt0Address5_Type()
)
bcamIfTabInt0Address5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInt0Address5.setStatus("mandatory")
_BcamIfTabInt0Address6_Type = PhysAddress
_BcamIfTabInt0Address6_Object = MibTableColumn
bcamIfTabInt0Address6 = _BcamIfTabInt0Address6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 51),
    _BcamIfTabInt0Address6_Type()
)
bcamIfTabInt0Address6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInt0Address6.setStatus("mandatory")
_BcamIfTabNumIntfAddress_Type = Integer32
_BcamIfTabNumIntfAddress_Object = MibTableColumn
bcamIfTabNumIntfAddress = _BcamIfTabNumIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 52),
    _BcamIfTabNumIntfAddress_Type()
)
bcamIfTabNumIntfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabNumIntfAddress.setStatus("mandatory")


class _BcamIfTabIntfAddress1_Type(OctetString):
    """Custom type bcamIfTabIntfAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamIfTabIntfAddress1_Type.__name__ = "OctetString"
_BcamIfTabIntfAddress1_Object = MibTableColumn
bcamIfTabIntfAddress1 = _BcamIfTabIntfAddress1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 53),
    _BcamIfTabIntfAddress1_Type()
)
bcamIfTabIntfAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIntfAddress1.setStatus("mandatory")


class _BcamIfTabIntfAddress2_Type(OctetString):
    """Custom type bcamIfTabIntfAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamIfTabIntfAddress2_Type.__name__ = "OctetString"
_BcamIfTabIntfAddress2_Object = MibTableColumn
bcamIfTabIntfAddress2 = _BcamIfTabIntfAddress2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 54),
    _BcamIfTabIntfAddress2_Type()
)
bcamIfTabIntfAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIntfAddress2.setStatus("mandatory")


class _BcamIfTabIntfAddress3_Type(OctetString):
    """Custom type bcamIfTabIntfAddress3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamIfTabIntfAddress3_Type.__name__ = "OctetString"
_BcamIfTabIntfAddress3_Object = MibTableColumn
bcamIfTabIntfAddress3 = _BcamIfTabIntfAddress3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 55),
    _BcamIfTabIntfAddress3_Type()
)
bcamIfTabIntfAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIntfAddress3.setStatus("mandatory")


class _BcamIfTabIntfAddress4_Type(OctetString):
    """Custom type bcamIfTabIntfAddress4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamIfTabIntfAddress4_Type.__name__ = "OctetString"
_BcamIfTabIntfAddress4_Object = MibTableColumn
bcamIfTabIntfAddress4 = _BcamIfTabIntfAddress4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 56),
    _BcamIfTabIntfAddress4_Type()
)
bcamIfTabIntfAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIntfAddress4.setStatus("mandatory")


class _BcamIfTabIntfAddress5_Type(OctetString):
    """Custom type bcamIfTabIntfAddress5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamIfTabIntfAddress5_Type.__name__ = "OctetString"
_BcamIfTabIntfAddress5_Object = MibTableColumn
bcamIfTabIntfAddress5 = _BcamIfTabIntfAddress5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 57),
    _BcamIfTabIntfAddress5_Type()
)
bcamIfTabIntfAddress5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIntfAddress5.setStatus("mandatory")


class _BcamIfTabIntfAddress6_Type(OctetString):
    """Custom type bcamIfTabIntfAddress6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BcamIfTabIntfAddress6_Type.__name__ = "OctetString"
_BcamIfTabIntfAddress6_Object = MibTableColumn
bcamIfTabIntfAddress6 = _BcamIfTabIntfAddress6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 58),
    _BcamIfTabIntfAddress6_Type()
)
bcamIfTabIntfAddress6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIntfAddress6.setStatus("mandatory")
_BcamIfTabBytesOutHighs_Type = Counter32
_BcamIfTabBytesOutHighs_Object = MibTableColumn
bcamIfTabBytesOutHighs = _BcamIfTabBytesOutHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 59),
    _BcamIfTabBytesOutHighs_Type()
)
bcamIfTabBytesOutHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabBytesOutHighs.setStatus("mandatory")
_BcamIfTabBytesOutLows_Type = Counter32
_BcamIfTabBytesOutLows_Object = MibTableColumn
bcamIfTabBytesOutLows = _BcamIfTabBytesOutLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 60),
    _BcamIfTabBytesOutLows_Type()
)
bcamIfTabBytesOutLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabBytesOutLows.setStatus("mandatory")
_BcamIfTabBytesInHighs_Type = Counter32
_BcamIfTabBytesInHighs_Object = MibTableColumn
bcamIfTabBytesInHighs = _BcamIfTabBytesInHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 61),
    _BcamIfTabBytesInHighs_Type()
)
bcamIfTabBytesInHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabBytesInHighs.setStatus("mandatory")
_BcamIfTabBytesInLows_Type = Counter32
_BcamIfTabBytesInLows_Object = MibTableColumn
bcamIfTabBytesInLows = _BcamIfTabBytesInLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 62),
    _BcamIfTabBytesInLows_Type()
)
bcamIfTabBytesInLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabBytesInLows.setStatus("mandatory")
_BcamIfTabIOsOutHighs_Type = Counter32
_BcamIfTabIOsOutHighs_Object = MibTableColumn
bcamIfTabIOsOutHighs = _BcamIfTabIOsOutHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 63),
    _BcamIfTabIOsOutHighs_Type()
)
bcamIfTabIOsOutHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIOsOutHighs.setStatus("mandatory")
_BcamIfTabIOsOutLows_Type = Counter32
_BcamIfTabIOsOutLows_Object = MibTableColumn
bcamIfTabIOsOutLows = _BcamIfTabIOsOutLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 64),
    _BcamIfTabIOsOutLows_Type()
)
bcamIfTabIOsOutLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIOsOutLows.setStatus("mandatory")
_BcamIfTabIOsInHighs_Type = Counter32
_BcamIfTabIOsInHighs_Object = MibTableColumn
bcamIfTabIOsInHighs = _BcamIfTabIOsInHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 65),
    _BcamIfTabIOsInHighs_Type()
)
bcamIfTabIOsInHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIOsInHighs.setStatus("mandatory")
_BcamIfTabIOsInLows_Type = Counter32
_BcamIfTabIOsInLows_Object = MibTableColumn
bcamIfTabIOsInLows = _BcamIfTabIOsInLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 66),
    _BcamIfTabIOsInLows_Type()
)
bcamIfTabIOsInLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIOsInLows.setStatus("mandatory")
_BcamIfTabOutputStops_Type = Counter32
_BcamIfTabOutputStops_Object = MibTableColumn
bcamIfTabOutputStops = _BcamIfTabOutputStops_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 67),
    _BcamIfTabOutputStops_Type()
)
bcamIfTabOutputStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabOutputStops.setStatus("mandatory")
_BcamIfTabInputStops_Type = Counter32
_BcamIfTabInputStops_Object = MibTableColumn
bcamIfTabInputStops = _BcamIfTabInputStops_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 68),
    _BcamIfTabInputStops_Type()
)
bcamIfTabInputStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInputStops.setStatus("mandatory")
_BcamIfTabIOErrorOuts_Type = Counter32
_BcamIfTabIOErrorOuts_Object = MibTableColumn
bcamIfTabIOErrorOuts = _BcamIfTabIOErrorOuts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 69),
    _BcamIfTabIOErrorOuts_Type()
)
bcamIfTabIOErrorOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIOErrorOuts.setStatus("mandatory")
_BcamIfTabIOErrorIns_Type = Counter32
_BcamIfTabIOErrorIns_Object = MibTableColumn
bcamIfTabIOErrorIns = _BcamIfTabIOErrorIns_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 70),
    _BcamIfTabIOErrorIns_Type()
)
bcamIfTabIOErrorIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabIOErrorIns.setStatus("mandatory")
_BcamIfTabPacketsNotReceiveds_Type = Counter32
_BcamIfTabPacketsNotReceiveds_Object = MibTableColumn
bcamIfTabPacketsNotReceiveds = _BcamIfTabPacketsNotReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 71),
    _BcamIfTabPacketsNotReceiveds_Type()
)
bcamIfTabPacketsNotReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabPacketsNotReceiveds.setStatus("mandatory")
_BcamIfTabInPacketsLanHighs_Type = Counter32
_BcamIfTabInPacketsLanHighs_Object = MibTableColumn
bcamIfTabInPacketsLanHighs = _BcamIfTabInPacketsLanHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 72),
    _BcamIfTabInPacketsLanHighs_Type()
)
bcamIfTabInPacketsLanHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInPacketsLanHighs.setStatus("mandatory")
_BcamIfTabInPacketsLanLows_Type = Counter32
_BcamIfTabInPacketsLanLows_Object = MibTableColumn
bcamIfTabInPacketsLanLows = _BcamIfTabInPacketsLanLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 73),
    _BcamIfTabInPacketsLanLows_Type()
)
bcamIfTabInPacketsLanLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabInPacketsLanLows.setStatus("mandatory")
_BcamIfTabOutPacketsLanHighs_Type = Counter32
_BcamIfTabOutPacketsLanHighs_Object = MibTableColumn
bcamIfTabOutPacketsLanHighs = _BcamIfTabOutPacketsLanHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 74),
    _BcamIfTabOutPacketsLanHighs_Type()
)
bcamIfTabOutPacketsLanHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabOutPacketsLanHighs.setStatus("mandatory")
_BcamIfTabOutPacketsLanLows_Type = Counter32
_BcamIfTabOutPacketsLanLows_Object = MibTableColumn
bcamIfTabOutPacketsLanLows = _BcamIfTabOutPacketsLanLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 75),
    _BcamIfTabOutPacketsLanLows_Type()
)
bcamIfTabOutPacketsLanLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabOutPacketsLanLows.setStatus("mandatory")
_BcamIfTabUnicastInHighs_Type = Counter32
_BcamIfTabUnicastInHighs_Object = MibTableColumn
bcamIfTabUnicastInHighs = _BcamIfTabUnicastInHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 76),
    _BcamIfTabUnicastInHighs_Type()
)
bcamIfTabUnicastInHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabUnicastInHighs.setStatus("mandatory")
_BcamIfTabUnicastInLows_Type = Counter32
_BcamIfTabUnicastInLows_Object = MibTableColumn
bcamIfTabUnicastInLows = _BcamIfTabUnicastInLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 77),
    _BcamIfTabUnicastInLows_Type()
)
bcamIfTabUnicastInLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabUnicastInLows.setStatus("mandatory")
_BcamIfTabUnicastOutHighs_Type = Counter32
_BcamIfTabUnicastOutHighs_Object = MibTableColumn
bcamIfTabUnicastOutHighs = _BcamIfTabUnicastOutHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 78),
    _BcamIfTabUnicastOutHighs_Type()
)
bcamIfTabUnicastOutHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabUnicastOutHighs.setStatus("mandatory")
_BcamIfTabUnicastOutLows_Type = Counter32
_BcamIfTabUnicastOutLows_Object = MibTableColumn
bcamIfTabUnicastOutLows = _BcamIfTabUnicastOutLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 79),
    _BcamIfTabUnicastOutLows_Type()
)
bcamIfTabUnicastOutLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabUnicastOutLows.setStatus("mandatory")
_BcamIfTabMulticastInHighs_Type = Counter32
_BcamIfTabMulticastInHighs_Object = MibTableColumn
bcamIfTabMulticastInHighs = _BcamIfTabMulticastInHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 80),
    _BcamIfTabMulticastInHighs_Type()
)
bcamIfTabMulticastInHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastInHighs.setStatus("mandatory")
_BcamIfTabMulticastInLows_Type = Counter32
_BcamIfTabMulticastInLows_Object = MibTableColumn
bcamIfTabMulticastInLows = _BcamIfTabMulticastInLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 81),
    _BcamIfTabMulticastInLows_Type()
)
bcamIfTabMulticastInLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastInLows.setStatus("mandatory")
_BcamIfTabMulticastOutHighs_Type = Counter32
_BcamIfTabMulticastOutHighs_Object = MibTableColumn
bcamIfTabMulticastOutHighs = _BcamIfTabMulticastOutHighs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 82),
    _BcamIfTabMulticastOutHighs_Type()
)
bcamIfTabMulticastOutHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastOutHighs.setStatus("mandatory")
_BcamIfTabMulticastOutLows_Type = Counter32
_BcamIfTabMulticastOutLows_Object = MibTableColumn
bcamIfTabMulticastOutLows = _BcamIfTabMulticastOutLows_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 83),
    _BcamIfTabMulticastOutLows_Type()
)
bcamIfTabMulticastOutLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabMulticastOutLows.setStatus("mandatory")
_BcamIfTabErrorPacketIns_Type = Counter32
_BcamIfTabErrorPacketIns_Object = MibTableColumn
bcamIfTabErrorPacketIns = _BcamIfTabErrorPacketIns_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 84),
    _BcamIfTabErrorPacketIns_Type()
)
bcamIfTabErrorPacketIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabErrorPacketIns.setStatus("mandatory")
_BcamIfTabErrorPacketOuts_Type = Counter32
_BcamIfTabErrorPacketOuts_Object = MibTableColumn
bcamIfTabErrorPacketOuts = _BcamIfTabErrorPacketOuts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 85),
    _BcamIfTabErrorPacketOuts_Type()
)
bcamIfTabErrorPacketOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabErrorPacketOuts.setStatus("mandatory")
_BcamIfTabDiscardIns_Type = Counter32
_BcamIfTabDiscardIns_Object = MibTableColumn
bcamIfTabDiscardIns = _BcamIfTabDiscardIns_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 86),
    _BcamIfTabDiscardIns_Type()
)
bcamIfTabDiscardIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabDiscardIns.setStatus("mandatory")
_BcamIfTabDiscardOuts_Type = Counter32
_BcamIfTabDiscardOuts_Object = MibTableColumn
bcamIfTabDiscardOuts = _BcamIfTabDiscardOuts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 87),
    _BcamIfTabDiscardOuts_Type()
)
bcamIfTabDiscardOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabDiscardOuts.setStatus("mandatory")
_BcamIfTabUnknownProtoIns_Type = Counter32
_BcamIfTabUnknownProtoIns_Object = MibTableColumn
bcamIfTabUnknownProtoIns = _BcamIfTabUnknownProtoIns_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 88),
    _BcamIfTabUnknownProtoIns_Type()
)
bcamIfTabUnknownProtoIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabUnknownProtoIns.setStatus("mandatory")


class _BcamIfTabTraceState_Type(Integer32):
    """Custom type bcamIfTabTraceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hold", 4),
          ("running", 1),
          ("save", 2),
          ("stopped", 8))
    )


_BcamIfTabTraceState_Type.__name__ = "Integer32"
_BcamIfTabTraceState_Object = MibTableColumn
bcamIfTabTraceState = _BcamIfTabTraceState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 89),
    _BcamIfTabTraceState_Type()
)
bcamIfTabTraceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabTraceState.setStatus("mandatory")


class _BcamIfTabTraceNumberBuffer_Type(Integer32):
    """Custom type bcamIfTabTraceNumberBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BcamIfTabTraceNumberBuffer_Type.__name__ = "Integer32"
_BcamIfTabTraceNumberBuffer_Object = MibTableColumn
bcamIfTabTraceNumberBuffer = _BcamIfTabTraceNumberBuffer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 90),
    _BcamIfTabTraceNumberBuffer_Type()
)
bcamIfTabTraceNumberBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabTraceNumberBuffer.setStatus("mandatory")


class _BcamIfTabTraceBufferLen_Type(Integer32):
    """Custom type bcamIfTabTraceBufferLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_BcamIfTabTraceBufferLen_Type.__name__ = "Integer32"
_BcamIfTabTraceBufferLen_Object = MibTableColumn
bcamIfTabTraceBufferLen = _BcamIfTabTraceBufferLen_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 8, 2, 1, 91),
    _BcamIfTabTraceBufferLen_Type()
)
bcamIfTabTraceBufferLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamIfTabTraceBufferLen.setStatus("mandatory")
_BcamRouter_ObjectIdentity = ObjectIdentity
bcamRouter = _BcamRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9)
)
_BcamRouterNumTable_Type = Integer32
_BcamRouterNumTable_Object = MibScalar
bcamRouterNumTable = _BcamRouterNumTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 1),
    _BcamRouterNumTable_Type()
)
bcamRouterNumTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouterNumTable.setStatus("mandatory")
_BcamRouterTab_Object = MibTable
bcamRouterTab = _BcamRouterTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2)
)
if mibBuilder.loadTexts:
    bcamRouterTab.setStatus("mandatory")
_BcamRouterTabEntry_Object = MibTableRow
bcamRouterTabEntry = _BcamRouterTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2, 1)
)
bcamRouterTabEntry.setIndexNames(
    (0, "BCAM-MIB", "bcamRouterTabIpLow"),
    (0, "BCAM-MIB", "bcamRouterTabIpHigh"),
    (0, "BCAM-MIB", "bcamRouterTabIpLocal"),
)
if mibBuilder.loadTexts:
    bcamRouterTabEntry.setStatus("mandatory")
_BcamRouterTabIpLow_Type = IpAddress
_BcamRouterTabIpLow_Object = MibTableColumn
bcamRouterTabIpLow = _BcamRouterTabIpLow_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2, 1, 1),
    _BcamRouterTabIpLow_Type()
)
bcamRouterTabIpLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouterTabIpLow.setStatus("mandatory")
_BcamRouterTabIpHigh_Type = IpAddress
_BcamRouterTabIpHigh_Object = MibTableColumn
bcamRouterTabIpHigh = _BcamRouterTabIpHigh_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2, 1, 2),
    _BcamRouterTabIpHigh_Type()
)
bcamRouterTabIpHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouterTabIpHigh.setStatus("mandatory")
_BcamRouterTabIpLocal_Type = IpAddress
_BcamRouterTabIpLocal_Object = MibTableColumn
bcamRouterTabIpLocal = _BcamRouterTabIpLocal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2, 1, 3),
    _BcamRouterTabIpLocal_Type()
)
bcamRouterTabIpLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouterTabIpLocal.setStatus("mandatory")
_BcamRouterTabIpRouter_Type = IpAddress
_BcamRouterTabIpRouter_Object = MibTableColumn
bcamRouterTabIpRouter = _BcamRouterTabIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2, 1, 4),
    _BcamRouterTabIpRouter_Type()
)
bcamRouterTabIpRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouterTabIpRouter.setStatus("mandatory")
_BcamRouterTabNumRouter_Type = Integer32
_BcamRouterTabNumRouter_Object = MibTableColumn
bcamRouterTabNumRouter = _BcamRouterTabNumRouter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 9, 2, 1, 5),
    _BcamRouterTabNumRouter_Type()
)
bcamRouterTabNumRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamRouterTabNumRouter.setStatus("mandatory")
_BcamHost_ObjectIdentity = ObjectIdentity
bcamHost = _BcamHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10)
)
_BcamHostNumTable_Type = Integer32
_BcamHostNumTable_Object = MibScalar
bcamHostNumTable = _BcamHostNumTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 1),
    _BcamHostNumTable_Type()
)
bcamHostNumTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamHostNumTable.setStatus("mandatory")
_BcamHostTab_Object = MibTable
bcamHostTab = _BcamHostTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2)
)
if mibBuilder.loadTexts:
    bcamHostTab.setStatus("mandatory")
_BcamHostTabEntry_Object = MibTableRow
bcamHostTabEntry = _BcamHostTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2, 1)
)
bcamHostTabEntry.setIndexNames(
    (0, "BCAM-MIB", "bcamHostTabNumber"),
)
if mibBuilder.loadTexts:
    bcamHostTabEntry.setStatus("mandatory")
_BcamHostTabNumber_Type = Integer32
_BcamHostTabNumber_Object = MibTableColumn
bcamHostTabNumber = _BcamHostTabNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2, 1, 1),
    _BcamHostTabNumber_Type()
)
bcamHostTabNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamHostTabNumber.setStatus("mandatory")


class _BcamHostTabName_Type(DisplayString):
    """Custom type bcamHostTabName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BcamHostTabName_Type.__name__ = "DisplayString"
_BcamHostTabName_Object = MibTableColumn
bcamHostTabName = _BcamHostTabName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2, 1, 2),
    _BcamHostTabName_Type()
)
bcamHostTabName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamHostTabName.setStatus("mandatory")


class _BcamHostTabSocketName_Type(DisplayString):
    """Custom type bcamHostTabSocketName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BcamHostTabSocketName_Type.__name__ = "DisplayString"
_BcamHostTabSocketName_Object = MibTableColumn
bcamHostTabSocketName = _BcamHostTabSocketName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2, 1, 3),
    _BcamHostTabSocketName_Type()
)
bcamHostTabSocketName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamHostTabSocketName.setStatus("mandatory")


class _BcamHostTabTyp_Type(Integer32):
    """Custom type bcamHostTabTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("virtual", 2))
    )


_BcamHostTabTyp_Type.__name__ = "Integer32"
_BcamHostTabTyp_Object = MibTableColumn
bcamHostTabTyp = _BcamHostTabTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2, 1, 4),
    _BcamHostTabTyp_Type()
)
bcamHostTabTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamHostTabTyp.setStatus("mandatory")


class _BcamHostTabState_Type(Integer32):
    """Custom type bcamHostTabState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("included", 2))
    )


_BcamHostTabState_Type.__name__ = "Integer32"
_BcamHostTabState_Object = MibTableColumn
bcamHostTabState = _BcamHostTabState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 10, 2, 1, 5),
    _BcamHostTabState_Type()
)
bcamHostTabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcamHostTabState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bcamTrapOutPoolOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 301)
)
bcamTrapOutPoolOver.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamMemoryPoolOutputLimitTrap"),
        ("BCAM-MIB", "bcamTrapOutPoolOverCurrent"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapOutPoolOver.setStatus(
        ""
    )

bcamTrapOutPoolUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 302)
)
bcamTrapOutPoolUnder.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamMemoryPoolOutputLimitTrap"),
        ("BCAM-MIB", "bcamTrapOutPoolUnderCurrent"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapOutPoolUnder.setStatus(
        ""
    )

bcamTrapInPoolOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 303)
)
bcamTrapInPoolOver.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamMemoryPoolInputLimitTrap"),
        ("BCAM-MIB", "bcamTrapInPoolOverCurrent"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapInPoolOver.setStatus(
        ""
    )

bcamTrapInPoolUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 304)
)
bcamTrapInPoolUnder.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamMemoryPoolInputLimitTrap"),
        ("BCAM-MIB", "bcamTrapInPoolUnderCurrent"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapInPoolUnder.setStatus(
        ""
    )

bcamTrapLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 305)
)
bcamTrapLinkUp.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamIfTabNumbers"),
        ("BCAM-MIB", "bcamIfTabName"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapLinkUp.setStatus(
        ""
    )

bcamTrapLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 306)
)
bcamTrapLinkDown.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamIfTabNumbers"),
        ("BCAM-MIB", "bcamIfTabName"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapLinkDown.setStatus(
        ""
    )

bcamTrapSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 17, 0, 307)
)
bcamTrapSystemUp.setObjects(
      *(("BCAM-MIB", "bcamGlobalUpTime"),
        ("BCAM-MIB", "bcamGlobalHostName"),
        ("BCAM-MIB", "bcamTrapString"))
)
if mibBuilder.loadTexts:
    bcamTrapSystemUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCAM-MIB",
    **{"PhysAddress": PhysAddress,
       "sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniBcam": sniBcam,
       "bcamTrapOutPoolOver": bcamTrapOutPoolOver,
       "bcamTrapOutPoolUnder": bcamTrapOutPoolUnder,
       "bcamTrapInPoolOver": bcamTrapInPoolOver,
       "bcamTrapInPoolUnder": bcamTrapInPoolUnder,
       "bcamTrapLinkUp": bcamTrapLinkUp,
       "bcamTrapLinkDown": bcamTrapLinkDown,
       "bcamTrapSystemUp": bcamTrapSystemUp,
       "bcamTrap": bcamTrap,
       "bcamTrapString": bcamTrapString,
       "bcamTrapOutPoolOverCurrent": bcamTrapOutPoolOverCurrent,
       "bcamTrapOutPoolUnderCurrent": bcamTrapOutPoolUnderCurrent,
       "bcamTrapInPoolOverCurrent": bcamTrapInPoolOverCurrent,
       "bcamTrapInPoolUnderCurrent": bcamTrapInPoolUnderCurrent,
       "bcamGlobal": bcamGlobal,
       "bcamGlobalBcamVersion": bcamGlobalBcamVersion,
       "bcamGlobalMibVersion": bcamGlobalMibVersion,
       "bcamGlobalUpTime": bcamGlobalUpTime,
       "bcamGlobalPortNonpriv": bcamGlobalPortNonpriv,
       "bcamGlobalPortFree": bcamGlobalPortFree,
       "bcamGlobalNumBitmap": bcamGlobalNumBitmap,
       "bcamGlobalMaxRemoteIp": bcamGlobalMaxRemoteIp,
       "bcamGlobalEsCreationIp": bcamGlobalEsCreationIp,
       "bcamGlobalEsCreationIso": bcamGlobalEsCreationIso,
       "bcamGlobalBroadcast": bcamGlobalBroadcast,
       "bcamGlobalArp": bcamGlobalArp,
       "bcamGlobalRarp": bcamGlobalRarp,
       "bcamGlobalInWaitLimit1": bcamGlobalInWaitLimit1,
       "bcamGlobalInWaitLimit2": bcamGlobalInWaitLimit2,
       "bcamGlobalInWaitLimit3": bcamGlobalInWaitLimit3,
       "bcamGlobalInWaitLimit4": bcamGlobalInWaitLimit4,
       "bcamGlobalInWaitChange": bcamGlobalInWaitChange,
       "bcamGlobalInWaitSet": bcamGlobalInWaitSet,
       "bcamGlobalReactLimit1": bcamGlobalReactLimit1,
       "bcamGlobalReactLimit2": bcamGlobalReactLimit2,
       "bcamGlobalReactLimit3": bcamGlobalReactLimit3,
       "bcamGlobalReactLimit4": bcamGlobalReactLimit4,
       "bcamGlobalReactChange": bcamGlobalReactChange,
       "bcamGlobalReactSet": bcamGlobalReactSet,
       "bcamGlobalInProcLimit1": bcamGlobalInProcLimit1,
       "bcamGlobalInProcLimit2": bcamGlobalInProcLimit2,
       "bcamGlobalInProcLimit3": bcamGlobalInProcLimit3,
       "bcamGlobalInProcLimit4": bcamGlobalInProcLimit4,
       "bcamGlobalInProcChange": bcamGlobalInProcChange,
       "bcamGlobalInProcSet": bcamGlobalInProcSet,
       "bcamGlobalOutProcLimit1": bcamGlobalOutProcLimit1,
       "bcamGlobalOutProcLimit2": bcamGlobalOutProcLimit2,
       "bcamGlobalOutProcLimit3": bcamGlobalOutProcLimit3,
       "bcamGlobalOutProcLimit4": bcamGlobalOutProcLimit4,
       "bcamGlobalOutProcChange": bcamGlobalOutProcChange,
       "bcamGlobalOutProcSet": bcamGlobalOutProcSet,
       "bcamGlobalSnmpRelease": bcamGlobalSnmpRelease,
       "bcamGlobalTrapPollInterval": bcamGlobalTrapPollInterval,
       "bcamGlobalFileApplTable": bcamGlobalFileApplTable,
       "bcamGlobalFileSocketHostTable": bcamGlobalFileSocketHostTable,
       "bcamGlobalFileProcTable": bcamGlobalFileProcTable,
       "bcamGlobalAccessProcTable": bcamGlobalAccessProcTable,
       "bcamGlobalHostName": bcamGlobalHostName,
       "bcamMemory": bcamMemory,
       "bcamMemoryClass3": bcamMemoryClass3,
       "bcamMemoryClass4": bcamMemoryClass4,
       "bcamMemoryLenLongEventSlot": bcamMemoryLenLongEventSlot,
       "bcamMemoryOccLongEventSlot": bcamMemoryOccLongEventSlot,
       "bcamMemoryLenShortEventSlot": bcamMemoryLenShortEventSlot,
       "bcamMemoryOccShortEventSlot": bcamMemoryOccShortEventSlot,
       "bcamMemoryLenTransParamSlot": bcamMemoryLenTransParamSlot,
       "bcamMemoryOccTransParamSlot": bcamMemoryOccTransParamSlot,
       "bcamMemoryLenSnmpParamSlot": bcamMemoryLenSnmpParamSlot,
       "bcamMemoryOccSnmpParamSlot": bcamMemoryOccSnmpParamSlot,
       "bcamMemoryLenApplCb": bcamMemoryLenApplCb,
       "bcamMemoryOccApplCb": bcamMemoryOccApplCb,
       "bcamMemoryLenEnaCb": bcamMemoryLenEnaCb,
       "bcamMemoryOccEnaCb": bcamMemoryOccEnaCb,
       "bcamMemoryLenExtApplCb": bcamMemoryLenExtApplCb,
       "bcamMemoryOccExtApplCb": bcamMemoryOccExtApplCb,
       "bcamMemoryLenShortResConn2": bcamMemoryLenShortResConn2,
       "bcamMemoryOccShortResConn2": bcamMemoryOccShortResConn2,
       "bcamMemoryLenLongResConn2": bcamMemoryLenLongResConn2,
       "bcamMemoryOccLongResConn2": bcamMemoryOccLongResConn2,
       "bcamMemoryLenShortPagConn1": bcamMemoryLenShortPagConn1,
       "bcamMemoryOccShortPagConn1": bcamMemoryOccShortPagConn1,
       "bcamMemoryLenSnmpConn": bcamMemoryLenSnmpConn,
       "bcamMemoryOccSnmpConn": bcamMemoryOccSnmpConn,
       "bcamMemoryLenLongPagConn1": bcamMemoryLenLongPagConn1,
       "bcamMemoryOccLongPagConn1": bcamMemoryOccLongPagConn1,
       "bcamMemoryLenShortPagConn2": bcamMemoryLenShortPagConn2,
       "bcamMemoryOccShortPagConn2": bcamMemoryOccShortPagConn2,
       "bcamMemoryPoolInputCurrent": bcamMemoryPoolInputCurrent,
       "bcamMemoryPoolInputResume": bcamMemoryPoolInputResume,
       "bcamMemoryPoolInputMonMax": bcamMemoryPoolInputMonMax,
       "bcamMemoryPoolInputMonMin": bcamMemoryPoolInputMonMin,
       "bcamMemoryPoolInputLimit": bcamMemoryPoolInputLimit,
       "bcamMemoryPoolInputLimitTrap": bcamMemoryPoolInputLimitTrap,
       "bcamMemoryPoolMaxResident": bcamMemoryPoolMaxResident,
       "bcamMemoryPoolMaxPageable": bcamMemoryPoolMaxPageable,
       "bcamMemoryPoolInputMaxPageable": bcamMemoryPoolInputMaxPageable,
       "bcamMemoryPoolOutputCurrent": bcamMemoryPoolOutputCurrent,
       "bcamMemoryPoolOutputResume": bcamMemoryPoolOutputResume,
       "bcamMemoryPoolOutputMonMax": bcamMemoryPoolOutputMonMax,
       "bcamMemoryPoolOutputMonMin": bcamMemoryPoolOutputMonMin,
       "bcamMemoryPoolOutputLimit": bcamMemoryPoolOutputLimit,
       "bcamMemoryPoolOutputLimitTrap": bcamMemoryPoolOutputLimitTrap,
       "bcamMemoryPoolMaxCells": bcamMemoryPoolMaxCells,
       "bcamMemoryPoolOutputMaxPageable": bcamMemoryPoolOutputMaxPageable,
       "bcamMemoryPoolRoutingCurrent": bcamMemoryPoolRoutingCurrent,
       "bcamMemoryPoolRoutingLimit": bcamMemoryPoolRoutingLimit,
       "bcamMemoryPoolPageableCurrent": bcamMemoryPoolPageableCurrent,
       "bcamMemoryPoolPageableFixed": bcamMemoryPoolPageableFixed,
       "bcamMemoryCellReqSucc": bcamMemoryCellReqSucc,
       "bcamMemoryCellReqResOutExceed": bcamMemoryCellReqResOutExceed,
       "bcamMemoryCellReqResInExceed": bcamMemoryCellReqResInExceed,
       "bcamMemoryCellReqTempExceed": bcamMemoryCellReqTempExceed,
       "bcamMemoryCellReqBitmapFull": bcamMemoryCellReqBitmapFull,
       "bcamMemoryCellReqNoMemory": bcamMemoryCellReqNoMemory,
       "bcamMemoryCellReqPagInExceed": bcamMemoryCellReqPagInExceed,
       "bcamMemoryCellReqPagOutExceed": bcamMemoryCellReqPagOutExceed,
       "bcamTrace": bcamTrace,
       "bcamTraceSavingState": bcamTraceSavingState,
       "bcamTraceFilename": bcamTraceFilename,
       "bcamTraceMaxFilesize": bcamTraceMaxFilesize,
       "bcamTraceNumberFiles": bcamTraceNumberFiles,
       "bcamTraceAdmState": bcamTraceAdmState,
       "bcamTraceAdmNumberBuffer": bcamTraceAdmNumberBuffer,
       "bcamTraceAdmBufferLen": bcamTraceAdmBufferLen,
       "bcamTraceBasicState": bcamTraceBasicState,
       "bcamTraceBasicNumberBuffer": bcamTraceBasicNumberBuffer,
       "bcamTraceBasicBufferLen": bcamTraceBasicBufferLen,
       "bcamTraceConnState": bcamTraceConnState,
       "bcamTraceConnNumberBuffer": bcamTraceConnNumberBuffer,
       "bcamTraceConnBufferLen": bcamTraceConnBufferLen,
       "bcamTraceLocalState": bcamTraceLocalState,
       "bcamTraceLocalNumberBuffer": bcamTraceLocalNumberBuffer,
       "bcamTraceLocalBufferLen": bcamTraceLocalBufferLen,
       "bcamTraceMappingState": bcamTraceMappingState,
       "bcamTraceMappingNumberBuffer": bcamTraceMappingNumberBuffer,
       "bcamTraceMappingBufferLen": bcamTraceMappingBufferLen,
       "bcamTraceMgmtState": bcamTraceMgmtState,
       "bcamTraceMgmtNumberBuffer": bcamTraceMgmtNumberBuffer,
       "bcamTraceMgmtBufferLen": bcamTraceMgmtBufferLen,
       "bcamTraceNetState": bcamTraceNetState,
       "bcamTraceNetNumberBuffer": bcamTraceNetNumberBuffer,
       "bcamTraceNetBufferLen": bcamTraceNetBufferLen,
       "bcamTraceSnmpState": bcamTraceSnmpState,
       "bcamTraceSnmpNumberBuffer": bcamTraceSnmpNumberBuffer,
       "bcamTraceSnmpBufferLen": bcamTraceSnmpBufferLen,
       "bcamTraceTransState": bcamTraceTransState,
       "bcamTraceTransNumberBuffer": bcamTraceTransNumberBuffer,
       "bcamTraceTransBufferLen": bcamTraceTransBufferLen,
       "bcamTraceInfoState": bcamTraceInfoState,
       "bcamTraceInfoNumberBuffer": bcamTraceInfoNumberBuffer,
       "bcamTraceInfoBufferLen": bcamTraceInfoBufferLen,
       "bcamTsap": bcamTsap,
       "bcamTsapCurrOpen": bcamTsapCurrOpen,
       "bcamTsapTotOpen": bcamTsapTotOpen,
       "bcamTsapSendCall": bcamTsapSendCall,
       "bcamTsapSendByteHigh": bcamTsapSendByteHigh,
       "bcamTsapSendByteLow": bcamTsapSendByteLow,
       "bcamTsapRecvCall": bcamTsapRecvCall,
       "bcamTsapRecvByteHigh": bcamTsapRecvByteHigh,
       "bcamTsapRecvByteLow": bcamTsapRecvByteLow,
       "bcamTsapSendCallCless": bcamTsapSendCallCless,
       "bcamTsapSendByteClessHigh": bcamTsapSendByteClessHigh,
       "bcamTsapSendByteClessLow": bcamTsapSendByteClessLow,
       "bcamTsapRecvCallCless": bcamTsapRecvCallCless,
       "bcamTsapRecvByteClessHigh": bcamTsapRecvByteClessHigh,
       "bcamTsapRecvByteClessLow": bcamTsapRecvByteClessLow,
       "bcamTsapNumTable": bcamTsapNumTable,
       "bcamTsapMaxTsap": bcamTsapMaxTsap,
       "bcamTsapMaxTsapTask": bcamTsapMaxTsapTask,
       "bcamTsapMaxCepTsap": bcamTsapMaxCepTsap,
       "bcamTsapRejTsap": bcamTsapRejTsap,
       "bcamTsapRejTsapTask": bcamTsapRejTsapTask,
       "bcamTsapRejCepTsap": bcamTsapRejCepTsap,
       "bcamTsapTab": bcamTsapTab,
       "bcamTsapTabEntry": bcamTsapTabEntry,
       "bcamTsapTabNumbers": bcamTsapTabNumbers,
       "bcamTsapTabState": bcamTsapTabState,
       "bcamTsapTabDuration": bcamTsapTabDuration,
       "bcamTsapTabDateApplEnable": bcamTsapTabDateApplEnable,
       "bcamTsapTabTimeApplEnable": bcamTsapTabTimeApplEnable,
       "bcamTsapTabTypName": bcamTsapTabTypName,
       "bcamTsapTabName": bcamTsapTabName,
       "bcamTsapTabPortnumber": bcamTsapTabPortnumber,
       "bcamTsapTabOsiTsel": bcamTsapTabOsiTsel,
       "bcamTsapTabNeaTsel": bcamTsapTabNeaTsel,
       "bcamTsapTabHost": bcamTsapTabHost,
       "bcamTsapTabDiagnostic": bcamTsapTabDiagnostic,
       "bcamTsapTabTsduSends": bcamTsapTabTsduSends,
       "bcamTsapTabByteSends": bcamTsapTabByteSends,
       "bcamTsapTabTsduReceiveds": bcamTsapTabTsduReceiveds,
       "bcamTsapTabByteReceiveds": bcamTsapTabByteReceiveds,
       "bcamTsapTabSendCallOverMaxs": bcamTsapTabSendCallOverMaxs,
       "bcamTsapTabLetterTimeouts": bcamTsapTabLetterTimeouts,
       "bcamTsapTabInWaitBuck1Hist": bcamTsapTabInWaitBuck1Hist,
       "bcamTsapTabInWaitBuck2Hist": bcamTsapTabInWaitBuck2Hist,
       "bcamTsapTabInWaitBuck3Hist": bcamTsapTabInWaitBuck3Hist,
       "bcamTsapTabInWaitBuck4Hist": bcamTsapTabInWaitBuck4Hist,
       "bcamTsapTabInWaitBuck5Hist": bcamTsapTabInWaitBuck5Hist,
       "bcamTsapTabReactBuck1Hist": bcamTsapTabReactBuck1Hist,
       "bcamTsapTabReactBuck2Hist": bcamTsapTabReactBuck2Hist,
       "bcamTsapTabReactBuck3Hist": bcamTsapTabReactBuck3Hist,
       "bcamTsapTabReactBuck4Hist": bcamTsapTabReactBuck4Hist,
       "bcamTsapTabReactBuck5Hist": bcamTsapTabReactBuck5Hist,
       "bcamTsapTabInWaitBuck1": bcamTsapTabInWaitBuck1,
       "bcamTsapTabInWaitBuck2": bcamTsapTabInWaitBuck2,
       "bcamTsapTabInWaitBuck3": bcamTsapTabInWaitBuck3,
       "bcamTsapTabInWaitBuck4": bcamTsapTabInWaitBuck4,
       "bcamTsapTabInWaitBuck5": bcamTsapTabInWaitBuck5,
       "bcamTsapTabReactBuck1": bcamTsapTabReactBuck1,
       "bcamTsapTabReactBuck2": bcamTsapTabReactBuck2,
       "bcamTsapTabReactBuck3": bcamTsapTabReactBuck3,
       "bcamTsapTabReactBuck4": bcamTsapTabReactBuck4,
       "bcamTsapTabReactBuck5": bcamTsapTabReactBuck5,
       "bcamTsapTabTsduSendHists": bcamTsapTabTsduSendHists,
       "bcamTsapTabByteSendHists": bcamTsapTabByteSendHists,
       "bcamTsapTabTsduReceivedHists": bcamTsapTabTsduReceivedHists,
       "bcamTsapTabByteReceivedHists": bcamTsapTabByteReceivedHists,
       "bcamTsapTabSendCallOverMaxHists": bcamTsapTabSendCallOverMaxHists,
       "bcamTsapTabLetterTimeoutHists": bcamTsapTabLetterTimeoutHists,
       "bcamTsapTabFunction": bcamTsapTabFunction,
       "bcamTsapTabCurrConn": bcamTsapTabCurrConn,
       "bcamTsapTabCloseConns": bcamTsapTabCloseConns,
       "bcamTsapTabClessSendBytes": bcamTsapTabClessSendBytes,
       "bcamTsapTabClessRecvBytes": bcamTsapTabClessRecvBytes,
       "bcamTsapTabClessSendCalls": bcamTsapTabClessSendCalls,
       "bcamTsapTabClessRecvCalls": bcamTsapTabClessRecvCalls,
       "bcamTsapTabOutbufTsdu": bcamTsapTabOutbufTsdu,
       "bcamTsapTabOutbufByte": bcamTsapTabOutbufByte,
       "bcamTsapTabInbufTsdu": bcamTsapTabInbufTsdu,
       "bcamTsapTabInbufByte": bcamTsapTabInbufByte,
       "bcamTsapTabOutbufTsduCless": bcamTsapTabOutbufTsduCless,
       "bcamTsapTabOutbufByteCless": bcamTsapTabOutbufByteCless,
       "bcamTsapTabInbufTsduCless": bcamTsapTabInbufTsduCless,
       "bcamTsapTabInbufByteCless": bcamTsapTabInbufByteCless,
       "bcamTsapTabClessTimeout": bcamTsapTabClessTimeout,
       "bcamCep": bcamCep,
       "bcamCepCurrent": bcamCepCurrent,
       "bcamCepClosed": bcamCepClosed,
       "bcamCepNotClosed": bcamCepNotClosed,
       "bcamCepRerouting": bcamCepRerouting,
       "bcamCepActiveTrials": bcamCepActiveTrials,
       "bcamCepActiveTrialFailures": bcamCepActiveTrialFailures,
       "bcamCepPassiveTrials": bcamCepPassiveTrials,
       "bcamCepPassiveTrialFailures": bcamCepPassiveTrialFailures,
       "bcamCepNumTable": bcamCepNumTable,
       "bcamCepTab": bcamCepTab,
       "bcamCepTabEntry": bcamCepTabEntry,
       "bcamCepTabProtocolClass": bcamCepTabProtocolClass,
       "bcamCepTabConnectionNumbers": bcamCepTabConnectionNumbers,
       "bcamCepTabDisconCommand": bcamCepTabDisconCommand,
       "bcamCepTabDisconInfoWord": bcamCepTabDisconInfoWord,
       "bcamCepTabTsduSends": bcamCepTabTsduSends,
       "bcamCepTabByteSends": bcamCepTabByteSends,
       "bcamCepTabTsduReceiveds": bcamCepTabTsduReceiveds,
       "bcamCepTabByteReceiveds": bcamCepTabByteReceiveds,
       "bcamCepTabSendCallOverMaxs": bcamCepTabSendCallOverMaxs,
       "bcamCepTabLetterTimeouts": bcamCepTabLetterTimeouts,
       "bcamCepTabOutbufTsduSend": bcamCepTabOutbufTsduSend,
       "bcamCepTabOutbufByteSend": bcamCepTabOutbufByteSend,
       "bcamCepTabOutbufMaxTsduSend": bcamCepTabOutbufMaxTsduSend,
       "bcamCepTabOutbufMaxByteSend": bcamCepTabOutbufMaxByteSend,
       "bcamCepTabInbufTsdu": bcamCepTabInbufTsdu,
       "bcamCepTabInbufByte": bcamCepTabInbufByte,
       "bcamCepTabInbufMaxTsduReceived": bcamCepTabInbufMaxTsduReceived,
       "bcamCepTabInbufMaxByteReceived": bcamCepTabInbufMaxByteReceived,
       "bcamCepTabPacketsDataSends": bcamCepTabPacketsDataSends,
       "bcamCepTabPacketsWindowSends": bcamCepTabPacketsWindowSends,
       "bcamCepTabPacketsDataReceiveds": bcamCepTabPacketsDataReceiveds,
       "bcamCepTabPacketsWindowReceiveds": bcamCepTabPacketsWindowReceiveds,
       "bcamCepTabGlobalZeroWindowSends": bcamCepTabGlobalZeroWindowSends,
       "bcamCepTabConnectionZeroWindowSends": bcamCepTabConnectionZeroWindowSends,
       "bcamCepTabZeroWindowReceiveds": bcamCepTabZeroWindowReceiveds,
       "bcamCepTabRoundTripTime": bcamCepTabRoundTripTime,
       "bcamCepTabRetransmitPacketsSends": bcamCepTabRetransmitPacketsSends,
       "bcamCepTabDetectedGapsReceiveds": bcamCepTabDetectedGapsReceiveds,
       "bcamCepTabDuplicatePacketsReceiveds": bcamCepTabDuplicatePacketsReceiveds,
       "bcamCepTabErrorPacketsReceiveds": bcamCepTabErrorPacketsReceiveds,
       "bcamCepTabConnectionState": bcamCepTabConnectionState,
       "bcamCepTabApplicationNumber": bcamCepTabApplicationNumber,
       "bcamCepTabRouteNumber": bcamCepTabRouteNumber,
       "bcamCepTabDuration": bcamCepTabDuration,
       "bcamCepTabDateConnectionEstablishment": bcamCepTabDateConnectionEstablishment,
       "bcamCepTabTimeConnectionEstablishment": bcamCepTabTimeConnectionEstablishment,
       "bcamCepTabTypPartnerName": bcamCepTabTypPartnerName,
       "bcamCepTabPartnerName": bcamCepTabPartnerName,
       "bcamCepTabLocalName": bcamCepTabLocalName,
       "bcamCepTabTypeL4Addr": bcamCepTabTypeL4Addr,
       "bcamCepTabL4AddrPartner": bcamCepTabL4AddrPartner,
       "bcamCepTabL4AddrLocal": bcamCepTabL4AddrLocal,
       "bcamCepTabPartnerEndsystem": bcamCepTabPartnerEndsystem,
       "bcamCepTabInWaitBuck1": bcamCepTabInWaitBuck1,
       "bcamCepTabInWaitBuck2": bcamCepTabInWaitBuck2,
       "bcamCepTabInWaitBuck3": bcamCepTabInWaitBuck3,
       "bcamCepTabInWaitBuck4": bcamCepTabInWaitBuck4,
       "bcamCepTabInWaitBuck5": bcamCepTabInWaitBuck5,
       "bcamCepTabReactBuck1": bcamCepTabReactBuck1,
       "bcamCepTabReactBuck2": bcamCepTabReactBuck2,
       "bcamCepTabReactBuck3": bcamCepTabReactBuck3,
       "bcamCepTabReactBuck4": bcamCepTabReactBuck4,
       "bcamCepTabReactBuck5": bcamCepTabReactBuck5,
       "bcamCepTabOutProcBuck1": bcamCepTabOutProcBuck1,
       "bcamCepTabOutProcBuck2": bcamCepTabOutProcBuck2,
       "bcamCepTabOutProcBuck3": bcamCepTabOutProcBuck3,
       "bcamCepTabOutProcBuck4": bcamCepTabOutProcBuck4,
       "bcamCepTabOutProcBuck5": bcamCepTabOutProcBuck5,
       "bcamCepTabInProcBuck1": bcamCepTabInProcBuck1,
       "bcamCepTabInProcBuck2": bcamCepTabInProcBuck2,
       "bcamCepTabInProcBuck3": bcamCepTabInProcBuck3,
       "bcamCepTabInProcBuck4": bcamCepTabInProcBuck4,
       "bcamCepTabInProcBuck5": bcamCepTabInProcBuck5,
       "bcamCepTabMaxSendLen": bcamCepTabMaxSendLen,
       "bcamCepTabMaxIndLen": bcamCepTabMaxIndLen,
       "bcamCepTabLocalEndsystem": bcamCepTabLocalEndsystem,
       "bcamRoute": bcamRoute,
       "bcamRouteNumTable": bcamRouteNumTable,
       "bcamRouteActive": bcamRouteActive,
       "bcamRouteArpDefault": bcamRouteArpDefault,
       "bcamRouteRoutingReqIp": bcamRouteRoutingReqIp,
       "bcamRouteRoutingReqIso": bcamRouteRoutingReqIso,
       "bcamRouteRoutingReqNea": bcamRouteRoutingReqNea,
       "bcamRouteSuccRoutingReqIp": bcamRouteSuccRoutingReqIp,
       "bcamRouteSuccRoutingReqIso": bcamRouteSuccRoutingReqIso,
       "bcamRouteSuccRoutingReqNea": bcamRouteSuccRoutingReqNea,
       "bcamRouteTab": bcamRouteTab,
       "bcamRouteTabEntry": bcamRouteTabEntry,
       "bcamRouteTabNumbers": bcamRouteTabNumbers,
       "bcamRouteTabName": bcamRouteTabName,
       "bcamRouteTabNumNeaConn": bcamRouteTabNumNeaConn,
       "bcamRouteTabNumIsoConn": bcamRouteTabNumIsoConn,
       "bcamRouteTabMaxNeaConn": bcamRouteTabMaxNeaConn,
       "bcamRouteTabMaxIsoConn": bcamRouteTabMaxIsoConn,
       "bcamRouteTabBadNeaElems": bcamRouteTabBadNeaElems,
       "bcamRouteTabBadIsoElems": bcamRouteTabBadIsoElems,
       "bcamRouteTabMaxL4Conn": bcamRouteTabMaxL4Conn,
       "bcamRouteTabMaxUnackTpdu": bcamRouteTabMaxUnackTpdu,
       "bcamRouteTabRouteNetTyp": bcamRouteTabRouteNetTyp,
       "bcamRouteTabNumberIsoIpRouter": bcamRouteTabNumberIsoIpRouter,
       "bcamRouteTabNumberNeaRouter": bcamRouteTabNumberNeaRouter,
       "bcamRouteTabNumberGateway": bcamRouteTabNumberGateway,
       "bcamRouteTabFunction": bcamRouteTabFunction,
       "bcamRouteTabProcNetTyp": bcamRouteTabProcNetTyp,
       "bcamRouteTabMaxTsduLen": bcamRouteTabMaxTsduLen,
       "bcamRouteTabNameEndsystem": bcamRouteTabNameEndsystem,
       "bcamRouteTabIso4WindowTimer": bcamRouteTabIso4WindowTimer,
       "bcamRouteTabIso4RetransTimer": bcamRouteTabIso4RetransTimer,
       "bcamRouteTabAckTimer": bcamRouteTabAckTimer,
       "bcamRouteTabErrorRecovTimer": bcamRouteTabErrorRecovTimer,
       "bcamRouteTabRejectTimer": bcamRouteTabRejectTimer,
       "bcamRouteTabExpedRetransTimer": bcamRouteTabExpedRetransTimer,
       "bcamRouteTabNameGateway": bcamRouteTabNameGateway,
       "bcamRouteTabNameX25Station": bcamRouteTabNameX25Station,
       "bcamRouteTabL3InputProfil": bcamRouteTabL3InputProfil,
       "bcamRouteTabTransState": bcamRouteTabTransState,
       "bcamRouteTabOption": bcamRouteTabOption,
       "bcamRouteTabTyp": bcamRouteTabTyp,
       "bcamRouteTabUsage": bcamRouteTabUsage,
       "bcamRouteTabL3Subprofile": bcamRouteTabL3Subprofile,
       "bcamRouteTabCommandState": bcamRouteTabCommandState,
       "bcamRouteTabChangeState": bcamRouteTabChangeState,
       "bcamRouteTabIso9542": bcamRouteTabIso9542,
       "bcamRouteTabMaxNetLength": bcamRouteTabMaxNetLength,
       "bcamRouteTabState2": bcamRouteTabState2,
       "bcamRouteTabDeactReason": bcamRouteTabDeactReason,
       "bcamRouteTabSwitchType": bcamRouteTabSwitchType,
       "bcamRouteTabReasonCreation": bcamRouteTabReasonCreation,
       "bcamRouteTabOrigLanAddress": bcamRouteTabOrigLanAddress,
       "bcamRouteTabLanAddress": bcamRouteTabLanAddress,
       "bcamRouteTabTypAddress": bcamRouteTabTypAddress,
       "bcamRouteTabLocalAddr": bcamRouteTabLocalAddr,
       "bcamRouteTabRemoteAddr": bcamRouteTabRemoteAddr,
       "bcamRouteTabOutPacketsDatas": bcamRouteTabOutPacketsDatas,
       "bcamRouteTabOutPacketsFlowControls": bcamRouteTabOutPacketsFlowControls,
       "bcamRouteTabInPacketsDatas": bcamRouteTabInPacketsDatas,
       "bcamRouteTabInPacketsFlowControls": bcamRouteTabInPacketsFlowControls,
       "bcamRouteTabOutRetransPackets": bcamRouteTabOutRetransPackets,
       "bcamRouteTabInDetectedGaps": bcamRouteTabInDetectedGaps,
       "bcamRouteTabInDuplicatedPackets": bcamRouteTabInDuplicatedPackets,
       "bcamRouteTabInIncorrectPackets": bcamRouteTabInIncorrectPackets,
       "bcamRouteTabRoundTripTimeClosed": bcamRouteTabRoundTripTimeClosed,
       "bcamRouteTabRoundTripTimeCurrent": bcamRouteTabRoundTripTimeCurrent,
       "bcamRouteTabArpReqSend": bcamRouteTabArpReqSend,
       "bcamRouteTabArpRepSend": bcamRouteTabArpRepSend,
       "bcamRouteTabArpReqRec": bcamRouteTabArpReqRec,
       "bcamRouteTabArpRepRec": bcamRouteTabArpRepRec,
       "bcamRouteTabIcmpReq": bcamRouteTabIcmpReq,
       "bcamRouteTabIcmpReply": bcamRouteTabIcmpReply,
       "bcamRouteTabIcmpRedirect": bcamRouteTabIcmpRedirect,
       "bcamRouteTabSwitched": bcamRouteTabSwitched,
       "bcamRouteTabDown": bcamRouteTabDown,
       "bcamRouteTabOspfHello": bcamRouteTabOspfHello,
       "bcamRouteTabPacketNoConn": bcamRouteTabPacketNoConn,
       "bcamRouteTabPacketInternDiscon": bcamRouteTabPacketInternDiscon,
       "bcamRouteTabPacketBadProtocol": bcamRouteTabPacketBadProtocol,
       "bcamRouteTabConnReqOut": bcamRouteTabConnReqOut,
       "bcamRouteTabConnReqOutAck": bcamRouteTabConnReqOutAck,
       "bcamRouteTabConnReqOutRej": bcamRouteTabConnReqOutRej,
       "bcamRouteTabConnReqIn": bcamRouteTabConnReqIn,
       "bcamRouteTabConnReqInAck": bcamRouteTabConnReqInAck,
       "bcamRouteTabConnReqInRej": bcamRouteTabConnReqInRej,
       "bcamRouteTabDisconnOut": bcamRouteTabDisconnOut,
       "bcamRouteTabDisconnOutAck": bcamRouteTabDisconnOutAck,
       "bcamRouteTabDisconnIn": bcamRouteTabDisconnIn,
       "bcamRouteTabDisconnInAck": bcamRouteTabDisconnInAck,
       "bcamRouteTabNumberLink": bcamRouteTabNumberLink,
       "bcamRouteTabArpFlag": bcamRouteTabArpFlag,
       "bcamRouteTabNsduLen": bcamRouteTabNsduLen,
       "bcamRouteTabMinNsduLen": bcamRouteTabMinNsduLen,
       "bcamRouteTabMaxNsduLen": bcamRouteTabMaxNsduLen,
       "bcamIf": bcamIf,
       "bcamIfNumTable": bcamIfNumTable,
       "bcamIfTab": bcamIfTab,
       "bcamIfTabEntry": bcamIfTabEntry,
       "bcamIfTabNumbers": bcamIfTabNumbers,
       "bcamIfTabName": bcamIfTabName,
       "bcamIfTabProfile": bcamIfTabProfile,
       "bcamIfTabMnemonicWrite": bcamIfTabMnemonicWrite,
       "bcamIfTabMnemonicRead": bcamIfTabMnemonicRead,
       "bcamIfTabLanAddress": bcamIfTabLanAddress,
       "bcamIfTabConfigUpdate": bcamIfTabConfigUpdate,
       "bcamIfTabMaxLpdu": bcamIfTabMaxLpdu,
       "bcamIfTabL2Monitoring": bcamIfTabL2Monitoring,
       "bcamIfTabDevice": bcamIfTabDevice,
       "bcamIfTabAdminState": bcamIfTabAdminState,
       "bcamIfTabCurrentState": bcamIfTabCurrentState,
       "bcamIfTabMode": bcamIfTabMode,
       "bcamIfTabPortName": bcamIfTabPortName,
       "bcamIfTabLenTraceOut": bcamIfTabLenTraceOut,
       "bcamIfTabLenTraceIn": bcamIfTabLenTraceIn,
       "bcamIfTabNumRouteSwitchings": bcamIfTabNumRouteSwitchings,
       "bcamIfTabTimeLastChange": bcamIfTabTimeLastChange,
       "bcamIfTabMnemonicDiag": bcamIfTabMnemonicDiag,
       "bcamIfTabNumMulticastAddr": bcamIfTabNumMulticastAddr,
       "bcamIfTabMulticastAddr1": bcamIfTabMulticastAddr1,
       "bcamIfTabMulticastAddr2": bcamIfTabMulticastAddr2,
       "bcamIfTabMulticastAddr3": bcamIfTabMulticastAddr3,
       "bcamIfTabMulticastAddr4": bcamIfTabMulticastAddr4,
       "bcamIfTabMulticastAddr5": bcamIfTabMulticastAddr5,
       "bcamIfTabMulticastAddr6": bcamIfTabMulticastAddr6,
       "bcamIfTabMulticastAddr7": bcamIfTabMulticastAddr7,
       "bcamIfTabMulticastAddr8": bcamIfTabMulticastAddr8,
       "bcamIfTabMulticastAddr9": bcamIfTabMulticastAddr9,
       "bcamIfTabMulticastAddr10": bcamIfTabMulticastAddr10,
       "bcamIfTabNumNeaAddress": bcamIfTabNumNeaAddress,
       "bcamIfTabNeaAddress1": bcamIfTabNeaAddress1,
       "bcamIfTabNeaAddress2": bcamIfTabNeaAddress2,
       "bcamIfTabNeaAddress3": bcamIfTabNeaAddress3,
       "bcamIfTabNeaAddress4": bcamIfTabNeaAddress4,
       "bcamIfTabNeaAddress5": bcamIfTabNeaAddress5,
       "bcamIfTabNeaAddress6": bcamIfTabNeaAddress6,
       "bcamIfTabNumIpAddress": bcamIfTabNumIpAddress,
       "bcamIfTabIpAddress1": bcamIfTabIpAddress1,
       "bcamIfTabIpAddress2": bcamIfTabIpAddress2,
       "bcamIfTabIpAddress3": bcamIfTabIpAddress3,
       "bcamIfTabIpAddress4": bcamIfTabIpAddress4,
       "bcamIfTabIpAddress5": bcamIfTabIpAddress5,
       "bcamIfTabIpAddress6": bcamIfTabIpAddress6,
       "bcamIfTabNumInt0Address": bcamIfTabNumInt0Address,
       "bcamIfTabInt0Address1": bcamIfTabInt0Address1,
       "bcamIfTabInt0Address2": bcamIfTabInt0Address2,
       "bcamIfTabInt0Address3": bcamIfTabInt0Address3,
       "bcamIfTabInt0Address4": bcamIfTabInt0Address4,
       "bcamIfTabInt0Address5": bcamIfTabInt0Address5,
       "bcamIfTabInt0Address6": bcamIfTabInt0Address6,
       "bcamIfTabNumIntfAddress": bcamIfTabNumIntfAddress,
       "bcamIfTabIntfAddress1": bcamIfTabIntfAddress1,
       "bcamIfTabIntfAddress2": bcamIfTabIntfAddress2,
       "bcamIfTabIntfAddress3": bcamIfTabIntfAddress3,
       "bcamIfTabIntfAddress4": bcamIfTabIntfAddress4,
       "bcamIfTabIntfAddress5": bcamIfTabIntfAddress5,
       "bcamIfTabIntfAddress6": bcamIfTabIntfAddress6,
       "bcamIfTabBytesOutHighs": bcamIfTabBytesOutHighs,
       "bcamIfTabBytesOutLows": bcamIfTabBytesOutLows,
       "bcamIfTabBytesInHighs": bcamIfTabBytesInHighs,
       "bcamIfTabBytesInLows": bcamIfTabBytesInLows,
       "bcamIfTabIOsOutHighs": bcamIfTabIOsOutHighs,
       "bcamIfTabIOsOutLows": bcamIfTabIOsOutLows,
       "bcamIfTabIOsInHighs": bcamIfTabIOsInHighs,
       "bcamIfTabIOsInLows": bcamIfTabIOsInLows,
       "bcamIfTabOutputStops": bcamIfTabOutputStops,
       "bcamIfTabInputStops": bcamIfTabInputStops,
       "bcamIfTabIOErrorOuts": bcamIfTabIOErrorOuts,
       "bcamIfTabIOErrorIns": bcamIfTabIOErrorIns,
       "bcamIfTabPacketsNotReceiveds": bcamIfTabPacketsNotReceiveds,
       "bcamIfTabInPacketsLanHighs": bcamIfTabInPacketsLanHighs,
       "bcamIfTabInPacketsLanLows": bcamIfTabInPacketsLanLows,
       "bcamIfTabOutPacketsLanHighs": bcamIfTabOutPacketsLanHighs,
       "bcamIfTabOutPacketsLanLows": bcamIfTabOutPacketsLanLows,
       "bcamIfTabUnicastInHighs": bcamIfTabUnicastInHighs,
       "bcamIfTabUnicastInLows": bcamIfTabUnicastInLows,
       "bcamIfTabUnicastOutHighs": bcamIfTabUnicastOutHighs,
       "bcamIfTabUnicastOutLows": bcamIfTabUnicastOutLows,
       "bcamIfTabMulticastInHighs": bcamIfTabMulticastInHighs,
       "bcamIfTabMulticastInLows": bcamIfTabMulticastInLows,
       "bcamIfTabMulticastOutHighs": bcamIfTabMulticastOutHighs,
       "bcamIfTabMulticastOutLows": bcamIfTabMulticastOutLows,
       "bcamIfTabErrorPacketIns": bcamIfTabErrorPacketIns,
       "bcamIfTabErrorPacketOuts": bcamIfTabErrorPacketOuts,
       "bcamIfTabDiscardIns": bcamIfTabDiscardIns,
       "bcamIfTabDiscardOuts": bcamIfTabDiscardOuts,
       "bcamIfTabUnknownProtoIns": bcamIfTabUnknownProtoIns,
       "bcamIfTabTraceState": bcamIfTabTraceState,
       "bcamIfTabTraceNumberBuffer": bcamIfTabTraceNumberBuffer,
       "bcamIfTabTraceBufferLen": bcamIfTabTraceBufferLen,
       "bcamRouter": bcamRouter,
       "bcamRouterNumTable": bcamRouterNumTable,
       "bcamRouterTab": bcamRouterTab,
       "bcamRouterTabEntry": bcamRouterTabEntry,
       "bcamRouterTabIpLow": bcamRouterTabIpLow,
       "bcamRouterTabIpHigh": bcamRouterTabIpHigh,
       "bcamRouterTabIpLocal": bcamRouterTabIpLocal,
       "bcamRouterTabIpRouter": bcamRouterTabIpRouter,
       "bcamRouterTabNumRouter": bcamRouterTabNumRouter,
       "bcamHost": bcamHost,
       "bcamHostNumTable": bcamHostNumTable,
       "bcamHostTab": bcamHostTab,
       "bcamHostTabEntry": bcamHostTabEntry,
       "bcamHostTabNumber": bcamHostTabNumber,
       "bcamHostTabName": bcamHostTabName,
       "bcamHostTabSocketName": bcamHostTabSocketName,
       "bcamHostTabTyp": bcamHostTabTyp,
       "bcamHostTabState": bcamHostTabState}
)
