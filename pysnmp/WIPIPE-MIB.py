# SNMP MIB module (WIPIPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WIPIPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:00 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wipipe_ObjectIdentity = ObjectIdentity
wipipe = _Wipipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992)
)
_WipipeMgmt_ObjectIdentity = ObjectIdentity
wipipeMgmt = _WipipeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 1)
)
_WipipeDevice_ObjectIdentity = ObjectIdentity
wipipeDevice = _WipipeDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1)
)


class _DevFWVersion_Type(DisplayString):
    """Custom type devFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevFWVersion_Type.__name__ = "DisplayString"
_DevFWVersion_Object = MibScalar
devFWVersion = _DevFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 1),
    _DevFWVersion_Type()
)
devFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFWVersion.setStatus("mandatory")


class _DevFWUpgrade_Type(Integer32):
    """Custom type devFWUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 3),
          ("none", 1))
    )


_DevFWUpgrade_Type.__name__ = "Integer32"
_DevFWUpgrade_Object = MibScalar
devFWUpgrade = _DevFWUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 2),
    _DevFWUpgrade_Type()
)
devFWUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFWUpgrade.setStatus("mandatory")


class _DevFWUpgradeURL_Type(DisplayString):
    """Custom type devFWUpgradeURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevFWUpgradeURL_Type.__name__ = "DisplayString"
_DevFWUpgradeURL_Object = MibScalar
devFWUpgradeURL = _DevFWUpgradeURL_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 3),
    _DevFWUpgradeURL_Type()
)
devFWUpgradeURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFWUpgradeURL.setStatus("mandatory")


class _DevFWUpgradeStatus_Type(Integer32):
    """Custom type devFWUpgradeStatus based on Integer32"""
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
        *(("failure", 5),
          ("idle", 1),
          ("updateAvail", 4),
          ("upgrading", 2),
          ("uptodate", 3))
    )


_DevFWUpgradeStatus_Type.__name__ = "Integer32"
_DevFWUpgradeStatus_Object = MibScalar
devFWUpgradeStatus = _DevFWUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 4),
    _DevFWUpgradeStatus_Type()
)
devFWUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFWUpgradeStatus.setStatus("mandatory")


class _DevGpioConfigInput_Type(Integer32):
    """Custom type devGpioConfigInput based on Integer32"""
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
        *(("ignitionSensing", 4),
          ("input", 2),
          ("none", 1),
          ("reboot", 3))
    )


_DevGpioConfigInput_Type.__name__ = "Integer32"
_DevGpioConfigInput_Object = MibScalar
devGpioConfigInput = _DevGpioConfigInput_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 5),
    _DevGpioConfigInput_Type()
)
devGpioConfigInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devGpioConfigInput.setStatus("mandatory")


class _DevGpioReadInput_Type(Integer32):
    """Custom type devGpioReadInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevGpioReadInput_Type.__name__ = "Integer32"
_DevGpioReadInput_Object = MibScalar
devGpioReadInput = _DevGpioReadInput_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 6),
    _DevGpioReadInput_Type()
)
devGpioReadInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devGpioReadInput.setStatus("mandatory")


class _DevGpioConfigOutput_Type(Integer32):
    """Custom type devGpioConfigOutput based on Integer32"""
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
        *(("high", 2),
          ("low", 1),
          ("modemConnected", 4),
          ("routerRunning", 3))
    )


_DevGpioConfigOutput_Type.__name__ = "Integer32"
_DevGpioConfigOutput_Object = MibScalar
devGpioConfigOutput = _DevGpioConfigOutput_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 7),
    _DevGpioConfigOutput_Type()
)
devGpioConfigOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devGpioConfigOutput.setStatus("mandatory")


class _DevGpioReadOutput_Type(Integer32):
    """Custom type devGpioReadOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevGpioReadOutput_Type.__name__ = "Integer32"
_DevGpioReadOutput_Object = MibScalar
devGpioReadOutput = _DevGpioReadOutput_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 1, 8),
    _DevGpioReadOutput_Type()
)
devGpioReadOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devGpioReadOutput.setStatus("mandatory")
_WipipeCellMdm_ObjectIdentity = ObjectIdentity
wipipeCellMdm = _WipipeCellMdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2)
)


class _MdmNumber_Type(Integer32):
    """Custom type mdmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MdmNumber_Type.__name__ = "Integer32"
_MdmNumber_Object = MibScalar
mdmNumber = _MdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 1),
    _MdmNumber_Type()
)
mdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNumber.setStatus("mandatory")
_MdmTable_Object = MibTable
mdmTable = _MdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mdmTable.setStatus("mandatory")
_MdmEntry_Object = MibTableRow
mdmEntry = _MdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1)
)
mdmEntry.setIndexNames(
    (0, "WIPIPE-MIB", "mdmIndex"),
)
if mibBuilder.loadTexts:
    mdmEntry.setStatus("mandatory")


class _MdmIndex_Type(Integer32):
    """Custom type mdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MdmIndex_Type.__name__ = "Integer32"
_MdmIndex_Object = MibTableColumn
mdmIndex = _MdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 1),
    _MdmIndex_Type()
)
mdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIndex.setStatus("mandatory")


class _MdmDescr_Type(DisplayString):
    """Custom type mdmDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdmDescr_Type.__name__ = "DisplayString"
_MdmDescr_Object = MibTableColumn
mdmDescr = _MdmDescr_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 2),
    _MdmDescr_Type()
)
mdmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDescr.setStatus("mandatory")


class _MdmPort_Type(DisplayString):
    """Custom type mdmPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdmPort_Type.__name__ = "DisplayString"
_MdmPort_Object = MibTableColumn
mdmPort = _MdmPort_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 3),
    _MdmPort_Type()
)
mdmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPort.setStatus("mandatory")


class _MdmSignalStrength_Type(Integer32):
    """Custom type mdmSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, -30),
    )


_MdmSignalStrength_Type.__name__ = "Integer32"
_MdmSignalStrength_Object = MibTableColumn
mdmSignalStrength = _MdmSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 4),
    _MdmSignalStrength_Type()
)
mdmSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSignalStrength.setStatus("mandatory")


class _MdmStatus_Type(Integer32):
    """Custom type mdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 5),
          ("disconnecting", 6),
          ("empty", 8),
          ("error", 4),
          ("established", 1),
          ("establishing", 2),
          ("notconfigured", 9),
          ("ready", 3),
          ("suspended", 7),
          ("userstopped", 10))
    )


_MdmStatus_Type.__name__ = "Integer32"
_MdmStatus_Object = MibTableColumn
mdmStatus = _MdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 5),
    _MdmStatus_Type()
)
mdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatus.setStatus("mandatory")


class _MdmECIO_Type(Integer32):
    """Custom type mdmECIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 0),
    )


_MdmECIO_Type.__name__ = "Integer32"
_MdmECIO_Object = MibTableColumn
mdmECIO = _MdmECIO_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 6),
    _MdmECIO_Type()
)
mdmECIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmECIO.setStatus("mandatory")


class _MdmSerialNumber_Type(DisplayString):
    """Custom type mdmSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmSerialNumber_Type.__name__ = "DisplayString"
_MdmSerialNumber_Object = MibTableColumn
mdmSerialNumber = _MdmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 7),
    _MdmSerialNumber_Type()
)
mdmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSerialNumber.setStatus("mandatory")


class _MdmFirmwareVersion_Type(DisplayString):
    """Custom type mdmFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MdmFirmwareVersion_Type.__name__ = "DisplayString"
_MdmFirmwareVersion_Object = MibTableColumn
mdmFirmwareVersion = _MdmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 8),
    _MdmFirmwareVersion_Type()
)
mdmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmFirmwareVersion.setStatus("mandatory")


class _MdmMDN_Type(DisplayString):
    """Custom type mdmMDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmMDN_Type.__name__ = "DisplayString"
_MdmMDN_Object = MibTableColumn
mdmMDN = _MdmMDN_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 9),
    _MdmMDN_Type()
)
mdmMDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMDN.setStatus("mandatory")


class _MdmSERDIS_Type(DisplayString):
    """Custom type mdmSERDIS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmSERDIS_Type.__name__ = "DisplayString"
_MdmSERDIS_Object = MibTableColumn
mdmSERDIS = _MdmSERDIS_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 10),
    _MdmSERDIS_Type()
)
mdmSERDIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSERDIS.setStatus("mandatory")


class _MdmPROF_Type(DisplayString):
    """Custom type mdmPROF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmPROF_Type.__name__ = "DisplayString"
_MdmPROF_Object = MibTableColumn
mdmPROF = _MdmPROF_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 11),
    _MdmPROF_Type()
)
mdmPROF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPROF.setStatus("mandatory")


class _MdmCINR_Type(Integer32):
    """Custom type mdmCINR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 0),
    )


_MdmCINR_Type.__name__ = "Integer32"
_MdmCINR_Object = MibTableColumn
mdmCINR = _MdmCINR_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 12),
    _MdmCINR_Type()
)
mdmCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCINR.setStatus("mandatory")


class _MdmSINR_Type(Integer32):
    """Custom type mdmSINR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 40),
    )


_MdmSINR_Type.__name__ = "Integer32"
_MdmSINR_Object = MibTableColumn
mdmSINR = _MdmSINR_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 13),
    _MdmSINR_Type()
)
mdmSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSINR.setStatus("mandatory")


class _MdmRSRP_Type(Integer32):
    """Custom type mdmRSRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 100),
    )


_MdmRSRP_Type.__name__ = "Integer32"
_MdmRSRP_Object = MibTableColumn
mdmRSRP = _MdmRSRP_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 14),
    _MdmRSRP_Type()
)
mdmRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRSRP.setStatus("mandatory")


class _MdmRSRQ_Type(Integer32):
    """Custom type mdmRSRQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, 50),
    )


_MdmRSRQ_Type.__name__ = "Integer32"
_MdmRSRQ_Object = MibTableColumn
mdmRSRQ = _MdmRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 15),
    _MdmRSRQ_Type()
)
mdmRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRSRQ.setStatus("mandatory")


class _MdmROAM_Type(Integer32):
    """Custom type mdmROAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MdmROAM_Type.__name__ = "Integer32"
_MdmROAM_Object = MibTableColumn
mdmROAM = _MdmROAM_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 16),
    _MdmROAM_Type()
)
mdmROAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmROAM.setStatus("mandatory")
_MdmRFBAND_Type = DisplayString
_MdmRFBAND_Object = MibTableColumn
mdmRFBAND = _MdmRFBAND_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 17),
    _MdmRFBAND_Type()
)
mdmRFBAND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRFBAND.setStatus("mandatory")


class _MdmHOMECARRIER_Type(DisplayString):
    """Custom type mdmHOMECARRIER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmHOMECARRIER_Type.__name__ = "DisplayString"
_MdmHOMECARRIER_Object = MibTableColumn
mdmHOMECARRIER = _MdmHOMECARRIER_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 18),
    _MdmHOMECARRIER_Type()
)
mdmHOMECARRIER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHOMECARRIER.setStatus("mandatory")


class _MdmIMSI_Type(DisplayString):
    """Custom type mdmIMSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmIMSI_Type.__name__ = "DisplayString"
_MdmIMSI_Object = MibTableColumn
mdmIMSI = _MdmIMSI_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 19),
    _MdmIMSI_Type()
)
mdmIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIMSI.setStatus("mandatory")


class _MdmIMEI_Type(DisplayString):
    """Custom type mdmIMEI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmIMEI_Type.__name__ = "DisplayString"
_MdmIMEI_Object = MibTableColumn
mdmIMEI = _MdmIMEI_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 20),
    _MdmIMEI_Type()
)
mdmIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIMEI.setStatus("mandatory")


class _MdmAPN_Type(DisplayString):
    """Custom type mdmAPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmAPN_Type.__name__ = "DisplayString"
_MdmAPN_Object = MibTableColumn
mdmAPN = _MdmAPN_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 21),
    _MdmAPN_Type()
)
mdmAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAPN.setStatus("mandatory")


class _MdmRFCHANNEL_Type(DisplayString):
    """Custom type mdmRFCHANNEL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmRFCHANNEL_Type.__name__ = "DisplayString"
_MdmRFCHANNEL_Object = MibTableColumn
mdmRFCHANNEL = _MdmRFCHANNEL_Object(
    (1, 3, 6, 1, 4, 1, 20992, 1, 2, 2, 1, 22),
    _MdmRFCHANNEL_Type()
)
mdmRFCHANNEL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRFCHANNEL.setStatus("mandatory")
_WipipeProd_ObjectIdentity = ObjectIdentity
wipipeProd = _WipipeProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2)
)
_Mbr1000_ObjectIdentity = ObjectIdentity
mbr1000 = _Mbr1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 1)
)
_Ctr500_ObjectIdentity = ObjectIdentity
ctr500 = _Ctr500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 2)
)
_Mbr800_ObjectIdentity = ObjectIdentity
mbr800 = _Mbr800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 3)
)
_Mbr1100_ObjectIdentity = ObjectIdentity
mbr1100 = _Mbr1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 4)
)
_Mbr1200_ObjectIdentity = ObjectIdentity
mbr1200 = _Mbr1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 5)
)
_Mbr900_ObjectIdentity = ObjectIdentity
mbr900 = _Mbr900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 6)
)
_Cba250_ObjectIdentity = ObjectIdentity
cba250 = _Cba250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 7)
)
_Cba750_ObjectIdentity = ObjectIdentity
cba750 = _Cba750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 8)
)
_Cx111_ObjectIdentity = ObjectIdentity
cx111 = _Cx111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 9)
)
_Mbr1400_ObjectIdentity = ObjectIdentity
mbr1400 = _Mbr1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 10)
)
_Mbr1200b_ObjectIdentity = ObjectIdentity
mbr1200b = _Mbr1200b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 11)
)
_Cbr400_ObjectIdentity = ObjectIdentity
cbr400 = _Cbr400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 12)
)
_Cbr450_ObjectIdentity = ObjectIdentity
cbr450 = _Cbr450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 13)
)
_Ibr600_ObjectIdentity = ObjectIdentity
ibr600 = _Ibr600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 14)
)
_Ibr650_ObjectIdentity = ObjectIdentity
ibr650 = _Ibr650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 15)
)
_Mbr1400v2_ObjectIdentity = ObjectIdentity
mbr1400v2 = _Mbr1400v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 16)
)
_Cba750b_ObjectIdentity = ObjectIdentity
cba750b = _Cba750b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 17)
)
_Aer2100_ObjectIdentity = ObjectIdentity
aer2100 = _Aer2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 18)
)
_Ibr1150_ObjectIdentity = ObjectIdentity
ibr1150 = _Ibr1150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 19)
)
_Ibr1100_ObjectIdentity = ObjectIdentity
ibr1100 = _Ibr1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 20)
)
_Cba850_ObjectIdentity = ObjectIdentity
cba850 = _Cba850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 21)
)
_Ibr350_ObjectIdentity = ObjectIdentity
ibr350 = _Ibr350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 22)
)
_Aer3100_ObjectIdentity = ObjectIdentity
aer3100 = _Aer3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 23)
)
_Aer1600_ObjectIdentity = ObjectIdentity
aer1600 = _Aer1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 24)
)
_Ibr650b_ObjectIdentity = ObjectIdentity
ibr650b = _Ibr650b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 25)
)
_Aer3150_ObjectIdentity = ObjectIdentity
aer3150 = _Aer3150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 26)
)
_Aer1650_ObjectIdentity = ObjectIdentity
aer1650 = _Aer1650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 27)
)
_Aer2150_ObjectIdentity = ObjectIdentity
aer2150 = _Aer2150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 28)
)
_Ibr600b_ObjectIdentity = ObjectIdentity
ibr600b = _Ibr600b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 29)
)
_Ibr950_ObjectIdentity = ObjectIdentity
ibr950 = _Ibr950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 30)
)
_Ibr900_ObjectIdentity = ObjectIdentity
ibr900 = _Ibr900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20992, 2, 31)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WIPIPE-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "wipipe": wipipe,
       "wipipeMgmt": wipipeMgmt,
       "wipipeDevice": wipipeDevice,
       "devFWVersion": devFWVersion,
       "devFWUpgrade": devFWUpgrade,
       "devFWUpgradeURL": devFWUpgradeURL,
       "devFWUpgradeStatus": devFWUpgradeStatus,
       "devGpioConfigInput": devGpioConfigInput,
       "devGpioReadInput": devGpioReadInput,
       "devGpioConfigOutput": devGpioConfigOutput,
       "devGpioReadOutput": devGpioReadOutput,
       "wipipeCellMdm": wipipeCellMdm,
       "mdmNumber": mdmNumber,
       "mdmTable": mdmTable,
       "mdmEntry": mdmEntry,
       "mdmIndex": mdmIndex,
       "mdmDescr": mdmDescr,
       "mdmPort": mdmPort,
       "mdmSignalStrength": mdmSignalStrength,
       "mdmStatus": mdmStatus,
       "mdmECIO": mdmECIO,
       "mdmSerialNumber": mdmSerialNumber,
       "mdmFirmwareVersion": mdmFirmwareVersion,
       "mdmMDN": mdmMDN,
       "mdmSERDIS": mdmSERDIS,
       "mdmPROF": mdmPROF,
       "mdmCINR": mdmCINR,
       "mdmSINR": mdmSINR,
       "mdmRSRP": mdmRSRP,
       "mdmRSRQ": mdmRSRQ,
       "mdmROAM": mdmROAM,
       "mdmRFBAND": mdmRFBAND,
       "mdmHOMECARRIER": mdmHOMECARRIER,
       "mdmIMSI": mdmIMSI,
       "mdmIMEI": mdmIMEI,
       "mdmAPN": mdmAPN,
       "mdmRFCHANNEL": mdmRFCHANNEL,
       "wipipeProd": wipipeProd,
       "mbr1000": mbr1000,
       "ctr500": ctr500,
       "mbr800": mbr800,
       "mbr1100": mbr1100,
       "mbr1200": mbr1200,
       "mbr900": mbr900,
       "cba250": cba250,
       "cba750": cba750,
       "cx111": cx111,
       "mbr1400": mbr1400,
       "mbr1200b": mbr1200b,
       "cbr400": cbr400,
       "cbr450": cbr450,
       "ibr600": ibr600,
       "ibr650": ibr650,
       "mbr1400v2": mbr1400v2,
       "cba750b": cba750b,
       "aer2100": aer2100,
       "ibr1150": ibr1150,
       "ibr1100": ibr1100,
       "cba850": cba850,
       "ibr350": ibr350,
       "aer3100": aer3100,
       "aer1600": aer1600,
       "ibr650b": ibr650b,
       "aer3150": aer3150,
       "aer1650": aer1650,
       "aer2150": aer2150,
       "ibr600b": ibr600b,
       "ibr950": ibr950,
       "ibr900": ibr900}
)
