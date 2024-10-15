# SNMP MIB module (RADLAN-AUTOUPDATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-AUTOUPDATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:38 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlAutoUpdate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 123)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlAutoUpdateEnable_Type = TruthValue
_RlAutoUpdateEnable_Object = MibScalar
rlAutoUpdateEnable = _RlAutoUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 123, 1),
    _RlAutoUpdateEnable_Type()
)
rlAutoUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoUpdateEnable.setStatus("current")
_RlAutoUpdateFilesBoot_Type = TruthValue
_RlAutoUpdateFilesBoot_Object = MibScalar
rlAutoUpdateFilesBoot = _RlAutoUpdateFilesBoot_Object(
    (1, 3, 6, 1, 4, 1, 89, 123, 2),
    _RlAutoUpdateFilesBoot_Type()
)
rlAutoUpdateFilesBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoUpdateFilesBoot.setStatus("current")
_RlAutoUpdateFilesImage_Type = TruthValue
_RlAutoUpdateFilesImage_Object = MibScalar
rlAutoUpdateFilesImage = _RlAutoUpdateFilesImage_Object(
    (1, 3, 6, 1, 4, 1, 89, 123, 3),
    _RlAutoUpdateFilesImage_Type()
)
rlAutoUpdateFilesImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoUpdateFilesImage.setStatus("current")
_RlAutoUpdateFilesConf_Type = TruthValue
_RlAutoUpdateFilesConf_Object = MibScalar
rlAutoUpdateFilesConf = _RlAutoUpdateFilesConf_Object(
    (1, 3, 6, 1, 4, 1, 89, 123, 4),
    _RlAutoUpdateFilesConf_Type()
)
rlAutoUpdateFilesConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoUpdateFilesConf.setStatus("current")
_RlAutoUpdateCopyEnable_Type = TruthValue
_RlAutoUpdateCopyEnable_Object = MibScalar
rlAutoUpdateCopyEnable = _RlAutoUpdateCopyEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 123, 5),
    _RlAutoUpdateCopyEnable_Type()
)
rlAutoUpdateCopyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoUpdateCopyEnable.setStatus("current")
_RlAutoUpdatePreserveIP_Type = TruthValue
_RlAutoUpdatePreserveIP_Object = MibScalar
rlAutoUpdatePreserveIP = _RlAutoUpdatePreserveIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 123, 6),
    _RlAutoUpdatePreserveIP_Type()
)
rlAutoUpdatePreserveIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAutoUpdatePreserveIP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-AUTOUPDATE-MIB",
    **{"rlAutoUpdate": rlAutoUpdate,
       "rlAutoUpdateEnable": rlAutoUpdateEnable,
       "rlAutoUpdateFilesBoot": rlAutoUpdateFilesBoot,
       "rlAutoUpdateFilesImage": rlAutoUpdateFilesImage,
       "rlAutoUpdateFilesConf": rlAutoUpdateFilesConf,
       "rlAutoUpdateCopyEnable": rlAutoUpdateCopyEnable,
       "rlAutoUpdatePreserveIP": rlAutoUpdatePreserveIP}
)
