# SNMP MIB module (DEVHW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVHW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:08 2024
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

aniDevHardware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevHwRevision_Type = Integer32
_AniDevHwRevision_Object = MibScalar
aniDevHwRevision = _AniDevHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3, 1),
    _AniDevHwRevision_Type()
)
aniDevHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevHwRevision.setStatus("current")
_AniDevHwSpeed_Type = DisplayString
_AniDevHwSpeed_Object = MibScalar
aniDevHwSpeed = _AniDevHwSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3, 2),
    _AniDevHwSpeed_Type()
)
aniDevHwSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevHwSpeed.setStatus("current")


class _AniDevHwBuildDate_Type(DisplayString):
    """Custom type aniDevHwBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_AniDevHwBuildDate_Type.__name__ = "DisplayString"
_AniDevHwBuildDate_Object = MibScalar
aniDevHwBuildDate = _AniDevHwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3, 3),
    _AniDevHwBuildDate_Type()
)
aniDevHwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevHwBuildDate.setStatus("current")


class _AniDevHwSerialNum_Type(DisplayString):
    """Custom type aniDevHwSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AniDevHwSerialNum_Type.__name__ = "DisplayString"
_AniDevHwSerialNum_Object = MibScalar
aniDevHwSerialNum = _AniDevHwSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3, 4),
    _AniDevHwSerialNum_Type()
)
aniDevHwSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevHwSerialNum.setStatus("current")
_AniDevHwBoardRevision_Type = Integer32
_AniDevHwBoardRevision_Object = MibScalar
aniDevHwBoardRevision = _AniDevHwBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 3, 5),
    _AniDevHwBoardRevision_Type()
)
aniDevHwBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevHwBoardRevision.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVHW-MIB",
    **{"aniDevHardware": aniDevHardware,
       "aniDevHwRevision": aniDevHwRevision,
       "aniDevHwSpeed": aniDevHwSpeed,
       "aniDevHwBuildDate": aniDevHwBuildDate,
       "aniDevHwSerialNum": aniDevHwSerialNum,
       "aniDevHwBoardRevision": aniDevHwBoardRevision}
)
