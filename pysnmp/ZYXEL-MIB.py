# SNMP MIB module (ZYXEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:20 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_Prestige_ObjectIdentity = ObjectIdentity
prestige = _Prestige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2)
)
_PSysVariables_ObjectIdentity = ObjectIdentity
pSysVariables = _PSysVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1)
)


class _PSysRasSWVersion_Type(DisplayString):
    """Custom type pSysRasSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PSysRasSWVersion_Type.__name__ = "DisplayString"
_PSysRasSWVersion_Object = MibScalar
pSysRasSWVersion = _PSysRasSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1),
    _PSysRasSWVersion_Type()
)
pSysRasSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSysRasSWVersion.setStatus("mandatory")


class _PSysIsdnFWVersion_Type(DisplayString):
    """Custom type pSysIsdnFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PSysIsdnFWVersion_Type.__name__ = "DisplayString"
_PSysIsdnFWVersion_Object = MibScalar
pSysIsdnFWVersion = _PSysIsdnFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2),
    _PSysIsdnFWVersion_Type()
)
pSysIsdnFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSysIsdnFWVersion.setStatus("mandatory")


class _PSysRouteIP_Type(Integer32):
    """Custom type pSysRouteIP based on Integer32"""
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


_PSysRouteIP_Type.__name__ = "Integer32"
_PSysRouteIP_Object = MibScalar
pSysRouteIP = _PSysRouteIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3),
    _PSysRouteIP_Type()
)
pSysRouteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSysRouteIP.setStatus("mandatory")


class _PSysRouteIPX_Type(Integer32):
    """Custom type pSysRouteIPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PSysRouteIPX_Type.__name__ = "Integer32"
_PSysRouteIPX_Object = MibScalar
pSysRouteIPX = _PSysRouteIPX_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4),
    _PSysRouteIPX_Type()
)
pSysRouteIPX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSysRouteIPX.setStatus("mandatory")


class _PSysRouteAPT_Type(Integer32):
    """Custom type pSysRouteAPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PSysRouteAPT_Type.__name__ = "Integer32"
_PSysRouteAPT_Object = MibScalar
pSysRouteAPT = _PSysRouteAPT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5),
    _PSysRouteAPT_Type()
)
pSysRouteAPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSysRouteAPT.setStatus("mandatory")


class _PSysBridge_Type(Integer32):
    """Custom type pSysBridge based on Integer32"""
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


_PSysBridge_Type.__name__ = "Integer32"
_PSysBridge_Object = MibScalar
pSysBridge = _PSysBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 6),
    _PSysBridge_Type()
)
pSysBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSysBridge.setStatus("mandatory")
_PBRIVariables_ObjectIdentity = ObjectIdentity
pBRIVariables = _PBRIVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2)
)


class _PBRISwitchType_Type(Integer32):
    """Custom type pBRISwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("at-tni-1", 8),
          ("at-tp2m", 9),
          ("at-tp2p", 5),
          ("dss1", 3),
          ("ltr6", 4),
          ("nortelcustom", 1),
          ("nortelni-1", 10))
    )


_PBRISwitchType_Type.__name__ = "Integer32"
_PBRISwitchType_Object = MibScalar
pBRISwitchType = _PBRISwitchType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 1),
    _PBRISwitchType_Type()
)
pBRISwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBRISwitchType.setStatus("mandatory")


class _PBChannelUsage_Type(Integer32):
    """Custom type pBChannelUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch-switch", 2),
          ("switch-unused", 1))
    )


_PBChannelUsage_Type.__name__ = "Integer32"
_PBChannelUsage_Object = MibScalar
pBChannelUsage = _PBChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 2),
    _PBChannelUsage_Type()
)
pBChannelUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBChannelUsage.setStatus("mandatory")


class _P1stPhoneNumber_Type(DisplayString):
    """Custom type p1stPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_P1stPhoneNumber_Type.__name__ = "DisplayString"
_P1stPhoneNumber_Object = MibScalar
p1stPhoneNumber = _P1stPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 3),
    _P1stPhoneNumber_Type()
)
p1stPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1stPhoneNumber.setStatus("mandatory")


class _P1stSpidNumber_Type(DisplayString):
    """Custom type p1stSpidNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_P1stSpidNumber_Type.__name__ = "DisplayString"
_P1stSpidNumber_Object = MibScalar
p1stSpidNumber = _P1stSpidNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 4),
    _P1stSpidNumber_Type()
)
p1stSpidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1stSpidNumber.setStatus("mandatory")


class _P1stAnalogCall_Type(Integer32):
    """Custom type p1stAnalogCall based on Integer32"""
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
        *(("data", 4),
          ("modem", 2),
          ("none", 1),
          ("voice", 3))
    )


_P1stAnalogCall_Type.__name__ = "Integer32"
_P1stAnalogCall_Object = MibScalar
p1stAnalogCall = _P1stAnalogCall_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 5),
    _P1stAnalogCall_Type()
)
p1stAnalogCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1stAnalogCall.setStatus("mandatory")


class _P2ndPhoneNumber_Type(DisplayString):
    """Custom type p2ndPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_P2ndPhoneNumber_Type.__name__ = "DisplayString"
_P2ndPhoneNumber_Object = MibScalar
p2ndPhoneNumber = _P2ndPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 6),
    _P2ndPhoneNumber_Type()
)
p2ndPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2ndPhoneNumber.setStatus("mandatory")


class _P2ndSpidNumber_Type(DisplayString):
    """Custom type p2ndSpidNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_P2ndSpidNumber_Type.__name__ = "DisplayString"
_P2ndSpidNumber_Object = MibScalar
p2ndSpidNumber = _P2ndSpidNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 7),
    _P2ndSpidNumber_Type()
)
p2ndSpidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2ndSpidNumber.setStatus("mandatory")


class _P2ndAnalogCall_Type(Integer32):
    """Custom type p2ndAnalogCall based on Integer32"""
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
        *(("data", 4),
          ("modem", 2),
          ("na", 5),
          ("none", 1),
          ("voice", 3))
    )


_P2ndAnalogCall_Type.__name__ = "Integer32"
_P2ndAnalogCall_Object = MibScalar
p2ndAnalogCall = _P2ndAnalogCall_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 2, 8),
    _P2ndAnalogCall_Type()
)
p2ndAnalogCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2ndAnalogCall.setStatus("mandatory")
_PIPXVariables_ObjectIdentity = ObjectIdentity
pIPXVariables = _PIPXVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3)
)


class _PFrameType8022_Type(Integer32):
    """Custom type pFrameType8022 based on Integer32"""
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


_PFrameType8022_Type.__name__ = "Integer32"
_PFrameType8022_Object = MibScalar
pFrameType8022 = _PFrameType8022_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 1),
    _PFrameType8022_Type()
)
pFrameType8022.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFrameType8022.setStatus("mandatory")


class _PSeedRouter8022_Type(Integer32):
    """Custom type pSeedRouter8022 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PSeedRouter8022_Type.__name__ = "Integer32"
_PSeedRouter8022_Object = MibScalar
pSeedRouter8022 = _PSeedRouter8022_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 2),
    _PSeedRouter8022_Type()
)
pSeedRouter8022.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSeedRouter8022.setStatus("mandatory")


class _PNetworkNumber8022_Type(DisplayString):
    """Custom type pNetworkNumber8022 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PNetworkNumber8022_Type.__name__ = "DisplayString"
_PNetworkNumber8022_Object = MibScalar
pNetworkNumber8022 = _PNetworkNumber8022_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 3),
    _PNetworkNumber8022_Type()
)
pNetworkNumber8022.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetworkNumber8022.setStatus("mandatory")


class _PFrameType8023_Type(Integer32):
    """Custom type pFrameType8023 based on Integer32"""
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


_PFrameType8023_Type.__name__ = "Integer32"
_PFrameType8023_Object = MibScalar
pFrameType8023 = _PFrameType8023_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 4),
    _PFrameType8023_Type()
)
pFrameType8023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFrameType8023.setStatus("mandatory")


class _PSeedRouter8023_Type(Integer32):
    """Custom type pSeedRouter8023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PSeedRouter8023_Type.__name__ = "Integer32"
_PSeedRouter8023_Object = MibScalar
pSeedRouter8023 = _PSeedRouter8023_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 5),
    _PSeedRouter8023_Type()
)
pSeedRouter8023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSeedRouter8023.setStatus("mandatory")


class _PNetworkNumber8023_Type(DisplayString):
    """Custom type pNetworkNumber8023 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PNetworkNumber8023_Type.__name__ = "DisplayString"
_PNetworkNumber8023_Object = MibScalar
pNetworkNumber8023 = _PNetworkNumber8023_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 6),
    _PNetworkNumber8023_Type()
)
pNetworkNumber8023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetworkNumber8023.setStatus("mandatory")


class _PFrameTypeEthernetII_Type(Integer32):
    """Custom type pFrameTypeEthernetII based on Integer32"""
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


_PFrameTypeEthernetII_Type.__name__ = "Integer32"
_PFrameTypeEthernetII_Object = MibScalar
pFrameTypeEthernetII = _PFrameTypeEthernetII_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 7),
    _PFrameTypeEthernetII_Type()
)
pFrameTypeEthernetII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFrameTypeEthernetII.setStatus("mandatory")


class _PSeedRouterEthernetII_Type(Integer32):
    """Custom type pSeedRouterEthernetII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PSeedRouterEthernetII_Type.__name__ = "Integer32"
_PSeedRouterEthernetII_Object = MibScalar
pSeedRouterEthernetII = _PSeedRouterEthernetII_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 8),
    _PSeedRouterEthernetII_Type()
)
pSeedRouterEthernetII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSeedRouterEthernetII.setStatus("mandatory")


class _PNetworkNumberEthernetII_Type(DisplayString):
    """Custom type pNetworkNumberEthernetII based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PNetworkNumberEthernetII_Type.__name__ = "DisplayString"
_PNetworkNumberEthernetII_Object = MibScalar
pNetworkNumberEthernetII = _PNetworkNumberEthernetII_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 9),
    _PNetworkNumberEthernetII_Type()
)
pNetworkNumberEthernetII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetworkNumberEthernetII.setStatus("mandatory")


class _PFrameTypeSnap_Type(Integer32):
    """Custom type pFrameTypeSnap based on Integer32"""
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


_PFrameTypeSnap_Type.__name__ = "Integer32"
_PFrameTypeSnap_Object = MibScalar
pFrameTypeSnap = _PFrameTypeSnap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 10),
    _PFrameTypeSnap_Type()
)
pFrameTypeSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFrameTypeSnap.setStatus("mandatory")


class _PSeedRouterSnap_Type(Integer32):
    """Custom type pSeedRouterSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PSeedRouterSnap_Type.__name__ = "Integer32"
_PSeedRouterSnap_Object = MibScalar
pSeedRouterSnap = _PSeedRouterSnap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 11),
    _PSeedRouterSnap_Type()
)
pSeedRouterSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSeedRouterSnap.setStatus("mandatory")


class _PNetworkNumberSnap_Type(DisplayString):
    """Custom type pNetworkNumberSnap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PNetworkNumberSnap_Type.__name__ = "DisplayString"
_PNetworkNumberSnap_Object = MibScalar
pNetworkNumberSnap = _PNetworkNumberSnap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 12),
    _PNetworkNumberSnap_Type()
)
pNetworkNumberSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetworkNumberSnap.setStatus("mandatory")
_PIPXRouteTable_Object = MibTable
pIPXRouteTable = _PIPXRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13)
)
if mibBuilder.loadTexts:
    pIPXRouteTable.setStatus("mandatory")
_PipxRouteEntry_Object = MibTableRow
pipxRouteEntry = _PipxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1)
)
pipxRouteEntry.setIndexNames(
    (0, "ZYXEL-MIB", "pIpxRtIndex"),
)
if mibBuilder.loadTexts:
    pipxRouteEntry.setStatus("mandatory")
_PIpxRtIndex_Type = Integer32
_PIpxRtIndex_Object = MibTableColumn
pIpxRtIndex = _PIpxRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 1),
    _PIpxRtIndex_Type()
)
pIpxRtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtIndex.setStatus("mandatory")


class _PIpxRtServerName_Type(DisplayString):
    """Custom type pIpxRtServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PIpxRtServerName_Type.__name__ = "DisplayString"
_PIpxRtServerName_Object = MibTableColumn
pIpxRtServerName = _PIpxRtServerName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 2),
    _PIpxRtServerName_Type()
)
pIpxRtServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtServerName.setStatus("mandatory")


class _PIpxRtActive_Type(Integer32):
    """Custom type pIpxRtActive based on Integer32"""
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


_PIpxRtActive_Type.__name__ = "Integer32"
_PIpxRtActive_Object = MibTableColumn
pIpxRtActive = _PIpxRtActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 3),
    _PIpxRtActive_Type()
)
pIpxRtActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtActive.setStatus("mandatory")


class _PIpxRtNetworkNumber_Type(DisplayString):
    """Custom type pIpxRtNetworkNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PIpxRtNetworkNumber_Type.__name__ = "DisplayString"
_PIpxRtNetworkNumber_Object = MibTableColumn
pIpxRtNetworkNumber = _PIpxRtNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 4),
    _PIpxRtNetworkNumber_Type()
)
pIpxRtNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtNetworkNumber.setStatus("mandatory")


class _PIpxRtNodeNumber_Type(DisplayString):
    """Custom type pIpxRtNodeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PIpxRtNodeNumber_Type.__name__ = "DisplayString"
_PIpxRtNodeNumber_Object = MibTableColumn
pIpxRtNodeNumber = _PIpxRtNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 5),
    _PIpxRtNodeNumber_Type()
)
pIpxRtNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtNodeNumber.setStatus("mandatory")


class _PIpxRtSocketNumber_Type(DisplayString):
    """Custom type pIpxRtSocketNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PIpxRtSocketNumber_Type.__name__ = "DisplayString"
_PIpxRtSocketNumber_Object = MibTableColumn
pIpxRtSocketNumber = _PIpxRtSocketNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 6),
    _PIpxRtSocketNumber_Type()
)
pIpxRtSocketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtSocketNumber.setStatus("mandatory")


class _PIpxRtTypeNumber_Type(DisplayString):
    """Custom type pIpxRtTypeNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PIpxRtTypeNumber_Type.__name__ = "DisplayString"
_PIpxRtTypeNumber_Object = MibTableColumn
pIpxRtTypeNumber = _PIpxRtTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 7),
    _PIpxRtTypeNumber_Type()
)
pIpxRtTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtTypeNumber.setStatus("mandatory")
_PIpxRtHopCount_Type = Integer32
_PIpxRtHopCount_Object = MibTableColumn
pIpxRtHopCount = _PIpxRtHopCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 8),
    _PIpxRtHopCount_Type()
)
pIpxRtHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtHopCount.setStatus("mandatory")
_PIpxRtTickCount_Type = Integer32
_PIpxRtTickCount_Object = MibTableColumn
pIpxRtTickCount = _PIpxRtTickCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 9),
    _PIpxRtTickCount_Type()
)
pIpxRtTickCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtTickCount.setStatus("mandatory")
_PIpxRtGatewayNode_Type = Integer32
_PIpxRtGatewayNode_Object = MibTableColumn
pIpxRtGatewayNode = _PIpxRtGatewayNode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 3, 13, 1, 10),
    _PIpxRtGatewayNode_Type()
)
pIpxRtGatewayNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIpxRtGatewayNode.setStatus("mandatory")
_PAPTVariables_ObjectIdentity = ObjectIdentity
pAPTVariables = _PAPTVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4)
)


class _PAPTSeedRouter_Type(Integer32):
    """Custom type pAPTSeedRouter based on Integer32"""
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


_PAPTSeedRouter_Type.__name__ = "Integer32"
_PAPTSeedRouter_Object = MibScalar
pAPTSeedRouter = _PAPTSeedRouter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 1),
    _PAPTSeedRouter_Type()
)
pAPTSeedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPTSeedRouter.setStatus("mandatory")


class _PAPTNetworkMin_Type(Integer32):
    """Custom type pAPTNetworkMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65536
        )
    )
    namedValues = NamedValues(
        ("na", 65536)
    )


_PAPTNetworkMin_Type.__name__ = "Integer32"
_PAPTNetworkMin_Object = MibScalar
pAPTNetworkMin = _PAPTNetworkMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 2),
    _PAPTNetworkMin_Type()
)
pAPTNetworkMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPTNetworkMin.setStatus("mandatory")


class _PAPTNetworkMax_Type(Integer32):
    """Custom type pAPTNetworkMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65536
        )
    )
    namedValues = NamedValues(
        ("na", 65536)
    )


_PAPTNetworkMax_Type.__name__ = "Integer32"
_PAPTNetworkMax_Object = MibScalar
pAPTNetworkMax = _PAPTNetworkMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 3),
    _PAPTNetworkMax_Type()
)
pAPTNetworkMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPTNetworkMax.setStatus("mandatory")


class _PAPT1stZoneName_Type(DisplayString):
    """Custom type pAPT1stZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PAPT1stZoneName_Type.__name__ = "DisplayString"
_PAPT1stZoneName_Object = MibScalar
pAPT1stZoneName = _PAPT1stZoneName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 4),
    _PAPT1stZoneName_Type()
)
pAPT1stZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPT1stZoneName.setStatus("mandatory")


class _PAPT2ndZoneName_Type(DisplayString):
    """Custom type pAPT2ndZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PAPT2ndZoneName_Type.__name__ = "DisplayString"
_PAPT2ndZoneName_Object = MibScalar
pAPT2ndZoneName = _PAPT2ndZoneName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 5),
    _PAPT2ndZoneName_Type()
)
pAPT2ndZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPT2ndZoneName.setStatus("mandatory")
_PAPTZipTimeout_Type = Integer32
_PAPTZipTimeout_Object = MibScalar
pAPTZipTimeout = _PAPTZipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 6),
    _PAPTZipTimeout_Type()
)
pAPTZipTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAPTZipTimeout.setStatus("mandatory")
_PAPTRouteTable_Object = MibTable
pAPTRouteTable = _PAPTRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7)
)
if mibBuilder.loadTexts:
    pAPTRouteTable.setStatus("mandatory")
_PaptRouteEntry_Object = MibTableRow
paptRouteEntry = _PaptRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1)
)
paptRouteEntry.setIndexNames(
    (0, "ZYXEL-MIB", "pAptRtIndex"),
)
if mibBuilder.loadTexts:
    paptRouteEntry.setStatus("mandatory")
_PAptRtIndex_Type = Integer32
_PAptRtIndex_Object = MibTableColumn
pAptRtIndex = _PAptRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 1),
    _PAptRtIndex_Type()
)
pAptRtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRtIndex.setStatus("mandatory")


class _PAptRt1stZoneName_Type(DisplayString):
    """Custom type pAptRt1stZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PAptRt1stZoneName_Type.__name__ = "DisplayString"
_PAptRt1stZoneName_Object = MibTableColumn
pAptRt1stZoneName = _PAptRt1stZoneName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 2),
    _PAptRt1stZoneName_Type()
)
pAptRt1stZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRt1stZoneName.setStatus("mandatory")


class _PAptRt2ndZoneName_Type(DisplayString):
    """Custom type pAptRt2ndZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PAptRt2ndZoneName_Type.__name__ = "DisplayString"
_PAptRt2ndZoneName_Object = MibTableColumn
pAptRt2ndZoneName = _PAptRt2ndZoneName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 3),
    _PAptRt2ndZoneName_Type()
)
pAptRt2ndZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRt2ndZoneName.setStatus("mandatory")
_PAptRtNetworkMin_Type = Integer32
_PAptRtNetworkMin_Object = MibTableColumn
pAptRtNetworkMin = _PAptRtNetworkMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 4),
    _PAptRtNetworkMin_Type()
)
pAptRtNetworkMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRtNetworkMin.setStatus("mandatory")
_PAptRtNetworkMax_Type = Integer32
_PAptRtNetworkMax_Object = MibTableColumn
pAptRtNetworkMax = _PAptRtNetworkMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 5),
    _PAptRtNetworkMax_Type()
)
pAptRtNetworkMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRtNetworkMax.setStatus("mandatory")


class _PAptRtActive_Type(Integer32):
    """Custom type pAptRtActive based on Integer32"""
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


_PAptRtActive_Type.__name__ = "Integer32"
_PAptRtActive_Object = MibTableColumn
pAptRtActive = _PAptRtActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 6),
    _PAptRtActive_Type()
)
pAptRtActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRtActive.setStatus("mandatory")
_PAptRtMetric_Type = Integer32
_PAptRtMetric_Object = MibTableColumn
pAptRtMetric = _PAptRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 7),
    _PAptRtMetric_Type()
)
pAptRtMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRtMetric.setStatus("mandatory")
_PAptRtGatewayNode_Type = Integer32
_PAptRtGatewayNode_Object = MibTableColumn
pAptRtGatewayNode = _PAptRtGatewayNode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 4, 7, 1, 8),
    _PAptRtGatewayNode_Type()
)
pAptRtGatewayNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAptRtGatewayNode.setStatus("mandatory")
_PBRGVariables_ObjectIdentity = ObjectIdentity
pBRGVariables = _PBRGVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5)
)


class _PBRGHandleIpx_Type(Integer32):
    """Custom type pBRGHandleIpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("none", 1),
          ("server", 3))
    )


_PBRGHandleIpx_Type.__name__ = "Integer32"
_PBRGHandleIpx_Object = MibScalar
pBRGHandleIpx = _PBRGHandleIpx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 1),
    _PBRGHandleIpx_Type()
)
pBRGHandleIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBRGHandleIpx.setStatus("mandatory")
_PBRGRouteTable_Object = MibTable
pBRGRouteTable = _PBRGRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    pBRGRouteTable.setStatus("mandatory")
_PbrgRouteEntry_Object = MibTableRow
pbrgRouteEntry = _PbrgRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1)
)
pbrgRouteEntry.setIndexNames(
    (0, "ZYXEL-MIB", "pBrgRtIndex"),
)
if mibBuilder.loadTexts:
    pbrgRouteEntry.setStatus("mandatory")
_PBrgRtIndex_Type = Integer32
_PBrgRtIndex_Object = MibTableColumn
pBrgRtIndex = _PBrgRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1, 1),
    _PBrgRtIndex_Type()
)
pBrgRtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBrgRtIndex.setStatus("mandatory")


class _PBrgRtRouteName_Type(DisplayString):
    """Custom type pBrgRtRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PBrgRtRouteName_Type.__name__ = "DisplayString"
_PBrgRtRouteName_Object = MibTableColumn
pBrgRtRouteName = _PBrgRtRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1, 2),
    _PBrgRtRouteName_Type()
)
pBrgRtRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBrgRtRouteName.setStatus("mandatory")


class _PBrgRtActive_Type(Integer32):
    """Custom type pBrgRtActive based on Integer32"""
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


_PBrgRtActive_Type.__name__ = "Integer32"
_PBrgRtActive_Object = MibTableColumn
pBrgRtActive = _PBrgRtActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1, 3),
    _PBrgRtActive_Type()
)
pBrgRtActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBrgRtActive.setStatus("mandatory")


class _PBrgRtEtherAddress_Type(DisplayString):
    """Custom type pBrgRtEtherAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PBrgRtEtherAddress_Type.__name__ = "DisplayString"
_PBrgRtEtherAddress_Object = MibTableColumn
pBrgRtEtherAddress = _PBrgRtEtherAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1, 4),
    _PBrgRtEtherAddress_Type()
)
pBrgRtEtherAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBrgRtEtherAddress.setStatus("mandatory")
_PBrgRtIpAddress_Type = IpAddress
_PBrgRtIpAddress_Object = MibTableColumn
pBrgRtIpAddress = _PBrgRtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1, 5),
    _PBrgRtIpAddress_Type()
)
pBrgRtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBrgRtIpAddress.setStatus("mandatory")
_PBrgRtGatewayNode_Type = Integer32
_PBrgRtGatewayNode_Object = MibTableColumn
pBrgRtGatewayNode = _PBrgRtGatewayNode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 5, 2, 1, 6),
    _PBrgRtGatewayNode_Type()
)
pBrgRtGatewayNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBrgRtGatewayNode.setStatus("mandatory")
_PDialInVariables_ObjectIdentity = ObjectIdentity
pDialInVariables = _PDialInVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6)
)


class _PDIClidAuthen_Type(Integer32):
    """Custom type pDIClidAuthen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("preferred", 3),
          ("required", 2))
    )


_PDIClidAuthen_Type.__name__ = "Integer32"
_PDIClidAuthen_Object = MibScalar
pDIClidAuthen = _PDIClidAuthen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 1),
    _PDIClidAuthen_Type()
)
pDIClidAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIClidAuthen.setStatus("mandatory")


class _PDIRecvAuthen_Type(Integer32):
    """Custom type pDIRecvAuthen based on Integer32"""
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
        *(("chap", 2),
          ("chap-pap", 1),
          ("none", 4),
          ("pap", 3))
    )


_PDIRecvAuthen_Type.__name__ = "Integer32"
_PDIRecvAuthen_Object = MibScalar
pDIRecvAuthen = _PDIRecvAuthen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 2),
    _PDIRecvAuthen_Type()
)
pDIRecvAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIRecvAuthen.setStatus("mandatory")


class _PDILinkCompression_Type(Integer32):
    """Custom type pDILinkCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("stac", 2),
          ("v42bis", 3))
    )


_PDILinkCompression_Type.__name__ = "Integer32"
_PDILinkCompression_Object = MibScalar
pDILinkCompression = _PDILinkCompression_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 3),
    _PDILinkCompression_Type()
)
pDILinkCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDILinkCompression.setStatus("mandatory")


class _PDIMaxTransferRate_Type(Integer32):
    """Custom type pDIMaxTransferRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-128k", 1),
          ("speed-64k", 2))
    )


_PDIMaxTransferRate_Type.__name__ = "Integer32"
_PDIMaxTransferRate_Object = MibScalar
pDIMaxTransferRate = _PDIMaxTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 4),
    _PDIMaxTransferRate_Type()
)
pDIMaxTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIMaxTransferRate.setStatus("mandatory")
_PDIIdleTimeout_Type = Integer32
_PDIIdleTimeout_Object = MibScalar
pDIIdleTimeout = _PDIIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 5),
    _PDIIdleTimeout_Type()
)
pDIIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIdleTimeout.setStatus("mandatory")


class _PDIIpAddressSupply_Type(Integer32):
    """Custom type pDIIpAddressSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pool", 2),
          ("user", 1))
    )


_PDIIpAddressSupply_Type.__name__ = "Integer32"
_PDIIpAddressSupply_Object = MibScalar
pDIIpAddressSupply = _PDIIpAddressSupply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 6),
    _PDIIpAddressSupply_Type()
)
pDIIpAddressSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIpAddressSupply.setStatus("mandatory")
_PDIIpPoolStartAddress_Type = IpAddress
_PDIIpPoolStartAddress_Object = MibScalar
pDIIpPoolStartAddress = _PDIIpPoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 7),
    _PDIIpPoolStartAddress_Type()
)
pDIIpPoolStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIpPoolStartAddress.setStatus("mandatory")


class _PDIIpPoolCount_Type(Integer32):
    """Custom type pDIIpPoolCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1000
        )
    )
    namedValues = NamedValues(
        ("na", 1000)
    )


_PDIIpPoolCount_Type.__name__ = "Integer32"
_PDIIpPoolCount_Object = MibScalar
pDIIpPoolCount = _PDIIpPoolCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 8),
    _PDIIpPoolCount_Type()
)
pDIIpPoolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIpPoolCount.setStatus("mandatory")


class _PDIIpxPool_Type(Integer32):
    """Custom type pDIIpxPool based on Integer32"""
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


_PDIIpxPool_Type.__name__ = "Integer32"
_PDIIpxPool_Object = MibScalar
pDIIpxPool = _PDIIpxPool_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 9),
    _PDIIpxPool_Type()
)
pDIIpxPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIpxPool.setStatus("mandatory")


class _PDIIpxPoolStartNetNumber_Type(DisplayString):
    """Custom type pDIIpxPoolStartNetNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PDIIpxPoolStartNetNumber_Type.__name__ = "DisplayString"
_PDIIpxPoolStartNetNumber_Object = MibScalar
pDIIpxPoolStartNetNumber = _PDIIpxPoolStartNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 10),
    _PDIIpxPoolStartNetNumber_Type()
)
pDIIpxPoolStartNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIpxPoolStartNetNumber.setStatus("mandatory")


class _PDIIpxPoolCount_Type(Integer32):
    """Custom type pDIIpxPoolCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1000
        )
    )
    namedValues = NamedValues(
        ("na", 1000)
    )


_PDIIpxPoolCount_Type.__name__ = "Integer32"
_PDIIpxPoolCount_Object = MibScalar
pDIIpxPoolCount = _PDIIpxPoolCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 6, 11),
    _PDIIpxPoolCount_Type()
)
pDIIpxPoolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDIIpxPoolCount.setStatus("mandatory")
_PRemoteNodeVariables_ObjectIdentity = ObjectIdentity
pRemoteNodeVariables = _PRemoteNodeVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7)
)
_PRemoteNodeTable_Object = MibTable
pRemoteNodeTable = _PRemoteNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    pRemoteNodeTable.setStatus("mandatory")
_PremoteNodeEntry_Object = MibTableRow
premoteNodeEntry = _PremoteNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1)
)
premoteNodeEntry.setIndexNames(
    (0, "ZYXEL-MIB", "pRNIndex"),
)
if mibBuilder.loadTexts:
    premoteNodeEntry.setStatus("mandatory")
_PRNIndex_Type = Integer32
_PRNIndex_Object = MibTableColumn
pRNIndex = _PRNIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 1),
    _PRNIndex_Type()
)
pRNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNIndex.setStatus("mandatory")


class _PRNName_Type(DisplayString):
    """Custom type pRNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRNName_Type.__name__ = "DisplayString"
_PRNName_Object = MibTableColumn
pRNName = _PRNName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 2),
    _PRNName_Type()
)
pRNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNName.setStatus("mandatory")


class _PRNActive_Type(Integer32):
    """Custom type pRNActive based on Integer32"""
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


_PRNActive_Type.__name__ = "Integer32"
_PRNActive_Object = MibTableColumn
pRNActive = _PRNActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 3),
    _PRNActive_Type()
)
pRNActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNActive.setStatus("mandatory")


class _PRNCallDirection_Type(Integer32):
    """Custom type pRNCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_PRNCallDirection_Type.__name__ = "Integer32"
_PRNCallDirection_Object = MibTableColumn
pRNCallDirection = _PRNCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 4),
    _PRNCallDirection_Type()
)
pRNCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNCallDirection.setStatus("mandatory")


class _PRNRemLogin_Type(DisplayString):
    """Custom type pRNRemLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRNRemLogin_Type.__name__ = "DisplayString"
_PRNRemLogin_Object = MibTableColumn
pRNRemLogin = _PRNRemLogin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 5),
    _PRNRemLogin_Type()
)
pRNRemLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNRemLogin.setStatus("mandatory")


class _PRNRemClid_Type(DisplayString):
    """Custom type pRNRemClid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRNRemClid_Type.__name__ = "DisplayString"
_PRNRemClid_Object = MibTableColumn
pRNRemClid = _PRNRemClid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 6),
    _PRNRemClid_Type()
)
pRNRemClid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNRemClid.setStatus("mandatory")


class _PRNCallBack_Type(Integer32):
    """Custom type pRNCallBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("no", 1),
          ("yes", 2))
    )


_PRNCallBack_Type.__name__ = "Integer32"
_PRNCallBack_Object = MibTableColumn
pRNCallBack = _PRNCallBack_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 7),
    _PRNCallBack_Type()
)
pRNCallBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNCallBack.setStatus("mandatory")


class _PRNMyLogin_Type(DisplayString):
    """Custom type pRNMyLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRNMyLogin_Type.__name__ = "DisplayString"
_PRNMyLogin_Object = MibTableColumn
pRNMyLogin = _PRNMyLogin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 8),
    _PRNMyLogin_Type()
)
pRNMyLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNMyLogin.setStatus("mandatory")


class _PRN1stPhoneNumber_Type(DisplayString):
    """Custom type pRN1stPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRN1stPhoneNumber_Type.__name__ = "DisplayString"
_PRN1stPhoneNumber_Object = MibTableColumn
pRN1stPhoneNumber = _PRN1stPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 9),
    _PRN1stPhoneNumber_Type()
)
pRN1stPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRN1stPhoneNumber.setStatus("mandatory")


class _PRN2ndPhoneNumber_Type(DisplayString):
    """Custom type pRN2ndPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRN2ndPhoneNumber_Type.__name__ = "DisplayString"
_PRN2ndPhoneNumber_Object = MibTableColumn
pRN2ndPhoneNumber = _PRN2ndPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 10),
    _PRN2ndPhoneNumber_Type()
)
pRN2ndPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRN2ndPhoneNumber.setStatus("mandatory")


class _PRNRouteType_Type(Integer32):
    """Custom type pRNRouteType based on Integer32"""
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
        *(("appletalk", 4),
          ("ip", 2),
          ("ip-appletalk", 6),
          ("ip-ipx", 5),
          ("ip-ipx-appletalk", 8),
          ("ipx", 3),
          ("ipx-appletalk", 7),
          ("none", 1))
    )


_PRNRouteType_Type.__name__ = "Integer32"
_PRNRouteType_Object = MibTableColumn
pRNRouteType = _PRNRouteType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 11),
    _PRNRouteType_Type()
)
pRNRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNRouteType.setStatus("mandatory")


class _PRNBridgeEnabled_Type(Integer32):
    """Custom type pRNBridgeEnabled based on Integer32"""
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


_PRNBridgeEnabled_Type.__name__ = "Integer32"
_PRNBridgeEnabled_Object = MibTableColumn
pRNBridgeEnabled = _PRNBridgeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 12),
    _PRNBridgeEnabled_Type()
)
pRNBridgeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNBridgeEnabled.setStatus("mandatory")


class _PRNEncapsulation_Type(Integer32):
    """Custom type pRNEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascend", 2),
          ("microsoft", 3),
          ("ppp", 1))
    )


_PRNEncapsulation_Type.__name__ = "Integer32"
_PRNEncapsulation_Object = MibTableColumn
pRNEncapsulation = _PRNEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 13),
    _PRNEncapsulation_Type()
)
pRNEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNEncapsulation.setStatus("mandatory")
_PRNIpAddress_Type = IpAddress
_PRNIpAddress_Object = MibTableColumn
pRNIpAddress = _PRNIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 14),
    _PRNIpAddress_Type()
)
pRNIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNIpAddress.setStatus("mandatory")


class _PRNTransferRate_Type(Integer32):
    """Custom type pRNTransferRate based on Integer32"""
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
        *(("speed-128k", 5),
          ("speed-2-2M", 1),
          ("speed-56k-only", 2),
          ("speed-64k", 4),
          ("speed-Modem", 3))
    )


_PRNTransferRate_Type.__name__ = "Integer32"
_PRNTransferRate_Object = MibTableColumn
pRNTransferRate = _PRNTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 15),
    _PRNTransferRate_Type()
)
pRNTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNTransferRate.setStatus("mandatory")
_PRNIdleTimeout_Type = Integer32
_PRNIdleTimeout_Object = MibTableColumn
pRNIdleTimeout = _PRNIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 7, 1, 1, 16),
    _PRNIdleTimeout_Type()
)
pRNIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRNIdleTimeout.setStatus("mandatory")
_PRemoteUserVariables_ObjectIdentity = ObjectIdentity
pRemoteUserVariables = _PRemoteUserVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8)
)
_PRemoteUserTable_Object = MibTable
pRemoteUserTable = _PRemoteUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    pRemoteUserTable.setStatus("mandatory")
_PremoteUserEntry_Object = MibTableRow
premoteUserEntry = _PremoteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1)
)
premoteUserEntry.setIndexNames(
    (0, "ZYXEL-MIB", "pRUIndex"),
)
if mibBuilder.loadTexts:
    premoteUserEntry.setStatus("mandatory")
_PRUIndex_Type = Integer32
_PRUIndex_Object = MibTableColumn
pRUIndex = _PRUIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 1),
    _PRUIndex_Type()
)
pRUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUIndex.setStatus("mandatory")


class _PRUName_Type(DisplayString):
    """Custom type pRUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRUName_Type.__name__ = "DisplayString"
_PRUName_Object = MibTableColumn
pRUName = _PRUName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 2),
    _PRUName_Type()
)
pRUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUName.setStatus("mandatory")


class _PRUActive_Type(Integer32):
    """Custom type pRUActive based on Integer32"""
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


_PRUActive_Type.__name__ = "Integer32"
_PRUActive_Object = MibTableColumn
pRUActive = _PRUActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 3),
    _PRUActive_Type()
)
pRUActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUActive.setStatus("mandatory")


class _PRUCallBack_Type(Integer32):
    """Custom type pRUCallBack based on Integer32"""
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


_PRUCallBack_Type.__name__ = "Integer32"
_PRUCallBack_Object = MibTableColumn
pRUCallBack = _PRUCallBack_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 4),
    _PRUCallBack_Type()
)
pRUCallBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUCallBack.setStatus("mandatory")


class _PRUCallBackNumber_Type(DisplayString):
    """Custom type pRUCallBackNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRUCallBackNumber_Type.__name__ = "DisplayString"
_PRUCallBackNumber_Object = MibTableColumn
pRUCallBackNumber = _PRUCallBackNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 5),
    _PRUCallBackNumber_Type()
)
pRUCallBackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUCallBackNumber.setStatus("mandatory")


class _PRUCallBackOverride_Type(Integer32):
    """Custom type pRUCallBackOverride based on Integer32"""
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


_PRUCallBackOverride_Type.__name__ = "Integer32"
_PRUCallBackOverride_Object = MibTableColumn
pRUCallBackOverride = _PRUCallBackOverride_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 6),
    _PRUCallBackOverride_Type()
)
pRUCallBackOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUCallBackOverride.setStatus("mandatory")


class _PRUClid_Type(DisplayString):
    """Custom type pRUClid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PRUClid_Type.__name__ = "DisplayString"
_PRUClid_Object = MibTableColumn
pRUClid = _PRUClid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 7),
    _PRUClid_Type()
)
pRUClid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUClid.setStatus("mandatory")
_PRUIdleTimeout_Type = Integer32
_PRUIdleTimeout_Object = MibTableColumn
pRUIdleTimeout = _PRUIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 8, 1, 1, 8),
    _PRUIdleTimeout_Type()
)
pRUIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRUIdleTimeout.setStatus("mandatory")
_ZyxelTraps_ObjectIdentity = ObjectIdentity
zyxelTraps = _ZyxelTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 9)
)
_WhyReboot_Type = DisplayString
_WhyReboot_Object = MibScalar
whyReboot = _WhyReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 9, 1),
    _WhyReboot_Type()
)
whyReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whyReboot.setStatus("mandatory")

# Managed Objects groups


# Notification objects

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 0, 1)
)
reboot.setObjects(
    ("ZYXEL-MIB", "whyReboot")
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MIB",
    **{"DisplayString": DisplayString,
       "zyxel": zyxel,
       "reboot": reboot,
       "products": products,
       "prestige": prestige,
       "pSysVariables": pSysVariables,
       "pSysRasSWVersion": pSysRasSWVersion,
       "pSysIsdnFWVersion": pSysIsdnFWVersion,
       "pSysRouteIP": pSysRouteIP,
       "pSysRouteIPX": pSysRouteIPX,
       "pSysRouteAPT": pSysRouteAPT,
       "pSysBridge": pSysBridge,
       "pBRIVariables": pBRIVariables,
       "pBRISwitchType": pBRISwitchType,
       "pBChannelUsage": pBChannelUsage,
       "p1stPhoneNumber": p1stPhoneNumber,
       "p1stSpidNumber": p1stSpidNumber,
       "p1stAnalogCall": p1stAnalogCall,
       "p2ndPhoneNumber": p2ndPhoneNumber,
       "p2ndSpidNumber": p2ndSpidNumber,
       "p2ndAnalogCall": p2ndAnalogCall,
       "pIPXVariables": pIPXVariables,
       "pFrameType8022": pFrameType8022,
       "pSeedRouter8022": pSeedRouter8022,
       "pNetworkNumber8022": pNetworkNumber8022,
       "pFrameType8023": pFrameType8023,
       "pSeedRouter8023": pSeedRouter8023,
       "pNetworkNumber8023": pNetworkNumber8023,
       "pFrameTypeEthernetII": pFrameTypeEthernetII,
       "pSeedRouterEthernetII": pSeedRouterEthernetII,
       "pNetworkNumberEthernetII": pNetworkNumberEthernetII,
       "pFrameTypeSnap": pFrameTypeSnap,
       "pSeedRouterSnap": pSeedRouterSnap,
       "pNetworkNumberSnap": pNetworkNumberSnap,
       "pIPXRouteTable": pIPXRouteTable,
       "pipxRouteEntry": pipxRouteEntry,
       "pIpxRtIndex": pIpxRtIndex,
       "pIpxRtServerName": pIpxRtServerName,
       "pIpxRtActive": pIpxRtActive,
       "pIpxRtNetworkNumber": pIpxRtNetworkNumber,
       "pIpxRtNodeNumber": pIpxRtNodeNumber,
       "pIpxRtSocketNumber": pIpxRtSocketNumber,
       "pIpxRtTypeNumber": pIpxRtTypeNumber,
       "pIpxRtHopCount": pIpxRtHopCount,
       "pIpxRtTickCount": pIpxRtTickCount,
       "pIpxRtGatewayNode": pIpxRtGatewayNode,
       "pAPTVariables": pAPTVariables,
       "pAPTSeedRouter": pAPTSeedRouter,
       "pAPTNetworkMin": pAPTNetworkMin,
       "pAPTNetworkMax": pAPTNetworkMax,
       "pAPT1stZoneName": pAPT1stZoneName,
       "pAPT2ndZoneName": pAPT2ndZoneName,
       "pAPTZipTimeout": pAPTZipTimeout,
       "pAPTRouteTable": pAPTRouteTable,
       "paptRouteEntry": paptRouteEntry,
       "pAptRtIndex": pAptRtIndex,
       "pAptRt1stZoneName": pAptRt1stZoneName,
       "pAptRt2ndZoneName": pAptRt2ndZoneName,
       "pAptRtNetworkMin": pAptRtNetworkMin,
       "pAptRtNetworkMax": pAptRtNetworkMax,
       "pAptRtActive": pAptRtActive,
       "pAptRtMetric": pAptRtMetric,
       "pAptRtGatewayNode": pAptRtGatewayNode,
       "pBRGVariables": pBRGVariables,
       "pBRGHandleIpx": pBRGHandleIpx,
       "pBRGRouteTable": pBRGRouteTable,
       "pbrgRouteEntry": pbrgRouteEntry,
       "pBrgRtIndex": pBrgRtIndex,
       "pBrgRtRouteName": pBrgRtRouteName,
       "pBrgRtActive": pBrgRtActive,
       "pBrgRtEtherAddress": pBrgRtEtherAddress,
       "pBrgRtIpAddress": pBrgRtIpAddress,
       "pBrgRtGatewayNode": pBrgRtGatewayNode,
       "pDialInVariables": pDialInVariables,
       "pDIClidAuthen": pDIClidAuthen,
       "pDIRecvAuthen": pDIRecvAuthen,
       "pDILinkCompression": pDILinkCompression,
       "pDIMaxTransferRate": pDIMaxTransferRate,
       "pDIIdleTimeout": pDIIdleTimeout,
       "pDIIpAddressSupply": pDIIpAddressSupply,
       "pDIIpPoolStartAddress": pDIIpPoolStartAddress,
       "pDIIpPoolCount": pDIIpPoolCount,
       "pDIIpxPool": pDIIpxPool,
       "pDIIpxPoolStartNetNumber": pDIIpxPoolStartNetNumber,
       "pDIIpxPoolCount": pDIIpxPoolCount,
       "pRemoteNodeVariables": pRemoteNodeVariables,
       "pRemoteNodeTable": pRemoteNodeTable,
       "premoteNodeEntry": premoteNodeEntry,
       "pRNIndex": pRNIndex,
       "pRNName": pRNName,
       "pRNActive": pRNActive,
       "pRNCallDirection": pRNCallDirection,
       "pRNRemLogin": pRNRemLogin,
       "pRNRemClid": pRNRemClid,
       "pRNCallBack": pRNCallBack,
       "pRNMyLogin": pRNMyLogin,
       "pRN1stPhoneNumber": pRN1stPhoneNumber,
       "pRN2ndPhoneNumber": pRN2ndPhoneNumber,
       "pRNRouteType": pRNRouteType,
       "pRNBridgeEnabled": pRNBridgeEnabled,
       "pRNEncapsulation": pRNEncapsulation,
       "pRNIpAddress": pRNIpAddress,
       "pRNTransferRate": pRNTransferRate,
       "pRNIdleTimeout": pRNIdleTimeout,
       "pRemoteUserVariables": pRemoteUserVariables,
       "pRemoteUserTable": pRemoteUserTable,
       "premoteUserEntry": premoteUserEntry,
       "pRUIndex": pRUIndex,
       "pRUName": pRUName,
       "pRUActive": pRUActive,
       "pRUCallBack": pRUCallBack,
       "pRUCallBackNumber": pRUCallBackNumber,
       "pRUCallBackOverride": pRUCallBackOverride,
       "pRUClid": pRUClid,
       "pRUIdleTimeout": pRUIdleTimeout,
       "zyxelTraps": zyxelTraps,
       "whyReboot": whyReboot}
)
