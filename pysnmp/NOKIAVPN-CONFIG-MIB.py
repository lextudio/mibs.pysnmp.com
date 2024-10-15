# SNMP MIB module (NOKIAVPN-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIAVPN-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:45 2024
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

(config,
 nokiaVPNModules) = mibBuilder.importSymbols(
    "NOKIAVPN-MIB",
    "config",
    "nokiaVPNModules")

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

nokiaVPNConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 5, 6)
)
nokiaVPNConfigMIB.setRevisions(
        ("2001-01-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ConfigDirtyBit_Type(Integer32):
    """Custom type configDirtyBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ConfigDirtyBit_Type.__name__ = "Integer32"
_ConfigDirtyBit_Object = MibScalar
configDirtyBit = _ConfigDirtyBit_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 1),
    _ConfigDirtyBit_Type()
)
configDirtyBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDirtyBit.setStatus("current")


class _ConfigCommit_Type(Integer32):
    """Custom type configCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ConfigCommit_Type.__name__ = "Integer32"
_ConfigCommit_Object = MibScalar
configCommit = _ConfigCommit_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 2),
    _ConfigCommit_Type()
)
configCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configCommit.setStatus("current")
_ConfigPollrate_Type = Integer32
_ConfigPollrate_Object = MibScalar
configPollrate = _ConfigPollrate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 3),
    _ConfigPollrate_Type()
)
configPollrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPollrate.setStatus("current")
_ConfigTrapDelay_Type = Integer32
_ConfigTrapDelay_Object = MibScalar
configTrapDelay = _ConfigTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 4),
    _ConfigTrapDelay_Type()
)
configTrapDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTrapDelay.setStatus("current")
_ConfigTresholdCPUUsage_Type = Integer32
_ConfigTresholdCPUUsage_Object = MibScalar
configTresholdCPUUsage = _ConfigTresholdCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 5),
    _ConfigTresholdCPUUsage_Type()
)
configTresholdCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTresholdCPUUsage.setStatus("current")
_ConfigTresholdIOLoad_Type = Integer32
_ConfigTresholdIOLoad_Object = MibScalar
configTresholdIOLoad = _ConfigTresholdIOLoad_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 6),
    _ConfigTresholdIOLoad_Type()
)
configTresholdIOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTresholdIOLoad.setStatus("current")
_ConfigTresholdUDPDrop_Type = Integer32
_ConfigTresholdUDPDrop_Object = MibScalar
configTresholdUDPDrop = _ConfigTresholdUDPDrop_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 7),
    _ConfigTresholdUDPDrop_Type()
)
configTresholdUDPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTresholdUDPDrop.setStatus("current")
_ConfigTresholdIPDrop_Type = Integer32
_ConfigTresholdIPDrop_Object = MibScalar
configTresholdIPDrop = _ConfigTresholdIPDrop_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 8),
    _ConfigTresholdIPDrop_Type()
)
configTresholdIPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTresholdIPDrop.setStatus("current")
_ConfigTresholdMemUsage_Type = Integer32
_ConfigTresholdMemUsage_Object = MibScalar
configTresholdMemUsage = _ConfigTresholdMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 9),
    _ConfigTresholdMemUsage_Type()
)
configTresholdMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTresholdMemUsage.setStatus("current")
_ConfigValCPUUsage_Type = Integer32
_ConfigValCPUUsage_Object = MibScalar
configValCPUUsage = _ConfigValCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 10),
    _ConfigValCPUUsage_Type()
)
configValCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configValCPUUsage.setStatus("current")
_ConfigValIOLoad_Type = Integer32
_ConfigValIOLoad_Object = MibScalar
configValIOLoad = _ConfigValIOLoad_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 11),
    _ConfigValIOLoad_Type()
)
configValIOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configValIOLoad.setStatus("current")
_ConfigValUDPDrop_Type = Integer32
_ConfigValUDPDrop_Object = MibScalar
configValUDPDrop = _ConfigValUDPDrop_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 12),
    _ConfigValUDPDrop_Type()
)
configValUDPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configValUDPDrop.setStatus("current")
_ConfigValIPDrop_Type = Integer32
_ConfigValIPDrop_Object = MibScalar
configValIPDrop = _ConfigValIPDrop_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 13),
    _ConfigValIPDrop_Type()
)
configValIPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configValIPDrop.setStatus("current")
_ConfigValMemUsage_Type = Integer32
_ConfigValMemUsage_Object = MibScalar
configValMemUsage = _ConfigValMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3, 14),
    _ConfigValMemUsage_Type()
)
configValMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configValMemUsage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIAVPN-CONFIG-MIB",
    **{"configDirtyBit": configDirtyBit,
       "configCommit": configCommit,
       "configPollrate": configPollrate,
       "configTrapDelay": configTrapDelay,
       "configTresholdCPUUsage": configTresholdCPUUsage,
       "configTresholdIOLoad": configTresholdIOLoad,
       "configTresholdUDPDrop": configTresholdUDPDrop,
       "configTresholdIPDrop": configTresholdIPDrop,
       "configTresholdMemUsage": configTresholdMemUsage,
       "configValCPUUsage": configValCPUUsage,
       "configValIOLoad": configValIOLoad,
       "configValUDPDrop": configValUDPDrop,
       "configValIPDrop": configValIPDrop,
       "configValMemUsage": configValMemUsage,
       "nokiaVPNConfigMIB": nokiaVPNConfigMIB}
)
