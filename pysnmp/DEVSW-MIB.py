# SNMP MIB module (DEVSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:12 2024
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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

aniDevSoftware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AniDevSwConfigFile_Type(DisplayString):
    """Custom type aniDevSwConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevSwConfigFile_Type.__name__ = "DisplayString"
_AniDevSwConfigFile_Object = MibScalar
aniDevSwConfigFile = _AniDevSwConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2, 1),
    _AniDevSwConfigFile_Type()
)
aniDevSwConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSwConfigFile.setStatus("current")


class _AniDevSwSystemSoftwareFile_Type(DisplayString):
    """Custom type aniDevSwSystemSoftwareFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevSwSystemSoftwareFile_Type.__name__ = "DisplayString"
_AniDevSwSystemSoftwareFile_Object = MibScalar
aniDevSwSystemSoftwareFile = _AniDevSwSystemSoftwareFile_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2, 2),
    _AniDevSwSystemSoftwareFile_Type()
)
aniDevSwSystemSoftwareFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSwSystemSoftwareFile.setStatus("current")


class _AniDevSwWssSoftwareFile_Type(DisplayString):
    """Custom type aniDevSwWssSoftwareFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevSwWssSoftwareFile_Type.__name__ = "DisplayString"
_AniDevSwWssSoftwareFile_Object = MibScalar
aniDevSwWssSoftwareFile = _AniDevSwWssSoftwareFile_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2, 3),
    _AniDevSwWssSoftwareFile_Type()
)
aniDevSwWssSoftwareFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSwWssSoftwareFile.setStatus("current")


class _AniDevSwVersion_Type(DisplayString):
    """Custom type aniDevSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AniDevSwVersion_Type.__name__ = "DisplayString"
_AniDevSwVersion_Object = MibScalar
aniDevSwVersion = _AniDevSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2, 4),
    _AniDevSwVersion_Type()
)
aniDevSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSwVersion.setStatus("current")
_AniDevSwBuild_Type = Integer32
_AniDevSwBuild_Object = MibScalar
aniDevSwBuild = _AniDevSwBuild_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2, 5),
    _AniDevSwBuild_Type()
)
aniDevSwBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSwBuild.setStatus("current")


class _AniDevSwBuildDate_Type(DisplayString):
    """Custom type aniDevSwBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_AniDevSwBuildDate_Type.__name__ = "DisplayString"
_AniDevSwBuildDate_Object = MibScalar
aniDevSwBuildDate = _AniDevSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 2, 6),
    _AniDevSwBuildDate_Type()
)
aniDevSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSwBuildDate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVSW-MIB",
    **{"aniDevSoftware": aniDevSoftware,
       "aniDevSwConfigFile": aniDevSwConfigFile,
       "aniDevSwSystemSoftwareFile": aniDevSwSystemSoftwareFile,
       "aniDevSwWssSoftwareFile": aniDevSwWssSoftwareFile,
       "aniDevSwVersion": aniDevSwVersion,
       "aniDevSwBuild": aniDevSwBuild,
       "aniDevSwBuildDate": aniDevSwBuildDate}
)
