# SNMP MIB module (MICOM-MPANL-LMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-MPANL-LMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:44 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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

_Micom_mlmi_ObjectIdentity = ObjectIdentity
micom_mlmi = _Micom_mlmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20)
)
_Mlmi_configuration_ObjectIdentity = ObjectIdentity
mlmi_configuration = _Mlmi_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1)
)


class _McmMLMIGenCfg4400Type_Type(Integer32):
    """Custom type mcmMLMIGenCfg4400Type based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("micom-4400", 1),
          ("nortel-DPN-4400", 2))
    )


_McmMLMIGenCfg4400Type_Type.__name__ = "Integer32"
_McmMLMIGenCfg4400Type_Object = MibScalar
mcmMLMIGenCfg4400Type = _McmMLMIGenCfg4400Type_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 1),
    _McmMLMIGenCfg4400Type_Type()
)
mcmMLMIGenCfg4400Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIGenCfg4400Type.setStatus("obsolete")


class _McmMLMIGenCfgSoftwareRev_Type(DisplayString):
    """Custom type mcmMLMIGenCfgSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_McmMLMIGenCfgSoftwareRev_Type.__name__ = "DisplayString"
_McmMLMIGenCfgSoftwareRev_Object = MibScalar
mcmMLMIGenCfgSoftwareRev = _McmMLMIGenCfgSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 2),
    _McmMLMIGenCfgSoftwareRev_Type()
)
mcmMLMIGenCfgSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIGenCfgSoftwareRev.setStatus("mandatory")
_McmMLMIServiceTable_Object = MibTable
mcmMLMIServiceTable = _McmMLMIServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3)
)
if mibBuilder.loadTexts:
    mcmMLMIServiceTable.setStatus("mandatory")
_McmMLMIServiceEntry_Object = MibTableRow
mcmMLMIServiceEntry = _McmMLMIServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1)
)
mcmMLMIServiceEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMIServiceIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMLMIServiceEntry.setStatus("mandatory")


class _McmMLMIServiceIfIndex_Type(Integer32):
    """Custom type mcmMLMIServiceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMLMIServiceIfIndex_Type.__name__ = "Integer32"
_McmMLMIServiceIfIndex_Object = MibTableColumn
mcmMLMIServiceIfIndex = _McmMLMIServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 1),
    _McmMLMIServiceIfIndex_Type()
)
mcmMLMIServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIServiceIfIndex.setStatus("mandatory")


class _McmMLMIServiceCUGFacility_Type(Integer32):
    """Custom type mcmMLMIServiceCUGFacility based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cUG-selection", 3),
          ("no-CUG", 1),
          ("simple-CUG", 2))
    )


_McmMLMIServiceCUGFacility_Type.__name__ = "Integer32"
_McmMLMIServiceCUGFacility_Object = MibTableColumn
mcmMLMIServiceCUGFacility = _McmMLMIServiceCUGFacility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 2),
    _McmMLMIServiceCUGFacility_Type()
)
mcmMLMIServiceCUGFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIServiceCUGFacility.setStatus("mandatory")


class _McmMLMIServiceCUGAccess_Type(Integer32):
    """Custom type mcmMLMIServiceCUGAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("incoming-access-right", 3),
          ("incoming-outgoing-access-right", 4),
          ("no-right", 1),
          ("outgoing-access-right", 2))
    )


_McmMLMIServiceCUGAccess_Type.__name__ = "Integer32"
_McmMLMIServiceCUGAccess_Object = MibTableColumn
mcmMLMIServiceCUGAccess = _McmMLMIServiceCUGAccess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 3),
    _McmMLMIServiceCUGAccess_Type()
)
mcmMLMIServiceCUGAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIServiceCUGAccess.setStatus("mandatory")


class _McmMLMIServiceCUGICType_Type(Integer32):
    """Custom type mcmMLMIServiceCUGICType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international-IC", 2),
          ("national-IC", 1))
    )


_McmMLMIServiceCUGICType_Type.__name__ = "Integer32"
_McmMLMIServiceCUGICType_Object = MibTableColumn
mcmMLMIServiceCUGICType = _McmMLMIServiceCUGICType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 4),
    _McmMLMIServiceCUGICType_Type()
)
mcmMLMIServiceCUGICType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIServiceCUGICType.setStatus("mandatory")


class _McmMLMIServiceCUGIC_Type(DisplayString):
    """Custom type mcmMLMIServiceCUGIC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_McmMLMIServiceCUGIC_Type.__name__ = "DisplayString"
_McmMLMIServiceCUGIC_Object = MibTableColumn
mcmMLMIServiceCUGIC = _McmMLMIServiceCUGIC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 5),
    _McmMLMIServiceCUGIC_Type()
)
mcmMLMIServiceCUGIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIServiceCUGIC.setStatus("mandatory")


class _McmMLMIServiceDNASuffix_Type(DisplayString):
    """Custom type mcmMLMIServiceDNASuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_McmMLMIServiceDNASuffix_Type.__name__ = "DisplayString"
_McmMLMIServiceDNASuffix_Object = MibTableColumn
mcmMLMIServiceDNASuffix = _McmMLMIServiceDNASuffix_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 6),
    _McmMLMIServiceDNASuffix_Type()
)
mcmMLMIServiceDNASuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIServiceDNASuffix.setStatus("mandatory")


class _NvmMLMIGenCfg4400Type_Type(Integer32):
    """Custom type nvmMLMIGenCfg4400Type based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("micom-4400", 1),
          ("nortel-DPN-4400", 2))
    )


_NvmMLMIGenCfg4400Type_Type.__name__ = "Integer32"
_NvmMLMIGenCfg4400Type_Object = MibScalar
nvmMLMIGenCfg4400Type = _NvmMLMIGenCfg4400Type_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 4),
    _NvmMLMIGenCfg4400Type_Type()
)
nvmMLMIGenCfg4400Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIGenCfg4400Type.setStatus("obsolete")
_NvmMLMIServiceTable_Object = MibTable
nvmMLMIServiceTable = _NvmMLMIServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5)
)
if mibBuilder.loadTexts:
    nvmMLMIServiceTable.setStatus("mandatory")
_NvmMLMIServiceEntry_Object = MibTableRow
nvmMLMIServiceEntry = _NvmMLMIServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1)
)
nvmMLMIServiceEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "nvmMLMIServiceIfIndex"),
)
if mibBuilder.loadTexts:
    nvmMLMIServiceEntry.setStatus("mandatory")


class _NvmMLMIServiceIfIndex_Type(Integer32):
    """Custom type nvmMLMIServiceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmMLMIServiceIfIndex_Type.__name__ = "Integer32"
_NvmMLMIServiceIfIndex_Object = MibTableColumn
nvmMLMIServiceIfIndex = _NvmMLMIServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 1),
    _NvmMLMIServiceIfIndex_Type()
)
nvmMLMIServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmMLMIServiceIfIndex.setStatus("mandatory")


class _NvmMLMIServiceCUGFacility_Type(Integer32):
    """Custom type nvmMLMIServiceCUGFacility based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cUG-selection", 3),
          ("no-CUG", 1),
          ("simple-CUG", 2))
    )


_NvmMLMIServiceCUGFacility_Type.__name__ = "Integer32"
_NvmMLMIServiceCUGFacility_Object = MibTableColumn
nvmMLMIServiceCUGFacility = _NvmMLMIServiceCUGFacility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 2),
    _NvmMLMIServiceCUGFacility_Type()
)
nvmMLMIServiceCUGFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIServiceCUGFacility.setStatus("mandatory")


class _NvmMLMIServiceCUGAccess_Type(Integer32):
    """Custom type nvmMLMIServiceCUGAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("incoming-access-right", 3),
          ("incoming-outgoing-access-right", 4),
          ("no-right", 1),
          ("outgoing-access-right", 2))
    )


_NvmMLMIServiceCUGAccess_Type.__name__ = "Integer32"
_NvmMLMIServiceCUGAccess_Object = MibTableColumn
nvmMLMIServiceCUGAccess = _NvmMLMIServiceCUGAccess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 3),
    _NvmMLMIServiceCUGAccess_Type()
)
nvmMLMIServiceCUGAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIServiceCUGAccess.setStatus("mandatory")


class _NvmMLMIServiceCUGICType_Type(Integer32):
    """Custom type nvmMLMIServiceCUGICType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international-IC", 2),
          ("national-IC", 1))
    )


_NvmMLMIServiceCUGICType_Type.__name__ = "Integer32"
_NvmMLMIServiceCUGICType_Object = MibTableColumn
nvmMLMIServiceCUGICType = _NvmMLMIServiceCUGICType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 4),
    _NvmMLMIServiceCUGICType_Type()
)
nvmMLMIServiceCUGICType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIServiceCUGICType.setStatus("mandatory")


class _NvmMLMIServiceCUGIC_Type(DisplayString):
    """Custom type nvmMLMIServiceCUGIC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_NvmMLMIServiceCUGIC_Type.__name__ = "DisplayString"
_NvmMLMIServiceCUGIC_Object = MibTableColumn
nvmMLMIServiceCUGIC = _NvmMLMIServiceCUGIC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 5),
    _NvmMLMIServiceCUGIC_Type()
)
nvmMLMIServiceCUGIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIServiceCUGIC.setStatus("mandatory")


class _NvmMLMIServiceDNASuffix_Type(DisplayString):
    """Custom type nvmMLMIServiceDNASuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_NvmMLMIServiceDNASuffix_Type.__name__ = "DisplayString"
_NvmMLMIServiceDNASuffix_Object = MibTableColumn
nvmMLMIServiceDNASuffix = _NvmMLMIServiceDNASuffix_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 6),
    _NvmMLMIServiceDNASuffix_Type()
)
nvmMLMIServiceDNASuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIServiceDNASuffix.setStatus("mandatory")


class _NvmMLMIServiceRowStatus_Type(Integer32):
    """Custom type nvmMLMIServiceRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NvmMLMIServiceRowStatus_Type.__name__ = "Integer32"
_NvmMLMIServiceRowStatus_Object = MibTableColumn
nvmMLMIServiceRowStatus = _NvmMLMIServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 7),
    _NvmMLMIServiceRowStatus_Type()
)
nvmMLMIServiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMIServiceRowStatus.setStatus("mandatory")
_McmMLMINetlinkTable_Object = MibTable
mcmMLMINetlinkTable = _McmMLMINetlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6)
)
if mibBuilder.loadTexts:
    mcmMLMINetlinkTable.setStatus("mandatory")
_McmMLMINetlinkEntry_Object = MibTableRow
mcmMLMINetlinkEntry = _McmMLMINetlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1)
)
mcmMLMINetlinkEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMLMINetlinkEntry.setStatus("mandatory")


class _McmMLMINetlinkIfIndex_Type(Integer32):
    """Custom type mcmMLMINetlinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMLMINetlinkIfIndex_Type.__name__ = "Integer32"
_McmMLMINetlinkIfIndex_Object = MibTableColumn
mcmMLMINetlinkIfIndex = _McmMLMINetlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 1),
    _McmMLMINetlinkIfIndex_Type()
)
mcmMLMINetlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkIfIndex.setStatus("mandatory")


class _McmMLMINetlinkTunnelingPVCDlci_Type(Integer32):
    """Custom type mcmMLMINetlinkTunnelingPVCDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmMLMINetlinkTunnelingPVCDlci_Type.__name__ = "Integer32"
_McmMLMINetlinkTunnelingPVCDlci_Object = MibTableColumn
mcmMLMINetlinkTunnelingPVCDlci = _McmMLMINetlinkTunnelingPVCDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 2),
    _McmMLMINetlinkTunnelingPVCDlci_Type()
)
mcmMLMINetlinkTunnelingPVCDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkTunnelingPVCDlci.setStatus("mandatory")


class _McmMLMINetlinkMpanlMode_Type(Integer32):
    """Custom type mcmMLMINetlinkMpanlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_McmMLMINetlinkMpanlMode_Type.__name__ = "Integer32"
_McmMLMINetlinkMpanlMode_Object = MibTableColumn
mcmMLMINetlinkMpanlMode = _McmMLMINetlinkMpanlMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 3),
    _McmMLMINetlinkMpanlMode_Type()
)
mcmMLMINetlinkMpanlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkMpanlMode.setStatus("mandatory")


class _McmMLMINetlinkDLCIAssignMethod_Type(Integer32):
    """Custom type mcmMLMINetlinkDLCIAssignMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 2),
          ("increment", 1))
    )


_McmMLMINetlinkDLCIAssignMethod_Type.__name__ = "Integer32"
_McmMLMINetlinkDLCIAssignMethod_Object = MibTableColumn
mcmMLMINetlinkDLCIAssignMethod = _McmMLMINetlinkDLCIAssignMethod_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 4),
    _McmMLMINetlinkDLCIAssignMethod_Type()
)
mcmMLMINetlinkDLCIAssignMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkDLCIAssignMethod.setStatus("mandatory")


class _McmMLMINetlinkRstrtT316Timer_Type(Integer32):
    """Custom type mcmMLMINetlinkRstrtT316Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_McmMLMINetlinkRstrtT316Timer_Type.__name__ = "Integer32"
_McmMLMINetlinkRstrtT316Timer_Object = MibTableColumn
mcmMLMINetlinkRstrtT316Timer = _McmMLMINetlinkRstrtT316Timer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 5),
    _McmMLMINetlinkRstrtT316Timer_Type()
)
mcmMLMINetlinkRstrtT316Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkRstrtT316Timer.setStatus("mandatory")


class _McmMLMINetlinkRstrtAckT317Timer_Type(Integer32):
    """Custom type mcmMLMINetlinkRstrtAckT317Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_McmMLMINetlinkRstrtAckT317Timer_Type.__name__ = "Integer32"
_McmMLMINetlinkRstrtAckT317Timer_Object = MibTableColumn
mcmMLMINetlinkRstrtAckT317Timer = _McmMLMINetlinkRstrtAckT317Timer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 6),
    _McmMLMINetlinkRstrtAckT317Timer_Type()
)
mcmMLMINetlinkRstrtAckT317Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkRstrtAckT317Timer.setStatus("mandatory")


class _McmMLMINetlinkNumUnsuccesRstrtAtmpts_Type(Integer32):
    """Custom type mcmMLMINetlinkNumUnsuccesRstrtAtmpts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmMLMINetlinkNumUnsuccesRstrtAtmpts_Type.__name__ = "Integer32"
_McmMLMINetlinkNumUnsuccesRstrtAtmpts_Object = MibTableColumn
mcmMLMINetlinkNumUnsuccesRstrtAtmpts = _McmMLMINetlinkNumUnsuccesRstrtAtmpts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 7),
    _McmMLMINetlinkNumUnsuccesRstrtAtmpts_Type()
)
mcmMLMINetlinkNumUnsuccesRstrtAtmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkNumUnsuccesRstrtAtmpts.setStatus("mandatory")
_NvmMLMINetlinkTable_Object = MibTable
nvmMLMINetlinkTable = _NvmMLMINetlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7)
)
if mibBuilder.loadTexts:
    nvmMLMINetlinkTable.setStatus("mandatory")
_NvmMLMINetlinkEntry_Object = MibTableRow
nvmMLMINetlinkEntry = _NvmMLMINetlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1)
)
nvmMLMINetlinkEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "nvmMLMINetlinkIfIndex"),
)
if mibBuilder.loadTexts:
    nvmMLMINetlinkEntry.setStatus("mandatory")


class _NvmMLMINetlinkIfIndex_Type(Integer32):
    """Custom type nvmMLMINetlinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmMLMINetlinkIfIndex_Type.__name__ = "Integer32"
_NvmMLMINetlinkIfIndex_Object = MibTableColumn
nvmMLMINetlinkIfIndex = _NvmMLMINetlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 1),
    _NvmMLMINetlinkIfIndex_Type()
)
nvmMLMINetlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmMLMINetlinkIfIndex.setStatus("mandatory")


class _NvmMLMINetlinkTunnelingPVCDlci_Type(Integer32):
    """Custom type nvmMLMINetlinkTunnelingPVCDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NvmMLMINetlinkTunnelingPVCDlci_Type.__name__ = "Integer32"
_NvmMLMINetlinkTunnelingPVCDlci_Object = MibTableColumn
nvmMLMINetlinkTunnelingPVCDlci = _NvmMLMINetlinkTunnelingPVCDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 2),
    _NvmMLMINetlinkTunnelingPVCDlci_Type()
)
nvmMLMINetlinkTunnelingPVCDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmMLMINetlinkTunnelingPVCDlci.setStatus("mandatory")


class _NvmMLMINetlinkDLCIAssignMethod_Type(Integer32):
    """Custom type nvmMLMINetlinkDLCIAssignMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 2),
          ("increment", 1))
    )


_NvmMLMINetlinkDLCIAssignMethod_Type.__name__ = "Integer32"
_NvmMLMINetlinkDLCIAssignMethod_Object = MibTableColumn
nvmMLMINetlinkDLCIAssignMethod = _NvmMLMINetlinkDLCIAssignMethod_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 3),
    _NvmMLMINetlinkDLCIAssignMethod_Type()
)
nvmMLMINetlinkDLCIAssignMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMINetlinkDLCIAssignMethod.setStatus("mandatory")


class _NvmMLMINetlinkRstrtT316Timer_Type(Integer32):
    """Custom type nvmMLMINetlinkRstrtT316Timer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NvmMLMINetlinkRstrtT316Timer_Type.__name__ = "Integer32"
_NvmMLMINetlinkRstrtT316Timer_Object = MibTableColumn
nvmMLMINetlinkRstrtT316Timer = _NvmMLMINetlinkRstrtT316Timer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 4),
    _NvmMLMINetlinkRstrtT316Timer_Type()
)
nvmMLMINetlinkRstrtT316Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMINetlinkRstrtT316Timer.setStatus("mandatory")


class _NvmMLMINetlinkRstrtAckT317Timer_Type(Integer32):
    """Custom type nvmMLMINetlinkRstrtAckT317Timer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NvmMLMINetlinkRstrtAckT317Timer_Type.__name__ = "Integer32"
_NvmMLMINetlinkRstrtAckT317Timer_Object = MibTableColumn
nvmMLMINetlinkRstrtAckT317Timer = _NvmMLMINetlinkRstrtAckT317Timer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 5),
    _NvmMLMINetlinkRstrtAckT317Timer_Type()
)
nvmMLMINetlinkRstrtAckT317Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMINetlinkRstrtAckT317Timer.setStatus("mandatory")


class _NvmMLMINetlinkNumUnsuccesRstrtAtmpts_Type(Integer32):
    """Custom type nvmMLMINetlinkNumUnsuccesRstrtAtmpts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmMLMINetlinkNumUnsuccesRstrtAtmpts_Type.__name__ = "Integer32"
_NvmMLMINetlinkNumUnsuccesRstrtAtmpts_Object = MibTableColumn
nvmMLMINetlinkNumUnsuccesRstrtAtmpts = _NvmMLMINetlinkNumUnsuccesRstrtAtmpts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 6),
    _NvmMLMINetlinkNumUnsuccesRstrtAtmpts_Type()
)
nvmMLMINetlinkNumUnsuccesRstrtAtmpts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmMLMINetlinkNumUnsuccesRstrtAtmpts.setStatus("mandatory")
_Mlmi_control_ObjectIdentity = ObjectIdentity
mlmi_control = _Mlmi_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 2)
)


class _McmMLMICntrAction_Type(Integer32):
    """Custom type mcmMLMICntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmMLMICntrAction_Type.__name__ = "Integer32"
_McmMLMICntrAction_Object = MibScalar
mcmMLMICntrAction = _McmMLMICntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 2, 1),
    _McmMLMICntrAction_Type()
)
mcmMLMICntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmMLMICntrAction.setStatus("obsolete")
_Mlmi_statistics_ObjectIdentity = ObjectIdentity
mlmi_statistics = _Mlmi_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3)
)
_McmMLMIStatsActiveVCs_Type = Counter32
_McmMLMIStatsActiveVCs_Object = MibScalar
mcmMLMIStatsActiveVCs = _McmMLMIStatsActiveVCs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 1),
    _McmMLMIStatsActiveVCs_Type()
)
mcmMLMIStatsActiveVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsActiveVCs.setStatus("mandatory")
_McmMLMIStatsRequestedCalls_Type = Counter32
_McmMLMIStatsRequestedCalls_Object = MibScalar
mcmMLMIStatsRequestedCalls = _McmMLMIStatsRequestedCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 2),
    _McmMLMIStatsRequestedCalls_Type()
)
mcmMLMIStatsRequestedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsRequestedCalls.setStatus("mandatory")
_McmMLMIStatsInitiatedCalls_Type = Counter32
_McmMLMIStatsInitiatedCalls_Object = MibScalar
mcmMLMIStatsInitiatedCalls = _McmMLMIStatsInitiatedCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 3),
    _McmMLMIStatsInitiatedCalls_Type()
)
mcmMLMIStatsInitiatedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsInitiatedCalls.setStatus("mandatory")
_McmMLMIStatsFailedCalls_Type = Counter32
_McmMLMIStatsFailedCalls_Object = MibScalar
mcmMLMIStatsFailedCalls = _McmMLMIStatsFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 4),
    _McmMLMIStatsFailedCalls_Type()
)
mcmMLMIStatsFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsFailedCalls.setStatus("mandatory")
_McmMLMIStatsSucceededCalls_Type = Counter32
_McmMLMIStatsSucceededCalls_Object = MibScalar
mcmMLMIStatsSucceededCalls = _McmMLMIStatsSucceededCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 5),
    _McmMLMIStatsSucceededCalls_Type()
)
mcmMLMIStatsSucceededCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsSucceededCalls.setStatus("mandatory")
_McmMLMIStatsReleasedCalls_Type = Counter32
_McmMLMIStatsReleasedCalls_Object = MibScalar
mcmMLMIStatsReleasedCalls = _McmMLMIStatsReleasedCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 6),
    _McmMLMIStatsReleasedCalls_Type()
)
mcmMLMIStatsReleasedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsReleasedCalls.setStatus("mandatory")
_McmMLMIStatsDisconnectedCalls_Type = Counter32
_McmMLMIStatsDisconnectedCalls_Object = MibScalar
mcmMLMIStatsDisconnectedCalls = _McmMLMIStatsDisconnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 7),
    _McmMLMIStatsDisconnectedCalls_Type()
)
mcmMLMIStatsDisconnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsDisconnectedCalls.setStatus("mandatory")
_McmMLMIStatsAdmittedCUGs_Type = Counter32
_McmMLMIStatsAdmittedCUGs_Object = MibScalar
mcmMLMIStatsAdmittedCUGs = _McmMLMIStatsAdmittedCUGs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 8),
    _McmMLMIStatsAdmittedCUGs_Type()
)
mcmMLMIStatsAdmittedCUGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsAdmittedCUGs.setStatus("mandatory")
_McmMLMIStatsRejectedCUGs_Type = Counter32
_McmMLMIStatsRejectedCUGs_Object = MibScalar
mcmMLMIStatsRejectedCUGs = _McmMLMIStatsRejectedCUGs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 9),
    _McmMLMIStatsRejectedCUGs_Type()
)
mcmMLMIStatsRejectedCUGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMIStatsRejectedCUGs.setStatus("mandatory")
_McmMLMINetlinkStatTable_Object = MibTable
mcmMLMINetlinkStatTable = _McmMLMINetlinkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10)
)
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatTable.setStatus("mandatory")
_McmMLMINetlinkStatEntry_Object = MibTableRow
mcmMLMINetlinkStatEntry = _McmMLMINetlinkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1)
)
mcmMLMINetlinkStatEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkStatIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatEntry.setStatus("mandatory")


class _McmMLMINetlinkStatIfIndex_Type(Integer32):
    """Custom type mcmMLMINetlinkStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMLMINetlinkStatIfIndex_Type.__name__ = "Integer32"
_McmMLMINetlinkStatIfIndex_Object = MibTableColumn
mcmMLMINetlinkStatIfIndex = _McmMLMINetlinkStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 1),
    _McmMLMINetlinkStatIfIndex_Type()
)
mcmMLMINetlinkStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatIfIndex.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxSetup_Type = Counter32
_McmMLMINetlinkStatMsgRxSetup_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxSetup = _McmMLMINetlinkStatMsgRxSetup_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 2),
    _McmMLMINetlinkStatMsgRxSetup_Type()
)
mcmMLMINetlinkStatMsgRxSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxSetup.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxSetup_Type = Counter32
_McmMLMINetlinkStatMsgTxSetup_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxSetup = _McmMLMINetlinkStatMsgTxSetup_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 3),
    _McmMLMINetlinkStatMsgTxSetup_Type()
)
mcmMLMINetlinkStatMsgTxSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxSetup.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxCallPrcdngs_Type = Counter32
_McmMLMINetlinkStatMsgRxCallPrcdngs_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxCallPrcdngs = _McmMLMINetlinkStatMsgRxCallPrcdngs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 4),
    _McmMLMINetlinkStatMsgRxCallPrcdngs_Type()
)
mcmMLMINetlinkStatMsgRxCallPrcdngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxCallPrcdngs.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxCallPrcdngs_Type = Counter32
_McmMLMINetlinkStatMsgTxCallPrcdngs_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxCallPrcdngs = _McmMLMINetlinkStatMsgTxCallPrcdngs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 5),
    _McmMLMINetlinkStatMsgTxCallPrcdngs_Type()
)
mcmMLMINetlinkStatMsgTxCallPrcdngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxCallPrcdngs.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxConn_Type = Counter32
_McmMLMINetlinkStatMsgRxConn_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxConn = _McmMLMINetlinkStatMsgRxConn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 6),
    _McmMLMINetlinkStatMsgRxConn_Type()
)
mcmMLMINetlinkStatMsgRxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxConn.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxConn_Type = Counter32
_McmMLMINetlinkStatMsgTxConn_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxConn = _McmMLMINetlinkStatMsgTxConn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 7),
    _McmMLMINetlinkStatMsgTxConn_Type()
)
mcmMLMINetlinkStatMsgTxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxConn.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxDisConn_Type = Counter32
_McmMLMINetlinkStatMsgRxDisConn_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxDisConn = _McmMLMINetlinkStatMsgRxDisConn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 8),
    _McmMLMINetlinkStatMsgRxDisConn_Type()
)
mcmMLMINetlinkStatMsgRxDisConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxDisConn.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxDisConn_Type = Counter32
_McmMLMINetlinkStatMsgTxDisConn_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxDisConn = _McmMLMINetlinkStatMsgTxDisConn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 9),
    _McmMLMINetlinkStatMsgTxDisConn_Type()
)
mcmMLMINetlinkStatMsgTxDisConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxDisConn.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxRls_Type = Counter32
_McmMLMINetlinkStatMsgRxRls_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxRls = _McmMLMINetlinkStatMsgRxRls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 10),
    _McmMLMINetlinkStatMsgRxRls_Type()
)
mcmMLMINetlinkStatMsgRxRls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxRls.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxRls_Type = Counter32
_McmMLMINetlinkStatMsgTxRls_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxRls = _McmMLMINetlinkStatMsgTxRls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 11),
    _McmMLMINetlinkStatMsgTxRls_Type()
)
mcmMLMINetlinkStatMsgTxRls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxRls.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxRlseComp_Type = Counter32
_McmMLMINetlinkStatMsgRxRlseComp_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxRlseComp = _McmMLMINetlinkStatMsgRxRlseComp_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 12),
    _McmMLMINetlinkStatMsgRxRlseComp_Type()
)
mcmMLMINetlinkStatMsgRxRlseComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxRlseComp.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxRlseComp_Type = Counter32
_McmMLMINetlinkStatMsgTxRlseComp_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxRlseComp = _McmMLMINetlinkStatMsgTxRlseComp_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 13),
    _McmMLMINetlinkStatMsgTxRlseComp_Type()
)
mcmMLMINetlinkStatMsgTxRlseComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxRlseComp.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxStatusInq_Type = Counter32
_McmMLMINetlinkStatMsgRxStatusInq_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxStatusInq = _McmMLMINetlinkStatMsgRxStatusInq_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 14),
    _McmMLMINetlinkStatMsgRxStatusInq_Type()
)
mcmMLMINetlinkStatMsgRxStatusInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxStatusInq.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxStatusInq_Type = Counter32
_McmMLMINetlinkStatMsgTxStatusInq_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxStatusInq = _McmMLMINetlinkStatMsgTxStatusInq_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 15),
    _McmMLMINetlinkStatMsgTxStatusInq_Type()
)
mcmMLMINetlinkStatMsgTxStatusInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxStatusInq.setStatus("mandatory")
_McmMLMINetlinkStatMsgRxStatus_Type = Counter32
_McmMLMINetlinkStatMsgRxStatus_Object = MibTableColumn
mcmMLMINetlinkStatMsgRxStatus = _McmMLMINetlinkStatMsgRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 16),
    _McmMLMINetlinkStatMsgRxStatus_Type()
)
mcmMLMINetlinkStatMsgRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgRxStatus.setStatus("mandatory")
_McmMLMINetlinkStatMsgTxStatus_Type = Counter32
_McmMLMINetlinkStatMsgTxStatus_Object = MibTableColumn
mcmMLMINetlinkStatMsgTxStatus = _McmMLMINetlinkStatMsgTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 17),
    _McmMLMINetlinkStatMsgTxStatus_Type()
)
mcmMLMINetlinkStatMsgTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatMsgTxStatus.setStatus("mandatory")
_McmMLMINetlinkStatLocalSVC_Type = Counter32
_McmMLMINetlinkStatLocalSVC_Object = MibTableColumn
mcmMLMINetlinkStatLocalSVC = _McmMLMINetlinkStatLocalSVC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 18),
    _McmMLMINetlinkStatLocalSVC_Type()
)
mcmMLMINetlinkStatLocalSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatLocalSVC.setStatus("mandatory")
_McmMLMINetlinkStatTransitSVC_Type = Counter32
_McmMLMINetlinkStatTransitSVC_Object = MibTableColumn
mcmMLMINetlinkStatTransitSVC = _McmMLMINetlinkStatTransitSVC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 19),
    _McmMLMINetlinkStatTransitSVC_Type()
)
mcmMLMINetlinkStatTransitSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatTransitSVC.setStatus("mandatory")
_McmMLMINetlinkStatVoiceCalls_Type = Counter32
_McmMLMINetlinkStatVoiceCalls_Object = MibTableColumn
mcmMLMINetlinkStatVoiceCalls = _McmMLMINetlinkStatVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 20),
    _McmMLMINetlinkStatVoiceCalls_Type()
)
mcmMLMINetlinkStatVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatVoiceCalls.setStatus("mandatory")
_McmMLMINetlinkStatLanCalls_Type = Counter32
_McmMLMINetlinkStatLanCalls_Object = MibTableColumn
mcmMLMINetlinkStatLanCalls = _McmMLMINetlinkStatLanCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 21),
    _McmMLMINetlinkStatLanCalls_Type()
)
mcmMLMINetlinkStatLanCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatLanCalls.setStatus("mandatory")
_McmMLMINetlinkStatRsiCalls_Type = Counter32
_McmMLMINetlinkStatRsiCalls_Object = MibTableColumn
mcmMLMINetlinkStatRsiCalls = _McmMLMINetlinkStatRsiCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 22),
    _McmMLMINetlinkStatRsiCalls_Type()
)
mcmMLMINetlinkStatRsiCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatRsiCalls.setStatus("mandatory")
_McmMLMINetlinkStatSpvcCalls_Type = Counter32
_McmMLMINetlinkStatSpvcCalls_Object = MibTableColumn
mcmMLMINetlinkStatSpvcCalls = _McmMLMINetlinkStatSpvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 23),
    _McmMLMINetlinkStatSpvcCalls_Type()
)
mcmMLMINetlinkStatSpvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatSpvcCalls.setStatus("mandatory")
_McmMLMINetlinkStatLnkupCnt_Type = Counter32
_McmMLMINetlinkStatLnkupCnt_Object = MibTableColumn
mcmMLMINetlinkStatLnkupCnt = _McmMLMINetlinkStatLnkupCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 24),
    _McmMLMINetlinkStatLnkupCnt_Type()
)
mcmMLMINetlinkStatLnkupCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatLnkupCnt.setStatus("mandatory")
_McmMLMINetlinkStatLnkDownCnt_Type = Counter32
_McmMLMINetlinkStatLnkDownCnt_Object = MibTableColumn
mcmMLMINetlinkStatLnkDownCnt = _McmMLMINetlinkStatLnkDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 25),
    _McmMLMINetlinkStatLnkDownCnt_Type()
)
mcmMLMINetlinkStatLnkDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatLnkDownCnt.setStatus("mandatory")
_McmMLMICircuitStatTable_Object = MibTable
mcmMLMICircuitStatTable = _McmMLMICircuitStatTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11)
)
if mibBuilder.loadTexts:
    mcmMLMICircuitStatTable.setStatus("mandatory")
_McmMLMICircuitStatEntry_Object = MibTableRow
mcmMLMICircuitStatEntry = _McmMLMICircuitStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1)
)
mcmMLMICircuitStatEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatIfIndex"),
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatSVCDLCI"),
)
if mibBuilder.loadTexts:
    mcmMLMICircuitStatEntry.setStatus("mandatory")


class _McmMLMICircuitStatIfIndex_Type(Integer32):
    """Custom type mcmMLMICircuitStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMLMICircuitStatIfIndex_Type.__name__ = "Integer32"
_McmMLMICircuitStatIfIndex_Object = MibTableColumn
mcmMLMICircuitStatIfIndex = _McmMLMICircuitStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 1),
    _McmMLMICircuitStatIfIndex_Type()
)
mcmMLMICircuitStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatIfIndex.setStatus("mandatory")


class _McmMLMICircuitStatSVCDLCI_Type(Integer32):
    """Custom type mcmMLMICircuitStatSVCDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 991),
    )


_McmMLMICircuitStatSVCDLCI_Type.__name__ = "Integer32"
_McmMLMICircuitStatSVCDLCI_Object = MibTableColumn
mcmMLMICircuitStatSVCDLCI = _McmMLMICircuitStatSVCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 2),
    _McmMLMICircuitStatSVCDLCI_Type()
)
mcmMLMICircuitStatSVCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatSVCDLCI.setStatus("mandatory")
_McmMLMICircuitStatMsgRxStatus_Type = Counter32
_McmMLMICircuitStatMsgRxStatus_Object = MibTableColumn
mcmMLMICircuitStatMsgRxStatus = _McmMLMICircuitStatMsgRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 3),
    _McmMLMICircuitStatMsgRxStatus_Type()
)
mcmMLMICircuitStatMsgRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatMsgRxStatus.setStatus("mandatory")
_McmMLMICircuitStatMsgTxStatus_Type = Counter32
_McmMLMICircuitStatMsgTxStatus_Object = MibTableColumn
mcmMLMICircuitStatMsgTxStatus = _McmMLMICircuitStatMsgTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 4),
    _McmMLMICircuitStatMsgTxStatus_Type()
)
mcmMLMICircuitStatMsgTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatMsgTxStatus.setStatus("mandatory")
_McmMLMICircuitStatMsgRxStatusInq_Type = Counter32
_McmMLMICircuitStatMsgRxStatusInq_Object = MibTableColumn
mcmMLMICircuitStatMsgRxStatusInq = _McmMLMICircuitStatMsgRxStatusInq_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 5),
    _McmMLMICircuitStatMsgRxStatusInq_Type()
)
mcmMLMICircuitStatMsgRxStatusInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatMsgRxStatusInq.setStatus("mandatory")
_McmMLMICircuitStatMsgTxStatusInq_Type = Counter32
_McmMLMICircuitStatMsgTxStatusInq_Object = MibTableColumn
mcmMLMICircuitStatMsgTxStatusInq = _McmMLMICircuitStatMsgTxStatusInq_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 6),
    _McmMLMICircuitStatMsgTxStatusInq_Type()
)
mcmMLMICircuitStatMsgTxStatusInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatMsgTxStatusInq.setStatus("mandatory")
_Mlmi_status_ObjectIdentity = ObjectIdentity
mlmi_status = _Mlmi_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4)
)
_McmMLMINetlinkStatusTable_Object = MibTable
mcmMLMINetlinkStatusTable = _McmMLMINetlinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1)
)
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusTable.setStatus("mandatory")
_McmMLMINetlinkStatusEntry_Object = MibTableRow
mcmMLMINetlinkStatusEntry = _McmMLMINetlinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1)
)
mcmMLMINetlinkStatusEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkStatusIfIndex"),
)
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusEntry.setStatus("mandatory")


class _McmMLMINetlinkStatusIfIndex_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMLMINetlinkStatusIfIndex_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusIfIndex_Object = MibTableColumn
mcmMLMINetlinkStatusIfIndex = _McmMLMINetlinkStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 1),
    _McmMLMINetlinkStatusIfIndex_Type()
)
mcmMLMINetlinkStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusIfIndex.setStatus("mandatory")


class _McmMLMINetlinkStatusMPANLStatus_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusMPANLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_McmMLMINetlinkStatusMPANLStatus_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusMPANLStatus_Object = MibTableColumn
mcmMLMINetlinkStatusMPANLStatus = _McmMLMINetlinkStatusMPANLStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 2),
    _McmMLMINetlinkStatusMPANLStatus_Type()
)
mcmMLMINetlinkStatusMPANLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusMPANLStatus.setStatus("mandatory")


class _McmMLMINetlinkStatusRestartState_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusRestartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rstrtRqstReceived", 3),
          ("rstrtRqstSent", 2))
    )


_McmMLMINetlinkStatusRestartState_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusRestartState_Object = MibTableColumn
mcmMLMINetlinkStatusRestartState = _McmMLMINetlinkStatusRestartState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 3),
    _McmMLMINetlinkStatusRestartState_Type()
)
mcmMLMINetlinkStatusRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusRestartState.setStatus("mandatory")


class _McmMLMINetlinkStatusLAPFState_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusLAPFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_McmMLMINetlinkStatusLAPFState_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusLAPFState_Object = MibTableColumn
mcmMLMINetlinkStatusLAPFState = _McmMLMINetlinkStatusLAPFState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 4),
    _McmMLMINetlinkStatusLAPFState_Type()
)
mcmMLMINetlinkStatusLAPFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusLAPFState.setStatus("mandatory")


class _McmMLMINetlinkStatusFrCoreState_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusFrCoreState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_McmMLMINetlinkStatusFrCoreState_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusFrCoreState_Object = MibTableColumn
mcmMLMINetlinkStatusFrCoreState = _McmMLMINetlinkStatusFrCoreState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 5),
    _McmMLMINetlinkStatusFrCoreState_Type()
)
mcmMLMINetlinkStatusFrCoreState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusFrCoreState.setStatus("mandatory")


class _McmMLMINetlinkStatusTxThrput_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusTxThrput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMINetlinkStatusTxThrput_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusTxThrput_Object = MibTableColumn
mcmMLMINetlinkStatusTxThrput = _McmMLMINetlinkStatusTxThrput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 6),
    _McmMLMINetlinkStatusTxThrput_Type()
)
mcmMLMINetlinkStatusTxThrput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusTxThrput.setStatus("obsolete")


class _McmMLMINetlinkStatusRxThrput_Type(Integer32):
    """Custom type mcmMLMINetlinkStatusRxThrput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMINetlinkStatusRxThrput_Type.__name__ = "Integer32"
_McmMLMINetlinkStatusRxThrput_Object = MibTableColumn
mcmMLMINetlinkStatusRxThrput = _McmMLMINetlinkStatusRxThrput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 7),
    _McmMLMINetlinkStatusRxThrput_Type()
)
mcmMLMINetlinkStatusRxThrput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMINetlinkStatusRxThrput.setStatus("obsolete")
_McmMLMICircuitStatusTable_Object = MibTable
mcmMLMICircuitStatusTable = _McmMLMICircuitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2)
)
if mibBuilder.loadTexts:
    mcmMLMICircuitStatusTable.setStatus("mandatory")
_McmMLMICircuitStatusEntry_Object = MibTableRow
mcmMLMICircuitStatusEntry = _McmMLMICircuitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1)
)
mcmMLMICircuitStatusEntry.setIndexNames(
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatusIfIndex"),
    (0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatusSVCDLCI"),
)
if mibBuilder.loadTexts:
    mcmMLMICircuitStatusEntry.setStatus("mandatory")


class _McmMLMICircuitStatusIfIndex_Type(Integer32):
    """Custom type mcmMLMICircuitStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmMLMICircuitStatusIfIndex_Type.__name__ = "Integer32"
_McmMLMICircuitStatusIfIndex_Object = MibTableColumn
mcmMLMICircuitStatusIfIndex = _McmMLMICircuitStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 1),
    _McmMLMICircuitStatusIfIndex_Type()
)
mcmMLMICircuitStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatusIfIndex.setStatus("mandatory")


class _McmMLMICircuitStatusSVCDLCI_Type(Integer32):
    """Custom type mcmMLMICircuitStatusSVCDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 991),
    )


_McmMLMICircuitStatusSVCDLCI_Type.__name__ = "Integer32"
_McmMLMICircuitStatusSVCDLCI_Object = MibTableColumn
mcmMLMICircuitStatusSVCDLCI = _McmMLMICircuitStatusSVCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 2),
    _McmMLMICircuitStatusSVCDLCI_Type()
)
mcmMLMICircuitStatusSVCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircuitStatusSVCDLCI.setStatus("mandatory")


class _McmMLMICircStatusRejectCause_Type(Integer32):
    """Custom type mcmMLMICircStatusRejectCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_McmMLMICircStatusRejectCause_Type.__name__ = "Integer32"
_McmMLMICircStatusRejectCause_Object = MibTableColumn
mcmMLMICircStatusRejectCause = _McmMLMICircStatusRejectCause_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 3),
    _McmMLMICircStatusRejectCause_Type()
)
mcmMLMICircStatusRejectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusRejectCause.setStatus("mandatory")


class _McmMLMICircStatusSVCType_Type(Integer32):
    """Custom type mcmMLMICircStatusSVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rfc1490", 1),
          ("rfc1490switched", 4),
          ("rsi", 5),
          ("switched", 3),
          ("voice", 2))
    )


_McmMLMICircStatusSVCType_Type.__name__ = "Integer32"
_McmMLMICircStatusSVCType_Object = MibTableColumn
mcmMLMICircStatusSVCType = _McmMLMICircStatusSVCType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 4),
    _McmMLMICircStatusSVCType_Type()
)
mcmMLMICircStatusSVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusSVCType.setStatus("mandatory")


class _McmMLMICircStatusAttriSetupPriority_Type(Integer32):
    """Custom type mcmMLMICircStatusAttriSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fivePriority", 5),
          ("fourPriority", 4),
          ("onePriority", 1),
          ("threePriority", 3),
          ("twoPriority", 2))
    )


_McmMLMICircStatusAttriSetupPriority_Type.__name__ = "Integer32"
_McmMLMICircStatusAttriSetupPriority_Object = MibTableColumn
mcmMLMICircStatusAttriSetupPriority = _McmMLMICircStatusAttriSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 5),
    _McmMLMICircStatusAttriSetupPriority_Type()
)
mcmMLMICircStatusAttriSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusAttriSetupPriority.setStatus("mandatory")


class _McmMLMICircStatusAttriHoldPriority_Type(Integer32):
    """Custom type mcmMLMICircStatusAttriHoldPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fivePriority", 5),
          ("fourPriority", 4),
          ("onePriority", 1),
          ("threePriority", 3),
          ("twoPriority", 2))
    )


_McmMLMICircStatusAttriHoldPriority_Type.__name__ = "Integer32"
_McmMLMICircStatusAttriHoldPriority_Object = MibTableColumn
mcmMLMICircStatusAttriHoldPriority = _McmMLMICircStatusAttriHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 6),
    _McmMLMICircStatusAttriHoldPriority_Type()
)
mcmMLMICircStatusAttriHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusAttriHoldPriority.setStatus("mandatory")


class _McmMLMICircStatusAttriDiscardPriority_Type(Integer32):
    """Custom type mcmMLMICircStatusAttriDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fivePriority", 5),
          ("fourPriority", 4),
          ("onePriority", 1),
          ("threePriority", 3),
          ("twoPriority", 2))
    )


_McmMLMICircStatusAttriDiscardPriority_Type.__name__ = "Integer32"
_McmMLMICircStatusAttriDiscardPriority_Object = MibTableColumn
mcmMLMICircStatusAttriDiscardPriority = _McmMLMICircStatusAttriDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 7),
    _McmMLMICircStatusAttriDiscardPriority_Type()
)
mcmMLMICircStatusAttriDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusAttriDiscardPriority.setStatus("mandatory")


class _McmMLMICircStatusClaimedBandWidth_Type(Integer32):
    """Custom type mcmMLMICircStatusClaimedBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusClaimedBandWidth_Type.__name__ = "Integer32"
_McmMLMICircStatusClaimedBandWidth_Object = MibTableColumn
mcmMLMICircStatusClaimedBandWidth = _McmMLMICircStatusClaimedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 8),
    _McmMLMICircStatusClaimedBandWidth_Type()
)
mcmMLMICircStatusClaimedBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusClaimedBandWidth.setStatus("mandatory")


class _McmMLMICircStatusQoSTxThrput_Type(Integer32):
    """Custom type mcmMLMICircStatusQoSTxThrput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusQoSTxThrput_Type.__name__ = "Integer32"
_McmMLMICircStatusQoSTxThrput_Object = MibTableColumn
mcmMLMICircStatusQoSTxThrput = _McmMLMICircStatusQoSTxThrput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 9),
    _McmMLMICircStatusQoSTxThrput_Type()
)
mcmMLMICircStatusQoSTxThrput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusQoSTxThrput.setStatus("mandatory")


class _McmMLMICircStatusQoSRxThrput_Type(Integer32):
    """Custom type mcmMLMICircStatusQoSRxThrput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusQoSRxThrput_Type.__name__ = "Integer32"
_McmMLMICircStatusQoSRxThrput_Object = MibTableColumn
mcmMLMICircStatusQoSRxThrput = _McmMLMICircStatusQoSRxThrput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 10),
    _McmMLMICircStatusQoSRxThrput_Type()
)
mcmMLMICircStatusQoSRxThrput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusQoSRxThrput.setStatus("mandatory")


class _McmMLMICircStatusQoSTxBrstSizGrntd_Type(Integer32):
    """Custom type mcmMLMICircStatusQoSTxBrstSizGrntd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusQoSTxBrstSizGrntd_Type.__name__ = "Integer32"
_McmMLMICircStatusQoSTxBrstSizGrntd_Object = MibTableColumn
mcmMLMICircStatusQoSTxBrstSizGrntd = _McmMLMICircStatusQoSTxBrstSizGrntd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 11),
    _McmMLMICircStatusQoSTxBrstSizGrntd_Type()
)
mcmMLMICircStatusQoSTxBrstSizGrntd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusQoSTxBrstSizGrntd.setStatus("mandatory")


class _McmMLMICircStatusQoSRxBrstSizGrntd_Type(Integer32):
    """Custom type mcmMLMICircStatusQoSRxBrstSizGrntd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusQoSRxBrstSizGrntd_Type.__name__ = "Integer32"
_McmMLMICircStatusQoSRxBrstSizGrntd_Object = MibTableColumn
mcmMLMICircStatusQoSRxBrstSizGrntd = _McmMLMICircStatusQoSRxBrstSizGrntd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 12),
    _McmMLMICircStatusQoSRxBrstSizGrntd_Type()
)
mcmMLMICircStatusQoSRxBrstSizGrntd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusQoSRxBrstSizGrntd.setStatus("mandatory")


class _McmMLMICircStatusQoSTxExRateGrntd_Type(Integer32):
    """Custom type mcmMLMICircStatusQoSTxExRateGrntd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusQoSTxExRateGrntd_Type.__name__ = "Integer32"
_McmMLMICircStatusQoSTxExRateGrntd_Object = MibTableColumn
mcmMLMICircStatusQoSTxExRateGrntd = _McmMLMICircStatusQoSTxExRateGrntd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 13),
    _McmMLMICircStatusQoSTxExRateGrntd_Type()
)
mcmMLMICircStatusQoSTxExRateGrntd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusQoSTxExRateGrntd.setStatus("mandatory")


class _McmMLMICircStatusQoSRxExRateGrntd_Type(Integer32):
    """Custom type mcmMLMICircStatusQoSRxExRateGrntd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmMLMICircStatusQoSRxExRateGrntd_Type.__name__ = "Integer32"
_McmMLMICircStatusQoSRxExRateGrntd_Object = MibTableColumn
mcmMLMICircStatusQoSRxExRateGrntd = _McmMLMICircStatusQoSRxExRateGrntd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 14),
    _McmMLMICircStatusQoSRxExRateGrntd_Type()
)
mcmMLMICircStatusQoSRxExRateGrntd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusQoSRxExRateGrntd.setStatus("mandatory")


class _McmMLMICircStatusPeerDLCI_Type(Integer32):
    """Custom type mcmMLMICircStatusPeerDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmMLMICircStatusPeerDLCI_Type.__name__ = "Integer32"
_McmMLMICircStatusPeerDLCI_Object = MibTableColumn
mcmMLMICircStatusPeerDLCI = _McmMLMICircStatusPeerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 15),
    _McmMLMICircStatusPeerDLCI_Type()
)
mcmMLMICircStatusPeerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusPeerDLCI.setStatus("mandatory")


class _McmMLMICircStatusPeerNetwork_Type(Integer32):
    """Custom type mcmMLMICircStatusPeerNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_McmMLMICircStatusPeerNetwork_Type.__name__ = "Integer32"
_McmMLMICircStatusPeerNetwork_Object = MibTableColumn
mcmMLMICircStatusPeerNetwork = _McmMLMICircStatusPeerNetwork_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 16),
    _McmMLMICircStatusPeerNetwork_Type()
)
mcmMLMICircStatusPeerNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusPeerNetwork.setStatus("mandatory")


class _McmMLMICircStatusCallingDNA_Type(DisplayString):
    """Custom type mcmMLMICircStatusCallingDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmMLMICircStatusCallingDNA_Type.__name__ = "DisplayString"
_McmMLMICircStatusCallingDNA_Object = MibTableColumn
mcmMLMICircStatusCallingDNA = _McmMLMICircStatusCallingDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 17),
    _McmMLMICircStatusCallingDNA_Type()
)
mcmMLMICircStatusCallingDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusCallingDNA.setStatus("mandatory")


class _McmMLMICircStatusCalledDNA_Type(DisplayString):
    """Custom type mcmMLMICircStatusCalledDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmMLMICircStatusCalledDNA_Type.__name__ = "DisplayString"
_McmMLMICircStatusCalledDNA_Object = MibTableColumn
mcmMLMICircStatusCalledDNA = _McmMLMICircStatusCalledDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 18),
    _McmMLMICircStatusCalledDNA_Type()
)
mcmMLMICircStatusCalledDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmMLMICircStatusCalledDNA.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmLMISVCCallRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 0, 1)
)
mcmLMISVCCallRejected.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
)
if mibBuilder.loadTexts:
    mcmLMISVCCallRejected.setStatus(
        ""
    )

mcmLMIIncompatibleType = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 0, 2)
)
mcmLMIIncompatibleType.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
)
if mibBuilder.loadTexts:
    mcmLMIIncompatibleType.setStatus(
        ""
    )

mcmLMIT317TimerExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 0, 3)
)
mcmLMIT317TimerExpired.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
)
if mibBuilder.loadTexts:
    mcmLMIT317TimerExpired.setStatus(
        ""
    )

mcmMLMIReachedMaxUnsucessfulRestartAttemps = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 0, 4)
)
mcmMLMIReachedMaxUnsucessfulRestartAttemps.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
)
if mibBuilder.loadTexts:
    mcmMLMIReachedMaxUnsucessfulRestartAttemps.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-MPANL-LMI-MIB",
    **{"micom-mlmi": micom_mlmi,
       "mcmLMISVCCallRejected": mcmLMISVCCallRejected,
       "mcmLMIIncompatibleType": mcmLMIIncompatibleType,
       "mcmLMIT317TimerExpired": mcmLMIT317TimerExpired,
       "mcmMLMIReachedMaxUnsucessfulRestartAttemps": mcmMLMIReachedMaxUnsucessfulRestartAttemps,
       "mlmi-configuration": mlmi_configuration,
       "mcmMLMIGenCfg4400Type": mcmMLMIGenCfg4400Type,
       "mcmMLMIGenCfgSoftwareRev": mcmMLMIGenCfgSoftwareRev,
       "mcmMLMIServiceTable": mcmMLMIServiceTable,
       "mcmMLMIServiceEntry": mcmMLMIServiceEntry,
       "mcmMLMIServiceIfIndex": mcmMLMIServiceIfIndex,
       "mcmMLMIServiceCUGFacility": mcmMLMIServiceCUGFacility,
       "mcmMLMIServiceCUGAccess": mcmMLMIServiceCUGAccess,
       "mcmMLMIServiceCUGICType": mcmMLMIServiceCUGICType,
       "mcmMLMIServiceCUGIC": mcmMLMIServiceCUGIC,
       "mcmMLMIServiceDNASuffix": mcmMLMIServiceDNASuffix,
       "nvmMLMIGenCfg4400Type": nvmMLMIGenCfg4400Type,
       "nvmMLMIServiceTable": nvmMLMIServiceTable,
       "nvmMLMIServiceEntry": nvmMLMIServiceEntry,
       "nvmMLMIServiceIfIndex": nvmMLMIServiceIfIndex,
       "nvmMLMIServiceCUGFacility": nvmMLMIServiceCUGFacility,
       "nvmMLMIServiceCUGAccess": nvmMLMIServiceCUGAccess,
       "nvmMLMIServiceCUGICType": nvmMLMIServiceCUGICType,
       "nvmMLMIServiceCUGIC": nvmMLMIServiceCUGIC,
       "nvmMLMIServiceDNASuffix": nvmMLMIServiceDNASuffix,
       "nvmMLMIServiceRowStatus": nvmMLMIServiceRowStatus,
       "mcmMLMINetlinkTable": mcmMLMINetlinkTable,
       "mcmMLMINetlinkEntry": mcmMLMINetlinkEntry,
       "mcmMLMINetlinkIfIndex": mcmMLMINetlinkIfIndex,
       "mcmMLMINetlinkTunnelingPVCDlci": mcmMLMINetlinkTunnelingPVCDlci,
       "mcmMLMINetlinkMpanlMode": mcmMLMINetlinkMpanlMode,
       "mcmMLMINetlinkDLCIAssignMethod": mcmMLMINetlinkDLCIAssignMethod,
       "mcmMLMINetlinkRstrtT316Timer": mcmMLMINetlinkRstrtT316Timer,
       "mcmMLMINetlinkRstrtAckT317Timer": mcmMLMINetlinkRstrtAckT317Timer,
       "mcmMLMINetlinkNumUnsuccesRstrtAtmpts": mcmMLMINetlinkNumUnsuccesRstrtAtmpts,
       "nvmMLMINetlinkTable": nvmMLMINetlinkTable,
       "nvmMLMINetlinkEntry": nvmMLMINetlinkEntry,
       "nvmMLMINetlinkIfIndex": nvmMLMINetlinkIfIndex,
       "nvmMLMINetlinkTunnelingPVCDlci": nvmMLMINetlinkTunnelingPVCDlci,
       "nvmMLMINetlinkDLCIAssignMethod": nvmMLMINetlinkDLCIAssignMethod,
       "nvmMLMINetlinkRstrtT316Timer": nvmMLMINetlinkRstrtT316Timer,
       "nvmMLMINetlinkRstrtAckT317Timer": nvmMLMINetlinkRstrtAckT317Timer,
       "nvmMLMINetlinkNumUnsuccesRstrtAtmpts": nvmMLMINetlinkNumUnsuccesRstrtAtmpts,
       "mlmi-control": mlmi_control,
       "mcmMLMICntrAction": mcmMLMICntrAction,
       "mlmi-statistics": mlmi_statistics,
       "mcmMLMIStatsActiveVCs": mcmMLMIStatsActiveVCs,
       "mcmMLMIStatsRequestedCalls": mcmMLMIStatsRequestedCalls,
       "mcmMLMIStatsInitiatedCalls": mcmMLMIStatsInitiatedCalls,
       "mcmMLMIStatsFailedCalls": mcmMLMIStatsFailedCalls,
       "mcmMLMIStatsSucceededCalls": mcmMLMIStatsSucceededCalls,
       "mcmMLMIStatsReleasedCalls": mcmMLMIStatsReleasedCalls,
       "mcmMLMIStatsDisconnectedCalls": mcmMLMIStatsDisconnectedCalls,
       "mcmMLMIStatsAdmittedCUGs": mcmMLMIStatsAdmittedCUGs,
       "mcmMLMIStatsRejectedCUGs": mcmMLMIStatsRejectedCUGs,
       "mcmMLMINetlinkStatTable": mcmMLMINetlinkStatTable,
       "mcmMLMINetlinkStatEntry": mcmMLMINetlinkStatEntry,
       "mcmMLMINetlinkStatIfIndex": mcmMLMINetlinkStatIfIndex,
       "mcmMLMINetlinkStatMsgRxSetup": mcmMLMINetlinkStatMsgRxSetup,
       "mcmMLMINetlinkStatMsgTxSetup": mcmMLMINetlinkStatMsgTxSetup,
       "mcmMLMINetlinkStatMsgRxCallPrcdngs": mcmMLMINetlinkStatMsgRxCallPrcdngs,
       "mcmMLMINetlinkStatMsgTxCallPrcdngs": mcmMLMINetlinkStatMsgTxCallPrcdngs,
       "mcmMLMINetlinkStatMsgRxConn": mcmMLMINetlinkStatMsgRxConn,
       "mcmMLMINetlinkStatMsgTxConn": mcmMLMINetlinkStatMsgTxConn,
       "mcmMLMINetlinkStatMsgRxDisConn": mcmMLMINetlinkStatMsgRxDisConn,
       "mcmMLMINetlinkStatMsgTxDisConn": mcmMLMINetlinkStatMsgTxDisConn,
       "mcmMLMINetlinkStatMsgRxRls": mcmMLMINetlinkStatMsgRxRls,
       "mcmMLMINetlinkStatMsgTxRls": mcmMLMINetlinkStatMsgTxRls,
       "mcmMLMINetlinkStatMsgRxRlseComp": mcmMLMINetlinkStatMsgRxRlseComp,
       "mcmMLMINetlinkStatMsgTxRlseComp": mcmMLMINetlinkStatMsgTxRlseComp,
       "mcmMLMINetlinkStatMsgRxStatusInq": mcmMLMINetlinkStatMsgRxStatusInq,
       "mcmMLMINetlinkStatMsgTxStatusInq": mcmMLMINetlinkStatMsgTxStatusInq,
       "mcmMLMINetlinkStatMsgRxStatus": mcmMLMINetlinkStatMsgRxStatus,
       "mcmMLMINetlinkStatMsgTxStatus": mcmMLMINetlinkStatMsgTxStatus,
       "mcmMLMINetlinkStatLocalSVC": mcmMLMINetlinkStatLocalSVC,
       "mcmMLMINetlinkStatTransitSVC": mcmMLMINetlinkStatTransitSVC,
       "mcmMLMINetlinkStatVoiceCalls": mcmMLMINetlinkStatVoiceCalls,
       "mcmMLMINetlinkStatLanCalls": mcmMLMINetlinkStatLanCalls,
       "mcmMLMINetlinkStatRsiCalls": mcmMLMINetlinkStatRsiCalls,
       "mcmMLMINetlinkStatSpvcCalls": mcmMLMINetlinkStatSpvcCalls,
       "mcmMLMINetlinkStatLnkupCnt": mcmMLMINetlinkStatLnkupCnt,
       "mcmMLMINetlinkStatLnkDownCnt": mcmMLMINetlinkStatLnkDownCnt,
       "mcmMLMICircuitStatTable": mcmMLMICircuitStatTable,
       "mcmMLMICircuitStatEntry": mcmMLMICircuitStatEntry,
       "mcmMLMICircuitStatIfIndex": mcmMLMICircuitStatIfIndex,
       "mcmMLMICircuitStatSVCDLCI": mcmMLMICircuitStatSVCDLCI,
       "mcmMLMICircuitStatMsgRxStatus": mcmMLMICircuitStatMsgRxStatus,
       "mcmMLMICircuitStatMsgTxStatus": mcmMLMICircuitStatMsgTxStatus,
       "mcmMLMICircuitStatMsgRxStatusInq": mcmMLMICircuitStatMsgRxStatusInq,
       "mcmMLMICircuitStatMsgTxStatusInq": mcmMLMICircuitStatMsgTxStatusInq,
       "mlmi-status": mlmi_status,
       "mcmMLMINetlinkStatusTable": mcmMLMINetlinkStatusTable,
       "mcmMLMINetlinkStatusEntry": mcmMLMINetlinkStatusEntry,
       "mcmMLMINetlinkStatusIfIndex": mcmMLMINetlinkStatusIfIndex,
       "mcmMLMINetlinkStatusMPANLStatus": mcmMLMINetlinkStatusMPANLStatus,
       "mcmMLMINetlinkStatusRestartState": mcmMLMINetlinkStatusRestartState,
       "mcmMLMINetlinkStatusLAPFState": mcmMLMINetlinkStatusLAPFState,
       "mcmMLMINetlinkStatusFrCoreState": mcmMLMINetlinkStatusFrCoreState,
       "mcmMLMINetlinkStatusTxThrput": mcmMLMINetlinkStatusTxThrput,
       "mcmMLMINetlinkStatusRxThrput": mcmMLMINetlinkStatusRxThrput,
       "mcmMLMICircuitStatusTable": mcmMLMICircuitStatusTable,
       "mcmMLMICircuitStatusEntry": mcmMLMICircuitStatusEntry,
       "mcmMLMICircuitStatusIfIndex": mcmMLMICircuitStatusIfIndex,
       "mcmMLMICircuitStatusSVCDLCI": mcmMLMICircuitStatusSVCDLCI,
       "mcmMLMICircStatusRejectCause": mcmMLMICircStatusRejectCause,
       "mcmMLMICircStatusSVCType": mcmMLMICircStatusSVCType,
       "mcmMLMICircStatusAttriSetupPriority": mcmMLMICircStatusAttriSetupPriority,
       "mcmMLMICircStatusAttriHoldPriority": mcmMLMICircStatusAttriHoldPriority,
       "mcmMLMICircStatusAttriDiscardPriority": mcmMLMICircStatusAttriDiscardPriority,
       "mcmMLMICircStatusClaimedBandWidth": mcmMLMICircStatusClaimedBandWidth,
       "mcmMLMICircStatusQoSTxThrput": mcmMLMICircStatusQoSTxThrput,
       "mcmMLMICircStatusQoSRxThrput": mcmMLMICircStatusQoSRxThrput,
       "mcmMLMICircStatusQoSTxBrstSizGrntd": mcmMLMICircStatusQoSTxBrstSizGrntd,
       "mcmMLMICircStatusQoSRxBrstSizGrntd": mcmMLMICircStatusQoSRxBrstSizGrntd,
       "mcmMLMICircStatusQoSTxExRateGrntd": mcmMLMICircStatusQoSTxExRateGrntd,
       "mcmMLMICircStatusQoSRxExRateGrntd": mcmMLMICircStatusQoSRxExRateGrntd,
       "mcmMLMICircStatusPeerDLCI": mcmMLMICircStatusPeerDLCI,
       "mcmMLMICircStatusPeerNetwork": mcmMLMICircStatusPeerNetwork,
       "mcmMLMICircStatusCallingDNA": mcmMLMICircStatusCallingDNA,
       "mcmMLMICircStatusCalledDNA": mcmMLMICircStatusCalledDNA}
)
