# SNMP MIB module (RADLAN-RCLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-RCLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:10 2024
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
    "RADLAN-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rlRCli = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 70)
)
rlRCli.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlRCliMibVersion_Type = Integer32
_RlRCliMibVersion_Object = MibScalar
rlRCliMibVersion = _RlRCliMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 1),
    _RlRCliMibVersion_Type()
)
rlRCliMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRCliMibVersion.setStatus("current")


class _RlRCliUserPassword_Type(OctetString):
    """Custom type rlRCliUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRCliUserPassword_Type.__name__ = "OctetString"
_RlRCliUserPassword_Object = MibScalar
rlRCliUserPassword = _RlRCliUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 2),
    _RlRCliUserPassword_Type()
)
rlRCliUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliUserPassword.setStatus("current")


class _RlRCliEnablePassword_Type(OctetString):
    """Custom type rlRCliEnablePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRCliEnablePassword_Type.__name__ = "OctetString"
_RlRCliEnablePassword_Object = MibScalar
rlRCliEnablePassword = _RlRCliEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 3),
    _RlRCliEnablePassword_Type()
)
rlRCliEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliEnablePassword.setStatus("current")


class _RlRCliConfigPassword_Type(OctetString):
    """Custom type rlRCliConfigPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRCliConfigPassword_Type.__name__ = "OctetString"
_RlRCliConfigPassword_Object = MibScalar
rlRCliConfigPassword = _RlRCliConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 4),
    _RlRCliConfigPassword_Type()
)
rlRCliConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliConfigPassword.setStatus("current")


class _RlRCliTimer_Type(Integer32):
    """Custom type rlRCliTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RlRCliTimer_Type.__name__ = "Integer32"
_RlRCliTimer_Object = MibScalar
rlRCliTimer = _RlRCliTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 5),
    _RlRCliTimer_Type()
)
rlRCliTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRCliTimer.setStatus("current")


class _RlRcliFileAction_Type(Integer32):
    """Custom type rlRcliFileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUsedAfterReset", 1),
          ("usedAfterReset", 2))
    )


_RlRcliFileAction_Type.__name__ = "Integer32"
_RlRcliFileAction_Object = MibScalar
rlRcliFileAction = _RlRcliFileAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 70, 6),
    _RlRcliFileAction_Type()
)
rlRcliFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRcliFileAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-RCLI-MIB",
    **{"rlRCli": rlRCli,
       "rlRCliMibVersion": rlRCliMibVersion,
       "rlRCliUserPassword": rlRCliUserPassword,
       "rlRCliEnablePassword": rlRCliEnablePassword,
       "rlRCliConfigPassword": rlRCliConfigPassword,
       "rlRCliTimer": rlRCliTimer,
       "rlRcliFileAction": rlRcliFileAction}
)
