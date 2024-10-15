# SNMP MIB module (BOOTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BOOTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:32 2024
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

(bootExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "bootExt")

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

bootExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApBootBootP_Type(Integer32):
    """Custom type apBootBootP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApBootBootP_Type.__name__ = "Integer32"
_ApBootBootP_Object = MibScalar
apBootBootP = _ApBootBootP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 2),
    _ApBootBootP_Type()
)
apBootBootP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootBootP.setStatus("current")
_ApBootIpOfSystem_Type = IpAddress
_ApBootIpOfSystem_Object = MibScalar
apBootIpOfSystem = _ApBootIpOfSystem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 3),
    _ApBootIpOfSystem_Type()
)
apBootIpOfSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootIpOfSystem.setStatus("current")


class _ApBootPrimaryType_Type(Integer32):
    """Custom type apBootPrimaryType based on Integer32"""
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
        *(("boot-from-disk", 1),
          ("boot-via-ftp", 2),
          ("boot-via-network", 3),
          ("not-configured", 4))
    )


_ApBootPrimaryType_Type.__name__ = "Integer32"
_ApBootPrimaryType_Object = MibScalar
apBootPrimaryType = _ApBootPrimaryType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 4),
    _ApBootPrimaryType_Type()
)
apBootPrimaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootPrimaryType.setStatus("current")


class _ApBootPrimaryFileName_Type(DisplayString):
    """Custom type apBootPrimaryFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootPrimaryFileName_Type.__name__ = "DisplayString"
_ApBootPrimaryFileName_Object = MibScalar
apBootPrimaryFileName = _ApBootPrimaryFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 5),
    _ApBootPrimaryFileName_Type()
)
apBootPrimaryFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootPrimaryFileName.setStatus("current")


class _ApBootPrimaryFTPRecordName_Type(DisplayString):
    """Custom type apBootPrimaryFTPRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApBootPrimaryFTPRecordName_Type.__name__ = "DisplayString"
_ApBootPrimaryFTPRecordName_Object = MibScalar
apBootPrimaryFTPRecordName = _ApBootPrimaryFTPRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 6),
    _ApBootPrimaryFTPRecordName_Type()
)
apBootPrimaryFTPRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootPrimaryFTPRecordName.setStatus("current")


class _ApBootSecondaryType_Type(Integer32):
    """Custom type apBootSecondaryType based on Integer32"""
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
        *(("boot-from-disk", 1),
          ("boot-via-ftp", 2),
          ("boot-via-network", 3),
          ("not-configured", 4))
    )


_ApBootSecondaryType_Type.__name__ = "Integer32"
_ApBootSecondaryType_Object = MibScalar
apBootSecondaryType = _ApBootSecondaryType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 7),
    _ApBootSecondaryType_Type()
)
apBootSecondaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootSecondaryType.setStatus("current")


class _ApBootSecondaryFileName_Type(DisplayString):
    """Custom type apBootSecondaryFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootSecondaryFileName_Type.__name__ = "DisplayString"
_ApBootSecondaryFileName_Object = MibScalar
apBootSecondaryFileName = _ApBootSecondaryFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 8),
    _ApBootSecondaryFileName_Type()
)
apBootSecondaryFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootSecondaryFileName.setStatus("current")


class _ApBootSecondaryFTPRecordName_Type(DisplayString):
    """Custom type apBootSecondaryFTPRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApBootSecondaryFTPRecordName_Type.__name__ = "DisplayString"
_ApBootSecondaryFTPRecordName_Object = MibScalar
apBootSecondaryFTPRecordName = _ApBootSecondaryFTPRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 9),
    _ApBootSecondaryFTPRecordName_Type()
)
apBootSecondaryFTPRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootSecondaryFTPRecordName.setStatus("current")


class _ApBootLastType_Type(Integer32):
    """Custom type apBootLastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot-from-disk", 1),
          ("boot-via-ftp", 2),
          ("boot-via-network", 3))
    )


_ApBootLastType_Type.__name__ = "Integer32"
_ApBootLastType_Object = MibScalar
apBootLastType = _ApBootLastType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 10),
    _ApBootLastType_Type()
)
apBootLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBootLastType.setStatus("current")


class _ApBootLastFileName_Type(DisplayString):
    """Custom type apBootLastFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootLastFileName_Type.__name__ = "DisplayString"
_ApBootLastFileName_Object = MibScalar
apBootLastFileName = _ApBootLastFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 11),
    _ApBootLastFileName_Type()
)
apBootLastFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBootLastFileName.setStatus("current")


class _ApBootLastFTPRecordName_Type(DisplayString):
    """Custom type apBootLastFTPRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApBootLastFTPRecordName_Type.__name__ = "DisplayString"
_ApBootLastFTPRecordName_Object = MibScalar
apBootLastFTPRecordName = _ApBootLastFTPRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 12),
    _ApBootLastFTPRecordName_Type()
)
apBootLastFTPRecordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBootLastFTPRecordName.setStatus("current")
_ApBootNetmaskOfSystem_Type = IpAddress
_ApBootNetmaskOfSystem_Object = MibScalar
apBootNetmaskOfSystem = _ApBootNetmaskOfSystem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 13),
    _ApBootNetmaskOfSystem_Type()
)
apBootNetmaskOfSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootNetmaskOfSystem.setStatus("current")


class _ApBootRedundantBootP_Type(Integer32):
    """Custom type apBootRedundantBootP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApBootRedundantBootP_Type.__name__ = "Integer32"
_ApBootRedundantBootP_Object = MibScalar
apBootRedundantBootP = _ApBootRedundantBootP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 14),
    _ApBootRedundantBootP_Type()
)
apBootRedundantBootP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantBootP.setStatus("current")
_ApBootRedundantIpOfSystem_Type = IpAddress
_ApBootRedundantIpOfSystem_Object = MibScalar
apBootRedundantIpOfSystem = _ApBootRedundantIpOfSystem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 15),
    _ApBootRedundantIpOfSystem_Type()
)
apBootRedundantIpOfSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantIpOfSystem.setStatus("current")


class _ApBootRedundantPrimaryType_Type(Integer32):
    """Custom type apBootRedundantPrimaryType based on Integer32"""
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
        *(("boot-from-disk", 1),
          ("boot-via-ftp", 2),
          ("boot-via-network", 3),
          ("not-configured", 4))
    )


_ApBootRedundantPrimaryType_Type.__name__ = "Integer32"
_ApBootRedundantPrimaryType_Object = MibScalar
apBootRedundantPrimaryType = _ApBootRedundantPrimaryType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 16),
    _ApBootRedundantPrimaryType_Type()
)
apBootRedundantPrimaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantPrimaryType.setStatus("current")


class _ApBootRedundantPrimaryFileName_Type(DisplayString):
    """Custom type apBootRedundantPrimaryFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootRedundantPrimaryFileName_Type.__name__ = "DisplayString"
_ApBootRedundantPrimaryFileName_Object = MibScalar
apBootRedundantPrimaryFileName = _ApBootRedundantPrimaryFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 17),
    _ApBootRedundantPrimaryFileName_Type()
)
apBootRedundantPrimaryFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantPrimaryFileName.setStatus("current")


class _ApBootRedundantPrimaryFTPRecordName_Type(DisplayString):
    """Custom type apBootRedundantPrimaryFTPRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApBootRedundantPrimaryFTPRecordName_Type.__name__ = "DisplayString"
_ApBootRedundantPrimaryFTPRecordName_Object = MibScalar
apBootRedundantPrimaryFTPRecordName = _ApBootRedundantPrimaryFTPRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 18),
    _ApBootRedundantPrimaryFTPRecordName_Type()
)
apBootRedundantPrimaryFTPRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantPrimaryFTPRecordName.setStatus("current")


class _ApBootRedundantSecondaryType_Type(Integer32):
    """Custom type apBootRedundantSecondaryType based on Integer32"""
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
        *(("boot-from-disk", 1),
          ("boot-via-ftp", 2),
          ("boot-via-network", 3),
          ("not-configured", 4))
    )


_ApBootRedundantSecondaryType_Type.__name__ = "Integer32"
_ApBootRedundantSecondaryType_Object = MibScalar
apBootRedundantSecondaryType = _ApBootRedundantSecondaryType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 19),
    _ApBootRedundantSecondaryType_Type()
)
apBootRedundantSecondaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantSecondaryType.setStatus("current")


class _ApBootRedundantSecondaryFileName_Type(DisplayString):
    """Custom type apBootRedundantSecondaryFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootRedundantSecondaryFileName_Type.__name__ = "DisplayString"
_ApBootRedundantSecondaryFileName_Object = MibScalar
apBootRedundantSecondaryFileName = _ApBootRedundantSecondaryFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 20),
    _ApBootRedundantSecondaryFileName_Type()
)
apBootRedundantSecondaryFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantSecondaryFileName.setStatus("current")


class _ApBootRedundantSecondaryFTPRecordName_Type(DisplayString):
    """Custom type apBootRedundantSecondaryFTPRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApBootRedundantSecondaryFTPRecordName_Type.__name__ = "DisplayString"
_ApBootRedundantSecondaryFTPRecordName_Object = MibScalar
apBootRedundantSecondaryFTPRecordName = _ApBootRedundantSecondaryFTPRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 21),
    _ApBootRedundantSecondaryFTPRecordName_Type()
)
apBootRedundantSecondaryFTPRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantSecondaryFTPRecordName.setStatus("current")


class _ApBootRedundantLastType_Type(Integer32):
    """Custom type apBootRedundantLastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot-from-disk", 1),
          ("boot-via-ftp", 2))
    )


_ApBootRedundantLastType_Type.__name__ = "Integer32"
_ApBootRedundantLastType_Object = MibScalar
apBootRedundantLastType = _ApBootRedundantLastType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 22),
    _ApBootRedundantLastType_Type()
)
apBootRedundantLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBootRedundantLastType.setStatus("current")


class _ApBootRedundantLastFileName_Type(DisplayString):
    """Custom type apBootRedundantLastFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootRedundantLastFileName_Type.__name__ = "DisplayString"
_ApBootRedundantLastFileName_Object = MibScalar
apBootRedundantLastFileName = _ApBootRedundantLastFileName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 23),
    _ApBootRedundantLastFileName_Type()
)
apBootRedundantLastFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBootRedundantLastFileName.setStatus("current")


class _ApBootRedundantLastFTPRecordName_Type(DisplayString):
    """Custom type apBootRedundantLastFTPRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApBootRedundantLastFTPRecordName_Type.__name__ = "DisplayString"
_ApBootRedundantLastFTPRecordName_Object = MibScalar
apBootRedundantLastFTPRecordName = _ApBootRedundantLastFTPRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 24),
    _ApBootRedundantLastFTPRecordName_Type()
)
apBootRedundantLastFTPRecordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBootRedundantLastFTPRecordName.setStatus("current")
_ApBootRedundantNetmaskOfSystem_Type = IpAddress
_ApBootRedundantNetmaskOfSystem_Object = MibScalar
apBootRedundantNetmaskOfSystem = _ApBootRedundantNetmaskOfSystem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 25),
    _ApBootRedundantNetmaskOfSystem_Type()
)
apBootRedundantNetmaskOfSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantNetmaskOfSystem.setStatus("current")


class _ApBootPrimaryAltCfgPath_Type(DisplayString):
    """Custom type apBootPrimaryAltCfgPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootPrimaryAltCfgPath_Type.__name__ = "DisplayString"
_ApBootPrimaryAltCfgPath_Object = MibScalar
apBootPrimaryAltCfgPath = _ApBootPrimaryAltCfgPath_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 26),
    _ApBootPrimaryAltCfgPath_Type()
)
apBootPrimaryAltCfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootPrimaryAltCfgPath.setStatus("current")


class _ApBootSecondaryAltCfgPath_Type(DisplayString):
    """Custom type apBootSecondaryAltCfgPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootSecondaryAltCfgPath_Type.__name__ = "DisplayString"
_ApBootSecondaryAltCfgPath_Object = MibScalar
apBootSecondaryAltCfgPath = _ApBootSecondaryAltCfgPath_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 27),
    _ApBootSecondaryAltCfgPath_Type()
)
apBootSecondaryAltCfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootSecondaryAltCfgPath.setStatus("current")


class _ApBootRedundantPrimaryAltCfgPath_Type(DisplayString):
    """Custom type apBootRedundantPrimaryAltCfgPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootRedundantPrimaryAltCfgPath_Type.__name__ = "DisplayString"
_ApBootRedundantPrimaryAltCfgPath_Object = MibScalar
apBootRedundantPrimaryAltCfgPath = _ApBootRedundantPrimaryAltCfgPath_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 28),
    _ApBootRedundantPrimaryAltCfgPath_Type()
)
apBootRedundantPrimaryAltCfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantPrimaryAltCfgPath.setStatus("current")


class _ApBootRedundantSecondaryAltCfgPath_Type(DisplayString):
    """Custom type apBootRedundantSecondaryAltCfgPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApBootRedundantSecondaryAltCfgPath_Type.__name__ = "DisplayString"
_ApBootRedundantSecondaryAltCfgPath_Object = MibScalar
apBootRedundantSecondaryAltCfgPath = _ApBootRedundantSecondaryAltCfgPath_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 31, 29),
    _ApBootRedundantSecondaryAltCfgPath_Type()
)
apBootRedundantSecondaryAltCfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBootRedundantSecondaryAltCfgPath.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BOOTEXT-MIB",
    **{"bootExtMib": bootExtMib,
       "apBootBootP": apBootBootP,
       "apBootIpOfSystem": apBootIpOfSystem,
       "apBootPrimaryType": apBootPrimaryType,
       "apBootPrimaryFileName": apBootPrimaryFileName,
       "apBootPrimaryFTPRecordName": apBootPrimaryFTPRecordName,
       "apBootSecondaryType": apBootSecondaryType,
       "apBootSecondaryFileName": apBootSecondaryFileName,
       "apBootSecondaryFTPRecordName": apBootSecondaryFTPRecordName,
       "apBootLastType": apBootLastType,
       "apBootLastFileName": apBootLastFileName,
       "apBootLastFTPRecordName": apBootLastFTPRecordName,
       "apBootNetmaskOfSystem": apBootNetmaskOfSystem,
       "apBootRedundantBootP": apBootRedundantBootP,
       "apBootRedundantIpOfSystem": apBootRedundantIpOfSystem,
       "apBootRedundantPrimaryType": apBootRedundantPrimaryType,
       "apBootRedundantPrimaryFileName": apBootRedundantPrimaryFileName,
       "apBootRedundantPrimaryFTPRecordName": apBootRedundantPrimaryFTPRecordName,
       "apBootRedundantSecondaryType": apBootRedundantSecondaryType,
       "apBootRedundantSecondaryFileName": apBootRedundantSecondaryFileName,
       "apBootRedundantSecondaryFTPRecordName": apBootRedundantSecondaryFTPRecordName,
       "apBootRedundantLastType": apBootRedundantLastType,
       "apBootRedundantLastFileName": apBootRedundantLastFileName,
       "apBootRedundantLastFTPRecordName": apBootRedundantLastFTPRecordName,
       "apBootRedundantNetmaskOfSystem": apBootRedundantNetmaskOfSystem,
       "apBootPrimaryAltCfgPath": apBootPrimaryAltCfgPath,
       "apBootSecondaryAltCfgPath": apBootSecondaryAltCfgPath,
       "apBootRedundantPrimaryAltCfgPath": apBootRedundantPrimaryAltCfgPath,
       "apBootRedundantSecondaryAltCfgPath": apBootRedundantSecondaryAltCfgPath}
)
