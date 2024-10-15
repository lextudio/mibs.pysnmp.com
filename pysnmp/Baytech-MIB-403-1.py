# SNMP MIB module (Baytech-MIB-403-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Baytech-MIB-403-1
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:23 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Baytech_ObjectIdentity = ObjectIdentity
baytech = _Baytech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779)
)
_Btadevices_ObjectIdentity = ObjectIdentity
btadevices = _Btadevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1)
)
_SBTAIdent_ObjectIdentity = ObjectIdentity
sBTAIdent = _SBTAIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 1)
)
_SBTAIdentFirmwareRev_Type = DisplayString
_SBTAIdentFirmwareRev_Object = MibScalar
sBTAIdentFirmwareRev = _SBTAIdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 1, 1),
    _SBTAIdentFirmwareRev_Type()
)
sBTAIdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAIdentFirmwareRev.setStatus("mandatory")
_SBTAIdentSerialNumber_Type = Integer32
_SBTAIdentSerialNumber_Object = MibScalar
sBTAIdentSerialNumber = _SBTAIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 1, 2),
    _SBTAIdentSerialNumber_Type()
)
sBTAIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAIdentSerialNumber.setStatus("mandatory")


class _SBTAIdentUnitName_Type(DisplayString):
    """Custom type sBTAIdentUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SBTAIdentUnitName_Type.__name__ = "DisplayString"
_SBTAIdentUnitName_Object = MibScalar
sBTAIdentUnitName = _SBTAIdentUnitName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 1, 3),
    _SBTAIdentUnitName_Type()
)
sBTAIdentUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAIdentUnitName.setStatus("mandatory")
_SBTANetworkConfig_ObjectIdentity = ObjectIdentity
sBTANetworkConfig = _SBTANetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2)
)


class _SBTANetworkConfigBootpEnable_Type(Integer32):
    """Custom type sBTANetworkConfigBootpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigBootpEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigBootpEnable_Object = MibScalar
sBTANetworkConfigBootpEnable = _SBTANetworkConfigBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 1),
    _SBTANetworkConfigBootpEnable_Type()
)
sBTANetworkConfigBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigBootpEnable.setStatus("mandatory")


class _SBTANetworkConfigDHCPEnable_Type(Integer32):
    """Custom type sBTANetworkConfigDHCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigDHCPEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigDHCPEnable_Object = MibScalar
sBTANetworkConfigDHCPEnable = _SBTANetworkConfigDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 2),
    _SBTANetworkConfigDHCPEnable_Type()
)
sBTANetworkConfigDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigDHCPEnable.setStatus("mandatory")


class _SBTANetworkConfigSSHEnable_Type(Integer32):
    """Custom type sBTANetworkConfigSSHEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigSSHEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigSSHEnable_Object = MibScalar
sBTANetworkConfigSSHEnable = _SBTANetworkConfigSSHEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 3),
    _SBTANetworkConfigSSHEnable_Type()
)
sBTANetworkConfigSSHEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigSSHEnable.setStatus("mandatory")


class _SBTANetworkConfigTelnetEnable_Type(Integer32):
    """Custom type sBTANetworkConfigTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigTelnetEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigTelnetEnable_Object = MibScalar
sBTANetworkConfigTelnetEnable = _SBTANetworkConfigTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 4),
    _SBTANetworkConfigTelnetEnable_Type()
)
sBTANetworkConfigTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigTelnetEnable.setStatus("mandatory")
_SBTANetworkConfigActivityTimeout_Type = Integer32
_SBTANetworkConfigActivityTimeout_Object = MibScalar
sBTANetworkConfigActivityTimeout = _SBTANetworkConfigActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 5),
    _SBTANetworkConfigActivityTimeout_Type()
)
sBTANetworkConfigActivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigActivityTimeout.setStatus("mandatory")


class _SBTANetworkConfigDirectConnEnable_Type(Integer32):
    """Custom type sBTANetworkConfigDirectConnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigDirectConnEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigDirectConnEnable_Object = MibScalar
sBTANetworkConfigDirectConnEnable = _SBTANetworkConfigDirectConnEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 6),
    _SBTANetworkConfigDirectConnEnable_Type()
)
sBTANetworkConfigDirectConnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigDirectConnEnable.setStatus("mandatory")
_SBTANetworkConfigSNMP_ObjectIdentity = ObjectIdentity
sBTANetworkConfigSNMP = _SBTANetworkConfigSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8)
)
_SBTANetworkConfigSNMPReadOnlyCommunity_Type = DisplayString
_SBTANetworkConfigSNMPReadOnlyCommunity_Object = MibScalar
sBTANetworkConfigSNMPReadOnlyCommunity = _SBTANetworkConfigSNMPReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 1),
    _SBTANetworkConfigSNMPReadOnlyCommunity_Type()
)
sBTANetworkConfigSNMPReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigSNMPReadOnlyCommunity.setStatus("mandatory")
_SBTANetworkConfigSNMPReadWriteCommunity_Type = DisplayString
_SBTANetworkConfigSNMPReadWriteCommunity_Object = MibScalar
sBTANetworkConfigSNMPReadWriteCommunity = _SBTANetworkConfigSNMPReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 2),
    _SBTANetworkConfigSNMPReadWriteCommunity_Type()
)
sBTANetworkConfigSNMPReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigSNMPReadWriteCommunity.setStatus("mandatory")
_SBTANetworkConfigSNMPNumTrapReceivers_Type = Integer32
_SBTANetworkConfigSNMPNumTrapReceivers_Object = MibScalar
sBTANetworkConfigSNMPNumTrapReceivers = _SBTANetworkConfigSNMPNumTrapReceivers_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 3),
    _SBTANetworkConfigSNMPNumTrapReceivers_Type()
)
sBTANetworkConfigSNMPNumTrapReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTANetworkConfigSNMPNumTrapReceivers.setStatus("mandatory")
_SBTANetworkConfigSNMPTrapReceiverTable_Object = MibTable
sBTANetworkConfigSNMPTrapReceiverTable = _SBTANetworkConfigSNMPTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    sBTANetworkConfigSNMPTrapReceiverTable.setStatus("mandatory")
_SBTANetworkConfigSNMPTrapReceiverEntry_Object = MibTableRow
sBTANetworkConfigSNMPTrapReceiverEntry = _SBTANetworkConfigSNMPTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 4, 1)
)
sBTANetworkConfigSNMPTrapReceiverEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "trapIndex"),
)
if mibBuilder.loadTexts:
    sBTANetworkConfigSNMPTrapReceiverEntry.setStatus("mandatory")
_TrapIndex_Type = Integer32
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 4, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")
_ReceiverAddress_Type = IpAddress
_ReceiverAddress_Object = MibTableColumn
receiverAddress = _ReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 8, 4, 1, 2),
    _ReceiverAddress_Type()
)
receiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverAddress.setStatus("mandatory")
_SBTANetworkConfigRadius_ObjectIdentity = ObjectIdentity
sBTANetworkConfigRadius = _SBTANetworkConfigRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 9)
)


class _SBTANetworkConfigRadiusEnable_Type(Integer32):
    """Custom type sBTANetworkConfigRadiusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SBTANetworkConfigRadiusEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigRadiusEnable_Object = MibScalar
sBTANetworkConfigRadiusEnable = _SBTANetworkConfigRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 9, 1),
    _SBTANetworkConfigRadiusEnable_Type()
)
sBTANetworkConfigRadiusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigRadiusEnable.setStatus("mandatory")
_SBTANetworkConfigRadiusPrimaryServer_Type = IpAddress
_SBTANetworkConfigRadiusPrimaryServer_Object = MibScalar
sBTANetworkConfigRadiusPrimaryServer = _SBTANetworkConfigRadiusPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 9, 2),
    _SBTANetworkConfigRadiusPrimaryServer_Type()
)
sBTANetworkConfigRadiusPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigRadiusPrimaryServer.setStatus("mandatory")
_SBTANetworkConfigRadiusSecondaryServer_Type = IpAddress
_SBTANetworkConfigRadiusSecondaryServer_Object = MibScalar
sBTANetworkConfigRadiusSecondaryServer = _SBTANetworkConfigRadiusSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 9, 3),
    _SBTANetworkConfigRadiusSecondaryServer_Type()
)
sBTANetworkConfigRadiusSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigRadiusSecondaryServer.setStatus("mandatory")


class _SBTANetworkConfigRadiusLocalLogin_Type(Integer32):
    """Custom type sBTANetworkConfigRadiusLocalLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SBTANetworkConfigRadiusLocalLogin_Type.__name__ = "Integer32"
_SBTANetworkConfigRadiusLocalLogin_Object = MibScalar
sBTANetworkConfigRadiusLocalLogin = _SBTANetworkConfigRadiusLocalLogin_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 9, 4),
    _SBTANetworkConfigRadiusLocalLogin_Type()
)
sBTANetworkConfigRadiusLocalLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigRadiusLocalLogin.setStatus("mandatory")
_SBTANetworkConfigWEB_ObjectIdentity = ObjectIdentity
sBTANetworkConfigWEB = _SBTANetworkConfigWEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 10)
)


class _SBTANetworkConfigWebEnable_Type(Integer32):
    """Custom type sBTANetworkConfigWebEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigWebEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigWebEnable_Object = MibScalar
sBTANetworkConfigWebEnable = _SBTANetworkConfigWebEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 10, 1),
    _SBTANetworkConfigWebEnable_Type()
)
sBTANetworkConfigWebEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigWebEnable.setStatus("mandatory")


class _SBTANetworkConfigWebSecureEnable_Type(Integer32):
    """Custom type sBTANetworkConfigWebSecureEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigWebSecureEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigWebSecureEnable_Object = MibScalar
sBTANetworkConfigWebSecureEnable = _SBTANetworkConfigWebSecureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 10, 2),
    _SBTANetworkConfigWebSecureEnable_Type()
)
sBTANetworkConfigWebSecureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigWebSecureEnable.setStatus("mandatory")


class _SBTANetworkConfigWebLoginEnable_Type(Integer32):
    """Custom type sBTANetworkConfigWebLoginEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SBTANetworkConfigWebLoginEnable_Type.__name__ = "Integer32"
_SBTANetworkConfigWebLoginEnable_Object = MibScalar
sBTANetworkConfigWebLoginEnable = _SBTANetworkConfigWebLoginEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 10, 3),
    _SBTANetworkConfigWebLoginEnable_Type()
)
sBTANetworkConfigWebLoginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigWebLoginEnable.setStatus("mandatory")
_SBTANetworkConfigWebActivityTimeout_Type = Integer32
_SBTANetworkConfigWebActivityTimeout_Object = MibScalar
sBTANetworkConfigWebActivityTimeout = _SBTANetworkConfigWebActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 2, 10, 4),
    _SBTANetworkConfigWebActivityTimeout_Type()
)
sBTANetworkConfigWebActivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTANetworkConfigWebActivityTimeout.setStatus("mandatory")
_SBTAModules_ObjectIdentity = ObjectIdentity
sBTAModules = _SBTAModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3)
)
_SBTAModulesNumberOfModules_Type = Integer32
_SBTAModulesNumberOfModules_Object = MibScalar
sBTAModulesNumberOfModules = _SBTAModulesNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 1),
    _SBTAModulesNumberOfModules_Type()
)
sBTAModulesNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesNumberOfModules.setStatus("mandatory")
_SBTAModulesModulesInstalled_Type = DisplayString
_SBTAModulesModulesInstalled_Object = MibScalar
sBTAModulesModulesInstalled = _SBTAModulesModulesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 2),
    _SBTAModulesModulesInstalled_Type()
)
sBTAModulesModulesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesModulesInstalled.setStatus("mandatory")
_SBTAModulesResetModulesCmd_Type = Integer32
_SBTAModulesResetModulesCmd_Object = MibScalar
sBTAModulesResetModulesCmd = _SBTAModulesResetModulesCmd_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 3),
    _SBTAModulesResetModulesCmd_Type()
)
sBTAModulesResetModulesCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesResetModulesCmd.setStatus("deprecated")
_SBTAModulesNumberOfIntelligentModules_Type = Integer32
_SBTAModulesNumberOfIntelligentModules_Object = MibScalar
sBTAModulesNumberOfIntelligentModules = _SBTAModulesNumberOfIntelligentModules_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 4),
    _SBTAModulesNumberOfIntelligentModules_Type()
)
sBTAModulesNumberOfIntelligentModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesNumberOfIntelligentModules.setStatus("mandatory")
_SBTAModulesRPC_ObjectIdentity = ObjectIdentity
sBTAModulesRPC = _SBTAModulesRPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5)
)
_SBTAModulesNumberOfRPCModules_Type = Integer32
_SBTAModulesNumberOfRPCModules_Object = MibScalar
sBTAModulesNumberOfRPCModules = _SBTAModulesNumberOfRPCModules_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 1),
    _SBTAModulesNumberOfRPCModules_Type()
)
sBTAModulesNumberOfRPCModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesNumberOfRPCModules.setStatus("mandatory")
_SBTAModulesRPCTable_Object = MibTable
sBTAModulesRPCTable = _SBTAModulesRPCTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    sBTAModulesRPCTable.setStatus("mandatory")
_SBTAModulesRPCEntry_Object = MibTableRow
sBTAModulesRPCEntry = _SBTAModulesRPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1)
)
sBTAModulesRPCEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sBTAModulesRPCIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesRPCEntry.setStatus("mandatory")
_SBTAModulesRPCIndex_Type = Integer32
_SBTAModulesRPCIndex_Object = MibTableColumn
sBTAModulesRPCIndex = _SBTAModulesRPCIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 1),
    _SBTAModulesRPCIndex_Type()
)
sBTAModulesRPCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCIndex.setStatus("mandatory")
_SBTAModulesRPCName_Type = DisplayString
_SBTAModulesRPCName_Object = MibTableColumn
sBTAModulesRPCName = _SBTAModulesRPCName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 2),
    _SBTAModulesRPCName_Type()
)
sBTAModulesRPCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCName.setStatus("mandatory")
_SBTAModulesRPCFirmwareVersion_Type = DisplayString
_SBTAModulesRPCFirmwareVersion_Object = MibTableColumn
sBTAModulesRPCFirmwareVersion = _SBTAModulesRPCFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 3),
    _SBTAModulesRPCFirmwareVersion_Type()
)
sBTAModulesRPCFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCFirmwareVersion.setStatus("mandatory")
_SBTAModulesRPCCurrent_Type = Integer32
_SBTAModulesRPCCurrent_Object = MibTableColumn
sBTAModulesRPCCurrent = _SBTAModulesRPCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 4),
    _SBTAModulesRPCCurrent_Type()
)
sBTAModulesRPCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCCurrent.setStatus("mandatory")
_SBTAModulesRPCMaxCurrent_Type = Integer32
_SBTAModulesRPCMaxCurrent_Object = MibTableColumn
sBTAModulesRPCMaxCurrent = _SBTAModulesRPCMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 5),
    _SBTAModulesRPCMaxCurrent_Type()
)
sBTAModulesRPCMaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCMaxCurrent.setStatus("mandatory")
_SBTAModulesRPCVoltage_Type = Integer32
_SBTAModulesRPCVoltage_Object = MibTableColumn
sBTAModulesRPCVoltage = _SBTAModulesRPCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 6),
    _SBTAModulesRPCVoltage_Type()
)
sBTAModulesRPCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCVoltage.setStatus("mandatory")
_SBTAModulesRPCPower_Type = Integer32
_SBTAModulesRPCPower_Object = MibTableColumn
sBTAModulesRPCPower = _SBTAModulesRPCPower_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 7),
    _SBTAModulesRPCPower_Type()
)
sBTAModulesRPCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCPower.setStatus("mandatory")
_SBTAModulesRPCTemperature_Type = Integer32
_SBTAModulesRPCTemperature_Object = MibTableColumn
sBTAModulesRPCTemperature = _SBTAModulesRPCTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 8),
    _SBTAModulesRPCTemperature_Type()
)
sBTAModulesRPCTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCTemperature.setStatus("mandatory")
_SBTAModulesRPCRebootTimeout_Type = Integer32
_SBTAModulesRPCRebootTimeout_Object = MibTableColumn
sBTAModulesRPCRebootTimeout = _SBTAModulesRPCRebootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 9),
    _SBTAModulesRPCRebootTimeout_Type()
)
sBTAModulesRPCRebootTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCRebootTimeout.setStatus("mandatory")


class _SBTAModulesRPCAllOutletsCmd_Type(Integer32):
    """Custom type sBTAModulesRPCAllOutletsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lockoff", 4),
          ("lockon", 3),
          ("off", 0),
          ("on", 1),
          ("reboot", 2),
          ("unknown", 6),
          ("unlock", 5))
    )


_SBTAModulesRPCAllOutletsCmd_Type.__name__ = "Integer32"
_SBTAModulesRPCAllOutletsCmd_Object = MibTableColumn
sBTAModulesRPCAllOutletsCmd = _SBTAModulesRPCAllOutletsCmd_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 10),
    _SBTAModulesRPCAllOutletsCmd_Type()
)
sBTAModulesRPCAllOutletsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCAllOutletsCmd.setStatus("mandatory")
_SBTAModulesRPCAllOutletsStatus_Type = DisplayString
_SBTAModulesRPCAllOutletsStatus_Object = MibTableColumn
sBTAModulesRPCAllOutletsStatus = _SBTAModulesRPCAllOutletsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 11),
    _SBTAModulesRPCAllOutletsStatus_Type()
)
sBTAModulesRPCAllOutletsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCAllOutletsStatus.setStatus("mandatory")
_SBTAModulesRPCCurrentAlarmThreshold_Type = Integer32
_SBTAModulesRPCCurrentAlarmThreshold_Object = MibTableColumn
sBTAModulesRPCCurrentAlarmThreshold = _SBTAModulesRPCCurrentAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 12),
    _SBTAModulesRPCCurrentAlarmThreshold_Type()
)
sBTAModulesRPCCurrentAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCCurrentAlarmThreshold.setStatus("mandatory")
_SBTAModulesRPCOverVoltageThreshold_Type = Integer32
_SBTAModulesRPCOverVoltageThreshold_Object = MibTableColumn
sBTAModulesRPCOverVoltageThreshold = _SBTAModulesRPCOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 13),
    _SBTAModulesRPCOverVoltageThreshold_Type()
)
sBTAModulesRPCOverVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCOverVoltageThreshold.setStatus("mandatory")
_SBTAModulesRPCUnderVoltageThreshold_Type = Integer32
_SBTAModulesRPCUnderVoltageThreshold_Object = MibTableColumn
sBTAModulesRPCUnderVoltageThreshold = _SBTAModulesRPCUnderVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 14),
    _SBTAModulesRPCUnderVoltageThreshold_Type()
)
sBTAModulesRPCUnderVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCUnderVoltageThreshold.setStatus("mandatory")
_SBTAModulesRPCNumberOfOutlets_Type = Integer32
_SBTAModulesRPCNumberOfOutlets_Object = MibTableColumn
sBTAModulesRPCNumberOfOutlets = _SBTAModulesRPCNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 15),
    _SBTAModulesRPCNumberOfOutlets_Type()
)
sBTAModulesRPCNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCNumberOfOutlets.setStatus("mandatory")


class _SBTAModulesRPCCircuitBreaker_Type(Integer32):
    """Custom type sBTAModulesRPCCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SBTAModulesRPCCircuitBreaker_Type.__name__ = "Integer32"
_SBTAModulesRPCCircuitBreaker_Object = MibTableColumn
sBTAModulesRPCCircuitBreaker = _SBTAModulesRPCCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 16),
    _SBTAModulesRPCCircuitBreaker_Type()
)
sBTAModulesRPCCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCCircuitBreaker.setStatus("mandatory")
_SBTAModulesRPCOverTempThreshold_Type = Integer32
_SBTAModulesRPCOverTempThreshold_Object = MibTableColumn
sBTAModulesRPCOverTempThreshold = _SBTAModulesRPCOverTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 17),
    _SBTAModulesRPCOverTempThreshold_Type()
)
sBTAModulesRPCOverTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCOverTempThreshold.setStatus("mandatory")
_SBTAModulesRPCUnitVA_Type = Integer32
_SBTAModulesRPCUnitVA_Object = MibTableColumn
sBTAModulesRPCUnitVA = _SBTAModulesRPCUnitVA_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 18),
    _SBTAModulesRPCUnitVA_Type()
)
sBTAModulesRPCUnitVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCUnitVA.setStatus("mandatory")
_SBTAModulesRPCNumberOfBreakers_Type = Integer32
_SBTAModulesRPCNumberOfBreakers_Object = MibTableColumn
sBTAModulesRPCNumberOfBreakers = _SBTAModulesRPCNumberOfBreakers_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 19),
    _SBTAModulesRPCNumberOfBreakers_Type()
)
sBTAModulesRPCNumberOfBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCNumberOfBreakers.setStatus("mandatory")
_SBTAModulesRPCLowCurrentThreshold_Type = Integer32
_SBTAModulesRPCLowCurrentThreshold_Object = MibTableColumn
sBTAModulesRPCLowCurrentThreshold = _SBTAModulesRPCLowCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 20),
    _SBTAModulesRPCLowCurrentThreshold_Type()
)
sBTAModulesRPCLowCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCLowCurrentThreshold.setStatus("mandatory")
_SBTAModulesRPCVoltageSource_Type = Integer32
_SBTAModulesRPCVoltageSource_Object = MibTableColumn
sBTAModulesRPCVoltageSource = _SBTAModulesRPCVoltageSource_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 21),
    _SBTAModulesRPCVoltageSource_Type()
)
sBTAModulesRPCVoltageSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCVoltageSource.setStatus("mandatory")
_SBTAModulesRPCSourceSwitchCount_Type = Integer32
_SBTAModulesRPCSourceSwitchCount_Object = MibTableColumn
sBTAModulesRPCSourceSwitchCount = _SBTAModulesRPCSourceSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 22),
    _SBTAModulesRPCSourceSwitchCount_Type()
)
sBTAModulesRPCSourceSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCSourceSwitchCount.setStatus("mandatory")
_SBTAModulesRPCNumberOfSensors_Type = Integer32
_SBTAModulesRPCNumberOfSensors_Object = MibTableColumn
sBTAModulesRPCNumberOfSensors = _SBTAModulesRPCNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 23),
    _SBTAModulesRPCNumberOfSensors_Type()
)
sBTAModulesRPCNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCNumberOfSensors.setStatus("mandatory")
_SBTAModulesRPCType_Type = DisplayString
_SBTAModulesRPCType_Object = MibTableColumn
sBTAModulesRPCType = _SBTAModulesRPCType_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 2, 1, 24),
    _SBTAModulesRPCType_Type()
)
sBTAModulesRPCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCType.setStatus("mandatory")
_SBTAModulesRPCOutletTable_Object = MibTable
sBTAModulesRPCOutletTable = _SBTAModulesRPCOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    sBTAModulesRPCOutletTable.setStatus("mandatory")
_SBTAModulesRPCOutletEntry_Object = MibTableRow
sBTAModulesRPCOutletEntry = _SBTAModulesRPCOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 3, 1)
)
sBTAModulesRPCOutletEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sBTAModulesRPCOutletModuleIndex"),
    (0, "Baytech-MIB-403-1", "sBTAModulesRPCOutletIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesRPCOutletEntry.setStatus("mandatory")
_SBTAModulesRPCOutletModuleIndex_Type = Integer32
_SBTAModulesRPCOutletModuleIndex_Object = MibTableColumn
sBTAModulesRPCOutletModuleIndex = _SBTAModulesRPCOutletModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 3, 1, 1),
    _SBTAModulesRPCOutletModuleIndex_Type()
)
sBTAModulesRPCOutletModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCOutletModuleIndex.setStatus("mandatory")
_SBTAModulesRPCOutletIndex_Type = Integer32
_SBTAModulesRPCOutletIndex_Object = MibTableColumn
sBTAModulesRPCOutletIndex = _SBTAModulesRPCOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 3, 1, 2),
    _SBTAModulesRPCOutletIndex_Type()
)
sBTAModulesRPCOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCOutletIndex.setStatus("mandatory")


class _SBTAModulesRPCOutletState_Type(Integer32):
    """Custom type sBTAModulesRPCOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lockoff", 4),
          ("lockon", 3),
          ("off", 0),
          ("on", 1),
          ("reboot", 2),
          ("unknown", 6),
          ("unlock", 5))
    )


_SBTAModulesRPCOutletState_Type.__name__ = "Integer32"
_SBTAModulesRPCOutletState_Object = MibTableColumn
sBTAModulesRPCOutletState = _SBTAModulesRPCOutletState_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 3, 1, 3),
    _SBTAModulesRPCOutletState_Type()
)
sBTAModulesRPCOutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCOutletState.setStatus("mandatory")
_SBTAModulesRPCOutletName_Type = DisplayString
_SBTAModulesRPCOutletName_Object = MibTableColumn
sBTAModulesRPCOutletName = _SBTAModulesRPCOutletName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 3, 1, 4),
    _SBTAModulesRPCOutletName_Type()
)
sBTAModulesRPCOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCOutletName.setStatus("mandatory")
_SBTAModulesRPCGroupCmd_Type = DisplayString
_SBTAModulesRPCGroupCmd_Object = MibScalar
sBTAModulesRPCGroupCmd = _SBTAModulesRPCGroupCmd_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 4),
    _SBTAModulesRPCGroupCmd_Type()
)
sBTAModulesRPCGroupCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCGroupCmd.setStatus("mandatory")
_SBTAModulesRPCModPortTable_Object = MibTable
sBTAModulesRPCModPortTable = _SBTAModulesRPCModPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5)
)
if mibBuilder.loadTexts:
    sBTAModulesRPCModPortTable.setStatus("mandatory")
_SBTAModulesRPCModPortEntry_Object = MibTableRow
sBTAModulesRPCModPortEntry = _SBTAModulesRPCModPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1)
)
sBTAModulesRPCModPortEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sRPCModuleIndex"),
    (0, "Baytech-MIB-403-1", "sRPCPortIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesRPCModPortEntry.setStatus("mandatory")
_SRPCModuleIndex_Type = Integer32
_SRPCModuleIndex_Object = MibTableColumn
sRPCModuleIndex = _SRPCModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 1),
    _SRPCModuleIndex_Type()
)
sRPCModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCModuleIndex.setStatus("mandatory")
_SRPCPortIndex_Type = Integer32
_SRPCPortIndex_Object = MibTableColumn
sRPCPortIndex = _SRPCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 2),
    _SRPCPortIndex_Type()
)
sRPCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCPortIndex.setStatus("mandatory")
_SRPCType_Type = DisplayString
_SRPCType_Object = MibTableColumn
sRPCType = _SRPCType_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 3),
    _SRPCType_Type()
)
sRPCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCType.setStatus("mandatory")
_SRPCName_Type = DisplayString
_SRPCName_Object = MibTableColumn
sRPCName = _SRPCName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 4),
    _SRPCName_Type()
)
sRPCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCName.setStatus("mandatory")
_SRPCFirmwareVersion_Type = DisplayString
_SRPCFirmwareVersion_Object = MibTableColumn
sRPCFirmwareVersion = _SRPCFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 5),
    _SRPCFirmwareVersion_Type()
)
sRPCFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCFirmwareVersion.setStatus("mandatory")
_SRPCCurrent_Type = Integer32
_SRPCCurrent_Object = MibTableColumn
sRPCCurrent = _SRPCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 6),
    _SRPCCurrent_Type()
)
sRPCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCCurrent.setStatus("mandatory")
_SRPCMaxCurrent_Type = Integer32
_SRPCMaxCurrent_Object = MibTableColumn
sRPCMaxCurrent = _SRPCMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 7),
    _SRPCMaxCurrent_Type()
)
sRPCMaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCMaxCurrent.setStatus("mandatory")
_SRPCVoltage_Type = Integer32
_SRPCVoltage_Object = MibTableColumn
sRPCVoltage = _SRPCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 8),
    _SRPCVoltage_Type()
)
sRPCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCVoltage.setStatus("mandatory")
_SRPCPower_Type = Integer32
_SRPCPower_Object = MibTableColumn
sRPCPower = _SRPCPower_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 9),
    _SRPCPower_Type()
)
sRPCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCPower.setStatus("mandatory")
_SRPCTemperature_Type = Integer32
_SRPCTemperature_Object = MibTableColumn
sRPCTemperature = _SRPCTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 10),
    _SRPCTemperature_Type()
)
sRPCTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCTemperature.setStatus("mandatory")
_SRPCRebootTimeout_Type = Integer32
_SRPCRebootTimeout_Object = MibTableColumn
sRPCRebootTimeout = _SRPCRebootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 11),
    _SRPCRebootTimeout_Type()
)
sRPCRebootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCRebootTimeout.setStatus("mandatory")


class _SRPCAllOutletsCmd_Type(Integer32):
    """Custom type sRPCAllOutletsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lockoff", 4),
          ("lockon", 3),
          ("off", 0),
          ("on", 1),
          ("reboot", 2),
          ("unknown", 6),
          ("unlock", 5))
    )


_SRPCAllOutletsCmd_Type.__name__ = "Integer32"
_SRPCAllOutletsCmd_Object = MibTableColumn
sRPCAllOutletsCmd = _SRPCAllOutletsCmd_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 12),
    _SRPCAllOutletsCmd_Type()
)
sRPCAllOutletsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCAllOutletsCmd.setStatus("mandatory")
_SRPCAllOutletsStatus_Type = DisplayString
_SRPCAllOutletsStatus_Object = MibTableColumn
sRPCAllOutletsStatus = _SRPCAllOutletsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 13),
    _SRPCAllOutletsStatus_Type()
)
sRPCAllOutletsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCAllOutletsStatus.setStatus("mandatory")
_SRPCCurrentAlarmThreshold_Type = Integer32
_SRPCCurrentAlarmThreshold_Object = MibTableColumn
sRPCCurrentAlarmThreshold = _SRPCCurrentAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 14),
    _SRPCCurrentAlarmThreshold_Type()
)
sRPCCurrentAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCCurrentAlarmThreshold.setStatus("mandatory")
_SRPCOverVoltageThreshold_Type = Integer32
_SRPCOverVoltageThreshold_Object = MibTableColumn
sRPCOverVoltageThreshold = _SRPCOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 15),
    _SRPCOverVoltageThreshold_Type()
)
sRPCOverVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOverVoltageThreshold.setStatus("mandatory")
_SRPCUnderVoltageThreshold_Type = Integer32
_SRPCUnderVoltageThreshold_Object = MibTableColumn
sRPCUnderVoltageThreshold = _SRPCUnderVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 16),
    _SRPCUnderVoltageThreshold_Type()
)
sRPCUnderVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCUnderVoltageThreshold.setStatus("mandatory")
_SRPCNumberOfOutlets_Type = Integer32
_SRPCNumberOfOutlets_Object = MibTableColumn
sRPCNumberOfOutlets = _SRPCNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 17),
    _SRPCNumberOfOutlets_Type()
)
sRPCNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCNumberOfOutlets.setStatus("mandatory")


class _SRPCCircuitBreaker_Type(Integer32):
    """Custom type sRPCCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SRPCCircuitBreaker_Type.__name__ = "Integer32"
_SRPCCircuitBreaker_Object = MibTableColumn
sRPCCircuitBreaker = _SRPCCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 18),
    _SRPCCircuitBreaker_Type()
)
sRPCCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCCircuitBreaker.setStatus("mandatory")
_SRPCOverTempThreshold_Type = Integer32
_SRPCOverTempThreshold_Object = MibTableColumn
sRPCOverTempThreshold = _SRPCOverTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 19),
    _SRPCOverTempThreshold_Type()
)
sRPCOverTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOverTempThreshold.setStatus("mandatory")
_SRPCUnitVA_Type = Integer32
_SRPCUnitVA_Object = MibTableColumn
sRPCUnitVA = _SRPCUnitVA_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 20),
    _SRPCUnitVA_Type()
)
sRPCUnitVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCUnitVA.setStatus("mandatory")
_SRPCNumberOfBreakers_Type = Integer32
_SRPCNumberOfBreakers_Object = MibTableColumn
sRPCNumberOfBreakers = _SRPCNumberOfBreakers_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 21),
    _SRPCNumberOfBreakers_Type()
)
sRPCNumberOfBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCNumberOfBreakers.setStatus("mandatory")
_SRPCLowCurrentThreshold_Type = Integer32
_SRPCLowCurrentThreshold_Object = MibTableColumn
sRPCLowCurrentThreshold = _SRPCLowCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 22),
    _SRPCLowCurrentThreshold_Type()
)
sRPCLowCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCLowCurrentThreshold.setStatus("mandatory")
_SRPCVoltageSource_Type = Integer32
_SRPCVoltageSource_Object = MibTableColumn
sRPCVoltageSource = _SRPCVoltageSource_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 23),
    _SRPCVoltageSource_Type()
)
sRPCVoltageSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCVoltageSource.setStatus("mandatory")
_SRPCSourceSwitchCount_Type = Integer32
_SRPCSourceSwitchCount_Object = MibTableColumn
sRPCSourceSwitchCount = _SRPCSourceSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 24),
    _SRPCSourceSwitchCount_Type()
)
sRPCSourceSwitchCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCSourceSwitchCount.setStatus("mandatory")
_SRPCNumberOfSensors_Type = Integer32
_SRPCNumberOfSensors_Object = MibTableColumn
sRPCNumberOfSensors = _SRPCNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 5, 1, 25),
    _SRPCNumberOfSensors_Type()
)
sRPCNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCNumberOfSensors.setStatus("mandatory")
_SBTAModulesRPCModPortOutletTable_Object = MibTable
sBTAModulesRPCModPortOutletTable = _SBTAModulesRPCModPortOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6)
)
if mibBuilder.loadTexts:
    sBTAModulesRPCModPortOutletTable.setStatus("mandatory")
_SBTAModulesRPCModPortOutletEntry_Object = MibTableRow
sBTAModulesRPCModPortOutletEntry = _SBTAModulesRPCModPortOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6, 1)
)
sBTAModulesRPCModPortOutletEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sRPCOutletModuleIndex"),
    (0, "Baytech-MIB-403-1", "sRPCOutletPortIndex"),
    (0, "Baytech-MIB-403-1", "sRPCOutletIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesRPCModPortOutletEntry.setStatus("mandatory")
_SRPCOutletModuleIndex_Type = Integer32
_SRPCOutletModuleIndex_Object = MibTableColumn
sRPCOutletModuleIndex = _SRPCOutletModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6, 1, 1),
    _SRPCOutletModuleIndex_Type()
)
sRPCOutletModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCOutletModuleIndex.setStatus("mandatory")
_SRPCOutletPortIndex_Type = Integer32
_SRPCOutletPortIndex_Object = MibTableColumn
sRPCOutletPortIndex = _SRPCOutletPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6, 1, 2),
    _SRPCOutletPortIndex_Type()
)
sRPCOutletPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCOutletPortIndex.setStatus("mandatory")
_SRPCOutletIndex_Type = Integer32
_SRPCOutletIndex_Object = MibTableColumn
sRPCOutletIndex = _SRPCOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6, 1, 3),
    _SRPCOutletIndex_Type()
)
sRPCOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCOutletIndex.setStatus("mandatory")


class _SRPCOutletState_Type(Integer32):
    """Custom type sRPCOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lockoff", 4),
          ("lockon", 3),
          ("off", 0),
          ("on", 1),
          ("reboot", 2),
          ("unknown", 6),
          ("unlock", 5))
    )


_SRPCOutletState_Type.__name__ = "Integer32"
_SRPCOutletState_Object = MibTableColumn
sRPCOutletState = _SRPCOutletState_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6, 1, 4),
    _SRPCOutletState_Type()
)
sRPCOutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOutletState.setStatus("mandatory")
_SRPCOutletName_Type = DisplayString
_SRPCOutletName_Object = MibTableColumn
sRPCOutletName = _SRPCOutletName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 6, 1, 5),
    _SRPCOutletName_Type()
)
sRPCOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOutletName.setStatus("mandatory")
_SBTAModulesRPCModPortGroupCmd_Type = DisplayString
_SBTAModulesRPCModPortGroupCmd_Object = MibScalar
sBTAModulesRPCModPortGroupCmd = _SBTAModulesRPCModPortGroupCmd_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 7),
    _SBTAModulesRPCModPortGroupCmd_Type()
)
sBTAModulesRPCModPortGroupCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCModPortGroupCmd.setStatus("mandatory")
_SBTAModulesRPCCurrentGroupsCurrentTable_Object = MibTable
sBTAModulesRPCCurrentGroupsCurrentTable = _SBTAModulesRPCCurrentGroupsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8)
)
if mibBuilder.loadTexts:
    sBTAModulesRPCCurrentGroupsCurrentTable.setStatus("mandatory")
_SBTAModulesRPCCurrentGroupsCurrentEntry_Object = MibTableRow
sBTAModulesRPCCurrentGroupsCurrentEntry = _SBTAModulesRPCCurrentGroupsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8, 1)
)
sBTAModulesRPCCurrentGroupsCurrentEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "groupCurrentIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesRPCCurrentGroupsCurrentEntry.setStatus("mandatory")
_GroupCurrentIndex_Type = Integer32
_GroupCurrentIndex_Object = MibTableColumn
groupCurrentIndex = _GroupCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8, 1, 1),
    _GroupCurrentIndex_Type()
)
groupCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrentIndex.setStatus("mandatory")
_GroupCurrent_Type = Integer32
_GroupCurrent_Object = MibTableColumn
groupCurrent = _GroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8, 1, 2),
    _GroupCurrent_Type()
)
groupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrent.setStatus("mandatory")
_RpcGroup_Type = DisplayString
_RpcGroup_Object = MibTableColumn
rpcGroup = _RpcGroup_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8, 1, 3),
    _RpcGroup_Type()
)
rpcGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcGroup.setStatus("mandatory")
_WarningThreshold_Type = Integer32
_WarningThreshold_Object = MibTableColumn
warningThreshold = _WarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8, 1, 4),
    _WarningThreshold_Type()
)
warningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningThreshold.setStatus("mandatory")
_EmergencyThreshold_Type = Integer32
_EmergencyThreshold_Object = MibTableColumn
emergencyThreshold = _EmergencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 8, 1, 5),
    _EmergencyThreshold_Type()
)
emergencyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emergencyThreshold.setStatus("mandatory")
_SBTAModulesRPCBreakersTable_Object = MibTable
sBTAModulesRPCBreakersTable = _SBTAModulesRPCBreakersTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9)
)
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersTable.setStatus("mandatory")
_SBTAModulesRPCBreakersEntry_Object = MibTableRow
sBTAModulesRPCBreakersEntry = _SBTAModulesRPCBreakersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1)
)
sBTAModulesRPCBreakersEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sBTAModulesRPCBreakersModulesIndex"),
    (0, "Baytech-MIB-403-1", "sBTAModulesRPCBreakersBreakersIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersEntry.setStatus("mandatory")
_SBTAModulesRPCBreakersModulesIndex_Type = Integer32
_SBTAModulesRPCBreakersModulesIndex_Object = MibTableColumn
sBTAModulesRPCBreakersModulesIndex = _SBTAModulesRPCBreakersModulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 1),
    _SBTAModulesRPCBreakersModulesIndex_Type()
)
sBTAModulesRPCBreakersModulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersModulesIndex.setStatus("mandatory")
_SBTAModulesRPCBreakersBreakersIndex_Type = Integer32
_SBTAModulesRPCBreakersBreakersIndex_Object = MibTableColumn
sBTAModulesRPCBreakersBreakersIndex = _SBTAModulesRPCBreakersBreakersIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 2),
    _SBTAModulesRPCBreakersBreakersIndex_Type()
)
sBTAModulesRPCBreakersBreakersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersBreakersIndex.setStatus("mandatory")


class _SBTAModulesRPCBreakersCircuitBreaker_Type(Integer32):
    """Custom type sBTAModulesRPCBreakersCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SBTAModulesRPCBreakersCircuitBreaker_Type.__name__ = "Integer32"
_SBTAModulesRPCBreakersCircuitBreaker_Object = MibTableColumn
sBTAModulesRPCBreakersCircuitBreaker = _SBTAModulesRPCBreakersCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 3),
    _SBTAModulesRPCBreakersCircuitBreaker_Type()
)
sBTAModulesRPCBreakersCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersCircuitBreaker.setStatus("mandatory")
_SBTAModulesRPCBreakersCurrent_Type = Integer32
_SBTAModulesRPCBreakersCurrent_Object = MibTableColumn
sBTAModulesRPCBreakersCurrent = _SBTAModulesRPCBreakersCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 4),
    _SBTAModulesRPCBreakersCurrent_Type()
)
sBTAModulesRPCBreakersCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersCurrent.setStatus("mandatory")
_SBTAModulesRPCBreakersMaxCurrent_Type = Integer32
_SBTAModulesRPCBreakersMaxCurrent_Object = MibTableColumn
sBTAModulesRPCBreakersMaxCurrent = _SBTAModulesRPCBreakersMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 5),
    _SBTAModulesRPCBreakersMaxCurrent_Type()
)
sBTAModulesRPCBreakersMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersMaxCurrent.setStatus("mandatory")
_SBTAModulesRPCBreakersVoltage_Type = Integer32
_SBTAModulesRPCBreakersVoltage_Object = MibTableColumn
sBTAModulesRPCBreakersVoltage = _SBTAModulesRPCBreakersVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 6),
    _SBTAModulesRPCBreakersVoltage_Type()
)
sBTAModulesRPCBreakersVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersVoltage.setStatus("mandatory")
_SBTAModulesRPCBreakersPower_Type = Integer32
_SBTAModulesRPCBreakersPower_Object = MibTableColumn
sBTAModulesRPCBreakersPower = _SBTAModulesRPCBreakersPower_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 7),
    _SBTAModulesRPCBreakersPower_Type()
)
sBTAModulesRPCBreakersPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersPower.setStatus("mandatory")
_SBTAModulesRPCBreakersVA_Type = Integer32
_SBTAModulesRPCBreakersVA_Object = MibTableColumn
sBTAModulesRPCBreakersVA = _SBTAModulesRPCBreakersVA_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 8),
    _SBTAModulesRPCBreakersVA_Type()
)
sBTAModulesRPCBreakersVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersVA.setStatus("mandatory")
_SBTAModulesRPCBreakersCurrentAlarmThreshold_Type = Integer32
_SBTAModulesRPCBreakersCurrentAlarmThreshold_Object = MibTableColumn
sBTAModulesRPCBreakersCurrentAlarmThreshold = _SBTAModulesRPCBreakersCurrentAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 9, 1, 9),
    _SBTAModulesRPCBreakersCurrentAlarmThreshold_Type()
)
sBTAModulesRPCBreakersCurrentAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesRPCBreakersCurrentAlarmThreshold.setStatus("mandatory")
_SRPCModPortBreakersTable_Object = MibTable
sRPCModPortBreakersTable = _SRPCModPortBreakersTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10)
)
if mibBuilder.loadTexts:
    sRPCModPortBreakersTable.setStatus("mandatory")
_SRPCModPortBreakersEntry_Object = MibTableRow
sRPCModPortBreakersEntry = _SRPCModPortBreakersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1)
)
sRPCModPortBreakersEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sRPCBreakersModIndex"),
    (0, "Baytech-MIB-403-1", "sRPCBreakersPortIndex"),
    (0, "Baytech-MIB-403-1", "sRPCBreakersBreakersIndex"),
)
if mibBuilder.loadTexts:
    sRPCModPortBreakersEntry.setStatus("mandatory")
_SRPCBreakersModIndex_Type = Integer32
_SRPCBreakersModIndex_Object = MibTableColumn
sRPCBreakersModIndex = _SRPCBreakersModIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 1),
    _SRPCBreakersModIndex_Type()
)
sRPCBreakersModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersModIndex.setStatus("mandatory")
_SRPCBreakersPortIndex_Type = Integer32
_SRPCBreakersPortIndex_Object = MibTableColumn
sRPCBreakersPortIndex = _SRPCBreakersPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 2),
    _SRPCBreakersPortIndex_Type()
)
sRPCBreakersPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersPortIndex.setStatus("mandatory")
_SRPCBreakersBreakersIndex_Type = Integer32
_SRPCBreakersBreakersIndex_Object = MibTableColumn
sRPCBreakersBreakersIndex = _SRPCBreakersBreakersIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 3),
    _SRPCBreakersBreakersIndex_Type()
)
sRPCBreakersBreakersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersBreakersIndex.setStatus("mandatory")


class _SRPCBreakersCircuitBreaker_Type(Integer32):
    """Custom type sRPCBreakersCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SRPCBreakersCircuitBreaker_Type.__name__ = "Integer32"
_SRPCBreakersCircuitBreaker_Object = MibTableColumn
sRPCBreakersCircuitBreaker = _SRPCBreakersCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 4),
    _SRPCBreakersCircuitBreaker_Type()
)
sRPCBreakersCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersCircuitBreaker.setStatus("mandatory")
_SRPCBreakersCurrent_Type = Integer32
_SRPCBreakersCurrent_Object = MibTableColumn
sRPCBreakersCurrent = _SRPCBreakersCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 5),
    _SRPCBreakersCurrent_Type()
)
sRPCBreakersCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersCurrent.setStatus("mandatory")
_SRPCBreakersMaxCurrent_Type = Integer32
_SRPCBreakersMaxCurrent_Object = MibTableColumn
sRPCBreakersMaxCurrent = _SRPCBreakersMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 6),
    _SRPCBreakersMaxCurrent_Type()
)
sRPCBreakersMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersMaxCurrent.setStatus("mandatory")
_SRPCBreakersVoltage_Type = Integer32
_SRPCBreakersVoltage_Object = MibTableColumn
sRPCBreakersVoltage = _SRPCBreakersVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 7),
    _SRPCBreakersVoltage_Type()
)
sRPCBreakersVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersVoltage.setStatus("mandatory")
_SRPCBreakersPower_Type = Integer32
_SRPCBreakersPower_Object = MibTableColumn
sRPCBreakersPower = _SRPCBreakersPower_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 8),
    _SRPCBreakersPower_Type()
)
sRPCBreakersPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersPower.setStatus("mandatory")
_SRPCBreakersVA_Type = Integer32
_SRPCBreakersVA_Object = MibTableColumn
sRPCBreakersVA = _SRPCBreakersVA_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 9),
    _SRPCBreakersVA_Type()
)
sRPCBreakersVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCBreakersVA.setStatus("mandatory")
_SRPCBreakersCurrentAlarmThreshold_Type = Integer32
_SRPCBreakersCurrentAlarmThreshold_Object = MibTableColumn
sRPCBreakersCurrentAlarmThreshold = _SRPCBreakersCurrentAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 10, 1, 10),
    _SRPCBreakersCurrentAlarmThreshold_Type()
)
sRPCBreakersCurrentAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCBreakersCurrentAlarmThreshold.setStatus("mandatory")
_SRPCOutletGroupTable_Object = MibTable
sRPCOutletGroupTable = _SRPCOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 11)
)
if mibBuilder.loadTexts:
    sRPCOutletGroupTable.setStatus("mandatory")
_SRPCOutletGroupEntry_Object = MibTableRow
sRPCOutletGroupEntry = _SRPCOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 11, 1)
)
sRPCOutletGroupEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sRPCOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    sRPCOutletGroupEntry.setStatus("mandatory")
_SRPCOutletGroupIndex_Type = Integer32
_SRPCOutletGroupIndex_Object = MibTableColumn
sRPCOutletGroupIndex = _SRPCOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 11, 1, 1),
    _SRPCOutletGroupIndex_Type()
)
sRPCOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCOutletGroupIndex.setStatus("mandatory")
_SRPCOutletGroupName_Type = DisplayString
_SRPCOutletGroupName_Object = MibTableColumn
sRPCOutletGroupName = _SRPCOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 11, 1, 2),
    _SRPCOutletGroupName_Type()
)
sRPCOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOutletGroupName.setStatus("mandatory")
_SRPCOutletGroupOutlets_Type = DisplayString
_SRPCOutletGroupOutlets_Object = MibTableColumn
sRPCOutletGroupOutlets = _SRPCOutletGroupOutlets_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 11, 1, 3),
    _SRPCOutletGroupOutlets_Type()
)
sRPCOutletGroupOutlets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOutletGroupOutlets.setStatus("mandatory")


class _SRPCOutletGroupCmd_Type(Integer32):
    """Custom type sRPCOutletGroupCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lockoff", 4),
          ("lockon", 3),
          ("off", 0),
          ("on", 1),
          ("reboot", 2),
          ("unknown", 6),
          ("unlock", 5))
    )


_SRPCOutletGroupCmd_Type.__name__ = "Integer32"
_SRPCOutletGroupCmd_Object = MibTableColumn
sRPCOutletGroupCmd = _SRPCOutletGroupCmd_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 5, 11, 1, 4),
    _SRPCOutletGroupCmd_Type()
)
sRPCOutletGroupCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCOutletGroupCmd.setStatus("mandatory")
_SBTAModulesSerial_ObjectIdentity = ObjectIdentity
sBTAModulesSerial = _SBTAModulesSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 6)
)
_SBTAModulesModem_ObjectIdentity = ObjectIdentity
sBTAModulesModem = _SBTAModulesModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 3, 7)
)
_SBTAControl_ObjectIdentity = ObjectIdentity
sBTAControl = _SBTAControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4)
)


class _SBTAControlResetUnit_Type(Integer32):
    """Custom type sBTAControlResetUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 0),
          ("reset", 1))
    )


_SBTAControlResetUnit_Type.__name__ = "Integer32"
_SBTAControlResetUnit_Object = MibScalar
sBTAControlResetUnit = _SBTAControlResetUnit_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 1),
    _SBTAControlResetUnit_Type()
)
sBTAControlResetUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAControlResetUnit.setStatus("mandatory")


class _SBTAControlResetModules_Type(Integer32):
    """Custom type sBTAControlResetModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 0),
          ("reset", 1))
    )


_SBTAControlResetModules_Type.__name__ = "Integer32"
_SBTAControlResetModules_Object = MibScalar
sBTAControlResetModules = _SBTAControlResetModules_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 2),
    _SBTAControlResetModules_Type()
)
sBTAControlResetModules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAControlResetModules.setStatus("mandatory")
_SBTAControlNumOfLoggedUsers_Type = Integer32
_SBTAControlNumOfLoggedUsers_Object = MibScalar
sBTAControlNumOfLoggedUsers = _SBTAControlNumOfLoggedUsers_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 3),
    _SBTAControlNumOfLoggedUsers_Type()
)
sBTAControlNumOfLoggedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlNumOfLoggedUsers.setStatus("mandatory")
_SBTAControlUserTable_Object = MibTable
sBTAControlUserTable = _SBTAControlUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4)
)
if mibBuilder.loadTexts:
    sBTAControlUserTable.setStatus("mandatory")
_SBTAControlUserEntry_Object = MibTableRow
sBTAControlUserEntry = _SBTAControlUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1)
)
sBTAControlUserEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sBTAControlUserIndex"),
)
if mibBuilder.loadTexts:
    sBTAControlUserEntry.setStatus("mandatory")
_SBTAControlUserIndex_Type = Integer32
_SBTAControlUserIndex_Object = MibTableColumn
sBTAControlUserIndex = _SBTAControlUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 1),
    _SBTAControlUserIndex_Type()
)
sBTAControlUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlUserIndex.setStatus("mandatory")
_SBTAControlUserName_Type = DisplayString
_SBTAControlUserName_Object = MibTableColumn
sBTAControlUserName = _SBTAControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 2),
    _SBTAControlUserName_Type()
)
sBTAControlUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlUserName.setStatus("mandatory")
_SBTAControlUserAddress_Type = IpAddress
_SBTAControlUserAddress_Object = MibTableColumn
sBTAControlUserAddress = _SBTAControlUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 3),
    _SBTAControlUserAddress_Type()
)
sBTAControlUserAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlUserAddress.setStatus("mandatory")


class _SBTAControlUserConnection_Type(Integer32):
    """Custom type sBTAControlUserConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("serialport", 0),
          ("ssh", 2),
          ("telnet", 1),
          ("unknown", 4))
    )


_SBTAControlUserConnection_Type.__name__ = "Integer32"
_SBTAControlUserConnection_Object = MibTableColumn
sBTAControlUserConnection = _SBTAControlUserConnection_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 4),
    _SBTAControlUserConnection_Type()
)
sBTAControlUserConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlUserConnection.setStatus("mandatory")
_SBTAControlUserConnModule_Type = Integer32
_SBTAControlUserConnModule_Object = MibTableColumn
sBTAControlUserConnModule = _SBTAControlUserConnModule_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 5),
    _SBTAControlUserConnModule_Type()
)
sBTAControlUserConnModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlUserConnModule.setStatus("mandatory")
_SBTAControlUserConnPort_Type = Integer32
_SBTAControlUserConnPort_Object = MibTableColumn
sBTAControlUserConnPort = _SBTAControlUserConnPort_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 6),
    _SBTAControlUserConnPort_Type()
)
sBTAControlUserConnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAControlUserConnPort.setStatus("mandatory")


class _SBTAControlUserTerminateUser_Type(Integer32):
    """Custom type sBTAControlUserTerminateUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("terminate", 1)
    )


_SBTAControlUserTerminateUser_Type.__name__ = "Integer32"
_SBTAControlUserTerminateUser_Object = MibTableColumn
sBTAControlUserTerminateUser = _SBTAControlUserTerminateUser_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 4, 4, 1, 7),
    _SBTAControlUserTerminateUser_Type()
)
sBTAControlUserTerminateUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAControlUserTerminateUser.setStatus("mandatory")
_SBTAFileTransfer_ObjectIdentity = ObjectIdentity
sBTAFileTransfer = _SBTAFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 5)
)


class _SBTAFileTransferEnableUpgradeFTPFileTransfer_Type(Integer32):
    """Custom type sBTAFileTransferEnableUpgradeFTPFileTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enableUpgradeFileTransferDownloadViaFTP", 1)
    )


_SBTAFileTransferEnableUpgradeFTPFileTransfer_Type.__name__ = "Integer32"
_SBTAFileTransferEnableUpgradeFTPFileTransfer_Object = MibScalar
sBTAFileTransferEnableUpgradeFTPFileTransfer = _SBTAFileTransferEnableUpgradeFTPFileTransfer_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 5, 1),
    _SBTAFileTransferEnableUpgradeFTPFileTransfer_Type()
)
sBTAFileTransferEnableUpgradeFTPFileTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAFileTransferEnableUpgradeFTPFileTransfer.setStatus("mandatory")
_SBTAEnvironmental_ObjectIdentity = ObjectIdentity
sBTAEnvironmental = _SBTAEnvironmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6)
)
_SBTAModulesEnvironmentalObjectsTable_Object = MibTable
sBTAModulesEnvironmentalObjectsTable = _SBTAModulesEnvironmentalObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalObjectsTable.setStatus("mandatory")
_SBTAModulesEnvironmentalObjectsEntry_Object = MibTableRow
sBTAModulesEnvironmentalObjectsEntry = _SBTAModulesEnvironmentalObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1)
)
sBTAModulesEnvironmentalObjectsEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sBTAModulesEnvironmentalModulesIndex"),
    (0, "Baytech-MIB-403-1", "sBTAModulesEnvironmentalSensorsIndex"),
)
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalObjectsEntry.setStatus("mandatory")
_SBTAModulesEnvironmentalModulesIndex_Type = Integer32
_SBTAModulesEnvironmentalModulesIndex_Object = MibTableColumn
sBTAModulesEnvironmentalModulesIndex = _SBTAModulesEnvironmentalModulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 1),
    _SBTAModulesEnvironmentalModulesIndex_Type()
)
sBTAModulesEnvironmentalModulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalModulesIndex.setStatus("mandatory")
_SBTAModulesEnvironmentalSensorsIndex_Type = Integer32
_SBTAModulesEnvironmentalSensorsIndex_Object = MibTableColumn
sBTAModulesEnvironmentalSensorsIndex = _SBTAModulesEnvironmentalSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 2),
    _SBTAModulesEnvironmentalSensorsIndex_Type()
)
sBTAModulesEnvironmentalSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalSensorsIndex.setStatus("mandatory")
_SBTAModulesEnvironmentalType_Type = Integer32
_SBTAModulesEnvironmentalType_Object = MibTableColumn
sBTAModulesEnvironmentalType = _SBTAModulesEnvironmentalType_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 3),
    _SBTAModulesEnvironmentalType_Type()
)
sBTAModulesEnvironmentalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalType.setStatus("mandatory")
_SBTAModulesEnvironmentalName_Type = DisplayString
_SBTAModulesEnvironmentalName_Object = MibTableColumn
sBTAModulesEnvironmentalName = _SBTAModulesEnvironmentalName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 4),
    _SBTAModulesEnvironmentalName_Type()
)
sBTAModulesEnvironmentalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalName.setStatus("mandatory")
_SBTAModulesEnvironmentalMeasurement_Type = Integer32
_SBTAModulesEnvironmentalMeasurement_Object = MibTableColumn
sBTAModulesEnvironmentalMeasurement = _SBTAModulesEnvironmentalMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 5),
    _SBTAModulesEnvironmentalMeasurement_Type()
)
sBTAModulesEnvironmentalMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalMeasurement.setStatus("mandatory")
_SBTAModulesEnvironmentalHiThreshold_Type = Integer32
_SBTAModulesEnvironmentalHiThreshold_Object = MibTableColumn
sBTAModulesEnvironmentalHiThreshold = _SBTAModulesEnvironmentalHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 6),
    _SBTAModulesEnvironmentalHiThreshold_Type()
)
sBTAModulesEnvironmentalHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalHiThreshold.setStatus("mandatory")
_SBTAModulesEnvironmentalLoThreshold_Type = Integer32
_SBTAModulesEnvironmentalLoThreshold_Object = MibTableColumn
sBTAModulesEnvironmentalLoThreshold = _SBTAModulesEnvironmentalLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 7),
    _SBTAModulesEnvironmentalLoThreshold_Type()
)
sBTAModulesEnvironmentalLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalLoThreshold.setStatus("mandatory")
_SBTAModulesEnvironmentalMax_Type = Integer32
_SBTAModulesEnvironmentalMax_Object = MibTableColumn
sBTAModulesEnvironmentalMax = _SBTAModulesEnvironmentalMax_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 8),
    _SBTAModulesEnvironmentalMax_Type()
)
sBTAModulesEnvironmentalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalMax.setStatus("mandatory")
_SBTAModulesEnvironmentalMin_Type = Integer32
_SBTAModulesEnvironmentalMin_Object = MibTableColumn
sBTAModulesEnvironmentalMin = _SBTAModulesEnvironmentalMin_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 9),
    _SBTAModulesEnvironmentalMin_Type()
)
sBTAModulesEnvironmentalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalMin.setStatus("mandatory")
_SBTAModulesEnvironmentalHiThresholdEn_Type = Integer32
_SBTAModulesEnvironmentalHiThresholdEn_Object = MibTableColumn
sBTAModulesEnvironmentalHiThresholdEn = _SBTAModulesEnvironmentalHiThresholdEn_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 10),
    _SBTAModulesEnvironmentalHiThresholdEn_Type()
)
sBTAModulesEnvironmentalHiThresholdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalHiThresholdEn.setStatus("mandatory")
_SBTAModulesEnvironmentalLoThresholdEn_Type = Integer32
_SBTAModulesEnvironmentalLoThresholdEn_Object = MibTableColumn
sBTAModulesEnvironmentalLoThresholdEn = _SBTAModulesEnvironmentalLoThresholdEn_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 11),
    _SBTAModulesEnvironmentalLoThresholdEn_Type()
)
sBTAModulesEnvironmentalLoThresholdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalLoThresholdEn.setStatus("mandatory")
_SBTAModulesEnvironmentalStateTrapEn_Type = Integer32
_SBTAModulesEnvironmentalStateTrapEn_Object = MibTableColumn
sBTAModulesEnvironmentalStateTrapEn = _SBTAModulesEnvironmentalStateTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 1, 1, 12),
    _SBTAModulesEnvironmentalStateTrapEn_Type()
)
sBTAModulesEnvironmentalStateTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAModulesEnvironmentalStateTrapEn.setStatus("mandatory")
_SRPCEnvironmentalObjectsTable_Object = MibTable
sRPCEnvironmentalObjectsTable = _SRPCEnvironmentalObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sRPCEnvironmentalObjectsTable.setStatus("mandatory")
_SRPCEnvironmentalObjectsEntry_Object = MibTableRow
sRPCEnvironmentalObjectsEntry = _SRPCEnvironmentalObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1)
)
sRPCEnvironmentalObjectsEntry.setIndexNames(
    (0, "Baytech-MIB-403-1", "sBTAEnvironmentalModuleIndex"),
    (0, "Baytech-MIB-403-1", "sBTAEnvironmentalPortIndex"),
    (0, "Baytech-MIB-403-1", "sBTAEnvironmentalSensorsIndex"),
)
if mibBuilder.loadTexts:
    sRPCEnvironmentalObjectsEntry.setStatus("mandatory")
_SRPCEnvironmentalModuleIndex_Type = Integer32
_SRPCEnvironmentalModuleIndex_Object = MibTableColumn
sRPCEnvironmentalModuleIndex = _SRPCEnvironmentalModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 1),
    _SRPCEnvironmentalModuleIndex_Type()
)
sRPCEnvironmentalModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCEnvironmentalModuleIndex.setStatus("mandatory")
_SRPCEnvironmentalPortIndex_Type = Integer32
_SRPCEnvironmentalPortIndex_Object = MibTableColumn
sRPCEnvironmentalPortIndex = _SRPCEnvironmentalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 2),
    _SRPCEnvironmentalPortIndex_Type()
)
sRPCEnvironmentalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCEnvironmentalPortIndex.setStatus("mandatory")
_SRPCEnvironmentalSensorsIndex_Type = Integer32
_SRPCEnvironmentalSensorsIndex_Object = MibTableColumn
sRPCEnvironmentalSensorsIndex = _SRPCEnvironmentalSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 3),
    _SRPCEnvironmentalSensorsIndex_Type()
)
sRPCEnvironmentalSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCEnvironmentalSensorsIndex.setStatus("mandatory")
_SRPCEnvironmentalType_Type = Integer32
_SRPCEnvironmentalType_Object = MibTableColumn
sRPCEnvironmentalType = _SRPCEnvironmentalType_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 4),
    _SRPCEnvironmentalType_Type()
)
sRPCEnvironmentalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCEnvironmentalType.setStatus("mandatory")
_SRPCEnvironmentalName_Type = DisplayString
_SRPCEnvironmentalName_Object = MibTableColumn
sRPCEnvironmentalName = _SRPCEnvironmentalName_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 5),
    _SRPCEnvironmentalName_Type()
)
sRPCEnvironmentalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalName.setStatus("mandatory")
_SRPCEnvironmentalMeasurement_Type = Integer32
_SRPCEnvironmentalMeasurement_Object = MibTableColumn
sRPCEnvironmentalMeasurement = _SRPCEnvironmentalMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 6),
    _SRPCEnvironmentalMeasurement_Type()
)
sRPCEnvironmentalMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sRPCEnvironmentalMeasurement.setStatus("mandatory")
_SRPCEnvironmentalHiThreshold_Type = Integer32
_SRPCEnvironmentalHiThreshold_Object = MibTableColumn
sRPCEnvironmentalHiThreshold = _SRPCEnvironmentalHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 7),
    _SRPCEnvironmentalHiThreshold_Type()
)
sRPCEnvironmentalHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalHiThreshold.setStatus("mandatory")
_SRPCEnvironmentalLoThreshold_Type = Integer32
_SRPCEnvironmentalLoThreshold_Object = MibTableColumn
sRPCEnvironmentalLoThreshold = _SRPCEnvironmentalLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 8),
    _SRPCEnvironmentalLoThreshold_Type()
)
sRPCEnvironmentalLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalLoThreshold.setStatus("mandatory")
_SRPCEnvironmentalMax_Type = Integer32
_SRPCEnvironmentalMax_Object = MibTableColumn
sRPCEnvironmentalMax = _SRPCEnvironmentalMax_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 9),
    _SRPCEnvironmentalMax_Type()
)
sRPCEnvironmentalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalMax.setStatus("mandatory")
_SRPCEnvironmentalMin_Type = Integer32
_SRPCEnvironmentalMin_Object = MibTableColumn
sRPCEnvironmentalMin = _SRPCEnvironmentalMin_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 10),
    _SRPCEnvironmentalMin_Type()
)
sRPCEnvironmentalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalMin.setStatus("mandatory")
_SRPCEnvironmentalHiThresholdEn_Type = Integer32
_SRPCEnvironmentalHiThresholdEn_Object = MibTableColumn
sRPCEnvironmentalHiThresholdEn = _SRPCEnvironmentalHiThresholdEn_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 11),
    _SRPCEnvironmentalHiThresholdEn_Type()
)
sRPCEnvironmentalHiThresholdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalHiThresholdEn.setStatus("mandatory")
_SRPCEnvironmentalLoThresholdEn_Type = Integer32
_SRPCEnvironmentalLoThresholdEn_Object = MibTableColumn
sRPCEnvironmentalLoThresholdEn = _SRPCEnvironmentalLoThresholdEn_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 12),
    _SRPCEnvironmentalLoThresholdEn_Type()
)
sRPCEnvironmentalLoThresholdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalLoThresholdEn.setStatus("mandatory")
_SRPCEnvironmentalStateTrapEn_Type = Integer32
_SRPCEnvironmentalStateTrapEn_Object = MibTableColumn
sRPCEnvironmentalStateTrapEn = _SRPCEnvironmentalStateTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 2, 1, 13),
    _SRPCEnvironmentalStateTrapEn_Type()
)
sRPCEnvironmentalStateTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sRPCEnvironmentalStateTrapEn.setStatus("mandatory")
_SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Type = Integer32
_SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Object = MibScalar
sBTAEnvironmentalAllTemperatureSensorsHiThreshold = _SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 3),
    _SBTAEnvironmentalAllTemperatureSensorsHiThreshold_Type()
)
sBTAEnvironmentalAllTemperatureSensorsHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllTemperatureSensorsHiThreshold.setStatus("mandatory")
_SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Type = Integer32
_SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Object = MibScalar
sBTAEnvironmentalAllTemperatureSensorsLoThreshold = _SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 4),
    _SBTAEnvironmentalAllTemperatureSensorsLoThreshold_Type()
)
sBTAEnvironmentalAllTemperatureSensorsLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllTemperatureSensorsLoThreshold.setStatus("mandatory")
_SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Type = Integer32
_SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Object = MibScalar
sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable = _SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 5),
    _SBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable_Type()
)
sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable.setStatus("mandatory")
_SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Type = Integer32
_SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Object = MibScalar
sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable = _SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 6),
    _SBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable_Type()
)
sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable.setStatus("mandatory")
_SBTAEnvironmentalAllSensorsStateTrapEnable_Type = Integer32
_SBTAEnvironmentalAllSensorsStateTrapEnable_Object = MibScalar
sBTAEnvironmentalAllSensorsStateTrapEnable = _SBTAEnvironmentalAllSensorsStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 7),
    _SBTAEnvironmentalAllSensorsStateTrapEnable_Type()
)
sBTAEnvironmentalAllSensorsStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllSensorsStateTrapEnable.setStatus("mandatory")
_SBTAEnvironmentalAllHumiditySensorsHiThreshold_Type = Integer32
_SBTAEnvironmentalAllHumiditySensorsHiThreshold_Object = MibScalar
sBTAEnvironmentalAllHumiditySensorsHiThreshold = _SBTAEnvironmentalAllHumiditySensorsHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 8),
    _SBTAEnvironmentalAllHumiditySensorsHiThreshold_Type()
)
sBTAEnvironmentalAllHumiditySensorsHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllHumiditySensorsHiThreshold.setStatus("mandatory")
_SBTAEnvironmentalAllHumiditySensorsLoThreshold_Type = Integer32
_SBTAEnvironmentalAllHumiditySensorsLoThreshold_Object = MibScalar
sBTAEnvironmentalAllHumiditySensorsLoThreshold = _SBTAEnvironmentalAllHumiditySensorsLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 9),
    _SBTAEnvironmentalAllHumiditySensorsLoThreshold_Type()
)
sBTAEnvironmentalAllHumiditySensorsLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllHumiditySensorsLoThreshold.setStatus("mandatory")
_SBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable_Type = Integer32
_SBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable_Object = MibScalar
sBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable = _SBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 10),
    _SBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable_Type()
)
sBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable.setStatus("mandatory")
_SBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable_Type = Integer32
_SBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable_Object = MibScalar
sBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable = _SBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 11),
    _SBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable_Type()
)
sBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable.setStatus("mandatory")
_SBTAEnvironmentalAllAirflowSensorsHiThreshold_Type = Integer32
_SBTAEnvironmentalAllAirflowSensorsHiThreshold_Object = MibScalar
sBTAEnvironmentalAllAirflowSensorsHiThreshold = _SBTAEnvironmentalAllAirflowSensorsHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 12),
    _SBTAEnvironmentalAllAirflowSensorsHiThreshold_Type()
)
sBTAEnvironmentalAllAirflowSensorsHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllAirflowSensorsHiThreshold.setStatus("mandatory")
_SBTAEnvironmentalAllAirflowSensorsLoThreshold_Type = Integer32
_SBTAEnvironmentalAllAirflowSensorsLoThreshold_Object = MibScalar
sBTAEnvironmentalAllAirflowSensorsLoThreshold = _SBTAEnvironmentalAllAirflowSensorsLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 13),
    _SBTAEnvironmentalAllAirflowSensorsLoThreshold_Type()
)
sBTAEnvironmentalAllAirflowSensorsLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllAirflowSensorsLoThreshold.setStatus("mandatory")
_SBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable_Type = Integer32
_SBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable_Object = MibScalar
sBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable = _SBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 14),
    _SBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable_Type()
)
sBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable.setStatus("mandatory")
_SBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable_Type = Integer32
_SBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable_Object = MibScalar
sBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable = _SBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4779, 1, 6, 15),
    _SBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable_Type()
)
sBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable.setStatus("mandatory")
_Mtrapargs_ObjectIdentity = ObjectIdentity
mtrapargs = _Mtrapargs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4779, 3)
)
_MtrapargsInteger_Type = Integer32
_MtrapargsInteger_Object = MibScalar
mtrapargsInteger = _MtrapargsInteger_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 1),
    _MtrapargsInteger_Type()
)
mtrapargsInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapargsInteger.setStatus("mandatory")
_MtrapargsIpAddress_Type = IpAddress
_MtrapargsIpAddress_Object = MibScalar
mtrapargsIpAddress = _MtrapargsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 2),
    _MtrapargsIpAddress_Type()
)
mtrapargsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapargsIpAddress.setStatus("mandatory")
_MtrapargsString_Type = DisplayString
_MtrapargsString_Object = MibScalar
mtrapargsString = _MtrapargsString_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 3),
    _MtrapargsString_Type()
)
mtrapargsString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapargsString.setStatus("mandatory")
_MtrapargsGauge_Type = Gauge32
_MtrapargsGauge_Object = MibScalar
mtrapargsGauge = _MtrapargsGauge_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 4),
    _MtrapargsGauge_Type()
)
mtrapargsGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapargsGauge.setStatus("mandatory")
_MtrapargsTimeTicks_Type = TimeTicks
_MtrapargsTimeTicks_Object = MibScalar
mtrapargsTimeTicks = _MtrapargsTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 5),
    _MtrapargsTimeTicks_Type()
)
mtrapargsTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtrapargsTimeTicks.setStatus("mandatory")
_SBTAModuleIndex_Type = Integer32
_SBTAModuleIndex_Object = MibScalar
sBTAModuleIndex = _SBTAModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 6),
    _SBTAModuleIndex_Type()
)
sBTAModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAModuleIndex.setStatus("mandatory")
_SBTAOutletIndex_Type = Integer32
_SBTAOutletIndex_Object = MibScalar
sBTAOutletIndex = _SBTAOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 7),
    _SBTAOutletIndex_Type()
)
sBTAOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAOutletIndex.setStatus("mandatory")
_SBTAPortIndex_Type = Integer32
_SBTAPortIndex_Object = MibScalar
sBTAPortIndex = _SBTAPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 8),
    _SBTAPortIndex_Type()
)
sBTAPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTAPortIndex.setStatus("mandatory")
_SBTAVoltageSource_Type = Integer32
_SBTAVoltageSource_Object = MibScalar
sBTAVoltageSource = _SBTAVoltageSource_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 9),
    _SBTAVoltageSource_Type()
)
sBTAVoltageSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sBTAVoltageSource.setStatus("mandatory")
_SBTASourceSwitchCount_Type = Integer32
_SBTASourceSwitchCount_Object = MibScalar
sBTASourceSwitchCount = _SBTASourceSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 10),
    _SBTASourceSwitchCount_Type()
)
sBTASourceSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTASourceSwitchCount.setStatus("mandatory")
_SBTASensorIndex_Type = Integer32
_SBTASensorIndex_Object = MibScalar
sBTASensorIndex = _SBTASensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 11),
    _SBTASensorIndex_Type()
)
sBTASensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTASensorIndex.setStatus("mandatory")
_SBTABreakerIndex_Type = Integer32
_SBTABreakerIndex_Object = MibScalar
sBTABreakerIndex = _SBTABreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4779, 3, 12),
    _SBTABreakerIndex_Type()
)
sBTABreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sBTABreakerIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects

communicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 1)
)
communicationLost.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsTimeTicks")
)
if mibBuilder.loadTexts:
    communicationLost.setStatus(
        ""
    )

communicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 2)
)
communicationEstablished.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    communicationEstablished.setStatus(
        ""
    )

outletOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 3)
)
outletOn.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAOutletIndex"))
)
if mibBuilder.loadTexts:
    outletOn.setStatus(
        ""
    )

outletOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 4)
)
outletOff.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAOutletIndex"))
)
if mibBuilder.loadTexts:
    outletOff.setStatus(
        ""
    )

outletReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 5)
)
outletReboot.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAOutletIndex"))
)
if mibBuilder.loadTexts:
    outletReboot.setStatus(
        ""
    )

outletLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 6)
)
outletLocked.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAOutletIndex"))
)
if mibBuilder.loadTexts:
    outletLocked.setStatus(
        ""
    )

outletUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 7)
)
outletUnlocked.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAOutletIndex"))
)
if mibBuilder.loadTexts:
    outletUnlocked.setStatus(
        ""
    )

configChangeSNMP = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 8)
)
if mibBuilder.loadTexts:
    configChangeSNMP.setStatus(
        ""
    )

configChangeOutlet = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 9)
)
configChangeOutlet.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAOutletIndex"))
)
if mibBuilder.loadTexts:
    configChangeOutlet.setStatus(
        ""
    )

accessViolationConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 10)
)
accessViolationConsole.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    accessViolationConsole.setStatus(
        ""
    )

accessViolationNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 11)
)
accessViolationNetwork.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    accessViolationNetwork.setStatus(
        ""
    )

userPasswordChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 12)
)
userPasswordChange.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    userPasswordChange.setStatus(
        ""
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 13)
)
userAdded.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        ""
    )

userLoggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 14)
)
userLoggedIn.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    userLoggedIn.setStatus(
        ""
    )

temperatureThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 15)
)
temperatureThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    temperatureThresholdViolation.setStatus(
        ""
    )

temperatureThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 16)
)
temperatureThresholdViolationCleared.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    temperatureThresholdViolationCleared.setStatus(
        ""
    )

currentThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 17)
)
currentThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    currentThresholdViolation.setStatus(
        ""
    )

currentThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 18)
)
currentThresholdViolationCleared.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    currentThresholdViolationCleared.setStatus(
        ""
    )

resetModulesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 19)
)
resetModulesEvent.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    resetModulesEvent.setStatus(
        ""
    )

resetModulesComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 20)
)
resetModulesComplete.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    resetModulesComplete.setStatus(
        ""
    )

errorExecutingSNMPCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 21)
)
errorExecutingSNMPCommand.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    errorExecutingSNMPCommand.setStatus(
        ""
    )

fileTransferComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 22)
)
if mibBuilder.loadTexts:
    fileTransferComplete.setStatus(
        ""
    )

userTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 23)
)
userTerminated.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    userTerminated.setStatus(
        ""
    )

voltageOverThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 24)
)
voltageOverThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    voltageOverThresholdViolation.setStatus(
        ""
    )

voltageOverThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 25)
)
voltageOverThresholdViolationCleared.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    voltageOverThresholdViolationCleared.setStatus(
        ""
    )

voltageUnderThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 26)
)
voltageUnderThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    voltageUnderThresholdViolation.setStatus(
        ""
    )

voltageUnderThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 27)
)
voltageUnderThresholdViolationCleared.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    voltageUnderThresholdViolationCleared.setStatus(
        ""
    )

circuitBreakerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 28)
)
circuitBreakerAlarm.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    circuitBreakerAlarm.setStatus(
        ""
    )

rpcFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 29)
)
rpcFailureAlarm.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    rpcFailureAlarm.setStatus(
        ""
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 30)
)
userDeleted.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsString")
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        ""
    )

warningThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 31)
)
warningThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    warningThresholdViolation.setStatus(
        ""
    )

warningThresholdViolationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 32)
)
warningThresholdViolationClear.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    warningThresholdViolationClear.setStatus(
        ""
    )

emergencyThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 33)
)
emergencyThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    emergencyThresholdViolation.setStatus(
        ""
    )

emergencyThresholdViolationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 34)
)
emergencyThresholdViolationClear.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    emergencyThresholdViolationClear.setStatus(
        ""
    )

circuitBreakerAlarmClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 35)
)
circuitBreakerAlarmClearTrap.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    circuitBreakerAlarmClearTrap.setStatus(
        ""
    )

currentUnderThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 36)
)
currentUnderThresholdViolation.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    currentUnderThresholdViolation.setStatus(
        ""
    )

currentUnderThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 37)
)
currentUnderThresholdViolationCleared.setObjects(
    ("Baytech-MIB-403-1", "mtrapargsInteger")
)
if mibBuilder.loadTexts:
    currentUnderThresholdViolationCleared.setStatus(
        ""
    )

voltageSourceChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 38)
)
voltageSourceChangeAlarm.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTAVoltageSource"),
        ("Baytech-MIB-403-1", "sBTASourceSwitchCount"))
)
if mibBuilder.loadTexts:
    voltageSourceChangeAlarm.setStatus(
        ""
    )

sensorTempThreshHiAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 39)
)
sensorTempThreshHiAlarmTrap.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    sensorTempThreshHiAlarmTrap.setStatus(
        ""
    )

sensorTempThreshHiAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 40)
)
sensorTempThreshHiAlarmClearedTrap.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    sensorTempThreshHiAlarmClearedTrap.setStatus(
        ""
    )

sensorTempThreshLoAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 41)
)
sensorTempThreshLoAlarmTrap.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    sensorTempThreshLoAlarmTrap.setStatus(
        ""
    )

sensorTempThreshLoAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 42)
)
sensorTempThreshLoAlarmClearedTrap.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    sensorTempThreshLoAlarmClearedTrap.setStatus(
        ""
    )

sensorStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 43)
)
sensorStateChangeTrap.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    sensorStateChangeTrap.setStatus(
        ""
    )

configChangeSensor = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 44)
)
configChangeSensor.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    configChangeSensor.setStatus(
        ""
    )

sensorTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4779, 0, 45)
)
sensorTypeChange.setObjects(
      *(("Baytech-MIB-403-1", "sBTAModuleIndex"),
        ("Baytech-MIB-403-1", "sBTASensorIndex"))
)
if mibBuilder.loadTexts:
    sensorTypeChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Baytech-MIB-403-1",
    **{"baytech": baytech,
       "communicationLost": communicationLost,
       "communicationEstablished": communicationEstablished,
       "outletOn": outletOn,
       "outletOff": outletOff,
       "outletReboot": outletReboot,
       "outletLocked": outletLocked,
       "outletUnlocked": outletUnlocked,
       "configChangeSNMP": configChangeSNMP,
       "configChangeOutlet": configChangeOutlet,
       "accessViolationConsole": accessViolationConsole,
       "accessViolationNetwork": accessViolationNetwork,
       "userPasswordChange": userPasswordChange,
       "userAdded": userAdded,
       "userLoggedIn": userLoggedIn,
       "temperatureThresholdViolation": temperatureThresholdViolation,
       "temperatureThresholdViolationCleared": temperatureThresholdViolationCleared,
       "currentThresholdViolation": currentThresholdViolation,
       "currentThresholdViolationCleared": currentThresholdViolationCleared,
       "resetModulesEvent": resetModulesEvent,
       "resetModulesComplete": resetModulesComplete,
       "errorExecutingSNMPCommand": errorExecutingSNMPCommand,
       "fileTransferComplete": fileTransferComplete,
       "userTerminated": userTerminated,
       "voltageOverThresholdViolation": voltageOverThresholdViolation,
       "voltageOverThresholdViolationCleared": voltageOverThresholdViolationCleared,
       "voltageUnderThresholdViolation": voltageUnderThresholdViolation,
       "voltageUnderThresholdViolationCleared": voltageUnderThresholdViolationCleared,
       "circuitBreakerAlarm": circuitBreakerAlarm,
       "rpcFailureAlarm": rpcFailureAlarm,
       "userDeleted": userDeleted,
       "warningThresholdViolation": warningThresholdViolation,
       "warningThresholdViolationClear": warningThresholdViolationClear,
       "emergencyThresholdViolation": emergencyThresholdViolation,
       "emergencyThresholdViolationClear": emergencyThresholdViolationClear,
       "circuitBreakerAlarmClearTrap": circuitBreakerAlarmClearTrap,
       "currentUnderThresholdViolation": currentUnderThresholdViolation,
       "currentUnderThresholdViolationCleared": currentUnderThresholdViolationCleared,
       "voltageSourceChangeAlarm": voltageSourceChangeAlarm,
       "sensorTempThreshHiAlarmTrap": sensorTempThreshHiAlarmTrap,
       "sensorTempThreshHiAlarmClearedTrap": sensorTempThreshHiAlarmClearedTrap,
       "sensorTempThreshLoAlarmTrap": sensorTempThreshLoAlarmTrap,
       "sensorTempThreshLoAlarmClearedTrap": sensorTempThreshLoAlarmClearedTrap,
       "sensorStateChangeTrap": sensorStateChangeTrap,
       "configChangeSensor": configChangeSensor,
       "sensorTypeChange": sensorTypeChange,
       "btadevices": btadevices,
       "sBTAIdent": sBTAIdent,
       "sBTAIdentFirmwareRev": sBTAIdentFirmwareRev,
       "sBTAIdentSerialNumber": sBTAIdentSerialNumber,
       "sBTAIdentUnitName": sBTAIdentUnitName,
       "sBTANetworkConfig": sBTANetworkConfig,
       "sBTANetworkConfigBootpEnable": sBTANetworkConfigBootpEnable,
       "sBTANetworkConfigDHCPEnable": sBTANetworkConfigDHCPEnable,
       "sBTANetworkConfigSSHEnable": sBTANetworkConfigSSHEnable,
       "sBTANetworkConfigTelnetEnable": sBTANetworkConfigTelnetEnable,
       "sBTANetworkConfigActivityTimeout": sBTANetworkConfigActivityTimeout,
       "sBTANetworkConfigDirectConnEnable": sBTANetworkConfigDirectConnEnable,
       "sBTANetworkConfigSNMP": sBTANetworkConfigSNMP,
       "sBTANetworkConfigSNMPReadOnlyCommunity": sBTANetworkConfigSNMPReadOnlyCommunity,
       "sBTANetworkConfigSNMPReadWriteCommunity": sBTANetworkConfigSNMPReadWriteCommunity,
       "sBTANetworkConfigSNMPNumTrapReceivers": sBTANetworkConfigSNMPNumTrapReceivers,
       "sBTANetworkConfigSNMPTrapReceiverTable": sBTANetworkConfigSNMPTrapReceiverTable,
       "sBTANetworkConfigSNMPTrapReceiverEntry": sBTANetworkConfigSNMPTrapReceiverEntry,
       "trapIndex": trapIndex,
       "receiverAddress": receiverAddress,
       "sBTANetworkConfigRadius": sBTANetworkConfigRadius,
       "sBTANetworkConfigRadiusEnable": sBTANetworkConfigRadiusEnable,
       "sBTANetworkConfigRadiusPrimaryServer": sBTANetworkConfigRadiusPrimaryServer,
       "sBTANetworkConfigRadiusSecondaryServer": sBTANetworkConfigRadiusSecondaryServer,
       "sBTANetworkConfigRadiusLocalLogin": sBTANetworkConfigRadiusLocalLogin,
       "sBTANetworkConfigWEB": sBTANetworkConfigWEB,
       "sBTANetworkConfigWebEnable": sBTANetworkConfigWebEnable,
       "sBTANetworkConfigWebSecureEnable": sBTANetworkConfigWebSecureEnable,
       "sBTANetworkConfigWebLoginEnable": sBTANetworkConfigWebLoginEnable,
       "sBTANetworkConfigWebActivityTimeout": sBTANetworkConfigWebActivityTimeout,
       "sBTAModules": sBTAModules,
       "sBTAModulesNumberOfModules": sBTAModulesNumberOfModules,
       "sBTAModulesModulesInstalled": sBTAModulesModulesInstalled,
       "sBTAModulesResetModulesCmd": sBTAModulesResetModulesCmd,
       "sBTAModulesNumberOfIntelligentModules": sBTAModulesNumberOfIntelligentModules,
       "sBTAModulesRPC": sBTAModulesRPC,
       "sBTAModulesNumberOfRPCModules": sBTAModulesNumberOfRPCModules,
       "sBTAModulesRPCTable": sBTAModulesRPCTable,
       "sBTAModulesRPCEntry": sBTAModulesRPCEntry,
       "sBTAModulesRPCIndex": sBTAModulesRPCIndex,
       "sBTAModulesRPCName": sBTAModulesRPCName,
       "sBTAModulesRPCFirmwareVersion": sBTAModulesRPCFirmwareVersion,
       "sBTAModulesRPCCurrent": sBTAModulesRPCCurrent,
       "sBTAModulesRPCMaxCurrent": sBTAModulesRPCMaxCurrent,
       "sBTAModulesRPCVoltage": sBTAModulesRPCVoltage,
       "sBTAModulesRPCPower": sBTAModulesRPCPower,
       "sBTAModulesRPCTemperature": sBTAModulesRPCTemperature,
       "sBTAModulesRPCRebootTimeout": sBTAModulesRPCRebootTimeout,
       "sBTAModulesRPCAllOutletsCmd": sBTAModulesRPCAllOutletsCmd,
       "sBTAModulesRPCAllOutletsStatus": sBTAModulesRPCAllOutletsStatus,
       "sBTAModulesRPCCurrentAlarmThreshold": sBTAModulesRPCCurrentAlarmThreshold,
       "sBTAModulesRPCOverVoltageThreshold": sBTAModulesRPCOverVoltageThreshold,
       "sBTAModulesRPCUnderVoltageThreshold": sBTAModulesRPCUnderVoltageThreshold,
       "sBTAModulesRPCNumberOfOutlets": sBTAModulesRPCNumberOfOutlets,
       "sBTAModulesRPCCircuitBreaker": sBTAModulesRPCCircuitBreaker,
       "sBTAModulesRPCOverTempThreshold": sBTAModulesRPCOverTempThreshold,
       "sBTAModulesRPCUnitVA": sBTAModulesRPCUnitVA,
       "sBTAModulesRPCNumberOfBreakers": sBTAModulesRPCNumberOfBreakers,
       "sBTAModulesRPCLowCurrentThreshold": sBTAModulesRPCLowCurrentThreshold,
       "sBTAModulesRPCVoltageSource": sBTAModulesRPCVoltageSource,
       "sBTAModulesRPCSourceSwitchCount": sBTAModulesRPCSourceSwitchCount,
       "sBTAModulesRPCNumberOfSensors": sBTAModulesRPCNumberOfSensors,
       "sBTAModulesRPCType": sBTAModulesRPCType,
       "sBTAModulesRPCOutletTable": sBTAModulesRPCOutletTable,
       "sBTAModulesRPCOutletEntry": sBTAModulesRPCOutletEntry,
       "sBTAModulesRPCOutletModuleIndex": sBTAModulesRPCOutletModuleIndex,
       "sBTAModulesRPCOutletIndex": sBTAModulesRPCOutletIndex,
       "sBTAModulesRPCOutletState": sBTAModulesRPCOutletState,
       "sBTAModulesRPCOutletName": sBTAModulesRPCOutletName,
       "sBTAModulesRPCGroupCmd": sBTAModulesRPCGroupCmd,
       "sBTAModulesRPCModPortTable": sBTAModulesRPCModPortTable,
       "sBTAModulesRPCModPortEntry": sBTAModulesRPCModPortEntry,
       "sRPCModuleIndex": sRPCModuleIndex,
       "sRPCPortIndex": sRPCPortIndex,
       "sRPCType": sRPCType,
       "sRPCName": sRPCName,
       "sRPCFirmwareVersion": sRPCFirmwareVersion,
       "sRPCCurrent": sRPCCurrent,
       "sRPCMaxCurrent": sRPCMaxCurrent,
       "sRPCVoltage": sRPCVoltage,
       "sRPCPower": sRPCPower,
       "sRPCTemperature": sRPCTemperature,
       "sRPCRebootTimeout": sRPCRebootTimeout,
       "sRPCAllOutletsCmd": sRPCAllOutletsCmd,
       "sRPCAllOutletsStatus": sRPCAllOutletsStatus,
       "sRPCCurrentAlarmThreshold": sRPCCurrentAlarmThreshold,
       "sRPCOverVoltageThreshold": sRPCOverVoltageThreshold,
       "sRPCUnderVoltageThreshold": sRPCUnderVoltageThreshold,
       "sRPCNumberOfOutlets": sRPCNumberOfOutlets,
       "sRPCCircuitBreaker": sRPCCircuitBreaker,
       "sRPCOverTempThreshold": sRPCOverTempThreshold,
       "sRPCUnitVA": sRPCUnitVA,
       "sRPCNumberOfBreakers": sRPCNumberOfBreakers,
       "sRPCLowCurrentThreshold": sRPCLowCurrentThreshold,
       "sRPCVoltageSource": sRPCVoltageSource,
       "sRPCSourceSwitchCount": sRPCSourceSwitchCount,
       "sRPCNumberOfSensors": sRPCNumberOfSensors,
       "sBTAModulesRPCModPortOutletTable": sBTAModulesRPCModPortOutletTable,
       "sBTAModulesRPCModPortOutletEntry": sBTAModulesRPCModPortOutletEntry,
       "sRPCOutletModuleIndex": sRPCOutletModuleIndex,
       "sRPCOutletPortIndex": sRPCOutletPortIndex,
       "sRPCOutletIndex": sRPCOutletIndex,
       "sRPCOutletState": sRPCOutletState,
       "sRPCOutletName": sRPCOutletName,
       "sBTAModulesRPCModPortGroupCmd": sBTAModulesRPCModPortGroupCmd,
       "sBTAModulesRPCCurrentGroupsCurrentTable": sBTAModulesRPCCurrentGroupsCurrentTable,
       "sBTAModulesRPCCurrentGroupsCurrentEntry": sBTAModulesRPCCurrentGroupsCurrentEntry,
       "groupCurrentIndex": groupCurrentIndex,
       "groupCurrent": groupCurrent,
       "rpcGroup": rpcGroup,
       "warningThreshold": warningThreshold,
       "emergencyThreshold": emergencyThreshold,
       "sBTAModulesRPCBreakersTable": sBTAModulesRPCBreakersTable,
       "sBTAModulesRPCBreakersEntry": sBTAModulesRPCBreakersEntry,
       "sBTAModulesRPCBreakersModulesIndex": sBTAModulesRPCBreakersModulesIndex,
       "sBTAModulesRPCBreakersBreakersIndex": sBTAModulesRPCBreakersBreakersIndex,
       "sBTAModulesRPCBreakersCircuitBreaker": sBTAModulesRPCBreakersCircuitBreaker,
       "sBTAModulesRPCBreakersCurrent": sBTAModulesRPCBreakersCurrent,
       "sBTAModulesRPCBreakersMaxCurrent": sBTAModulesRPCBreakersMaxCurrent,
       "sBTAModulesRPCBreakersVoltage": sBTAModulesRPCBreakersVoltage,
       "sBTAModulesRPCBreakersPower": sBTAModulesRPCBreakersPower,
       "sBTAModulesRPCBreakersVA": sBTAModulesRPCBreakersVA,
       "sBTAModulesRPCBreakersCurrentAlarmThreshold": sBTAModulesRPCBreakersCurrentAlarmThreshold,
       "sRPCModPortBreakersTable": sRPCModPortBreakersTable,
       "sRPCModPortBreakersEntry": sRPCModPortBreakersEntry,
       "sRPCBreakersModIndex": sRPCBreakersModIndex,
       "sRPCBreakersPortIndex": sRPCBreakersPortIndex,
       "sRPCBreakersBreakersIndex": sRPCBreakersBreakersIndex,
       "sRPCBreakersCircuitBreaker": sRPCBreakersCircuitBreaker,
       "sRPCBreakersCurrent": sRPCBreakersCurrent,
       "sRPCBreakersMaxCurrent": sRPCBreakersMaxCurrent,
       "sRPCBreakersVoltage": sRPCBreakersVoltage,
       "sRPCBreakersPower": sRPCBreakersPower,
       "sRPCBreakersVA": sRPCBreakersVA,
       "sRPCBreakersCurrentAlarmThreshold": sRPCBreakersCurrentAlarmThreshold,
       "sRPCOutletGroupTable": sRPCOutletGroupTable,
       "sRPCOutletGroupEntry": sRPCOutletGroupEntry,
       "sRPCOutletGroupIndex": sRPCOutletGroupIndex,
       "sRPCOutletGroupName": sRPCOutletGroupName,
       "sRPCOutletGroupOutlets": sRPCOutletGroupOutlets,
       "sRPCOutletGroupCmd": sRPCOutletGroupCmd,
       "sBTAModulesSerial": sBTAModulesSerial,
       "sBTAModulesModem": sBTAModulesModem,
       "sBTAControl": sBTAControl,
       "sBTAControlResetUnit": sBTAControlResetUnit,
       "sBTAControlResetModules": sBTAControlResetModules,
       "sBTAControlNumOfLoggedUsers": sBTAControlNumOfLoggedUsers,
       "sBTAControlUserTable": sBTAControlUserTable,
       "sBTAControlUserEntry": sBTAControlUserEntry,
       "sBTAControlUserIndex": sBTAControlUserIndex,
       "sBTAControlUserName": sBTAControlUserName,
       "sBTAControlUserAddress": sBTAControlUserAddress,
       "sBTAControlUserConnection": sBTAControlUserConnection,
       "sBTAControlUserConnModule": sBTAControlUserConnModule,
       "sBTAControlUserConnPort": sBTAControlUserConnPort,
       "sBTAControlUserTerminateUser": sBTAControlUserTerminateUser,
       "sBTAFileTransfer": sBTAFileTransfer,
       "sBTAFileTransferEnableUpgradeFTPFileTransfer": sBTAFileTransferEnableUpgradeFTPFileTransfer,
       "sBTAEnvironmental": sBTAEnvironmental,
       "sBTAModulesEnvironmentalObjectsTable": sBTAModulesEnvironmentalObjectsTable,
       "sBTAModulesEnvironmentalObjectsEntry": sBTAModulesEnvironmentalObjectsEntry,
       "sBTAModulesEnvironmentalModulesIndex": sBTAModulesEnvironmentalModulesIndex,
       "sBTAModulesEnvironmentalSensorsIndex": sBTAModulesEnvironmentalSensorsIndex,
       "sBTAModulesEnvironmentalType": sBTAModulesEnvironmentalType,
       "sBTAModulesEnvironmentalName": sBTAModulesEnvironmentalName,
       "sBTAModulesEnvironmentalMeasurement": sBTAModulesEnvironmentalMeasurement,
       "sBTAModulesEnvironmentalHiThreshold": sBTAModulesEnvironmentalHiThreshold,
       "sBTAModulesEnvironmentalLoThreshold": sBTAModulesEnvironmentalLoThreshold,
       "sBTAModulesEnvironmentalMax": sBTAModulesEnvironmentalMax,
       "sBTAModulesEnvironmentalMin": sBTAModulesEnvironmentalMin,
       "sBTAModulesEnvironmentalHiThresholdEn": sBTAModulesEnvironmentalHiThresholdEn,
       "sBTAModulesEnvironmentalLoThresholdEn": sBTAModulesEnvironmentalLoThresholdEn,
       "sBTAModulesEnvironmentalStateTrapEn": sBTAModulesEnvironmentalStateTrapEn,
       "sRPCEnvironmentalObjectsTable": sRPCEnvironmentalObjectsTable,
       "sRPCEnvironmentalObjectsEntry": sRPCEnvironmentalObjectsEntry,
       "sRPCEnvironmentalModuleIndex": sRPCEnvironmentalModuleIndex,
       "sRPCEnvironmentalPortIndex": sRPCEnvironmentalPortIndex,
       "sRPCEnvironmentalSensorsIndex": sRPCEnvironmentalSensorsIndex,
       "sRPCEnvironmentalType": sRPCEnvironmentalType,
       "sRPCEnvironmentalName": sRPCEnvironmentalName,
       "sRPCEnvironmentalMeasurement": sRPCEnvironmentalMeasurement,
       "sRPCEnvironmentalHiThreshold": sRPCEnvironmentalHiThreshold,
       "sRPCEnvironmentalLoThreshold": sRPCEnvironmentalLoThreshold,
       "sRPCEnvironmentalMax": sRPCEnvironmentalMax,
       "sRPCEnvironmentalMin": sRPCEnvironmentalMin,
       "sRPCEnvironmentalHiThresholdEn": sRPCEnvironmentalHiThresholdEn,
       "sRPCEnvironmentalLoThresholdEn": sRPCEnvironmentalLoThresholdEn,
       "sRPCEnvironmentalStateTrapEn": sRPCEnvironmentalStateTrapEn,
       "sBTAEnvironmentalAllTemperatureSensorsHiThreshold": sBTAEnvironmentalAllTemperatureSensorsHiThreshold,
       "sBTAEnvironmentalAllTemperatureSensorsLoThreshold": sBTAEnvironmentalAllTemperatureSensorsLoThreshold,
       "sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable": sBTAEnvironmentalAllTemperatureSensorsHiThresholdTrapEnable,
       "sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable": sBTAEnvironmentalAllTemperatureSensorsLoThresholdTrapEnable,
       "sBTAEnvironmentalAllSensorsStateTrapEnable": sBTAEnvironmentalAllSensorsStateTrapEnable,
       "sBTAEnvironmentalAllHumiditySensorsHiThreshold": sBTAEnvironmentalAllHumiditySensorsHiThreshold,
       "sBTAEnvironmentalAllHumiditySensorsLoThreshold": sBTAEnvironmentalAllHumiditySensorsLoThreshold,
       "sBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable": sBTAEnvironmentalAllHumiditySensorsHiThresholdTrapEnable,
       "sBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable": sBTAEnvironmentalAllHumiditySensorsLoThresholdTrapEnable,
       "sBTAEnvironmentalAllAirflowSensorsHiThreshold": sBTAEnvironmentalAllAirflowSensorsHiThreshold,
       "sBTAEnvironmentalAllAirflowSensorsLoThreshold": sBTAEnvironmentalAllAirflowSensorsLoThreshold,
       "sBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable": sBTAEnvironmentalAllAirflowSensorsHiThresholdTrapEnable,
       "sBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable": sBTAEnvironmentalAllAirflowSensorsLoThresholdTrapEnable,
       "mtrapargs": mtrapargs,
       "mtrapargsInteger": mtrapargsInteger,
       "mtrapargsIpAddress": mtrapargsIpAddress,
       "mtrapargsString": mtrapargsString,
       "mtrapargsGauge": mtrapargsGauge,
       "mtrapargsTimeTicks": mtrapargsTimeTicks,
       "sBTAModuleIndex": sBTAModuleIndex,
       "sBTAOutletIndex": sBTAOutletIndex,
       "sBTAPortIndex": sBTAPortIndex,
       "sBTAVoltageSource": sBTAVoltageSource,
       "sBTASourceSwitchCount": sBTASourceSwitchCount,
       "sBTASensorIndex": sBTASensorIndex,
       "sBTABreakerIndex": sBTABreakerIndex}
)
