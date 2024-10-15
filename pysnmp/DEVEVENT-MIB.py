# SNMP MIB module (DEVEVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVEVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:07 2024
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

aniDevEvent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevEvNotify_ObjectIdentity = ObjectIdentity
aniDevEvNotify = _AniDevEvNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6, 2)
)


class _AniDevEmailSending_Type(Integer32):
    """Custom type aniDevEmailSending based on Integer32"""
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


_AniDevEmailSending_Type.__name__ = "Integer32"
_AniDevEmailSending_Object = MibScalar
aniDevEmailSending = _AniDevEmailSending_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 1),
    _AniDevEmailSending_Type()
)
aniDevEmailSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevEmailSending.setStatus("current")


class _AniDevEmailSender_Type(DisplayString):
    """Custom type aniDevEmailSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevEmailSender_Type.__name__ = "DisplayString"
_AniDevEmailSender_Object = MibScalar
aniDevEmailSender = _AniDevEmailSender_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 2),
    _AniDevEmailSender_Type()
)
aniDevEmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevEmailSender.setStatus("current")


class _AniDevDomainName_Type(DisplayString):
    """Custom type aniDevDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevDomainName_Type.__name__ = "DisplayString"
_AniDevDomainName_Object = MibScalar
aniDevDomainName = _AniDevDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 3),
    _AniDevDomainName_Type()
)
aniDevDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevDomainName.setStatus("current")


class _AniDevEmailReceiver1_Type(DisplayString):
    """Custom type aniDevEmailReceiver1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevEmailReceiver1_Type.__name__ = "DisplayString"
_AniDevEmailReceiver1_Object = MibScalar
aniDevEmailReceiver1 = _AniDevEmailReceiver1_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 4),
    _AniDevEmailReceiver1_Type()
)
aniDevEmailReceiver1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevEmailReceiver1.setStatus("current")


class _AniDevEmailReceiver2_Type(DisplayString):
    """Custom type aniDevEmailReceiver2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AniDevEmailReceiver2_Type.__name__ = "DisplayString"
_AniDevEmailReceiver2_Object = MibScalar
aniDevEmailReceiver2 = _AniDevEmailReceiver2_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 5),
    _AniDevEmailReceiver2_Type()
)
aniDevEmailReceiver2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevEmailReceiver2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVEVENT-MIB",
    **{"aniDevEvent": aniDevEvent,
       "aniDevEvNotify": aniDevEvNotify,
       "aniDevEmailSending": aniDevEmailSending,
       "aniDevEmailSender": aniDevEmailSender,
       "aniDevDomainName": aniDevDomainName,
       "aniDevEmailReceiver1": aniDevEmailReceiver1,
       "aniDevEmailReceiver2": aniDevEmailReceiver2}
)
