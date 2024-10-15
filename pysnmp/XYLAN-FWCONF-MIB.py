# SNMP MIB module (XYLAN-FWCONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-FWCONF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:03 2024
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

(xylanFwArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanFwArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanFwConfig_ObjectIdentity = ObjectIdentity
xylanFwConfig = _XylanFwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1)
)


class _XylanFwStatus_Type(Integer32):
    """Custom type xylanFwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XylanFwStatus_Type.__name__ = "Integer32"
_XylanFwStatus_Object = MibScalar
xylanFwStatus = _XylanFwStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 1),
    _XylanFwStatus_Type()
)
xylanFwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFwStatus.setStatus("mandatory")


class _XylanFwMode_Type(Integer32):
    """Custom type xylanFwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("open", 2))
    )


_XylanFwMode_Type.__name__ = "Integer32"
_XylanFwMode_Object = MibScalar
xylanFwMode = _XylanFwMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 2),
    _XylanFwMode_Type()
)
xylanFwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFwMode.setStatus("mandatory")
_XylanFwPrimaryAddr_Type = IpAddress
_XylanFwPrimaryAddr_Object = MibScalar
xylanFwPrimaryAddr = _XylanFwPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 3),
    _XylanFwPrimaryAddr_Type()
)
xylanFwPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFwPrimaryAddr.setStatus("mandatory")


class _XylanFwPrimaryPassword_Type(DisplayString):
    """Custom type xylanFwPrimaryPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_XylanFwPrimaryPassword_Type.__name__ = "DisplayString"
_XylanFwPrimaryPassword_Object = MibScalar
xylanFwPrimaryPassword = _XylanFwPrimaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 4),
    _XylanFwPrimaryPassword_Type()
)
xylanFwPrimaryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFwPrimaryPassword.setStatus("mandatory")
_XylanFwBackupAddr_Type = IpAddress
_XylanFwBackupAddr_Object = MibScalar
xylanFwBackupAddr = _XylanFwBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 5),
    _XylanFwBackupAddr_Type()
)
xylanFwBackupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFwBackupAddr.setStatus("mandatory")


class _XylanFwBackupPassword_Type(DisplayString):
    """Custom type xylanFwBackupPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_XylanFwBackupPassword_Type.__name__ = "DisplayString"
_XylanFwBackupPassword_Object = MibScalar
xylanFwBackupPassword = _XylanFwBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 6),
    _XylanFwBackupPassword_Type()
)
xylanFwBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanFwBackupPassword.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-FWCONF-MIB",
    **{"xylanFwConfig": xylanFwConfig,
       "xylanFwStatus": xylanFwStatus,
       "xylanFwMode": xylanFwMode,
       "xylanFwPrimaryAddr": xylanFwPrimaryAddr,
       "xylanFwPrimaryPassword": xylanFwPrimaryPassword,
       "xylanFwBackupAddr": xylanFwBackupAddr,
       "xylanFwBackupPassword": xylanFwBackupPassword}
)
