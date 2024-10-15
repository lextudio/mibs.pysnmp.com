# SNMP MIB module (DEVCONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVCONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:05 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aniDevControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevControlResetDevice_Type = TruthValue
_AniDevControlResetDevice_Object = MibScalar
aniDevControlResetDevice = _AniDevControlResetDevice_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 4, 1),
    _AniDevControlResetDevice_Type()
)
aniDevControlResetDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevControlResetDevice.setStatus("current")
_AniDevControlSetFactoryDefaults_Type = TruthValue
_AniDevControlSetFactoryDefaults_Object = MibScalar
aniDevControlSetFactoryDefaults = _AniDevControlSetFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 4, 2),
    _AniDevControlSetFactoryDefaults_Type()
)
aniDevControlSetFactoryDefaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevControlSetFactoryDefaults.setStatus("current")
_AniDevControlStartUpload_Type = TruthValue
_AniDevControlStartUpload_Object = MibScalar
aniDevControlStartUpload = _AniDevControlStartUpload_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 4, 3),
    _AniDevControlStartUpload_Type()
)
aniDevControlStartUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevControlStartUpload.setStatus("current")


class _AniDevControlUploadState_Type(Integer32):
    """Custom type aniDevControlUploadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("successful", 1))
    )


_AniDevControlUploadState_Type.__name__ = "Integer32"
_AniDevControlUploadState_Object = MibScalar
aniDevControlUploadState = _AniDevControlUploadState_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 4, 4),
    _AniDevControlUploadState_Type()
)
aniDevControlUploadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevControlUploadState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVCONTROL-MIB",
    **{"aniDevControl": aniDevControl,
       "aniDevControlResetDevice": aniDevControlResetDevice,
       "aniDevControlSetFactoryDefaults": aniDevControlSetFactoryDefaults,
       "aniDevControlStartUpload": aniDevControlStartUpload,
       "aniDevControlUploadState": aniDevControlUploadState}
)
