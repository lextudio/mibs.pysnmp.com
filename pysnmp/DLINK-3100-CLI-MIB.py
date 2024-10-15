# SNMP MIB module (DLINK-3100-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-CLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:48 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

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

rlCli = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52)
)
rlCli.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlCliMibVersion_Type = Integer32
_RlCliMibVersion_Object = MibScalar
rlCliMibVersion = _RlCliMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 1),
    _RlCliMibVersion_Type()
)
rlCliMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCliMibVersion.setStatus("current")


class _RlCliPassword_Type(DisplayString):
    """Custom type rlCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlCliPassword_Type.__name__ = "DisplayString"
_RlCliPassword_Object = MibScalar
rlCliPassword = _RlCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 2),
    _RlCliPassword_Type()
)
rlCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliPassword.setStatus("current")


class _RlCliTimer_Type(Integer32):
    """Custom type rlCliTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RlCliTimer_Type.__name__ = "Integer32"
_RlCliTimer_Object = MibScalar
rlCliTimer = _RlCliTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 3),
    _RlCliTimer_Type()
)
rlCliTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliTimer.setStatus("current")
_RlCliFileEnable_Type = TruthValue
_RlCliFileEnable_Object = MibScalar
rlCliFileEnable = _RlCliFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 4),
    _RlCliFileEnable_Type()
)
rlCliFileEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCliFileEnable.setStatus("current")
_RlCliFileEnableAfterReset_Type = TruthValue
_RlCliFileEnableAfterReset_Object = MibScalar
rlCliFileEnableAfterReset = _RlCliFileEnableAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 5),
    _RlCliFileEnableAfterReset_Type()
)
rlCliFileEnableAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliFileEnableAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-CLI-MIB",
    **{"rlCli": rlCli,
       "rlCliMibVersion": rlCliMibVersion,
       "rlCliPassword": rlCliPassword,
       "rlCliTimer": rlCliTimer,
       "rlCliFileEnable": rlCliFileEnable,
       "rlCliFileEnableAfterReset": rlCliFileEnableAfterReset}
)
