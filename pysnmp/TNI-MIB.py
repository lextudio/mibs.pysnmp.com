# SNMP MIB module (TNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:29 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class CpsConnector(Integer32):
    """Custom type CpsConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 20),
          ("bncdual", 30),
          ("db9rsxxx", 31),
          ("din6", 38),
          ("lc", 19),
          ("mtrjmm", 18),
          ("mtrjsm", 25),
          ("rj-45", 10),
          ("rj11", 33),
          ("sc125km", 35),
          ("sc40km", 34),
          ("scmm", 13),
          ("scmm1300", 23),
          ("scsimplex", 29),
          ("scsm", 14),
          ("scsmelh", 16),
          ("scsmlh", 15),
          ("scsmlhlw", 17),
          ("scsmsh", 28),
          ("serial26", 26),
          ("stmm", 11),
          ("stmm1300", 24),
          ("stmmlh", 27),
          ("stsm", 12),
          ("stsmelh", 22),
          ("stsmlh", 21),
          ("termblock", 32))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Transition_ObjectIdentity = ObjectIdentity
transition = _Transition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868)
)
_ProductId_ObjectIdentity = ObjectIdentity
productId = _ProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1)
)
_RptrProdsId_ObjectIdentity = ObjectIdentity
rptrProdsId = _RptrProdsId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1)
)
_RptrStackMId_ObjectIdentity = ObjectIdentity
rptrStackMId = _RptrStackMId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1)
)
_RptrSMVer1Id_ObjectIdentity = ObjectIdentity
rptrSMVer1Id = _RptrSMVer1Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 1)
)
_RptrSMVer2Id_ObjectIdentity = ObjectIdentity
rptrSMVer2Id = _RptrSMVer2Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 2)
)
_RptrSM08TId_ObjectIdentity = ObjectIdentity
rptrSM08TId = _RptrSM08TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 3)
)
_RptrSM08TSId_ObjectIdentity = ObjectIdentity
rptrSM08TSId = _RptrSM08TSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 4)
)
_RptrSM06FId_ObjectIdentity = ObjectIdentity
rptrSM06FId = _RptrSM06FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 5)
)
_RptrSM06FSId_ObjectIdentity = ObjectIdentity
rptrSM06FSId = _RptrSM06FSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 6)
)
_RptrSM8T0Id_ObjectIdentity = ObjectIdentity
rptrSM8T0Id = _RptrSM8T0Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 7)
)
_RptrSM8TS0Id_ObjectIdentity = ObjectIdentity
rptrSM8TS0Id = _RptrSM8TS0Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 8)
)
_RptrSM6F0Id_ObjectIdentity = ObjectIdentity
rptrSM6F0Id = _RptrSM6F0Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 9)
)
_RptrSM6FS0Id_ObjectIdentity = ObjectIdentity
rptrSM6FS0Id = _RptrSM6FS0Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 10)
)
_RptrSM8T6FId_ObjectIdentity = ObjectIdentity
rptrSM8T6FId = _RptrSM8T6FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 11)
)
_RptrSM8TS6FId_ObjectIdentity = ObjectIdentity
rptrSM8TS6FId = _RptrSM8TS6FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 12)
)
_RptrSM8T6FSId_ObjectIdentity = ObjectIdentity
rptrSM8T6FSId = _RptrSM8T6FSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 13)
)
_RptrSM8TS6FSId_ObjectIdentity = ObjectIdentity
rptrSM8TS6FSId = _RptrSM8TS6FSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 14)
)
_RptrSM6F8TId_ObjectIdentity = ObjectIdentity
rptrSM6F8TId = _RptrSM6F8TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 15)
)
_RptrSM6FS8TId_ObjectIdentity = ObjectIdentity
rptrSM6FS8TId = _RptrSM6FS8TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 16)
)
_RptrSM6F8TSId_ObjectIdentity = ObjectIdentity
rptrSM6F8TSId = _RptrSM6F8TSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 17)
)
_RptrSM6FS8TSId_ObjectIdentity = ObjectIdentity
rptrSM6FS8TSId = _RptrSM6FS8TSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 18)
)
_RptrSM8T8TId_ObjectIdentity = ObjectIdentity
rptrSM8T8TId = _RptrSM8T8TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 19)
)
_RptrSM8TS8TId_ObjectIdentity = ObjectIdentity
rptrSM8TS8TId = _RptrSM8TS8TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 20)
)
_RptrSM8T8TSId_ObjectIdentity = ObjectIdentity
rptrSM8T8TSId = _RptrSM8T8TSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 21)
)
_RptrSM8TS8TSId_ObjectIdentity = ObjectIdentity
rptrSM8TS8TSId = _RptrSM8TS8TSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 22)
)
_RptrSM6F6FId_ObjectIdentity = ObjectIdentity
rptrSM6F6FId = _RptrSM6F6FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 23)
)
_RptrSM6FS6FId_ObjectIdentity = ObjectIdentity
rptrSM6FS6FId = _RptrSM6FS6FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 24)
)
_RptrSM6F6FSId_ObjectIdentity = ObjectIdentity
rptrSM6F6FSId = _RptrSM6F6FSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 25)
)
_RptrSM6FS6FSId_ObjectIdentity = ObjectIdentity
rptrSM6FS6FSId = _RptrSM6FS6FSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 26)
)
_RptrSM24TId_ObjectIdentity = ObjectIdentity
rptrSM24TId = _RptrSM24TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 27)
)
_RptrSM16TId_ObjectIdentity = ObjectIdentity
rptrSM16TId = _RptrSM16TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 28)
)
_RptrSM14FId_ObjectIdentity = ObjectIdentity
rptrSM14FId = _RptrSM14FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 29)
)
_RptrSM12FId_ObjectIdentity = ObjectIdentity
rptrSM12FId = _RptrSM12FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 30)
)
_RptrSM6FId_ObjectIdentity = ObjectIdentity
rptrSM6FId = _RptrSM6FId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 31)
)
_RptrSM0Id_ObjectIdentity = ObjectIdentity
rptrSM0Id = _RptrSM0Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 1, 32)
)
_RptrSPSId_ObjectIdentity = ObjectIdentity
rptrSPSId = _RptrSPSId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 2)
)
_RptrSPSVer1Id_ObjectIdentity = ObjectIdentity
rptrSPSVer1Id = _RptrSPSVer1Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 2, 1)
)
_RptrESPS24Id_ObjectIdentity = ObjectIdentity
rptrESPS24Id = _RptrESPS24Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 2, 2)
)
_RptrESPS24SId_ObjectIdentity = ObjectIdentity
rptrESPS24SId = _RptrESPS24SId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 1, 2, 3)
)
_RingProdsId_ObjectIdentity = ObjectIdentity
ringProdsId = _RingProdsId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 2)
)
_RingStackTRId_ObjectIdentity = ObjectIdentity
ringStackTRId = _RingStackTRId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 2, 1)
)
_RingTRVer1Id_ObjectIdentity = ObjectIdentity
ringTRVer1Id = _RingTRVer1Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 2, 1, 1)
)
_RingTRVer2Id_ObjectIdentity = ObjectIdentity
ringTRVer2Id = _RingTRVer2Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 2, 1, 2)
)
_RingTR0Id_ObjectIdentity = ObjectIdentity
ringTR0Id = _RingTR0Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 2, 1, 3)
)
_RingTR16TId_ObjectIdentity = ObjectIdentity
ringTR16TId = _RingTR16TId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 2, 1, 4)
)
_BrdgProdsId_ObjectIdentity = ObjectIdentity
brdgProdsId = _BrdgProdsId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 3)
)
_BrdgSwitchMId_ObjectIdentity = ObjectIdentity
brdgSwitchMId = _BrdgSwitchMId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 1)
)
_BrdgSWVer1Id_ObjectIdentity = ObjectIdentity
brdgSWVer1Id = _BrdgSWVer1Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 1, 1)
)
_BrdgFBRMId_ObjectIdentity = ObjectIdentity
brdgFBRMId = _BrdgFBRMId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2)
)
_Repeater_ObjectIdentity = ObjectIdentity
repeater = _Repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1)
)
_TnStackM_ObjectIdentity = ObjectIdentity
tnStackM = _TnStackM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1)
)
_TnSMCommon_ObjectIdentity = ObjectIdentity
tnSMCommon = _TnSMCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1)
)


class _TnSMComHwReset_Type(Integer32):
    """Custom type tnSMComHwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_TnSMComHwReset_Type.__name__ = "Integer32"
_TnSMComHwReset_Object = MibScalar
tnSMComHwReset = _TnSMComHwReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1, 1),
    _TnSMComHwReset_Type()
)
tnSMComHwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSMComHwReset.setStatus("mandatory")


class _TnSMComMgmtHwRev_Type(DisplayString):
    """Custom type tnSMComMgmtHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSMComMgmtHwRev_Type.__name__ = "DisplayString"
_TnSMComMgmtHwRev_Object = MibScalar
tnSMComMgmtHwRev = _TnSMComMgmtHwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1, 2),
    _TnSMComMgmtHwRev_Type()
)
tnSMComMgmtHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSMComMgmtHwRev.setStatus("mandatory")


class _TnSMComDiagSwRev_Type(DisplayString):
    """Custom type tnSMComDiagSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSMComDiagSwRev_Type.__name__ = "DisplayString"
_TnSMComDiagSwRev_Object = MibScalar
tnSMComDiagSwRev = _TnSMComDiagSwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1, 3),
    _TnSMComDiagSwRev_Type()
)
tnSMComDiagSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSMComDiagSwRev.setStatus("mandatory")


class _TnSMComMgmtSwRev_Type(DisplayString):
    """Custom type tnSMComMgmtSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSMComMgmtSwRev_Type.__name__ = "DisplayString"
_TnSMComMgmtSwRev_Object = MibScalar
tnSMComMgmtSwRev = _TnSMComMgmtSwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1, 4),
    _TnSMComMgmtSwRev_Type()
)
tnSMComMgmtSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSMComMgmtSwRev.setStatus("mandatory")
_TnSMComIpAddr_Type = IpAddress
_TnSMComIpAddr_Object = MibScalar
tnSMComIpAddr = _TnSMComIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1, 5),
    _TnSMComIpAddr_Type()
)
tnSMComIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSMComIpAddr.setStatus("mandatory")
_TnSMComNetMask_Type = IpAddress
_TnSMComNetMask_Object = MibScalar
tnSMComNetMask = _TnSMComNetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 1, 6),
    _TnSMComNetMask_Type()
)
tnSMComNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSMComNetMask.setStatus("mandatory")
_TnSMVer1_ObjectIdentity = ObjectIdentity
tnSMVer1 = _TnSMVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 2)
)
_TnSMVer2_ObjectIdentity = ObjectIdentity
tnSMVer2 = _TnSMVer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 1, 3)
)
_Sps_ObjectIdentity = ObjectIdentity
sps = _Sps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2)
)
_SpsCommon_ObjectIdentity = ObjectIdentity
spsCommon = _SpsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1)
)


class _SpsReset_Type(Integer32):
    """Custom type spsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_SpsReset_Type.__name__ = "Integer32"
_SpsReset_Object = MibScalar
spsReset = _SpsReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 1),
    _SpsReset_Type()
)
spsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsReset.setStatus("mandatory")


class _SpsConfig_Type(DisplayString):
    """Custom type spsConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpsConfig_Type.__name__ = "DisplayString"
_SpsConfig_Object = MibScalar
spsConfig = _SpsConfig_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 2),
    _SpsConfig_Type()
)
spsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsConfig.setStatus("mandatory")


class _SpsBootpEnable_Type(Integer32):
    """Custom type spsBootpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SpsBootpEnable_Type.__name__ = "Integer32"
_SpsBootpEnable_Object = MibScalar
spsBootpEnable = _SpsBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 3),
    _SpsBootpEnable_Type()
)
spsBootpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsBootpEnable.setStatus("mandatory")
_SpsBootpServer_Type = IpAddress
_SpsBootpServer_Object = MibScalar
spsBootpServer = _SpsBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 4),
    _SpsBootpServer_Type()
)
spsBootpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsBootpServer.setStatus("mandatory")


class _SpsBootpFilename_Type(DisplayString):
    """Custom type spsBootpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SpsBootpFilename_Type.__name__ = "DisplayString"
_SpsBootpFilename_Object = MibScalar
spsBootpFilename = _SpsBootpFilename_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 5),
    _SpsBootpFilename_Type()
)
spsBootpFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsBootpFilename.setStatus("mandatory")
_SpsDefaultGateway_Type = IpAddress
_SpsDefaultGateway_Object = MibScalar
spsDefaultGateway = _SpsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 6),
    _SpsDefaultGateway_Type()
)
spsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsDefaultGateway.setStatus("mandatory")
_SpsMgmtSegment_Type = Integer32
_SpsMgmtSegment_Object = MibScalar
spsMgmtSegment = _SpsMgmtSegment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 7),
    _SpsMgmtSegment_Type()
)
spsMgmtSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsMgmtSegment.setStatus("mandatory")
_SpsIpAddrTable_Object = MibTable
spsIpAddrTable = _SpsIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    spsIpAddrTable.setStatus("mandatory")
_SpsIpAddrEntry_Object = MibTableRow
spsIpAddrEntry = _SpsIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 8, 1)
)
spsIpAddrEntry.setIndexNames(
    (0, "TNI-MIB", "spsIpIfIndex"),
)
if mibBuilder.loadTexts:
    spsIpAddrEntry.setStatus("mandatory")
_SpsIpIfIndex_Type = Integer32
_SpsIpIfIndex_Object = MibTableColumn
spsIpIfIndex = _SpsIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 8, 1, 1),
    _SpsIpIfIndex_Type()
)
spsIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsIpIfIndex.setStatus("mandatory")
_SpsIpAddr_Type = IpAddress
_SpsIpAddr_Object = MibTableColumn
spsIpAddr = _SpsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 8, 1, 2),
    _SpsIpAddr_Type()
)
spsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsIpAddr.setStatus("mandatory")
_SpsIpNetMask_Type = IpAddress
_SpsIpNetMask_Object = MibTableColumn
spsIpNetMask = _SpsIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 8, 1, 3),
    _SpsIpNetMask_Type()
)
spsIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsIpNetMask.setStatus("mandatory")
_SpsTrapTable_Object = MibTable
spsTrapTable = _SpsTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    spsTrapTable.setStatus("mandatory")
_SpsTrapEntry_Object = MibTableRow
spsTrapEntry = _SpsTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 9, 1)
)
spsTrapEntry.setIndexNames(
    (0, "TNI-MIB", "spsTrapIndex"),
)
if mibBuilder.loadTexts:
    spsTrapEntry.setStatus("mandatory")
_SpsTrapIndex_Type = Integer32
_SpsTrapIndex_Object = MibTableColumn
spsTrapIndex = _SpsTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 9, 1, 1),
    _SpsTrapIndex_Type()
)
spsTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsTrapIndex.setStatus("mandatory")
_SpsTrapDestination_Type = IpAddress
_SpsTrapDestination_Object = MibTableColumn
spsTrapDestination = _SpsTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 9, 1, 2),
    _SpsTrapDestination_Type()
)
spsTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsTrapDestination.setStatus("mandatory")


class _SpsTrapCommunity_Type(DisplayString):
    """Custom type spsTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SpsTrapCommunity_Type.__name__ = "DisplayString"
_SpsTrapCommunity_Object = MibTableColumn
spsTrapCommunity = _SpsTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 1, 9, 1, 3),
    _SpsTrapCommunity_Type()
)
spsTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsTrapCommunity.setStatus("mandatory")
_SpsVer1_ObjectIdentity = ObjectIdentity
spsVer1 = _SpsVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2)
)
_SpsMaxSegment_Type = Integer32
_SpsMaxSegment_Object = MibScalar
spsMaxSegment = _SpsMaxSegment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 1),
    _SpsMaxSegment_Type()
)
spsMaxSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsMaxSegment.setStatus("mandatory")


class _SpsPasswdReset_Type(Integer32):
    """Custom type spsPasswdReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_SpsPasswdReset_Type.__name__ = "Integer32"
_SpsPasswdReset_Object = MibScalar
spsPasswdReset = _SpsPasswdReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 2),
    _SpsPasswdReset_Type()
)
spsPasswdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsPasswdReset.setStatus("mandatory")


class _SpsExternalPowerSupply_Type(Integer32):
    """Custom type spsExternalPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_SpsExternalPowerSupply_Type.__name__ = "Integer32"
_SpsExternalPowerSupply_Object = MibScalar
spsExternalPowerSupply = _SpsExternalPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 3),
    _SpsExternalPowerSupply_Type()
)
spsExternalPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsExternalPowerSupply.setStatus("mandatory")


class _SpsDisplayString_Type(DisplayString):
    """Custom type spsDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SpsDisplayString_Type.__name__ = "DisplayString"
_SpsDisplayString_Object = MibScalar
spsDisplayString = _SpsDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 4),
    _SpsDisplayString_Type()
)
spsDisplayString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsDisplayString.setStatus("mandatory")
_SpsRptrGroupTable_Object = MibTable
spsRptrGroupTable = _SpsRptrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    spsRptrGroupTable.setStatus("mandatory")
_SpsRptrGroupEntry_Object = MibTableRow
spsRptrGroupEntry = _SpsRptrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 5, 1)
)
spsRptrGroupEntry.setIndexNames(
    (0, "TNI-MIB", "spsRptrGroupIndex"),
)
if mibBuilder.loadTexts:
    spsRptrGroupEntry.setStatus("mandatory")
_SpsRptrGroupIndex_Type = Integer32
_SpsRptrGroupIndex_Object = MibTableColumn
spsRptrGroupIndex = _SpsRptrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 5, 1, 1),
    _SpsRptrGroupIndex_Type()
)
spsRptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsRptrGroupIndex.setStatus("mandatory")


class _SpsRptrGroupUnitId_Type(OctetString):
    """Custom type spsRptrGroupUnitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SpsRptrGroupUnitId_Type.__name__ = "OctetString"
_SpsRptrGroupUnitId_Object = MibTableColumn
spsRptrGroupUnitId = _SpsRptrGroupUnitId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 5, 1, 2),
    _SpsRptrGroupUnitId_Type()
)
spsRptrGroupUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsRptrGroupUnitId.setStatus("mandatory")


class _SpsRptrGroupInternalPowerSupply_Type(Integer32):
    """Custom type spsRptrGroupInternalPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_SpsRptrGroupInternalPowerSupply_Type.__name__ = "Integer32"
_SpsRptrGroupInternalPowerSupply_Object = MibTableColumn
spsRptrGroupInternalPowerSupply = _SpsRptrGroupInternalPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 5, 1, 3),
    _SpsRptrGroupInternalPowerSupply_Type()
)
spsRptrGroupInternalPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsRptrGroupInternalPowerSupply.setStatus("mandatory")
_SpsRptrPortTable_Object = MibTable
spsRptrPortTable = _SpsRptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    spsRptrPortTable.setStatus("mandatory")
_SpsRptrPortEntry_Object = MibTableRow
spsRptrPortEntry = _SpsRptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1)
)
spsRptrPortEntry.setIndexNames(
    (0, "TNI-MIB", "spsRptrPortGroupIndex"),
    (0, "TNI-MIB", "spsRptrPortIndex"),
)
if mibBuilder.loadTexts:
    spsRptrPortEntry.setStatus("mandatory")
_SpsRptrPortGroupIndex_Type = Integer32
_SpsRptrPortGroupIndex_Object = MibTableColumn
spsRptrPortGroupIndex = _SpsRptrPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 1),
    _SpsRptrPortGroupIndex_Type()
)
spsRptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsRptrPortGroupIndex.setStatus("mandatory")
_SpsRptrPortIndex_Type = Integer32
_SpsRptrPortIndex_Object = MibTableColumn
spsRptrPortIndex = _SpsRptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 2),
    _SpsRptrPortIndex_Type()
)
spsRptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsRptrPortIndex.setStatus("mandatory")
_SpsRptrPortSegment_Type = Integer32
_SpsRptrPortSegment_Object = MibTableColumn
spsRptrPortSegment = _SpsRptrPortSegment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 3),
    _SpsRptrPortSegment_Type()
)
spsRptrPortSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsRptrPortSegment.setStatus("mandatory")
_SpsRptrPortSrcAddr_Type = MacAddress
_SpsRptrPortSrcAddr_Object = MibTableColumn
spsRptrPortSrcAddr = _SpsRptrPortSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 4),
    _SpsRptrPortSrcAddr_Type()
)
spsRptrPortSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsRptrPortSrcAddr.setStatus("mandatory")


class _SpsRptrPortEavesdropping_Type(Integer32):
    """Custom type spsRptrPortEavesdropping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SpsRptrPortEavesdropping_Type.__name__ = "Integer32"
_SpsRptrPortEavesdropping_Object = MibTableColumn
spsRptrPortEavesdropping = _SpsRptrPortEavesdropping_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 5),
    _SpsRptrPortEavesdropping_Type()
)
spsRptrPortEavesdropping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsRptrPortEavesdropping.setStatus("mandatory")


class _SpsRptrPortIntrusion_Type(Integer32):
    """Custom type spsRptrPortIntrusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SpsRptrPortIntrusion_Type.__name__ = "Integer32"
_SpsRptrPortIntrusion_Object = MibTableColumn
spsRptrPortIntrusion = _SpsRptrPortIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 6),
    _SpsRptrPortIntrusion_Type()
)
spsRptrPortIntrusion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsRptrPortIntrusion.setStatus("mandatory")


class _SpsRptrPortCollisionLimit_Type(Integer32):
    """Custom type spsRptrPortCollisionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(31,
              63,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("collision-limit-127", 127),
          ("collision-limit-155", 255),
          ("collision-limit-31", 31),
          ("collision-limit-63", 63))
    )


_SpsRptrPortCollisionLimit_Type.__name__ = "Integer32"
_SpsRptrPortCollisionLimit_Object = MibTableColumn
spsRptrPortCollisionLimit = _SpsRptrPortCollisionLimit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 7),
    _SpsRptrPortCollisionLimit_Type()
)
spsRptrPortCollisionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsRptrPortCollisionLimit.setStatus("mandatory")


class _SpsRptrPortEnableIntruderDetectTrap_Type(Integer32):
    """Custom type spsRptrPortEnableIntruderDetectTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SpsRptrPortEnableIntruderDetectTrap_Type.__name__ = "Integer32"
_SpsRptrPortEnableIntruderDetectTrap_Object = MibTableColumn
spsRptrPortEnableIntruderDetectTrap = _SpsRptrPortEnableIntruderDetectTrap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 8),
    _SpsRptrPortEnableIntruderDetectTrap_Type()
)
spsRptrPortEnableIntruderDetectTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spsRptrPortEnableIntruderDetectTrap.setStatus("mandatory")


class _SpsRptrPortDisableIntruder_Type(Integer32):
    """Custom type spsRptrPortDisableIntruder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SpsRptrPortDisableIntruder_Type.__name__ = "Integer32"
_SpsRptrPortDisableIntruder_Object = MibTableColumn
spsRptrPortDisableIntruder = _SpsRptrPortDisableIntruder_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 6, 1, 9),
    _SpsRptrPortDisableIntruder_Type()
)
spsRptrPortDisableIntruder.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    spsRptrPortDisableIntruder.setStatus("mandatory")
_SpsSerialPortTable_Object = MibTable
spsSerialPortTable = _SpsSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    spsSerialPortTable.setStatus("mandatory")
_SpsSerialPortEntry_Object = MibTableRow
spsSerialPortEntry = _SpsSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 7, 1)
)
spsSerialPortEntry.setIndexNames(
    (0, "TNI-MIB", "spsSerialPortIndex"),
)
if mibBuilder.loadTexts:
    spsSerialPortEntry.setStatus("mandatory")
_SpsSerialPortIndex_Type = Integer32
_SpsSerialPortIndex_Object = MibTableColumn
spsSerialPortIndex = _SpsSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 7, 1, 1),
    _SpsSerialPortIndex_Type()
)
spsSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsSerialPortIndex.setStatus("mandatory")


class _SpsSerialPortModemControl_Type(Integer32):
    """Custom type spsSerialPortModemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SpsSerialPortModemControl_Type.__name__ = "Integer32"
_SpsSerialPortModemControl_Object = MibTableColumn
spsSerialPortModemControl = _SpsSerialPortModemControl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 7, 1, 2),
    _SpsSerialPortModemControl_Type()
)
spsSerialPortModemControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsSerialPortModemControl.setStatus("mandatory")
_SpsMonitorSegmentTable_Object = MibTable
spsMonitorSegmentTable = _SpsMonitorSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    spsMonitorSegmentTable.setStatus("mandatory")
_SpsMonitorSegmentEntry_Object = MibTableRow
spsMonitorSegmentEntry = _SpsMonitorSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 8, 1)
)
spsMonitorSegmentEntry.setIndexNames(
    (0, "TNI-MIB", "spsMonitorSegmentIndex"),
)
if mibBuilder.loadTexts:
    spsMonitorSegmentEntry.setStatus("mandatory")


class _SpsMonitorSegmentIndex_Type(Integer32):
    """Custom type spsMonitorSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SpsMonitorSegmentIndex_Type.__name__ = "Integer32"
_SpsMonitorSegmentIndex_Object = MibTableColumn
spsMonitorSegmentIndex = _SpsMonitorSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 8, 1, 1),
    _SpsMonitorSegmentIndex_Type()
)
spsMonitorSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsMonitorSegmentIndex.setStatus("mandatory")
_SpsMonitorSegmentTotalFrames_Type = Counter32
_SpsMonitorSegmentTotalFrames_Object = MibTableColumn
spsMonitorSegmentTotalFrames = _SpsMonitorSegmentTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 8, 1, 2),
    _SpsMonitorSegmentTotalFrames_Type()
)
spsMonitorSegmentTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsMonitorSegmentTotalFrames.setStatus("mandatory")
_SpsMonitorSegmentTotalOctets_Type = Counter32
_SpsMonitorSegmentTotalOctets_Object = MibTableColumn
spsMonitorSegmentTotalOctets = _SpsMonitorSegmentTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 8, 1, 3),
    _SpsMonitorSegmentTotalOctets_Type()
)
spsMonitorSegmentTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsMonitorSegmentTotalOctets.setStatus("mandatory")
_SpsMonitorSegmentTotalErrors_Type = Counter32
_SpsMonitorSegmentTotalErrors_Object = MibTableColumn
spsMonitorSegmentTotalErrors = _SpsMonitorSegmentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 1, 2, 2, 8, 1, 4),
    _SpsMonitorSegmentTotalErrors_Type()
)
spsMonitorSegmentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spsMonitorSegmentTotalErrors.setStatus("mandatory")
_Ring_ObjectIdentity = ObjectIdentity
ring = _Ring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 2)
)
_TnStackTR_ObjectIdentity = ObjectIdentity
tnStackTR = _TnStackTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1)
)
_TnTRCommon_ObjectIdentity = ObjectIdentity
tnTRCommon = _TnTRCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1)
)


class _TnTRComHwReset_Type(Integer32):
    """Custom type tnTRComHwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_TnTRComHwReset_Type.__name__ = "Integer32"
_TnTRComHwReset_Object = MibScalar
tnTRComHwReset = _TnTRComHwReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 1),
    _TnTRComHwReset_Type()
)
tnTRComHwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRComHwReset.setStatus("mandatory")


class _TnTRComMgmtHwRev_Type(DisplayString):
    """Custom type tnTRComMgmtHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnTRComMgmtHwRev_Type.__name__ = "DisplayString"
_TnTRComMgmtHwRev_Object = MibScalar
tnTRComMgmtHwRev = _TnTRComMgmtHwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 2),
    _TnTRComMgmtHwRev_Type()
)
tnTRComMgmtHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRComMgmtHwRev.setStatus("mandatory")


class _TnTRComDiagSwRev_Type(DisplayString):
    """Custom type tnTRComDiagSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnTRComDiagSwRev_Type.__name__ = "DisplayString"
_TnTRComDiagSwRev_Object = MibScalar
tnTRComDiagSwRev = _TnTRComDiagSwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 3),
    _TnTRComDiagSwRev_Type()
)
tnTRComDiagSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRComDiagSwRev.setStatus("mandatory")


class _TnTRComMgmtSwRev_Type(DisplayString):
    """Custom type tnTRComMgmtSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnTRComMgmtSwRev_Type.__name__ = "DisplayString"
_TnTRComMgmtSwRev_Object = MibScalar
tnTRComMgmtSwRev = _TnTRComMgmtSwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 4),
    _TnTRComMgmtSwRev_Type()
)
tnTRComMgmtSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRComMgmtSwRev.setStatus("mandatory")
_TnTRComIpAddr_Type = IpAddress
_TnTRComIpAddr_Object = MibScalar
tnTRComIpAddr = _TnTRComIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 5),
    _TnTRComIpAddr_Type()
)
tnTRComIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRComIpAddr.setStatus("mandatory")
_TnTRComNetMask_Type = IpAddress
_TnTRComNetMask_Object = MibScalar
tnTRComNetMask = _TnTRComNetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 6),
    _TnTRComNetMask_Type()
)
tnTRComNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRComNetMask.setStatus("mandatory")
_TnTRComIfaceCapacity_Type = Integer32
_TnTRComIfaceCapacity_Object = MibScalar
tnTRComIfaceCapacity = _TnTRComIfaceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 1, 7),
    _TnTRComIfaceCapacity_Type()
)
tnTRComIfaceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRComIfaceCapacity.setStatus("mandatory")
_TnTRVer1_ObjectIdentity = ObjectIdentity
tnTRVer1 = _TnTRVer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2)
)


class _TnTRV1Commands_Type(Integer32):
    """Custom type tnTRV1Commands based on Integer32"""
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
        *(("close", 4),
          ("no-op", 1),
          ("open", 2),
          ("reset", 3))
    )


_TnTRV1Commands_Type.__name__ = "Integer32"
_TnTRV1Commands_Object = MibScalar
tnTRV1Commands = _TnTRV1Commands_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 1),
    _TnTRV1Commands_Type()
)
tnTRV1Commands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRV1Commands.setStatus("mandatory")
_TnTRV1RingStatus_Type = Integer32
_TnTRV1RingStatus_Object = MibScalar
tnTRV1RingStatus = _TnTRV1RingStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 2),
    _TnTRV1RingStatus_Type()
)
tnTRV1RingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1RingStatus.setStatus("mandatory")


class _TnTRV1RingState_Type(Integer32):
    """Custom type tnTRV1RingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_TnTRV1RingState_Type.__name__ = "Integer32"
_TnTRV1RingState_Object = MibScalar
tnTRV1RingState = _TnTRV1RingState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 3),
    _TnTRV1RingState_Type()
)
tnTRV1RingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1RingState.setStatus("mandatory")


class _TnTRV1RingOpenStatus_Type(Integer32):
    """Custom type tnTRV1RingOpenStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("badParam", 2),
          ("beaconing", 7),
          ("duplicateMAC", 8),
          ("insertionTimeout", 5),
          ("lobeFailed", 3),
          ("noOpen", 1),
          ("open", 11),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("signalLoss", 4))
    )


_TnTRV1RingOpenStatus_Type.__name__ = "Integer32"
_TnTRV1RingOpenStatus_Object = MibScalar
tnTRV1RingOpenStatus = _TnTRV1RingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 4),
    _TnTRV1RingOpenStatus_Type()
)
tnTRV1RingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1RingOpenStatus.setStatus("mandatory")


class _TnTRV1RingSpeed_Type(Integer32):
    """Custom type tnTRV1RingSpeed based on Integer32"""
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
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("unknown", 1))
    )


_TnTRV1RingSpeed_Type.__name__ = "Integer32"
_TnTRV1RingSpeed_Object = MibScalar
tnTRV1RingSpeed = _TnTRV1RingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 5),
    _TnTRV1RingSpeed_Type()
)
tnTRV1RingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRV1RingSpeed.setStatus("mandatory")
_TnTRV1UpStream_Type = MacAddress
_TnTRV1UpStream_Object = MibScalar
tnTRV1UpStream = _TnTRV1UpStream_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 6),
    _TnTRV1UpStream_Type()
)
tnTRV1UpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1UpStream.setStatus("mandatory")


class _TnTRV1ActMonParticipate_Type(Integer32):
    """Custom type tnTRV1ActMonParticipate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_TnTRV1ActMonParticipate_Type.__name__ = "Integer32"
_TnTRV1ActMonParticipate_Object = MibScalar
tnTRV1ActMonParticipate = _TnTRV1ActMonParticipate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 7),
    _TnTRV1ActMonParticipate_Type()
)
tnTRV1ActMonParticipate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRV1ActMonParticipate.setStatus("mandatory")
_TnTRV1Functional_Type = MacAddress
_TnTRV1Functional_Object = MibScalar
tnTRV1Functional = _TnTRV1Functional_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 8),
    _TnTRV1Functional_Type()
)
tnTRV1Functional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTRV1Functional.setStatus("mandatory")
_TnTRV1StatsLineErrors_Type = Counter32
_TnTRV1StatsLineErrors_Object = MibScalar
tnTRV1StatsLineErrors = _TnTRV1StatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 9),
    _TnTRV1StatsLineErrors_Type()
)
tnTRV1StatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsLineErrors.setStatus("mandatory")
_TnTRV1StatsBurstErrors_Type = Counter32
_TnTRV1StatsBurstErrors_Object = MibScalar
tnTRV1StatsBurstErrors = _TnTRV1StatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 10),
    _TnTRV1StatsBurstErrors_Type()
)
tnTRV1StatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsBurstErrors.setStatus("mandatory")
_TnTRV1StatsACErrors_Type = Counter32
_TnTRV1StatsACErrors_Object = MibScalar
tnTRV1StatsACErrors = _TnTRV1StatsACErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 11),
    _TnTRV1StatsACErrors_Type()
)
tnTRV1StatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsACErrors.setStatus("mandatory")
_TnTRV1StatsAbortTransErrors_Type = Counter32
_TnTRV1StatsAbortTransErrors_Object = MibScalar
tnTRV1StatsAbortTransErrors = _TnTRV1StatsAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 12),
    _TnTRV1StatsAbortTransErrors_Type()
)
tnTRV1StatsAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsAbortTransErrors.setStatus("mandatory")
_TnTRV1StatsInternalErrors_Type = Counter32
_TnTRV1StatsInternalErrors_Object = MibScalar
tnTRV1StatsInternalErrors = _TnTRV1StatsInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 13),
    _TnTRV1StatsInternalErrors_Type()
)
tnTRV1StatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsInternalErrors.setStatus("mandatory")
_TnTRV1StatsLostFrameErrors_Type = Counter32
_TnTRV1StatsLostFrameErrors_Object = MibScalar
tnTRV1StatsLostFrameErrors = _TnTRV1StatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 14),
    _TnTRV1StatsLostFrameErrors_Type()
)
tnTRV1StatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsLostFrameErrors.setStatus("mandatory")
_TnTRV1StatsReceiveCongestions_Type = Counter32
_TnTRV1StatsReceiveCongestions_Object = MibScalar
tnTRV1StatsReceiveCongestions = _TnTRV1StatsReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 15),
    _TnTRV1StatsReceiveCongestions_Type()
)
tnTRV1StatsReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsReceiveCongestions.setStatus("mandatory")
_TnTRV1StatsFrameCopiedErrors_Type = Counter32
_TnTRV1StatsFrameCopiedErrors_Object = MibScalar
tnTRV1StatsFrameCopiedErrors = _TnTRV1StatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 16),
    _TnTRV1StatsFrameCopiedErrors_Type()
)
tnTRV1StatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsFrameCopiedErrors.setStatus("mandatory")
_TnTRV1StatsTokenErrors_Type = Counter32
_TnTRV1StatsTokenErrors_Object = MibScalar
tnTRV1StatsTokenErrors = _TnTRV1StatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 17),
    _TnTRV1StatsTokenErrors_Type()
)
tnTRV1StatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsTokenErrors.setStatus("mandatory")
_TnTRV1StatsSoftErrors_Type = Counter32
_TnTRV1StatsSoftErrors_Object = MibScalar
tnTRV1StatsSoftErrors = _TnTRV1StatsSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 18),
    _TnTRV1StatsSoftErrors_Type()
)
tnTRV1StatsSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsSoftErrors.setStatus("mandatory")
_TnTRV1StatsHardErrors_Type = Counter32
_TnTRV1StatsHardErrors_Object = MibScalar
tnTRV1StatsHardErrors = _TnTRV1StatsHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 19),
    _TnTRV1StatsHardErrors_Type()
)
tnTRV1StatsHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsHardErrors.setStatus("mandatory")
_TnTRV1StatsSignalLoss_Type = Counter32
_TnTRV1StatsSignalLoss_Object = MibScalar
tnTRV1StatsSignalLoss = _TnTRV1StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 20),
    _TnTRV1StatsSignalLoss_Type()
)
tnTRV1StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsSignalLoss.setStatus("mandatory")
_TnTRV1StatsTransmitBeacons_Type = Counter32
_TnTRV1StatsTransmitBeacons_Object = MibScalar
tnTRV1StatsTransmitBeacons = _TnTRV1StatsTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 21),
    _TnTRV1StatsTransmitBeacons_Type()
)
tnTRV1StatsTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsTransmitBeacons.setStatus("mandatory")
_TnTRV1StatsRecoverys_Type = Counter32
_TnTRV1StatsRecoverys_Object = MibScalar
tnTRV1StatsRecoverys = _TnTRV1StatsRecoverys_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 22),
    _TnTRV1StatsRecoverys_Type()
)
tnTRV1StatsRecoverys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsRecoverys.setStatus("mandatory")
_TnTRV1StatsLobeWires_Type = Counter32
_TnTRV1StatsLobeWires_Object = MibScalar
tnTRV1StatsLobeWires = _TnTRV1StatsLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 23),
    _TnTRV1StatsLobeWires_Type()
)
tnTRV1StatsLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsLobeWires.setStatus("mandatory")
_TnTRV1StatsRemoves_Type = Counter32
_TnTRV1StatsRemoves_Object = MibScalar
tnTRV1StatsRemoves = _TnTRV1StatsRemoves_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 24),
    _TnTRV1StatsRemoves_Type()
)
tnTRV1StatsRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsRemoves.setStatus("mandatory")
_TnTRV1StatsSingles_Type = Counter32
_TnTRV1StatsSingles_Object = MibScalar
tnTRV1StatsSingles = _TnTRV1StatsSingles_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 25),
    _TnTRV1StatsSingles_Type()
)
tnTRV1StatsSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsSingles.setStatus("mandatory")
_TnTRV1StatsFreqErrors_Type = Counter32
_TnTRV1StatsFreqErrors_Object = MibScalar
tnTRV1StatsFreqErrors = _TnTRV1StatsFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 26),
    _TnTRV1StatsFreqErrors_Type()
)
tnTRV1StatsFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1StatsFreqErrors.setStatus("optional")
_TnTRV1TimerReturnRepeat_Type = Integer32
_TnTRV1TimerReturnRepeat_Object = MibScalar
tnTRV1TimerReturnRepeat = _TnTRV1TimerReturnRepeat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 27),
    _TnTRV1TimerReturnRepeat_Type()
)
tnTRV1TimerReturnRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerReturnRepeat.setStatus("mandatory")
_TnTRV1TimerHolding_Type = Integer32
_TnTRV1TimerHolding_Object = MibScalar
tnTRV1TimerHolding = _TnTRV1TimerHolding_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 28),
    _TnTRV1TimerHolding_Type()
)
tnTRV1TimerHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerHolding.setStatus("mandatory")
_TnTRV1TimerQueuePDU_Type = Integer32
_TnTRV1TimerQueuePDU_Object = MibScalar
tnTRV1TimerQueuePDU = _TnTRV1TimerQueuePDU_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 29),
    _TnTRV1TimerQueuePDU_Type()
)
tnTRV1TimerQueuePDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerQueuePDU.setStatus("mandatory")
_TnTRV1TimerValidTransmit_Type = Integer32
_TnTRV1TimerValidTransmit_Object = MibScalar
tnTRV1TimerValidTransmit = _TnTRV1TimerValidTransmit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 30),
    _TnTRV1TimerValidTransmit_Type()
)
tnTRV1TimerValidTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerValidTransmit.setStatus("mandatory")
_TnTRV1TimerNoToken_Type = Integer32
_TnTRV1TimerNoToken_Object = MibScalar
tnTRV1TimerNoToken = _TnTRV1TimerNoToken_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 31),
    _TnTRV1TimerNoToken_Type()
)
tnTRV1TimerNoToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerNoToken.setStatus("mandatory")
_TnTRV1TimerActiveMon_Type = Integer32
_TnTRV1TimerActiveMon_Object = MibScalar
tnTRV1TimerActiveMon = _TnTRV1TimerActiveMon_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 32),
    _TnTRV1TimerActiveMon_Type()
)
tnTRV1TimerActiveMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerActiveMon.setStatus("mandatory")
_TnTRV1TimerStandbyMon_Type = Integer32
_TnTRV1TimerStandbyMon_Object = MibScalar
tnTRV1TimerStandbyMon = _TnTRV1TimerStandbyMon_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 33),
    _TnTRV1TimerStandbyMon_Type()
)
tnTRV1TimerStandbyMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerStandbyMon.setStatus("mandatory")
_TnTRV1TimerErrorReport_Type = Integer32
_TnTRV1TimerErrorReport_Object = MibScalar
tnTRV1TimerErrorReport = _TnTRV1TimerErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 34),
    _TnTRV1TimerErrorReport_Type()
)
tnTRV1TimerErrorReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerErrorReport.setStatus("mandatory")
_TnTRV1TimerBeaconTransmit_Type = Integer32
_TnTRV1TimerBeaconTransmit_Object = MibScalar
tnTRV1TimerBeaconTransmit = _TnTRV1TimerBeaconTransmit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 35),
    _TnTRV1TimerBeaconTransmit_Type()
)
tnTRV1TimerBeaconTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerBeaconTransmit.setStatus("mandatory")
_TnTRV1TimerBeaconReceive_Type = Integer32
_TnTRV1TimerBeaconReceive_Object = MibScalar
tnTRV1TimerBeaconReceive = _TnTRV1TimerBeaconReceive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 2, 36),
    _TnTRV1TimerBeaconReceive_Type()
)
tnTRV1TimerBeaconReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTRV1TimerBeaconReceive.setStatus("mandatory")
_TnTRVer2_ObjectIdentity = ObjectIdentity
tnTRVer2 = _TnTRVer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 2, 1, 3)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 3)
)
_Sfbrm10x100_ObjectIdentity = ObjectIdentity
sfbrm10x100 = _Sfbrm10x100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1)
)
_SfbrmSystem_ObjectIdentity = ObjectIdentity
sfbrmSystem = _SfbrmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1)
)
_Sfbrm100SystemTable_Object = MibTable
sfbrm100SystemTable = _Sfbrm100SystemTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sfbrm100SystemTable.setStatus("mandatory")
_Sfbrm100SystemEntry_Object = MibTableRow
sfbrm100SystemEntry = _Sfbrm100SystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1)
)
sfbrm100SystemEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100SysLocPortIndex"),
    (0, "TNI-MIB", "sfbrm100SysSecIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100SystemEntry.setStatus("mandatory")
_Sfbrm100SysLocPortIndex_Type = Integer32
_Sfbrm100SysLocPortIndex_Object = MibTableColumn
sfbrm100SysLocPortIndex = _Sfbrm100SysLocPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 1),
    _Sfbrm100SysLocPortIndex_Type()
)
sfbrm100SysLocPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysLocPortIndex.setStatus("mandatory")
_Sfbrm100SysSecIndex_Type = Integer32
_Sfbrm100SysSecIndex_Object = MibTableColumn
sfbrm100SysSecIndex = _Sfbrm100SysSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 2),
    _Sfbrm100SysSecIndex_Type()
)
sfbrm100SysSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysSecIndex.setStatus("mandatory")
_Sfbrm100SysGrpString_Type = DisplayString
_Sfbrm100SysGrpString_Object = MibTableColumn
sfbrm100SysGrpString = _Sfbrm100SysGrpString_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 3),
    _Sfbrm100SysGrpString_Type()
)
sfbrm100SysGrpString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysGrpString.setStatus("mandatory")
_Sfbrm100SysMRevision_Type = Integer32
_Sfbrm100SysMRevision_Object = MibTableColumn
sfbrm100SysMRevision = _Sfbrm100SysMRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 4),
    _Sfbrm100SysMRevision_Type()
)
sfbrm100SysMRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysMRevision.setStatus("mandatory")


class _Sfbrm100SysCfgMatch_Type(Integer32):
    """Custom type sfbrm100SysCfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 3),
          ("yes", 1))
    )


_Sfbrm100SysCfgMatch_Type.__name__ = "Integer32"
_Sfbrm100SysCfgMatch_Object = MibTableColumn
sfbrm100SysCfgMatch = _Sfbrm100SysCfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 5),
    _Sfbrm100SysCfgMatch_Type()
)
sfbrm100SysCfgMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysCfgMatch.setStatus("mandatory")
_Sfbrm100SysBootLoaderRevision_Type = OctetString
_Sfbrm100SysBootLoaderRevision_Object = MibTableColumn
sfbrm100SysBootLoaderRevision = _Sfbrm100SysBootLoaderRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 6),
    _Sfbrm100SysBootLoaderRevision_Type()
)
sfbrm100SysBootLoaderRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysBootLoaderRevision.setStatus("mandatory")
_Sfbrm100SysFirmwareRevision_Type = OctetString
_Sfbrm100SysFirmwareRevision_Object = MibTableColumn
sfbrm100SysFirmwareRevision = _Sfbrm100SysFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 7),
    _Sfbrm100SysFirmwareRevision_Type()
)
sfbrm100SysFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysFirmwareRevision.setStatus("mandatory")
_Sfbrm100SysSerialNumber_Type = Integer32
_Sfbrm100SysSerialNumber_Object = MibTableColumn
sfbrm100SysSerialNumber = _Sfbrm100SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 8),
    _Sfbrm100SysSerialNumber_Type()
)
sfbrm100SysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysSerialNumber.setStatus("mandatory")
_Sfbrm100SysBIAddress_Type = Integer32
_Sfbrm100SysBIAddress_Object = MibTableColumn
sfbrm100SysBIAddress = _Sfbrm100SysBIAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 9),
    _Sfbrm100SysBIAddress_Type()
)
sfbrm100SysBIAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysBIAddress.setStatus("mandatory")
_Sfbrm100SysSlotIndex_Type = Integer32
_Sfbrm100SysSlotIndex_Object = MibTableColumn
sfbrm100SysSlotIndex = _Sfbrm100SysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 10),
    _Sfbrm100SysSlotIndex_Type()
)
sfbrm100SysSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysSlotIndex.setStatus("mandatory")
_Sfbrm100SysNumPorts_Type = Integer32
_Sfbrm100SysNumPorts_Object = MibTableColumn
sfbrm100SysNumPorts = _Sfbrm100SysNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 11),
    _Sfbrm100SysNumPorts_Type()
)
sfbrm100SysNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysNumPorts.setStatus("mandatory")
_Sfbrm100SysMACAddress_Type = PhysAddress
_Sfbrm100SysMACAddress_Object = MibTableColumn
sfbrm100SysMACAddress = _Sfbrm100SysMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 12),
    _Sfbrm100SysMACAddress_Type()
)
sfbrm100SysMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysMACAddress.setStatus("mandatory")


class _Sfbrm100SystemReset_Type(Integer32):
    """Custom type sfbrm100SystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("reset", 1))
    )


_Sfbrm100SystemReset_Type.__name__ = "Integer32"
_Sfbrm100SystemReset_Object = MibTableColumn
sfbrm100SystemReset = _Sfbrm100SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 13),
    _Sfbrm100SystemReset_Type()
)
sfbrm100SystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SystemReset.setStatus("mandatory")
_Sfbrm100SysIPaddress_Type = IpAddress
_Sfbrm100SysIPaddress_Object = MibTableColumn
sfbrm100SysIPaddress = _Sfbrm100SysIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 14),
    _Sfbrm100SysIPaddress_Type()
)
sfbrm100SysIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysIPaddress.setStatus("mandatory")
_Sfbrm100SysSubnetMask_Type = IpAddress
_Sfbrm100SysSubnetMask_Object = MibTableColumn
sfbrm100SysSubnetMask = _Sfbrm100SysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 15),
    _Sfbrm100SysSubnetMask_Type()
)
sfbrm100SysSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysSubnetMask.setStatus("mandatory")
_Sfbrm100SysDefGateway_Type = IpAddress
_Sfbrm100SysDefGateway_Object = MibTableColumn
sfbrm100SysDefGateway = _Sfbrm100SysDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 16),
    _Sfbrm100SysDefGateway_Type()
)
sfbrm100SysDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysDefGateway.setStatus("mandatory")
_Sfbrm100SysSNMPTrapMgr_Type = IpAddress
_Sfbrm100SysSNMPTrapMgr_Object = MibTableColumn
sfbrm100SysSNMPTrapMgr = _Sfbrm100SysSNMPTrapMgr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 17),
    _Sfbrm100SysSNMPTrapMgr_Type()
)
sfbrm100SysSNMPTrapMgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysSNMPTrapMgr.setStatus("mandatory")


class _Sfbrm100SysRadiusAuth_Type(Integer32):
    """Custom type sfbrm100SysRadiusAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Sfbrm100SysRadiusAuth_Type.__name__ = "Integer32"
_Sfbrm100SysRadiusAuth_Object = MibTableColumn
sfbrm100SysRadiusAuth = _Sfbrm100SysRadiusAuth_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 18),
    _Sfbrm100SysRadiusAuth_Type()
)
sfbrm100SysRadiusAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysRadiusAuth.setStatus("mandatory")
_Sfbrm100SysRadiusServerAddr_Type = IpAddress
_Sfbrm100SysRadiusServerAddr_Object = MibTableColumn
sfbrm100SysRadiusServerAddr = _Sfbrm100SysRadiusServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 19),
    _Sfbrm100SysRadiusServerAddr_Type()
)
sfbrm100SysRadiusServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysRadiusServerAddr.setStatus("mandatory")
_Sfbrm100SysRadiusSecret_Type = OctetString
_Sfbrm100SysRadiusSecret_Object = MibTableColumn
sfbrm100SysRadiusSecret = _Sfbrm100SysRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 20),
    _Sfbrm100SysRadiusSecret_Type()
)
sfbrm100SysRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysRadiusSecret.setStatus("mandatory")
_Sfbrm100SysRadiusRetry_Type = Integer32
_Sfbrm100SysRadiusRetry_Object = MibTableColumn
sfbrm100SysRadiusRetry = _Sfbrm100SysRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 21),
    _Sfbrm100SysRadiusRetry_Type()
)
sfbrm100SysRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysRadiusRetry.setStatus("mandatory")
_Sfbrm100SysRadiusTimeout_Type = Integer32
_Sfbrm100SysRadiusTimeout_Object = MibTableColumn
sfbrm100SysRadiusTimeout = _Sfbrm100SysRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 22),
    _Sfbrm100SysRadiusTimeout_Type()
)
sfbrm100SysRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysRadiusTimeout.setStatus("mandatory")


class _Sfbrm100SysDHCPEnable_Type(Integer32):
    """Custom type sfbrm100SysDHCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysDHCPEnable_Type.__name__ = "Integer32"
_Sfbrm100SysDHCPEnable_Object = MibTableColumn
sfbrm100SysDHCPEnable = _Sfbrm100SysDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 23),
    _Sfbrm100SysDHCPEnable_Type()
)
sfbrm100SysDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysDHCPEnable.setStatus("mandatory")


class _Sfbrm100SysSerialAccess_Type(Integer32):
    """Custom type sfbrm100SysSerialAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysSerialAccess_Type.__name__ = "Integer32"
_Sfbrm100SysSerialAccess_Object = MibTableColumn
sfbrm100SysSerialAccess = _Sfbrm100SysSerialAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 24),
    _Sfbrm100SysSerialAccess_Type()
)
sfbrm100SysSerialAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysSerialAccess.setStatus("mandatory")


class _Sfbrm100SysTLPT_Type(Integer32):
    """Custom type sfbrm100SysTLPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysTLPT_Type.__name__ = "Integer32"
_Sfbrm100SysTLPT_Object = MibTableColumn
sfbrm100SysTLPT = _Sfbrm100SysTLPT_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 25),
    _Sfbrm100SysTLPT_Type()
)
sfbrm100SysTLPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysTLPT.setStatus("mandatory")
_Sfbrm100SysTFTPServerAddr_Type = IpAddress
_Sfbrm100SysTFTPServerAddr_Object = MibTableColumn
sfbrm100SysTFTPServerAddr = _Sfbrm100SysTFTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 26),
    _Sfbrm100SysTFTPServerAddr_Type()
)
sfbrm100SysTFTPServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysTFTPServerAddr.setStatus("mandatory")
_Sfbrm100SysTFTPfilename_Type = OctetString
_Sfbrm100SysTFTPfilename_Object = MibTableColumn
sfbrm100SysTFTPfilename = _Sfbrm100SysTFTPfilename_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 27),
    _Sfbrm100SysTFTPfilename_Type()
)
sfbrm100SysTFTPfilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysTFTPfilename.setStatus("mandatory")


class _Sfbrm100SysTFTPCmd_Type(Integer32):
    """Custom type sfbrm100SysTFTPCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 2),
          ("notApplicable", 3),
          ("perform", 1))
    )


_Sfbrm100SysTFTPCmd_Type.__name__ = "Integer32"
_Sfbrm100SysTFTPCmd_Object = MibTableColumn
sfbrm100SysTFTPCmd = _Sfbrm100SysTFTPCmd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 28),
    _Sfbrm100SysTFTPCmd_Type()
)
sfbrm100SysTFTPCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysTFTPCmd.setStatus("mandatory")


class _Sfbrm100SysTFTPServerIgnore_Type(Integer32):
    """Custom type sfbrm100SysTFTPServerIgnore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100SysTFTPServerIgnore_Type.__name__ = "Integer32"
_Sfbrm100SysTFTPServerIgnore_Object = MibTableColumn
sfbrm100SysTFTPServerIgnore = _Sfbrm100SysTFTPServerIgnore_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 29),
    _Sfbrm100SysTFTPServerIgnore_Type()
)
sfbrm100SysTFTPServerIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysTFTPServerIgnore.setStatus("mandatory")
_Sfbrm100SysMgmtVlanId_Type = Integer32
_Sfbrm100SysMgmtVlanId_Object = MibTableColumn
sfbrm100SysMgmtVlanId = _Sfbrm100SysMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 30),
    _Sfbrm100SysMgmtVlanId_Type()
)
sfbrm100SysMgmtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysMgmtVlanId.setStatus("mandatory")


class _Sfbrm100SysSNMPAccess_Type(Integer32):
    """Custom type sfbrm100SysSNMPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysSNMPAccess_Type.__name__ = "Integer32"
_Sfbrm100SysSNMPAccess_Object = MibTableColumn
sfbrm100SysSNMPAccess = _Sfbrm100SysSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 31),
    _Sfbrm100SysSNMPAccess_Type()
)
sfbrm100SysSNMPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysSNMPAccess.setStatus("mandatory")


class _Sfbrm100SysIPAccess_Type(Integer32):
    """Custom type sfbrm100SysIPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysIPAccess_Type.__name__ = "Integer32"
_Sfbrm100SysIPAccess_Object = MibTableColumn
sfbrm100SysIPAccess = _Sfbrm100SysIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 32),
    _Sfbrm100SysIPAccess_Type()
)
sfbrm100SysIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysIPAccess.setStatus("mandatory")


class _Sfbrm100SysLastGaspPdu_Type(Integer32):
    """Custom type sfbrm100SysLastGaspPdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamDyingGaspPdu", 2),
          ("snmpTrap", 1))
    )


_Sfbrm100SysLastGaspPdu_Type.__name__ = "Integer32"
_Sfbrm100SysLastGaspPdu_Object = MibTableColumn
sfbrm100SysLastGaspPdu = _Sfbrm100SysLastGaspPdu_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 33),
    _Sfbrm100SysLastGaspPdu_Type()
)
sfbrm100SysLastGaspPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysLastGaspPdu.setStatus("mandatory")
_Sfbrm100SysLastGaspPort_Type = Integer32
_Sfbrm100SysLastGaspPort_Object = MibTableColumn
sfbrm100SysLastGaspPort = _Sfbrm100SysLastGaspPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 34),
    _Sfbrm100SysLastGaspPort_Type()
)
sfbrm100SysLastGaspPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysLastGaspPort.setStatus("mandatory")


class _Sfbrm100SysLocalLPT_Type(Integer32):
    """Custom type sfbrm100SysLocalLPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysLocalLPT_Type.__name__ = "Integer32"
_Sfbrm100SysLocalLPT_Object = MibTableColumn
sfbrm100SysLocalLPT = _Sfbrm100SysLocalLPT_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 35),
    _Sfbrm100SysLocalLPT_Type()
)
sfbrm100SysLocalLPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysLocalLPT.setStatus("mandatory")
_Sfbrm100SysLPTPort_Type = Integer32
_Sfbrm100SysLPTPort_Object = MibTableColumn
sfbrm100SysLPTPort = _Sfbrm100SysLPTPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 36),
    _Sfbrm100SysLPTPort_Type()
)
sfbrm100SysLPTPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysLPTPort.setStatus("mandatory")


class _Sfbrm100SysAutoUpgrade_Type(Integer32):
    """Custom type sfbrm100SysAutoUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SysAutoUpgrade_Type.__name__ = "Integer32"
_Sfbrm100SysAutoUpgrade_Object = MibTableColumn
sfbrm100SysAutoUpgrade = _Sfbrm100SysAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 37),
    _Sfbrm100SysAutoUpgrade_Type()
)
sfbrm100SysAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysAutoUpgrade.setStatus("mandatory")
_Sfbrm100SysFormFactorSlot_Type = Integer32
_Sfbrm100SysFormFactorSlot_Object = MibTableColumn
sfbrm100SysFormFactorSlot = _Sfbrm100SysFormFactorSlot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 38),
    _Sfbrm100SysFormFactorSlot_Type()
)
sfbrm100SysFormFactorSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysFormFactorSlot.setStatus("mandatory")
_Sfbrm100SysFormFactorPort_Type = Integer32
_Sfbrm100SysFormFactorPort_Object = MibTableColumn
sfbrm100SysFormFactorPort = _Sfbrm100SysFormFactorPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 39),
    _Sfbrm100SysFormFactorPort_Type()
)
sfbrm100SysFormFactorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SysFormFactorPort.setStatus("mandatory")
_Sfbrm100SysOAMPort_Type = Integer32
_Sfbrm100SysOAMPort_Object = MibTableColumn
sfbrm100SysOAMPort = _Sfbrm100SysOAMPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 1, 1, 1, 40),
    _Sfbrm100SysOAMPort_Type()
)
sfbrm100SysOAMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SysOAMPort.setStatus("mandatory")
_SfbrmSwitch_ObjectIdentity = ObjectIdentity
sfbrmSwitch = _SfbrmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2)
)
_Sfbrm100SwTable_Object = MibTable
sfbrm100SwTable = _Sfbrm100SwTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sfbrm100SwTable.setStatus("mandatory")
_Sfbrm100SwEntry_Object = MibTableRow
sfbrm100SwEntry = _Sfbrm100SwEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1)
)
sfbrm100SwEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100SwPortIndex"),
    (0, "TNI-MIB", "sfbrm100SwSecIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100SwEntry.setStatus("mandatory")
_Sfbrm100SwPortIndex_Type = Integer32
_Sfbrm100SwPortIndex_Object = MibTableColumn
sfbrm100SwPortIndex = _Sfbrm100SwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 1),
    _Sfbrm100SwPortIndex_Type()
)
sfbrm100SwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SwPortIndex.setStatus("mandatory")
_Sfbrm100SwSecIndex_Type = Integer32
_Sfbrm100SwSecIndex_Object = MibTableColumn
sfbrm100SwSecIndex = _Sfbrm100SwSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 2),
    _Sfbrm100SwSecIndex_Type()
)
sfbrm100SwSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SwSecIndex.setStatus("mandatory")
_Sfbrm100SwATUAgeTimeout_Type = Integer32
_Sfbrm100SwATUAgeTimeout_Object = MibTableColumn
sfbrm100SwATUAgeTimeout = _Sfbrm100SwATUAgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 3),
    _Sfbrm100SwATUAgeTimeout_Type()
)
sfbrm100SwATUAgeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwATUAgeTimeout.setStatus("mandatory")
_Sfbrm100SwIngressMonPort_Type = Integer32
_Sfbrm100SwIngressMonPort_Object = MibTableColumn
sfbrm100SwIngressMonPort = _Sfbrm100SwIngressMonPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 4),
    _Sfbrm100SwIngressMonPort_Type()
)
sfbrm100SwIngressMonPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIngressMonPort.setStatus("mandatory")
_Sfbrm100SwEgressMonPort_Type = Integer32
_Sfbrm100SwEgressMonPort_Object = MibTableColumn
sfbrm100SwEgressMonPort = _Sfbrm100SwEgressMonPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 5),
    _Sfbrm100SwEgressMonPort_Type()
)
sfbrm100SwEgressMonPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwEgressMonPort.setStatus("mandatory")


class _Sfbrm100SwFactoryDefaults_Type(Integer32):
    """Custom type sfbrm100SwFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 2),
          ("reset", 1))
    )


_Sfbrm100SwFactoryDefaults_Type.__name__ = "Integer32"
_Sfbrm100SwFactoryDefaults_Object = MibTableColumn
sfbrm100SwFactoryDefaults = _Sfbrm100SwFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 6),
    _Sfbrm100SwFactoryDefaults_Type()
)
sfbrm100SwFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwFactoryDefaults.setStatus("mandatory")


class _Sfbrm100SwResetCounters_Type(Integer32):
    """Custom type sfbrm100SwResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 2),
          ("reset", 1))
    )


_Sfbrm100SwResetCounters_Type.__name__ = "Integer32"
_Sfbrm100SwResetCounters_Object = MibTableColumn
sfbrm100SwResetCounters = _Sfbrm100SwResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 7),
    _Sfbrm100SwResetCounters_Type()
)
sfbrm100SwResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwResetCounters.setStatus("mandatory")


class _Sfbrm100SwHistMode_Type(Integer32):
    """Custom type sfbrm100SwHistMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cntRx", 1),
          ("cntRxTx", 3),
          ("cntTx", 2))
    )


_Sfbrm100SwHistMode_Type.__name__ = "Integer32"
_Sfbrm100SwHistMode_Object = MibTableColumn
sfbrm100SwHistMode = _Sfbrm100SwHistMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 8),
    _Sfbrm100SwHistMode_Type()
)
sfbrm100SwHistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwHistMode.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap0_Type = Integer32
_Sfbrm100SwIEEEPriRemap0_Object = MibTableColumn
sfbrm100SwIEEEPriRemap0 = _Sfbrm100SwIEEEPriRemap0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 9),
    _Sfbrm100SwIEEEPriRemap0_Type()
)
sfbrm100SwIEEEPriRemap0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap0.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap1_Type = Integer32
_Sfbrm100SwIEEEPriRemap1_Object = MibTableColumn
sfbrm100SwIEEEPriRemap1 = _Sfbrm100SwIEEEPriRemap1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 10),
    _Sfbrm100SwIEEEPriRemap1_Type()
)
sfbrm100SwIEEEPriRemap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap1.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap2_Type = Integer32
_Sfbrm100SwIEEEPriRemap2_Object = MibTableColumn
sfbrm100SwIEEEPriRemap2 = _Sfbrm100SwIEEEPriRemap2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 11),
    _Sfbrm100SwIEEEPriRemap2_Type()
)
sfbrm100SwIEEEPriRemap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap2.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap3_Type = Integer32
_Sfbrm100SwIEEEPriRemap3_Object = MibTableColumn
sfbrm100SwIEEEPriRemap3 = _Sfbrm100SwIEEEPriRemap3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 12),
    _Sfbrm100SwIEEEPriRemap3_Type()
)
sfbrm100SwIEEEPriRemap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap3.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap4_Type = Integer32
_Sfbrm100SwIEEEPriRemap4_Object = MibTableColumn
sfbrm100SwIEEEPriRemap4 = _Sfbrm100SwIEEEPriRemap4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 13),
    _Sfbrm100SwIEEEPriRemap4_Type()
)
sfbrm100SwIEEEPriRemap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap4.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap5_Type = Integer32
_Sfbrm100SwIEEEPriRemap5_Object = MibTableColumn
sfbrm100SwIEEEPriRemap5 = _Sfbrm100SwIEEEPriRemap5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 14),
    _Sfbrm100SwIEEEPriRemap5_Type()
)
sfbrm100SwIEEEPriRemap5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap5.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap6_Type = Integer32
_Sfbrm100SwIEEEPriRemap6_Object = MibTableColumn
sfbrm100SwIEEEPriRemap6 = _Sfbrm100SwIEEEPriRemap6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 15),
    _Sfbrm100SwIEEEPriRemap6_Type()
)
sfbrm100SwIEEEPriRemap6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap6.setStatus("mandatory")
_Sfbrm100SwIEEEPriRemap7_Type = Integer32
_Sfbrm100SwIEEEPriRemap7_Object = MibTableColumn
sfbrm100SwIEEEPriRemap7 = _Sfbrm100SwIEEEPriRemap7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 16),
    _Sfbrm100SwIEEEPriRemap7_Type()
)
sfbrm100SwIEEEPriRemap7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIEEEPriRemap7.setStatus("mandatory")


class _Sfbrm100SwFlushFdb_Type(Integer32):
    """Custom type sfbrm100SwFlushFdb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 3),
          ("flushAll", 1),
          ("flushNonStatic", 2))
    )


_Sfbrm100SwFlushFdb_Type.__name__ = "Integer32"
_Sfbrm100SwFlushFdb_Object = MibTableColumn
sfbrm100SwFlushFdb = _Sfbrm100SwFlushFdb_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 17),
    _Sfbrm100SwFlushFdb_Type()
)
sfbrm100SwFlushFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwFlushFdb.setStatus("mandatory")


class _Sfbrm100SwFlushVlandb_Type(Integer32):
    """Custom type sfbrm100SwFlushVlandb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("flushAll", 1))
    )


_Sfbrm100SwFlushVlandb_Type.__name__ = "Integer32"
_Sfbrm100SwFlushVlandb_Object = MibTableColumn
sfbrm100SwFlushVlandb = _Sfbrm100SwFlushVlandb_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 18),
    _Sfbrm100SwFlushVlandb_Type()
)
sfbrm100SwFlushVlandb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwFlushVlandb.setStatus("mandatory")


class _Sfbrm100SwUseDoubleTagData_Type(Integer32):
    """Custom type sfbrm100SwUseDoubleTagData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("use", 1))
    )


_Sfbrm100SwUseDoubleTagData_Type.__name__ = "Integer32"
_Sfbrm100SwUseDoubleTagData_Object = MibTableColumn
sfbrm100SwUseDoubleTagData = _Sfbrm100SwUseDoubleTagData_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 19),
    _Sfbrm100SwUseDoubleTagData_Type()
)
sfbrm100SwUseDoubleTagData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwUseDoubleTagData.setStatus("mandatory")


class _Sfbrm100SwFiberRedundancy_Type(Integer32):
    """Custom type sfbrm100SwFiberRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100SwFiberRedundancy_Type.__name__ = "Integer32"
_Sfbrm100SwFiberRedundancy_Object = MibTableColumn
sfbrm100SwFiberRedundancy = _Sfbrm100SwFiberRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 20),
    _Sfbrm100SwFiberRedundancy_Type()
)
sfbrm100SwFiberRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwFiberRedundancy.setStatus("mandatory")


class _Sfbrm100SwFiberRedundRevert_Type(Integer32):
    """Custom type sfbrm100SwFiberRedundRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRevert", 2),
          ("notApplicable", 3),
          ("revert", 1))
    )


_Sfbrm100SwFiberRedundRevert_Type.__name__ = "Integer32"
_Sfbrm100SwFiberRedundRevert_Object = MibTableColumn
sfbrm100SwFiberRedundRevert = _Sfbrm100SwFiberRedundRevert_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 21),
    _Sfbrm100SwFiberRedundRevert_Type()
)
sfbrm100SwFiberRedundRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwFiberRedundRevert.setStatus("mandatory")
_Sfbrm100SwFbrRedundActivePort_Type = Integer32
_Sfbrm100SwFbrRedundActivePort_Object = MibTableColumn
sfbrm100SwFbrRedundActivePort = _Sfbrm100SwFbrRedundActivePort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 22),
    _Sfbrm100SwFbrRedundActivePort_Type()
)
sfbrm100SwFbrRedundActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwFbrRedundActivePort.setStatus("mandatory")


class _Sfbrm100SwSupressVlanViolations_Type(Integer32):
    """Custom type sfbrm100SwSupressVlanViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SwSupressVlanViolations_Type.__name__ = "Integer32"
_Sfbrm100SwSupressVlanViolations_Object = MibTableColumn
sfbrm100SwSupressVlanViolations = _Sfbrm100SwSupressVlanViolations_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 23),
    _Sfbrm100SwSupressVlanViolations_Type()
)
sfbrm100SwSupressVlanViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwSupressVlanViolations.setStatus("mandatory")


class _Sfbrm100SwSupressMACViolations_Type(Integer32):
    """Custom type sfbrm100SwSupressMACViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100SwSupressMACViolations_Type.__name__ = "Integer32"
_Sfbrm100SwSupressMACViolations_Object = MibTableColumn
sfbrm100SwSupressMACViolations = _Sfbrm100SwSupressMACViolations_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 1, 1, 24),
    _Sfbrm100SwSupressMACViolations_Type()
)
sfbrm100SwSupressMACViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwSupressMACViolations.setStatus("mandatory")
_Sfbrm100SwIPPrioTable_Object = MibTable
sfbrm100SwIPPrioTable = _Sfbrm100SwIPPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sfbrm100SwIPPrioTable.setStatus("mandatory")
_Sfbrm100SwIPPrioEntry_Object = MibTableRow
sfbrm100SwIPPrioEntry = _Sfbrm100SwIPPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 2, 1)
)
sfbrm100SwIPPrioEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100SwIPPrioPortIndex"),
    (0, "TNI-MIB", "sfbrm100SwIPPrioIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100SwIPPrioEntry.setStatus("mandatory")
_Sfbrm100SwIPPrioPortIndex_Type = Integer32
_Sfbrm100SwIPPrioPortIndex_Object = MibTableColumn
sfbrm100SwIPPrioPortIndex = _Sfbrm100SwIPPrioPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 2, 1, 1),
    _Sfbrm100SwIPPrioPortIndex_Type()
)
sfbrm100SwIPPrioPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SwIPPrioPortIndex.setStatus("mandatory")
_Sfbrm100SwIPPrioIndex_Type = Integer32
_Sfbrm100SwIPPrioIndex_Object = MibTableColumn
sfbrm100SwIPPrioIndex = _Sfbrm100SwIPPrioIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 2, 1, 2),
    _Sfbrm100SwIPPrioIndex_Type()
)
sfbrm100SwIPPrioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SwIPPrioIndex.setStatus("mandatory")
_Sfbrm100SwIPPrioTC_Type = Integer32
_Sfbrm100SwIPPrioTC_Object = MibTableColumn
sfbrm100SwIPPrioTC = _Sfbrm100SwIPPrioTC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 2, 1, 3),
    _Sfbrm100SwIPPrioTC_Type()
)
sfbrm100SwIPPrioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100SwIPPrioTC.setStatus("mandatory")


class _Sfbrm100SwIPPrioRemap_Type(Integer32):
    """Custom type sfbrm100SwIPPrioRemap based on Integer32"""
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
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4))
    )


_Sfbrm100SwIPPrioRemap_Type.__name__ = "Integer32"
_Sfbrm100SwIPPrioRemap_Object = MibTableColumn
sfbrm100SwIPPrioRemap = _Sfbrm100SwIPPrioRemap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 2, 2, 1, 4),
    _Sfbrm100SwIPPrioRemap_Type()
)
sfbrm100SwIPPrioRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SwIPPrioRemap.setStatus("mandatory")
_SfbrmPort_ObjectIdentity = ObjectIdentity
sfbrmPort = _SfbrmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3)
)
_Sfbrm100PortTable_Object = MibTable
sfbrm100PortTable = _Sfbrm100PortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sfbrm100PortTable.setStatus("mandatory")
_Sfbrm100PortEntry_Object = MibTableRow
sfbrm100PortEntry = _Sfbrm100PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1)
)
sfbrm100PortEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100PortLocIndex"),
    (0, "TNI-MIB", "sfbrm100PortRmtIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100PortEntry.setStatus("mandatory")
_Sfbrm100PortLocIndex_Type = Integer32
_Sfbrm100PortLocIndex_Object = MibTableColumn
sfbrm100PortLocIndex = _Sfbrm100PortLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 1),
    _Sfbrm100PortLocIndex_Type()
)
sfbrm100PortLocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortLocIndex.setStatus("mandatory")
_Sfbrm100PortRmtIndex_Type = Integer32
_Sfbrm100PortRmtIndex_Object = MibTableColumn
sfbrm100PortRmtIndex = _Sfbrm100PortRmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 2),
    _Sfbrm100PortRmtIndex_Type()
)
sfbrm100PortRmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortRmtIndex.setStatus("mandatory")
_Sfbrm100PortGrpString_Type = DisplayString
_Sfbrm100PortGrpString_Object = MibTableColumn
sfbrm100PortGrpString = _Sfbrm100PortGrpString_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 3),
    _Sfbrm100PortGrpString_Type()
)
sfbrm100PortGrpString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortGrpString.setStatus("mandatory")
_Sfbrm100PortConnType_Type = CpsConnector
_Sfbrm100PortConnType_Object = MibTableColumn
sfbrm100PortConnType = _Sfbrm100PortConnType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 4),
    _Sfbrm100PortConnType_Type()
)
sfbrm100PortConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortConnType.setStatus("mandatory")


class _Sfbrm100PortOAMState_Type(Integer32):
    """Custom type sfbrm100PortOAMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortOAMState_Type.__name__ = "Integer32"
_Sfbrm100PortOAMState_Object = MibTableColumn
sfbrm100PortOAMState = _Sfbrm100PortOAMState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 5),
    _Sfbrm100PortOAMState_Type()
)
sfbrm100PortOAMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortOAMState.setStatus("mandatory")


class _Sfbrm100PortOAMModeCtrl_Type(Integer32):
    """Custom type sfbrm100PortOAMModeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Sfbrm100PortOAMModeCtrl_Type.__name__ = "Integer32"
_Sfbrm100PortOAMModeCtrl_Object = MibTableColumn
sfbrm100PortOAMModeCtrl = _Sfbrm100PortOAMModeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 6),
    _Sfbrm100PortOAMModeCtrl_Type()
)
sfbrm100PortOAMModeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortOAMModeCtrl.setStatus("mandatory")


class _Sfbrm100PortRmtLoopback_Type(Integer32):
    """Custom type sfbrm100PortRmtLoopback based on Integer32"""
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
        *(("alternateLoopback", 2),
          ("disable", 3),
          ("notSupported", 4),
          ("oamLoopback", 1))
    )


_Sfbrm100PortRmtLoopback_Type.__name__ = "Integer32"
_Sfbrm100PortRmtLoopback_Object = MibTableColumn
sfbrm100PortRmtLoopback = _Sfbrm100PortRmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 7),
    _Sfbrm100PortRmtLoopback_Type()
)
sfbrm100PortRmtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortRmtLoopback.setStatus("mandatory")


class _Sfbrm100PortIgnoreLoopback_Type(Integer32):
    """Custom type sfbrm100PortIgnoreLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_Sfbrm100PortIgnoreLoopback_Type.__name__ = "Integer32"
_Sfbrm100PortIgnoreLoopback_Object = MibTableColumn
sfbrm100PortIgnoreLoopback = _Sfbrm100PortIgnoreLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 8),
    _Sfbrm100PortIgnoreLoopback_Type()
)
sfbrm100PortIgnoreLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIgnoreLoopback.setStatus("mandatory")


class _Sfbrm100PortAdvPause_Type(Integer32):
    """Custom type sfbrm100PortAdvPause based on Integer32"""
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
        *(("asymPauseCon", 4),
          ("asymPauseLp", 3),
          ("noPause", 1),
          ("notApplicable", 5),
          ("symPause", 2))
    )


_Sfbrm100PortAdvPause_Type.__name__ = "Integer32"
_Sfbrm100PortAdvPause_Object = MibTableColumn
sfbrm100PortAdvPause = _Sfbrm100PortAdvPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 9),
    _Sfbrm100PortAdvPause_Type()
)
sfbrm100PortAdvPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdvPause.setStatus("mandatory")


class _Sfbrm100PortAdv1000FDX_Type(Integer32):
    """Custom type sfbrm100PortAdv1000FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortAdv1000FDX_Type.__name__ = "Integer32"
_Sfbrm100PortAdv1000FDX_Object = MibTableColumn
sfbrm100PortAdv1000FDX = _Sfbrm100PortAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 10),
    _Sfbrm100PortAdv1000FDX_Type()
)
sfbrm100PortAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdv1000FDX.setStatus("mandatory")


class _Sfbrm100PortAdv1000HDX_Type(Integer32):
    """Custom type sfbrm100PortAdv1000HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortAdv1000HDX_Type.__name__ = "Integer32"
_Sfbrm100PortAdv1000HDX_Object = MibTableColumn
sfbrm100PortAdv1000HDX = _Sfbrm100PortAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 11),
    _Sfbrm100PortAdv1000HDX_Type()
)
sfbrm100PortAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdv1000HDX.setStatus("mandatory")


class _Sfbrm100PortAdv100FDX_Type(Integer32):
    """Custom type sfbrm100PortAdv100FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortAdv100FDX_Type.__name__ = "Integer32"
_Sfbrm100PortAdv100FDX_Object = MibTableColumn
sfbrm100PortAdv100FDX = _Sfbrm100PortAdv100FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 12),
    _Sfbrm100PortAdv100FDX_Type()
)
sfbrm100PortAdv100FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdv100FDX.setStatus("mandatory")


class _Sfbrm100PortAdv100HDX_Type(Integer32):
    """Custom type sfbrm100PortAdv100HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortAdv100HDX_Type.__name__ = "Integer32"
_Sfbrm100PortAdv100HDX_Object = MibTableColumn
sfbrm100PortAdv100HDX = _Sfbrm100PortAdv100HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 13),
    _Sfbrm100PortAdv100HDX_Type()
)
sfbrm100PortAdv100HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdv100HDX.setStatus("mandatory")


class _Sfbrm100PortAdv10FDX_Type(Integer32):
    """Custom type sfbrm100PortAdv10FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortAdv10FDX_Type.__name__ = "Integer32"
_Sfbrm100PortAdv10FDX_Object = MibTableColumn
sfbrm100PortAdv10FDX = _Sfbrm100PortAdv10FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 14),
    _Sfbrm100PortAdv10FDX_Type()
)
sfbrm100PortAdv10FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdv10FDX.setStatus("mandatory")


class _Sfbrm100PortAdv10HDX_Type(Integer32):
    """Custom type sfbrm100PortAdv10HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortAdv10HDX_Type.__name__ = "Integer32"
_Sfbrm100PortAdv10HDX_Object = MibTableColumn
sfbrm100PortAdv10HDX = _Sfbrm100PortAdv10HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 15),
    _Sfbrm100PortAdv10HDX_Type()
)
sfbrm100PortAdv10HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdv10HDX.setStatus("mandatory")


class _Sfbrm100PortAutoneg_Type(Integer32):
    """Custom type sfbrm100PortAutoneg based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("negotiating", 3),
          ("resolved", 4))
    )


_Sfbrm100PortAutoneg_Type.__name__ = "Integer32"
_Sfbrm100PortAutoneg_Object = MibTableColumn
sfbrm100PortAutoneg = _Sfbrm100PortAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 16),
    _Sfbrm100PortAutoneg_Type()
)
sfbrm100PortAutoneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAutoneg.setStatus("mandatory")


class _Sfbrm100PortFDuplex_Type(Integer32):
    """Custom type sfbrm100PortFDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 3))
    )


_Sfbrm100PortFDuplex_Type.__name__ = "Integer32"
_Sfbrm100PortFDuplex_Object = MibTableColumn
sfbrm100PortFDuplex = _Sfbrm100PortFDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 17),
    _Sfbrm100PortFDuplex_Type()
)
sfbrm100PortFDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortFDuplex.setStatus("mandatory")


class _Sfbrm100PortFSpeed_Type(Integer32):
    """Custom type sfbrm100PortFSpeed based on Integer32"""
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
        *(("mbps10", 1),
          ("mbps100", 2),
          ("mbps1000", 3),
          ("notApplicable", 4))
    )


_Sfbrm100PortFSpeed_Type.__name__ = "Integer32"
_Sfbrm100PortFSpeed_Object = MibTableColumn
sfbrm100PortFSpeed = _Sfbrm100PortFSpeed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 18),
    _Sfbrm100PortFSpeed_Type()
)
sfbrm100PortFSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortFSpeed.setStatus("mandatory")


class _Sfbrm100PortLpPauseAbility_Type(Integer32):
    """Custom type sfbrm100PortLpPauseAbility based on Integer32"""
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
        *(("asymPauseCon", 4),
          ("asymPauseLp", 3),
          ("noPause", 1),
          ("notApplicable", 5),
          ("symPause", 2))
    )


_Sfbrm100PortLpPauseAbility_Type.__name__ = "Integer32"
_Sfbrm100PortLpPauseAbility_Object = MibTableColumn
sfbrm100PortLpPauseAbility = _Sfbrm100PortLpPauseAbility_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 19),
    _Sfbrm100PortLpPauseAbility_Type()
)
sfbrm100PortLpPauseAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortLpPauseAbility.setStatus("mandatory")


class _Sfbrm100PortLpAutonegAbility_Type(Integer32):
    """Custom type sfbrm100PortLpAutonegAbility based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("notcapable", 13),
          ("spd1000DupAuto", 2),
          ("spd1000DupFull", 7),
          ("spd1000DupHalf", 8),
          ("spd100DupAuto", 3),
          ("spd100DupFull", 9),
          ("spd100DupHalf", 10),
          ("spd10DupAuto", 4),
          ("spd10DupFull", 11),
          ("spd10DupHalf", 12),
          ("spdAutoDupAuto", 1),
          ("spdAutoDupFull", 5),
          ("spdAutoDupHalf", 6))
    )


_Sfbrm100PortLpAutonegAbility_Type.__name__ = "Integer32"
_Sfbrm100PortLpAutonegAbility_Object = MibTableColumn
sfbrm100PortLpAutonegAbility = _Sfbrm100PortLpAutonegAbility_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 20),
    _Sfbrm100PortLpAutonegAbility_Type()
)
sfbrm100PortLpAutonegAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortLpAutonegAbility.setStatus("mandatory")


class _Sfbrm100PortLinkState_Type(Integer32):
    """Custom type sfbrm100PortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notApplicable", 3),
          ("up", 1))
    )


_Sfbrm100PortLinkState_Type.__name__ = "Integer32"
_Sfbrm100PortLinkState_Object = MibTableColumn
sfbrm100PortLinkState = _Sfbrm100PortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 21),
    _Sfbrm100PortLinkState_Type()
)
sfbrm100PortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortLinkState.setStatus("mandatory")


class _Sfbrm100PortAutonegState_Type(Integer32):
    """Custom type sfbrm100PortAutonegState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notResolved", 2),
          ("resolved", 1))
    )


_Sfbrm100PortAutonegState_Type.__name__ = "Integer32"
_Sfbrm100PortAutonegState_Object = MibTableColumn
sfbrm100PortAutonegState = _Sfbrm100PortAutonegState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 22),
    _Sfbrm100PortAutonegState_Type()
)
sfbrm100PortAutonegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortAutonegState.setStatus("mandatory")


class _Sfbrm100PortDuplex_Type(Integer32):
    """Custom type sfbrm100PortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 3))
    )


_Sfbrm100PortDuplex_Type.__name__ = "Integer32"
_Sfbrm100PortDuplex_Object = MibTableColumn
sfbrm100PortDuplex = _Sfbrm100PortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 23),
    _Sfbrm100PortDuplex_Type()
)
sfbrm100PortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortDuplex.setStatus("mandatory")


class _Sfbrm100PortSpeed_Type(Integer32):
    """Custom type sfbrm100PortSpeed based on Integer32"""
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
        *(("mbps10", 1),
          ("mbps100", 2),
          ("mbps1000", 3),
          ("notApplicable", 4))
    )


_Sfbrm100PortSpeed_Type.__name__ = "Integer32"
_Sfbrm100PortSpeed_Object = MibTableColumn
sfbrm100PortSpeed = _Sfbrm100PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 24),
    _Sfbrm100PortSpeed_Type()
)
sfbrm100PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortSpeed.setStatus("mandatory")


class _Sfbrm100PortFEFI_Type(Integer32):
    """Custom type sfbrm100PortFEFI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Sfbrm100PortFEFI_Type.__name__ = "Integer32"
_Sfbrm100PortFEFI_Object = MibTableColumn
sfbrm100PortFEFI = _Sfbrm100PortFEFI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 25),
    _Sfbrm100PortFEFI_Type()
)
sfbrm100PortFEFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortFEFI.setStatus("mandatory")


class _Sfbrm100PortAutocross_Type(Integer32):
    """Custom type sfbrm100PortAutocross based on Integer32"""
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
        *(("autoCross", 3),
          ("mdi", 1),
          ("mdiX", 2),
          ("notApplicable", 4))
    )


_Sfbrm100PortAutocross_Type.__name__ = "Integer32"
_Sfbrm100PortAutocross_Object = MibTableColumn
sfbrm100PortAutocross = _Sfbrm100PortAutocross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 26),
    _Sfbrm100PortAutocross_Type()
)
sfbrm100PortAutocross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAutocross.setStatus("mandatory")


class _Sfbrm100PortLock_Type(Integer32):
    """Custom type sfbrm100PortLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortLock_Type.__name__ = "Integer32"
_Sfbrm100PortLock_Object = MibTableColumn
sfbrm100PortLock = _Sfbrm100PortLock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 27),
    _Sfbrm100PortLock_Type()
)
sfbrm100PortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortLock.setStatus("mandatory")


class _Sfbrm100PortIgnoreWrongData_Type(Integer32):
    """Custom type sfbrm100PortIgnoreWrongData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortIgnoreWrongData_Type.__name__ = "Integer32"
_Sfbrm100PortIgnoreWrongData_Object = MibTableColumn
sfbrm100PortIgnoreWrongData = _Sfbrm100PortIgnoreWrongData_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 28),
    _Sfbrm100PortIgnoreWrongData_Type()
)
sfbrm100PortIgnoreWrongData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIgnoreWrongData.setStatus("mandatory")


class _Sfbrm100PortIGMPSnoop_Type(Integer32):
    """Custom type sfbrm100PortIGMPSnoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortIGMPSnoop_Type.__name__ = "Integer32"
_Sfbrm100PortIGMPSnoop_Object = MibTableColumn
sfbrm100PortIGMPSnoop = _Sfbrm100PortIGMPSnoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 29),
    _Sfbrm100PortIGMPSnoop_Type()
)
sfbrm100PortIGMPSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIGMPSnoop.setStatus("mandatory")


class _Sfbrm100PortDoubleTagging_Type(Integer32):
    """Custom type sfbrm100PortDoubleTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortDoubleTagging_Type.__name__ = "Integer32"
_Sfbrm100PortDoubleTagging_Object = MibTableColumn
sfbrm100PortDoubleTagging = _Sfbrm100PortDoubleTagging_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 30),
    _Sfbrm100PortDoubleTagging_Type()
)
sfbrm100PortDoubleTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDoubleTagging.setStatus("mandatory")


class _Sfbrm100PortUseIPTC_Type(Integer32):
    """Custom type sfbrm100PortUseIPTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortUseIPTC_Type.__name__ = "Integer32"
_Sfbrm100PortUseIPTC_Object = MibTableColumn
sfbrm100PortUseIPTC = _Sfbrm100PortUseIPTC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 31),
    _Sfbrm100PortUseIPTC_Type()
)
sfbrm100PortUseIPTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortUseIPTC.setStatus("mandatory")


class _Sfbrm100PortUseTagTC_Type(Integer32):
    """Custom type sfbrm100PortUseTagTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortUseTagTC_Type.__name__ = "Integer32"
_Sfbrm100PortUseTagTC_Object = MibTableColumn
sfbrm100PortUseTagTC = _Sfbrm100PortUseTagTC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 32),
    _Sfbrm100PortUseTagTC_Type()
)
sfbrm100PortUseTagTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortUseTagTC.setStatus("mandatory")


class _Sfbrm100PortUseBothTC_Type(Integer32):
    """Custom type sfbrm100PortUseBothTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useIP", 1),
          ("useTag", 2))
    )


_Sfbrm100PortUseBothTC_Type.__name__ = "Integer32"
_Sfbrm100PortUseBothTC_Object = MibTableColumn
sfbrm100PortUseBothTC = _Sfbrm100PortUseBothTC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 33),
    _Sfbrm100PortUseBothTC_Type()
)
sfbrm100PortUseBothTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortUseBothTC.setStatus("mandatory")


class _Sfbrm100PortVLANTunnel_Type(Integer32):
    """Custom type sfbrm100PortVLANTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortVLANTunnel_Type.__name__ = "Integer32"
_Sfbrm100PortVLANTunnel_Object = MibTableColumn
sfbrm100PortVLANTunnel = _Sfbrm100PortVLANTunnel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 34),
    _Sfbrm100PortVLANTunnel_Type()
)
sfbrm100PortVLANTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortVLANTunnel.setStatus("mandatory")


class _Sfbrm100PortFwdUnknown_Type(Integer32):
    """Custom type sfbrm100PortFwdUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortFwdUnknown_Type.__name__ = "Integer32"
_Sfbrm100PortFwdUnknown_Object = MibTableColumn
sfbrm100PortFwdUnknown = _Sfbrm100PortFwdUnknown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 35),
    _Sfbrm100PortFwdUnknown_Type()
)
sfbrm100PortFwdUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortFwdUnknown.setStatus("mandatory")


class _Sfbrm100PortDefForward_Type(Integer32):
    """Custom type sfbrm100PortDefForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortDefForward_Type.__name__ = "Integer32"
_Sfbrm100PortDefForward_Object = MibTableColumn
sfbrm100PortDefForward = _Sfbrm100PortDefForward_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 36),
    _Sfbrm100PortDefForward_Type()
)
sfbrm100PortDefForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDefForward.setStatus("mandatory")


class _Sfbrm100PortAdminState_Type(Integer32):
    """Custom type sfbrm100PortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortAdminState_Type.__name__ = "Integer32"
_Sfbrm100PortAdminState_Object = MibTableColumn
sfbrm100PortAdminState = _Sfbrm100PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 37),
    _Sfbrm100PortAdminState_Type()
)
sfbrm100PortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAdminState.setStatus("mandatory")


class _Sfbrm100PortVTUPriOverride_Type(Integer32):
    """Custom type sfbrm100PortVTUPriOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortVTUPriOverride_Type.__name__ = "Integer32"
_Sfbrm100PortVTUPriOverride_Object = MibTableColumn
sfbrm100PortVTUPriOverride = _Sfbrm100PortVTUPriOverride_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 38),
    _Sfbrm100PortVTUPriOverride_Type()
)
sfbrm100PortVTUPriOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortVTUPriOverride.setStatus("mandatory")


class _Sfbrm100PortSAPriOverride_Type(Integer32):
    """Custom type sfbrm100PortSAPriOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortSAPriOverride_Type.__name__ = "Integer32"
_Sfbrm100PortSAPriOverride_Object = MibTableColumn
sfbrm100PortSAPriOverride = _Sfbrm100PortSAPriOverride_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 39),
    _Sfbrm100PortSAPriOverride_Type()
)
sfbrm100PortSAPriOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortSAPriOverride.setStatus("mandatory")


class _Sfbrm100PortDAPriOverride_Type(Integer32):
    """Custom type sfbrm100PortDAPriOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortDAPriOverride_Type.__name__ = "Integer32"
_Sfbrm100PortDAPriOverride_Object = MibTableColumn
sfbrm100PortDAPriOverride = _Sfbrm100PortDAPriOverride_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 40),
    _Sfbrm100PortDAPriOverride_Type()
)
sfbrm100PortDAPriOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDAPriOverride.setStatus("mandatory")


class _Sfbrm100PortVLANStatus_Type(Integer32):
    """Custom type sfbrm100PortVLANStatus based on Integer32"""
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
        *(("check", 3),
          ("fallback", 2),
          ("secure", 4),
          ("vlanDisabled", 1))
    )


_Sfbrm100PortVLANStatus_Type.__name__ = "Integer32"
_Sfbrm100PortVLANStatus_Object = MibTableColumn
sfbrm100PortVLANStatus = _Sfbrm100PortVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 41),
    _Sfbrm100PortVLANStatus_Type()
)
sfbrm100PortVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortVLANStatus.setStatus("mandatory")


class _Sfbrm100PortDiscardTagged_Type(Integer32):
    """Custom type sfbrm100PortDiscardTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortDiscardTagged_Type.__name__ = "Integer32"
_Sfbrm100PortDiscardTagged_Object = MibTableColumn
sfbrm100PortDiscardTagged = _Sfbrm100PortDiscardTagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 42),
    _Sfbrm100PortDiscardTagged_Type()
)
sfbrm100PortDiscardTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDiscardTagged.setStatus("mandatory")


class _Sfbrm100PortDiscardUntagged_Type(Integer32):
    """Custom type sfbrm100PortDiscardUntagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortDiscardUntagged_Type.__name__ = "Integer32"
_Sfbrm100PortDiscardUntagged_Object = MibTableColumn
sfbrm100PortDiscardUntagged = _Sfbrm100PortDiscardUntagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 43),
    _Sfbrm100PortDiscardUntagged_Type()
)
sfbrm100PortDiscardUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDiscardUntagged.setStatus("mandatory")


class _Sfbrm100PortEgressMonitor_Type(Integer32):
    """Custom type sfbrm100PortEgressMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortEgressMonitor_Type.__name__ = "Integer32"
_Sfbrm100PortEgressMonitor_Object = MibTableColumn
sfbrm100PortEgressMonitor = _Sfbrm100PortEgressMonitor_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 44),
    _Sfbrm100PortEgressMonitor_Type()
)
sfbrm100PortEgressMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortEgressMonitor.setStatus("mandatory")


class _Sfbrm100PortIngressMonitor_Type(Integer32):
    """Custom type sfbrm100PortIngressMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortIngressMonitor_Type.__name__ = "Integer32"
_Sfbrm100PortIngressMonitor_Object = MibTableColumn
sfbrm100PortIngressMonitor = _Sfbrm100PortIngressMonitor_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 45),
    _Sfbrm100PortIngressMonitor_Type()
)
sfbrm100PortIngressMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIngressMonitor.setStatus("mandatory")


class _Sfbrm100PortPri3IngressRateCtrl_Type(Integer32):
    """Custom type sfbrm100PortPri3IngressRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sameAsPri2", 1),
          ("twiceAsPri2", 2))
    )


_Sfbrm100PortPri3IngressRateCtrl_Type.__name__ = "Integer32"
_Sfbrm100PortPri3IngressRateCtrl_Object = MibTableColumn
sfbrm100PortPri3IngressRateCtrl = _Sfbrm100PortPri3IngressRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 46),
    _Sfbrm100PortPri3IngressRateCtrl_Type()
)
sfbrm100PortPri3IngressRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortPri3IngressRateCtrl.setStatus("mandatory")


class _Sfbrm100PortPri2IngressRateCtrl_Type(Integer32):
    """Custom type sfbrm100PortPri2IngressRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sameAsPri1", 1),
          ("twiceAsPri1", 2))
    )


_Sfbrm100PortPri2IngressRateCtrl_Type.__name__ = "Integer32"
_Sfbrm100PortPri2IngressRateCtrl_Object = MibTableColumn
sfbrm100PortPri2IngressRateCtrl = _Sfbrm100PortPri2IngressRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 47),
    _Sfbrm100PortPri2IngressRateCtrl_Type()
)
sfbrm100PortPri2IngressRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortPri2IngressRateCtrl.setStatus("mandatory")


class _Sfbrm100PortPri1IngressRateCtrl_Type(Integer32):
    """Custom type sfbrm100PortPri1IngressRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sameAsPri0", 1),
          ("twiceAsPri0", 2))
    )


_Sfbrm100PortPri1IngressRateCtrl_Type.__name__ = "Integer32"
_Sfbrm100PortPri1IngressRateCtrl_Object = MibTableColumn
sfbrm100PortPri1IngressRateCtrl = _Sfbrm100PortPri1IngressRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 48),
    _Sfbrm100PortPri1IngressRateCtrl_Type()
)
sfbrm100PortPri1IngressRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortPri1IngressRateCtrl.setStatus("mandatory")


class _Sfbrm100PortPri0IngressRate_Type(Integer32):
    """Custom type sfbrm100PortPri0IngressRate based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("rate1-2M", 14),
          ("rate1-5M", 15),
          ("rate10M", 21),
          ("rate128K", 4),
          ("rate128M", 27),
          ("rate160K", 5),
          ("rate192K", 6),
          ("rate1M", 13),
          ("rate20M", 22),
          ("rate224K", 7),
          ("rate256K", 8),
          ("rate256M", 28),
          ("rate2M", 16),
          ("rate30M", 23),
          ("rate320K", 9),
          ("rate384K", 10),
          ("rate3M", 17),
          ("rate40M", 24),
          ("rate4M", 18),
          ("rate512K", 11),
          ("rate5M", 19),
          ("rate60M", 25),
          ("rate64K", 2),
          ("rate768K", 12),
          ("rate80M", 26),
          ("rate8M", 20),
          ("rate96K", 3))
    )


_Sfbrm100PortPri0IngressRate_Type.__name__ = "Integer32"
_Sfbrm100PortPri0IngressRate_Object = MibTableColumn
sfbrm100PortPri0IngressRate = _Sfbrm100PortPri0IngressRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 49),
    _Sfbrm100PortPri0IngressRate_Type()
)
sfbrm100PortPri0IngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortPri0IngressRate.setStatus("mandatory")


class _Sfbrm100PortIngressLimitMode_Type(Integer32):
    """Custom type sfbrm100PortIngressLimitMode based on Integer32"""
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
        *(("all", 1),
          ("bCastMCastFloodedUCast", 2),
          ("bCastMCastOnly", 3),
          ("bCastOnly", 4))
    )


_Sfbrm100PortIngressLimitMode_Type.__name__ = "Integer32"
_Sfbrm100PortIngressLimitMode_Object = MibTableColumn
sfbrm100PortIngressLimitMode = _Sfbrm100PortIngressLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 50),
    _Sfbrm100PortIngressLimitMode_Type()
)
sfbrm100PortIngressLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIngressLimitMode.setStatus("mandatory")


class _Sfbrm100PortEgressRate_Type(Integer32):
    """Custom type sfbrm100PortEgressRate based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("rate1-2M", 14),
          ("rate1-5M", 15),
          ("rate10M", 21),
          ("rate128K", 4),
          ("rate128M", 27),
          ("rate160K", 5),
          ("rate192K", 6),
          ("rate1M", 13),
          ("rate20M", 22),
          ("rate224K", 7),
          ("rate256K", 8),
          ("rate256M", 28),
          ("rate2M", 16),
          ("rate30M", 23),
          ("rate320K", 9),
          ("rate384K", 10),
          ("rate3M", 17),
          ("rate40M", 24),
          ("rate4M", 18),
          ("rate512K", 11),
          ("rate5M", 19),
          ("rate60M", 25),
          ("rate64K", 2),
          ("rate768K", 12),
          ("rate80M", 26),
          ("rate8M", 20),
          ("rate96K", 3))
    )


_Sfbrm100PortEgressRate_Type.__name__ = "Integer32"
_Sfbrm100PortEgressRate_Object = MibTableColumn
sfbrm100PortEgressRate = _Sfbrm100PortEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 51),
    _Sfbrm100PortEgressRate_Type()
)
sfbrm100PortEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortEgressRate.setStatus("mandatory")
_Sfbrm100PortDefaultPriority_Type = Integer32
_Sfbrm100PortDefaultPriority_Object = MibTableColumn
sfbrm100PortDefaultPriority = _Sfbrm100PortDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 52),
    _Sfbrm100PortDefaultPriority_Type()
)
sfbrm100PortDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDefaultPriority.setStatus("mandatory")


class _Sfbrm100PortForceDefVLANId_Type(Integer32):
    """Custom type sfbrm100PortForceDefVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortForceDefVLANId_Type.__name__ = "Integer32"
_Sfbrm100PortForceDefVLANId_Object = MibTableColumn
sfbrm100PortForceDefVLANId = _Sfbrm100PortForceDefVLANId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 53),
    _Sfbrm100PortForceDefVLANId_Type()
)
sfbrm100PortForceDefVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortForceDefVLANId.setStatus("mandatory")
_Sfbrm100PortDefaultVLANId_Type = Integer32
_Sfbrm100PortDefaultVLANId_Object = MibTableColumn
sfbrm100PortDefaultVLANId = _Sfbrm100PortDefaultVLANId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 54),
    _Sfbrm100PortDefaultVLANId_Type()
)
sfbrm100PortDefaultVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortDefaultVLANId.setStatus("mandatory")
_Sfbrm100PortBasedVLANTbl_Type = Integer32
_Sfbrm100PortBasedVLANTbl_Object = MibTableColumn
sfbrm100PortBasedVLANTbl = _Sfbrm100PortBasedVLANTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 55),
    _Sfbrm100PortBasedVLANTbl_Type()
)
sfbrm100PortBasedVLANTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortBasedVLANTbl.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap0_Type = Integer32
_Sfbrm100PortIEEEPriRemap0_Object = MibTableColumn
sfbrm100PortIEEEPriRemap0 = _Sfbrm100PortIEEEPriRemap0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 56),
    _Sfbrm100PortIEEEPriRemap0_Type()
)
sfbrm100PortIEEEPriRemap0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap0.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap1_Type = Integer32
_Sfbrm100PortIEEEPriRemap1_Object = MibTableColumn
sfbrm100PortIEEEPriRemap1 = _Sfbrm100PortIEEEPriRemap1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 57),
    _Sfbrm100PortIEEEPriRemap1_Type()
)
sfbrm100PortIEEEPriRemap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap1.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap2_Type = Integer32
_Sfbrm100PortIEEEPriRemap2_Object = MibTableColumn
sfbrm100PortIEEEPriRemap2 = _Sfbrm100PortIEEEPriRemap2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 58),
    _Sfbrm100PortIEEEPriRemap2_Type()
)
sfbrm100PortIEEEPriRemap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap2.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap3_Type = Integer32
_Sfbrm100PortIEEEPriRemap3_Object = MibTableColumn
sfbrm100PortIEEEPriRemap3 = _Sfbrm100PortIEEEPriRemap3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 59),
    _Sfbrm100PortIEEEPriRemap3_Type()
)
sfbrm100PortIEEEPriRemap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap3.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap4_Type = Integer32
_Sfbrm100PortIEEEPriRemap4_Object = MibTableColumn
sfbrm100PortIEEEPriRemap4 = _Sfbrm100PortIEEEPriRemap4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 60),
    _Sfbrm100PortIEEEPriRemap4_Type()
)
sfbrm100PortIEEEPriRemap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap4.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap5_Type = Integer32
_Sfbrm100PortIEEEPriRemap5_Object = MibTableColumn
sfbrm100PortIEEEPriRemap5 = _Sfbrm100PortIEEEPriRemap5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 61),
    _Sfbrm100PortIEEEPriRemap5_Type()
)
sfbrm100PortIEEEPriRemap5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap5.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap6_Type = Integer32
_Sfbrm100PortIEEEPriRemap6_Object = MibTableColumn
sfbrm100PortIEEEPriRemap6 = _Sfbrm100PortIEEEPriRemap6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 62),
    _Sfbrm100PortIEEEPriRemap6_Type()
)
sfbrm100PortIEEEPriRemap6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap6.setStatus("mandatory")
_Sfbrm100PortIEEEPriRemap7_Type = Integer32
_Sfbrm100PortIEEEPriRemap7_Object = MibTableColumn
sfbrm100PortIEEEPriRemap7 = _Sfbrm100PortIEEEPriRemap7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 63),
    _Sfbrm100PortIEEEPriRemap7_Type()
)
sfbrm100PortIEEEPriRemap7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIEEEPriRemap7.setStatus("mandatory")


class _Sfbrm100PortVCTest_Type(Integer32):
    """Custom type sfbrm100PortVCTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("perform", 1))
    )


_Sfbrm100PortVCTest_Type.__name__ = "Integer32"
_Sfbrm100PortVCTest_Object = MibTableColumn
sfbrm100PortVCTest = _Sfbrm100PortVCTest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 64),
    _Sfbrm100PortVCTest_Type()
)
sfbrm100PortVCTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortVCTest.setStatus("mandatory")


class _Sfbrm100PortVCTxMDI0Status_Type(Integer32):
    """Custom type sfbrm100PortVCTxMDI0Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 5),
          ("impedanceMismatch", 2),
          ("normal", 1),
          ("notApplicable", 6),
          ("openInCable", 4),
          ("shortInCable", 3))
    )


_Sfbrm100PortVCTxMDI0Status_Type.__name__ = "Integer32"
_Sfbrm100PortVCTxMDI0Status_Object = MibTableColumn
sfbrm100PortVCTxMDI0Status = _Sfbrm100PortVCTxMDI0Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 65),
    _Sfbrm100PortVCTxMDI0Status_Type()
)
sfbrm100PortVCTxMDI0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortVCTxMDI0Status.setStatus("mandatory")


class _Sfbrm100PortTxMDI0Dist_Type(Integer32):
    """Custom type sfbrm100PortTxMDI0Dist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("between110m140m", 4),
          ("between50m80m", 2),
          ("between80m110m", 3),
          ("lessThan50m", 1),
          ("morethan140m", 5),
          ("notApplicable", 6))
    )


_Sfbrm100PortTxMDI0Dist_Type.__name__ = "Integer32"
_Sfbrm100PortTxMDI0Dist_Object = MibTableColumn
sfbrm100PortTxMDI0Dist = _Sfbrm100PortTxMDI0Dist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 66),
    _Sfbrm100PortTxMDI0Dist_Type()
)
sfbrm100PortTxMDI0Dist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortTxMDI0Dist.setStatus("mandatory")


class _Sfbrm100PortVCRxMDI1Status_Type(Integer32):
    """Custom type sfbrm100PortVCRxMDI1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 5),
          ("impedanceMismatch", 2),
          ("normal", 1),
          ("notApplicable", 6),
          ("openInCable", 4),
          ("shortInCable", 3))
    )


_Sfbrm100PortVCRxMDI1Status_Type.__name__ = "Integer32"
_Sfbrm100PortVCRxMDI1Status_Object = MibTableColumn
sfbrm100PortVCRxMDI1Status = _Sfbrm100PortVCRxMDI1Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 67),
    _Sfbrm100PortVCRxMDI1Status_Type()
)
sfbrm100PortVCRxMDI1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortVCRxMDI1Status.setStatus("mandatory")


class _Sfbrm100PortRxMDI1Dist_Type(Integer32):
    """Custom type sfbrm100PortRxMDI1Dist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("between110m140m", 4),
          ("between50m80m", 2),
          ("between80m110m", 3),
          ("lessThan50m", 1),
          ("morethan140m", 5),
          ("notApplicable", 6))
    )


_Sfbrm100PortRxMDI1Dist_Type.__name__ = "Integer32"
_Sfbrm100PortRxMDI1Dist_Object = MibTableColumn
sfbrm100PortRxMDI1Dist = _Sfbrm100PortRxMDI1Dist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 68),
    _Sfbrm100PortRxMDI1Dist_Type()
)
sfbrm100PortRxMDI1Dist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortRxMDI1Dist.setStatus("mandatory")


class _Sfbrm100PortVCMDI2Status_Type(Integer32):
    """Custom type sfbrm100PortVCMDI2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 5),
          ("impedanceMismatch", 2),
          ("normal", 1),
          ("notApplicable", 6),
          ("openInCable", 4),
          ("shortInCable", 3))
    )


_Sfbrm100PortVCMDI2Status_Type.__name__ = "Integer32"
_Sfbrm100PortVCMDI2Status_Object = MibTableColumn
sfbrm100PortVCMDI2Status = _Sfbrm100PortVCMDI2Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 69),
    _Sfbrm100PortVCMDI2Status_Type()
)
sfbrm100PortVCMDI2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortVCMDI2Status.setStatus("mandatory")


class _Sfbrm100PortMDI2Dist_Type(Integer32):
    """Custom type sfbrm100PortMDI2Dist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("between110m140m", 4),
          ("between50m80m", 2),
          ("between80m110m", 3),
          ("lessThan50m", 1),
          ("morethan140m", 5),
          ("notApplicable", 6))
    )


_Sfbrm100PortMDI2Dist_Type.__name__ = "Integer32"
_Sfbrm100PortMDI2Dist_Object = MibTableColumn
sfbrm100PortMDI2Dist = _Sfbrm100PortMDI2Dist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 70),
    _Sfbrm100PortMDI2Dist_Type()
)
sfbrm100PortMDI2Dist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortMDI2Dist.setStatus("mandatory")


class _Sfbrm100PortVCMDI3Status_Type(Integer32):
    """Custom type sfbrm100PortVCMDI3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 5),
          ("impedanceMismatch", 2),
          ("normal", 1),
          ("notApplicable", 6),
          ("openInCable", 4),
          ("shortInCable", 3))
    )


_Sfbrm100PortVCMDI3Status_Type.__name__ = "Integer32"
_Sfbrm100PortVCMDI3Status_Object = MibTableColumn
sfbrm100PortVCMDI3Status = _Sfbrm100PortVCMDI3Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 71),
    _Sfbrm100PortVCMDI3Status_Type()
)
sfbrm100PortVCMDI3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortVCMDI3Status.setStatus("mandatory")


class _Sfbrm100PortMDI3Dist_Type(Integer32):
    """Custom type sfbrm100PortMDI3Dist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("between110m140m", 4),
          ("between50m80m", 2),
          ("between80m110m", 3),
          ("lessThan50m", 1),
          ("morethan140m", 5),
          ("notApplicable", 6))
    )


_Sfbrm100PortMDI3Dist_Type.__name__ = "Integer32"
_Sfbrm100PortMDI3Dist_Object = MibTableColumn
sfbrm100PortMDI3Dist = _Sfbrm100PortMDI3Dist_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 72),
    _Sfbrm100PortMDI3Dist_Type()
)
sfbrm100PortMDI3Dist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortMDI3Dist.setStatus("mandatory")


class _Sfbrm100PortResetCounters_Type(Integer32):
    """Custom type sfbrm100PortResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 2),
          ("reset", 1))
    )


_Sfbrm100PortResetCounters_Type.__name__ = "Integer32"
_Sfbrm100PortResetCounters_Object = MibTableColumn
sfbrm100PortResetCounters = _Sfbrm100PortResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 73),
    _Sfbrm100PortResetCounters_Type()
)
sfbrm100PortResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortResetCounters.setStatus("mandatory")


class _Sfbrm100PortIPTrafficAccess_Type(Integer32):
    """Custom type sfbrm100PortIPTrafficAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortIPTrafficAccess_Type.__name__ = "Integer32"
_Sfbrm100PortIPTrafficAccess_Object = MibTableColumn
sfbrm100PortIPTrafficAccess = _Sfbrm100PortIPTrafficAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 74),
    _Sfbrm100PortIPTrafficAccess_Type()
)
sfbrm100PortIPTrafficAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIPTrafficAccess.setStatus("mandatory")


class _Sfbrm100PortResetOAMCounters_Type(Integer32):
    """Custom type sfbrm100PortResetOAMCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortResetOAMCounters_Type.__name__ = "Integer32"
_Sfbrm100PortResetOAMCounters_Object = MibTableColumn
sfbrm100PortResetOAMCounters = _Sfbrm100PortResetOAMCounters_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 75),
    _Sfbrm100PortResetOAMCounters_Type()
)
sfbrm100PortResetOAMCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortResetOAMCounters.setStatus("mandatory")


class _Sfbrm100PortForceAutoUpgrade_Type(Integer32):
    """Custom type sfbrm100PortForceAutoUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sfbrm100PortForceAutoUpgrade_Type.__name__ = "Integer32"
_Sfbrm100PortForceAutoUpgrade_Object = MibTableColumn
sfbrm100PortForceAutoUpgrade = _Sfbrm100PortForceAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 76),
    _Sfbrm100PortForceAutoUpgrade_Type()
)
sfbrm100PortForceAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortForceAutoUpgrade.setStatus("mandatory")


class _Sfbrm100PortModeType_Type(Integer32):
    """Custom type sfbrm100PortModeType based on Integer32"""
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
        *(("mode1000BaseX", 2),
          ("mode100BaseFX", 4),
          ("mode10or100BaseT", 3),
          ("mode10or100or1000BaseT", 1))
    )


_Sfbrm100PortModeType_Type.__name__ = "Integer32"
_Sfbrm100PortModeType_Object = MibTableColumn
sfbrm100PortModeType = _Sfbrm100PortModeType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 77),
    _Sfbrm100PortModeType_Type()
)
sfbrm100PortModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortModeType.setStatus("mandatory")


class _Sfbrm100PortOAMMode_Type(Integer32):
    """Custom type sfbrm100PortOAMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_Sfbrm100PortOAMMode_Type.__name__ = "Integer32"
_Sfbrm100PortOAMMode_Object = MibTableColumn
sfbrm100PortOAMMode = _Sfbrm100PortOAMMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 78),
    _Sfbrm100PortOAMMode_Type()
)
sfbrm100PortOAMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortOAMMode.setStatus("mandatory")
_Sfbrm100PortPhyNumber_Type = Integer32
_Sfbrm100PortPhyNumber_Object = MibTableColumn
sfbrm100PortPhyNumber = _Sfbrm100PortPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 79),
    _Sfbrm100PortPhyNumber_Type()
)
sfbrm100PortPhyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortPhyNumber.setStatus("mandatory")


class _Sfbrm100PortIngressRateLimit2_Type(Integer32):
    """Custom type sfbrm100PortIngressRateLimit2 based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("rate100M", 24),
          ("rate10M", 16),
          ("rate128K", 3),
          ("rate192K", 4),
          ("rate1M", 10),
          ("rate200M", 25),
          ("rate20M", 17),
          ("rate256K", 5),
          ("rate2M", 11),
          ("rate300M", 26),
          ("rate30M", 18),
          ("rate320K", 6),
          ("rate384K", 7),
          ("rate3M", 12),
          ("rate400M", 27),
          ("rate40M", 19),
          ("rate4M", 13),
          ("rate500M", 28),
          ("rate50M", 20),
          ("rate512K", 8),
          ("rate600M", 29),
          ("rate60M", 21),
          ("rate64K", 2),
          ("rate6M", 14),
          ("rate700M", 30),
          ("rate70M", 22),
          ("rate768K", 9),
          ("rate800M", 31),
          ("rate80M", 23),
          ("rate8M", 15),
          ("rate900M", 32))
    )


_Sfbrm100PortIngressRateLimit2_Type.__name__ = "Integer32"
_Sfbrm100PortIngressRateLimit2_Object = MibTableColumn
sfbrm100PortIngressRateLimit2 = _Sfbrm100PortIngressRateLimit2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 80),
    _Sfbrm100PortIngressRateLimit2_Type()
)
sfbrm100PortIngressRateLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortIngressRateLimit2.setStatus("mandatory")


class _Sfbrm100PortEgressRateLimit2_Type(Integer32):
    """Custom type sfbrm100PortEgressRateLimit2 based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("rate100M", 24),
          ("rate10M", 16),
          ("rate128K", 3),
          ("rate192K", 4),
          ("rate1M", 10),
          ("rate200M", 25),
          ("rate20M", 17),
          ("rate256K", 5),
          ("rate2M", 11),
          ("rate300M", 26),
          ("rate30M", 18),
          ("rate320K", 6),
          ("rate384K", 7),
          ("rate3M", 12),
          ("rate400M", 27),
          ("rate40M", 19),
          ("rate4M", 13),
          ("rate500M", 28),
          ("rate50M", 20),
          ("rate512K", 8),
          ("rate600M", 29),
          ("rate60M", 21),
          ("rate64K", 2),
          ("rate6M", 14),
          ("rate700M", 30),
          ("rate70M", 22),
          ("rate768K", 9),
          ("rate800M", 31),
          ("rate80M", 23),
          ("rate8M", 15),
          ("rate900M", 32))
    )


_Sfbrm100PortEgressRateLimit2_Type.__name__ = "Integer32"
_Sfbrm100PortEgressRateLimit2_Object = MibTableColumn
sfbrm100PortEgressRateLimit2 = _Sfbrm100PortEgressRateLimit2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 1, 1, 81),
    _Sfbrm100PortEgressRateLimit2_Type()
)
sfbrm100PortEgressRateLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortEgressRateLimit2.setStatus("mandatory")
_Sfbrm100PortStatsTable_Object = MibTable
sfbrm100PortStatsTable = _Sfbrm100PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sfbrm100PortStatsTable.setStatus("mandatory")
_Sfbrm100PortStatsEntry_Object = MibTableRow
sfbrm100PortStatsEntry = _Sfbrm100PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1)
)
sfbrm100PortStatsEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100PortLocStatsIndex"),
    (0, "TNI-MIB", "sfbrm100PortRmtStatsIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100PortStatsEntry.setStatus("mandatory")
_Sfbrm100PortLocStatsIndex_Type = Integer32
_Sfbrm100PortLocStatsIndex_Object = MibTableColumn
sfbrm100PortLocStatsIndex = _Sfbrm100PortLocStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 1),
    _Sfbrm100PortLocStatsIndex_Type()
)
sfbrm100PortLocStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortLocStatsIndex.setStatus("mandatory")
_Sfbrm100PortRmtStatsIndex_Type = Integer32
_Sfbrm100PortRmtStatsIndex_Object = MibTableColumn
sfbrm100PortRmtStatsIndex = _Sfbrm100PortRmtStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 2),
    _Sfbrm100PortRmtStatsIndex_Type()
)
sfbrm100PortRmtStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortRmtStatsIndex.setStatus("mandatory")
_Sfbrm100PortInGoodOctetsLo_Type = Integer32
_Sfbrm100PortInGoodOctetsLo_Object = MibTableColumn
sfbrm100PortInGoodOctetsLo = _Sfbrm100PortInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 3),
    _Sfbrm100PortInGoodOctetsLo_Type()
)
sfbrm100PortInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInGoodOctetsLo.setStatus("mandatory")
_Sfbrm100PortInGoodOctetsHi_Type = Integer32
_Sfbrm100PortInGoodOctetsHi_Object = MibTableColumn
sfbrm100PortInGoodOctetsHi = _Sfbrm100PortInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 4),
    _Sfbrm100PortInGoodOctetsHi_Type()
)
sfbrm100PortInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInGoodOctetsHi.setStatus("mandatory")
_Sfbrm100PortInBadOctets_Type = Integer32
_Sfbrm100PortInBadOctets_Object = MibTableColumn
sfbrm100PortInBadOctets = _Sfbrm100PortInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 5),
    _Sfbrm100PortInBadOctets_Type()
)
sfbrm100PortInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInBadOctets.setStatus("mandatory")
_Sfbrm100PortInUnicasts_Type = Integer32
_Sfbrm100PortInUnicasts_Object = MibTableColumn
sfbrm100PortInUnicasts = _Sfbrm100PortInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 6),
    _Sfbrm100PortInUnicasts_Type()
)
sfbrm100PortInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInUnicasts.setStatus("mandatory")
_Sfbrm100PortInBroadcasts_Type = Integer32
_Sfbrm100PortInBroadcasts_Object = MibTableColumn
sfbrm100PortInBroadcasts = _Sfbrm100PortInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 7),
    _Sfbrm100PortInBroadcasts_Type()
)
sfbrm100PortInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInBroadcasts.setStatus("mandatory")
_Sfbrm100PortInMulticasts_Type = Integer32
_Sfbrm100PortInMulticasts_Object = MibTableColumn
sfbrm100PortInMulticasts = _Sfbrm100PortInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 8),
    _Sfbrm100PortInMulticasts_Type()
)
sfbrm100PortInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInMulticasts.setStatus("mandatory")
_Sfbrm100PortInPause_Type = Integer32
_Sfbrm100PortInPause_Object = MibTableColumn
sfbrm100PortInPause = _Sfbrm100PortInPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 9),
    _Sfbrm100PortInPause_Type()
)
sfbrm100PortInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInPause.setStatus("mandatory")
_Sfbrm100PortInUndersize_Type = Integer32
_Sfbrm100PortInUndersize_Object = MibTableColumn
sfbrm100PortInUndersize = _Sfbrm100PortInUndersize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 10),
    _Sfbrm100PortInUndersize_Type()
)
sfbrm100PortInUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInUndersize.setStatus("mandatory")
_Sfbrm100PortInFragments_Type = Integer32
_Sfbrm100PortInFragments_Object = MibTableColumn
sfbrm100PortInFragments = _Sfbrm100PortInFragments_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 11),
    _Sfbrm100PortInFragments_Type()
)
sfbrm100PortInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInFragments.setStatus("mandatory")
_Sfbrm100PortInOversize_Type = Integer32
_Sfbrm100PortInOversize_Object = MibTableColumn
sfbrm100PortInOversize = _Sfbrm100PortInOversize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 12),
    _Sfbrm100PortInOversize_Type()
)
sfbrm100PortInOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInOversize.setStatus("mandatory")
_Sfbrm100PortInJabber_Type = Integer32
_Sfbrm100PortInJabber_Object = MibTableColumn
sfbrm100PortInJabber = _Sfbrm100PortInJabber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 13),
    _Sfbrm100PortInJabber_Type()
)
sfbrm100PortInJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInJabber.setStatus("mandatory")
_Sfbrm100PortInRxErr_Type = Integer32
_Sfbrm100PortInRxErr_Object = MibTableColumn
sfbrm100PortInRxErr = _Sfbrm100PortInRxErr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 14),
    _Sfbrm100PortInRxErr_Type()
)
sfbrm100PortInRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInRxErr.setStatus("mandatory")
_Sfbrm100PortInFCSErr_Type = Integer32
_Sfbrm100PortInFCSErr_Object = MibTableColumn
sfbrm100PortInFCSErr = _Sfbrm100PortInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 15),
    _Sfbrm100PortInFCSErr_Type()
)
sfbrm100PortInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInFCSErr.setStatus("mandatory")
_Sfbrm100PortIn64Octets_Type = Integer32
_Sfbrm100PortIn64Octets_Object = MibTableColumn
sfbrm100PortIn64Octets = _Sfbrm100PortIn64Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 16),
    _Sfbrm100PortIn64Octets_Type()
)
sfbrm100PortIn64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortIn64Octets.setStatus("mandatory")
_Sfbrm100PortIn65to127Octets_Type = Integer32
_Sfbrm100PortIn65to127Octets_Object = MibTableColumn
sfbrm100PortIn65to127Octets = _Sfbrm100PortIn65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 17),
    _Sfbrm100PortIn65to127Octets_Type()
)
sfbrm100PortIn65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortIn65to127Octets.setStatus("mandatory")
_Sfbrm100PortIn128to255Octets_Type = Integer32
_Sfbrm100PortIn128to255Octets_Object = MibTableColumn
sfbrm100PortIn128to255Octets = _Sfbrm100PortIn128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 18),
    _Sfbrm100PortIn128to255Octets_Type()
)
sfbrm100PortIn128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortIn128to255Octets.setStatus("mandatory")
_Sfbrm100PortIn256to511Octets_Type = Integer32
_Sfbrm100PortIn256to511Octets_Object = MibTableColumn
sfbrm100PortIn256to511Octets = _Sfbrm100PortIn256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 19),
    _Sfbrm100PortIn256to511Octets_Type()
)
sfbrm100PortIn256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortIn256to511Octets.setStatus("mandatory")
_Sfbrm100PortIn512to1023Octets_Type = Integer32
_Sfbrm100PortIn512to1023Octets_Object = MibTableColumn
sfbrm100PortIn512to1023Octets = _Sfbrm100PortIn512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 20),
    _Sfbrm100PortIn512to1023Octets_Type()
)
sfbrm100PortIn512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortIn512to1023Octets.setStatus("mandatory")
_Sfbrm100PortIn1024toMaxOctets_Type = Integer32
_Sfbrm100PortIn1024toMaxOctets_Object = MibTableColumn
sfbrm100PortIn1024toMaxOctets = _Sfbrm100PortIn1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 21),
    _Sfbrm100PortIn1024toMaxOctets_Type()
)
sfbrm100PortIn1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortIn1024toMaxOctets.setStatus("mandatory")
_Sfbrm100PortOutOctetsLo_Type = Integer32
_Sfbrm100PortOutOctetsLo_Object = MibTableColumn
sfbrm100PortOutOctetsLo = _Sfbrm100PortOutOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 22),
    _Sfbrm100PortOutOctetsLo_Type()
)
sfbrm100PortOutOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutOctetsLo.setStatus("mandatory")
_Sfbrm100PortOutOctetsHi_Type = Integer32
_Sfbrm100PortOutOctetsHi_Object = MibTableColumn
sfbrm100PortOutOctetsHi = _Sfbrm100PortOutOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 23),
    _Sfbrm100PortOutOctetsHi_Type()
)
sfbrm100PortOutOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutOctetsHi.setStatus("mandatory")
_Sfbrm100PortOutUnicasts_Type = Integer32
_Sfbrm100PortOutUnicasts_Object = MibTableColumn
sfbrm100PortOutUnicasts = _Sfbrm100PortOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 24),
    _Sfbrm100PortOutUnicasts_Type()
)
sfbrm100PortOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutUnicasts.setStatus("mandatory")
_Sfbrm100PortOutBroadcasts_Type = Integer32
_Sfbrm100PortOutBroadcasts_Object = MibTableColumn
sfbrm100PortOutBroadcasts = _Sfbrm100PortOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 25),
    _Sfbrm100PortOutBroadcasts_Type()
)
sfbrm100PortOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutBroadcasts.setStatus("mandatory")
_Sfbrm100PortOutMulticasts_Type = Integer32
_Sfbrm100PortOutMulticasts_Object = MibTableColumn
sfbrm100PortOutMulticasts = _Sfbrm100PortOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 26),
    _Sfbrm100PortOutMulticasts_Type()
)
sfbrm100PortOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutMulticasts.setStatus("mandatory")
_Sfbrm100PortOutPause_Type = Integer32
_Sfbrm100PortOutPause_Object = MibTableColumn
sfbrm100PortOutPause = _Sfbrm100PortOutPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 27),
    _Sfbrm100PortOutPause_Type()
)
sfbrm100PortOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutPause.setStatus("mandatory")
_Sfbrm100PortOutDeferred_Type = Integer32
_Sfbrm100PortOutDeferred_Object = MibTableColumn
sfbrm100PortOutDeferred = _Sfbrm100PortOutDeferred_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 28),
    _Sfbrm100PortOutDeferred_Type()
)
sfbrm100PortOutDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutDeferred.setStatus("mandatory")
_Sfbrm100PortOutCollisions_Type = Integer32
_Sfbrm100PortOutCollisions_Object = MibTableColumn
sfbrm100PortOutCollisions = _Sfbrm100PortOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 29),
    _Sfbrm100PortOutCollisions_Type()
)
sfbrm100PortOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutCollisions.setStatus("mandatory")
_Sfbrm100PortOutSingle_Type = Integer32
_Sfbrm100PortOutSingle_Object = MibTableColumn
sfbrm100PortOutSingle = _Sfbrm100PortOutSingle_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 30),
    _Sfbrm100PortOutSingle_Type()
)
sfbrm100PortOutSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutSingle.setStatus("mandatory")
_Sfbrm100PortOutMultiple_Type = Integer32
_Sfbrm100PortOutMultiple_Object = MibTableColumn
sfbrm100PortOutMultiple = _Sfbrm100PortOutMultiple_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 31),
    _Sfbrm100PortOutMultiple_Type()
)
sfbrm100PortOutMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutMultiple.setStatus("mandatory")
_Sfbrm100PortOutExcessive_Type = Integer32
_Sfbrm100PortOutExcessive_Object = MibTableColumn
sfbrm100PortOutExcessive = _Sfbrm100PortOutExcessive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 32),
    _Sfbrm100PortOutExcessive_Type()
)
sfbrm100PortOutExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutExcessive.setStatus("mandatory")
_Sfbrm100PortOutLate_Type = Integer32
_Sfbrm100PortOutLate_Object = MibTableColumn
sfbrm100PortOutLate = _Sfbrm100PortOutLate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 33),
    _Sfbrm100PortOutLate_Type()
)
sfbrm100PortOutLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutLate.setStatus("mandatory")
_Sfbrm100PortOutFCSErr_Type = Integer32
_Sfbrm100PortOutFCSErr_Object = MibTableColumn
sfbrm100PortOutFCSErr = _Sfbrm100PortOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 34),
    _Sfbrm100PortOutFCSErr_Type()
)
sfbrm100PortOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutFCSErr.setStatus("mandatory")
_Sfbrm100PortInDiscard_Type = Integer32
_Sfbrm100PortInDiscard_Object = MibTableColumn
sfbrm100PortInDiscard = _Sfbrm100PortInDiscard_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 35),
    _Sfbrm100PortInDiscard_Type()
)
sfbrm100PortInDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInDiscard.setStatus("mandatory")
_Sfbrm100PortInFiltered_Type = Integer32
_Sfbrm100PortInFiltered_Object = MibTableColumn
sfbrm100PortInFiltered = _Sfbrm100PortInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 36),
    _Sfbrm100PortInFiltered_Type()
)
sfbrm100PortInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortInFiltered.setStatus("mandatory")
_Sfbrm100PortOutFiltered_Type = Integer32
_Sfbrm100PortOutFiltered_Object = MibTableColumn
sfbrm100PortOutFiltered = _Sfbrm100PortOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 2, 1, 37),
    _Sfbrm100PortOutFiltered_Type()
)
sfbrm100PortOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortOutFiltered.setStatus("mandatory")
_Sfbrm100DMITable_Object = MibTable
sfbrm100DMITable = _Sfbrm100DMITable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sfbrm100DMITable.setStatus("mandatory")
_Sfbrm100DMIEntry_Object = MibTableRow
sfbrm100DMIEntry = _Sfbrm100DMIEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1)
)
sfbrm100DMIEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100DMILocPortIndex"),
    (0, "TNI-MIB", "sfbrm100DMIRmtPortIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100DMIEntry.setStatus("mandatory")
_Sfbrm100DMILocPortIndex_Type = Integer32
_Sfbrm100DMILocPortIndex_Object = MibTableColumn
sfbrm100DMILocPortIndex = _Sfbrm100DMILocPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 1),
    _Sfbrm100DMILocPortIndex_Type()
)
sfbrm100DMILocPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILocPortIndex.setStatus("mandatory")
_Sfbrm100DMIRmtPortIndex_Type = Integer32
_Sfbrm100DMIRmtPortIndex_Object = MibTableColumn
sfbrm100DMIRmtPortIndex = _Sfbrm100DMIRmtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 2),
    _Sfbrm100DMIRmtPortIndex_Type()
)
sfbrm100DMIRmtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMIRmtPortIndex.setStatus("mandatory")
_Sfbrm100DMIRxPwrLvlPreset_Type = Integer32
_Sfbrm100DMIRxPwrLvlPreset_Object = MibTableColumn
sfbrm100DMIRxPwrLvlPreset = _Sfbrm100DMIRxPwrLvlPreset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 3),
    _Sfbrm100DMIRxPwrLvlPreset_Type()
)
sfbrm100DMIRxPwrLvlPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100DMIRxPwrLvlPreset.setStatus("mandatory")
_Sfbrm100DMIConnType_Type = CpsConnector
_Sfbrm100DMIConnType_Object = MibTableColumn
sfbrm100DMIConnType = _Sfbrm100DMIConnType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 4),
    _Sfbrm100DMIConnType_Type()
)
sfbrm100DMIConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMIConnType.setStatus("mandatory")
_Sfbrm100DMIBitRate_Type = Integer32
_Sfbrm100DMIBitRate_Object = MibTableColumn
sfbrm100DMIBitRate = _Sfbrm100DMIBitRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 5),
    _Sfbrm100DMIBitRate_Type()
)
sfbrm100DMIBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMIBitRate.setStatus("mandatory")
_Sfbrm100DMILenFor9x125umKM_Type = Integer32
_Sfbrm100DMILenFor9x125umKM_Object = MibTableColumn
sfbrm100DMILenFor9x125umKM = _Sfbrm100DMILenFor9x125umKM_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 6),
    _Sfbrm100DMILenFor9x125umKM_Type()
)
sfbrm100DMILenFor9x125umKM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILenFor9x125umKM.setStatus("mandatory")
_Sfbrm100DMILenFor9x125um100M_Type = Integer32
_Sfbrm100DMILenFor9x125um100M_Object = MibTableColumn
sfbrm100DMILenFor9x125um100M = _Sfbrm100DMILenFor9x125um100M_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 7),
    _Sfbrm100DMILenFor9x125um100M_Type()
)
sfbrm100DMILenFor9x125um100M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILenFor9x125um100M.setStatus("mandatory")
_Sfbrm100DMILenFor50x125um10M_Type = Integer32
_Sfbrm100DMILenFor50x125um10M_Object = MibTableColumn
sfbrm100DMILenFor50x125um10M = _Sfbrm100DMILenFor50x125um10M_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 8),
    _Sfbrm100DMILenFor50x125um10M_Type()
)
sfbrm100DMILenFor50x125um10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILenFor50x125um10M.setStatus("mandatory")
_Sfbrm100DMILenFor625x125um10M_Type = Integer32
_Sfbrm100DMILenFor625x125um10M_Object = MibTableColumn
sfbrm100DMILenFor625x125um10M = _Sfbrm100DMILenFor625x125um10M_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 9),
    _Sfbrm100DMILenFor625x125um10M_Type()
)
sfbrm100DMILenFor625x125um10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILenFor625x125um10M.setStatus("mandatory")
_Sfbrm100DMILenForCopper_Type = Integer32
_Sfbrm100DMILenForCopper_Object = MibTableColumn
sfbrm100DMILenForCopper = _Sfbrm100DMILenForCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 10),
    _Sfbrm100DMILenForCopper_Type()
)
sfbrm100DMILenForCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILenForCopper.setStatus("mandatory")
_Sfbrm100DMIId_Type = Integer32
_Sfbrm100DMIId_Object = MibTableColumn
sfbrm100DMIId = _Sfbrm100DMIId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 11),
    _Sfbrm100DMIId_Type()
)
sfbrm100DMIId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMIId.setStatus("mandatory")
_Sfbrm100DMILaserWavelength_Type = Integer32
_Sfbrm100DMILaserWavelength_Object = MibTableColumn
sfbrm100DMILaserWavelength = _Sfbrm100DMILaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 12),
    _Sfbrm100DMILaserWavelength_Type()
)
sfbrm100DMILaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMILaserWavelength.setStatus("mandatory")
_Sfbrm100DMITemperature_Type = Integer32
_Sfbrm100DMITemperature_Object = MibTableColumn
sfbrm100DMITemperature = _Sfbrm100DMITemperature_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 13),
    _Sfbrm100DMITemperature_Type()
)
sfbrm100DMITemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMITemperature.setStatus("mandatory")


class _Sfbrm100DMITempAlarm_Type(Integer32):
    """Custom type sfbrm100DMITempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 7),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Sfbrm100DMITempAlarm_Type.__name__ = "Integer32"
_Sfbrm100DMITempAlarm_Object = MibTableColumn
sfbrm100DMITempAlarm = _Sfbrm100DMITempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 14),
    _Sfbrm100DMITempAlarm_Type()
)
sfbrm100DMITempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMITempAlarm.setStatus("mandatory")
_Sfbrm100DMITxBiasCurrent_Type = Integer32
_Sfbrm100DMITxBiasCurrent_Object = MibTableColumn
sfbrm100DMITxBiasCurrent = _Sfbrm100DMITxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 15),
    _Sfbrm100DMITxBiasCurrent_Type()
)
sfbrm100DMITxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMITxBiasCurrent.setStatus("mandatory")


class _Sfbrm100DMITxBiasAlarm_Type(Integer32):
    """Custom type sfbrm100DMITxBiasAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 7),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Sfbrm100DMITxBiasAlarm_Type.__name__ = "Integer32"
_Sfbrm100DMITxBiasAlarm_Object = MibTableColumn
sfbrm100DMITxBiasAlarm = _Sfbrm100DMITxBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 16),
    _Sfbrm100DMITxBiasAlarm_Type()
)
sfbrm100DMITxBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMITxBiasAlarm.setStatus("mandatory")
_Sfbrm100DMITxPowerLevel_Type = Integer32
_Sfbrm100DMITxPowerLevel_Object = MibTableColumn
sfbrm100DMITxPowerLevel = _Sfbrm100DMITxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 17),
    _Sfbrm100DMITxPowerLevel_Type()
)
sfbrm100DMITxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMITxPowerLevel.setStatus("mandatory")


class _Sfbrm100DMITxPowerAlarm_Type(Integer32):
    """Custom type sfbrm100DMITxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 7),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Sfbrm100DMITxPowerAlarm_Type.__name__ = "Integer32"
_Sfbrm100DMITxPowerAlarm_Object = MibTableColumn
sfbrm100DMITxPowerAlarm = _Sfbrm100DMITxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 18),
    _Sfbrm100DMITxPowerAlarm_Type()
)
sfbrm100DMITxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMITxPowerAlarm.setStatus("mandatory")
_Sfbrm100DMIRxPowerLevel_Type = Integer32
_Sfbrm100DMIRxPowerLevel_Object = MibTableColumn
sfbrm100DMIRxPowerLevel = _Sfbrm100DMIRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 19),
    _Sfbrm100DMIRxPowerLevel_Type()
)
sfbrm100DMIRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMIRxPowerLevel.setStatus("mandatory")


class _Sfbrm100DMIRxPowerAlarm_Type(Integer32):
    """Custom type sfbrm100DMIRxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 7),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Sfbrm100DMIRxPowerAlarm_Type.__name__ = "Integer32"
_Sfbrm100DMIRxPowerAlarm_Object = MibTableColumn
sfbrm100DMIRxPowerAlarm = _Sfbrm100DMIRxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 3, 1, 20),
    _Sfbrm100DMIRxPowerAlarm_Type()
)
sfbrm100DMIRxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100DMIRxPowerAlarm.setStatus("mandatory")
_Sfbrm100PortL2CPTable_Object = MibTable
sfbrm100PortL2CPTable = _Sfbrm100PortL2CPTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    sfbrm100PortL2CPTable.setStatus("mandatory")
_Sfbrm100PortL2CPEntry_Object = MibTableRow
sfbrm100PortL2CPEntry = _Sfbrm100PortL2CPEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1)
)
sfbrm100PortL2CPEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100PortLocIndex"),
    (0, "TNI-MIB", "sfbrm100PortRmtIndex"),
)
if mibBuilder.loadTexts:
    sfbrm100PortL2CPEntry.setStatus("mandatory")
_Sfbrm100PortL2CPLocIndex_Type = Integer32
_Sfbrm100PortL2CPLocIndex_Object = MibTableColumn
sfbrm100PortL2CPLocIndex = _Sfbrm100PortL2CPLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 1),
    _Sfbrm100PortL2CPLocIndex_Type()
)
sfbrm100PortL2CPLocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortL2CPLocIndex.setStatus("mandatory")
_Sfbrm100PortL2CPRmtIndex_Type = Integer32
_Sfbrm100PortL2CPRmtIndex_Object = MibTableColumn
sfbrm100PortL2CPRmtIndex = _Sfbrm100PortL2CPRmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 2),
    _Sfbrm100PortL2CPRmtIndex_Type()
)
sfbrm100PortL2CPRmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100PortL2CPRmtIndex.setStatus("mandatory")


class _Sfbrm100STPProtocolsFwd_Type(Integer32):
    """Custom type sfbrm100STPProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100STPProtocolsFwd_Type.__name__ = "Integer32"
_Sfbrm100STPProtocolsFwd_Object = MibTableColumn
sfbrm100STPProtocolsFwd = _Sfbrm100STPProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 3),
    _Sfbrm100STPProtocolsFwd_Type()
)
sfbrm100STPProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100STPProtocolsFwd.setStatus("mandatory")


class _Sfbrm100SlowProtocolsFwd_Type(Integer32):
    """Custom type sfbrm100SlowProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100SlowProtocolsFwd_Type.__name__ = "Integer32"
_Sfbrm100SlowProtocolsFwd_Object = MibTableColumn
sfbrm100SlowProtocolsFwd = _Sfbrm100SlowProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 4),
    _Sfbrm100SlowProtocolsFwd_Type()
)
sfbrm100SlowProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100SlowProtocolsFwd.setStatus("mandatory")


class _Sfbrm100PortAuthProtocolFwd_Type(Integer32):
    """Custom type sfbrm100PortAuthProtocolFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100PortAuthProtocolFwd_Type.__name__ = "Integer32"
_Sfbrm100PortAuthProtocolFwd_Object = MibTableColumn
sfbrm100PortAuthProtocolFwd = _Sfbrm100PortAuthProtocolFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 5),
    _Sfbrm100PortAuthProtocolFwd_Type()
)
sfbrm100PortAuthProtocolFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100PortAuthProtocolFwd.setStatus("mandatory")


class _Sfbrm100ELMIProtocolFwd_Type(Integer32):
    """Custom type sfbrm100ELMIProtocolFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100ELMIProtocolFwd_Type.__name__ = "Integer32"
_Sfbrm100ELMIProtocolFwd_Object = MibTableColumn
sfbrm100ELMIProtocolFwd = _Sfbrm100ELMIProtocolFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 6),
    _Sfbrm100ELMIProtocolFwd_Type()
)
sfbrm100ELMIProtocolFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100ELMIProtocolFwd.setStatus("mandatory")


class _Sfbrm100LLDPProtocolFwd_Type(Integer32):
    """Custom type sfbrm100LLDPProtocolFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100LLDPProtocolFwd_Type.__name__ = "Integer32"
_Sfbrm100LLDPProtocolFwd_Object = MibTableColumn
sfbrm100LLDPProtocolFwd = _Sfbrm100LLDPProtocolFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 7),
    _Sfbrm100LLDPProtocolFwd_Type()
)
sfbrm100LLDPProtocolFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100LLDPProtocolFwd.setStatus("mandatory")


class _Sfbrm100BridgeMgmtProtocolsFwd_Type(Integer32):
    """Custom type sfbrm100BridgeMgmtProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100BridgeMgmtProtocolsFwd_Type.__name__ = "Integer32"
_Sfbrm100BridgeMgmtProtocolsFwd_Object = MibTableColumn
sfbrm100BridgeMgmtProtocolsFwd = _Sfbrm100BridgeMgmtProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 8),
    _Sfbrm100BridgeMgmtProtocolsFwd_Type()
)
sfbrm100BridgeMgmtProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100BridgeMgmtProtocolsFwd.setStatus("mandatory")


class _Sfbrm100GARPBlockProtocolsFwd_Type(Integer32):
    """Custom type sfbrm100GARPBlockProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100GARPBlockProtocolsFwd_Type.__name__ = "Integer32"
_Sfbrm100GARPBlockProtocolsFwd_Object = MibTableColumn
sfbrm100GARPBlockProtocolsFwd = _Sfbrm100GARPBlockProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 9),
    _Sfbrm100GARPBlockProtocolsFwd_Type()
)
sfbrm100GARPBlockProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100GARPBlockProtocolsFwd.setStatus("mandatory")


class _Sfbrm100BridgeBlkOtherMulticastsFwd_Type(Integer32):
    """Custom type sfbrm100BridgeBlkOtherMulticastsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tunnel", 1))
    )


_Sfbrm100BridgeBlkOtherMulticastsFwd_Type.__name__ = "Integer32"
_Sfbrm100BridgeBlkOtherMulticastsFwd_Object = MibTableColumn
sfbrm100BridgeBlkOtherMulticastsFwd = _Sfbrm100BridgeBlkOtherMulticastsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 3, 4, 1, 10),
    _Sfbrm100BridgeBlkOtherMulticastsFwd_Type()
)
sfbrm100BridgeBlkOtherMulticastsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100BridgeBlkOtherMulticastsFwd.setStatus("mandatory")
_SfbrmAddrDB_ObjectIdentity = ObjectIdentity
sfbrmAddrDB = _SfbrmAddrDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4)
)
_Sfbrm100FwdDBTable_Object = MibTable
sfbrm100FwdDBTable = _Sfbrm100FwdDBTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sfbrm100FwdDBTable.setStatus("mandatory")
_Sfbrm100FwdDBEntry_Object = MibTableRow
sfbrm100FwdDBEntry = _Sfbrm100FwdDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1)
)
sfbrm100FwdDBEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100FwdLocPortIndex"),
    (0, "TNI-MIB", "sfbrm100FwdDBNum"),
    (0, "TNI-MIB", "sfbrm100FwdMacAddress"),
)
if mibBuilder.loadTexts:
    sfbrm100FwdDBEntry.setStatus("mandatory")
_Sfbrm100FwdLocPortIndex_Type = Integer32
_Sfbrm100FwdLocPortIndex_Object = MibTableColumn
sfbrm100FwdLocPortIndex = _Sfbrm100FwdLocPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 1),
    _Sfbrm100FwdLocPortIndex_Type()
)
sfbrm100FwdLocPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100FwdLocPortIndex.setStatus("mandatory")


class _Sfbrm100FwdDBNum_Type(Integer32):
    """Custom type sfbrm100FwdDBNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Sfbrm100FwdDBNum_Type.__name__ = "Integer32"
_Sfbrm100FwdDBNum_Object = MibTableColumn
sfbrm100FwdDBNum = _Sfbrm100FwdDBNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 2),
    _Sfbrm100FwdDBNum_Type()
)
sfbrm100FwdDBNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100FwdDBNum.setStatus("mandatory")
_Sfbrm100FwdMacAddress_Type = PhysAddress
_Sfbrm100FwdMacAddress_Object = MibTableColumn
sfbrm100FwdMacAddress = _Sfbrm100FwdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 3),
    _Sfbrm100FwdMacAddress_Type()
)
sfbrm100FwdMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100FwdMacAddress.setStatus("mandatory")
_Sfbrm100FwdConnPort_Type = Integer32
_Sfbrm100FwdConnPort_Object = MibTableColumn
sfbrm100FwdConnPort = _Sfbrm100FwdConnPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 4),
    _Sfbrm100FwdConnPort_Type()
)
sfbrm100FwdConnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100FwdConnPort.setStatus("mandatory")
_Sfbrm100FwdPriority_Type = Integer32
_Sfbrm100FwdPriority_Object = MibTableColumn
sfbrm100FwdPriority = _Sfbrm100FwdPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 5),
    _Sfbrm100FwdPriority_Type()
)
sfbrm100FwdPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100FwdPriority.setStatus("mandatory")


class _Sfbrm100FwdEntryType_Type(Integer32):
    """Custom type sfbrm100FwdEntryType based on Integer32"""
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
        *(("dynamic", 4),
          ("static", 1),
          ("staticNRL", 2),
          ("staticPA", 3))
    )


_Sfbrm100FwdEntryType_Type.__name__ = "Integer32"
_Sfbrm100FwdEntryType_Object = MibTableColumn
sfbrm100FwdEntryType = _Sfbrm100FwdEntryType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 6),
    _Sfbrm100FwdEntryType_Type()
)
sfbrm100FwdEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100FwdEntryType.setStatus("mandatory")


class _Sfbrm100FwdEntryStatus_Type(Integer32):
    """Custom type sfbrm100FwdEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("valid", 3),
          ("write", 1))
    )


_Sfbrm100FwdEntryStatus_Type.__name__ = "Integer32"
_Sfbrm100FwdEntryStatus_Object = MibTableColumn
sfbrm100FwdEntryStatus = _Sfbrm100FwdEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 1, 1, 7),
    _Sfbrm100FwdEntryStatus_Type()
)
sfbrm100FwdEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100FwdEntryStatus.setStatus("mandatory")
_Sfbrm100VlanTable_Object = MibTable
sfbrm100VlanTable = _Sfbrm100VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sfbrm100VlanTable.setStatus("mandatory")
_Sfbrm100VlanEntry_Object = MibTableRow
sfbrm100VlanEntry = _Sfbrm100VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1)
)
sfbrm100VlanEntry.setIndexNames(
    (0, "TNI-MIB", "sfbrm100VlanLocPortIndex"),
    (0, "TNI-MIB", "sfbrm100VlanDBNum"),
    (0, "TNI-MIB", "sfbrm100VlanVID"),
)
if mibBuilder.loadTexts:
    sfbrm100VlanEntry.setStatus("mandatory")
_Sfbrm100VlanLocPortIndex_Type = Integer32
_Sfbrm100VlanLocPortIndex_Object = MibTableColumn
sfbrm100VlanLocPortIndex = _Sfbrm100VlanLocPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 1),
    _Sfbrm100VlanLocPortIndex_Type()
)
sfbrm100VlanLocPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100VlanLocPortIndex.setStatus("mandatory")


class _Sfbrm100VlanDBNum_Type(Integer32):
    """Custom type sfbrm100VlanDBNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Sfbrm100VlanDBNum_Type.__name__ = "Integer32"
_Sfbrm100VlanDBNum_Object = MibTableColumn
sfbrm100VlanDBNum = _Sfbrm100VlanDBNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 2),
    _Sfbrm100VlanDBNum_Type()
)
sfbrm100VlanDBNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100VlanDBNum.setStatus("mandatory")
_Sfbrm100VlanVID_Type = Integer32
_Sfbrm100VlanVID_Object = MibTableColumn
sfbrm100VlanVID = _Sfbrm100VlanVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 3),
    _Sfbrm100VlanVID_Type()
)
sfbrm100VlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfbrm100VlanVID.setStatus("mandatory")


class _Sfbrm100VlanVIDPriOverride_Type(Integer32):
    """Custom type sfbrm100VlanVIDPriOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Sfbrm100VlanVIDPriOverride_Type.__name__ = "Integer32"
_Sfbrm100VlanVIDPriOverride_Object = MibTableColumn
sfbrm100VlanVIDPriOverride = _Sfbrm100VlanVIDPriOverride_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 4),
    _Sfbrm100VlanVIDPriOverride_Type()
)
sfbrm100VlanVIDPriOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanVIDPriOverride.setStatus("mandatory")
_Sfbrm100VlanVIDPriority_Type = Integer32
_Sfbrm100VlanVIDPriority_Object = MibTableColumn
sfbrm100VlanVIDPriority = _Sfbrm100VlanVIDPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 5),
    _Sfbrm100VlanVIDPriority_Type()
)
sfbrm100VlanVIDPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanVIDPriority.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort1_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort1 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort1_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort1_Object = MibTableColumn
sfbrm100VlanMemTagPort1 = _Sfbrm100VlanMemTagPort1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 6),
    _Sfbrm100VlanMemTagPort1_Type()
)
sfbrm100VlanMemTagPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort1.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort2_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort2 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort2_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort2_Object = MibTableColumn
sfbrm100VlanMemTagPort2 = _Sfbrm100VlanMemTagPort2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 7),
    _Sfbrm100VlanMemTagPort2_Type()
)
sfbrm100VlanMemTagPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort2.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort3_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort3 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort3_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort3_Object = MibTableColumn
sfbrm100VlanMemTagPort3 = _Sfbrm100VlanMemTagPort3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 8),
    _Sfbrm100VlanMemTagPort3_Type()
)
sfbrm100VlanMemTagPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort3.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort4_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort4 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort4_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort4_Object = MibTableColumn
sfbrm100VlanMemTagPort4 = _Sfbrm100VlanMemTagPort4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 9),
    _Sfbrm100VlanMemTagPort4_Type()
)
sfbrm100VlanMemTagPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort4.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort5_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort5 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort5_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort5_Object = MibTableColumn
sfbrm100VlanMemTagPort5 = _Sfbrm100VlanMemTagPort5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 10),
    _Sfbrm100VlanMemTagPort5_Type()
)
sfbrm100VlanMemTagPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort5.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort6_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort6 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort6_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort6_Object = MibTableColumn
sfbrm100VlanMemTagPort6 = _Sfbrm100VlanMemTagPort6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 11),
    _Sfbrm100VlanMemTagPort6_Type()
)
sfbrm100VlanMemTagPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort6.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort7_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort7 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort7_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort7_Object = MibTableColumn
sfbrm100VlanMemTagPort7 = _Sfbrm100VlanMemTagPort7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 12),
    _Sfbrm100VlanMemTagPort7_Type()
)
sfbrm100VlanMemTagPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort7.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort8_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort8 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort8_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort8_Object = MibTableColumn
sfbrm100VlanMemTagPort8 = _Sfbrm100VlanMemTagPort8_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 13),
    _Sfbrm100VlanMemTagPort8_Type()
)
sfbrm100VlanMemTagPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort8.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort9_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort9 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort9_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort9_Object = MibTableColumn
sfbrm100VlanMemTagPort9 = _Sfbrm100VlanMemTagPort9_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 14),
    _Sfbrm100VlanMemTagPort9_Type()
)
sfbrm100VlanMemTagPort9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort9.setStatus("mandatory")


class _Sfbrm100VlanMemTagPort10_Type(Integer32):
    """Custom type sfbrm100VlanMemTagPort10 based on Integer32"""
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
        *(("memEgressNoMod", 1),
          ("memEgressNoTag", 2),
          ("memEgressTag", 3),
          ("notApplicable", 5),
          ("notMember", 4))
    )


_Sfbrm100VlanMemTagPort10_Type.__name__ = "Integer32"
_Sfbrm100VlanMemTagPort10_Object = MibTableColumn
sfbrm100VlanMemTagPort10 = _Sfbrm100VlanMemTagPort10_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 15),
    _Sfbrm100VlanMemTagPort10_Type()
)
sfbrm100VlanMemTagPort10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanMemTagPort10.setStatus("mandatory")


class _Sfbrm100VlanEntryStatus_Type(Integer32):
    """Custom type sfbrm100VlanEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("valid", 3),
          ("write", 1))
    )


_Sfbrm100VlanEntryStatus_Type.__name__ = "Integer32"
_Sfbrm100VlanEntryStatus_Object = MibTableColumn
sfbrm100VlanEntryStatus = _Sfbrm100VlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 3, 1, 4, 2, 1, 16),
    _Sfbrm100VlanEntryStatus_Type()
)
sfbrm100VlanEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfbrm100VlanEntryStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tnIntruderDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 0, 1)
)
tnIntruderDetect.setObjects(
      *(("TNI-MIB", "spsRptrPortGroupIndex"),
        ("TNI-MIB", "spsRptrPortIndex"))
)
if mibBuilder.loadTexts:
    tnIntruderDetect.setStatus(
        ""
    )

sfbrm100ATUDbFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 119)
)
if mibBuilder.loadTexts:
    sfbrm100ATUDbFull.setStatus(
        ""
    )

sfbrm100VTUMemberViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 120)
)
if mibBuilder.loadTexts:
    sfbrm100VTUMemberViolation.setStatus(
        ""
    )

sfbrm100VTUMissViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 121)
)
if mibBuilder.loadTexts:
    sfbrm100VTUMissViolation.setStatus(
        ""
    )

sfbrm100ATUMemberViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 122)
)
if mibBuilder.loadTexts:
    sfbrm100ATUMemberViolation.setStatus(
        ""
    )

sfbrm100ATUMissViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 123)
)
if mibBuilder.loadTexts:
    sfbrm100ATUMissViolation.setStatus(
        ""
    )

sfbrm100OAMRemoteDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 124)
)
if mibBuilder.loadTexts:
    sfbrm100OAMRemoteDetected.setStatus(
        ""
    )

sfbrm100EEPROMOnFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 125)
)
if mibBuilder.loadTexts:
    sfbrm100EEPROMOnFiber.setStatus(
        ""
    )

sfbrm100DMIOnFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 126)
)
if mibBuilder.loadTexts:
    sfbrm100DMIOnFiber.setStatus(
        ""
    )

sfbrm100LinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 127)
)
if mibBuilder.loadTexts:
    sfbrm100LinkChanged.setStatus(
        ""
    )

sfbrm100DMILowRxIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 128)
)
if mibBuilder.loadTexts:
    sfbrm100DMILowRxIntrusion.setStatus(
        ""
    )

sfbrm100DMILowRxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 129)
)
if mibBuilder.loadTexts:
    sfbrm100DMILowRxPower.setStatus(
        ""
    )

sfbrm100DMILowTxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 130)
)
if mibBuilder.loadTexts:
    sfbrm100DMILowTxPower.setStatus(
        ""
    )

sfbrm100DMILowTxBias = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 131)
)
if mibBuilder.loadTexts:
    sfbrm100DMILowTxBias.setStatus(
        ""
    )

sfbrm100DMILowTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 132)
)
if mibBuilder.loadTexts:
    sfbrm100DMILowTemperature.setStatus(
        ""
    )

sfbrm100LastGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 133)
)
if mibBuilder.loadTexts:
    sfbrm100LastGasp.setStatus(
        ""
    )

sfbrm100OAMPeerLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 134)
)
if mibBuilder.loadTexts:
    sfbrm100OAMPeerLinkDown.setStatus(
        ""
    )

sfbrm100OAMPeerLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 135)
)
if mibBuilder.loadTexts:
    sfbrm100OAMPeerLinkUp.setStatus(
        ""
    )

sfbrm100OAMPeerDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 136)
)
if mibBuilder.loadTexts:
    sfbrm100OAMPeerDyingGasp.setStatus(
        ""
    )

sfbrm100OAMThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 137)
)
if mibBuilder.loadTexts:
    sfbrm100OAMThresholdEvent.setStatus(
        ""
    )

sfbrm100PeerVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 3, 2, 0, 138)
)
if mibBuilder.loadTexts:
    sfbrm100PeerVersionMismatch.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TNI-MIB",
    **{"MacAddress": MacAddress,
       "CpsConnector": CpsConnector,
       "transition": transition,
       "tnIntruderDetect": tnIntruderDetect,
       "productId": productId,
       "rptrProdsId": rptrProdsId,
       "rptrStackMId": rptrStackMId,
       "rptrSMVer1Id": rptrSMVer1Id,
       "rptrSMVer2Id": rptrSMVer2Id,
       "rptrSM08TId": rptrSM08TId,
       "rptrSM08TSId": rptrSM08TSId,
       "rptrSM06FId": rptrSM06FId,
       "rptrSM06FSId": rptrSM06FSId,
       "rptrSM8T0Id": rptrSM8T0Id,
       "rptrSM8TS0Id": rptrSM8TS0Id,
       "rptrSM6F0Id": rptrSM6F0Id,
       "rptrSM6FS0Id": rptrSM6FS0Id,
       "rptrSM8T6FId": rptrSM8T6FId,
       "rptrSM8TS6FId": rptrSM8TS6FId,
       "rptrSM8T6FSId": rptrSM8T6FSId,
       "rptrSM8TS6FSId": rptrSM8TS6FSId,
       "rptrSM6F8TId": rptrSM6F8TId,
       "rptrSM6FS8TId": rptrSM6FS8TId,
       "rptrSM6F8TSId": rptrSM6F8TSId,
       "rptrSM6FS8TSId": rptrSM6FS8TSId,
       "rptrSM8T8TId": rptrSM8T8TId,
       "rptrSM8TS8TId": rptrSM8TS8TId,
       "rptrSM8T8TSId": rptrSM8T8TSId,
       "rptrSM8TS8TSId": rptrSM8TS8TSId,
       "rptrSM6F6FId": rptrSM6F6FId,
       "rptrSM6FS6FId": rptrSM6FS6FId,
       "rptrSM6F6FSId": rptrSM6F6FSId,
       "rptrSM6FS6FSId": rptrSM6FS6FSId,
       "rptrSM24TId": rptrSM24TId,
       "rptrSM16TId": rptrSM16TId,
       "rptrSM14FId": rptrSM14FId,
       "rptrSM12FId": rptrSM12FId,
       "rptrSM6FId": rptrSM6FId,
       "rptrSM0Id": rptrSM0Id,
       "rptrSPSId": rptrSPSId,
       "rptrSPSVer1Id": rptrSPSVer1Id,
       "rptrESPS24Id": rptrESPS24Id,
       "rptrESPS24SId": rptrESPS24SId,
       "ringProdsId": ringProdsId,
       "ringStackTRId": ringStackTRId,
       "ringTRVer1Id": ringTRVer1Id,
       "ringTRVer2Id": ringTRVer2Id,
       "ringTR0Id": ringTR0Id,
       "ringTR16TId": ringTR16TId,
       "brdgProdsId": brdgProdsId,
       "brdgSwitchMId": brdgSwitchMId,
       "brdgSWVer1Id": brdgSWVer1Id,
       "brdgFBRMId": brdgFBRMId,
       "sfbrm100ATUDbFull": sfbrm100ATUDbFull,
       "sfbrm100VTUMemberViolation": sfbrm100VTUMemberViolation,
       "sfbrm100VTUMissViolation": sfbrm100VTUMissViolation,
       "sfbrm100ATUMemberViolation": sfbrm100ATUMemberViolation,
       "sfbrm100ATUMissViolation": sfbrm100ATUMissViolation,
       "sfbrm100OAMRemoteDetected": sfbrm100OAMRemoteDetected,
       "sfbrm100EEPROMOnFiber": sfbrm100EEPROMOnFiber,
       "sfbrm100DMIOnFiber": sfbrm100DMIOnFiber,
       "sfbrm100LinkChanged": sfbrm100LinkChanged,
       "sfbrm100DMILowRxIntrusion": sfbrm100DMILowRxIntrusion,
       "sfbrm100DMILowRxPower": sfbrm100DMILowRxPower,
       "sfbrm100DMILowTxPower": sfbrm100DMILowTxPower,
       "sfbrm100DMILowTxBias": sfbrm100DMILowTxBias,
       "sfbrm100DMILowTemperature": sfbrm100DMILowTemperature,
       "sfbrm100LastGasp": sfbrm100LastGasp,
       "sfbrm100OAMPeerLinkDown": sfbrm100OAMPeerLinkDown,
       "sfbrm100OAMPeerLinkUp": sfbrm100OAMPeerLinkUp,
       "sfbrm100OAMPeerDyingGasp": sfbrm100OAMPeerDyingGasp,
       "sfbrm100OAMThresholdEvent": sfbrm100OAMThresholdEvent,
       "sfbrm100PeerVersionMismatch": sfbrm100PeerVersionMismatch,
       "products": products,
       "repeater": repeater,
       "tnStackM": tnStackM,
       "tnSMCommon": tnSMCommon,
       "tnSMComHwReset": tnSMComHwReset,
       "tnSMComMgmtHwRev": tnSMComMgmtHwRev,
       "tnSMComDiagSwRev": tnSMComDiagSwRev,
       "tnSMComMgmtSwRev": tnSMComMgmtSwRev,
       "tnSMComIpAddr": tnSMComIpAddr,
       "tnSMComNetMask": tnSMComNetMask,
       "tnSMVer1": tnSMVer1,
       "tnSMVer2": tnSMVer2,
       "sps": sps,
       "spsCommon": spsCommon,
       "spsReset": spsReset,
       "spsConfig": spsConfig,
       "spsBootpEnable": spsBootpEnable,
       "spsBootpServer": spsBootpServer,
       "spsBootpFilename": spsBootpFilename,
       "spsDefaultGateway": spsDefaultGateway,
       "spsMgmtSegment": spsMgmtSegment,
       "spsIpAddrTable": spsIpAddrTable,
       "spsIpAddrEntry": spsIpAddrEntry,
       "spsIpIfIndex": spsIpIfIndex,
       "spsIpAddr": spsIpAddr,
       "spsIpNetMask": spsIpNetMask,
       "spsTrapTable": spsTrapTable,
       "spsTrapEntry": spsTrapEntry,
       "spsTrapIndex": spsTrapIndex,
       "spsTrapDestination": spsTrapDestination,
       "spsTrapCommunity": spsTrapCommunity,
       "spsVer1": spsVer1,
       "spsMaxSegment": spsMaxSegment,
       "spsPasswdReset": spsPasswdReset,
       "spsExternalPowerSupply": spsExternalPowerSupply,
       "spsDisplayString": spsDisplayString,
       "spsRptrGroupTable": spsRptrGroupTable,
       "spsRptrGroupEntry": spsRptrGroupEntry,
       "spsRptrGroupIndex": spsRptrGroupIndex,
       "spsRptrGroupUnitId": spsRptrGroupUnitId,
       "spsRptrGroupInternalPowerSupply": spsRptrGroupInternalPowerSupply,
       "spsRptrPortTable": spsRptrPortTable,
       "spsRptrPortEntry": spsRptrPortEntry,
       "spsRptrPortGroupIndex": spsRptrPortGroupIndex,
       "spsRptrPortIndex": spsRptrPortIndex,
       "spsRptrPortSegment": spsRptrPortSegment,
       "spsRptrPortSrcAddr": spsRptrPortSrcAddr,
       "spsRptrPortEavesdropping": spsRptrPortEavesdropping,
       "spsRptrPortIntrusion": spsRptrPortIntrusion,
       "spsRptrPortCollisionLimit": spsRptrPortCollisionLimit,
       "spsRptrPortEnableIntruderDetectTrap": spsRptrPortEnableIntruderDetectTrap,
       "spsRptrPortDisableIntruder": spsRptrPortDisableIntruder,
       "spsSerialPortTable": spsSerialPortTable,
       "spsSerialPortEntry": spsSerialPortEntry,
       "spsSerialPortIndex": spsSerialPortIndex,
       "spsSerialPortModemControl": spsSerialPortModemControl,
       "spsMonitorSegmentTable": spsMonitorSegmentTable,
       "spsMonitorSegmentEntry": spsMonitorSegmentEntry,
       "spsMonitorSegmentIndex": spsMonitorSegmentIndex,
       "spsMonitorSegmentTotalFrames": spsMonitorSegmentTotalFrames,
       "spsMonitorSegmentTotalOctets": spsMonitorSegmentTotalOctets,
       "spsMonitorSegmentTotalErrors": spsMonitorSegmentTotalErrors,
       "ring": ring,
       "tnStackTR": tnStackTR,
       "tnTRCommon": tnTRCommon,
       "tnTRComHwReset": tnTRComHwReset,
       "tnTRComMgmtHwRev": tnTRComMgmtHwRev,
       "tnTRComDiagSwRev": tnTRComDiagSwRev,
       "tnTRComMgmtSwRev": tnTRComMgmtSwRev,
       "tnTRComIpAddr": tnTRComIpAddr,
       "tnTRComNetMask": tnTRComNetMask,
       "tnTRComIfaceCapacity": tnTRComIfaceCapacity,
       "tnTRVer1": tnTRVer1,
       "tnTRV1Commands": tnTRV1Commands,
       "tnTRV1RingStatus": tnTRV1RingStatus,
       "tnTRV1RingState": tnTRV1RingState,
       "tnTRV1RingOpenStatus": tnTRV1RingOpenStatus,
       "tnTRV1RingSpeed": tnTRV1RingSpeed,
       "tnTRV1UpStream": tnTRV1UpStream,
       "tnTRV1ActMonParticipate": tnTRV1ActMonParticipate,
       "tnTRV1Functional": tnTRV1Functional,
       "tnTRV1StatsLineErrors": tnTRV1StatsLineErrors,
       "tnTRV1StatsBurstErrors": tnTRV1StatsBurstErrors,
       "tnTRV1StatsACErrors": tnTRV1StatsACErrors,
       "tnTRV1StatsAbortTransErrors": tnTRV1StatsAbortTransErrors,
       "tnTRV1StatsInternalErrors": tnTRV1StatsInternalErrors,
       "tnTRV1StatsLostFrameErrors": tnTRV1StatsLostFrameErrors,
       "tnTRV1StatsReceiveCongestions": tnTRV1StatsReceiveCongestions,
       "tnTRV1StatsFrameCopiedErrors": tnTRV1StatsFrameCopiedErrors,
       "tnTRV1StatsTokenErrors": tnTRV1StatsTokenErrors,
       "tnTRV1StatsSoftErrors": tnTRV1StatsSoftErrors,
       "tnTRV1StatsHardErrors": tnTRV1StatsHardErrors,
       "tnTRV1StatsSignalLoss": tnTRV1StatsSignalLoss,
       "tnTRV1StatsTransmitBeacons": tnTRV1StatsTransmitBeacons,
       "tnTRV1StatsRecoverys": tnTRV1StatsRecoverys,
       "tnTRV1StatsLobeWires": tnTRV1StatsLobeWires,
       "tnTRV1StatsRemoves": tnTRV1StatsRemoves,
       "tnTRV1StatsSingles": tnTRV1StatsSingles,
       "tnTRV1StatsFreqErrors": tnTRV1StatsFreqErrors,
       "tnTRV1TimerReturnRepeat": tnTRV1TimerReturnRepeat,
       "tnTRV1TimerHolding": tnTRV1TimerHolding,
       "tnTRV1TimerQueuePDU": tnTRV1TimerQueuePDU,
       "tnTRV1TimerValidTransmit": tnTRV1TimerValidTransmit,
       "tnTRV1TimerNoToken": tnTRV1TimerNoToken,
       "tnTRV1TimerActiveMon": tnTRV1TimerActiveMon,
       "tnTRV1TimerStandbyMon": tnTRV1TimerStandbyMon,
       "tnTRV1TimerErrorReport": tnTRV1TimerErrorReport,
       "tnTRV1TimerBeaconTransmit": tnTRV1TimerBeaconTransmit,
       "tnTRV1TimerBeaconReceive": tnTRV1TimerBeaconReceive,
       "tnTRVer2": tnTRVer2,
       "bridge": bridge,
       "sfbrm10x100": sfbrm10x100,
       "sfbrmSystem": sfbrmSystem,
       "sfbrm100SystemTable": sfbrm100SystemTable,
       "sfbrm100SystemEntry": sfbrm100SystemEntry,
       "sfbrm100SysLocPortIndex": sfbrm100SysLocPortIndex,
       "sfbrm100SysSecIndex": sfbrm100SysSecIndex,
       "sfbrm100SysGrpString": sfbrm100SysGrpString,
       "sfbrm100SysMRevision": sfbrm100SysMRevision,
       "sfbrm100SysCfgMatch": sfbrm100SysCfgMatch,
       "sfbrm100SysBootLoaderRevision": sfbrm100SysBootLoaderRevision,
       "sfbrm100SysFirmwareRevision": sfbrm100SysFirmwareRevision,
       "sfbrm100SysSerialNumber": sfbrm100SysSerialNumber,
       "sfbrm100SysBIAddress": sfbrm100SysBIAddress,
       "sfbrm100SysSlotIndex": sfbrm100SysSlotIndex,
       "sfbrm100SysNumPorts": sfbrm100SysNumPorts,
       "sfbrm100SysMACAddress": sfbrm100SysMACAddress,
       "sfbrm100SystemReset": sfbrm100SystemReset,
       "sfbrm100SysIPaddress": sfbrm100SysIPaddress,
       "sfbrm100SysSubnetMask": sfbrm100SysSubnetMask,
       "sfbrm100SysDefGateway": sfbrm100SysDefGateway,
       "sfbrm100SysSNMPTrapMgr": sfbrm100SysSNMPTrapMgr,
       "sfbrm100SysRadiusAuth": sfbrm100SysRadiusAuth,
       "sfbrm100SysRadiusServerAddr": sfbrm100SysRadiusServerAddr,
       "sfbrm100SysRadiusSecret": sfbrm100SysRadiusSecret,
       "sfbrm100SysRadiusRetry": sfbrm100SysRadiusRetry,
       "sfbrm100SysRadiusTimeout": sfbrm100SysRadiusTimeout,
       "sfbrm100SysDHCPEnable": sfbrm100SysDHCPEnable,
       "sfbrm100SysSerialAccess": sfbrm100SysSerialAccess,
       "sfbrm100SysTLPT": sfbrm100SysTLPT,
       "sfbrm100SysTFTPServerAddr": sfbrm100SysTFTPServerAddr,
       "sfbrm100SysTFTPfilename": sfbrm100SysTFTPfilename,
       "sfbrm100SysTFTPCmd": sfbrm100SysTFTPCmd,
       "sfbrm100SysTFTPServerIgnore": sfbrm100SysTFTPServerIgnore,
       "sfbrm100SysMgmtVlanId": sfbrm100SysMgmtVlanId,
       "sfbrm100SysSNMPAccess": sfbrm100SysSNMPAccess,
       "sfbrm100SysIPAccess": sfbrm100SysIPAccess,
       "sfbrm100SysLastGaspPdu": sfbrm100SysLastGaspPdu,
       "sfbrm100SysLastGaspPort": sfbrm100SysLastGaspPort,
       "sfbrm100SysLocalLPT": sfbrm100SysLocalLPT,
       "sfbrm100SysLPTPort": sfbrm100SysLPTPort,
       "sfbrm100SysAutoUpgrade": sfbrm100SysAutoUpgrade,
       "sfbrm100SysFormFactorSlot": sfbrm100SysFormFactorSlot,
       "sfbrm100SysFormFactorPort": sfbrm100SysFormFactorPort,
       "sfbrm100SysOAMPort": sfbrm100SysOAMPort,
       "sfbrmSwitch": sfbrmSwitch,
       "sfbrm100SwTable": sfbrm100SwTable,
       "sfbrm100SwEntry": sfbrm100SwEntry,
       "sfbrm100SwPortIndex": sfbrm100SwPortIndex,
       "sfbrm100SwSecIndex": sfbrm100SwSecIndex,
       "sfbrm100SwATUAgeTimeout": sfbrm100SwATUAgeTimeout,
       "sfbrm100SwIngressMonPort": sfbrm100SwIngressMonPort,
       "sfbrm100SwEgressMonPort": sfbrm100SwEgressMonPort,
       "sfbrm100SwFactoryDefaults": sfbrm100SwFactoryDefaults,
       "sfbrm100SwResetCounters": sfbrm100SwResetCounters,
       "sfbrm100SwHistMode": sfbrm100SwHistMode,
       "sfbrm100SwIEEEPriRemap0": sfbrm100SwIEEEPriRemap0,
       "sfbrm100SwIEEEPriRemap1": sfbrm100SwIEEEPriRemap1,
       "sfbrm100SwIEEEPriRemap2": sfbrm100SwIEEEPriRemap2,
       "sfbrm100SwIEEEPriRemap3": sfbrm100SwIEEEPriRemap3,
       "sfbrm100SwIEEEPriRemap4": sfbrm100SwIEEEPriRemap4,
       "sfbrm100SwIEEEPriRemap5": sfbrm100SwIEEEPriRemap5,
       "sfbrm100SwIEEEPriRemap6": sfbrm100SwIEEEPriRemap6,
       "sfbrm100SwIEEEPriRemap7": sfbrm100SwIEEEPriRemap7,
       "sfbrm100SwFlushFdb": sfbrm100SwFlushFdb,
       "sfbrm100SwFlushVlandb": sfbrm100SwFlushVlandb,
       "sfbrm100SwUseDoubleTagData": sfbrm100SwUseDoubleTagData,
       "sfbrm100SwFiberRedundancy": sfbrm100SwFiberRedundancy,
       "sfbrm100SwFiberRedundRevert": sfbrm100SwFiberRedundRevert,
       "sfbrm100SwFbrRedundActivePort": sfbrm100SwFbrRedundActivePort,
       "sfbrm100SwSupressVlanViolations": sfbrm100SwSupressVlanViolations,
       "sfbrm100SwSupressMACViolations": sfbrm100SwSupressMACViolations,
       "sfbrm100SwIPPrioTable": sfbrm100SwIPPrioTable,
       "sfbrm100SwIPPrioEntry": sfbrm100SwIPPrioEntry,
       "sfbrm100SwIPPrioPortIndex": sfbrm100SwIPPrioPortIndex,
       "sfbrm100SwIPPrioIndex": sfbrm100SwIPPrioIndex,
       "sfbrm100SwIPPrioTC": sfbrm100SwIPPrioTC,
       "sfbrm100SwIPPrioRemap": sfbrm100SwIPPrioRemap,
       "sfbrmPort": sfbrmPort,
       "sfbrm100PortTable": sfbrm100PortTable,
       "sfbrm100PortEntry": sfbrm100PortEntry,
       "sfbrm100PortLocIndex": sfbrm100PortLocIndex,
       "sfbrm100PortRmtIndex": sfbrm100PortRmtIndex,
       "sfbrm100PortGrpString": sfbrm100PortGrpString,
       "sfbrm100PortConnType": sfbrm100PortConnType,
       "sfbrm100PortOAMState": sfbrm100PortOAMState,
       "sfbrm100PortOAMModeCtrl": sfbrm100PortOAMModeCtrl,
       "sfbrm100PortRmtLoopback": sfbrm100PortRmtLoopback,
       "sfbrm100PortIgnoreLoopback": sfbrm100PortIgnoreLoopback,
       "sfbrm100PortAdvPause": sfbrm100PortAdvPause,
       "sfbrm100PortAdv1000FDX": sfbrm100PortAdv1000FDX,
       "sfbrm100PortAdv1000HDX": sfbrm100PortAdv1000HDX,
       "sfbrm100PortAdv100FDX": sfbrm100PortAdv100FDX,
       "sfbrm100PortAdv100HDX": sfbrm100PortAdv100HDX,
       "sfbrm100PortAdv10FDX": sfbrm100PortAdv10FDX,
       "sfbrm100PortAdv10HDX": sfbrm100PortAdv10HDX,
       "sfbrm100PortAutoneg": sfbrm100PortAutoneg,
       "sfbrm100PortFDuplex": sfbrm100PortFDuplex,
       "sfbrm100PortFSpeed": sfbrm100PortFSpeed,
       "sfbrm100PortLpPauseAbility": sfbrm100PortLpPauseAbility,
       "sfbrm100PortLpAutonegAbility": sfbrm100PortLpAutonegAbility,
       "sfbrm100PortLinkState": sfbrm100PortLinkState,
       "sfbrm100PortAutonegState": sfbrm100PortAutonegState,
       "sfbrm100PortDuplex": sfbrm100PortDuplex,
       "sfbrm100PortSpeed": sfbrm100PortSpeed,
       "sfbrm100PortFEFI": sfbrm100PortFEFI,
       "sfbrm100PortAutocross": sfbrm100PortAutocross,
       "sfbrm100PortLock": sfbrm100PortLock,
       "sfbrm100PortIgnoreWrongData": sfbrm100PortIgnoreWrongData,
       "sfbrm100PortIGMPSnoop": sfbrm100PortIGMPSnoop,
       "sfbrm100PortDoubleTagging": sfbrm100PortDoubleTagging,
       "sfbrm100PortUseIPTC": sfbrm100PortUseIPTC,
       "sfbrm100PortUseTagTC": sfbrm100PortUseTagTC,
       "sfbrm100PortUseBothTC": sfbrm100PortUseBothTC,
       "sfbrm100PortVLANTunnel": sfbrm100PortVLANTunnel,
       "sfbrm100PortFwdUnknown": sfbrm100PortFwdUnknown,
       "sfbrm100PortDefForward": sfbrm100PortDefForward,
       "sfbrm100PortAdminState": sfbrm100PortAdminState,
       "sfbrm100PortVTUPriOverride": sfbrm100PortVTUPriOverride,
       "sfbrm100PortSAPriOverride": sfbrm100PortSAPriOverride,
       "sfbrm100PortDAPriOverride": sfbrm100PortDAPriOverride,
       "sfbrm100PortVLANStatus": sfbrm100PortVLANStatus,
       "sfbrm100PortDiscardTagged": sfbrm100PortDiscardTagged,
       "sfbrm100PortDiscardUntagged": sfbrm100PortDiscardUntagged,
       "sfbrm100PortEgressMonitor": sfbrm100PortEgressMonitor,
       "sfbrm100PortIngressMonitor": sfbrm100PortIngressMonitor,
       "sfbrm100PortPri3IngressRateCtrl": sfbrm100PortPri3IngressRateCtrl,
       "sfbrm100PortPri2IngressRateCtrl": sfbrm100PortPri2IngressRateCtrl,
       "sfbrm100PortPri1IngressRateCtrl": sfbrm100PortPri1IngressRateCtrl,
       "sfbrm100PortPri0IngressRate": sfbrm100PortPri0IngressRate,
       "sfbrm100PortIngressLimitMode": sfbrm100PortIngressLimitMode,
       "sfbrm100PortEgressRate": sfbrm100PortEgressRate,
       "sfbrm100PortDefaultPriority": sfbrm100PortDefaultPriority,
       "sfbrm100PortForceDefVLANId": sfbrm100PortForceDefVLANId,
       "sfbrm100PortDefaultVLANId": sfbrm100PortDefaultVLANId,
       "sfbrm100PortBasedVLANTbl": sfbrm100PortBasedVLANTbl,
       "sfbrm100PortIEEEPriRemap0": sfbrm100PortIEEEPriRemap0,
       "sfbrm100PortIEEEPriRemap1": sfbrm100PortIEEEPriRemap1,
       "sfbrm100PortIEEEPriRemap2": sfbrm100PortIEEEPriRemap2,
       "sfbrm100PortIEEEPriRemap3": sfbrm100PortIEEEPriRemap3,
       "sfbrm100PortIEEEPriRemap4": sfbrm100PortIEEEPriRemap4,
       "sfbrm100PortIEEEPriRemap5": sfbrm100PortIEEEPriRemap5,
       "sfbrm100PortIEEEPriRemap6": sfbrm100PortIEEEPriRemap6,
       "sfbrm100PortIEEEPriRemap7": sfbrm100PortIEEEPriRemap7,
       "sfbrm100PortVCTest": sfbrm100PortVCTest,
       "sfbrm100PortVCTxMDI0Status": sfbrm100PortVCTxMDI0Status,
       "sfbrm100PortTxMDI0Dist": sfbrm100PortTxMDI0Dist,
       "sfbrm100PortVCRxMDI1Status": sfbrm100PortVCRxMDI1Status,
       "sfbrm100PortRxMDI1Dist": sfbrm100PortRxMDI1Dist,
       "sfbrm100PortVCMDI2Status": sfbrm100PortVCMDI2Status,
       "sfbrm100PortMDI2Dist": sfbrm100PortMDI2Dist,
       "sfbrm100PortVCMDI3Status": sfbrm100PortVCMDI3Status,
       "sfbrm100PortMDI3Dist": sfbrm100PortMDI3Dist,
       "sfbrm100PortResetCounters": sfbrm100PortResetCounters,
       "sfbrm100PortIPTrafficAccess": sfbrm100PortIPTrafficAccess,
       "sfbrm100PortResetOAMCounters": sfbrm100PortResetOAMCounters,
       "sfbrm100PortForceAutoUpgrade": sfbrm100PortForceAutoUpgrade,
       "sfbrm100PortModeType": sfbrm100PortModeType,
       "sfbrm100PortOAMMode": sfbrm100PortOAMMode,
       "sfbrm100PortPhyNumber": sfbrm100PortPhyNumber,
       "sfbrm100PortIngressRateLimit2": sfbrm100PortIngressRateLimit2,
       "sfbrm100PortEgressRateLimit2": sfbrm100PortEgressRateLimit2,
       "sfbrm100PortStatsTable": sfbrm100PortStatsTable,
       "sfbrm100PortStatsEntry": sfbrm100PortStatsEntry,
       "sfbrm100PortLocStatsIndex": sfbrm100PortLocStatsIndex,
       "sfbrm100PortRmtStatsIndex": sfbrm100PortRmtStatsIndex,
       "sfbrm100PortInGoodOctetsLo": sfbrm100PortInGoodOctetsLo,
       "sfbrm100PortInGoodOctetsHi": sfbrm100PortInGoodOctetsHi,
       "sfbrm100PortInBadOctets": sfbrm100PortInBadOctets,
       "sfbrm100PortInUnicasts": sfbrm100PortInUnicasts,
       "sfbrm100PortInBroadcasts": sfbrm100PortInBroadcasts,
       "sfbrm100PortInMulticasts": sfbrm100PortInMulticasts,
       "sfbrm100PortInPause": sfbrm100PortInPause,
       "sfbrm100PortInUndersize": sfbrm100PortInUndersize,
       "sfbrm100PortInFragments": sfbrm100PortInFragments,
       "sfbrm100PortInOversize": sfbrm100PortInOversize,
       "sfbrm100PortInJabber": sfbrm100PortInJabber,
       "sfbrm100PortInRxErr": sfbrm100PortInRxErr,
       "sfbrm100PortInFCSErr": sfbrm100PortInFCSErr,
       "sfbrm100PortIn64Octets": sfbrm100PortIn64Octets,
       "sfbrm100PortIn65to127Octets": sfbrm100PortIn65to127Octets,
       "sfbrm100PortIn128to255Octets": sfbrm100PortIn128to255Octets,
       "sfbrm100PortIn256to511Octets": sfbrm100PortIn256to511Octets,
       "sfbrm100PortIn512to1023Octets": sfbrm100PortIn512to1023Octets,
       "sfbrm100PortIn1024toMaxOctets": sfbrm100PortIn1024toMaxOctets,
       "sfbrm100PortOutOctetsLo": sfbrm100PortOutOctetsLo,
       "sfbrm100PortOutOctetsHi": sfbrm100PortOutOctetsHi,
       "sfbrm100PortOutUnicasts": sfbrm100PortOutUnicasts,
       "sfbrm100PortOutBroadcasts": sfbrm100PortOutBroadcasts,
       "sfbrm100PortOutMulticasts": sfbrm100PortOutMulticasts,
       "sfbrm100PortOutPause": sfbrm100PortOutPause,
       "sfbrm100PortOutDeferred": sfbrm100PortOutDeferred,
       "sfbrm100PortOutCollisions": sfbrm100PortOutCollisions,
       "sfbrm100PortOutSingle": sfbrm100PortOutSingle,
       "sfbrm100PortOutMultiple": sfbrm100PortOutMultiple,
       "sfbrm100PortOutExcessive": sfbrm100PortOutExcessive,
       "sfbrm100PortOutLate": sfbrm100PortOutLate,
       "sfbrm100PortOutFCSErr": sfbrm100PortOutFCSErr,
       "sfbrm100PortInDiscard": sfbrm100PortInDiscard,
       "sfbrm100PortInFiltered": sfbrm100PortInFiltered,
       "sfbrm100PortOutFiltered": sfbrm100PortOutFiltered,
       "sfbrm100DMITable": sfbrm100DMITable,
       "sfbrm100DMIEntry": sfbrm100DMIEntry,
       "sfbrm100DMILocPortIndex": sfbrm100DMILocPortIndex,
       "sfbrm100DMIRmtPortIndex": sfbrm100DMIRmtPortIndex,
       "sfbrm100DMIRxPwrLvlPreset": sfbrm100DMIRxPwrLvlPreset,
       "sfbrm100DMIConnType": sfbrm100DMIConnType,
       "sfbrm100DMIBitRate": sfbrm100DMIBitRate,
       "sfbrm100DMILenFor9x125umKM": sfbrm100DMILenFor9x125umKM,
       "sfbrm100DMILenFor9x125um100M": sfbrm100DMILenFor9x125um100M,
       "sfbrm100DMILenFor50x125um10M": sfbrm100DMILenFor50x125um10M,
       "sfbrm100DMILenFor625x125um10M": sfbrm100DMILenFor625x125um10M,
       "sfbrm100DMILenForCopper": sfbrm100DMILenForCopper,
       "sfbrm100DMIId": sfbrm100DMIId,
       "sfbrm100DMILaserWavelength": sfbrm100DMILaserWavelength,
       "sfbrm100DMITemperature": sfbrm100DMITemperature,
       "sfbrm100DMITempAlarm": sfbrm100DMITempAlarm,
       "sfbrm100DMITxBiasCurrent": sfbrm100DMITxBiasCurrent,
       "sfbrm100DMITxBiasAlarm": sfbrm100DMITxBiasAlarm,
       "sfbrm100DMITxPowerLevel": sfbrm100DMITxPowerLevel,
       "sfbrm100DMITxPowerAlarm": sfbrm100DMITxPowerAlarm,
       "sfbrm100DMIRxPowerLevel": sfbrm100DMIRxPowerLevel,
       "sfbrm100DMIRxPowerAlarm": sfbrm100DMIRxPowerAlarm,
       "sfbrm100PortL2CPTable": sfbrm100PortL2CPTable,
       "sfbrm100PortL2CPEntry": sfbrm100PortL2CPEntry,
       "sfbrm100PortL2CPLocIndex": sfbrm100PortL2CPLocIndex,
       "sfbrm100PortL2CPRmtIndex": sfbrm100PortL2CPRmtIndex,
       "sfbrm100STPProtocolsFwd": sfbrm100STPProtocolsFwd,
       "sfbrm100SlowProtocolsFwd": sfbrm100SlowProtocolsFwd,
       "sfbrm100PortAuthProtocolFwd": sfbrm100PortAuthProtocolFwd,
       "sfbrm100ELMIProtocolFwd": sfbrm100ELMIProtocolFwd,
       "sfbrm100LLDPProtocolFwd": sfbrm100LLDPProtocolFwd,
       "sfbrm100BridgeMgmtProtocolsFwd": sfbrm100BridgeMgmtProtocolsFwd,
       "sfbrm100GARPBlockProtocolsFwd": sfbrm100GARPBlockProtocolsFwd,
       "sfbrm100BridgeBlkOtherMulticastsFwd": sfbrm100BridgeBlkOtherMulticastsFwd,
       "sfbrmAddrDB": sfbrmAddrDB,
       "sfbrm100FwdDBTable": sfbrm100FwdDBTable,
       "sfbrm100FwdDBEntry": sfbrm100FwdDBEntry,
       "sfbrm100FwdLocPortIndex": sfbrm100FwdLocPortIndex,
       "sfbrm100FwdDBNum": sfbrm100FwdDBNum,
       "sfbrm100FwdMacAddress": sfbrm100FwdMacAddress,
       "sfbrm100FwdConnPort": sfbrm100FwdConnPort,
       "sfbrm100FwdPriority": sfbrm100FwdPriority,
       "sfbrm100FwdEntryType": sfbrm100FwdEntryType,
       "sfbrm100FwdEntryStatus": sfbrm100FwdEntryStatus,
       "sfbrm100VlanTable": sfbrm100VlanTable,
       "sfbrm100VlanEntry": sfbrm100VlanEntry,
       "sfbrm100VlanLocPortIndex": sfbrm100VlanLocPortIndex,
       "sfbrm100VlanDBNum": sfbrm100VlanDBNum,
       "sfbrm100VlanVID": sfbrm100VlanVID,
       "sfbrm100VlanVIDPriOverride": sfbrm100VlanVIDPriOverride,
       "sfbrm100VlanVIDPriority": sfbrm100VlanVIDPriority,
       "sfbrm100VlanMemTagPort1": sfbrm100VlanMemTagPort1,
       "sfbrm100VlanMemTagPort2": sfbrm100VlanMemTagPort2,
       "sfbrm100VlanMemTagPort3": sfbrm100VlanMemTagPort3,
       "sfbrm100VlanMemTagPort4": sfbrm100VlanMemTagPort4,
       "sfbrm100VlanMemTagPort5": sfbrm100VlanMemTagPort5,
       "sfbrm100VlanMemTagPort6": sfbrm100VlanMemTagPort6,
       "sfbrm100VlanMemTagPort7": sfbrm100VlanMemTagPort7,
       "sfbrm100VlanMemTagPort8": sfbrm100VlanMemTagPort8,
       "sfbrm100VlanMemTagPort9": sfbrm100VlanMemTagPort9,
       "sfbrm100VlanMemTagPort10": sfbrm100VlanMemTagPort10,
       "sfbrm100VlanEntryStatus": sfbrm100VlanEntryStatus}
)
