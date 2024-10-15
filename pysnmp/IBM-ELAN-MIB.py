# SNMP MIB module (IBM-ELAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-ELAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:27 2024
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

(AtmLaneAddress,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress")

(elanConfEntry,
 elanLesEntry,
 lecsConfEntry) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "elanConfEntry",
    "elanLesEntry",
    "lecsConfEntry")

(AtmPrivateAddrEsi,
 AtmSelector,
 mssServerLanE) = mibBuilder.importSymbols(
    "NWAYSMSS-MIB",
    "AtmPrivateAddrEsi",
    "AtmSelector",
    "mssServerLanE")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmElanMIB_ObjectIdentity = ObjectIdentity
ibmElanMIB = _IbmElanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4)
)
_IbmElanAdminGroup_ObjectIdentity = ObjectIdentity
ibmElanAdminGroup = _IbmElanAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 1)
)
_IbmElanConfGroup_ObjectIdentity = ObjectIdentity
ibmElanConfGroup = _IbmElanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2)
)
_IbmElanLesTable_Object = MibTable
ibmElanLesTable = _IbmElanLesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ibmElanLesTable.setStatus("mandatory")
_IbmElanLesEntry_Object = MibTableRow
ibmElanLesEntry = _IbmElanLesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2, 1)
)
ibmElanLesEntry.setIndexNames(
    (0, "IBM-ELAN-MIB", "elanConfIndex"),
    (0, "IBM-ELAN-MIB", "elanLesIndex"),
)
if mibBuilder.loadTexts:
    ibmElanLesEntry.setStatus("mandatory")


class _IbmBackupLesAtmAddrValid_Type(TruthValue):
    """Custom type ibmBackupLesAtmAddrValid based on TruthValue"""


_IbmBackupLesAtmAddrValid_Object = MibTableColumn
ibmBackupLesAtmAddrValid = _IbmBackupLesAtmAddrValid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2, 1, 1),
    _IbmBackupLesAtmAddrValid_Type()
)
ibmBackupLesAtmAddrValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmBackupLesAtmAddrValid.setStatus("mandatory")
_IbmBackupLesAtmAddr_Type = AtmLaneAddress
_IbmBackupLesAtmAddr_Object = MibTableColumn
ibmBackupLesAtmAddr = _IbmBackupLesAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2, 1, 2),
    _IbmBackupLesAtmAddr_Type()
)
ibmBackupLesAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmBackupLesAtmAddr.setStatus("mandatory")
_IbmElanLecsGroup_ObjectIdentity = ObjectIdentity
ibmElanLecsGroup = _IbmElanLecsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3)
)
_IbmElanLecsConfGroup_ObjectIdentity = ObjectIdentity
ibmElanLecsConfGroup = _IbmElanLecsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1)
)
_IbmLecsConfTable_Object = MibTable
ibmLecsConfTable = _IbmLecsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibmLecsConfTable.setStatus("mandatory")
_IbmLecsConfEntry_Object = MibTableRow
ibmLecsConfEntry = _IbmLecsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1)
)
ibmLecsConfEntry.setIndexNames(
    (0, "IBM-ELAN-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    ibmLecsConfEntry.setStatus("mandatory")


class _LecsUseBurnedInEsi_Type(TruthValue):
    """Custom type lecsUseBurnedInEsi based on TruthValue"""


_LecsUseBurnedInEsi_Object = MibTableColumn
lecsUseBurnedInEsi = _LecsUseBurnedInEsi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 1),
    _LecsUseBurnedInEsi_Type()
)
lecsUseBurnedInEsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsUseBurnedInEsi.setStatus("mandatory")
_LecsConfiguredEsi_Type = AtmPrivateAddrEsi
_LecsConfiguredEsi_Object = MibTableColumn
lecsConfiguredEsi = _LecsConfiguredEsi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 2),
    _LecsConfiguredEsi_Type()
)
lecsConfiguredEsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsConfiguredEsi.setStatus("mandatory")
_LecsConfiguredSelector_Type = AtmSelector
_LecsConfiguredSelector_Object = MibTableColumn
lecsConfiguredSelector = _LecsConfiguredSelector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 3),
    _LecsConfiguredSelector_Type()
)
lecsConfiguredSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsConfiguredSelector.setStatus("mandatory")
_LecsValidateBestEffortPcr_Type = TruthValue
_LecsValidateBestEffortPcr_Object = MibTableColumn
lecsValidateBestEffortPcr = _LecsValidateBestEffortPcr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 4),
    _LecsValidateBestEffortPcr_Type()
)
lecsValidateBestEffortPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsValidateBestEffortPcr.setStatus("mandatory")


class _ConfigDirectMaxReservedBw_Type(Integer32):
    """Custom type configDirectMaxReservedBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000),
    )


_ConfigDirectMaxReservedBw_Type.__name__ = "Integer32"
_ConfigDirectMaxReservedBw_Object = MibTableColumn
configDirectMaxReservedBw = _ConfigDirectMaxReservedBw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 5),
    _ConfigDirectMaxReservedBw_Type()
)
configDirectMaxReservedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDirectMaxReservedBw.setStatus("mandatory")
_AtmDevLineSpeed_Type = Unsigned32
_AtmDevLineSpeed_Object = MibTableColumn
atmDevLineSpeed = _AtmDevLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 6),
    _AtmDevLineSpeed_Type()
)
atmDevLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDevLineSpeed.setStatus("mandatory")


class _IdleVccTime_Type(Unsigned32):
    """Custom type idleVccTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 43200),
    )


_IdleVccTime_Type.__name__ = "Unsigned32"
_IdleVccTime_Object = MibTableColumn
idleVccTime = _IdleVccTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 7),
    _IdleVccTime_Type()
)
idleVccTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleVccTime.setStatus("mandatory")


class _LecsMaxVccs_Type(Unsigned32):
    """Custom type lecsMaxVccs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LecsMaxVccs_Type.__name__ = "Unsigned32"
_LecsMaxVccs_Object = MibTableColumn
lecsMaxVccs = _LecsMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 8),
    _LecsMaxVccs_Type()
)
lecsMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsMaxVccs.setStatus("mandatory")


class _LecsDomainName_Type(DisplayString):
    """Custom type lecsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecsDomainName_Type.__name__ = "DisplayString"
_LecsDomainName_Object = MibTableColumn
lecsDomainName = _LecsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 9),
    _LecsDomainName_Type()
)
lecsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsDomainName.setStatus("mandatory")
_IbmElanMIBConformance_ObjectIdentity = ObjectIdentity
ibmElanMIBConformance = _IbmElanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4)
)
_IbmElanMIBGroups_ObjectIdentity = ObjectIdentity
ibmElanMIBGroups = _IbmElanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 1)
)
_IbmElanCConfGroup_ObjectIdentity = ObjectIdentity
ibmElanCConfGroup = _IbmElanCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 1, 1)
)
_IbmLecsCGroup_ObjectIdentity = ObjectIdentity
ibmLecsCGroup = _IbmLecsCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 1, 2)
)
_IbmElanMIBCompliances_ObjectIdentity = ObjectIdentity
ibmElanMIBCompliances = _IbmElanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 2)
)
_IbmElanMIBCompliance_ObjectIdentity = ObjectIdentity
ibmElanMIBCompliance = _IbmElanMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-ELAN-MIB",
    **{"ibmElanMIB": ibmElanMIB,
       "ibmElanAdminGroup": ibmElanAdminGroup,
       "ibmElanConfGroup": ibmElanConfGroup,
       "ibmElanLesTable": ibmElanLesTable,
       "ibmElanLesEntry": ibmElanLesEntry,
       "ibmBackupLesAtmAddrValid": ibmBackupLesAtmAddrValid,
       "ibmBackupLesAtmAddr": ibmBackupLesAtmAddr,
       "ibmElanLecsGroup": ibmElanLecsGroup,
       "ibmElanLecsConfGroup": ibmElanLecsConfGroup,
       "ibmLecsConfTable": ibmLecsConfTable,
       "ibmLecsConfEntry": ibmLecsConfEntry,
       "lecsUseBurnedInEsi": lecsUseBurnedInEsi,
       "lecsConfiguredEsi": lecsConfiguredEsi,
       "lecsConfiguredSelector": lecsConfiguredSelector,
       "lecsValidateBestEffortPcr": lecsValidateBestEffortPcr,
       "configDirectMaxReservedBw": configDirectMaxReservedBw,
       "atmDevLineSpeed": atmDevLineSpeed,
       "idleVccTime": idleVccTime,
       "lecsMaxVccs": lecsMaxVccs,
       "lecsDomainName": lecsDomainName,
       "ibmElanMIBConformance": ibmElanMIBConformance,
       "ibmElanMIBGroups": ibmElanMIBGroups,
       "ibmElanCConfGroup": ibmElanCConfGroup,
       "ibmLecsCGroup": ibmLecsCGroup,
       "ibmElanMIBCompliances": ibmElanMIBCompliances,
       "ibmElanMIBCompliance": ibmElanMIBCompliance}
)
