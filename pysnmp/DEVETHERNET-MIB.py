# SNMP MIB module (DEVETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:06 2024
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

aniDevEthernet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevEthernetConfig_ObjectIdentity = ObjectIdentity
aniDevEthernetConfig = _AniDevEthernetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11, 1)
)


class _AniDevEthernetConfigMode_Type(Integer32):
    """Custom type aniDevEthernetConfigMode based on Integer32"""
    defaultValue = 1

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
        *(("auto-negotiate", 1),
          ("speed-100mbps-full", 2),
          ("speed-100mbps-half", 3),
          ("speed-10mbps-full", 4),
          ("speed-10mbps-half", 5))
    )


_AniDevEthernetConfigMode_Type.__name__ = "Integer32"
_AniDevEthernetConfigMode_Object = MibScalar
aniDevEthernetConfigMode = _AniDevEthernetConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 1),
    _AniDevEthernetConfigMode_Type()
)
aniDevEthernetConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevEthernetConfigMode.setStatus("current")


class _AniDevEthernetCurrentLinkStatus_Type(Integer32):
    """Custom type aniDevEthernetCurrentLinkStatus based on Integer32"""
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


_AniDevEthernetCurrentLinkStatus_Type.__name__ = "Integer32"
_AniDevEthernetCurrentLinkStatus_Object = MibScalar
aniDevEthernetCurrentLinkStatus = _AniDevEthernetCurrentLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 2),
    _AniDevEthernetCurrentLinkStatus_Type()
)
aniDevEthernetCurrentLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevEthernetCurrentLinkStatus.setStatus("current")


class _AniDevEthernetCurrentSpeed_Type(Integer32):
    """Custom type aniDevEthernetCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 3),
          ("speed-10-mbps", 1),
          ("speed-100-mbps", 2))
    )


_AniDevEthernetCurrentSpeed_Type.__name__ = "Integer32"
_AniDevEthernetCurrentSpeed_Object = MibScalar
aniDevEthernetCurrentSpeed = _AniDevEthernetCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 3),
    _AniDevEthernetCurrentSpeed_Type()
)
aniDevEthernetCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevEthernetCurrentSpeed.setStatus("current")


class _AniDevEthernetCurrentDuplex_Type(Integer32):
    """Custom type aniDevEthernetCurrentDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1),
          ("not-applicable", 3))
    )


_AniDevEthernetCurrentDuplex_Type.__name__ = "Integer32"
_AniDevEthernetCurrentDuplex_Object = MibScalar
aniDevEthernetCurrentDuplex = _AniDevEthernetCurrentDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 11, 1, 4),
    _AniDevEthernetCurrentDuplex_Type()
)
aniDevEthernetCurrentDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevEthernetCurrentDuplex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVETHERNET-MIB",
    **{"aniDevEthernet": aniDevEthernet,
       "aniDevEthernetConfig": aniDevEthernetConfig,
       "aniDevEthernetConfigMode": aniDevEthernetConfigMode,
       "aniDevEthernetCurrentLinkStatus": aniDevEthernetCurrentLinkStatus,
       "aniDevEthernetCurrentSpeed": aniDevEthernetCurrentSpeed,
       "aniDevEthernetCurrentDuplex": aniDevEthernetCurrentDuplex}
)
