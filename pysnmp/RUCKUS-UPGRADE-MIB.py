# SNMP MIB module (RUCKUS-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-UPGRADE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:49 2024
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

(ruckusCommonUpgradeModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonUpgradeModule")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusUpgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusUpgradeObjects_ObjectIdentity = ObjectIdentity
ruckusUpgradeObjects = _RuckusUpgradeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1)
)
_RuckusFileTransfer_ObjectIdentity = ObjectIdentity
ruckusFileTransfer = _RuckusFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1)
)


class _RuckusFileTransferMethod_Type(Integer32):
    """Custom type ruckusFileTransferMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("tftp", 1),
          ("web", 3))
    )


_RuckusFileTransferMethod_Type.__name__ = "Integer32"
_RuckusFileTransferMethod_Object = MibScalar
ruckusFileTransferMethod = _RuckusFileTransferMethod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 1),
    _RuckusFileTransferMethod_Type()
)
ruckusFileTransferMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferMethod.setStatus("current")
_RuckusFileTransferHostName_Type = DisplayString
_RuckusFileTransferHostName_Object = MibScalar
ruckusFileTransferHostName = _RuckusFileTransferHostName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 2),
    _RuckusFileTransferHostName_Type()
)
ruckusFileTransferHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferHostName.setStatus("current")


class _RuckusFileTransferHostAddr_Type(OctetString):
    """Custom type ruckusFileTransferHostAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusFileTransferHostAddr_Type.__name__ = "OctetString"
_RuckusFileTransferHostAddr_Object = MibScalar
ruckusFileTransferHostAddr = _RuckusFileTransferHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 3),
    _RuckusFileTransferHostAddr_Type()
)
ruckusFileTransferHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferHostAddr.setStatus("current")


class _RuckusFileTransferControlFileName_Type(DisplayString):
    """Custom type ruckusFileTransferControlFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusFileTransferControlFileName_Type.__name__ = "DisplayString"
_RuckusFileTransferControlFileName_Object = MibScalar
ruckusFileTransferControlFileName = _RuckusFileTransferControlFileName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 4),
    _RuckusFileTransferControlFileName_Type()
)
ruckusFileTransferControlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferControlFileName.setStatus("current")


class _RuckusFileTransferFTPUsername_Type(DisplayString):
    """Custom type ruckusFileTransferFTPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusFileTransferFTPUsername_Type.__name__ = "DisplayString"
_RuckusFileTransferFTPUsername_Object = MibScalar
ruckusFileTransferFTPUsername = _RuckusFileTransferFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 5),
    _RuckusFileTransferFTPUsername_Type()
)
ruckusFileTransferFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferFTPUsername.setStatus("current")


class _RuckusFileTransferFTPPassword_Type(DisplayString):
    """Custom type ruckusFileTransferFTPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusFileTransferFTPPassword_Type.__name__ = "DisplayString"
_RuckusFileTransferFTPPassword_Object = MibScalar
ruckusFileTransferFTPPassword = _RuckusFileTransferFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 6),
    _RuckusFileTransferFTPPassword_Type()
)
ruckusFileTransferFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferFTPPassword.setStatus("current")
_RuckusFileTransferUpgradeNow_Type = TruthValue
_RuckusFileTransferUpgradeNow_Object = MibScalar
ruckusFileTransferUpgradeNow = _RuckusFileTransferUpgradeNow_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 7),
    _RuckusFileTransferUpgradeNow_Type()
)
ruckusFileTransferUpgradeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferUpgradeNow.setStatus("current")
_RuckusFileTransferTakeEffectImmediately_Type = TruthValue
_RuckusFileTransferTakeEffectImmediately_Object = MibScalar
ruckusFileTransferTakeEffectImmediately = _RuckusFileTransferTakeEffectImmediately_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 1, 8),
    _RuckusFileTransferTakeEffectImmediately_Type()
)
ruckusFileTransferTakeEffectImmediately.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusFileTransferTakeEffectImmediately.setStatus("current")
_RuckusAutoUpgrade_ObjectIdentity = ObjectIdentity
ruckusAutoUpgrade = _RuckusAutoUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2)
)


class _RuckusAutoUpgradeInitialCheckInterval_Type(Unsigned32):
    """Custom type ruckusAutoUpgradeInitialCheckInterval based on Unsigned32"""
    defaultValue = 5


_RuckusAutoUpgradeInitialCheckInterval_Object = MibScalar
ruckusAutoUpgradeInitialCheckInterval = _RuckusAutoUpgradeInitialCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2, 1),
    _RuckusAutoUpgradeInitialCheckInterval_Type()
)
ruckusAutoUpgradeInitialCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusAutoUpgradeInitialCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAutoUpgradeInitialCheckInterval.setUnits("minutes")


class _RuckusAutoUpgradeCheckInterval_Type(Unsigned32):
    """Custom type ruckusAutoUpgradeCheckInterval based on Unsigned32"""
    defaultValue = 720


_RuckusAutoUpgradeCheckInterval_Object = MibScalar
ruckusAutoUpgradeCheckInterval = _RuckusAutoUpgradeCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2, 2),
    _RuckusAutoUpgradeCheckInterval_Type()
)
ruckusAutoUpgradeCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusAutoUpgradeCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAutoUpgradeCheckInterval.setUnits("minutes")
_RuckusAutoUpgradeStatus_Type = Unsigned32
_RuckusAutoUpgradeStatus_Object = MibScalar
ruckusAutoUpgradeStatus = _RuckusAutoUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 5, 1, 1, 2, 3),
    _RuckusAutoUpgradeStatus_Type()
)
ruckusAutoUpgradeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusAutoUpgradeStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-UPGRADE-MIB",
    **{"ruckusUpgradeMIB": ruckusUpgradeMIB,
       "ruckusUpgradeObjects": ruckusUpgradeObjects,
       "ruckusFileTransfer": ruckusFileTransfer,
       "ruckusFileTransferMethod": ruckusFileTransferMethod,
       "ruckusFileTransferHostName": ruckusFileTransferHostName,
       "ruckusFileTransferHostAddr": ruckusFileTransferHostAddr,
       "ruckusFileTransferControlFileName": ruckusFileTransferControlFileName,
       "ruckusFileTransferFTPUsername": ruckusFileTransferFTPUsername,
       "ruckusFileTransferFTPPassword": ruckusFileTransferFTPPassword,
       "ruckusFileTransferUpgradeNow": ruckusFileTransferUpgradeNow,
       "ruckusFileTransferTakeEffectImmediately": ruckusFileTransferTakeEffectImmediately,
       "ruckusAutoUpgrade": ruckusAutoUpgrade,
       "ruckusAutoUpgradeInitialCheckInterval": ruckusAutoUpgradeInitialCheckInterval,
       "ruckusAutoUpgradeCheckInterval": ruckusAutoUpgradeCheckInterval,
       "ruckusAutoUpgradeStatus": ruckusAutoUpgradeStatus}
)
