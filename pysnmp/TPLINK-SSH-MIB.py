# SNMP MIB module (TPLINK-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:41 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5)
)
tplinkSshMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSshMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSshMIBObjects = _TplinkSshMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1)
)


class _TpSshEnable_Type(Integer32):
    """Custom type tpSshEnable based on Integer32"""
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


_TpSshEnable_Type.__name__ = "Integer32"
_TpSshEnable_Object = MibScalar
tpSshEnable = _TpSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 1),
    _TpSshEnable_Type()
)
tpSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEnable.setStatus("current")


class _TpSshProtocolV1Enable_Type(Integer32):
    """Custom type tpSshProtocolV1Enable based on Integer32"""
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


_TpSshProtocolV1Enable_Type.__name__ = "Integer32"
_TpSshProtocolV1Enable_Object = MibScalar
tpSshProtocolV1Enable = _TpSshProtocolV1Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 2),
    _TpSshProtocolV1Enable_Type()
)
tpSshProtocolV1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshProtocolV1Enable.setStatus("current")


class _TpSshProtocolV2Enable_Type(Integer32):
    """Custom type tpSshProtocolV2Enable based on Integer32"""
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


_TpSshProtocolV2Enable_Type.__name__ = "Integer32"
_TpSshProtocolV2Enable_Object = MibScalar
tpSshProtocolV2Enable = _TpSshProtocolV2Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 3),
    _TpSshProtocolV2Enable_Type()
)
tpSshProtocolV2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshProtocolV2Enable.setStatus("current")


class _TpSshQuietPeriod_Type(Integer32):
    """Custom type tpSshQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TpSshQuietPeriod_Type.__name__ = "Integer32"
_TpSshQuietPeriod_Object = MibScalar
tpSshQuietPeriod = _TpSshQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 4),
    _TpSshQuietPeriod_Type()
)
tpSshQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshQuietPeriod.setStatus("current")


class _TpSshMaxConnections_Type(Integer32):
    """Custom type tpSshMaxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpSshMaxConnections_Type.__name__ = "Integer32"
_TpSshMaxConnections_Object = MibScalar
tpSshMaxConnections = _TpSshMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 5),
    _TpSshMaxConnections_Type()
)
tpSshMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshMaxConnections.setStatus("current")


class _TpSshEncryptAlgAES128Enable_Type(Integer32):
    """Custom type tpSshEncryptAlgAES128Enable based on Integer32"""
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


_TpSshEncryptAlgAES128Enable_Type.__name__ = "Integer32"
_TpSshEncryptAlgAES128Enable_Object = MibScalar
tpSshEncryptAlgAES128Enable = _TpSshEncryptAlgAES128Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 6),
    _TpSshEncryptAlgAES128Enable_Type()
)
tpSshEncryptAlgAES128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEncryptAlgAES128Enable.setStatus("current")


class _TpSshEncryptAlgAES192Enable_Type(Integer32):
    """Custom type tpSshEncryptAlgAES192Enable based on Integer32"""
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


_TpSshEncryptAlgAES192Enable_Type.__name__ = "Integer32"
_TpSshEncryptAlgAES192Enable_Object = MibScalar
tpSshEncryptAlgAES192Enable = _TpSshEncryptAlgAES192Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 7),
    _TpSshEncryptAlgAES192Enable_Type()
)
tpSshEncryptAlgAES192Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEncryptAlgAES192Enable.setStatus("current")


class _TpSshEncryptAlgAES256Enable_Type(Integer32):
    """Custom type tpSshEncryptAlgAES256Enable based on Integer32"""
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


_TpSshEncryptAlgAES256Enable_Type.__name__ = "Integer32"
_TpSshEncryptAlgAES256Enable_Object = MibScalar
tpSshEncryptAlgAES256Enable = _TpSshEncryptAlgAES256Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 8),
    _TpSshEncryptAlgAES256Enable_Type()
)
tpSshEncryptAlgAES256Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEncryptAlgAES256Enable.setStatus("current")


class _TpSshEncryptAlgBlowfishEnable_Type(Integer32):
    """Custom type tpSshEncryptAlgBlowfishEnable based on Integer32"""
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


_TpSshEncryptAlgBlowfishEnable_Type.__name__ = "Integer32"
_TpSshEncryptAlgBlowfishEnable_Object = MibScalar
tpSshEncryptAlgBlowfishEnable = _TpSshEncryptAlgBlowfishEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 9),
    _TpSshEncryptAlgBlowfishEnable_Type()
)
tpSshEncryptAlgBlowfishEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEncryptAlgBlowfishEnable.setStatus("current")


class _TpSshEncryptAlgCast128Enable_Type(Integer32):
    """Custom type tpSshEncryptAlgCast128Enable based on Integer32"""
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


_TpSshEncryptAlgCast128Enable_Type.__name__ = "Integer32"
_TpSshEncryptAlgCast128Enable_Object = MibScalar
tpSshEncryptAlgCast128Enable = _TpSshEncryptAlgCast128Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 10),
    _TpSshEncryptAlgCast128Enable_Type()
)
tpSshEncryptAlgCast128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEncryptAlgCast128Enable.setStatus("current")


class _TpSshEncryptAlg3DESEnable_Type(Integer32):
    """Custom type tpSshEncryptAlg3DESEnable based on Integer32"""
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


_TpSshEncryptAlg3DESEnable_Type.__name__ = "Integer32"
_TpSshEncryptAlg3DESEnable_Object = MibScalar
tpSshEncryptAlg3DESEnable = _TpSshEncryptAlg3DESEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 11),
    _TpSshEncryptAlg3DESEnable_Type()
)
tpSshEncryptAlg3DESEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshEncryptAlg3DESEnable.setStatus("current")


class _TpSshInteAlgSHA1Enable_Type(Integer32):
    """Custom type tpSshInteAlgSHA1Enable based on Integer32"""
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


_TpSshInteAlgSHA1Enable_Type.__name__ = "Integer32"
_TpSshInteAlgSHA1Enable_Object = MibScalar
tpSshInteAlgSHA1Enable = _TpSshInteAlgSHA1Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 12),
    _TpSshInteAlgSHA1Enable_Type()
)
tpSshInteAlgSHA1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshInteAlgSHA1Enable.setStatus("current")


class _TpSshInteAlgMD5Enable_Type(Integer32):
    """Custom type tpSshInteAlgMD5Enable based on Integer32"""
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


_TpSshInteAlgMD5Enable_Type.__name__ = "Integer32"
_TpSshInteAlgMD5Enable_Object = MibScalar
tpSshInteAlgMD5Enable = _TpSshInteAlgMD5Enable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 1, 13),
    _TpSshInteAlgMD5Enable_Type()
)
tpSshInteAlgMD5Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSshInteAlgMD5Enable.setStatus("current")
_TplinkSshNotifications_ObjectIdentity = ObjectIdentity
tplinkSshNotifications = _TplinkSshNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 5, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SSH-MIB",
    **{"tplinkSshMIB": tplinkSshMIB,
       "tplinkSshMIBObjects": tplinkSshMIBObjects,
       "tpSshEnable": tpSshEnable,
       "tpSshProtocolV1Enable": tpSshProtocolV1Enable,
       "tpSshProtocolV2Enable": tpSshProtocolV2Enable,
       "tpSshQuietPeriod": tpSshQuietPeriod,
       "tpSshMaxConnections": tpSshMaxConnections,
       "tpSshEncryptAlgAES128Enable": tpSshEncryptAlgAES128Enable,
       "tpSshEncryptAlgAES192Enable": tpSshEncryptAlgAES192Enable,
       "tpSshEncryptAlgAES256Enable": tpSshEncryptAlgAES256Enable,
       "tpSshEncryptAlgBlowfishEnable": tpSshEncryptAlgBlowfishEnable,
       "tpSshEncryptAlgCast128Enable": tpSshEncryptAlgCast128Enable,
       "tpSshEncryptAlg3DESEnable": tpSshEncryptAlg3DESEnable,
       "tpSshInteAlgSHA1Enable": tpSshInteAlgSHA1Enable,
       "tpSshInteAlgMD5Enable": tpSshInteAlgMD5Enable,
       "tplinkSshNotifications": tplinkSshNotifications}
)
