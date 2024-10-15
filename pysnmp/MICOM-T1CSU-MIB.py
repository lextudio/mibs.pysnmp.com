# SNMP MIB module (MICOM-T1CSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-T1CSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:51 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_t1csu_ObjectIdentity = ObjectIdentity
micom_t1csu = _Micom_t1csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26)
)
_T1csu_configuration_ObjectIdentity = ObjectIdentity
t1csu_configuration = _T1csu_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1)
)
_McmT1CsuCfgGroup_ObjectIdentity = ObjectIdentity
mcmT1CsuCfgGroup = _McmT1CsuCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1)
)


class _McmT1CsuCfgLineBuildOut_Type(Integer32):
    """Custom type mcmT1CsuCfgLineBuildOut based on Integer32"""
    defaultValue = 6

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
        *(("dist-0-133-feet", 1),
          ("dist-133-266-feet", 2),
          ("dist-266-399-feet", 3),
          ("dist-399-533-feet", 4),
          ("dist-533-655-feet", 5),
          ("neg-15-db", 7),
          ("neg-22pt5-db", 8),
          ("neg-7pt5-db", 6))
    )


_McmT1CsuCfgLineBuildOut_Type.__name__ = "Integer32"
_McmT1CsuCfgLineBuildOut_Object = MibScalar
mcmT1CsuCfgLineBuildOut = _McmT1CsuCfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 1),
    _McmT1CsuCfgLineBuildOut_Type()
)
mcmT1CsuCfgLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgLineBuildOut.setStatus("deprecated")


class _McmT1CsuCfgFrameFmt_Type(Integer32):
    """Custom type mcmT1CsuCfgFrameFmt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4FramingMode", 1),
          ("esfFramingMode", 2))
    )


_McmT1CsuCfgFrameFmt_Type.__name__ = "Integer32"
_McmT1CsuCfgFrameFmt_Object = MibScalar
mcmT1CsuCfgFrameFmt = _McmT1CsuCfgFrameFmt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 2),
    _McmT1CsuCfgFrameFmt_Type()
)
mcmT1CsuCfgFrameFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgFrameFmt.setStatus("deprecated")


class _McmT1CsuCfgTxIdleCode_Type(Integer32):
    """Custom type mcmT1CsuCfgTxIdleCode based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuCfgTxIdleCode_Type.__name__ = "Integer32"
_McmT1CsuCfgTxIdleCode_Object = MibScalar
mcmT1CsuCfgTxIdleCode = _McmT1CsuCfgTxIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 3),
    _McmT1CsuCfgTxIdleCode_Type()
)
mcmT1CsuCfgTxIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgTxIdleCode.setStatus("deprecated")


class _McmT1CsuCfgTxRx0CodeSuppress_Type(Integer32):
    """Custom type mcmT1CsuCfgTxRx0CodeSuppress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b8zsDisable", 1),
          ("b8zsEnable", 2))
    )


_McmT1CsuCfgTxRx0CodeSuppress_Type.__name__ = "Integer32"
_McmT1CsuCfgTxRx0CodeSuppress_Object = MibScalar
mcmT1CsuCfgTxRx0CodeSuppress = _McmT1CsuCfgTxRx0CodeSuppress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 4),
    _McmT1CsuCfgTxRx0CodeSuppress_Type()
)
mcmT1CsuCfgTxRx0CodeSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgTxRx0CodeSuppress.setStatus("deprecated")


class _McmT1CsuCfgTxB7ZeroSuppress_Type(Integer32):
    """Custom type mcmT1CsuCfgTxB7ZeroSuppress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b7zsDisable", 1),
          ("b7zsEnable", 2))
    )


_McmT1CsuCfgTxB7ZeroSuppress_Type.__name__ = "Integer32"
_McmT1CsuCfgTxB7ZeroSuppress_Object = MibScalar
mcmT1CsuCfgTxB7ZeroSuppress = _McmT1CsuCfgTxB7ZeroSuppress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 5),
    _McmT1CsuCfgTxB7ZeroSuppress_Type()
)
mcmT1CsuCfgTxB7ZeroSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgTxB7ZeroSuppress.setStatus("deprecated")


class _McmT1CsuCfgTxRxClkSource_Type(Integer32):
    """Custom type mcmT1CsuCfgTxRxClkSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClockingSource", 2),
          ("internalClockingSource", 1))
    )


_McmT1CsuCfgTxRxClkSource_Type.__name__ = "Integer32"
_McmT1CsuCfgTxRxClkSource_Object = MibScalar
mcmT1CsuCfgTxRxClkSource = _McmT1CsuCfgTxRxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 6),
    _McmT1CsuCfgTxRxClkSource_Type()
)
mcmT1CsuCfgTxRxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgTxRxClkSource.setStatus("deprecated")


class _McmT1CsuCfgDS0BasicRate_Type(Integer32):
    """Custom type mcmT1CsuCfgDS0BasicRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicRate-56K", 2),
          ("basicRate-64K", 1))
    )


_McmT1CsuCfgDS0BasicRate_Type.__name__ = "Integer32"
_McmT1CsuCfgDS0BasicRate_Object = MibScalar
mcmT1CsuCfgDS0BasicRate = _McmT1CsuCfgDS0BasicRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 7),
    _McmT1CsuCfgDS0BasicRate_Type()
)
mcmT1CsuCfgDS0BasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgDS0BasicRate.setStatus("deprecated")


class _McmT1CsuCfgDS0Connection_Type(DisplayString):
    """Custom type mcmT1CsuCfgDS0Connection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 73),
    )


_McmT1CsuCfgDS0Connection_Type.__name__ = "DisplayString"
_McmT1CsuCfgDS0Connection_Object = MibScalar
mcmT1CsuCfgDS0Connection = _McmT1CsuCfgDS0Connection_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 8),
    _McmT1CsuCfgDS0Connection_Type()
)
mcmT1CsuCfgDS0Connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgDS0Connection.setStatus("deprecated")


class _McmT1CsuCfgLocalLoopback_Type(Integer32):
    """Custom type mcmT1CsuCfgLocalLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmT1CsuCfgLocalLoopback_Type.__name__ = "Integer32"
_McmT1CsuCfgLocalLoopback_Object = MibScalar
mcmT1CsuCfgLocalLoopback = _McmT1CsuCfgLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 9),
    _McmT1CsuCfgLocalLoopback_Type()
)
mcmT1CsuCfgLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgLocalLoopback.setStatus("deprecated")


class _McmT1CsuCfgRemoteLoopback_Type(Integer32):
    """Custom type mcmT1CsuCfgRemoteLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmT1CsuCfgRemoteLoopback_Type.__name__ = "Integer32"
_McmT1CsuCfgRemoteLoopback_Object = MibScalar
mcmT1CsuCfgRemoteLoopback = _McmT1CsuCfgRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 10),
    _McmT1CsuCfgRemoteLoopback_Type()
)
mcmT1CsuCfgRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgRemoteLoopback.setStatus("deprecated")


class _McmT1CsuCfgPayloadLoopback_Type(Integer32):
    """Custom type mcmT1CsuCfgPayloadLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmT1CsuCfgPayloadLoopback_Type.__name__ = "Integer32"
_McmT1CsuCfgPayloadLoopback_Object = MibScalar
mcmT1CsuCfgPayloadLoopback = _McmT1CsuCfgPayloadLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 11),
    _McmT1CsuCfgPayloadLoopback_Type()
)
mcmT1CsuCfgPayloadLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgPayloadLoopback.setStatus("deprecated")


class _McmT1CsuCfgFramerLoopback_Type(Integer32):
    """Custom type mcmT1CsuCfgFramerLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmT1CsuCfgFramerLoopback_Type.__name__ = "Integer32"
_McmT1CsuCfgFramerLoopback_Object = MibScalar
mcmT1CsuCfgFramerLoopback = _McmT1CsuCfgFramerLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 12),
    _McmT1CsuCfgFramerLoopback_Type()
)
mcmT1CsuCfgFramerLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgFramerLoopback.setStatus("deprecated")


class _McmT1CsuCfgTransmitLoopUp_Type(Integer32):
    """Custom type mcmT1CsuCfgTransmitLoopUp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmT1CsuCfgTransmitLoopUp_Type.__name__ = "Integer32"
_McmT1CsuCfgTransmitLoopUp_Object = MibScalar
mcmT1CsuCfgTransmitLoopUp = _McmT1CsuCfgTransmitLoopUp_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 13),
    _McmT1CsuCfgTransmitLoopUp_Type()
)
mcmT1CsuCfgTransmitLoopUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgTransmitLoopUp.setStatus("deprecated")


class _McmT1CsuCfgTransmitLoopDown_Type(Integer32):
    """Custom type mcmT1CsuCfgTransmitLoopDown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmT1CsuCfgTransmitLoopDown_Type.__name__ = "Integer32"
_McmT1CsuCfgTransmitLoopDown_Object = MibScalar
mcmT1CsuCfgTransmitLoopDown = _McmT1CsuCfgTransmitLoopDown_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 14),
    _McmT1CsuCfgTransmitLoopDown_Type()
)
mcmT1CsuCfgTransmitLoopDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1CsuCfgTransmitLoopDown.setStatus("deprecated")
_NvmT1CsuCfgGroup_ObjectIdentity = ObjectIdentity
nvmT1CsuCfgGroup = _NvmT1CsuCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2)
)


class _NvmT1CsuCfgLineBuildOut_Type(Integer32):
    """Custom type nvmT1CsuCfgLineBuildOut based on Integer32"""
    defaultValue = 6

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
        *(("dist-0-133-feet", 1),
          ("dist-133-266-feet", 2),
          ("dist-266-399-feet", 3),
          ("dist-399-533-feet", 4),
          ("dist-533-655-feet", 5),
          ("neg-15-db", 7),
          ("neg-22pt5-db", 8),
          ("neg-7pt5-db", 6))
    )


_NvmT1CsuCfgLineBuildOut_Type.__name__ = "Integer32"
_NvmT1CsuCfgLineBuildOut_Object = MibScalar
nvmT1CsuCfgLineBuildOut = _NvmT1CsuCfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 1),
    _NvmT1CsuCfgLineBuildOut_Type()
)
nvmT1CsuCfgLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgLineBuildOut.setStatus("obsolete")


class _NvmT1CsuCfgFrameFmt_Type(Integer32):
    """Custom type nvmT1CsuCfgFrameFmt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4FramingMode", 1),
          ("esfFramingMode", 2))
    )


_NvmT1CsuCfgFrameFmt_Type.__name__ = "Integer32"
_NvmT1CsuCfgFrameFmt_Object = MibScalar
nvmT1CsuCfgFrameFmt = _NvmT1CsuCfgFrameFmt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 2),
    _NvmT1CsuCfgFrameFmt_Type()
)
nvmT1CsuCfgFrameFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgFrameFmt.setStatus("obsolete")


class _NvmT1CsuCfgTxIdleCode_Type(Integer32):
    """Custom type nvmT1CsuCfgTxIdleCode based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmT1CsuCfgTxIdleCode_Type.__name__ = "Integer32"
_NvmT1CsuCfgTxIdleCode_Object = MibScalar
nvmT1CsuCfgTxIdleCode = _NvmT1CsuCfgTxIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 3),
    _NvmT1CsuCfgTxIdleCode_Type()
)
nvmT1CsuCfgTxIdleCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgTxIdleCode.setStatus("obsolete")


class _NvmT1CsuCfgTxRx0CodeSuppress_Type(Integer32):
    """Custom type nvmT1CsuCfgTxRx0CodeSuppress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b8zsDisable", 1),
          ("b8zsEnable", 2))
    )


_NvmT1CsuCfgTxRx0CodeSuppress_Type.__name__ = "Integer32"
_NvmT1CsuCfgTxRx0CodeSuppress_Object = MibScalar
nvmT1CsuCfgTxRx0CodeSuppress = _NvmT1CsuCfgTxRx0CodeSuppress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 4),
    _NvmT1CsuCfgTxRx0CodeSuppress_Type()
)
nvmT1CsuCfgTxRx0CodeSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgTxRx0CodeSuppress.setStatus("obsolete")


class _NvmT1CsuCfgTxB7ZeroSuppress_Type(Integer32):
    """Custom type nvmT1CsuCfgTxB7ZeroSuppress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b7zsDisable", 1),
          ("b7zsEnable", 2))
    )


_NvmT1CsuCfgTxB7ZeroSuppress_Type.__name__ = "Integer32"
_NvmT1CsuCfgTxB7ZeroSuppress_Object = MibScalar
nvmT1CsuCfgTxB7ZeroSuppress = _NvmT1CsuCfgTxB7ZeroSuppress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 5),
    _NvmT1CsuCfgTxB7ZeroSuppress_Type()
)
nvmT1CsuCfgTxB7ZeroSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgTxB7ZeroSuppress.setStatus("obsolete")


class _NvmT1CsuCfgTxRxClkSource_Type(Integer32):
    """Custom type nvmT1CsuCfgTxRxClkSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClockingSource", 2),
          ("internalClockingSource", 1))
    )


_NvmT1CsuCfgTxRxClkSource_Type.__name__ = "Integer32"
_NvmT1CsuCfgTxRxClkSource_Object = MibScalar
nvmT1CsuCfgTxRxClkSource = _NvmT1CsuCfgTxRxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 6),
    _NvmT1CsuCfgTxRxClkSource_Type()
)
nvmT1CsuCfgTxRxClkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgTxRxClkSource.setStatus("obsolete")


class _NvmT1CsuCfgDS0BasicRate_Type(Integer32):
    """Custom type nvmT1CsuCfgDS0BasicRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicRate-56K", 2),
          ("basicRate-64K", 1))
    )


_NvmT1CsuCfgDS0BasicRate_Type.__name__ = "Integer32"
_NvmT1CsuCfgDS0BasicRate_Object = MibScalar
nvmT1CsuCfgDS0BasicRate = _NvmT1CsuCfgDS0BasicRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 7),
    _NvmT1CsuCfgDS0BasicRate_Type()
)
nvmT1CsuCfgDS0BasicRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgDS0BasicRate.setStatus("obsolete")


class _NvmT1CsuCfgDS0Connection_Type(DisplayString):
    """Custom type nvmT1CsuCfgDS0Connection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 73),
    )


_NvmT1CsuCfgDS0Connection_Type.__name__ = "DisplayString"
_NvmT1CsuCfgDS0Connection_Object = MibScalar
nvmT1CsuCfgDS0Connection = _NvmT1CsuCfgDS0Connection_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 8),
    _NvmT1CsuCfgDS0Connection_Type()
)
nvmT1CsuCfgDS0Connection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgDS0Connection.setStatus("obsolete")


class _NvmT1CsuCfgLocalLoopback_Type(Integer32):
    """Custom type nvmT1CsuCfgLocalLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmT1CsuCfgLocalLoopback_Type.__name__ = "Integer32"
_NvmT1CsuCfgLocalLoopback_Object = MibScalar
nvmT1CsuCfgLocalLoopback = _NvmT1CsuCfgLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 9),
    _NvmT1CsuCfgLocalLoopback_Type()
)
nvmT1CsuCfgLocalLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgLocalLoopback.setStatus("obsolete")


class _NvmT1CsuCfgRemoteLoopback_Type(Integer32):
    """Custom type nvmT1CsuCfgRemoteLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmT1CsuCfgRemoteLoopback_Type.__name__ = "Integer32"
_NvmT1CsuCfgRemoteLoopback_Object = MibScalar
nvmT1CsuCfgRemoteLoopback = _NvmT1CsuCfgRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 10),
    _NvmT1CsuCfgRemoteLoopback_Type()
)
nvmT1CsuCfgRemoteLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgRemoteLoopback.setStatus("obsolete")


class _NvmT1CsuCfgPayloadLoopback_Type(Integer32):
    """Custom type nvmT1CsuCfgPayloadLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmT1CsuCfgPayloadLoopback_Type.__name__ = "Integer32"
_NvmT1CsuCfgPayloadLoopback_Object = MibScalar
nvmT1CsuCfgPayloadLoopback = _NvmT1CsuCfgPayloadLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 11),
    _NvmT1CsuCfgPayloadLoopback_Type()
)
nvmT1CsuCfgPayloadLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgPayloadLoopback.setStatus("obsolete")


class _NvmT1CsuCfgFramerLoopback_Type(Integer32):
    """Custom type nvmT1CsuCfgFramerLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmT1CsuCfgFramerLoopback_Type.__name__ = "Integer32"
_NvmT1CsuCfgFramerLoopback_Object = MibScalar
nvmT1CsuCfgFramerLoopback = _NvmT1CsuCfgFramerLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 12),
    _NvmT1CsuCfgFramerLoopback_Type()
)
nvmT1CsuCfgFramerLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgFramerLoopback.setStatus("obsolete")


class _NvmT1CsuCfgTransmitLoopUp_Type(Integer32):
    """Custom type nvmT1CsuCfgTransmitLoopUp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmT1CsuCfgTransmitLoopUp_Type.__name__ = "Integer32"
_NvmT1CsuCfgTransmitLoopUp_Object = MibScalar
nvmT1CsuCfgTransmitLoopUp = _NvmT1CsuCfgTransmitLoopUp_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 13),
    _NvmT1CsuCfgTransmitLoopUp_Type()
)
nvmT1CsuCfgTransmitLoopUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgTransmitLoopUp.setStatus("obsolete")


class _NvmT1CsuCfgTransmitLoopDown_Type(Integer32):
    """Custom type nvmT1CsuCfgTransmitLoopDown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmT1CsuCfgTransmitLoopDown_Type.__name__ = "Integer32"
_NvmT1CsuCfgTransmitLoopDown_Object = MibScalar
nvmT1CsuCfgTransmitLoopDown = _NvmT1CsuCfgTransmitLoopDown_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 14),
    _NvmT1CsuCfgTransmitLoopDown_Type()
)
nvmT1CsuCfgTransmitLoopDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmT1CsuCfgTransmitLoopDown.setStatus("obsolete")
_T1csu_status_ObjectIdentity = ObjectIdentity
t1csu_status = _T1csu_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2)
)


class _McmT1CsuStatusT1LineSpeed_Type(Integer32):
    """Custom type mcmT1CsuStatusT1LineSpeed based on Integer32"""
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
              49)
        )
    )
    namedValues = NamedValues(
        *(("idle", 49),
          ("ls-10ds0Times56K-560K", 34),
          ("ls-10ds0Times64K-640K", 10),
          ("ls-11ds0Times56K-616K", 35),
          ("ls-11ds0Times64K-704K", 11),
          ("ls-12ds0Times56K-672K", 36),
          ("ls-12ds0Times64K-768K", 12),
          ("ls-13ds0Times56K-728K", 37),
          ("ls-13ds0Times64K-832K", 13),
          ("ls-14ds0Times56K-784K", 38),
          ("ls-14ds0Times64K-896K", 14),
          ("ls-15ds0Times56K-840K", 39),
          ("ls-15ds0Times64K-960K", 15),
          ("ls-16ds0Times56K-896K", 40),
          ("ls-16ds0Times64K-1024K", 16),
          ("ls-17ds0Times56K-952K", 41),
          ("ls-17ds0Times64K-1088K", 17),
          ("ls-18ds0Times56K-1008K", 42),
          ("ls-18ds0Times64K-1152K", 18),
          ("ls-19ds0Times56K-1064K", 43),
          ("ls-19ds0Times64K-1216K", 19),
          ("ls-1ds0Times56K-56K", 25),
          ("ls-1ds0Times64K-64K", 1),
          ("ls-20ds0Times56K-1120K", 44),
          ("ls-20ds0Times64K-1280K", 20),
          ("ls-21ds0Times56K-1176K", 45),
          ("ls-21ds0Times64K-1344K", 21),
          ("ls-22ds0Times56K-1232K", 46),
          ("ls-22ds0Times64K-1408K", 22),
          ("ls-23ds0Times56K-1288K", 47),
          ("ls-23ds0Times64K-1472K", 23),
          ("ls-24ds0Times56K-1344K", 48),
          ("ls-24ds0Times64K-1536K", 24),
          ("ls-2ds0Times56K-112K", 26),
          ("ls-2ds0Times64K-128K", 2),
          ("ls-3ds0Times56K-168K", 27),
          ("ls-3ds0Times64K-192K", 3),
          ("ls-4ds0Times56K-224K", 28),
          ("ls-4ds0Times64K-256K", 4),
          ("ls-5ds0Times56K-280K", 29),
          ("ls-5ds0Times64K-320K", 5),
          ("ls-6ds0Times56K-336K", 30),
          ("ls-6ds0Times64K-384K", 6),
          ("ls-7ds0Times56K-392K", 31),
          ("ls-7ds0Times64K-448K", 7),
          ("ls-8ds0Times56K-448K", 32),
          ("ls-8ds0Times64K-512K", 8),
          ("ls-9ds0Times56K-504K", 33),
          ("ls-9ds0Times64K-576K", 9))
    )


_McmT1CsuStatusT1LineSpeed_Type.__name__ = "Integer32"
_McmT1CsuStatusT1LineSpeed_Object = MibScalar
mcmT1CsuStatusT1LineSpeed = _McmT1CsuStatusT1LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 1),
    _McmT1CsuStatusT1LineSpeed_Type()
)
mcmT1CsuStatusT1LineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusT1LineSpeed.setStatus("deprecated")
_McmT1CsuCntlRegStatusGroup_ObjectIdentity = ObjectIdentity
mcmT1CsuCntlRegStatusGroup = _McmT1CsuCntlRegStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2)
)


class _McmT1CsuStatusCntlReg1_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg1_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg1_Object = MibScalar
mcmT1CsuStatusCntlReg1 = _McmT1CsuStatusCntlReg1_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 1),
    _McmT1CsuStatusCntlReg1_Type()
)
mcmT1CsuStatusCntlReg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg1.setStatus("deprecated")


class _McmT1CsuStatusCntlReg2_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg2_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg2_Object = MibScalar
mcmT1CsuStatusCntlReg2 = _McmT1CsuStatusCntlReg2_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 2),
    _McmT1CsuStatusCntlReg2_Type()
)
mcmT1CsuStatusCntlReg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg2.setStatus("deprecated")


class _McmT1CsuStatusCntlReg3_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg3_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg3_Object = MibScalar
mcmT1CsuStatusCntlReg3 = _McmT1CsuStatusCntlReg3_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 3),
    _McmT1CsuStatusCntlReg3_Type()
)
mcmT1CsuStatusCntlReg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg3.setStatus("deprecated")


class _McmT1CsuStatusCntlReg4_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg4_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg4_Object = MibScalar
mcmT1CsuStatusCntlReg4 = _McmT1CsuStatusCntlReg4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 4),
    _McmT1CsuStatusCntlReg4_Type()
)
mcmT1CsuStatusCntlReg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg4.setStatus("deprecated")


class _McmT1CsuStatusCntlReg5_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg5_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg5_Object = MibScalar
mcmT1CsuStatusCntlReg5 = _McmT1CsuStatusCntlReg5_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 5),
    _McmT1CsuStatusCntlReg5_Type()
)
mcmT1CsuStatusCntlReg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg5.setStatus("deprecated")


class _McmT1CsuStatusCntlReg6_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg6_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg6_Object = MibScalar
mcmT1CsuStatusCntlReg6 = _McmT1CsuStatusCntlReg6_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 6),
    _McmT1CsuStatusCntlReg6_Type()
)
mcmT1CsuStatusCntlReg6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg6.setStatus("deprecated")


class _McmT1CsuStatusCntlReg7_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg7_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg7_Object = MibScalar
mcmT1CsuStatusCntlReg7 = _McmT1CsuStatusCntlReg7_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 7),
    _McmT1CsuStatusCntlReg7_Type()
)
mcmT1CsuStatusCntlReg7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg7.setStatus("deprecated")


class _McmT1CsuStatusCntlReg8_Type(Integer32):
    """Custom type mcmT1CsuStatusCntlReg8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuStatusCntlReg8_Type.__name__ = "Integer32"
_McmT1CsuStatusCntlReg8_Object = MibScalar
mcmT1CsuStatusCntlReg8 = _McmT1CsuStatusCntlReg8_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 8),
    _McmT1CsuStatusCntlReg8_Type()
)
mcmT1CsuStatusCntlReg8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuStatusCntlReg8.setStatus("deprecated")
_McmT1CsuGenStatusGroup_ObjectIdentity = ObjectIdentity
mcmT1CsuGenStatusGroup = _McmT1CsuGenStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3)
)


class _McmT1CsuGenStatusLineStatus_Type(Integer32):
    """Custom type mcmT1CsuGenStatusLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmMode", 2),
          ("operational", 1),
          ("testMode", 3))
    )


_McmT1CsuGenStatusLineStatus_Type.__name__ = "Integer32"
_McmT1CsuGenStatusLineStatus_Object = MibScalar
mcmT1CsuGenStatusLineStatus = _McmT1CsuGenStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 1),
    _McmT1CsuGenStatusLineStatus_Type()
)
mcmT1CsuGenStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusLineStatus.setStatus("deprecated")


class _McmT1CsuGenStatusRedAlarm_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedAlarm", 2),
          ("redAlarm", 1))
    )


_McmT1CsuGenStatusRedAlarm_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRedAlarm_Object = MibScalar
mcmT1CsuGenStatusRedAlarm = _McmT1CsuGenStatusRedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 2),
    _McmT1CsuGenStatusRedAlarm_Type()
)
mcmT1CsuGenStatusRedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRedAlarm.setStatus("deprecated")


class _McmT1CsuGenStatusYellowAlarm_Type(Integer32):
    """Custom type mcmT1CsuGenStatusYellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noYellowAlarm", 2),
          ("yellowAlarm", 1))
    )


_McmT1CsuGenStatusYellowAlarm_Type.__name__ = "Integer32"
_McmT1CsuGenStatusYellowAlarm_Object = MibScalar
mcmT1CsuGenStatusYellowAlarm = _McmT1CsuGenStatusYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 3),
    _McmT1CsuGenStatusYellowAlarm_Type()
)
mcmT1CsuGenStatusYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusYellowAlarm.setStatus("deprecated")


class _McmT1CsuGenStatusBlueAlarm_Type(Integer32):
    """Custom type mcmT1CsuGenStatusBlueAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blueAlarm", 1),
          ("noBlueAlarm", 2))
    )


_McmT1CsuGenStatusBlueAlarm_Type.__name__ = "Integer32"
_McmT1CsuGenStatusBlueAlarm_Object = MibScalar
mcmT1CsuGenStatusBlueAlarm = _McmT1CsuGenStatusBlueAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 4),
    _McmT1CsuGenStatusBlueAlarm_Type()
)
mcmT1CsuGenStatusBlueAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusBlueAlarm.setStatus("deprecated")


class _McmT1CsuGenStatusRxLevel_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxLevel based on Integer32"""
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
        *(("lessThan-neg22pt5db", 4),
          ("neg15db-to-neg22pt5db", 3),
          ("neg7pt5db-to-neg15db", 2),
          ("plus2db-to-neg7pt5db", 1))
    )


_McmT1CsuGenStatusRxLevel_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxLevel_Object = MibScalar
mcmT1CsuGenStatusRxLevel = _McmT1CsuGenStatusRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 5),
    _McmT1CsuGenStatusRxLevel_Type()
)
mcmT1CsuGenStatusRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxLevel.setStatus("deprecated")


class _McmT1CsuGenStatusRxElasStrFull_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxElasStrFull based on Integer32"""
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


_McmT1CsuGenStatusRxElasStrFull_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxElasStrFull_Object = MibScalar
mcmT1CsuGenStatusRxElasStrFull = _McmT1CsuGenStatusRxElasStrFull_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 6),
    _McmT1CsuGenStatusRxElasStrFull_Type()
)
mcmT1CsuGenStatusRxElasStrFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxElasStrFull.setStatus("deprecated")


class _McmT1CsuGenStatusRxElasStrEmpty_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxElasStrEmpty based on Integer32"""
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


_McmT1CsuGenStatusRxElasStrEmpty_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxElasStrEmpty_Object = MibScalar
mcmT1CsuGenStatusRxElasStrEmpty = _McmT1CsuGenStatusRxElasStrEmpty_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 7),
    _McmT1CsuGenStatusRxElasStrEmpty_Type()
)
mcmT1CsuGenStatusRxElasStrEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxElasStrEmpty.setStatus("deprecated")


class _McmT1CsuGenStatusRxPlsDensViolate_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxPlsDensViolate based on Integer32"""
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


_McmT1CsuGenStatusRxPlsDensViolate_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxPlsDensViolate_Object = MibScalar
mcmT1CsuGenStatusRxPlsDensViolate = _McmT1CsuGenStatusRxPlsDensViolate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 8),
    _McmT1CsuGenStatusRxPlsDensViolate_Type()
)
mcmT1CsuGenStatusRxPlsDensViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxPlsDensViolate.setStatus("deprecated")


class _McmT1CsuGenStatusTxPlsDensViolate_Type(Integer32):
    """Custom type mcmT1CsuGenStatusTxPlsDensViolate based on Integer32"""
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


_McmT1CsuGenStatusTxPlsDensViolate_Type.__name__ = "Integer32"
_McmT1CsuGenStatusTxPlsDensViolate_Object = MibScalar
mcmT1CsuGenStatusTxPlsDensViolate = _McmT1CsuGenStatusTxPlsDensViolate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 9),
    _McmT1CsuGenStatusTxPlsDensViolate_Type()
)
mcmT1CsuGenStatusTxPlsDensViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusTxPlsDensViolate.setStatus("deprecated")


class _McmT1CsuGenStatusRxCarrierLoss_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxCarrierLoss based on Integer32"""
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


_McmT1CsuGenStatusRxCarrierLoss_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxCarrierLoss_Object = MibScalar
mcmT1CsuGenStatusRxCarrierLoss = _McmT1CsuGenStatusRxCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 10),
    _McmT1CsuGenStatusRxCarrierLoss_Type()
)
mcmT1CsuGenStatusRxCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxCarrierLoss.setStatus("deprecated")


class _McmT1CsuGenStatusRxSyncLoss_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxSyncLoss based on Integer32"""
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


_McmT1CsuGenStatusRxSyncLoss_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxSyncLoss_Object = MibScalar
mcmT1CsuGenStatusRxSyncLoss = _McmT1CsuGenStatusRxSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 11),
    _McmT1CsuGenStatusRxSyncLoss_Type()
)
mcmT1CsuGenStatusRxSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxSyncLoss.setStatus("deprecated")


class _McmT1CsuGenStatusLnCdViolHighByte_Type(Integer32):
    """Custom type mcmT1CsuGenStatusLnCdViolHighByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuGenStatusLnCdViolHighByte_Type.__name__ = "Integer32"
_McmT1CsuGenStatusLnCdViolHighByte_Object = MibScalar
mcmT1CsuGenStatusLnCdViolHighByte = _McmT1CsuGenStatusLnCdViolHighByte_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 12),
    _McmT1CsuGenStatusLnCdViolHighByte_Type()
)
mcmT1CsuGenStatusLnCdViolHighByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusLnCdViolHighByte.setStatus("deprecated")


class _McmT1CsuGenStatusLnCdViolLowByte_Type(Integer32):
    """Custom type mcmT1CsuGenStatusLnCdViolLowByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1CsuGenStatusLnCdViolLowByte_Type.__name__ = "Integer32"
_McmT1CsuGenStatusLnCdViolLowByte_Object = MibScalar
mcmT1CsuGenStatusLnCdViolLowByte = _McmT1CsuGenStatusLnCdViolLowByte_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 13),
    _McmT1CsuGenStatusLnCdViolLowByte_Type()
)
mcmT1CsuGenStatusLnCdViolLowByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusLnCdViolLowByte.setStatus("deprecated")


class _McmT1CsuGenStatusRxLoopUpCdDetect_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxLoopUpCdDetect based on Integer32"""
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


_McmT1CsuGenStatusRxLoopUpCdDetect_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxLoopUpCdDetect_Object = MibScalar
mcmT1CsuGenStatusRxLoopUpCdDetect = _McmT1CsuGenStatusRxLoopUpCdDetect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 14),
    _McmT1CsuGenStatusRxLoopUpCdDetect_Type()
)
mcmT1CsuGenStatusRxLoopUpCdDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxLoopUpCdDetect.setStatus("deprecated")


class _McmT1CsuGenStatusRxLoopDnCdDetect_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxLoopDnCdDetect based on Integer32"""
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


_McmT1CsuGenStatusRxLoopDnCdDetect_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxLoopDnCdDetect_Object = MibScalar
mcmT1CsuGenStatusRxLoopDnCdDetect = _McmT1CsuGenStatusRxLoopDnCdDetect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 15),
    _McmT1CsuGenStatusRxLoopDnCdDetect_Type()
)
mcmT1CsuGenStatusRxLoopDnCdDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxLoopDnCdDetect.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-T1CSU-MIB",
    **{"micom-t1csu": micom_t1csu,
       "t1csu-configuration": t1csu_configuration,
       "mcmT1CsuCfgGroup": mcmT1CsuCfgGroup,
       "mcmT1CsuCfgLineBuildOut": mcmT1CsuCfgLineBuildOut,
       "mcmT1CsuCfgFrameFmt": mcmT1CsuCfgFrameFmt,
       "mcmT1CsuCfgTxIdleCode": mcmT1CsuCfgTxIdleCode,
       "mcmT1CsuCfgTxRx0CodeSuppress": mcmT1CsuCfgTxRx0CodeSuppress,
       "mcmT1CsuCfgTxB7ZeroSuppress": mcmT1CsuCfgTxB7ZeroSuppress,
       "mcmT1CsuCfgTxRxClkSource": mcmT1CsuCfgTxRxClkSource,
       "mcmT1CsuCfgDS0BasicRate": mcmT1CsuCfgDS0BasicRate,
       "mcmT1CsuCfgDS0Connection": mcmT1CsuCfgDS0Connection,
       "mcmT1CsuCfgLocalLoopback": mcmT1CsuCfgLocalLoopback,
       "mcmT1CsuCfgRemoteLoopback": mcmT1CsuCfgRemoteLoopback,
       "mcmT1CsuCfgPayloadLoopback": mcmT1CsuCfgPayloadLoopback,
       "mcmT1CsuCfgFramerLoopback": mcmT1CsuCfgFramerLoopback,
       "mcmT1CsuCfgTransmitLoopUp": mcmT1CsuCfgTransmitLoopUp,
       "mcmT1CsuCfgTransmitLoopDown": mcmT1CsuCfgTransmitLoopDown,
       "nvmT1CsuCfgGroup": nvmT1CsuCfgGroup,
       "nvmT1CsuCfgLineBuildOut": nvmT1CsuCfgLineBuildOut,
       "nvmT1CsuCfgFrameFmt": nvmT1CsuCfgFrameFmt,
       "nvmT1CsuCfgTxIdleCode": nvmT1CsuCfgTxIdleCode,
       "nvmT1CsuCfgTxRx0CodeSuppress": nvmT1CsuCfgTxRx0CodeSuppress,
       "nvmT1CsuCfgTxB7ZeroSuppress": nvmT1CsuCfgTxB7ZeroSuppress,
       "nvmT1CsuCfgTxRxClkSource": nvmT1CsuCfgTxRxClkSource,
       "nvmT1CsuCfgDS0BasicRate": nvmT1CsuCfgDS0BasicRate,
       "nvmT1CsuCfgDS0Connection": nvmT1CsuCfgDS0Connection,
       "nvmT1CsuCfgLocalLoopback": nvmT1CsuCfgLocalLoopback,
       "nvmT1CsuCfgRemoteLoopback": nvmT1CsuCfgRemoteLoopback,
       "nvmT1CsuCfgPayloadLoopback": nvmT1CsuCfgPayloadLoopback,
       "nvmT1CsuCfgFramerLoopback": nvmT1CsuCfgFramerLoopback,
       "nvmT1CsuCfgTransmitLoopUp": nvmT1CsuCfgTransmitLoopUp,
       "nvmT1CsuCfgTransmitLoopDown": nvmT1CsuCfgTransmitLoopDown,
       "t1csu-status": t1csu_status,
       "mcmT1CsuStatusT1LineSpeed": mcmT1CsuStatusT1LineSpeed,
       "mcmT1CsuCntlRegStatusGroup": mcmT1CsuCntlRegStatusGroup,
       "mcmT1CsuStatusCntlReg1": mcmT1CsuStatusCntlReg1,
       "mcmT1CsuStatusCntlReg2": mcmT1CsuStatusCntlReg2,
       "mcmT1CsuStatusCntlReg3": mcmT1CsuStatusCntlReg3,
       "mcmT1CsuStatusCntlReg4": mcmT1CsuStatusCntlReg4,
       "mcmT1CsuStatusCntlReg5": mcmT1CsuStatusCntlReg5,
       "mcmT1CsuStatusCntlReg6": mcmT1CsuStatusCntlReg6,
       "mcmT1CsuStatusCntlReg7": mcmT1CsuStatusCntlReg7,
       "mcmT1CsuStatusCntlReg8": mcmT1CsuStatusCntlReg8,
       "mcmT1CsuGenStatusGroup": mcmT1CsuGenStatusGroup,
       "mcmT1CsuGenStatusLineStatus": mcmT1CsuGenStatusLineStatus,
       "mcmT1CsuGenStatusRedAlarm": mcmT1CsuGenStatusRedAlarm,
       "mcmT1CsuGenStatusYellowAlarm": mcmT1CsuGenStatusYellowAlarm,
       "mcmT1CsuGenStatusBlueAlarm": mcmT1CsuGenStatusBlueAlarm,
       "mcmT1CsuGenStatusRxLevel": mcmT1CsuGenStatusRxLevel,
       "mcmT1CsuGenStatusRxElasStrFull": mcmT1CsuGenStatusRxElasStrFull,
       "mcmT1CsuGenStatusRxElasStrEmpty": mcmT1CsuGenStatusRxElasStrEmpty,
       "mcmT1CsuGenStatusRxPlsDensViolate": mcmT1CsuGenStatusRxPlsDensViolate,
       "mcmT1CsuGenStatusTxPlsDensViolate": mcmT1CsuGenStatusTxPlsDensViolate,
       "mcmT1CsuGenStatusRxCarrierLoss": mcmT1CsuGenStatusRxCarrierLoss,
       "mcmT1CsuGenStatusRxSyncLoss": mcmT1CsuGenStatusRxSyncLoss,
       "mcmT1CsuGenStatusLnCdViolHighByte": mcmT1CsuGenStatusLnCdViolHighByte,
       "mcmT1CsuGenStatusLnCdViolLowByte": mcmT1CsuGenStatusLnCdViolLowByte,
       "mcmT1CsuGenStatusRxLoopUpCdDetect": mcmT1CsuGenStatusRxLoopUpCdDetect,
       "mcmT1CsuGenStatusRxLoopDnCdDetect": mcmT1CsuGenStatusRxLoopDnCdDetect}
)
