# SNMP MIB module (MICOM-56KCSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-56KCSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:38 2024
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

_Micom_56kcsu_ObjectIdentity = ObjectIdentity
micom_56kcsu = _Micom_56kcsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28)
)
_Csu56k_configuration_ObjectIdentity = ObjectIdentity
csu56k_configuration = _Csu56k_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1)
)
_Mcm56kCsuCfgGroup_ObjectIdentity = ObjectIdentity
mcm56kCsuCfgGroup = _Mcm56kCsuCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1)
)


class _Mcm56kCsuCfgOperatingMode_Type(Integer32):
    """Custom type mcm56kCsuCfgOperatingMode based on Integer32"""
    defaultValue = 1

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
        *(("cc-64k-ClearChannel-64k", 3),
          ("dds-pri-2Wire-56k", 4),
          ("dds-pri-4Wire-56k", 1),
          ("dds-sc-WithSecondaryChannel-72k", 2))
    )


_Mcm56kCsuCfgOperatingMode_Type.__name__ = "Integer32"
_Mcm56kCsuCfgOperatingMode_Object = MibScalar
mcm56kCsuCfgOperatingMode = _Mcm56kCsuCfgOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 1),
    _Mcm56kCsuCfgOperatingMode_Type()
)
mcm56kCsuCfgOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgOperatingMode.setStatus("deprecated")


class _Mcm56kCsuCfgClockingSource_Type(Integer32):
    """Custom type mcm56kCsuCfgClockingSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClock", 1),
          ("internalClock", 2))
    )


_Mcm56kCsuCfgClockingSource_Type.__name__ = "Integer32"
_Mcm56kCsuCfgClockingSource_Object = MibScalar
mcm56kCsuCfgClockingSource = _Mcm56kCsuCfgClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 2),
    _Mcm56kCsuCfgClockingSource_Type()
)
mcm56kCsuCfgClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgClockingSource.setStatus("deprecated")


class _Mcm56kCsuCfgTxOutOfFrame_Type(Integer32):
    """Custom type mcm56kCsuCfgTxOutOfFrame based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitOutOfFrame", 2))
    )


_Mcm56kCsuCfgTxOutOfFrame_Type.__name__ = "Integer32"
_Mcm56kCsuCfgTxOutOfFrame_Object = MibScalar
mcm56kCsuCfgTxOutOfFrame = _Mcm56kCsuCfgTxOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 3),
    _Mcm56kCsuCfgTxOutOfFrame_Type()
)
mcm56kCsuCfgTxOutOfFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgTxOutOfFrame.setStatus("deprecated")


class _Mcm56kCsuCfgTxOutOfService_Type(Integer32):
    """Custom type mcm56kCsuCfgTxOutOfService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitOutOfService", 2))
    )


_Mcm56kCsuCfgTxOutOfService_Type.__name__ = "Integer32"
_Mcm56kCsuCfgTxOutOfService_Object = MibScalar
mcm56kCsuCfgTxOutOfService = _Mcm56kCsuCfgTxOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 4),
    _Mcm56kCsuCfgTxOutOfService_Type()
)
mcm56kCsuCfgTxOutOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgTxOutOfService.setStatus("deprecated")


class _Mcm56kCsuCfgTxControlModeIdle_Type(Integer32):
    """Custom type mcm56kCsuCfgTxControlModeIdle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitControlModeIdle", 2))
    )


_Mcm56kCsuCfgTxControlModeIdle_Type.__name__ = "Integer32"
_Mcm56kCsuCfgTxControlModeIdle_Object = MibScalar
mcm56kCsuCfgTxControlModeIdle = _Mcm56kCsuCfgTxControlModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 5),
    _Mcm56kCsuCfgTxControlModeIdle_Type()
)
mcm56kCsuCfgTxControlModeIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgTxControlModeIdle.setStatus("deprecated")


class _Mcm56kCsuCfgZeroSuppressDisable_Type(Integer32):
    """Custom type mcm56kCsuCfgZeroSuppressDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("zeroSuppressionDisable", 2))
    )


_Mcm56kCsuCfgZeroSuppressDisable_Type.__name__ = "Integer32"
_Mcm56kCsuCfgZeroSuppressDisable_Object = MibScalar
mcm56kCsuCfgZeroSuppressDisable = _Mcm56kCsuCfgZeroSuppressDisable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 6),
    _Mcm56kCsuCfgZeroSuppressDisable_Type()
)
mcm56kCsuCfgZeroSuppressDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgZeroSuppressDisable.setStatus("deprecated")


class _Mcm56kCsuCfgTxIdle_Type(Integer32):
    """Custom type mcm56kCsuCfgTxIdle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitIdle", 2))
    )


_Mcm56kCsuCfgTxIdle_Type.__name__ = "Integer32"
_Mcm56kCsuCfgTxIdle_Object = MibScalar
mcm56kCsuCfgTxIdle = _Mcm56kCsuCfgTxIdle_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 7),
    _Mcm56kCsuCfgTxIdle_Type()
)
mcm56kCsuCfgTxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgTxIdle.setStatus("deprecated")


class _Mcm56kCsuCfgCSULoopback_Type(Integer32):
    """Custom type mcm56kCsuCfgCSULoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceCSUtoLoopback", 2),
          ("normalReceiveCondition", 1))
    )


_Mcm56kCsuCfgCSULoopback_Type.__name__ = "Integer32"
_Mcm56kCsuCfgCSULoopback_Object = MibScalar
mcm56kCsuCfgCSULoopback = _Mcm56kCsuCfgCSULoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 8),
    _Mcm56kCsuCfgCSULoopback_Type()
)
mcm56kCsuCfgCSULoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgCSULoopback.setStatus("deprecated")


class _Mcm56kCsuCfgFilterForceEnable_Type(Integer32):
    """Custom type mcm56kCsuCfgFilterForceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterForceEnable", 2),
          ("normalReceiveCondition", 1))
    )


_Mcm56kCsuCfgFilterForceEnable_Type.__name__ = "Integer32"
_Mcm56kCsuCfgFilterForceEnable_Object = MibScalar
mcm56kCsuCfgFilterForceEnable = _Mcm56kCsuCfgFilterForceEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 9),
    _Mcm56kCsuCfgFilterForceEnable_Type()
)
mcm56kCsuCfgFilterForceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgFilterForceEnable.setStatus("deprecated")


class _Mcm56kCsuCfgFilterForcingCntl_Type(Integer32):
    """Custom type mcm56kCsuCfgFilterForcingCntl based on Integer32"""
    defaultValue = 16

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
              16)
        )
    )
    namedValues = NamedValues(
        *(("filterGain-0db", 16),
          ("filterGain-12db", 14),
          ("filterGain-18db", 13),
          ("filterGain-24db", 12),
          ("filterGain-30db", 11),
          ("filterGain-36db", 10),
          ("filterGain-42db", 9),
          ("filterGain-48db", 8),
          ("filterGain-54db", 7),
          ("filterGain-60db", 6),
          ("filterGain-66db", 5),
          ("filterGain-6db", 15),
          ("filterGain-72db", 4),
          ("filterGain-78db", 3),
          ("filterGain-84db", 2),
          ("filterGain-90db", 1))
    )


_Mcm56kCsuCfgFilterForcingCntl_Type.__name__ = "Integer32"
_Mcm56kCsuCfgFilterForcingCntl_Object = MibScalar
mcm56kCsuCfgFilterForcingCntl = _Mcm56kCsuCfgFilterForcingCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 1, 10),
    _Mcm56kCsuCfgFilterForcingCntl_Type()
)
mcm56kCsuCfgFilterForcingCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm56kCsuCfgFilterForcingCntl.setStatus("deprecated")
_Nvm56kCsuCfgGroup_ObjectIdentity = ObjectIdentity
nvm56kCsuCfgGroup = _Nvm56kCsuCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2)
)


class _Nvm56kCsuCfgOperatingMode_Type(Integer32):
    """Custom type nvm56kCsuCfgOperatingMode based on Integer32"""
    defaultValue = 1

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
        *(("cc-64k-ClearChannel-64k", 3),
          ("dds-pri-2Wire-56k", 4),
          ("dds-pri-4Wire-56k", 1),
          ("dds-sc-WithSecondaryChannel-72k", 2))
    )


_Nvm56kCsuCfgOperatingMode_Type.__name__ = "Integer32"
_Nvm56kCsuCfgOperatingMode_Object = MibScalar
nvm56kCsuCfgOperatingMode = _Nvm56kCsuCfgOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 1),
    _Nvm56kCsuCfgOperatingMode_Type()
)
nvm56kCsuCfgOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgOperatingMode.setStatus("obsolete")


class _Nvm56kCsuCfgClockingSource_Type(Integer32):
    """Custom type nvm56kCsuCfgClockingSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClock", 1),
          ("internalClock", 2))
    )


_Nvm56kCsuCfgClockingSource_Type.__name__ = "Integer32"
_Nvm56kCsuCfgClockingSource_Object = MibScalar
nvm56kCsuCfgClockingSource = _Nvm56kCsuCfgClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 2),
    _Nvm56kCsuCfgClockingSource_Type()
)
nvm56kCsuCfgClockingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgClockingSource.setStatus("obsolete")


class _Nvm56kCsuCfgTxOutOfFrame_Type(Integer32):
    """Custom type nvm56kCsuCfgTxOutOfFrame based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitOutOfFrame", 2))
    )


_Nvm56kCsuCfgTxOutOfFrame_Type.__name__ = "Integer32"
_Nvm56kCsuCfgTxOutOfFrame_Object = MibScalar
nvm56kCsuCfgTxOutOfFrame = _Nvm56kCsuCfgTxOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 3),
    _Nvm56kCsuCfgTxOutOfFrame_Type()
)
nvm56kCsuCfgTxOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgTxOutOfFrame.setStatus("obsolete")


class _Nvm56kCsuCfgTxOutOfService_Type(Integer32):
    """Custom type nvm56kCsuCfgTxOutOfService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitOutOfService", 2))
    )


_Nvm56kCsuCfgTxOutOfService_Type.__name__ = "Integer32"
_Nvm56kCsuCfgTxOutOfService_Object = MibScalar
nvm56kCsuCfgTxOutOfService = _Nvm56kCsuCfgTxOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 4),
    _Nvm56kCsuCfgTxOutOfService_Type()
)
nvm56kCsuCfgTxOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgTxOutOfService.setStatus("obsolete")


class _Nvm56kCsuCfgTxControlModeIdle_Type(Integer32):
    """Custom type nvm56kCsuCfgTxControlModeIdle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitControlModeIdle", 2))
    )


_Nvm56kCsuCfgTxControlModeIdle_Type.__name__ = "Integer32"
_Nvm56kCsuCfgTxControlModeIdle_Object = MibScalar
nvm56kCsuCfgTxControlModeIdle = _Nvm56kCsuCfgTxControlModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 5),
    _Nvm56kCsuCfgTxControlModeIdle_Type()
)
nvm56kCsuCfgTxControlModeIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgTxControlModeIdle.setStatus("obsolete")


class _Nvm56kCsuCfgZeroSuppressDisable_Type(Integer32):
    """Custom type nvm56kCsuCfgZeroSuppressDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("zeroSuppressionDisable", 2))
    )


_Nvm56kCsuCfgZeroSuppressDisable_Type.__name__ = "Integer32"
_Nvm56kCsuCfgZeroSuppressDisable_Object = MibScalar
nvm56kCsuCfgZeroSuppressDisable = _Nvm56kCsuCfgZeroSuppressDisable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 6),
    _Nvm56kCsuCfgZeroSuppressDisable_Type()
)
nvm56kCsuCfgZeroSuppressDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgZeroSuppressDisable.setStatus("obsolete")


class _Nvm56kCsuCfgTxIdle_Type(Integer32):
    """Custom type nvm56kCsuCfgTxIdle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitIdle", 2))
    )


_Nvm56kCsuCfgTxIdle_Type.__name__ = "Integer32"
_Nvm56kCsuCfgTxIdle_Object = MibScalar
nvm56kCsuCfgTxIdle = _Nvm56kCsuCfgTxIdle_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 7),
    _Nvm56kCsuCfgTxIdle_Type()
)
nvm56kCsuCfgTxIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgTxIdle.setStatus("obsolete")


class _Nvm56kCsuCfgCSULoopback_Type(Integer32):
    """Custom type nvm56kCsuCfgCSULoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceCSUtoLoopback", 2),
          ("normalReceiveCondition", 1))
    )


_Nvm56kCsuCfgCSULoopback_Type.__name__ = "Integer32"
_Nvm56kCsuCfgCSULoopback_Object = MibScalar
nvm56kCsuCfgCSULoopback = _Nvm56kCsuCfgCSULoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 8),
    _Nvm56kCsuCfgCSULoopback_Type()
)
nvm56kCsuCfgCSULoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgCSULoopback.setStatus("obsolete")


class _Nvm56kCsuCfgFilterForceEnable_Type(Integer32):
    """Custom type nvm56kCsuCfgFilterForceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterForceEnable", 2),
          ("normalReceiveCondition", 1))
    )


_Nvm56kCsuCfgFilterForceEnable_Type.__name__ = "Integer32"
_Nvm56kCsuCfgFilterForceEnable_Object = MibScalar
nvm56kCsuCfgFilterForceEnable = _Nvm56kCsuCfgFilterForceEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 9),
    _Nvm56kCsuCfgFilterForceEnable_Type()
)
nvm56kCsuCfgFilterForceEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgFilterForceEnable.setStatus("obsolete")


class _Nvm56kCsuCfgFilterForcingCntl_Type(Integer32):
    """Custom type nvm56kCsuCfgFilterForcingCntl based on Integer32"""
    defaultValue = 16

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
              16)
        )
    )
    namedValues = NamedValues(
        *(("filterGain-0db", 16),
          ("filterGain-12db", 14),
          ("filterGain-18db", 13),
          ("filterGain-24db", 12),
          ("filterGain-30db", 11),
          ("filterGain-36db", 10),
          ("filterGain-42db", 9),
          ("filterGain-48db", 8),
          ("filterGain-54db", 7),
          ("filterGain-60db", 6),
          ("filterGain-66db", 5),
          ("filterGain-6db", 15),
          ("filterGain-72db", 4),
          ("filterGain-78db", 3),
          ("filterGain-84db", 2),
          ("filterGain-90db", 1))
    )


_Nvm56kCsuCfgFilterForcingCntl_Type.__name__ = "Integer32"
_Nvm56kCsuCfgFilterForcingCntl_Object = MibScalar
nvm56kCsuCfgFilterForcingCntl = _Nvm56kCsuCfgFilterForcingCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 1, 2, 10),
    _Nvm56kCsuCfgFilterForcingCntl_Type()
)
nvm56kCsuCfgFilterForcingCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm56kCsuCfgFilterForcingCntl.setStatus("obsolete")
_Csu56k_status_ObjectIdentity = ObjectIdentity
csu56k_status = _Csu56k_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2)
)
_Mcm56KCsuStatusGroup_ObjectIdentity = ObjectIdentity
mcm56KCsuStatusGroup = _Mcm56KCsuStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1)
)


class _Mcm56KCsuStatusLineStatus_Type(Integer32):
    """Custom type mcm56KCsuStatusLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("operational", 1),
          ("testMode", 3))
    )


_Mcm56KCsuStatusLineStatus_Type.__name__ = "Integer32"
_Mcm56KCsuStatusLineStatus_Object = MibScalar
mcm56KCsuStatusLineStatus = _Mcm56KCsuStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 1),
    _Mcm56KCsuStatusLineStatus_Type()
)
mcm56KCsuStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusLineStatus.setStatus("deprecated")


class _Mcm56KCsuStatusRxLossOfSignal_Type(Integer32):
    """Custom type mcm56KCsuStatusRxLossOfSignal based on Integer32"""
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


_Mcm56KCsuStatusRxLossOfSignal_Type.__name__ = "Integer32"
_Mcm56KCsuStatusRxLossOfSignal_Object = MibScalar
mcm56KCsuStatusRxLossOfSignal = _Mcm56KCsuStatusRxLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 2),
    _Mcm56KCsuStatusRxLossOfSignal_Type()
)
mcm56KCsuStatusRxLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusRxLossOfSignal.setStatus("deprecated")


class _Mcm56KCsuStatusFAWSync_Type(Integer32):
    """Custom type mcm56KCsuStatusFAWSync based on Integer32"""
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


_Mcm56KCsuStatusFAWSync_Type.__name__ = "Integer32"
_Mcm56KCsuStatusFAWSync_Object = MibScalar
mcm56KCsuStatusFAWSync = _Mcm56KCsuStatusFAWSync_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 3),
    _Mcm56KCsuStatusFAWSync_Type()
)
mcm56KCsuStatusFAWSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusFAWSync.setStatus("deprecated")


class _Mcm56KCsuStatusLoopPresent_Type(Integer32):
    """Custom type mcm56KCsuStatusLoopPresent based on Integer32"""
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


_Mcm56KCsuStatusLoopPresent_Type.__name__ = "Integer32"
_Mcm56KCsuStatusLoopPresent_Object = MibScalar
mcm56KCsuStatusLoopPresent = _Mcm56KCsuStatusLoopPresent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 4),
    _Mcm56KCsuStatusLoopPresent_Type()
)
mcm56KCsuStatusLoopPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusLoopPresent.setStatus("deprecated")
_Mcm56KCsuStatusInsertLossLineLength_Type = Integer32
_Mcm56KCsuStatusInsertLossLineLength_Object = MibScalar
mcm56KCsuStatusInsertLossLineLength = _Mcm56KCsuStatusInsertLossLineLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 5),
    _Mcm56KCsuStatusInsertLossLineLength_Type()
)
mcm56KCsuStatusInsertLossLineLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusInsertLossLineLength.setStatus("deprecated")
_Mcm56KCsuStatusRxSignalMag_Type = Integer32
_Mcm56KCsuStatusRxSignalMag_Object = MibScalar
mcm56KCsuStatusRxSignalMag = _Mcm56KCsuStatusRxSignalMag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 6),
    _Mcm56KCsuStatusRxSignalMag_Type()
)
mcm56KCsuStatusRxSignalMag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusRxSignalMag.setStatus("deprecated")
_Mcm56KCsuStatusInvalidBPVcount_Type = Integer32
_Mcm56KCsuStatusInvalidBPVcount_Object = MibScalar
mcm56KCsuStatusInvalidBPVcount = _Mcm56KCsuStatusInvalidBPVcount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 28, 2, 1, 7),
    _Mcm56KCsuStatusInvalidBPVcount_Type()
)
mcm56KCsuStatusInvalidBPVcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm56KCsuStatusInvalidBPVcount.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-56KCSU-MIB",
    **{"micom-56kcsu": micom_56kcsu,
       "csu56k-configuration": csu56k_configuration,
       "mcm56kCsuCfgGroup": mcm56kCsuCfgGroup,
       "mcm56kCsuCfgOperatingMode": mcm56kCsuCfgOperatingMode,
       "mcm56kCsuCfgClockingSource": mcm56kCsuCfgClockingSource,
       "mcm56kCsuCfgTxOutOfFrame": mcm56kCsuCfgTxOutOfFrame,
       "mcm56kCsuCfgTxOutOfService": mcm56kCsuCfgTxOutOfService,
       "mcm56kCsuCfgTxControlModeIdle": mcm56kCsuCfgTxControlModeIdle,
       "mcm56kCsuCfgZeroSuppressDisable": mcm56kCsuCfgZeroSuppressDisable,
       "mcm56kCsuCfgTxIdle": mcm56kCsuCfgTxIdle,
       "mcm56kCsuCfgCSULoopback": mcm56kCsuCfgCSULoopback,
       "mcm56kCsuCfgFilterForceEnable": mcm56kCsuCfgFilterForceEnable,
       "mcm56kCsuCfgFilterForcingCntl": mcm56kCsuCfgFilterForcingCntl,
       "nvm56kCsuCfgGroup": nvm56kCsuCfgGroup,
       "nvm56kCsuCfgOperatingMode": nvm56kCsuCfgOperatingMode,
       "nvm56kCsuCfgClockingSource": nvm56kCsuCfgClockingSource,
       "nvm56kCsuCfgTxOutOfFrame": nvm56kCsuCfgTxOutOfFrame,
       "nvm56kCsuCfgTxOutOfService": nvm56kCsuCfgTxOutOfService,
       "nvm56kCsuCfgTxControlModeIdle": nvm56kCsuCfgTxControlModeIdle,
       "nvm56kCsuCfgZeroSuppressDisable": nvm56kCsuCfgZeroSuppressDisable,
       "nvm56kCsuCfgTxIdle": nvm56kCsuCfgTxIdle,
       "nvm56kCsuCfgCSULoopback": nvm56kCsuCfgCSULoopback,
       "nvm56kCsuCfgFilterForceEnable": nvm56kCsuCfgFilterForceEnable,
       "nvm56kCsuCfgFilterForcingCntl": nvm56kCsuCfgFilterForcingCntl,
       "csu56k-status": csu56k_status,
       "mcm56KCsuStatusGroup": mcm56KCsuStatusGroup,
       "mcm56KCsuStatusLineStatus": mcm56KCsuStatusLineStatus,
       "mcm56KCsuStatusRxLossOfSignal": mcm56KCsuStatusRxLossOfSignal,
       "mcm56KCsuStatusFAWSync": mcm56KCsuStatusFAWSync,
       "mcm56KCsuStatusLoopPresent": mcm56KCsuStatusLoopPresent,
       "mcm56KCsuStatusInsertLossLineLength": mcm56KCsuStatusInsertLossLineLength,
       "mcm56KCsuStatusRxSignalMag": mcm56KCsuStatusRxSignalMag,
       "mcm56KCsuStatusInvalidBPVcount": mcm56KCsuStatusInvalidBPVcount}
)
