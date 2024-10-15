# SNMP MIB module (NSC-BORDERGUARD-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSC-BORDERGUARD-TRAP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:25 2024
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

(nscBorderGuard,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscBorderGuard")

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

_NscBorderGuardTraps_ObjectIdentity = ObjectIdentity
nscBorderGuardTraps = _NscBorderGuardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1)
)
_NscBorderGuardTrapsBadImage_Type = Integer32
_NscBorderGuardTrapsBadImage_Object = MibScalar
nscBorderGuardTrapsBadImage = _NscBorderGuardTrapsBadImage_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 1),
    _NscBorderGuardTrapsBadImage_Type()
)
nscBorderGuardTrapsBadImage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscBorderGuardTrapsBadImage.setStatus("mandatory")
_NscBorderGuardTrapsCurrentImage_Type = Integer32
_NscBorderGuardTrapsCurrentImage_Object = MibScalar
nscBorderGuardTrapsCurrentImage = _NscBorderGuardTrapsCurrentImage_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 2),
    _NscBorderGuardTrapsCurrentImage_Type()
)
nscBorderGuardTrapsCurrentImage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscBorderGuardTrapsCurrentImage.setStatus("mandatory")
_NscBorderGuardTrapsBadFileSystem_Type = Integer32
_NscBorderGuardTrapsBadFileSystem_Object = MibScalar
nscBorderGuardTrapsBadFileSystem = _NscBorderGuardTrapsBadFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 3),
    _NscBorderGuardTrapsBadFileSystem_Type()
)
nscBorderGuardTrapsBadFileSystem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscBorderGuardTrapsBadFileSystem.setStatus("mandatory")
_NscBorderGuardTrapsSoftFault_Type = Integer32
_NscBorderGuardTrapsSoftFault_Object = MibScalar
nscBorderGuardTrapsSoftFault = _NscBorderGuardTrapsSoftFault_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 4),
    _NscBorderGuardTrapsSoftFault_Type()
)
nscBorderGuardTrapsSoftFault.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscBorderGuardTrapsSoftFault.setStatus("mandatory")


class _NscBorderGuardTrapsEventReason_Type(DisplayString):
    """Custom type nscBorderGuardTrapsEventReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NscBorderGuardTrapsEventReason_Type.__name__ = "DisplayString"
_NscBorderGuardTrapsEventReason_Object = MibScalar
nscBorderGuardTrapsEventReason = _NscBorderGuardTrapsEventReason_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 5),
    _NscBorderGuardTrapsEventReason_Type()
)
nscBorderGuardTrapsEventReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nscBorderGuardTrapsEventReason.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nscBorderGuardBadCRC = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 0, 1)
)
nscBorderGuardBadCRC.setObjects(
      *(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsBadImage"),
        ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsCurrentImage"),
        ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
)
if mibBuilder.loadTexts:
    nscBorderGuardBadCRC.setStatus(
        ""
    )

nscBorderGuardBadFileSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 0, 2)
)
nscBorderGuardBadFileSystem.setObjects(
      *(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsBadFileSystem"),
        ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
)
if mibBuilder.loadTexts:
    nscBorderGuardBadFileSystem.setStatus(
        ""
    )

nscBorderGuardSoftFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 0, 3)
)
nscBorderGuardSoftFault.setObjects(
      *(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsSoftFault"),
        ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
)
if mibBuilder.loadTexts:
    nscBorderGuardSoftFault.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSC-BORDERGUARD-TRAP",
    **{"nscBorderGuardTraps": nscBorderGuardTraps,
       "nscBorderGuardBadCRC": nscBorderGuardBadCRC,
       "nscBorderGuardBadFileSystem": nscBorderGuardBadFileSystem,
       "nscBorderGuardSoftFault": nscBorderGuardSoftFault,
       "nscBorderGuardTrapsBadImage": nscBorderGuardTrapsBadImage,
       "nscBorderGuardTrapsCurrentImage": nscBorderGuardTrapsCurrentImage,
       "nscBorderGuardTrapsBadFileSystem": nscBorderGuardTrapsBadFileSystem,
       "nscBorderGuardTrapsSoftFault": nscBorderGuardTrapsSoftFault,
       "nscBorderGuardTrapsEventReason": nscBorderGuardTrapsEventReason}
)
