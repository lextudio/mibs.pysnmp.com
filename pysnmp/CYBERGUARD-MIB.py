# SNMP MIB module (CYBERGUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYBERGUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:21 2024
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1)
)
_UnixWare_ObjectIdentity = ObjectIdentity
unixWare = _UnixWare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 13)
)
_CyberGuard_ObjectIdentity = ObjectIdentity
cyberGuard = _CyberGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25)
)
_CgfwMIB_ObjectIdentity = ObjectIdentity
cgfwMIB = _CgfwMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1)
)
_CgfwEvent_ObjectIdentity = ObjectIdentity
cgfwEvent = _CgfwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2)
)


class _CgAccessDeny_Type(DisplayString):
    """Custom type cgAccessDeny based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgAccessDeny_Type.__name__ = "DisplayString"
_CgAccessDeny_Object = MibScalar
cgAccessDeny = _CgAccessDeny_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 1),
    _CgAccessDeny_Type()
)
cgAccessDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgAccessDeny.setStatus("mandatory")


class _CgAccessGrant_Type(DisplayString):
    """Custom type cgAccessGrant based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgAccessGrant_Type.__name__ = "DisplayString"
_CgAccessGrant_Object = MibScalar
cgAccessGrant = _CgAccessGrant_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 2),
    _CgAccessGrant_Type()
)
cgAccessGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgAccessGrant.setStatus("mandatory")


class _CgDiskSpace_Type(DisplayString):
    """Custom type cgDiskSpace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgDiskSpace_Type.__name__ = "DisplayString"
_CgDiskSpace_Object = MibScalar
cgDiskSpace = _CgDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 3),
    _CgDiskSpace_Type()
)
cgDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgDiskSpace.setStatus("mandatory")


class _CgFailedLogin_Type(DisplayString):
    """Custom type cgFailedLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgFailedLogin_Type.__name__ = "DisplayString"
_CgFailedLogin_Object = MibScalar
cgFailedLogin = _CgFailedLogin_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 4),
    _CgFailedLogin_Type()
)
cgFailedLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgFailedLogin.setStatus("mandatory")


class _CgHostLimit_Type(DisplayString):
    """Custom type cgHostLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgHostLimit_Type.__name__ = "DisplayString"
_CgHostLimit_Object = MibScalar
cgHostLimit = _CgHostLimit_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 5),
    _CgHostLimit_Type()
)
cgHostLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgHostLimit.setStatus("mandatory")


class _CgForwardAttack_Type(DisplayString):
    """Custom type cgForwardAttack based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgForwardAttack_Type.__name__ = "DisplayString"
_CgForwardAttack_Object = MibScalar
cgForwardAttack = _CgForwardAttack_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 6),
    _CgForwardAttack_Type()
)
cgForwardAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgForwardAttack.setStatus("mandatory")


class _CgLandAttack_Type(DisplayString):
    """Custom type cgLandAttack based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgLandAttack_Type.__name__ = "DisplayString"
_CgLandAttack_Object = MibScalar
cgLandAttack = _CgLandAttack_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 7),
    _CgLandAttack_Type()
)
cgLandAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgLandAttack.setStatus("mandatory")


class _CgPingOfDeath_Type(DisplayString):
    """Custom type cgPingOfDeath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgPingOfDeath_Type.__name__ = "DisplayString"
_CgPingOfDeath_Object = MibScalar
cgPingOfDeath = _CgPingOfDeath_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 8),
    _CgPingOfDeath_Type()
)
cgPingOfDeath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgPingOfDeath.setStatus("mandatory")


class _CgTcpSynFlood_Type(DisplayString):
    """Custom type cgTcpSynFlood based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgTcpSynFlood_Type.__name__ = "DisplayString"
_CgTcpSynFlood_Object = MibScalar
cgTcpSynFlood = _CgTcpSynFlood_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 9),
    _CgTcpSynFlood_Type()
)
cgTcpSynFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgTcpSynFlood.setStatus("mandatory")


class _CgIntfSpoof_Type(DisplayString):
    """Custom type cgIntfSpoof based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgIntfSpoof_Type.__name__ = "DisplayString"
_CgIntfSpoof_Object = MibScalar
cgIntfSpoof = _CgIntfSpoof_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 10),
    _CgIntfSpoof_Type()
)
cgIntfSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgIntfSpoof.setStatus("mandatory")


class _CgMacViolation_Type(DisplayString):
    """Custom type cgMacViolation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgMacViolation_Type.__name__ = "DisplayString"
_CgMacViolation_Object = MibScalar
cgMacViolation = _CgMacViolation_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 11),
    _CgMacViolation_Type()
)
cgMacViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgMacViolation.setStatus("mandatory")


class _CgPortScan_Type(DisplayString):
    """Custom type cgPortScan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgPortScan_Type.__name__ = "DisplayString"
_CgPortScan_Object = MibScalar
cgPortScan = _CgPortScan_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 12),
    _CgPortScan_Type()
)
cgPortScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgPortScan.setStatus("mandatory")


class _CgBlockedFile_Type(DisplayString):
    """Custom type cgBlockedFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgBlockedFile_Type.__name__ = "DisplayString"
_CgBlockedFile_Object = MibScalar
cgBlockedFile = _CgBlockedFile_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 13),
    _CgBlockedFile_Type()
)
cgBlockedFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgBlockedFile.setStatus("mandatory")


class _CgHaTransition_Type(DisplayString):
    """Custom type cgHaTransition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgHaTransition_Type.__name__ = "DisplayString"
_CgHaTransition_Object = MibScalar
cgHaTransition = _CgHaTransition_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 14),
    _CgHaTransition_Type()
)
cgHaTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgHaTransition.setStatus("mandatory")


class _CgHaNoHB_Type(DisplayString):
    """Custom type cgHaNoHB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgHaNoHB_Type.__name__ = "DisplayString"
_CgHaNoHB_Object = MibScalar
cgHaNoHB = _CgHaNoHB_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 15),
    _CgHaNoHB_Type()
)
cgHaNoHB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgHaNoHB.setStatus("mandatory")


class _CgSwUpdate_Type(DisplayString):
    """Custom type cgSwUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgSwUpdate_Type.__name__ = "DisplayString"
_CgSwUpdate_Object = MibScalar
cgSwUpdate = _CgSwUpdate_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 16),
    _CgSwUpdate_Type()
)
cgSwUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgSwUpdate.setStatus("mandatory")


class _CgPlatformSensor_Type(DisplayString):
    """Custom type cgPlatformSensor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgPlatformSensor_Type.__name__ = "DisplayString"
_CgPlatformSensor_Object = MibScalar
cgPlatformSensor = _CgPlatformSensor_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 17),
    _CgPlatformSensor_Type()
)
cgPlatformSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgPlatformSensor.setStatus("mandatory")


class _CgAuditArchive_Type(DisplayString):
    """Custom type cgAuditArchive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CgAuditArchive_Type.__name__ = "DisplayString"
_CgAuditArchive_Object = MibScalar
cgAuditArchive = _CgAuditArchive_Object(
    (1, 3, 6, 1, 4, 1, 23, 1, 13, 25, 1, 2, 18),
    _CgAuditArchive_Type()
)
cgAuditArchive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgAuditArchive.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYBERGUARD-MIB",
    **{"DisplayString": DisplayString,
       "novell": novell,
       "products": products,
       "unixWare": unixWare,
       "cyberGuard": cyberGuard,
       "cgfwMIB": cgfwMIB,
       "cgfwEvent": cgfwEvent,
       "cgAccessDeny": cgAccessDeny,
       "cgAccessGrant": cgAccessGrant,
       "cgDiskSpace": cgDiskSpace,
       "cgFailedLogin": cgFailedLogin,
       "cgHostLimit": cgHostLimit,
       "cgForwardAttack": cgForwardAttack,
       "cgLandAttack": cgLandAttack,
       "cgPingOfDeath": cgPingOfDeath,
       "cgTcpSynFlood": cgTcpSynFlood,
       "cgIntfSpoof": cgIntfSpoof,
       "cgMacViolation": cgMacViolation,
       "cgPortScan": cgPortScan,
       "cgBlockedFile": cgBlockedFile,
       "cgHaTransition": cgHaTransition,
       "cgHaNoHB": cgHaNoHB,
       "cgSwUpdate": cgSwUpdate,
       "cgPlatformSensor": cgPlatformSensor,
       "cgAuditArchive": cgAuditArchive}
)
