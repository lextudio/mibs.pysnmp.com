# SNMP MIB module (POWERHUB-TCPIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POWERHUB-TCPIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:25 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fore_ObjectIdentity = ObjectIdentity
fore = _Fore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_Lsd_ObjectIdentity = ObjectIdentity
lsd = _Lsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6)
)
_Lsdproducts_ObjectIdentity = ObjectIdentity
lsdproducts = _Lsdproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1)
)
_Lsdcommon_ObjectIdentity = ObjectIdentity
lsdcommon = _Lsdcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2)
)
_Alrip_ObjectIdentity = ObjectIdentity
alrip = _Alrip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4)
)


class _AlripControlType_Type(Integer32):
    """Custom type alripControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("vlan", 2))
    )


_AlripControlType_Type.__name__ = "Integer32"
_AlripControlType_Object = MibScalar
alripControlType = _AlripControlType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 1),
    _AlripControlType_Type()
)
alripControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripControlType.setStatus("mandatory")
_AlRipNormalConfigTable_Object = MibTable
alRipNormalConfigTable = _AlRipNormalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2)
)
if mibBuilder.loadTexts:
    alRipNormalConfigTable.setStatus("mandatory")
_AlripNormalConfigEntry_Object = MibTableRow
alripNormalConfigEntry = _AlripNormalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1)
)
alripNormalConfigEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alripNormalConfigPort"),
)
if mibBuilder.loadTexts:
    alripNormalConfigEntry.setStatus("mandatory")
_AlripNormalConfigPort_Type = Integer32
_AlripNormalConfigPort_Object = MibTableColumn
alripNormalConfigPort = _AlripNormalConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 1),
    _AlripNormalConfigPort_Type()
)
alripNormalConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigPort.setStatus("mandatory")


class _AlripNormalConfigTalk_Type(Integer32):
    """Custom type alripNormalConfigTalk based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripNormalConfigTalk_Type.__name__ = "Integer32"
_AlripNormalConfigTalk_Object = MibTableColumn
alripNormalConfigTalk = _AlripNormalConfigTalk_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 2),
    _AlripNormalConfigTalk_Type()
)
alripNormalConfigTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigTalk.setStatus("mandatory")


class _AlripNormalConfigListen_Type(Integer32):
    """Custom type alripNormalConfigListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripNormalConfigListen_Type.__name__ = "Integer32"
_AlripNormalConfigListen_Object = MibTableColumn
alripNormalConfigListen = _AlripNormalConfigListen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 3),
    _AlripNormalConfigListen_Type()
)
alripNormalConfigListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigListen.setStatus("mandatory")


class _AlripNormalConfigPoison_Type(Integer32):
    """Custom type alripNormalConfigPoison based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripNormalConfigPoison_Type.__name__ = "Integer32"
_AlripNormalConfigPoison_Object = MibTableColumn
alripNormalConfigPoison = _AlripNormalConfigPoison_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 4),
    _AlripNormalConfigPoison_Type()
)
alripNormalConfigPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigPoison.setStatus("mandatory")


class _AlripNormalConfigRptStaticRt_Type(Integer32):
    """Custom type alripNormalConfigRptStaticRt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripNormalConfigRptStaticRt_Type.__name__ = "Integer32"
_AlripNormalConfigRptStaticRt_Object = MibTableColumn
alripNormalConfigRptStaticRt = _AlripNormalConfigRptStaticRt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 5),
    _AlripNormalConfigRptStaticRt_Type()
)
alripNormalConfigRptStaticRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigRptStaticRt.setStatus("mandatory")


class _AlripNormalConfigRptDefaultRt_Type(Integer32):
    """Custom type alripNormalConfigRptDefaultRt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripNormalConfigRptDefaultRt_Type.__name__ = "Integer32"
_AlripNormalConfigRptDefaultRt_Object = MibTableColumn
alripNormalConfigRptDefaultRt = _AlripNormalConfigRptDefaultRt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 6),
    _AlripNormalConfigRptDefaultRt_Type()
)
alripNormalConfigRptDefaultRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigRptDefaultRt.setStatus("mandatory")


class _AlripNormalConfigAccptDefaultRt_Type(Integer32):
    """Custom type alripNormalConfigAccptDefaultRt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripNormalConfigAccptDefaultRt_Type.__name__ = "Integer32"
_AlripNormalConfigAccptDefaultRt_Object = MibTableColumn
alripNormalConfigAccptDefaultRt = _AlripNormalConfigAccptDefaultRt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 2, 1, 7),
    _AlripNormalConfigAccptDefaultRt_Type()
)
alripNormalConfigAccptDefaultRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripNormalConfigAccptDefaultRt.setStatus("mandatory")
_AlRipVLANConfigTable_Object = MibTable
alRipVLANConfigTable = _AlRipVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3)
)
if mibBuilder.loadTexts:
    alRipVLANConfigTable.setStatus("mandatory")
_AlripVLANConfigEntry_Object = MibTableRow
alripVLANConfigEntry = _AlripVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1)
)
alripVLANConfigEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alripVLANConfigNetNumber"),
)
if mibBuilder.loadTexts:
    alripVLANConfigEntry.setStatus("mandatory")
_AlripVLANConfigNetNumber_Type = IpAddress
_AlripVLANConfigNetNumber_Object = MibTableColumn
alripVLANConfigNetNumber = _AlripVLANConfigNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 1),
    _AlripVLANConfigNetNumber_Type()
)
alripVLANConfigNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigNetNumber.setStatus("mandatory")


class _AlripVLANConfigTalk_Type(Integer32):
    """Custom type alripVLANConfigTalk based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripVLANConfigTalk_Type.__name__ = "Integer32"
_AlripVLANConfigTalk_Object = MibTableColumn
alripVLANConfigTalk = _AlripVLANConfigTalk_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 2),
    _AlripVLANConfigTalk_Type()
)
alripVLANConfigTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigTalk.setStatus("mandatory")


class _AlripVLANConfigListen_Type(Integer32):
    """Custom type alripVLANConfigListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripVLANConfigListen_Type.__name__ = "Integer32"
_AlripVLANConfigListen_Object = MibTableColumn
alripVLANConfigListen = _AlripVLANConfigListen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 3),
    _AlripVLANConfigListen_Type()
)
alripVLANConfigListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigListen.setStatus("mandatory")


class _AlripVLANConfigPoison_Type(Integer32):
    """Custom type alripVLANConfigPoison based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripVLANConfigPoison_Type.__name__ = "Integer32"
_AlripVLANConfigPoison_Object = MibTableColumn
alripVLANConfigPoison = _AlripVLANConfigPoison_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 4),
    _AlripVLANConfigPoison_Type()
)
alripVLANConfigPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigPoison.setStatus("mandatory")


class _AlripVLANConfigRptStaticRt_Type(Integer32):
    """Custom type alripVLANConfigRptStaticRt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripVLANConfigRptStaticRt_Type.__name__ = "Integer32"
_AlripVLANConfigRptStaticRt_Object = MibTableColumn
alripVLANConfigRptStaticRt = _AlripVLANConfigRptStaticRt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 5),
    _AlripVLANConfigRptStaticRt_Type()
)
alripVLANConfigRptStaticRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigRptStaticRt.setStatus("mandatory")


class _AlripVLANConfigRptDefaultRt_Type(Integer32):
    """Custom type alripVLANConfigRptDefaultRt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripVLANConfigRptDefaultRt_Type.__name__ = "Integer32"
_AlripVLANConfigRptDefaultRt_Object = MibTableColumn
alripVLANConfigRptDefaultRt = _AlripVLANConfigRptDefaultRt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 6),
    _AlripVLANConfigRptDefaultRt_Type()
)
alripVLANConfigRptDefaultRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigRptDefaultRt.setStatus("mandatory")


class _AlripVLANConfigAccptDefaultRt_Type(Integer32):
    """Custom type alripVLANConfigAccptDefaultRt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlripVLANConfigAccptDefaultRt_Type.__name__ = "Integer32"
_AlripVLANConfigAccptDefaultRt_Object = MibTableColumn
alripVLANConfigAccptDefaultRt = _AlripVLANConfigAccptDefaultRt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 7),
    _AlripVLANConfigAccptDefaultRt_Type()
)
alripVLANConfigAccptDefaultRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigAccptDefaultRt.setStatus("mandatory")


class _AlripVLANConfigDelete_Type(Integer32):
    """Custom type alripVLANConfigDelete based on Integer32"""
    defaultValue = 0


_AlripVLANConfigDelete_Object = MibTableColumn
alripVLANConfigDelete = _AlripVLANConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 3, 1, 8),
    _AlripVLANConfigDelete_Type()
)
alripVLANConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripVLANConfigDelete.setStatus("mandatory")


class _AlripStatsClear_Type(Integer32):
    """Custom type alripStatsClear based on Integer32"""
    defaultValue = 0


_AlripStatsClear_Object = MibScalar
alripStatsClear = _AlripStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 4),
    _AlripStatsClear_Type()
)
alripStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alripStatsClear.setStatus("mandatory")
_AlRipStatPktsRcvd_Type = Counter32
_AlRipStatPktsRcvd_Object = MibScalar
alRipStatPktsRcvd = _AlRipStatPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 5),
    _AlRipStatPktsRcvd_Type()
)
alRipStatPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsRcvd.setStatus("mandatory")
_AlRipStatPktsXmitted_Type = Counter32
_AlRipStatPktsXmitted_Object = MibScalar
alRipStatPktsXmitted = _AlRipStatPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 6),
    _AlRipStatPktsXmitted_Type()
)
alRipStatPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsXmitted.setStatus("mandatory")
_AlRipStatReqsRcvd_Type = Counter32
_AlRipStatReqsRcvd_Object = MibScalar
alRipStatReqsRcvd = _AlRipStatReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 7),
    _AlRipStatReqsRcvd_Type()
)
alRipStatReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatReqsRcvd.setStatus("mandatory")
_AlRipStatRespRcvd_Type = Counter32
_AlRipStatRespRcvd_Object = MibScalar
alRipStatRespRcvd = _AlRipStatRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 8),
    _AlRipStatRespRcvd_Type()
)
alRipStatRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatRespRcvd.setStatus("mandatory")
_AlRipStatReqsXmitted_Type = Counter32
_AlRipStatReqsXmitted_Object = MibScalar
alRipStatReqsXmitted = _AlRipStatReqsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 9),
    _AlRipStatReqsXmitted_Type()
)
alRipStatReqsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatReqsXmitted.setStatus("mandatory")
_AlRipStatRespXmitted_Type = Counter32
_AlRipStatRespXmitted_Object = MibScalar
alRipStatRespXmitted = _AlRipStatRespXmitted_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 10),
    _AlRipStatRespXmitted_Type()
)
alRipStatRespXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatRespXmitted.setStatus("mandatory")
_AlRipStatRouteTimeOuts_Type = Counter32
_AlRipStatRouteTimeOuts_Object = MibScalar
alRipStatRouteTimeOuts = _AlRipStatRouteTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 11),
    _AlRipStatRouteTimeOuts_Type()
)
alRipStatRouteTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatRouteTimeOuts.setStatus("mandatory")
_AlRipStatShortPkts_Type = Counter32
_AlRipStatShortPkts_Object = MibScalar
alRipStatShortPkts = _AlRipStatShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 12),
    _AlRipStatShortPkts_Type()
)
alRipStatShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatShortPkts.setStatus("mandatory")
_AlRipStatBadVer_Type = Counter32
_AlRipStatBadVer_Object = MibScalar
alRipStatBadVer = _AlRipStatBadVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 13),
    _AlRipStatBadVer_Type()
)
alRipStatBadVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadVer.setStatus("mandatory")
_AlRipStatBadZeroes_Type = Counter32
_AlRipStatBadZeroes_Object = MibScalar
alRipStatBadZeroes = _AlRipStatBadZeroes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 14),
    _AlRipStatBadZeroes_Type()
)
alRipStatBadZeroes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadZeroes.setStatus("mandatory")
_AlRipStatBadSrcPort_Type = Counter32
_AlRipStatBadSrcPort_Object = MibScalar
alRipStatBadSrcPort = _AlRipStatBadSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 15),
    _AlRipStatBadSrcPort_Type()
)
alRipStatBadSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadSrcPort.setStatus("mandatory")
_AlRipStatBadSrcIp_Type = Counter32
_AlRipStatBadSrcIp_Object = MibScalar
alRipStatBadSrcIp = _AlRipStatBadSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 16),
    _AlRipStatBadSrcIp_Type()
)
alRipStatBadSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadSrcIp.setStatus("mandatory")
_AlRipStatPktsSelf_Type = Counter32
_AlRipStatPktsSelf_Object = MibScalar
alRipStatPktsSelf = _AlRipStatPktsSelf_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 17),
    _AlRipStatPktsSelf_Type()
)
alRipStatPktsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsSelf.setStatus("mandatory")
_AlRipigUpdates_Type = Counter32
_AlRipigUpdates_Object = MibScalar
alRipigUpdates = _AlRipigUpdates_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 18),
    _AlRipigUpdates_Type()
)
alRipigUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipigUpdates.setStatus("mandatory")
_AlRipStatPqueuePktsQueued_Type = Counter32
_AlRipStatPqueuePktsQueued_Object = MibScalar
alRipStatPqueuePktsQueued = _AlRipStatPqueuePktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 19),
    _AlRipStatPqueuePktsQueued_Type()
)
alRipStatPqueuePktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPqueuePktsQueued.setStatus("mandatory")
_AlRipStatPqueueFreeQueue_Type = Counter32
_AlRipStatPqueueFreeQueue_Object = MibScalar
alRipStatPqueueFreeQueue = _AlRipStatPqueueFreeQueue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 20),
    _AlRipStatPqueueFreeQueue_Type()
)
alRipStatPqueueFreeQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPqueueFreeQueue.setStatus("mandatory")
_AlRipStatTqueuePktsQueued_Type = Counter32
_AlRipStatTqueuePktsQueued_Object = MibScalar
alRipStatTqueuePktsQueued = _AlRipStatTqueuePktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 21),
    _AlRipStatTqueuePktsQueued_Type()
)
alRipStatTqueuePktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatTqueuePktsQueued.setStatus("mandatory")
_AlRipStatTqueueFreeQueue_Type = Counter32
_AlRipStatTqueueFreeQueue_Object = MibScalar
alRipStatTqueueFreeQueue = _AlRipStatTqueueFreeQueue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 22),
    _AlRipStatTqueueFreeQueue_Type()
)
alRipStatTqueueFreeQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatTqueueFreeQueue.setStatus("mandatory")
_AlRipDynPktsRcvd_Type = Counter32
_AlRipDynPktsRcvd_Object = MibScalar
alRipDynPktsRcvd = _AlRipDynPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 23),
    _AlRipDynPktsRcvd_Type()
)
alRipDynPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsRcvd.setStatus("mandatory")
_AlRipDynPktsXmitted_Type = Counter32
_AlRipDynPktsXmitted_Object = MibScalar
alRipDynPktsXmitted = _AlRipDynPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 24),
    _AlRipDynPktsXmitted_Type()
)
alRipDynPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsXmitted.setStatus("mandatory")
_AlRipDynReqsRcvd_Type = Counter32
_AlRipDynReqsRcvd_Object = MibScalar
alRipDynReqsRcvd = _AlRipDynReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 25),
    _AlRipDynReqsRcvd_Type()
)
alRipDynReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynReqsRcvd.setStatus("mandatory")
_AlRipDynRespRcvd_Type = Counter32
_AlRipDynRespRcvd_Object = MibScalar
alRipDynRespRcvd = _AlRipDynRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 26),
    _AlRipDynRespRcvd_Type()
)
alRipDynRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynRespRcvd.setStatus("mandatory")
_AlRipDynReqsXmitted_Type = Counter32
_AlRipDynReqsXmitted_Object = MibScalar
alRipDynReqsXmitted = _AlRipDynReqsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 27),
    _AlRipDynReqsXmitted_Type()
)
alRipDynReqsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynReqsXmitted.setStatus("mandatory")
_AlRipDynRespXmitted_Type = Counter32
_AlRipDynRespXmitted_Object = MibScalar
alRipDynRespXmitted = _AlRipDynRespXmitted_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 28),
    _AlRipDynRespXmitted_Type()
)
alRipDynRespXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynRespXmitted.setStatus("mandatory")
_AlRipDynRouteTimeOuts_Type = Counter32
_AlRipDynRouteTimeOuts_Object = MibScalar
alRipDynRouteTimeOuts = _AlRipDynRouteTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 29),
    _AlRipDynRouteTimeOuts_Type()
)
alRipDynRouteTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynRouteTimeOuts.setStatus("mandatory")
_AlRipDynShortPkts_Type = Counter32
_AlRipDynShortPkts_Object = MibScalar
alRipDynShortPkts = _AlRipDynShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 30),
    _AlRipDynShortPkts_Type()
)
alRipDynShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynShortPkts.setStatus("mandatory")
_AlRipDynBadVer_Type = Counter32
_AlRipDynBadVer_Object = MibScalar
alRipDynBadVer = _AlRipDynBadVer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 31),
    _AlRipDynBadVer_Type()
)
alRipDynBadVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadVer.setStatus("mandatory")
_AlRipDynBadZeroes_Type = Counter32
_AlRipDynBadZeroes_Object = MibScalar
alRipDynBadZeroes = _AlRipDynBadZeroes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 32),
    _AlRipDynBadZeroes_Type()
)
alRipDynBadZeroes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadZeroes.setStatus("mandatory")
_AlRipDynBadSrcPort_Type = Counter32
_AlRipDynBadSrcPort_Object = MibScalar
alRipDynBadSrcPort = _AlRipDynBadSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 33),
    _AlRipDynBadSrcPort_Type()
)
alRipDynBadSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadSrcPort.setStatus("mandatory")
_AlRipDynBadSrcIp_Type = Counter32
_AlRipDynBadSrcIp_Object = MibScalar
alRipDynBadSrcIp = _AlRipDynBadSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 34),
    _AlRipDynBadSrcIp_Type()
)
alRipDynBadSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadSrcIp.setStatus("mandatory")
_AlRipDynPktsSelf_Type = Counter32
_AlRipDynPktsSelf_Object = MibScalar
alRipDynPktsSelf = _AlRipDynPktsSelf_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 35),
    _AlRipDynPktsSelf_Type()
)
alRipDynPktsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsSelf.setStatus("mandatory")
_AlRipDynNumTrigUpdates_Type = Counter32
_AlRipDynNumTrigUpdates_Object = MibScalar
alRipDynNumTrigUpdates = _AlRipDynNumTrigUpdates_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 36),
    _AlRipDynNumTrigUpdates_Type()
)
alRipDynNumTrigUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynNumTrigUpdates.setStatus("mandatory")
_AlRipDyntPqueuePktsQueued_Type = Counter32
_AlRipDyntPqueuePktsQueued_Object = MibScalar
alRipDyntPqueuePktsQueued = _AlRipDyntPqueuePktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 37),
    _AlRipDyntPqueuePktsQueued_Type()
)
alRipDyntPqueuePktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDyntPqueuePktsQueued.setStatus("mandatory")
_AlRipDynPqueueFreeQueue_Type = Counter32
_AlRipDynPqueueFreeQueue_Object = MibScalar
alRipDynPqueueFreeQueue = _AlRipDynPqueueFreeQueue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 38),
    _AlRipDynPqueueFreeQueue_Type()
)
alRipDynPqueueFreeQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPqueueFreeQueue.setStatus("mandatory")
_AlRipDynTqueuePktsQueued_Type = Counter32
_AlRipDynTqueuePktsQueued_Object = MibScalar
alRipDynTqueuePktsQueued = _AlRipDynTqueuePktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 39),
    _AlRipDynTqueuePktsQueued_Type()
)
alRipDynTqueuePktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynTqueuePktsQueued.setStatus("mandatory")
_AlRipDynTqueueFreeQueue_Type = Counter32
_AlRipDynTqueueFreeQueue_Object = MibScalar
alRipDynTqueueFreeQueue = _AlRipDynTqueueFreeQueue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 40),
    _AlRipDynTqueueFreeQueue_Type()
)
alRipDynTqueueFreeQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynTqueueFreeQueue.setStatus("mandatory")
_AlRipAccptFilTable_Object = MibTable
alRipAccptFilTable = _AlRipAccptFilTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 41)
)
if mibBuilder.loadTexts:
    alRipAccptFilTable.setStatus("mandatory")
_RipAccptFilEntry_Object = MibTableRow
ripAccptFilEntry = _RipAccptFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 41, 1)
)
ripAccptFilEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "ripAccptFilNumber"),
)
if mibBuilder.loadTexts:
    ripAccptFilEntry.setStatus("mandatory")


class _RipAccptFilNumber_Type(Integer32):
    """Custom type ripAccptFilNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RipAccptFilNumber_Type.__name__ = "Integer32"
_RipAccptFilNumber_Object = MibTableColumn
ripAccptFilNumber = _RipAccptFilNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 41, 1, 1),
    _RipAccptFilNumber_Type()
)
ripAccptFilNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilNumber.setStatus("mandatory")
_RipAccptFilAddr_Type = IpAddress
_RipAccptFilAddr_Object = MibTableColumn
ripAccptFilAddr = _RipAccptFilAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 41, 1, 2),
    _RipAccptFilAddr_Type()
)
ripAccptFilAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilAddr.setStatus("mandatory")
_RipAccptFilMask_Type = IpAddress
_RipAccptFilMask_Object = MibTableColumn
ripAccptFilMask = _RipAccptFilMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 41, 1, 3),
    _RipAccptFilMask_Type()
)
ripAccptFilMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilMask.setStatus("mandatory")


class _RipAccptFilPort_Type(Integer32):
    """Custom type ripAccptFilPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_RipAccptFilPort_Type.__name__ = "Integer32"
_RipAccptFilPort_Object = MibTableColumn
ripAccptFilPort = _RipAccptFilPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 41, 1, 4),
    _RipAccptFilPort_Type()
)
ripAccptFilPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilPort.setStatus("mandatory")
_AlRipReportFilTable_Object = MibTable
alRipReportFilTable = _AlRipReportFilTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 42)
)
if mibBuilder.loadTexts:
    alRipReportFilTable.setStatus("mandatory")
_RipReportFilEntry_Object = MibTableRow
ripReportFilEntry = _RipReportFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 42, 1)
)
ripReportFilEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "ripReportFilNumber"),
)
if mibBuilder.loadTexts:
    ripReportFilEntry.setStatus("mandatory")


class _RipReportFilNumber_Type(Integer32):
    """Custom type ripReportFilNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RipReportFilNumber_Type.__name__ = "Integer32"
_RipReportFilNumber_Object = MibTableColumn
ripReportFilNumber = _RipReportFilNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 42, 1, 1),
    _RipReportFilNumber_Type()
)
ripReportFilNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilNumber.setStatus("mandatory")
_RipReportFilAddr_Type = IpAddress
_RipReportFilAddr_Object = MibTableColumn
ripReportFilAddr = _RipReportFilAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 42, 1, 2),
    _RipReportFilAddr_Type()
)
ripReportFilAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilAddr.setStatus("mandatory")
_RipReportFilMask_Type = IpAddress
_RipReportFilMask_Object = MibTableColumn
ripReportFilMask = _RipReportFilMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 42, 1, 3),
    _RipReportFilMask_Type()
)
ripReportFilMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilMask.setStatus("mandatory")


class _RipReportFilPort_Type(Integer32):
    """Custom type ripReportFilPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_RipReportFilPort_Type.__name__ = "Integer32"
_RipReportFilPort_Object = MibTableColumn
ripReportFilPort = _RipReportFilPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 4, 42, 1, 4),
    _RipReportFilPort_Type()
)
ripReportFilPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilPort.setStatus("mandatory")
_Altcp_ObjectIdentity = ObjectIdentity
altcp = _Altcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5)
)
_AlTcpConnIdleTime_Type = Integer32
_AlTcpConnIdleTime_Object = MibScalar
alTcpConnIdleTime = _AlTcpConnIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 1),
    _AlTcpConnIdleTime_Type()
)
alTcpConnIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpConnIdleTime.setStatus("mandatory")
_AlTcpKeepAliveInt_Type = Integer32
_AlTcpKeepAliveInt_Object = MibScalar
alTcpKeepAliveInt = _AlTcpKeepAliveInt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 2),
    _AlTcpKeepAliveInt_Type()
)
alTcpKeepAliveInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpKeepAliveInt.setStatus("mandatory")
_AlTcpDisconnectInt_Type = Integer32
_AlTcpDisconnectInt_Object = MibScalar
alTcpDisconnectInt = _AlTcpDisconnectInt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 3),
    _AlTcpDisconnectInt_Type()
)
alTcpDisconnectInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpDisconnectInt.setStatus("mandatory")
_AlTcpShortSegRcvd_Type = Integer32
_AlTcpShortSegRcvd_Object = MibScalar
alTcpShortSegRcvd = _AlTcpShortSegRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 4),
    _AlTcpShortSegRcvd_Type()
)
alTcpShortSegRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpShortSegRcvd.setStatus("mandatory")
_AlTcpStatsClear_Type = Integer32
_AlTcpStatsClear_Object = MibScalar
alTcpStatsClear = _AlTcpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 5),
    _AlTcpStatsClear_Type()
)
alTcpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpStatsClear.setStatus("mandatory")
_AlTcpConnTable_Object = MibTable
alTcpConnTable = _AlTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6)
)
if mibBuilder.loadTexts:
    alTcpConnTable.setStatus("mandatory")
_AlTcpConnEntry_Object = MibTableRow
alTcpConnEntry = _AlTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1)
)
alTcpConnEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alTcpConnId"),
)
if mibBuilder.loadTexts:
    alTcpConnEntry.setStatus("mandatory")
_AlTcpConnId_Type = Integer32
_AlTcpConnId_Object = MibTableColumn
alTcpConnId = _AlTcpConnId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1, 1),
    _AlTcpConnId_Type()
)
alTcpConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnId.setStatus("mandatory")


class _AlTcpConnState_Type(Integer32):
    """Custom type alTcpConnState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_AlTcpConnState_Type.__name__ = "Integer32"
_AlTcpConnState_Object = MibTableColumn
alTcpConnState = _AlTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1, 2),
    _AlTcpConnState_Type()
)
alTcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpConnState.setStatus("mandatory")
_AlTcpConnLocalAddress_Type = IpAddress
_AlTcpConnLocalAddress_Object = MibTableColumn
alTcpConnLocalAddress = _AlTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1, 3),
    _AlTcpConnLocalAddress_Type()
)
alTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnLocalAddress.setStatus("mandatory")
_AlTcpConnLocalPort_Type = Integer32
_AlTcpConnLocalPort_Object = MibTableColumn
alTcpConnLocalPort = _AlTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1, 4),
    _AlTcpConnLocalPort_Type()
)
alTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnLocalPort.setStatus("mandatory")
_AlTcpConnRemAddress_Type = IpAddress
_AlTcpConnRemAddress_Object = MibTableColumn
alTcpConnRemAddress = _AlTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1, 5),
    _AlTcpConnRemAddress_Type()
)
alTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnRemAddress.setStatus("mandatory")
_AlTcpConnRemPort_Type = Integer32
_AlTcpConnRemPort_Object = MibTableColumn
alTcpConnRemPort = _AlTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 6, 1, 6),
    _AlTcpConnRemPort_Type()
)
alTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnRemPort.setStatus("mandatory")
_AlTcpFilTable_Object = MibTable
alTcpFilTable = _AlTcpFilTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7)
)
if mibBuilder.loadTexts:
    alTcpFilTable.setStatus("mandatory")
_TcpFilEntry_Object = MibTableRow
tcpFilEntry = _TcpFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7, 1)
)
tcpFilEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "tcpFilNumber"),
)
if mibBuilder.loadTexts:
    tcpFilEntry.setStatus("mandatory")
_TcpFilNumber_Type = Integer32
_TcpFilNumber_Object = MibTableColumn
tcpFilNumber = _TcpFilNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7, 1, 1),
    _TcpFilNumber_Type()
)
tcpFilNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilNumber.setStatus("mandatory")
_TcpFilSrcAddr_Type = IpAddress
_TcpFilSrcAddr_Object = MibTableColumn
tcpFilSrcAddr = _TcpFilSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7, 1, 2),
    _TcpFilSrcAddr_Type()
)
tcpFilSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilSrcAddr.setStatus("mandatory")
_TcpFilSrcMask_Type = IpAddress
_TcpFilSrcMask_Object = MibTableColumn
tcpFilSrcMask = _TcpFilSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7, 1, 3),
    _TcpFilSrcMask_Type()
)
tcpFilSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilSrcMask.setStatus("mandatory")
_TcpFilProtocol_Type = Integer32
_TcpFilProtocol_Object = MibTableColumn
tcpFilProtocol = _TcpFilProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7, 1, 4),
    _TcpFilProtocol_Type()
)
tcpFilProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilProtocol.setStatus("mandatory")
_TcpFilDstPort_Type = Integer32
_TcpFilDstPort_Object = MibTableColumn
tcpFilDstPort = _TcpFilDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 5, 7, 1, 5),
    _TcpFilDstPort_Type()
)
tcpFilDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilDstPort.setStatus("mandatory")
_Alip_ObjectIdentity = ObjectIdentity
alip = _Alip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6)
)
_AlArpTableClear_Type = Integer32
_AlArpTableClear_Object = MibScalar
alArpTableClear = _AlArpTableClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 1),
    _AlArpTableClear_Type()
)
alArpTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alArpTableClear.setStatus("mandatory")
_AlArpAge_Type = Integer32
_AlArpAge_Object = MibScalar
alArpAge = _AlArpAge_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 2),
    _AlArpAge_Type()
)
alArpAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alArpAge.setStatus("mandatory")
_AlArpStatReqsRcvd_Type = Counter32
_AlArpStatReqsRcvd_Object = MibScalar
alArpStatReqsRcvd = _AlArpStatReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 3),
    _AlArpStatReqsRcvd_Type()
)
alArpStatReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatReqsRcvd.setStatus("mandatory")
_AlArpStatRepliesRcvd_Type = Counter32
_AlArpStatRepliesRcvd_Object = MibScalar
alArpStatRepliesRcvd = _AlArpStatRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 4),
    _AlArpStatRepliesRcvd_Type()
)
alArpStatRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatRepliesRcvd.setStatus("mandatory")
_AlArpStatInvalidOpcodes_Type = Counter32
_AlArpStatInvalidOpcodes_Object = MibScalar
alArpStatInvalidOpcodes = _AlArpStatInvalidOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 5),
    _AlArpStatInvalidOpcodes_Type()
)
alArpStatInvalidOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatInvalidOpcodes.setStatus("mandatory")
_AlArpStatRequestsSent_Type = Counter32
_AlArpStatRequestsSent_Object = MibScalar
alArpStatRequestsSent = _AlArpStatRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 6),
    _AlArpStatRequestsSent_Type()
)
alArpStatRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatRequestsSent.setStatus("mandatory")
_AlArpStatRepliesSent_Type = Counter32
_AlArpStatRepliesSent_Object = MibScalar
alArpStatRepliesSent = _AlArpStatRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 7),
    _AlArpStatRepliesSent_Type()
)
alArpStatRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatRepliesSent.setStatus("mandatory")
_AlArpStatProxyReplies_Type = Counter32
_AlArpStatProxyReplies_Object = MibScalar
alArpStatProxyReplies = _AlArpStatProxyReplies_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 8),
    _AlArpStatProxyReplies_Type()
)
alArpStatProxyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatProxyReplies.setStatus("mandatory")
_AlArpDynReqsRcvd_Type = Counter32
_AlArpDynReqsRcvd_Object = MibScalar
alArpDynReqsRcvd = _AlArpDynReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 9),
    _AlArpDynReqsRcvd_Type()
)
alArpDynReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynReqsRcvd.setStatus("mandatory")
_AlArpDynRepliesRcvd_Type = Counter32
_AlArpDynRepliesRcvd_Object = MibScalar
alArpDynRepliesRcvd = _AlArpDynRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 10),
    _AlArpDynRepliesRcvd_Type()
)
alArpDynRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynRepliesRcvd.setStatus("mandatory")
_AlArpDynInvalidOpcodes_Type = Counter32
_AlArpDynInvalidOpcodes_Object = MibScalar
alArpDynInvalidOpcodes = _AlArpDynInvalidOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 11),
    _AlArpDynInvalidOpcodes_Type()
)
alArpDynInvalidOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynInvalidOpcodes.setStatus("mandatory")
_AlArpDynRequestsSent_Type = Counter32
_AlArpDynRequestsSent_Object = MibScalar
alArpDynRequestsSent = _AlArpDynRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 12),
    _AlArpDynRequestsSent_Type()
)
alArpDynRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynRequestsSent.setStatus("mandatory")
_AlArpDynRepliesSent_Type = Counter32
_AlArpDynRepliesSent_Object = MibScalar
alArpDynRepliesSent = _AlArpDynRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 13),
    _AlArpDynRepliesSent_Type()
)
alArpDynRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynRepliesSent.setStatus("mandatory")
_AlArpDynProxyReplies_Type = Counter32
_AlArpDynProxyReplies_Object = MibScalar
alArpDynProxyReplies = _AlArpDynProxyReplies_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 14),
    _AlArpDynProxyReplies_Type()
)
alArpDynProxyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynProxyReplies.setStatus("mandatory")


class _AlArpStatsClear_Type(Integer32):
    """Custom type alArpStatsClear based on Integer32"""
    defaultValue = 0


_AlArpStatsClear_Object = MibScalar
alArpStatsClear = _AlArpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 15),
    _AlArpStatsClear_Type()
)
alArpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alArpStatsClear.setStatus("mandatory")
_AlArpProxyTable_Object = MibTable
alArpProxyTable = _AlArpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 16)
)
if mibBuilder.loadTexts:
    alArpProxyTable.setStatus("mandatory")
_ArpProxyEntry_Object = MibTableRow
arpProxyEntry = _ArpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 16, 1)
)
arpProxyEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "arpProxyPort"),
)
if mibBuilder.loadTexts:
    arpProxyEntry.setStatus("mandatory")
_ArpProxyPort_Type = Integer32
_ArpProxyPort_Object = MibTableColumn
arpProxyPort = _ArpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 16, 1, 1),
    _ArpProxyPort_Type()
)
arpProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyPort.setStatus("mandatory")


class _ArpProxyEnable_Type(Integer32):
    """Custom type arpProxyEnable based on Integer32"""
    defaultValue = 2


_ArpProxyEnable_Object = MibTableColumn
arpProxyEnable = _ArpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 16, 1, 2),
    _ArpProxyEnable_Type()
)
arpProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpProxyEnable.setStatus("mandatory")
_AlIpTemplateTable_Object = MibTable
alIpTemplateTable = _AlIpTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17)
)
if mibBuilder.loadTexts:
    alIpTemplateTable.setStatus("mandatory")
_AlipTemplateEntry_Object = MibTableRow
alipTemplateEntry = _AlipTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1)
)
alipTemplateEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alipTemplateNumber"),
)
if mibBuilder.loadTexts:
    alipTemplateEntry.setStatus("mandatory")


class _AlipTemplateNumber_Type(Integer32):
    """Custom type alipTemplateNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AlipTemplateNumber_Type.__name__ = "Integer32"
_AlipTemplateNumber_Object = MibTableColumn
alipTemplateNumber = _AlipTemplateNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 1),
    _AlipTemplateNumber_Type()
)
alipTemplateNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateNumber.setStatus("mandatory")


class _AlipTemplateDelete_Type(Integer32):
    """Custom type alipTemplateDelete based on Integer32"""
    defaultValue = 0


_AlipTemplateDelete_Object = MibTableColumn
alipTemplateDelete = _AlipTemplateDelete_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 2),
    _AlipTemplateDelete_Type()
)
alipTemplateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateDelete.setStatus("mandatory")


class _AlipTemplateAction_Type(Integer32):
    """Custom type alipTemplateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("forward", 1))
    )


_AlipTemplateAction_Type.__name__ = "Integer32"
_AlipTemplateAction_Object = MibTableColumn
alipTemplateAction = _AlipTemplateAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 3),
    _AlipTemplateAction_Type()
)
alipTemplateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateAction.setStatus("mandatory")
_AlipTemplateSrcAddr_Type = IpAddress
_AlipTemplateSrcAddr_Object = MibTableColumn
alipTemplateSrcAddr = _AlipTemplateSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 4),
    _AlipTemplateSrcAddr_Type()
)
alipTemplateSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateSrcAddr.setStatus("mandatory")
_AlipTemplateSrcMask_Type = IpAddress
_AlipTemplateSrcMask_Object = MibTableColumn
alipTemplateSrcMask = _AlipTemplateSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 5),
    _AlipTemplateSrcMask_Type()
)
alipTemplateSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateSrcMask.setStatus("mandatory")
_AlipTemplateDstAddr_Type = IpAddress
_AlipTemplateDstAddr_Object = MibTableColumn
alipTemplateDstAddr = _AlipTemplateDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 6),
    _AlipTemplateDstAddr_Type()
)
alipTemplateDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateDstAddr.setStatus("mandatory")
_AlipTemplateDstMask_Type = IpAddress
_AlipTemplateDstMask_Object = MibTableColumn
alipTemplateDstMask = _AlipTemplateDstMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 7),
    _AlipTemplateDstMask_Type()
)
alipTemplateDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateDstMask.setStatus("mandatory")


class _AlipTemplateProtocol_Type(Integer32):
    """Custom type alipTemplateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlipTemplateProtocol_Type.__name__ = "Integer32"
_AlipTemplateProtocol_Object = MibTableColumn
alipTemplateProtocol = _AlipTemplateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 8),
    _AlipTemplateProtocol_Type()
)
alipTemplateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateProtocol.setStatus("mandatory")


class _AlipTemplateOperator_Type(Integer32):
    """Custom type alipTemplateOperator based on Integer32"""
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
        *(("conreq", 6),
          ("equalto", 2),
          ("greaterthan", 5),
          ("lessthan", 4),
          ("notequalto", 3),
          ("unknown", 1))
    )


_AlipTemplateOperator_Type.__name__ = "Integer32"
_AlipTemplateOperator_Object = MibTableColumn
alipTemplateOperator = _AlipTemplateOperator_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 9),
    _AlipTemplateOperator_Type()
)
alipTemplateOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateOperator.setStatus("mandatory")


class _AlipTemplateDstPort_Type(Integer32):
    """Custom type alipTemplateDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlipTemplateDstPort_Type.__name__ = "Integer32"
_AlipTemplateDstPort_Object = MibTableColumn
alipTemplateDstPort = _AlipTemplateDstPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 17, 1, 10),
    _AlipTemplateDstPort_Type()
)
alipTemplateDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipTemplateDstPort.setStatus("mandatory")
_AlIpRuleTable_Object = MibTable
alIpRuleTable = _AlIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 18)
)
if mibBuilder.loadTexts:
    alIpRuleTable.setStatus("mandatory")
_AlipRuleEntry_Object = MibTableRow
alipRuleEntry = _AlipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 18, 1)
)
alipRuleEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alipRuleNumber"),
)
if mibBuilder.loadTexts:
    alipRuleEntry.setStatus("mandatory")


class _AlipRuleNumber_Type(Integer32):
    """Custom type alipRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AlipRuleNumber_Type.__name__ = "Integer32"
_AlipRuleNumber_Object = MibTableColumn
alipRuleNumber = _AlipRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 18, 1, 1),
    _AlipRuleNumber_Type()
)
alipRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipRuleNumber.setStatus("mandatory")


class _AlipRuleDelete_Type(Integer32):
    """Custom type alipRuleDelete based on Integer32"""
    defaultValue = 0


_AlipRuleDelete_Object = MibTableColumn
alipRuleDelete = _AlipRuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 18, 1, 2),
    _AlipRuleDelete_Type()
)
alipRuleDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipRuleDelete.setStatus("mandatory")
_AlipRuleTemplates_Type = DisplayString
_AlipRuleTemplates_Object = MibTableColumn
alipRuleTemplates = _AlipRuleTemplates_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 18, 1, 3),
    _AlipRuleTemplates_Type()
)
alipRuleTemplates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipRuleTemplates.setStatus("mandatory")
_AlipAcsCtrlTable_Object = MibTable
alipAcsCtrlTable = _AlipAcsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 19)
)
if mibBuilder.loadTexts:
    alipAcsCtrlTable.setStatus("mandatory")
_AlipAcsCtrlEntry_Object = MibTableRow
alipAcsCtrlEntry = _AlipAcsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 19, 1)
)
alipAcsCtrlEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alipAcsCtrlPort"),
)
if mibBuilder.loadTexts:
    alipAcsCtrlEntry.setStatus("mandatory")
_AlipAcsCtrlPort_Type = Integer32
_AlipAcsCtrlPort_Object = MibTableColumn
alipAcsCtrlPort = _AlipAcsCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 19, 1, 1),
    _AlipAcsCtrlPort_Type()
)
alipAcsCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipAcsCtrlPort.setStatus("mandatory")


class _AlipAcsCtrlDelete_Type(Integer32):
    """Custom type alipAcsCtrlDelete based on Integer32"""
    defaultValue = 0


_AlipAcsCtrlDelete_Object = MibTableColumn
alipAcsCtrlDelete = _AlipAcsCtrlDelete_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 19, 1, 2),
    _AlipAcsCtrlDelete_Type()
)
alipAcsCtrlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipAcsCtrlDelete.setStatus("mandatory")
_AlipAcsCtrlSourceRule_Type = Integer32
_AlipAcsCtrlSourceRule_Object = MibScalar
alipAcsCtrlSourceRule = _AlipAcsCtrlSourceRule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 19, 1, 3),
    _AlipAcsCtrlSourceRule_Type()
)
alipAcsCtrlSourceRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipAcsCtrlSourceRule.setStatus("mandatory")
_AlipAcsCtrlDestRule_Type = Integer32
_AlipAcsCtrlDestRule_Object = MibScalar
alipAcsCtrlDestRule = _AlipAcsCtrlDestRule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 19, 1, 4),
    _AlipAcsCtrlDestRule_Type()
)
alipAcsCtrlDestRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alipAcsCtrlDestRule.setStatus("mandatory")
_AlipFilStatStatsTable_Object = MibTable
alipFilStatStatsTable = _AlipFilStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 20)
)
if mibBuilder.loadTexts:
    alipFilStatStatsTable.setStatus("mandatory")
_AlipFilStatStatsEntry_Object = MibTableRow
alipFilStatStatsEntry = _AlipFilStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 20, 1)
)
alipFilStatStatsEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alipFilStatStatsTemplate"),
)
if mibBuilder.loadTexts:
    alipFilStatStatsEntry.setStatus("mandatory")
_AlipFilStatStatsTemplate_Type = Counter32
_AlipFilStatStatsTemplate_Object = MibTableColumn
alipFilStatStatsTemplate = _AlipFilStatStatsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 20, 1, 1),
    _AlipFilStatStatsTemplate_Type()
)
alipFilStatStatsTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipFilStatStatsTemplate.setStatus("mandatory")
_AlipFilStatStatsInPkts_Type = Counter32
_AlipFilStatStatsInPkts_Object = MibTableColumn
alipFilStatStatsInPkts = _AlipFilStatStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 20, 1, 2),
    _AlipFilStatStatsInPkts_Type()
)
alipFilStatStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipFilStatStatsInPkts.setStatus("mandatory")
_AlipFilStatStatsOutPkts_Type = Counter32
_AlipFilStatStatsOutPkts_Object = MibTableColumn
alipFilStatStatsOutPkts = _AlipFilStatStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 20, 1, 3),
    _AlipFilStatStatsOutPkts_Type()
)
alipFilStatStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipFilStatStatsOutPkts.setStatus("mandatory")
_AlipFilDynStatsTable_Object = MibTable
alipFilDynStatsTable = _AlipFilDynStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 21)
)
if mibBuilder.loadTexts:
    alipFilDynStatsTable.setStatus("mandatory")
_AlipFilDynStatsEntry_Object = MibTableRow
alipFilDynStatsEntry = _AlipFilDynStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 21, 1)
)
alipFilDynStatsEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "alipFilDynStatsTemplate"),
)
if mibBuilder.loadTexts:
    alipFilDynStatsEntry.setStatus("mandatory")
_AlipFilDynStatsTemplate_Type = Counter32
_AlipFilDynStatsTemplate_Object = MibTableColumn
alipFilDynStatsTemplate = _AlipFilDynStatsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 21, 1, 1),
    _AlipFilDynStatsTemplate_Type()
)
alipFilDynStatsTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipFilDynStatsTemplate.setStatus("mandatory")
_AlipFilDynStatsInPkts_Type = Counter32
_AlipFilDynStatsInPkts_Object = MibTableColumn
alipFilDynStatsInPkts = _AlipFilDynStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 21, 1, 2),
    _AlipFilDynStatsInPkts_Type()
)
alipFilDynStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipFilDynStatsInPkts.setStatus("mandatory")
_AlipFilDynStatsOutPkts_Type = Counter32
_AlipFilDynStatsOutPkts_Object = MibTableColumn
alipFilDynStatsOutPkts = _AlipFilDynStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 21, 1, 3),
    _AlipFilDynStatsOutPkts_Type()
)
alipFilDynStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipFilDynStatsOutPkts.setStatus("mandatory")
_AlipFilDynStatsClear_Type = Integer32
_AlipFilDynStatsClear_Object = MibTableColumn
alipFilDynStatsClear = _AlipFilDynStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 21, 1, 4),
    _AlipFilDynStatsClear_Type()
)
alipFilDynStatsClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alipFilDynStatsClear.setStatus("mandatory")
_AlipTotalFilPacketForward_Type = Counter32
_AlipTotalFilPacketForward_Object = MibScalar
alipTotalFilPacketForward = _AlipTotalFilPacketForward_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 22),
    _AlipTotalFilPacketForward_Type()
)
alipTotalFilPacketForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipTotalFilPacketForward.setStatus("mandatory")
_AlipTotalFilPacketBlock_Type = Counter32
_AlipTotalFilPacketBlock_Object = MibScalar
alipTotalFilPacketBlock = _AlipTotalFilPacketBlock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 23),
    _AlipTotalFilPacketBlock_Type()
)
alipTotalFilPacketBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipTotalFilPacketBlock.setStatus("mandatory")
_AlipCurrentFilPacketForward_Type = Counter32
_AlipCurrentFilPacketForward_Object = MibScalar
alipCurrentFilPacketForward = _AlipCurrentFilPacketForward_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 24),
    _AlipCurrentFilPacketForward_Type()
)
alipCurrentFilPacketForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipCurrentFilPacketForward.setStatus("mandatory")
_AlipCurrentFilPacketBlock_Type = Counter32
_AlipCurrentFilPacketBlock_Object = MibScalar
alipCurrentFilPacketBlock = _AlipCurrentFilPacketBlock_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 25),
    _AlipCurrentFilPacketBlock_Type()
)
alipCurrentFilPacketBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alipCurrentFilPacketBlock.setStatus("mandatory")
_AlIpInterfaceTable_Object = MibTable
alIpInterfaceTable = _AlIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26)
)
if mibBuilder.loadTexts:
    alIpInterfaceTable.setStatus("mandatory")
_AlIpInterfaceEntry_Object = MibTableRow
alIpInterfaceEntry = _AlIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1)
)
alIpInterfaceEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "ipInterfaceNumber"),
    (0, "POWERHUB-TCPIP-MIB", "ipInterfaceAddress"),
)
if mibBuilder.loadTexts:
    alIpInterfaceEntry.setStatus("mandatory")
_IpInterfaceNumber_Type = Integer32
_IpInterfaceNumber_Object = MibTableColumn
ipInterfaceNumber = _IpInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 1),
    _IpInterfaceNumber_Type()
)
ipInterfaceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceNumber.setStatus("mandatory")
_IpInterfaceAddress_Type = IpAddress
_IpInterfaceAddress_Object = MibTableColumn
ipInterfaceAddress = _IpInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 2),
    _IpInterfaceAddress_Type()
)
ipInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceAddress.setStatus("mandatory")
_IpInterfaceSubnetMask_Type = IpAddress
_IpInterfaceSubnetMask_Object = MibTableColumn
ipInterfaceSubnetMask = _IpInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 3),
    _IpInterfaceSubnetMask_Type()
)
ipInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceSubnetMask.setStatus("mandatory")


class _IpInterfaceBroadCast_Type(Integer32):
    """Custom type ipInterfaceBroadCast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("br0", 1),
          ("br1", 2))
    )


_IpInterfaceBroadCast_Type.__name__ = "Integer32"
_IpInterfaceBroadCast_Object = MibTableColumn
ipInterfaceBroadCast = _IpInterfaceBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 4),
    _IpInterfaceBroadCast_Type()
)
ipInterfaceBroadCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceBroadCast.setStatus("mandatory")


class _IpInterfaceCost_Type(Integer32):
    """Custom type ipInterfaceCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_IpInterfaceCost_Type.__name__ = "Integer32"
_IpInterfaceCost_Object = MibTableColumn
ipInterfaceCost = _IpInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 5),
    _IpInterfaceCost_Type()
)
ipInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceCost.setStatus("mandatory")
_IpInterfaceDelete_Type = Integer32
_IpInterfaceDelete_Object = MibTableColumn
ipInterfaceDelete = _IpInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 6),
    _IpInterfaceDelete_Type()
)
ipInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceDelete.setStatus("mandatory")
_IpInterfaceMtu_Type = Integer32
_IpInterfaceMtu_Object = MibTableColumn
ipInterfaceMtu = _IpInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 7),
    _IpInterfaceMtu_Type()
)
ipInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceMtu.setStatus("mandatory")


class _IpInterfaceState_Type(Integer32):
    """Custom type ipInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_IpInterfaceState_Type.__name__ = "Integer32"
_IpInterfaceState_Object = MibTableColumn
ipInterfaceState = _IpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 8),
    _IpInterfaceState_Type()
)
ipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceState.setStatus("mandatory")
_IpInterfacePktsIn_Type = Counter32
_IpInterfacePktsIn_Object = MibTableColumn
ipInterfacePktsIn = _IpInterfacePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 9),
    _IpInterfacePktsIn_Type()
)
ipInterfacePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfacePktsIn.setStatus("mandatory")
_IpInterfaceOctetsIn_Type = Counter32
_IpInterfaceOctetsIn_Object = MibTableColumn
ipInterfaceOctetsIn = _IpInterfaceOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 10),
    _IpInterfaceOctetsIn_Type()
)
ipInterfaceOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceOctetsIn.setStatus("mandatory")
_IpInterfacePktsOut_Type = Counter32
_IpInterfacePktsOut_Object = MibTableColumn
ipInterfacePktsOut = _IpInterfacePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 11),
    _IpInterfacePktsOut_Type()
)
ipInterfacePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfacePktsOut.setStatus("mandatory")
_IpInterfaceOctetsOut_Type = Counter32
_IpInterfaceOctetsOut_Object = MibTableColumn
ipInterfaceOctetsOut = _IpInterfaceOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 26, 1, 12),
    _IpInterfaceOctetsOut_Type()
)
ipInterfaceOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceOctetsOut.setStatus("mandatory")
_AlIpRtCacheTable_Object = MibTable
alIpRtCacheTable = _AlIpRtCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 27)
)
if mibBuilder.loadTexts:
    alIpRtCacheTable.setStatus("mandatory")
_AlIpRtCacheEntry_Object = MibTableRow
alIpRtCacheEntry = _AlIpRtCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 27, 1)
)
alIpRtCacheEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "ipRtCachePort"),
    (0, "POWERHUB-TCPIP-MIB", "ipRtCacheDstAddress"),
)
if mibBuilder.loadTexts:
    alIpRtCacheEntry.setStatus("mandatory")
_IpRtCachePort_Type = Integer32
_IpRtCachePort_Object = MibTableColumn
ipRtCachePort = _IpRtCachePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 27, 1, 1),
    _IpRtCachePort_Type()
)
ipRtCachePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtCachePort.setStatus("mandatory")
_IpRtCacheDstAddress_Type = Integer32
_IpRtCacheDstAddress_Object = MibTableColumn
ipRtCacheDstAddress = _IpRtCacheDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 27, 1, 2),
    _IpRtCacheDstAddress_Type()
)
ipRtCacheDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtCacheDstAddress.setStatus("mandatory")
_IpRtCacheClear_Type = Integer32
_IpRtCacheClear_Object = MibTableColumn
ipRtCacheClear = _IpRtCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 27, 1, 3),
    _IpRtCacheClear_Type()
)
ipRtCacheClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipRtCacheClear.setStatus("mandatory")
_AlVlanIpInterfaceTable_Object = MibTable
alVlanIpInterfaceTable = _AlVlanIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28)
)
if mibBuilder.loadTexts:
    alVlanIpInterfaceTable.setStatus("mandatory")
_AlVlanIpInterfaceEntry_Object = MibTableRow
alVlanIpInterfaceEntry = _AlVlanIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1)
)
alVlanIpInterfaceEntry.setIndexNames(
    (0, "POWERHUB-TCPIP-MIB", "vlanIpInterfaceNameLen"),
    (0, "POWERHUB-TCPIP-MIB", "vlanIpInterfaceName"),
    (0, "POWERHUB-TCPIP-MIB", "vlanIpInterfaceAddress"),
)
if mibBuilder.loadTexts:
    alVlanIpInterfaceEntry.setStatus("mandatory")
_VlanIpInterfaceNameLen_Type = Integer32
_VlanIpInterfaceNameLen_Object = MibTableColumn
vlanIpInterfaceNameLen = _VlanIpInterfaceNameLen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 1),
    _VlanIpInterfaceNameLen_Type()
)
vlanIpInterfaceNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIpInterfaceNameLen.setStatus("mandatory")
_VlanIpInterfaceName_Type = DisplayString
_VlanIpInterfaceName_Object = MibTableColumn
vlanIpInterfaceName = _VlanIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 2),
    _VlanIpInterfaceName_Type()
)
vlanIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIpInterfaceName.setStatus("mandatory")
_VlanIpInterfaceAddress_Type = IpAddress
_VlanIpInterfaceAddress_Object = MibTableColumn
vlanIpInterfaceAddress = _VlanIpInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 3),
    _VlanIpInterfaceAddress_Type()
)
vlanIpInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIpInterfaceAddress.setStatus("mandatory")
_VlanIpInterfaceSubnetMask_Type = IpAddress
_VlanIpInterfaceSubnetMask_Object = MibTableColumn
vlanIpInterfaceSubnetMask = _VlanIpInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 4),
    _VlanIpInterfaceSubnetMask_Type()
)
vlanIpInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpInterfaceSubnetMask.setStatus("mandatory")


class _VlanIpInterfaceType_Type(Integer32):
    """Custom type vlanIpInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 4))
    )


_VlanIpInterfaceType_Type.__name__ = "Integer32"
_VlanIpInterfaceType_Object = MibTableColumn
vlanIpInterfaceType = _VlanIpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 5),
    _VlanIpInterfaceType_Type()
)
vlanIpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpInterfaceType.setStatus("mandatory")
_VlanIpInterfaceNeighborAddress_Type = IpAddress
_VlanIpInterfaceNeighborAddress_Object = MibTableColumn
vlanIpInterfaceNeighborAddress = _VlanIpInterfaceNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 6),
    _VlanIpInterfaceNeighborAddress_Type()
)
vlanIpInterfaceNeighborAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpInterfaceNeighborAddress.setStatus("mandatory")


class _VlanIpInterfaceRowStatus_Type(Integer32):
    """Custom type vlanIpInterfaceRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInservice", 2),
          ("notReady", 3))
    )


_VlanIpInterfaceRowStatus_Type.__name__ = "Integer32"
_VlanIpInterfaceRowStatus_Object = MibTableColumn
vlanIpInterfaceRowStatus = _VlanIpInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2, 6, 28, 1, 7),
    _VlanIpInterfaceRowStatus_Type()
)
vlanIpInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpInterfaceRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWERHUB-TCPIP-MIB",
    **{"fore": fore,
       "systems": systems,
       "lsd": lsd,
       "lsdproducts": lsdproducts,
       "lsdcommon": lsdcommon,
       "alrip": alrip,
       "alripControlType": alripControlType,
       "alRipNormalConfigTable": alRipNormalConfigTable,
       "alripNormalConfigEntry": alripNormalConfigEntry,
       "alripNormalConfigPort": alripNormalConfigPort,
       "alripNormalConfigTalk": alripNormalConfigTalk,
       "alripNormalConfigListen": alripNormalConfigListen,
       "alripNormalConfigPoison": alripNormalConfigPoison,
       "alripNormalConfigRptStaticRt": alripNormalConfigRptStaticRt,
       "alripNormalConfigRptDefaultRt": alripNormalConfigRptDefaultRt,
       "alripNormalConfigAccptDefaultRt": alripNormalConfigAccptDefaultRt,
       "alRipVLANConfigTable": alRipVLANConfigTable,
       "alripVLANConfigEntry": alripVLANConfigEntry,
       "alripVLANConfigNetNumber": alripVLANConfigNetNumber,
       "alripVLANConfigTalk": alripVLANConfigTalk,
       "alripVLANConfigListen": alripVLANConfigListen,
       "alripVLANConfigPoison": alripVLANConfigPoison,
       "alripVLANConfigRptStaticRt": alripVLANConfigRptStaticRt,
       "alripVLANConfigRptDefaultRt": alripVLANConfigRptDefaultRt,
       "alripVLANConfigAccptDefaultRt": alripVLANConfigAccptDefaultRt,
       "alripVLANConfigDelete": alripVLANConfigDelete,
       "alripStatsClear": alripStatsClear,
       "alRipStatPktsRcvd": alRipStatPktsRcvd,
       "alRipStatPktsXmitted": alRipStatPktsXmitted,
       "alRipStatReqsRcvd": alRipStatReqsRcvd,
       "alRipStatRespRcvd": alRipStatRespRcvd,
       "alRipStatReqsXmitted": alRipStatReqsXmitted,
       "alRipStatRespXmitted": alRipStatRespXmitted,
       "alRipStatRouteTimeOuts": alRipStatRouteTimeOuts,
       "alRipStatShortPkts": alRipStatShortPkts,
       "alRipStatBadVer": alRipStatBadVer,
       "alRipStatBadZeroes": alRipStatBadZeroes,
       "alRipStatBadSrcPort": alRipStatBadSrcPort,
       "alRipStatBadSrcIp": alRipStatBadSrcIp,
       "alRipStatPktsSelf": alRipStatPktsSelf,
       "alRipigUpdates": alRipigUpdates,
       "alRipStatPqueuePktsQueued": alRipStatPqueuePktsQueued,
       "alRipStatPqueueFreeQueue": alRipStatPqueueFreeQueue,
       "alRipStatTqueuePktsQueued": alRipStatTqueuePktsQueued,
       "alRipStatTqueueFreeQueue": alRipStatTqueueFreeQueue,
       "alRipDynPktsRcvd": alRipDynPktsRcvd,
       "alRipDynPktsXmitted": alRipDynPktsXmitted,
       "alRipDynReqsRcvd": alRipDynReqsRcvd,
       "alRipDynRespRcvd": alRipDynRespRcvd,
       "alRipDynReqsXmitted": alRipDynReqsXmitted,
       "alRipDynRespXmitted": alRipDynRespXmitted,
       "alRipDynRouteTimeOuts": alRipDynRouteTimeOuts,
       "alRipDynShortPkts": alRipDynShortPkts,
       "alRipDynBadVer": alRipDynBadVer,
       "alRipDynBadZeroes": alRipDynBadZeroes,
       "alRipDynBadSrcPort": alRipDynBadSrcPort,
       "alRipDynBadSrcIp": alRipDynBadSrcIp,
       "alRipDynPktsSelf": alRipDynPktsSelf,
       "alRipDynNumTrigUpdates": alRipDynNumTrigUpdates,
       "alRipDyntPqueuePktsQueued": alRipDyntPqueuePktsQueued,
       "alRipDynPqueueFreeQueue": alRipDynPqueueFreeQueue,
       "alRipDynTqueuePktsQueued": alRipDynTqueuePktsQueued,
       "alRipDynTqueueFreeQueue": alRipDynTqueueFreeQueue,
       "alRipAccptFilTable": alRipAccptFilTable,
       "ripAccptFilEntry": ripAccptFilEntry,
       "ripAccptFilNumber": ripAccptFilNumber,
       "ripAccptFilAddr": ripAccptFilAddr,
       "ripAccptFilMask": ripAccptFilMask,
       "ripAccptFilPort": ripAccptFilPort,
       "alRipReportFilTable": alRipReportFilTable,
       "ripReportFilEntry": ripReportFilEntry,
       "ripReportFilNumber": ripReportFilNumber,
       "ripReportFilAddr": ripReportFilAddr,
       "ripReportFilMask": ripReportFilMask,
       "ripReportFilPort": ripReportFilPort,
       "altcp": altcp,
       "alTcpConnIdleTime": alTcpConnIdleTime,
       "alTcpKeepAliveInt": alTcpKeepAliveInt,
       "alTcpDisconnectInt": alTcpDisconnectInt,
       "alTcpShortSegRcvd": alTcpShortSegRcvd,
       "alTcpStatsClear": alTcpStatsClear,
       "alTcpConnTable": alTcpConnTable,
       "alTcpConnEntry": alTcpConnEntry,
       "alTcpConnId": alTcpConnId,
       "alTcpConnState": alTcpConnState,
       "alTcpConnLocalAddress": alTcpConnLocalAddress,
       "alTcpConnLocalPort": alTcpConnLocalPort,
       "alTcpConnRemAddress": alTcpConnRemAddress,
       "alTcpConnRemPort": alTcpConnRemPort,
       "alTcpFilTable": alTcpFilTable,
       "tcpFilEntry": tcpFilEntry,
       "tcpFilNumber": tcpFilNumber,
       "tcpFilSrcAddr": tcpFilSrcAddr,
       "tcpFilSrcMask": tcpFilSrcMask,
       "tcpFilProtocol": tcpFilProtocol,
       "tcpFilDstPort": tcpFilDstPort,
       "alip": alip,
       "alArpTableClear": alArpTableClear,
       "alArpAge": alArpAge,
       "alArpStatReqsRcvd": alArpStatReqsRcvd,
       "alArpStatRepliesRcvd": alArpStatRepliesRcvd,
       "alArpStatInvalidOpcodes": alArpStatInvalidOpcodes,
       "alArpStatRequestsSent": alArpStatRequestsSent,
       "alArpStatRepliesSent": alArpStatRepliesSent,
       "alArpStatProxyReplies": alArpStatProxyReplies,
       "alArpDynReqsRcvd": alArpDynReqsRcvd,
       "alArpDynRepliesRcvd": alArpDynRepliesRcvd,
       "alArpDynInvalidOpcodes": alArpDynInvalidOpcodes,
       "alArpDynRequestsSent": alArpDynRequestsSent,
       "alArpDynRepliesSent": alArpDynRepliesSent,
       "alArpDynProxyReplies": alArpDynProxyReplies,
       "alArpStatsClear": alArpStatsClear,
       "alArpProxyTable": alArpProxyTable,
       "arpProxyEntry": arpProxyEntry,
       "arpProxyPort": arpProxyPort,
       "arpProxyEnable": arpProxyEnable,
       "alIpTemplateTable": alIpTemplateTable,
       "alipTemplateEntry": alipTemplateEntry,
       "alipTemplateNumber": alipTemplateNumber,
       "alipTemplateDelete": alipTemplateDelete,
       "alipTemplateAction": alipTemplateAction,
       "alipTemplateSrcAddr": alipTemplateSrcAddr,
       "alipTemplateSrcMask": alipTemplateSrcMask,
       "alipTemplateDstAddr": alipTemplateDstAddr,
       "alipTemplateDstMask": alipTemplateDstMask,
       "alipTemplateProtocol": alipTemplateProtocol,
       "alipTemplateOperator": alipTemplateOperator,
       "alipTemplateDstPort": alipTemplateDstPort,
       "alIpRuleTable": alIpRuleTable,
       "alipRuleEntry": alipRuleEntry,
       "alipRuleNumber": alipRuleNumber,
       "alipRuleDelete": alipRuleDelete,
       "alipRuleTemplates": alipRuleTemplates,
       "alipAcsCtrlTable": alipAcsCtrlTable,
       "alipAcsCtrlEntry": alipAcsCtrlEntry,
       "alipAcsCtrlPort": alipAcsCtrlPort,
       "alipAcsCtrlDelete": alipAcsCtrlDelete,
       "alipAcsCtrlSourceRule": alipAcsCtrlSourceRule,
       "alipAcsCtrlDestRule": alipAcsCtrlDestRule,
       "alipFilStatStatsTable": alipFilStatStatsTable,
       "alipFilStatStatsEntry": alipFilStatStatsEntry,
       "alipFilStatStatsTemplate": alipFilStatStatsTemplate,
       "alipFilStatStatsInPkts": alipFilStatStatsInPkts,
       "alipFilStatStatsOutPkts": alipFilStatStatsOutPkts,
       "alipFilDynStatsTable": alipFilDynStatsTable,
       "alipFilDynStatsEntry": alipFilDynStatsEntry,
       "alipFilDynStatsTemplate": alipFilDynStatsTemplate,
       "alipFilDynStatsInPkts": alipFilDynStatsInPkts,
       "alipFilDynStatsOutPkts": alipFilDynStatsOutPkts,
       "alipFilDynStatsClear": alipFilDynStatsClear,
       "alipTotalFilPacketForward": alipTotalFilPacketForward,
       "alipTotalFilPacketBlock": alipTotalFilPacketBlock,
       "alipCurrentFilPacketForward": alipCurrentFilPacketForward,
       "alipCurrentFilPacketBlock": alipCurrentFilPacketBlock,
       "alIpInterfaceTable": alIpInterfaceTable,
       "alIpInterfaceEntry": alIpInterfaceEntry,
       "ipInterfaceNumber": ipInterfaceNumber,
       "ipInterfaceAddress": ipInterfaceAddress,
       "ipInterfaceSubnetMask": ipInterfaceSubnetMask,
       "ipInterfaceBroadCast": ipInterfaceBroadCast,
       "ipInterfaceCost": ipInterfaceCost,
       "ipInterfaceDelete": ipInterfaceDelete,
       "ipInterfaceMtu": ipInterfaceMtu,
       "ipInterfaceState": ipInterfaceState,
       "ipInterfacePktsIn": ipInterfacePktsIn,
       "ipInterfaceOctetsIn": ipInterfaceOctetsIn,
       "ipInterfacePktsOut": ipInterfacePktsOut,
       "ipInterfaceOctetsOut": ipInterfaceOctetsOut,
       "alIpRtCacheTable": alIpRtCacheTable,
       "alIpRtCacheEntry": alIpRtCacheEntry,
       "ipRtCachePort": ipRtCachePort,
       "ipRtCacheDstAddress": ipRtCacheDstAddress,
       "ipRtCacheClear": ipRtCacheClear,
       "alVlanIpInterfaceTable": alVlanIpInterfaceTable,
       "alVlanIpInterfaceEntry": alVlanIpInterfaceEntry,
       "vlanIpInterfaceNameLen": vlanIpInterfaceNameLen,
       "vlanIpInterfaceName": vlanIpInterfaceName,
       "vlanIpInterfaceAddress": vlanIpInterfaceAddress,
       "vlanIpInterfaceSubnetMask": vlanIpInterfaceSubnetMask,
       "vlanIpInterfaceType": vlanIpInterfaceType,
       "vlanIpInterfaceNeighborAddress": vlanIpInterfaceNeighborAddress,
       "vlanIpInterfaceRowStatus": vlanIpInterfaceRowStatus}
)
