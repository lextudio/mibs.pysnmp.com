# SNMP MIB module (JUNIPER-JVAE-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JVAE-NODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:24 2024
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

(jnxJVAEMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJVAEMibRoot")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxJVAENodeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2)
)
jnxJVAENodeMIB.setRevisions(
        ("2012-08-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJVAENodeNotifications_ObjectIdentity = ObjectIdentity
jnxJVAENodeNotifications = _JnxJVAENodeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0)
)
_JnxJVAENodeObjects_ObjectIdentity = ObjectIdentity
jnxJVAENodeObjects = _JnxJVAENodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1)
)
_JnxJVAENodeTables_ObjectIdentity = ObjectIdentity
jnxJVAENodeTables = _JnxJVAENodeTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1)
)
_JnxJVAECNSysInfoTable_Object = MibTable
jnxJVAECNSysInfoTable = _JnxJVAECNSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJVAECNSysInfoTable.setStatus("current")
_JnxJVAECNSysInfoEntry_Object = MibTableRow
jnxJVAECNSysInfoEntry = _JnxJVAECNSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1)
)
jnxJVAECNSysInfoEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNSysInfoEntry.setStatus("current")


class _JnxJVAECNSysId_Type(DisplayString):
    """Custom type jnxJVAECNSysId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJVAECNSysId_Type.__name__ = "DisplayString"
_JnxJVAECNSysId_Object = MibTableColumn
jnxJVAECNSysId = _JnxJVAECNSysId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 1),
    _JnxJVAECNSysId_Type()
)
jnxJVAECNSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNSysId.setStatus("current")
_JnxJVAECNSysCpus_Type = Integer32
_JnxJVAECNSysCpus_Object = MibTableColumn
jnxJVAECNSysCpus = _JnxJVAECNSysCpus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 2),
    _JnxJVAECNSysCpus_Type()
)
jnxJVAECNSysCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysCpus.setStatus("current")


class _JnxJVAECNSysProcessingLoad_Type(Integer32):
    """Custom type jnxJVAECNSysProcessingLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxJVAECNSysProcessingLoad_Type.__name__ = "Integer32"
_JnxJVAECNSysProcessingLoad_Object = MibTableColumn
jnxJVAECNSysProcessingLoad = _JnxJVAECNSysProcessingLoad_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 3),
    _JnxJVAECNSysProcessingLoad_Type()
)
jnxJVAECNSysProcessingLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysProcessingLoad.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysProcessingLoad.setUnits("%")
_JnxJVAECNSysMemCapacity_Type = Gauge32
_JnxJVAECNSysMemCapacity_Object = MibTableColumn
jnxJVAECNSysMemCapacity = _JnxJVAECNSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 4),
    _JnxJVAECNSysMemCapacity_Type()
)
jnxJVAECNSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemCapacity.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemCapacity.setUnits("KB")
_JnxJVAECNSysMemUsed_Type = Gauge32
_JnxJVAECNSysMemUsed_Object = MibTableColumn
jnxJVAECNSysMemUsed = _JnxJVAECNSysMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 5),
    _JnxJVAECNSysMemUsed_Type()
)
jnxJVAECNSysMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemUsed.setUnits("KB")
_JnxJVAECNSysMemFree_Type = Gauge32
_JnxJVAECNSysMemFree_Object = MibTableColumn
jnxJVAECNSysMemFree = _JnxJVAECNSysMemFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 6),
    _JnxJVAECNSysMemFree_Type()
)
jnxJVAECNSysMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemFree.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemFree.setUnits("KB")


class _JnxJVAECNSysMemUsedPr_Type(Integer32):
    """Custom type jnxJVAECNSysMemUsedPr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxJVAECNSysMemUsedPr_Type.__name__ = "Integer32"
_JnxJVAECNSysMemUsedPr_Object = MibTableColumn
jnxJVAECNSysMemUsedPr = _JnxJVAECNSysMemUsedPr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 7),
    _JnxJVAECNSysMemUsedPr_Type()
)
jnxJVAECNSysMemUsedPr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemUsedPr.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysMemUsedPr.setUnits("%")
_JnxJVAECNSysSwapCapacity_Type = Gauge32
_JnxJVAECNSysSwapCapacity_Object = MibTableColumn
jnxJVAECNSysSwapCapacity = _JnxJVAECNSysSwapCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 8),
    _JnxJVAECNSysSwapCapacity_Type()
)
jnxJVAECNSysSwapCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysSwapCapacity.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysSwapCapacity.setUnits("KB")
_JnxJVAECNSysSwapFree_Type = Gauge32
_JnxJVAECNSysSwapFree_Object = MibTableColumn
jnxJVAECNSysSwapFree = _JnxJVAECNSysSwapFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 9),
    _JnxJVAECNSysSwapFree_Type()
)
jnxJVAECNSysSwapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysSwapFree.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysSwapFree.setUnits("KB")


class _JnxJVAECNSysBootMethod_Type(Integer32):
    """Custom type jnxJVAECNSysBootMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("network", 1),
          ("unknown", 0))
    )


_JnxJVAECNSysBootMethod_Type.__name__ = "Integer32"
_JnxJVAECNSysBootMethod_Object = MibTableColumn
jnxJVAECNSysBootMethod = _JnxJVAECNSysBootMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 10),
    _JnxJVAECNSysBootMethod_Type()
)
jnxJVAECNSysBootMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysBootMethod.setStatus("current")


class _JnxJVAECNSysLastReboot_Type(DisplayString):
    """Custom type jnxJVAECNSysLastReboot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_JnxJVAECNSysLastReboot_Type.__name__ = "DisplayString"
_JnxJVAECNSysLastReboot_Object = MibTableColumn
jnxJVAECNSysLastReboot = _JnxJVAECNSysLastReboot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 11),
    _JnxJVAECNSysLastReboot_Type()
)
jnxJVAECNSysLastReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSysLastReboot.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNSysLastReboot.setUnits("Secs")
_JnxJVAECNProcessorTable_Object = MibTable
jnxJVAECNProcessorTable = _JnxJVAECNProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJVAECNProcessorTable.setStatus("current")
_JnxJVAECNProcessorEntry_Object = MibTableRow
jnxJVAECNProcessorEntry = _JnxJVAECNProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2, 1)
)
jnxJVAECNProcessorEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNProcessorEntry.setStatus("current")


class _JnxJVAECNProcessorId_Type(Integer32):
    """Custom type jnxJVAECNProcessorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_JnxJVAECNProcessorId_Type.__name__ = "Integer32"
_JnxJVAECNProcessorId_Object = MibTableColumn
jnxJVAECNProcessorId = _JnxJVAECNProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2, 1, 1),
    _JnxJVAECNProcessorId_Type()
)
jnxJVAECNProcessorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNProcessorId.setStatus("current")


class _JnxJVAECNProcessorLoad_Type(Integer32):
    """Custom type jnxJVAECNProcessorLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxJVAECNProcessorLoad_Type.__name__ = "Integer32"
_JnxJVAECNProcessorLoad_Object = MibTableColumn
jnxJVAECNProcessorLoad = _JnxJVAECNProcessorLoad_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2, 1, 2),
    _JnxJVAECNProcessorLoad_Type()
)
jnxJVAECNProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNProcessorLoad.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNProcessorLoad.setUnits("%")
_JnxJVAECNifTable_Object = MibTable
jnxJVAECNifTable = _JnxJVAECNifTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxJVAECNifTable.setStatus("current")
_JnxJVAECNifEntry_Object = MibTableRow
jnxJVAECNifEntry = _JnxJVAECNifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1)
)
jnxJVAECNifEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNifEntry.setStatus("current")


class _JnxJVAECNifId_Type(Integer32):
    """Custom type jnxJVAECNifId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxJVAECNifId_Type.__name__ = "Integer32"
_JnxJVAECNifId_Object = MibTableColumn
jnxJVAECNifId = _JnxJVAECNifId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 1),
    _JnxJVAECNifId_Type()
)
jnxJVAECNifId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNifId.setStatus("current")


class _JnxJVAECNifName_Type(DisplayString):
    """Custom type jnxJVAECNifName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_JnxJVAECNifName_Type.__name__ = "DisplayString"
_JnxJVAECNifName_Object = MibTableColumn
jnxJVAECNifName = _JnxJVAECNifName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 2),
    _JnxJVAECNifName_Type()
)
jnxJVAECNifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifName.setStatus("current")


class _JnxJVAECNifOperStatus_Type(Integer32):
    """Custom type jnxJVAECNifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_JnxJVAECNifOperStatus_Type.__name__ = "Integer32"
_JnxJVAECNifOperStatus_Object = MibTableColumn
jnxJVAECNifOperStatus = _JnxJVAECNifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 3),
    _JnxJVAECNifOperStatus_Type()
)
jnxJVAECNifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifOperStatus.setStatus("current")


class _JnxJVAECNifAdminStatus_Type(Integer32):
    """Custom type jnxJVAECNifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_JnxJVAECNifAdminStatus_Type.__name__ = "Integer32"
_JnxJVAECNifAdminStatus_Object = MibTableColumn
jnxJVAECNifAdminStatus = _JnxJVAECNifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 4),
    _JnxJVAECNifAdminStatus_Type()
)
jnxJVAECNifAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifAdminStatus.setStatus("current")
_JnxJVAECNifLinkDetect_Type = TruthValue
_JnxJVAECNifLinkDetect_Object = MibTableColumn
jnxJVAECNifLinkDetect = _JnxJVAECNifLinkDetect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 5),
    _JnxJVAECNifLinkDetect_Type()
)
jnxJVAECNifLinkDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifLinkDetect.setStatus("current")
_JnxJVAECNifAddress_Type = PhysAddress
_JnxJVAECNifAddress_Object = MibTableColumn
jnxJVAECNifAddress = _JnxJVAECNifAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 6),
    _JnxJVAECNifAddress_Type()
)
jnxJVAECNifAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifAddress.setStatus("current")
_JnxJVAECNifInPkts_Type = Counter64
_JnxJVAECNifInPkts_Object = MibTableColumn
jnxJVAECNifInPkts = _JnxJVAECNifInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 7),
    _JnxJVAECNifInPkts_Type()
)
jnxJVAECNifInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifInPkts.setStatus("current")
_JnxJVAECNifInDiscards_Type = Counter64
_JnxJVAECNifInDiscards_Object = MibTableColumn
jnxJVAECNifInDiscards = _JnxJVAECNifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 8),
    _JnxJVAECNifInDiscards_Type()
)
jnxJVAECNifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifInDiscards.setStatus("current")
_JnxJVAECNifInErrors_Type = Counter64
_JnxJVAECNifInErrors_Object = MibTableColumn
jnxJVAECNifInErrors = _JnxJVAECNifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 9),
    _JnxJVAECNifInErrors_Type()
)
jnxJVAECNifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifInErrors.setStatus("current")
_JnxJVAECNifOutPkts_Type = Counter64
_JnxJVAECNifOutPkts_Object = MibTableColumn
jnxJVAECNifOutPkts = _JnxJVAECNifOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 10),
    _JnxJVAECNifOutPkts_Type()
)
jnxJVAECNifOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifOutPkts.setStatus("current")
_JnxJVAECNifOutDiscards_Type = Counter64
_JnxJVAECNifOutDiscards_Object = MibTableColumn
jnxJVAECNifOutDiscards = _JnxJVAECNifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 11),
    _JnxJVAECNifOutDiscards_Type()
)
jnxJVAECNifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifOutDiscards.setStatus("current")
_JnxJVAECNifOutErrors_Type = Counter64
_JnxJVAECNifOutErrors_Object = MibTableColumn
jnxJVAECNifOutErrors = _JnxJVAECNifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 12),
    _JnxJVAECNifOutErrors_Type()
)
jnxJVAECNifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNifOutErrors.setStatus("current")
_JnxJVAECNFileSysTable_Object = MibTable
jnxJVAECNFileSysTable = _JnxJVAECNFileSysTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxJVAECNFileSysTable.setStatus("current")
_JnxJVAECNFileSysEntry_Object = MibTableRow
jnxJVAECNFileSysEntry = _JnxJVAECNFileSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1)
)
jnxJVAECNFileSysEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNFileSysEntry.setStatus("current")


class _JnxJVAECNFileSysId_Type(Integer32):
    """Custom type jnxJVAECNFileSysId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_JnxJVAECNFileSysId_Type.__name__ = "Integer32"
_JnxJVAECNFileSysId_Object = MibTableColumn
jnxJVAECNFileSysId = _JnxJVAECNFileSysId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 1),
    _JnxJVAECNFileSysId_Type()
)
jnxJVAECNFileSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysId.setStatus("current")


class _JnxJVAECNFileSysMountPoint_Type(DisplayString):
    """Custom type jnxJVAECNFileSysMountPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAECNFileSysMountPoint_Type.__name__ = "DisplayString"
_JnxJVAECNFileSysMountPoint_Object = MibTableColumn
jnxJVAECNFileSysMountPoint = _JnxJVAECNFileSysMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 2),
    _JnxJVAECNFileSysMountPoint_Type()
)
jnxJVAECNFileSysMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysMountPoint.setStatus("current")
_JnxJVAECNFileSysSize_Type = Gauge32
_JnxJVAECNFileSysSize_Object = MibTableColumn
jnxJVAECNFileSysSize = _JnxJVAECNFileSysSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 3),
    _JnxJVAECNFileSysSize_Type()
)
jnxJVAECNFileSysSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysSize.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysSize.setUnits("KB")
_JnxJVAECNFileSysUsed_Type = Gauge32
_JnxJVAECNFileSysUsed_Object = MibTableColumn
jnxJVAECNFileSysUsed = _JnxJVAECNFileSysUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 4),
    _JnxJVAECNFileSysUsed_Type()
)
jnxJVAECNFileSysUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysUsed.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysUsed.setUnits("KB")
_JnxJVAECNFileSysFree_Type = Gauge32
_JnxJVAECNFileSysFree_Object = MibTableColumn
jnxJVAECNFileSysFree = _JnxJVAECNFileSysFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 5),
    _JnxJVAECNFileSysFree_Type()
)
jnxJVAECNFileSysFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysFree.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysFree.setUnits("KB")


class _JnxJVAECNFileSysUsedPr_Type(Integer32):
    """Custom type jnxJVAECNFileSysUsedPr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxJVAECNFileSysUsedPr_Type.__name__ = "Integer32"
_JnxJVAECNFileSysUsedPr_Object = MibTableColumn
jnxJVAECNFileSysUsedPr = _JnxJVAECNFileSysUsedPr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 6),
    _JnxJVAECNFileSysUsedPr_Type()
)
jnxJVAECNFileSysUsedPr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysUsedPr.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNFileSysUsedPr.setUnits("%")
_JnxJVAECNDiskTable_Object = MibTable
jnxJVAECNDiskTable = _JnxJVAECNDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxJVAECNDiskTable.setStatus("current")
_JnxJVAECNDiskEntry_Object = MibTableRow
jnxJVAECNDiskEntry = _JnxJVAECNDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1)
)
jnxJVAECNDiskEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNDiskId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNDiskEntry.setStatus("current")


class _JnxJVAECNDiskId_Type(Integer32):
    """Custom type jnxJVAECNDiskId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_JnxJVAECNDiskId_Type.__name__ = "Integer32"
_JnxJVAECNDiskId_Object = MibTableColumn
jnxJVAECNDiskId = _JnxJVAECNDiskId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 1),
    _JnxJVAECNDiskId_Type()
)
jnxJVAECNDiskId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNDiskId.setStatus("current")


class _JnxJVAECNDiskSlot_Type(Integer32):
    """Custom type jnxJVAECNDiskSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_JnxJVAECNDiskSlot_Type.__name__ = "Integer32"
_JnxJVAECNDiskSlot_Object = MibTableColumn
jnxJVAECNDiskSlot = _JnxJVAECNDiskSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 2),
    _JnxJVAECNDiskSlot_Type()
)
jnxJVAECNDiskSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNDiskSlot.setStatus("current")


class _JnxJVAECNDiskModel_Type(DisplayString):
    """Custom type jnxJVAECNDiskModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxJVAECNDiskModel_Type.__name__ = "DisplayString"
_JnxJVAECNDiskModel_Object = MibTableColumn
jnxJVAECNDiskModel = _JnxJVAECNDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 3),
    _JnxJVAECNDiskModel_Type()
)
jnxJVAECNDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNDiskModel.setStatus("current")


class _JnxJVAECNDiskRevision_Type(DisplayString):
    """Custom type jnxJVAECNDiskRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAECNDiskRevision_Type.__name__ = "DisplayString"
_JnxJVAECNDiskRevision_Object = MibTableColumn
jnxJVAECNDiskRevision = _JnxJVAECNDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 4),
    _JnxJVAECNDiskRevision_Type()
)
jnxJVAECNDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNDiskRevision.setStatus("current")


class _JnxJVAECNDiskVendor_Type(DisplayString):
    """Custom type jnxJVAECNDiskVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAECNDiskVendor_Type.__name__ = "DisplayString"
_JnxJVAECNDiskVendor_Object = MibTableColumn
jnxJVAECNDiskVendor = _JnxJVAECNDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 5),
    _JnxJVAECNDiskVendor_Type()
)
jnxJVAECNDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNDiskVendor.setStatus("current")


class _JnxJVAECNDiskOSPath_Type(DisplayString):
    """Custom type jnxJVAECNDiskOSPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAECNDiskOSPath_Type.__name__ = "DisplayString"
_JnxJVAECNDiskOSPath_Object = MibTableColumn
jnxJVAECNDiskOSPath = _JnxJVAECNDiskOSPath_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 6),
    _JnxJVAECNDiskOSPath_Type()
)
jnxJVAECNDiskOSPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNDiskOSPath.setStatus("current")
_JnxJVAECNRaidTable_Object = MibTable
jnxJVAECNRaidTable = _JnxJVAECNRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxJVAECNRaidTable.setStatus("current")
_JnxJVAECNRaidEntry_Object = MibTableRow
jnxJVAECNRaidEntry = _JnxJVAECNRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1)
)
jnxJVAECNRaidEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNRaidEntry.setStatus("current")


class _JnxJVAECNRaidId_Type(Integer32):
    """Custom type jnxJVAECNRaidId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_JnxJVAECNRaidId_Type.__name__ = "Integer32"
_JnxJVAECNRaidId_Object = MibTableColumn
jnxJVAECNRaidId = _JnxJVAECNRaidId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 1),
    _JnxJVAECNRaidId_Type()
)
jnxJVAECNRaidId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNRaidId.setStatus("current")


class _JnxJVAECNRaidName_Type(DisplayString):
    """Custom type jnxJVAECNRaidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxJVAECNRaidName_Type.__name__ = "DisplayString"
_JnxJVAECNRaidName_Object = MibTableColumn
jnxJVAECNRaidName = _JnxJVAECNRaidName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 2),
    _JnxJVAECNRaidName_Type()
)
jnxJVAECNRaidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidName.setStatus("current")


class _JnxJVAECNRaidState_Type(DisplayString):
    """Custom type jnxJVAECNRaidState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxJVAECNRaidState_Type.__name__ = "DisplayString"
_JnxJVAECNRaidState_Object = MibTableColumn
jnxJVAECNRaidState = _JnxJVAECNRaidState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 3),
    _JnxJVAECNRaidState_Type()
)
jnxJVAECNRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidState.setStatus("current")
_JnxJVAECNRaidLevel_Type = Integer32
_JnxJVAECNRaidLevel_Object = MibTableColumn
jnxJVAECNRaidLevel = _JnxJVAECNRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 4),
    _JnxJVAECNRaidLevel_Type()
)
jnxJVAECNRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidLevel.setStatus("current")
_JnxJVAECNRaidSize_Type = Gauge32
_JnxJVAECNRaidSize_Object = MibTableColumn
jnxJVAECNRaidSize = _JnxJVAECNRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 5),
    _JnxJVAECNRaidSize_Type()
)
jnxJVAECNRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    jnxJVAECNRaidSize.setUnits("GB")
_JnxJVAECNRaidMembers_Type = Integer32
_JnxJVAECNRaidMembers_Object = MibTableColumn
jnxJVAECNRaidMembers = _JnxJVAECNRaidMembers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 6),
    _JnxJVAECNRaidMembers_Type()
)
jnxJVAECNRaidMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidMembers.setStatus("current")


class _JnxJVAECNRaidMemberDiskPartitions_Type(DisplayString):
    """Custom type jnxJVAECNRaidMemberDiskPartitions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxJVAECNRaidMemberDiskPartitions_Type.__name__ = "DisplayString"
_JnxJVAECNRaidMemberDiskPartitions_Object = MibTableColumn
jnxJVAECNRaidMemberDiskPartitions = _JnxJVAECNRaidMemberDiskPartitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 7),
    _JnxJVAECNRaidMemberDiskPartitions_Type()
)
jnxJVAECNRaidMemberDiskPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidMemberDiskPartitions.setStatus("current")


class _JnxJVAECNRaidMemberDiskAtSlots_Type(DisplayString):
    """Custom type jnxJVAECNRaidMemberDiskAtSlots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxJVAECNRaidMemberDiskAtSlots_Type.__name__ = "DisplayString"
_JnxJVAECNRaidMemberDiskAtSlots_Object = MibTableColumn
jnxJVAECNRaidMemberDiskAtSlots = _JnxJVAECNRaidMemberDiskAtSlots_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 8),
    _JnxJVAECNRaidMemberDiskAtSlots_Type()
)
jnxJVAECNRaidMemberDiskAtSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidMemberDiskAtSlots.setStatus("current")


class _JnxJVAECNRaidOSPath_Type(DisplayString):
    """Custom type jnxJVAECNRaidOSPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_JnxJVAECNRaidOSPath_Type.__name__ = "DisplayString"
_JnxJVAECNRaidOSPath_Object = MibTableColumn
jnxJVAECNRaidOSPath = _JnxJVAECNRaidOSPath_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 9),
    _JnxJVAECNRaidOSPath_Type()
)
jnxJVAECNRaidOSPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNRaidOSPath.setStatus("current")
_JnxJVAECNSensorTable_Object = MibTable
jnxJVAECNSensorTable = _JnxJVAECNSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxJVAECNSensorTable.setStatus("current")
_JnxJVAECNSensorEntry_Object = MibTableRow
jnxJVAECNSensorEntry = _JnxJVAECNSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1)
)
jnxJVAECNSensorEntry.setIndexNames(
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
    (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorId"),
)
if mibBuilder.loadTexts:
    jnxJVAECNSensorEntry.setStatus("current")


class _JnxJVAECNSensorId_Type(Integer32):
    """Custom type jnxJVAECNSensorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxJVAECNSensorId_Type.__name__ = "Integer32"
_JnxJVAECNSensorId_Object = MibTableColumn
jnxJVAECNSensorId = _JnxJVAECNSensorId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 1),
    _JnxJVAECNSensorId_Type()
)
jnxJVAECNSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJVAECNSensorId.setStatus("current")


class _JnxJVAECNSensorType_Type(Integer32):
    """Custom type jnxJVAECNSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fan", 2),
          ("temperature", 1),
          ("voltage", 0))
    )


_JnxJVAECNSensorType_Type.__name__ = "Integer32"
_JnxJVAECNSensorType_Object = MibTableColumn
jnxJVAECNSensorType = _JnxJVAECNSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 2),
    _JnxJVAECNSensorType_Type()
)
jnxJVAECNSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSensorType.setStatus("current")


class _JnxJVAECNSensorValue_Type(DisplayString):
    """Custom type jnxJVAECNSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxJVAECNSensorValue_Type.__name__ = "DisplayString"
_JnxJVAECNSensorValue_Object = MibTableColumn
jnxJVAECNSensorValue = _JnxJVAECNSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 3),
    _JnxJVAECNSensorValue_Type()
)
jnxJVAECNSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSensorValue.setStatus("current")


class _JnxJVAECNSensorRange_Type(DisplayString):
    """Custom type jnxJVAECNSensorRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxJVAECNSensorRange_Type.__name__ = "DisplayString"
_JnxJVAECNSensorRange_Object = MibTableColumn
jnxJVAECNSensorRange = _JnxJVAECNSensorRange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 4),
    _JnxJVAECNSensorRange_Type()
)
jnxJVAECNSensorRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSensorRange.setStatus("current")


class _JnxJVAECNSensorDesc_Type(DisplayString):
    """Custom type jnxJVAECNSensorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxJVAECNSensorDesc_Type.__name__ = "DisplayString"
_JnxJVAECNSensorDesc_Object = MibTableColumn
jnxJVAECNSensorDesc = _JnxJVAECNSensorDesc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 5),
    _JnxJVAECNSensorDesc_Type()
)
jnxJVAECNSensorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJVAECNSensorDesc.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJVAECNMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 1)
)
jnxJVAECNMemoryLow.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemCapacity"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsed"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemFree"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsedPr"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapCapacity"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapFree"))
)
if mibBuilder.loadTexts:
    jnxJVAECNMemoryLow.setStatus(
        "current"
    )

jnxJVAECNMemoryOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 2)
)
jnxJVAECNMemoryOk.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemCapacity"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsed"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemFree"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsedPr"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapCapacity"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapFree"))
)
if mibBuilder.loadTexts:
    jnxJVAECNMemoryOk.setStatus(
        "current"
    )

jnxJVAECNProcessingLoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 3)
)
jnxJVAECNProcessingLoadHigh.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysProcessingLoad"))
)
if mibBuilder.loadTexts:
    jnxJVAECNProcessingLoadHigh.setStatus(
        "current"
    )

jnxJVAECNProcessingLoadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 4)
)
jnxJVAECNProcessingLoadOk.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysProcessingLoad"))
)
if mibBuilder.loadTexts:
    jnxJVAECNProcessingLoadOk.setStatus(
        "current"
    )

jnxJVAECNProcessorLoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 5)
)
jnxJVAECNProcessorLoadHigh.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorLoad"))
)
if mibBuilder.loadTexts:
    jnxJVAECNProcessorLoadHigh.setStatus(
        "current"
    )

jnxJVAECNProcessorLoadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 6)
)
jnxJVAECNProcessorLoadOk.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorLoad"))
)
if mibBuilder.loadTexts:
    jnxJVAECNProcessorLoadOk.setStatus(
        "current"
    )

jnxJVAECNifDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 7)
)
jnxJVAECNifDown.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifName"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifOperStatus"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifAdminStatus"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifLinkDetect"))
)
if mibBuilder.loadTexts:
    jnxJVAECNifDown.setStatus(
        "current"
    )

jnxJVAECNifUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 8)
)
jnxJVAECNifUp.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifName"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifOperStatus"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifAdminStatus"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifLinkDetect"))
)
if mibBuilder.loadTexts:
    jnxJVAECNifUp.setStatus(
        "current"
    )

jnxJVAECNStorageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 9)
)
jnxJVAECNStorageLow.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysMountPoint"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysSize"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsed"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysFree"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsedPr"))
)
if mibBuilder.loadTexts:
    jnxJVAECNStorageLow.setStatus(
        "current"
    )

jnxJVAECNStorageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 10)
)
jnxJVAECNStorageOk.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysMountPoint"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysSize"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsed"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysFree"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsedPr"))
)
if mibBuilder.loadTexts:
    jnxJVAECNStorageOk.setStatus(
        "current"
    )

jnxJVAECNRaidError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 11)
)
jnxJVAECNRaidError.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidName"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidState"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidOSPath"))
)
if mibBuilder.loadTexts:
    jnxJVAECNRaidError.setStatus(
        "current"
    )

jnxJVAECNRaidOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 12)
)
jnxJVAECNRaidOk.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidName"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidState"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidOSPath"))
)
if mibBuilder.loadTexts:
    jnxJVAECNRaidOk.setStatus(
        "current"
    )

jnxJVAECNSensorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 13)
)
jnxJVAECNSensorAlert.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorValue"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorType"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorRange"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorDesc"))
)
if mibBuilder.loadTexts:
    jnxJVAECNSensorAlert.setStatus(
        "current"
    )

jnxJVAECNSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 14)
)
jnxJVAECNSensorOk.setObjects(
      *(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorId"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorValue"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorType"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorRange"),
        ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorDesc"))
)
if mibBuilder.loadTexts:
    jnxJVAECNSensorOk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JVAE-NODE-MIB",
    **{"jnxJVAENodeMIB": jnxJVAENodeMIB,
       "jnxJVAENodeNotifications": jnxJVAENodeNotifications,
       "jnxJVAECNMemoryLow": jnxJVAECNMemoryLow,
       "jnxJVAECNMemoryOk": jnxJVAECNMemoryOk,
       "jnxJVAECNProcessingLoadHigh": jnxJVAECNProcessingLoadHigh,
       "jnxJVAECNProcessingLoadOk": jnxJVAECNProcessingLoadOk,
       "jnxJVAECNProcessorLoadHigh": jnxJVAECNProcessorLoadHigh,
       "jnxJVAECNProcessorLoadOk": jnxJVAECNProcessorLoadOk,
       "jnxJVAECNifDown": jnxJVAECNifDown,
       "jnxJVAECNifUp": jnxJVAECNifUp,
       "jnxJVAECNStorageLow": jnxJVAECNStorageLow,
       "jnxJVAECNStorageOk": jnxJVAECNStorageOk,
       "jnxJVAECNRaidError": jnxJVAECNRaidError,
       "jnxJVAECNRaidOk": jnxJVAECNRaidOk,
       "jnxJVAECNSensorAlert": jnxJVAECNSensorAlert,
       "jnxJVAECNSensorOk": jnxJVAECNSensorOk,
       "jnxJVAENodeObjects": jnxJVAENodeObjects,
       "jnxJVAENodeTables": jnxJVAENodeTables,
       "jnxJVAECNSysInfoTable": jnxJVAECNSysInfoTable,
       "jnxJVAECNSysInfoEntry": jnxJVAECNSysInfoEntry,
       "jnxJVAECNSysId": jnxJVAECNSysId,
       "jnxJVAECNSysCpus": jnxJVAECNSysCpus,
       "jnxJVAECNSysProcessingLoad": jnxJVAECNSysProcessingLoad,
       "jnxJVAECNSysMemCapacity": jnxJVAECNSysMemCapacity,
       "jnxJVAECNSysMemUsed": jnxJVAECNSysMemUsed,
       "jnxJVAECNSysMemFree": jnxJVAECNSysMemFree,
       "jnxJVAECNSysMemUsedPr": jnxJVAECNSysMemUsedPr,
       "jnxJVAECNSysSwapCapacity": jnxJVAECNSysSwapCapacity,
       "jnxJVAECNSysSwapFree": jnxJVAECNSysSwapFree,
       "jnxJVAECNSysBootMethod": jnxJVAECNSysBootMethod,
       "jnxJVAECNSysLastReboot": jnxJVAECNSysLastReboot,
       "jnxJVAECNProcessorTable": jnxJVAECNProcessorTable,
       "jnxJVAECNProcessorEntry": jnxJVAECNProcessorEntry,
       "jnxJVAECNProcessorId": jnxJVAECNProcessorId,
       "jnxJVAECNProcessorLoad": jnxJVAECNProcessorLoad,
       "jnxJVAECNifTable": jnxJVAECNifTable,
       "jnxJVAECNifEntry": jnxJVAECNifEntry,
       "jnxJVAECNifId": jnxJVAECNifId,
       "jnxJVAECNifName": jnxJVAECNifName,
       "jnxJVAECNifOperStatus": jnxJVAECNifOperStatus,
       "jnxJVAECNifAdminStatus": jnxJVAECNifAdminStatus,
       "jnxJVAECNifLinkDetect": jnxJVAECNifLinkDetect,
       "jnxJVAECNifAddress": jnxJVAECNifAddress,
       "jnxJVAECNifInPkts": jnxJVAECNifInPkts,
       "jnxJVAECNifInDiscards": jnxJVAECNifInDiscards,
       "jnxJVAECNifInErrors": jnxJVAECNifInErrors,
       "jnxJVAECNifOutPkts": jnxJVAECNifOutPkts,
       "jnxJVAECNifOutDiscards": jnxJVAECNifOutDiscards,
       "jnxJVAECNifOutErrors": jnxJVAECNifOutErrors,
       "jnxJVAECNFileSysTable": jnxJVAECNFileSysTable,
       "jnxJVAECNFileSysEntry": jnxJVAECNFileSysEntry,
       "jnxJVAECNFileSysId": jnxJVAECNFileSysId,
       "jnxJVAECNFileSysMountPoint": jnxJVAECNFileSysMountPoint,
       "jnxJVAECNFileSysSize": jnxJVAECNFileSysSize,
       "jnxJVAECNFileSysUsed": jnxJVAECNFileSysUsed,
       "jnxJVAECNFileSysFree": jnxJVAECNFileSysFree,
       "jnxJVAECNFileSysUsedPr": jnxJVAECNFileSysUsedPr,
       "jnxJVAECNDiskTable": jnxJVAECNDiskTable,
       "jnxJVAECNDiskEntry": jnxJVAECNDiskEntry,
       "jnxJVAECNDiskId": jnxJVAECNDiskId,
       "jnxJVAECNDiskSlot": jnxJVAECNDiskSlot,
       "jnxJVAECNDiskModel": jnxJVAECNDiskModel,
       "jnxJVAECNDiskRevision": jnxJVAECNDiskRevision,
       "jnxJVAECNDiskVendor": jnxJVAECNDiskVendor,
       "jnxJVAECNDiskOSPath": jnxJVAECNDiskOSPath,
       "jnxJVAECNRaidTable": jnxJVAECNRaidTable,
       "jnxJVAECNRaidEntry": jnxJVAECNRaidEntry,
       "jnxJVAECNRaidId": jnxJVAECNRaidId,
       "jnxJVAECNRaidName": jnxJVAECNRaidName,
       "jnxJVAECNRaidState": jnxJVAECNRaidState,
       "jnxJVAECNRaidLevel": jnxJVAECNRaidLevel,
       "jnxJVAECNRaidSize": jnxJVAECNRaidSize,
       "jnxJVAECNRaidMembers": jnxJVAECNRaidMembers,
       "jnxJVAECNRaidMemberDiskPartitions": jnxJVAECNRaidMemberDiskPartitions,
       "jnxJVAECNRaidMemberDiskAtSlots": jnxJVAECNRaidMemberDiskAtSlots,
       "jnxJVAECNRaidOSPath": jnxJVAECNRaidOSPath,
       "jnxJVAECNSensorTable": jnxJVAECNSensorTable,
       "jnxJVAECNSensorEntry": jnxJVAECNSensorEntry,
       "jnxJVAECNSensorId": jnxJVAECNSensorId,
       "jnxJVAECNSensorType": jnxJVAECNSensorType,
       "jnxJVAECNSensorValue": jnxJVAECNSensorValue,
       "jnxJVAECNSensorRange": jnxJVAECNSensorRange,
       "jnxJVAECNSensorDesc": jnxJVAECNSensorDesc}
)
