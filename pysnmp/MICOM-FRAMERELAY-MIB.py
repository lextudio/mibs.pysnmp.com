# SNMP MIB module (MICOM-FRAMERELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-FRAMERELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:40 2024
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

(mcmSysAsciiTimeOfDay,
 mcmSysIfExtModule,
 mcmSysIfExtPPA) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay",
    "mcmSysIfExtModule",
    "mcmSysIfExtPPA")

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



class Index(Integer32):
    """Custom type Index based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_frame_relay_ObjectIdentity = ObjectIdentity
micom_frame_relay = _Micom_frame_relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7)
)
_Fr_configuration_ObjectIdentity = ObjectIdentity
fr_configuration = _Fr_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1)
)
_McmFrGlobalGroup_ObjectIdentity = ObjectIdentity
mcmFrGlobalGroup = _McmFrGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1)
)
_McmFrMaxDLCI_Type = Integer32
_McmFrMaxDLCI_Object = MibScalar
mcmFrMaxDLCI = _McmFrMaxDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 1),
    _McmFrMaxDLCI_Type()
)
mcmFrMaxDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMaxDLCI.setStatus("mandatory")


class _McmFrMaxVirtualPorts_Type(Integer32):
    """Custom type mcmFrMaxVirtualPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmFrMaxVirtualPorts_Type.__name__ = "Integer32"
_McmFrMaxVirtualPorts_Object = MibScalar
mcmFrMaxVirtualPorts = _McmFrMaxVirtualPorts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 2),
    _McmFrMaxVirtualPorts_Type()
)
mcmFrMaxVirtualPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMaxVirtualPorts.setStatus("mandatory")


class _McmFrMaxDlciPerLine_Type(Integer32):
    """Custom type mcmFrMaxDlciPerLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrMaxDlciPerLine_Type.__name__ = "Integer32"
_McmFrMaxDlciPerLine_Object = MibScalar
mcmFrMaxDlciPerLine = _McmFrMaxDlciPerLine_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 3),
    _McmFrMaxDlciPerLine_Type()
)
mcmFrMaxDlciPerLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMaxDlciPerLine.setStatus("mandatory")
_McmFrConnectTime_Type = TimeTicks
_McmFrConnectTime_Object = MibScalar
mcmFrConnectTime = _McmFrConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 4),
    _McmFrConnectTime_Type()
)
mcmFrConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrConnectTime.setStatus("mandatory")
_McmFrOctetsSent_Type = Counter32
_McmFrOctetsSent_Object = MibScalar
mcmFrOctetsSent = _McmFrOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 5),
    _McmFrOctetsSent_Type()
)
mcmFrOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrOctetsSent.setStatus("mandatory")
_McmFrOctetsReceived_Type = Counter32
_McmFrOctetsReceived_Object = MibScalar
mcmFrOctetsReceived = _McmFrOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 6),
    _McmFrOctetsReceived_Type()
)
mcmFrOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrOctetsReceived.setStatus("mandatory")
_McmFrFramesSent_Type = Counter32
_McmFrFramesSent_Object = MibScalar
mcmFrFramesSent = _McmFrFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 7),
    _McmFrFramesSent_Type()
)
mcmFrFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrFramesSent.setStatus("mandatory")
_McmFrFramesReceived_Type = Counter32
_McmFrFramesReceived_Object = MibScalar
mcmFrFramesReceived = _McmFrFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 8),
    _McmFrFramesReceived_Type()
)
mcmFrFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrFramesReceived.setStatus("mandatory")


class _McmFrGlobalGroupCntrAction_Type(Integer32):
    """Custom type mcmFrGlobalGroupCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmFrGlobalGroupCntrAction_Type.__name__ = "Integer32"
_McmFrGlobalGroupCntrAction_Object = MibScalar
mcmFrGlobalGroupCntrAction = _McmFrGlobalGroupCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 9),
    _McmFrGlobalGroupCntrAction_Type()
)
mcmFrGlobalGroupCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrGlobalGroupCntrAction.setStatus("obsolete")


class _McmFrDNANumberingPlan_Type(Integer32):
    """Custom type mcmFrDNANumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 3))
    )


_McmFrDNANumberingPlan_Type.__name__ = "Integer32"
_McmFrDNANumberingPlan_Object = MibScalar
mcmFrDNANumberingPlan = _McmFrDNANumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 10),
    _McmFrDNANumberingPlan_Type()
)
mcmFrDNANumberingPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDNANumberingPlan.setStatus("mandatory")
_McmFrActivePanlDlciSVCs_Type = Counter32
_McmFrActivePanlDlciSVCs_Object = MibScalar
mcmFrActivePanlDlciSVCs = _McmFrActivePanlDlciSVCs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 11),
    _McmFrActivePanlDlciSVCs_Type()
)
mcmFrActivePanlDlciSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrActivePanlDlciSVCs.setStatus("mandatory")
_McmFrTotalTunnelingPVCs_Type = Counter32
_McmFrTotalTunnelingPVCs_Object = MibScalar
mcmFrTotalTunnelingPVCs = _McmFrTotalTunnelingPVCs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 12),
    _McmFrTotalTunnelingPVCs_Type()
)
mcmFrTotalTunnelingPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTotalTunnelingPVCs.setStatus("mandatory")
_McmFrActiveTunnelingPVCs_Type = Counter32
_McmFrActiveTunnelingPVCs_Object = MibScalar
mcmFrActiveTunnelingPVCs = _McmFrActiveTunnelingPVCs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 13),
    _McmFrActiveTunnelingPVCs_Type()
)
mcmFrActiveTunnelingPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrActiveTunnelingPVCs.setStatus("mandatory")


class _McmFrPanlLmiTrapEnable_Type(Integer32):
    """Custom type mcmFrPanlLmiTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmFrPanlLmiTrapEnable_Type.__name__ = "Integer32"
_McmFrPanlLmiTrapEnable_Object = MibScalar
mcmFrPanlLmiTrapEnable = _McmFrPanlLmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 14),
    _McmFrPanlLmiTrapEnable_Type()
)
mcmFrPanlLmiTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPanlLmiTrapEnable.setStatus("mandatory")


class _McmFrMsmTrapEnable_Type(Integer32):
    """Custom type mcmFrMsmTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmFrMsmTrapEnable_Type.__name__ = "Integer32"
_McmFrMsmTrapEnable_Object = MibScalar
mcmFrMsmTrapEnable = _McmFrMsmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 15),
    _McmFrMsmTrapEnable_Type()
)
mcmFrMsmTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMsmTrapEnable.setStatus("mandatory")


class _McmFrCoreTrapEnable_Type(Integer32):
    """Custom type mcmFrCoreTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmFrCoreTrapEnable_Type.__name__ = "Integer32"
_McmFrCoreTrapEnable_Object = MibScalar
mcmFrCoreTrapEnable = _McmFrCoreTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 16),
    _McmFrCoreTrapEnable_Type()
)
mcmFrCoreTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrCoreTrapEnable.setStatus("mandatory")


class _McmFrPlmTrapEnable_Type(Integer32):
    """Custom type mcmFrPlmTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmFrPlmTrapEnable_Type.__name__ = "Integer32"
_McmFrPlmTrapEnable_Object = MibScalar
mcmFrPlmTrapEnable = _McmFrPlmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 1, 17),
    _McmFrPlmTrapEnable_Type()
)
mcmFrPlmTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPlmTrapEnable.setStatus("mandatory")
_McmFrPhyPortTable_Object = MibTable
mcmFrPhyPortTable = _McmFrPhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2)
)
if mibBuilder.loadTexts:
    mcmFrPhyPortTable.setStatus("mandatory")
_McmFrPhyPortEntry_Object = MibTableRow
mcmFrPhyPortEntry = _McmFrPhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1)
)
mcmFrPhyPortEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPhyPortExtIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrPhyPortEntry.setStatus("mandatory")
_McmFrPhyPortExtIfIndex_Type = Integer32
_McmFrPhyPortExtIfIndex_Object = MibTableColumn
mcmFrPhyPortExtIfIndex = _McmFrPhyPortExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 1),
    _McmFrPhyPortExtIfIndex_Type()
)
mcmFrPhyPortExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortExtIfIndex.setStatus("mandatory")


class _McmFrPhyPortFlowControl_Type(Integer32):
    """Custom type mcmFrPhyPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmFrPhyPortFlowControl_Type.__name__ = "Integer32"
_McmFrPhyPortFlowControl_Object = MibTableColumn
mcmFrPhyPortFlowControl = _McmFrPhyPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 2),
    _McmFrPhyPortFlowControl_Type()
)
mcmFrPhyPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortFlowControl.setStatus("mandatory")
_McmFrPhyPortThroughput_Type = Integer32
_McmFrPhyPortThroughput_Object = MibTableColumn
mcmFrPhyPortThroughput = _McmFrPhyPortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 3),
    _McmFrPhyPortThroughput_Type()
)
mcmFrPhyPortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortThroughput.setStatus("deprecated")
_McmFrPhyPortDelta_Type = Integer32
_McmFrPhyPortDelta_Object = MibTableColumn
mcmFrPhyPortDelta = _McmFrPhyPortDelta_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 4),
    _McmFrPhyPortDelta_Type()
)
mcmFrPhyPortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortDelta.setStatus("mandatory")
_McmFrPhyPortConsectiveFrames_Type = Integer32
_McmFrPhyPortConsectiveFrames_Object = MibTableColumn
mcmFrPhyPortConsectiveFrames = _McmFrPhyPortConsectiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 5),
    _McmFrPhyPortConsectiveFrames_Type()
)
mcmFrPhyPortConsectiveFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortConsectiveFrames.setStatus("mandatory")
_McmFrPhyPortMtuSize_Type = Integer32
_McmFrPhyPortMtuSize_Object = MibTableColumn
mcmFrPhyPortMtuSize = _McmFrPhyPortMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 6),
    _McmFrPhyPortMtuSize_Type()
)
mcmFrPhyPortMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortMtuSize.setStatus("deprecated")
_McmFrPhyPortConnectTime_Type = TimeTicks
_McmFrPhyPortConnectTime_Object = MibTableColumn
mcmFrPhyPortConnectTime = _McmFrPhyPortConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 7),
    _McmFrPhyPortConnectTime_Type()
)
mcmFrPhyPortConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortConnectTime.setStatus("mandatory")
_McmFrPhyPortLMISent_Type = Counter32
_McmFrPhyPortLMISent_Object = MibTableColumn
mcmFrPhyPortLMISent = _McmFrPhyPortLMISent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 8),
    _McmFrPhyPortLMISent_Type()
)
mcmFrPhyPortLMISent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortLMISent.setStatus("mandatory")
_McmFrPhyPortLMIReceived_Type = Counter32
_McmFrPhyPortLMIReceived_Object = MibTableColumn
mcmFrPhyPortLMIReceived = _McmFrPhyPortLMIReceived_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 9),
    _McmFrPhyPortLMIReceived_Type()
)
mcmFrPhyPortLMIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortLMIReceived.setStatus("mandatory")
_McmFrPhyPortXIDSent_Type = Counter32
_McmFrPhyPortXIDSent_Object = MibTableColumn
mcmFrPhyPortXIDSent = _McmFrPhyPortXIDSent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 10),
    _McmFrPhyPortXIDSent_Type()
)
mcmFrPhyPortXIDSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortXIDSent.setStatus("mandatory")
_McmFrPhyPortXIDReceived_Type = Counter32
_McmFrPhyPortXIDReceived_Object = MibTableColumn
mcmFrPhyPortXIDReceived = _McmFrPhyPortXIDReceived_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 11),
    _McmFrPhyPortXIDReceived_Type()
)
mcmFrPhyPortXIDReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortXIDReceived.setStatus("mandatory")
_McmFrPhyPortCLLMSent_Type = Counter32
_McmFrPhyPortCLLMSent_Object = MibTableColumn
mcmFrPhyPortCLLMSent = _McmFrPhyPortCLLMSent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 12),
    _McmFrPhyPortCLLMSent_Type()
)
mcmFrPhyPortCLLMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortCLLMSent.setStatus("mandatory")
_McmFrPhyPortCLLMReceived_Type = Counter32
_McmFrPhyPortCLLMReceived_Object = MibTableColumn
mcmFrPhyPortCLLMReceived = _McmFrPhyPortCLLMReceived_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 13),
    _McmFrPhyPortCLLMReceived_Type()
)
mcmFrPhyPortCLLMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortCLLMReceived.setStatus("mandatory")
_McmFrPhyPortHeaderErrors_Type = Counter32
_McmFrPhyPortHeaderErrors_Object = MibTableColumn
mcmFrPhyPortHeaderErrors = _McmFrPhyPortHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 14),
    _McmFrPhyPortHeaderErrors_Type()
)
mcmFrPhyPortHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortHeaderErrors.setStatus("mandatory")
_McmFrPhyPortInvalidDLCI_Type = Counter32
_McmFrPhyPortInvalidDLCI_Object = MibTableColumn
mcmFrPhyPortInvalidDLCI = _McmFrPhyPortInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 15),
    _McmFrPhyPortInvalidDLCI_Type()
)
mcmFrPhyPortInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortInvalidDLCI.setStatus("mandatory")
_McmFrPhyPortShortFrames_Type = Counter32
_McmFrPhyPortShortFrames_Object = MibTableColumn
mcmFrPhyPortShortFrames = _McmFrPhyPortShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 16),
    _McmFrPhyPortShortFrames_Type()
)
mcmFrPhyPortShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortShortFrames.setStatus("mandatory")
_McmFrPhyPortLongFrames_Type = Counter32
_McmFrPhyPortLongFrames_Object = MibTableColumn
mcmFrPhyPortLongFrames = _McmFrPhyPortLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 17),
    _McmFrPhyPortLongFrames_Type()
)
mcmFrPhyPortLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortLongFrames.setStatus("mandatory")
_McmFrPhyPortIgnoredFrames_Type = Counter32
_McmFrPhyPortIgnoredFrames_Object = MibTableColumn
mcmFrPhyPortIgnoredFrames = _McmFrPhyPortIgnoredFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 18),
    _McmFrPhyPortIgnoredFrames_Type()
)
mcmFrPhyPortIgnoredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortIgnoredFrames.setStatus("mandatory")
_McmFrPhyPortXIDExpirations_Type = Counter32
_McmFrPhyPortXIDExpirations_Object = MibTableColumn
mcmFrPhyPortXIDExpirations = _McmFrPhyPortXIDExpirations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 19),
    _McmFrPhyPortXIDExpirations_Type()
)
mcmFrPhyPortXIDExpirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortXIDExpirations.setStatus("mandatory")
_McmFrPhyPortTxExpirations_Type = Counter32
_McmFrPhyPortTxExpirations_Object = MibTableColumn
mcmFrPhyPortTxExpirations = _McmFrPhyPortTxExpirations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 20),
    _McmFrPhyPortTxExpirations_Type()
)
mcmFrPhyPortTxExpirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxExpirations.setStatus("mandatory")


class _McmFrPhyPortPVCLMIStatus_Type(Integer32):
    """Custom type mcmFrPhyPortPVCLMIStatus based on Integer32"""
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


_McmFrPhyPortPVCLMIStatus_Type.__name__ = "Integer32"
_McmFrPhyPortPVCLMIStatus_Object = MibTableColumn
mcmFrPhyPortPVCLMIStatus = _McmFrPhyPortPVCLMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 21),
    _McmFrPhyPortPVCLMIStatus_Type()
)
mcmFrPhyPortPVCLMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortPVCLMIStatus.setStatus("mandatory")


class _McmFrPhyPortSVCLMIStatus_Type(Integer32):
    """Custom type mcmFrPhyPortSVCLMIStatus based on Integer32"""
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


_McmFrPhyPortSVCLMIStatus_Type.__name__ = "Integer32"
_McmFrPhyPortSVCLMIStatus_Object = MibTableColumn
mcmFrPhyPortSVCLMIStatus = _McmFrPhyPortSVCLMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 22),
    _McmFrPhyPortSVCLMIStatus_Type()
)
mcmFrPhyPortSVCLMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortSVCLMIStatus.setStatus("obsolete")
_McmFrPhyPortActivePanlDlciSVCs_Type = Counter32
_McmFrPhyPortActivePanlDlciSVCs_Object = MibTableColumn
mcmFrPhyPortActivePanlDlciSVCs = _McmFrPhyPortActivePanlDlciSVCs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 23),
    _McmFrPhyPortActivePanlDlciSVCs_Type()
)
mcmFrPhyPortActivePanlDlciSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortActivePanlDlciSVCs.setStatus("mandatory")
_McmFrPhyPortRxDataFrames_Type = Counter32
_McmFrPhyPortRxDataFrames_Object = MibTableColumn
mcmFrPhyPortRxDataFrames = _McmFrPhyPortRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 24),
    _McmFrPhyPortRxDataFrames_Type()
)
mcmFrPhyPortRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxDataFrames.setStatus("deprecated")
_McmFrPhyPortTxDataFrames_Type = Counter32
_McmFrPhyPortTxDataFrames_Object = MibTableColumn
mcmFrPhyPortTxDataFrames = _McmFrPhyPortTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 25),
    _McmFrPhyPortTxDataFrames_Type()
)
mcmFrPhyPortTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxDataFrames.setStatus("deprecated")
_McmFrPhyPortRxActivations_Type = Counter32
_McmFrPhyPortRxActivations_Object = MibTableColumn
mcmFrPhyPortRxActivations = _McmFrPhyPortRxActivations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 26),
    _McmFrPhyPortRxActivations_Type()
)
mcmFrPhyPortRxActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxActivations.setStatus("mandatory")
_McmFrPhyPortRxDeactivations_Type = Counter32
_McmFrPhyPortRxDeactivations_Object = MibTableColumn
mcmFrPhyPortRxDeactivations = _McmFrPhyPortRxDeactivations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 27),
    _McmFrPhyPortRxDeactivations_Type()
)
mcmFrPhyPortRxDeactivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxDeactivations.setStatus("mandatory")
_McmFrPhyPortRxOkAcks_Type = Counter32
_McmFrPhyPortRxOkAcks_Object = MibTableColumn
mcmFrPhyPortRxOkAcks = _McmFrPhyPortRxOkAcks_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 28),
    _McmFrPhyPortRxOkAcks_Type()
)
mcmFrPhyPortRxOkAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxOkAcks.setStatus("mandatory")
_McmFrPhyPortRxErrAcks_Type = Counter32
_McmFrPhyPortRxErrAcks_Object = MibTableColumn
mcmFrPhyPortRxErrAcks = _McmFrPhyPortRxErrAcks_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 29),
    _McmFrPhyPortRxErrAcks_Type()
)
mcmFrPhyPortRxErrAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxErrAcks.setStatus("mandatory")
_McmFrPhyPortRxUnknowns_Type = Counter32
_McmFrPhyPortRxUnknowns_Object = MibTableColumn
mcmFrPhyPortRxUnknowns = _McmFrPhyPortRxUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 30),
    _McmFrPhyPortRxUnknowns_Type()
)
mcmFrPhyPortRxUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxUnknowns.setStatus("mandatory")
_McmFrPhyPortRxErrors_Type = Counter32
_McmFrPhyPortRxErrors_Object = MibTableColumn
mcmFrPhyPortRxErrors = _McmFrPhyPortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 31),
    _McmFrPhyPortRxErrors_Type()
)
mcmFrPhyPortRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxErrors.setStatus("mandatory")
_McmFrPhyPortRxOctets_Type = Counter32
_McmFrPhyPortRxOctets_Object = MibTableColumn
mcmFrPhyPortRxOctets = _McmFrPhyPortRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 32),
    _McmFrPhyPortRxOctets_Type()
)
mcmFrPhyPortRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxOctets.setStatus("mandatory")
_McmFrPhyPortTxOctets_Type = Counter32
_McmFrPhyPortTxOctets_Object = MibTableColumn
mcmFrPhyPortTxOctets = _McmFrPhyPortTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 33),
    _McmFrPhyPortTxOctets_Type()
)
mcmFrPhyPortTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxOctets.setStatus("mandatory")
_McmFrPhyPortTxThroughput_Type = Integer32
_McmFrPhyPortTxThroughput_Object = MibTableColumn
mcmFrPhyPortTxThroughput = _McmFrPhyPortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 34),
    _McmFrPhyPortTxThroughput_Type()
)
mcmFrPhyPortTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxThroughput.setStatus("mandatory")
_McmFrPhyPortRxThroughput_Type = Integer32
_McmFrPhyPortRxThroughput_Object = MibTableColumn
mcmFrPhyPortRxThroughput = _McmFrPhyPortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 35),
    _McmFrPhyPortRxThroughput_Type()
)
mcmFrPhyPortRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxThroughput.setStatus("mandatory")
_McmFrPhyPortTxMaxFrameSize_Type = Integer32
_McmFrPhyPortTxMaxFrameSize_Object = MibTableColumn
mcmFrPhyPortTxMaxFrameSize = _McmFrPhyPortTxMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 36),
    _McmFrPhyPortTxMaxFrameSize_Type()
)
mcmFrPhyPortTxMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxMaxFrameSize.setStatus("mandatory")
_McmFrPhyPortRxMaxFrameSize_Type = Integer32
_McmFrPhyPortRxMaxFrameSize_Object = MibTableColumn
mcmFrPhyPortRxMaxFrameSize = _McmFrPhyPortRxMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 37),
    _McmFrPhyPortRxMaxFrameSize_Type()
)
mcmFrPhyPortRxMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxMaxFrameSize.setStatus("mandatory")


class _McmFrPhyPortRateEnf_Type(Integer32):
    """Custom type mcmFrPhyPortRateEnf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmFrPhyPortRateEnf_Type.__name__ = "Integer32"
_McmFrPhyPortRateEnf_Object = MibTableColumn
mcmFrPhyPortRateEnf = _McmFrPhyPortRateEnf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 38),
    _McmFrPhyPortRateEnf_Type()
)
mcmFrPhyPortRateEnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRateEnf.setStatus("mandatory")
_McmFrPhyPortTxBc_Type = Integer32
_McmFrPhyPortTxBc_Object = MibTableColumn
mcmFrPhyPortTxBc = _McmFrPhyPortTxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 39),
    _McmFrPhyPortTxBc_Type()
)
mcmFrPhyPortTxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxBc.setStatus("mandatory")
_McmFrPhyPortRxBc_Type = Integer32
_McmFrPhyPortRxBc_Object = MibTableColumn
mcmFrPhyPortRxBc = _McmFrPhyPortRxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 40),
    _McmFrPhyPortRxBc_Type()
)
mcmFrPhyPortRxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxBc.setStatus("mandatory")
_McmFrPhyPortTxBe_Type = Integer32
_McmFrPhyPortTxBe_Object = MibTableColumn
mcmFrPhyPortTxBe = _McmFrPhyPortTxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 41),
    _McmFrPhyPortTxBe_Type()
)
mcmFrPhyPortTxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortTxBe.setStatus("mandatory")
_McmFrPhyPortRxBe_Type = Integer32
_McmFrPhyPortRxBe_Object = MibTableColumn
mcmFrPhyPortRxBe = _McmFrPhyPortRxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 42),
    _McmFrPhyPortRxBe_Type()
)
mcmFrPhyPortRxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortRxBe.setStatus("mandatory")
_McmFrPhyPortDataFrames_Type = Counter32
_McmFrPhyPortDataFrames_Object = MibTableColumn
mcmFrPhyPortDataFrames = _McmFrPhyPortDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 2, 1, 43),
    _McmFrPhyPortDataFrames_Type()
)
mcmFrPhyPortDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortDataFrames.setStatus("mandatory")
_McmFrPVCPhyTable_Object = MibTable
mcmFrPVCPhyTable = _McmFrPVCPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 3)
)
if mibBuilder.loadTexts:
    mcmFrPVCPhyTable.setStatus("mandatory")
_McmFrPVCPhyEntry_Object = MibTableRow
mcmFrPVCPhyEntry = _McmFrPVCPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 3, 1)
)
mcmFrPVCPhyEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPVCPhyIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrPVCPhyEntry.setStatus("mandatory")
_McmFrPVCPhyIfIndex_Type = Integer32
_McmFrPVCPhyIfIndex_Object = MibTableColumn
mcmFrPVCPhyIfIndex = _McmFrPVCPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 3, 1, 1),
    _McmFrPVCPhyIfIndex_Type()
)
mcmFrPVCPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCPhyIfIndex.setStatus("mandatory")


class _McmFrPVCLMIMode_Type(Integer32):
    """Custom type mcmFrPVCLMIMode based on Integer32"""
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


_McmFrPVCLMIMode_Type.__name__ = "Integer32"
_McmFrPVCLMIMode_Object = MibTableColumn
mcmFrPVCLMIMode = _McmFrPVCLMIMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 3, 1, 2),
    _McmFrPVCLMIMode_Type()
)
mcmFrPVCLMIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCLMIMode.setStatus("mandatory")


class _McmFrPVCBiDir_Type(Integer32):
    """Custom type mcmFrPVCBiDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_McmFrPVCBiDir_Type.__name__ = "Integer32"
_McmFrPVCBiDir_Object = MibTableColumn
mcmFrPVCBiDir = _McmFrPVCBiDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 3, 1, 3),
    _McmFrPVCBiDir_Type()
)
mcmFrPVCBiDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCBiDir.setStatus("mandatory")
_McmFrSVCPhyTable_Object = MibTable
mcmFrSVCPhyTable = _McmFrSVCPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4)
)
if mibBuilder.loadTexts:
    mcmFrSVCPhyTable.setStatus("mandatory")
_McmFrSVCPhyEntry_Object = MibTableRow
mcmFrSVCPhyEntry = _McmFrSVCPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1)
)
mcmFrSVCPhyEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCPhyIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrSVCPhyEntry.setStatus("mandatory")
_McmFrSVCPhyIfIndex_Type = Integer32
_McmFrSVCPhyIfIndex_Object = MibTableColumn
mcmFrSVCPhyIfIndex = _McmFrSVCPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 1),
    _McmFrSVCPhyIfIndex_Type()
)
mcmFrSVCPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCPhyIfIndex.setStatus("mandatory")


class _McmFrSVCState_Type(Integer32):
    """Custom type mcmFrSVCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("q933svc", 1)
    )


_McmFrSVCState_Type.__name__ = "Integer32"
_McmFrSVCState_Object = MibTableColumn
mcmFrSVCState = _McmFrSVCState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 2),
    _McmFrSVCState_Type()
)
mcmFrSVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCState.setStatus("mandatory")
_McmFrSVCT303_Type = Integer32
_McmFrSVCT303_Object = MibTableColumn
mcmFrSVCT303 = _McmFrSVCT303_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 3),
    _McmFrSVCT303_Type()
)
mcmFrSVCT303.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCT303.setStatus("mandatory")
_McmFrSVCT305_Type = Integer32
_McmFrSVCT305_Object = MibTableColumn
mcmFrSVCT305 = _McmFrSVCT305_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 4),
    _McmFrSVCT305_Type()
)
mcmFrSVCT305.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCT305.setStatus("mandatory")
_McmFrSVCT308_Type = Integer32
_McmFrSVCT308_Object = MibTableColumn
mcmFrSVCT308 = _McmFrSVCT308_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 5),
    _McmFrSVCT308_Type()
)
mcmFrSVCT308.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCT308.setStatus("mandatory")
_McmFrSVCT310_Type = Integer32
_McmFrSVCT310_Object = MibTableColumn
mcmFrSVCT310 = _McmFrSVCT310_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 6),
    _McmFrSVCT310_Type()
)
mcmFrSVCT310.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCT310.setStatus("mandatory")


class _McmFrSVCMaxCalls_Type(Integer32):
    """Custom type mcmFrSVCMaxCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrSVCMaxCalls_Type.__name__ = "Integer32"
_McmFrSVCMaxCalls_Object = MibTableColumn
mcmFrSVCMaxCalls = _McmFrSVCMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 7),
    _McmFrSVCMaxCalls_Type()
)
mcmFrSVCMaxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMaxCalls.setStatus("mandatory")
_McmFrSVCMaxTxSize_Type = Integer32
_McmFrSVCMaxTxSize_Object = MibTableColumn
mcmFrSVCMaxTxSize = _McmFrSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 8),
    _McmFrSVCMaxTxSize_Type()
)
mcmFrSVCMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMaxTxSize.setStatus("mandatory")
_McmFrSVCMaxRxSize_Type = Integer32
_McmFrSVCMaxRxSize_Object = MibTableColumn
mcmFrSVCMaxRxSize = _McmFrSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 9),
    _McmFrSVCMaxRxSize_Type()
)
mcmFrSVCMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMaxRxSize.setStatus("mandatory")
_McmFrSVCMinDLCI_Type = Integer32
_McmFrSVCMinDLCI_Object = MibTableColumn
mcmFrSVCMinDLCI = _McmFrSVCMinDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 10),
    _McmFrSVCMinDLCI_Type()
)
mcmFrSVCMinDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMinDLCI.setStatus("mandatory")
_McmFrSVCMaxDLCI_Type = Integer32
_McmFrSVCMaxDLCI_Object = MibTableColumn
mcmFrSVCMaxDLCI = _McmFrSVCMaxDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 11),
    _McmFrSVCMaxDLCI_Type()
)
mcmFrSVCMaxDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMaxDLCI.setStatus("mandatory")
_McmFrSVCMinTxThroughput_Type = Integer32
_McmFrSVCMinTxThroughput_Object = MibTableColumn
mcmFrSVCMinTxThroughput = _McmFrSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 12),
    _McmFrSVCMinTxThroughput_Type()
)
mcmFrSVCMinTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMinTxThroughput.setStatus("mandatory")
_McmFrSVCMinRxThroughput_Type = Integer32
_McmFrSVCMinRxThroughput_Object = MibTableColumn
mcmFrSVCMinRxThroughput = _McmFrSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 13),
    _McmFrSVCMinRxThroughput_Type()
)
mcmFrSVCMinRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMinRxThroughput.setStatus("mandatory")
_McmFrSVCMaxTxThroughput_Type = Integer32
_McmFrSVCMaxTxThroughput_Object = MibTableColumn
mcmFrSVCMaxTxThroughput = _McmFrSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 14),
    _McmFrSVCMaxTxThroughput_Type()
)
mcmFrSVCMaxTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMaxTxThroughput.setStatus("mandatory")
_McmFrSVCMaxRxThroughput_Type = Integer32
_McmFrSVCMaxRxThroughput_Object = MibTableColumn
mcmFrSVCMaxRxThroughput = _McmFrSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 15),
    _McmFrSVCMaxRxThroughput_Type()
)
mcmFrSVCMaxRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMaxRxThroughput.setStatus("mandatory")
_McmFrSVCTxBurstSize_Type = Integer32
_McmFrSVCTxBurstSize_Object = MibTableColumn
mcmFrSVCTxBurstSize = _McmFrSVCTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 16),
    _McmFrSVCTxBurstSize_Type()
)
mcmFrSVCTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCTxBurstSize.setStatus("mandatory")
_McmFrSVCRxBurstSize_Type = Integer32
_McmFrSVCRxBurstSize_Object = MibTableColumn
mcmFrSVCRxBurstSize = _McmFrSVCRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 17),
    _McmFrSVCRxBurstSize_Type()
)
mcmFrSVCRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCRxBurstSize.setStatus("mandatory")
_McmFrSVCExcessTxBurstSize_Type = Integer32
_McmFrSVCExcessTxBurstSize_Object = MibTableColumn
mcmFrSVCExcessTxBurstSize = _McmFrSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 18),
    _McmFrSVCExcessTxBurstSize_Type()
)
mcmFrSVCExcessTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCExcessTxBurstSize.setStatus("mandatory")
_McmFrSVCExcessRxBurstSize_Type = Integer32
_McmFrSVCExcessRxBurstSize_Object = MibTableColumn
mcmFrSVCExcessRxBurstSize = _McmFrSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 4, 1, 19),
    _McmFrSVCExcessRxBurstSize_Type()
)
mcmFrSVCExcessRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCExcessRxBurstSize.setStatus("mandatory")
_McmFrVirtualPortTable_Object = MibTable
mcmFrVirtualPortTable = _McmFrVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5)
)
if mibBuilder.loadTexts:
    mcmFrVirtualPortTable.setStatus("mandatory")
_McmFrVirtualPortEntry_Object = MibTableRow
mcmFrVirtualPortEntry = _McmFrVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1)
)
mcmFrVirtualPortEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrVirtualPortIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrVirtualPortEntry.setStatus("mandatory")


class _McmFrVirtualPortIfIndex_Type(Integer32):
    """Custom type mcmFrVirtualPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrVirtualPortIfIndex_Type.__name__ = "Integer32"
_McmFrVirtualPortIfIndex_Object = MibTableColumn
mcmFrVirtualPortIfIndex = _McmFrVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 1),
    _McmFrVirtualPortIfIndex_Type()
)
mcmFrVirtualPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortIfIndex.setStatus("mandatory")


class _McmFrVirtualPortPhyPortIfIndex_Type(Integer32):
    """Custom type mcmFrVirtualPortPhyPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrVirtualPortPhyPortIfIndex_Type.__name__ = "Integer32"
_McmFrVirtualPortPhyPortIfIndex_Object = MibTableColumn
mcmFrVirtualPortPhyPortIfIndex = _McmFrVirtualPortPhyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 2),
    _McmFrVirtualPortPhyPortIfIndex_Type()
)
mcmFrVirtualPortPhyPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortPhyPortIfIndex.setStatus("obsolete")


class _McmFrVirtualPortPPA_Type(Integer32):
    """Custom type mcmFrVirtualPortPPA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_McmFrVirtualPortPPA_Type.__name__ = "Integer32"
_McmFrVirtualPortPPA_Object = MibTableColumn
mcmFrVirtualPortPPA = _McmFrVirtualPortPPA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 3),
    _McmFrVirtualPortPPA_Type()
)
mcmFrVirtualPortPPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortPPA.setStatus("obsolete")


class _McmFrVirtualPortMode_Type(Integer32):
    """Custom type mcmFrVirtualPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("easyRouting", 2))
    )


_McmFrVirtualPortMode_Type.__name__ = "Integer32"
_McmFrVirtualPortMode_Object = MibTableColumn
mcmFrVirtualPortMode = _McmFrVirtualPortMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 4),
    _McmFrVirtualPortMode_Type()
)
mcmFrVirtualPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortMode.setStatus("mandatory")


class _McmFrVirtualPortState_Type(Integer32):
    """Custom type mcmFrVirtualPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("uninitialized", 3),
          ("up", 1))
    )


_McmFrVirtualPortState_Type.__name__ = "Integer32"
_McmFrVirtualPortState_Object = MibTableColumn
mcmFrVirtualPortState = _McmFrVirtualPortState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 5),
    _McmFrVirtualPortState_Type()
)
mcmFrVirtualPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortState.setStatus("mandatory")


class _McmFrVirtualPortEntryStatus_Type(Integer32):
    """Custom type mcmFrVirtualPortEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_McmFrVirtualPortEntryStatus_Type.__name__ = "Integer32"
_McmFrVirtualPortEntryStatus_Object = MibTableColumn
mcmFrVirtualPortEntryStatus = _McmFrVirtualPortEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 6),
    _McmFrVirtualPortEntryStatus_Type()
)
mcmFrVirtualPortEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortEntryStatus.setStatus("mandatory")


class _McmFrVirtualPortProtocolBinding_Type(Integer32):
    """Custom type mcmFrVirtualPortProtocolBinding based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bridge-configured", 4),
          ("ip-and-bridge-configured", 5),
          ("ip-and-ipx-and-bridge-configured", 7),
          ("ip-and-ipx-configured", 3),
          ("ip-configured", 1),
          ("ipx-and-bridge-configured", 6),
          ("ipx-configured", 2),
          ("sNA-configured", 8),
          ("x25-configured", 9))
    )


_McmFrVirtualPortProtocolBinding_Type.__name__ = "Integer32"
_McmFrVirtualPortProtocolBinding_Object = MibTableColumn
mcmFrVirtualPortProtocolBinding = _McmFrVirtualPortProtocolBinding_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 7),
    _McmFrVirtualPortProtocolBinding_Type()
)
mcmFrVirtualPortProtocolBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortProtocolBinding.setStatus("mandatory")
_McmFrVirtualPortNumber_Type = Integer32
_McmFrVirtualPortNumber_Object = MibTableColumn
mcmFrVirtualPortNumber = _McmFrVirtualPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 5, 1, 8),
    _McmFrVirtualPortNumber_Type()
)
mcmFrVirtualPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortNumber.setStatus("mandatory")
_McmFrSVCMapTable_Object = MibTable
mcmFrSVCMapTable = _McmFrSVCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6)
)
if mibBuilder.loadTexts:
    mcmFrSVCMapTable.setStatus("mandatory")
_McmFrSVCMapEntry_Object = MibTableRow
mcmFrSVCMapEntry = _McmFrSVCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1)
)
mcmFrSVCMapEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCMapVirtualPortIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCMapDNA"),
)
if mibBuilder.loadTexts:
    mcmFrSVCMapEntry.setStatus("mandatory")
_McmFrSVCMapVirtualPortIfIndex_Type = Integer32
_McmFrSVCMapVirtualPortIfIndex_Object = MibTableColumn
mcmFrSVCMapVirtualPortIfIndex = _McmFrSVCMapVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 1),
    _McmFrSVCMapVirtualPortIfIndex_Type()
)
mcmFrSVCMapVirtualPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapVirtualPortIfIndex.setStatus("mandatory")
_McmFrSVCMapDNA_Type = OctetString
_McmFrSVCMapDNA_Object = MibTableColumn
mcmFrSVCMapDNA = _McmFrSVCMapDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 2),
    _McmFrSVCMapDNA_Type()
)
mcmFrSVCMapDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapDNA.setStatus("mandatory")
_McmFrSVCMapDLCI_Type = Integer32
_McmFrSVCMapDLCI_Object = MibTableColumn
mcmFrSVCMapDLCI = _McmFrSVCMapDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 3),
    _McmFrSVCMapDLCI_Type()
)
mcmFrSVCMapDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapDLCI.setStatus("mandatory")
_McmFrSVCMapMaxTxSize_Type = Integer32
_McmFrSVCMapMaxTxSize_Object = MibTableColumn
mcmFrSVCMapMaxTxSize = _McmFrSVCMapMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 4),
    _McmFrSVCMapMaxTxSize_Type()
)
mcmFrSVCMapMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapMaxTxSize.setStatus("mandatory")
_McmFrSVCMapMaxRxSize_Type = Integer32
_McmFrSVCMapMaxRxSize_Object = MibTableColumn
mcmFrSVCMapMaxRxSize = _McmFrSVCMapMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 5),
    _McmFrSVCMapMaxRxSize_Type()
)
mcmFrSVCMapMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapMaxRxSize.setStatus("mandatory")
_McmFrSVCMapMinTxThroughput_Type = Integer32
_McmFrSVCMapMinTxThroughput_Object = MibTableColumn
mcmFrSVCMapMinTxThroughput = _McmFrSVCMapMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 6),
    _McmFrSVCMapMinTxThroughput_Type()
)
mcmFrSVCMapMinTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapMinTxThroughput.setStatus("mandatory")
_McmFrSVCMapMinRxThroughput_Type = Integer32
_McmFrSVCMapMinRxThroughput_Object = MibTableColumn
mcmFrSVCMapMinRxThroughput = _McmFrSVCMapMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 7),
    _McmFrSVCMapMinRxThroughput_Type()
)
mcmFrSVCMapMinRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapMinRxThroughput.setStatus("mandatory")
_McmFrSVCMapMaxTxThroughput_Type = Integer32
_McmFrSVCMapMaxTxThroughput_Object = MibTableColumn
mcmFrSVCMapMaxTxThroughput = _McmFrSVCMapMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 8),
    _McmFrSVCMapMaxTxThroughput_Type()
)
mcmFrSVCMapMaxTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapMaxTxThroughput.setStatus("mandatory")
_McmFrSVCMapMaxRxThroughput_Type = Integer32
_McmFrSVCMapMaxRxThroughput_Object = MibTableColumn
mcmFrSVCMapMaxRxThroughput = _McmFrSVCMapMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 9),
    _McmFrSVCMapMaxRxThroughput_Type()
)
mcmFrSVCMapMaxRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapMaxRxThroughput.setStatus("mandatory")
_McmFrSVCMapTxBurstSize_Type = Integer32
_McmFrSVCMapTxBurstSize_Object = MibTableColumn
mcmFrSVCMapTxBurstSize = _McmFrSVCMapTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 10),
    _McmFrSVCMapTxBurstSize_Type()
)
mcmFrSVCMapTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapTxBurstSize.setStatus("mandatory")
_McmFrSVCMapRxBurstSize_Type = Integer32
_McmFrSVCMapRxBurstSize_Object = MibTableColumn
mcmFrSVCMapRxBurstSize = _McmFrSVCMapRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 11),
    _McmFrSVCMapRxBurstSize_Type()
)
mcmFrSVCMapRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapRxBurstSize.setStatus("mandatory")
_McmFrSVCMapExcessTxBurstSize_Type = Integer32
_McmFrSVCMapExcessTxBurstSize_Object = MibTableColumn
mcmFrSVCMapExcessTxBurstSize = _McmFrSVCMapExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 12),
    _McmFrSVCMapExcessTxBurstSize_Type()
)
mcmFrSVCMapExcessTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapExcessTxBurstSize.setStatus("mandatory")
_McmFrSVCMapExcessRxBurstSize_Type = Integer32
_McmFrSVCMapExcessRxBurstSize_Object = MibTableColumn
mcmFrSVCMapExcessRxBurstSize = _McmFrSVCMapExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 13),
    _McmFrSVCMapExcessRxBurstSize_Type()
)
mcmFrSVCMapExcessRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapExcessRxBurstSize.setStatus("mandatory")
_McmFrSVCMapPriority_Type = Integer32
_McmFrSVCMapPriority_Object = MibTableColumn
mcmFrSVCMapPriority = _McmFrSVCMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 14),
    _McmFrSVCMapPriority_Type()
)
mcmFrSVCMapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapPriority.setStatus("mandatory")


class _McmFrSVCMapEntryStatus_Type(Integer32):
    """Custom type mcmFrSVCMapEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_McmFrSVCMapEntryStatus_Type.__name__ = "Integer32"
_McmFrSVCMapEntryStatus_Object = MibTableColumn
mcmFrSVCMapEntryStatus = _McmFrSVCMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 15),
    _McmFrSVCMapEntryStatus_Type()
)
mcmFrSVCMapEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapEntryStatus.setStatus("mandatory")


class _McmFrSVCMapTransferPriority_Type(Integer32):
    """Custom type mcmFrSVCMapTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmFrSVCMapTransferPriority_Type.__name__ = "Integer32"
_McmFrSVCMapTransferPriority_Object = MibTableColumn
mcmFrSVCMapTransferPriority = _McmFrSVCMapTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 16),
    _McmFrSVCMapTransferPriority_Type()
)
mcmFrSVCMapTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapTransferPriority.setStatus("mandatory")


class _McmFrSVCMapDisableCause_Type(Integer32):
    """Custom type mcmFrSVCMapDisableCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              21,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              47,
              49,
              50,
              57,
              58,
              63,
              65,
              66,
              70,
              79,
              81,
              82,
              87,
              88,
              90,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              111,
              127,
              128)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-implemented", 65),
          ("bearer-capability-not-presently-available", 58),
          ("call-awarded-and-being-delivered-in-an-est-channel", 7),
          ("channel-type-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("destination-out-of-order", 27),
          ("element-non-existent-or-not-implemented", 99),
          ("facility-rejected", 29),
          ("identified-channel-does-not-exist", 82),
          ("incompatible-destination", 88),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-element", 100),
          ("invalid-message-for-state", 101),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network-selection", 91),
          ("message-not-compatible", 98),
          ("message-type-unknown", 97),
          ("missing-element", 96),
          ("network-out-of-order", 38),
          ("no-DLCI-available", 34),
          ("no-route-to-destination", 3),
          ("no-route-to-specified-transit-network", 2),
          ("no-user-present-in-call", 18),
          ("non-existent-CUG", 90),
          ("normal-call-clearing", 16),
          ("normal-condition", 128),
          ("normal-unspecified", 31),
          ("only-restricted-digital-capability-is-available", 70),
          ("permanent-frame-mode-connection-operational", 40),
          ("permanent-frame-mode-connection-out-of-service", 39),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-not-available", 49),
          ("remote-PVC-already-connected-ie-busy", 17),
          ("remote-PVC-down-ie-unavailable", 21),
          ("requested-facility-not-subscribed", 50),
          ("resource-unavailable", 47),
          ("response-to-status-inquiry", 30),
          ("service-or-option-not-available-unspecified", 63),
          ("service-or-option-not-implemented-unspecified", 79),
          ("specified-DLCI-unavailable", 44),
          ("switching-equipment-congestion", 42),
          ("temporary-failure", 41),
          ("the-PVC-does-not-exist-ie-unassigned", 1),
          ("timer-recovery", 102),
          ("user-not-member-of-CUG", 87))
    )


_McmFrSVCMapDisableCause_Type.__name__ = "Integer32"
_McmFrSVCMapDisableCause_Object = MibTableColumn
mcmFrSVCMapDisableCause = _McmFrSVCMapDisableCause_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 17),
    _McmFrSVCMapDisableCause_Type()
)
mcmFrSVCMapDisableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapDisableCause.setStatus("mandatory")
_McmFrSvcMapSvcIfIndex_Type = Integer32
_McmFrSvcMapSvcIfIndex_Object = MibTableColumn
mcmFrSvcMapSvcIfIndex = _McmFrSvcMapSvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 18),
    _McmFrSvcMapSvcIfIndex_Type()
)
mcmFrSvcMapSvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSvcMapSvcIfIndex.setStatus("mandatory")


class _McmFrSVCMapDiscardPriority_Type(Integer32):
    """Custom type mcmFrSVCMapDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_McmFrSVCMapDiscardPriority_Type.__name__ = "Integer32"
_McmFrSVCMapDiscardPriority_Object = MibTableColumn
mcmFrSVCMapDiscardPriority = _McmFrSVCMapDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 19),
    _McmFrSVCMapDiscardPriority_Type()
)
mcmFrSVCMapDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapDiscardPriority.setStatus("mandatory")


class _McmFrSVCMapSetupPriority_Type(Integer32):
    """Custom type mcmFrSVCMapSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrSVCMapSetupPriority_Type.__name__ = "Integer32"
_McmFrSVCMapSetupPriority_Object = MibTableColumn
mcmFrSVCMapSetupPriority = _McmFrSVCMapSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 20),
    _McmFrSVCMapSetupPriority_Type()
)
mcmFrSVCMapSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapSetupPriority.setStatus("mandatory")


class _McmFrSVCMapHoldingPriority_Type(Integer32):
    """Custom type mcmFrSVCMapHoldingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrSVCMapHoldingPriority_Type.__name__ = "Integer32"
_McmFrSVCMapHoldingPriority_Object = MibTableColumn
mcmFrSVCMapHoldingPriority = _McmFrSVCMapHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 6, 1, 21),
    _McmFrSVCMapHoldingPriority_Type()
)
mcmFrSVCMapHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCMapHoldingPriority.setStatus("mandatory")
_McmFrPVCMapTable_Object = MibTable
mcmFrPVCMapTable = _McmFrPVCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7)
)
if mibBuilder.loadTexts:
    mcmFrPVCMapTable.setStatus("obsolete")
_McmFrPVCMapEntry_Object = MibTableRow
mcmFrPVCMapEntry = _McmFrPVCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7, 1)
)
mcmFrPVCMapEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPVCMapVirtualPortIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPVCMapDLCI"),
)
if mibBuilder.loadTexts:
    mcmFrPVCMapEntry.setStatus("obsolete")
_McmFrPVCMapVirtualPortIfIndex_Type = Integer32
_McmFrPVCMapVirtualPortIfIndex_Object = MibTableColumn
mcmFrPVCMapVirtualPortIfIndex = _McmFrPVCMapVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7, 1, 1),
    _McmFrPVCMapVirtualPortIfIndex_Type()
)
mcmFrPVCMapVirtualPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCMapVirtualPortIfIndex.setStatus("obsolete")
_McmFrPVCMapDLCI_Type = Integer32
_McmFrPVCMapDLCI_Object = MibTableColumn
mcmFrPVCMapDLCI = _McmFrPVCMapDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7, 1, 2),
    _McmFrPVCMapDLCI_Type()
)
mcmFrPVCMapDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCMapDLCI.setStatus("obsolete")


class _McmFrPVCMapState_Type(Integer32):
    """Custom type mcmFrPVCMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_McmFrPVCMapState_Type.__name__ = "Integer32"
_McmFrPVCMapState_Object = MibTableColumn
mcmFrPVCMapState = _McmFrPVCMapState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7, 1, 3),
    _McmFrPVCMapState_Type()
)
mcmFrPVCMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCMapState.setStatus("obsolete")


class _McmFrPVCMapEntryStatus_Type(Integer32):
    """Custom type mcmFrPVCMapEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_McmFrPVCMapEntryStatus_Type.__name__ = "Integer32"
_McmFrPVCMapEntryStatus_Object = MibTableColumn
mcmFrPVCMapEntryStatus = _McmFrPVCMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7, 1, 4),
    _McmFrPVCMapEntryStatus_Type()
)
mcmFrPVCMapEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCMapEntryStatus.setStatus("obsolete")
_McmFrPVCMapPhysIfIndex_Type = Integer32
_McmFrPVCMapPhysIfIndex_Object = MibTableColumn
mcmFrPVCMapPhysIfIndex = _McmFrPVCMapPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 7, 1, 5),
    _McmFrPVCMapPhysIfIndex_Type()
)
mcmFrPVCMapPhysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCMapPhysIfIndex.setStatus("obsolete")
_McmFrSVCCircuitTable_Object = MibTable
mcmFrSVCCircuitTable = _McmFrSVCCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8)
)
if mibBuilder.loadTexts:
    mcmFrSVCCircuitTable.setStatus("mandatory")
_McmFrSVCCircuitEntry_Object = MibTableRow
mcmFrSVCCircuitEntry = _McmFrSVCCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1)
)
mcmFrSVCCircuitEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCCircuitIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCCircuitDNA"),
)
if mibBuilder.loadTexts:
    mcmFrSVCCircuitEntry.setStatus("mandatory")


class _McmFrSVCCircuitIfIndex_Type(Integer32):
    """Custom type mcmFrSVCCircuitIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrSVCCircuitIfIndex_Type.__name__ = "Integer32"
_McmFrSVCCircuitIfIndex_Object = MibTableColumn
mcmFrSVCCircuitIfIndex = _McmFrSVCCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 1),
    _McmFrSVCCircuitIfIndex_Type()
)
mcmFrSVCCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitIfIndex.setStatus("mandatory")


class _McmFrSVCCircuitDNA_Type(OctetString):
    """Custom type mcmFrSVCCircuitDNA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrSVCCircuitDNA_Type.__name__ = "OctetString"
_McmFrSVCCircuitDNA_Object = MibTableColumn
mcmFrSVCCircuitDNA = _McmFrSVCCircuitDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 2),
    _McmFrSVCCircuitDNA_Type()
)
mcmFrSVCCircuitDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitDNA.setStatus("mandatory")


class _McmFrSVCCircuitDlci_Type(Integer32):
    """Custom type mcmFrSVCCircuitDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrSVCCircuitDlci_Type.__name__ = "Integer32"
_McmFrSVCCircuitDlci_Object = MibTableColumn
mcmFrSVCCircuitDlci = _McmFrSVCCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 3),
    _McmFrSVCCircuitDlci_Type()
)
mcmFrSVCCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitDlci.setStatus("mandatory")


class _McmFrSVCCircuitState_Type(Integer32):
    """Custom type mcmFrSVCCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_McmFrSVCCircuitState_Type.__name__ = "Integer32"
_McmFrSVCCircuitState_Object = MibTableColumn
mcmFrSVCCircuitState = _McmFrSVCCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 4),
    _McmFrSVCCircuitState_Type()
)
mcmFrSVCCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitState.setStatus("mandatory")
_McmFrSVCCircuitReceivedFECNs_Type = Counter32
_McmFrSVCCircuitReceivedFECNs_Object = MibTableColumn
mcmFrSVCCircuitReceivedFECNs = _McmFrSVCCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 5),
    _McmFrSVCCircuitReceivedFECNs_Type()
)
mcmFrSVCCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitReceivedFECNs.setStatus("mandatory")
_McmFrSVCCircuitReceivedBECNs_Type = Counter32
_McmFrSVCCircuitReceivedBECNs_Object = MibTableColumn
mcmFrSVCCircuitReceivedBECNs = _McmFrSVCCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 6),
    _McmFrSVCCircuitReceivedBECNs_Type()
)
mcmFrSVCCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitReceivedBECNs.setStatus("mandatory")
_McmFrSVCCircuitSentFrames_Type = Counter32
_McmFrSVCCircuitSentFrames_Object = MibTableColumn
mcmFrSVCCircuitSentFrames = _McmFrSVCCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 7),
    _McmFrSVCCircuitSentFrames_Type()
)
mcmFrSVCCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitSentFrames.setStatus("mandatory")
_McmFrSVCCircuitSentOctets_Type = Counter32
_McmFrSVCCircuitSentOctets_Object = MibTableColumn
mcmFrSVCCircuitSentOctets = _McmFrSVCCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 8),
    _McmFrSVCCircuitSentOctets_Type()
)
mcmFrSVCCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitSentOctets.setStatus("mandatory")
_McmFrSVCCircuitReceivedFrames_Type = Counter32
_McmFrSVCCircuitReceivedFrames_Object = MibTableColumn
mcmFrSVCCircuitReceivedFrames = _McmFrSVCCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 9),
    _McmFrSVCCircuitReceivedFrames_Type()
)
mcmFrSVCCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitReceivedFrames.setStatus("mandatory")
_McmFrSVCCircuitReceivedOctets_Type = Counter32
_McmFrSVCCircuitReceivedOctets_Object = MibTableColumn
mcmFrSVCCircuitReceivedOctets = _McmFrSVCCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 10),
    _McmFrSVCCircuitReceivedOctets_Type()
)
mcmFrSVCCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitReceivedOctets.setStatus("mandatory")
_McmFrSVCCircuitCreationTime_Type = TimeTicks
_McmFrSVCCircuitCreationTime_Object = MibTableColumn
mcmFrSVCCircuitCreationTime = _McmFrSVCCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 11),
    _McmFrSVCCircuitCreationTime_Type()
)
mcmFrSVCCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitCreationTime.setStatus("mandatory")


class _McmFrSVCCircuitCallOriginator_Type(OctetString):
    """Custom type mcmFrSVCCircuitCallOriginator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrSVCCircuitCallOriginator_Type.__name__ = "OctetString"
_McmFrSVCCircuitCallOriginator_Object = MibTableColumn
mcmFrSVCCircuitCallOriginator = _McmFrSVCCircuitCallOriginator_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 12),
    _McmFrSVCCircuitCallOriginator_Type()
)
mcmFrSVCCircuitCallOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitCallOriginator.setStatus("mandatory")
_McmFrSVCCircuitLastTimeChange_Type = TimeTicks
_McmFrSVCCircuitLastTimeChange_Object = MibTableColumn
mcmFrSVCCircuitLastTimeChange = _McmFrSVCCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 13),
    _McmFrSVCCircuitLastTimeChange_Type()
)
mcmFrSVCCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitLastTimeChange.setStatus("mandatory")


class _McmFrSVCCircuitCommittedBurst_Type(Integer32):
    """Custom type mcmFrSVCCircuitCommittedBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitCommittedBurst_Type.__name__ = "Integer32"
_McmFrSVCCircuitCommittedBurst_Object = MibTableColumn
mcmFrSVCCircuitCommittedBurst = _McmFrSVCCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 14),
    _McmFrSVCCircuitCommittedBurst_Type()
)
mcmFrSVCCircuitCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitCommittedBurst.setStatus("deprecated")


class _McmFrSVCCircuitExcessBurst_Type(Integer32):
    """Custom type mcmFrSVCCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitExcessBurst_Type.__name__ = "Integer32"
_McmFrSVCCircuitExcessBurst_Object = MibTableColumn
mcmFrSVCCircuitExcessBurst = _McmFrSVCCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 15),
    _McmFrSVCCircuitExcessBurst_Type()
)
mcmFrSVCCircuitExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitExcessBurst.setStatus("deprecated")


class _McmFrSVCCircuitThroughput_Type(Integer32):
    """Custom type mcmFrSVCCircuitThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitThroughput_Type.__name__ = "Integer32"
_McmFrSVCCircuitThroughput_Object = MibTableColumn
mcmFrSVCCircuitThroughput = _McmFrSVCCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 16),
    _McmFrSVCCircuitThroughput_Type()
)
mcmFrSVCCircuitThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitThroughput.setStatus("mandatory")


class _McmFrSVCCircuitNegMaxTxSize_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrSVCCircuitNegMaxTxSize_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegMaxTxSize_Object = MibTableColumn
mcmFrSVCCircuitNegMaxTxSize = _McmFrSVCCircuitNegMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 17),
    _McmFrSVCCircuitNegMaxTxSize_Type()
)
mcmFrSVCCircuitNegMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegMaxTxSize.setStatus("mandatory")


class _McmFrSVCCircuitNegMaxRxSize_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrSVCCircuitNegMaxRxSize_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegMaxRxSize_Object = MibTableColumn
mcmFrSVCCircuitNegMaxRxSize = _McmFrSVCCircuitNegMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 18),
    _McmFrSVCCircuitNegMaxRxSize_Type()
)
mcmFrSVCCircuitNegMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegMaxRxSize.setStatus("mandatory")


class _McmFrSVCCircuitNegTxThroughput_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitNegTxThroughput_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegTxThroughput_Object = MibTableColumn
mcmFrSVCCircuitNegTxThroughput = _McmFrSVCCircuitNegTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 19),
    _McmFrSVCCircuitNegTxThroughput_Type()
)
mcmFrSVCCircuitNegTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegTxThroughput.setStatus("mandatory")


class _McmFrSVCCircuitNegRxThroughput_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitNegRxThroughput_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegRxThroughput_Object = MibTableColumn
mcmFrSVCCircuitNegRxThroughput = _McmFrSVCCircuitNegRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 20),
    _McmFrSVCCircuitNegRxThroughput_Type()
)
mcmFrSVCCircuitNegRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegRxThroughput.setStatus("mandatory")


class _McmFrSVCCircuitNegTxBurst_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegTxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitNegTxBurst_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegTxBurst_Object = MibTableColumn
mcmFrSVCCircuitNegTxBurst = _McmFrSVCCircuitNegTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 21),
    _McmFrSVCCircuitNegTxBurst_Type()
)
mcmFrSVCCircuitNegTxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegTxBurst.setStatus("mandatory")


class _McmFrSVCCircuitNegRxBurst_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegRxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitNegRxBurst_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegRxBurst_Object = MibTableColumn
mcmFrSVCCircuitNegRxBurst = _McmFrSVCCircuitNegRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 22),
    _McmFrSVCCircuitNegRxBurst_Type()
)
mcmFrSVCCircuitNegRxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegRxBurst.setStatus("mandatory")


class _McmFrSVCCircuitNegTxExcess_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegTxExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitNegTxExcess_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegTxExcess_Object = MibTableColumn
mcmFrSVCCircuitNegTxExcess = _McmFrSVCCircuitNegTxExcess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 23),
    _McmFrSVCCircuitNegTxExcess_Type()
)
mcmFrSVCCircuitNegTxExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegTxExcess.setStatus("mandatory")


class _McmFrSVCCircuitNegRxExcess_Type(Integer32):
    """Custom type mcmFrSVCCircuitNegRxExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrSVCCircuitNegRxExcess_Type.__name__ = "Integer32"
_McmFrSVCCircuitNegRxExcess_Object = MibTableColumn
mcmFrSVCCircuitNegRxExcess = _McmFrSVCCircuitNegRxExcess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 24),
    _McmFrSVCCircuitNegRxExcess_Type()
)
mcmFrSVCCircuitNegRxExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitNegRxExcess.setStatus("mandatory")
_McmFrSVCCircuitTxDiscardCIRPolice_Type = Counter32
_McmFrSVCCircuitTxDiscardCIRPolice_Object = MibTableColumn
mcmFrSVCCircuitTxDiscardCIRPolice = _McmFrSVCCircuitTxDiscardCIRPolice_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 25),
    _McmFrSVCCircuitTxDiscardCIRPolice_Type()
)
mcmFrSVCCircuitTxDiscardCIRPolice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitTxDiscardCIRPolice.setStatus("mandatory")


class _McmFrSVCCircuitPriority_Type(Integer32):
    """Custom type mcmFrSVCCircuitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmFrSVCCircuitPriority_Type.__name__ = "Integer32"
_McmFrSVCCircuitPriority_Object = MibTableColumn
mcmFrSVCCircuitPriority = _McmFrSVCCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 26),
    _McmFrSVCCircuitPriority_Type()
)
mcmFrSVCCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitPriority.setStatus("mandatory")
_McmFrSVCCircuitSvcIfIndex_Type = Integer32
_McmFrSVCCircuitSvcIfIndex_Object = MibTableColumn
mcmFrSVCCircuitSvcIfIndex = _McmFrSVCCircuitSvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 27),
    _McmFrSVCCircuitSvcIfIndex_Type()
)
mcmFrSVCCircuitSvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitSvcIfIndex.setStatus("mandatory")


class _McmFrSVCCircuitDiscardPriority_Type(Integer32):
    """Custom type mcmFrSVCCircuitDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_McmFrSVCCircuitDiscardPriority_Type.__name__ = "Integer32"
_McmFrSVCCircuitDiscardPriority_Object = MibTableColumn
mcmFrSVCCircuitDiscardPriority = _McmFrSVCCircuitDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 28),
    _McmFrSVCCircuitDiscardPriority_Type()
)
mcmFrSVCCircuitDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitDiscardPriority.setStatus("mandatory")


class _McmFrSVCCircuitSetupPriority_Type(Integer32):
    """Custom type mcmFrSVCCircuitSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrSVCCircuitSetupPriority_Type.__name__ = "Integer32"
_McmFrSVCCircuitSetupPriority_Object = MibTableColumn
mcmFrSVCCircuitSetupPriority = _McmFrSVCCircuitSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 29),
    _McmFrSVCCircuitSetupPriority_Type()
)
mcmFrSVCCircuitSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitSetupPriority.setStatus("mandatory")


class _McmFrSVCCircuitHoldingPriority_Type(Integer32):
    """Custom type mcmFrSVCCircuitHoldingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrSVCCircuitHoldingPriority_Type.__name__ = "Integer32"
_McmFrSVCCircuitHoldingPriority_Object = MibTableColumn
mcmFrSVCCircuitHoldingPriority = _McmFrSVCCircuitHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 8, 1, 30),
    _McmFrSVCCircuitHoldingPriority_Type()
)
mcmFrSVCCircuitHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrSVCCircuitHoldingPriority.setStatus("mandatory")
_NvmFrGlobalGroup_ObjectIdentity = ObjectIdentity
nvmFrGlobalGroup = _NvmFrGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9)
)


class _NvmFrMaxDLCI_Type(Integer32):
    """Custom type nvmFrMaxDLCI based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrMaxDLCI_Type.__name__ = "Integer32"
_NvmFrMaxDLCI_Object = MibScalar
nvmFrMaxDLCI = _NvmFrMaxDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 1),
    _NvmFrMaxDLCI_Type()
)
nvmFrMaxDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrMaxDLCI.setStatus("mandatory")


class _NvmFrMaxVirtualPorts_Type(Integer32):
    """Custom type nvmFrMaxVirtualPorts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmFrMaxVirtualPorts_Type.__name__ = "Integer32"
_NvmFrMaxVirtualPorts_Object = MibScalar
nvmFrMaxVirtualPorts = _NvmFrMaxVirtualPorts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 2),
    _NvmFrMaxVirtualPorts_Type()
)
nvmFrMaxVirtualPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrMaxVirtualPorts.setStatus("mandatory")


class _NvmFrMaxDlciPerLine_Type(Integer32):
    """Custom type nvmFrMaxDlciPerLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrMaxDlciPerLine_Type.__name__ = "Integer32"
_NvmFrMaxDlciPerLine_Object = MibScalar
nvmFrMaxDlciPerLine = _NvmFrMaxDlciPerLine_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 3),
    _NvmFrMaxDlciPerLine_Type()
)
nvmFrMaxDlciPerLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrMaxDlciPerLine.setStatus("mandatory")


class _NvmFrDNANumberingPlan_Type(Integer32):
    """Custom type nvmFrDNANumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 3))
    )


_NvmFrDNANumberingPlan_Type.__name__ = "Integer32"
_NvmFrDNANumberingPlan_Object = MibScalar
nvmFrDNANumberingPlan = _NvmFrDNANumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 4),
    _NvmFrDNANumberingPlan_Type()
)
nvmFrDNANumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDNANumberingPlan.setStatus("mandatory")


class _NvmFrPanlLmiTrapEnable_Type(Integer32):
    """Custom type nvmFrPanlLmiTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmFrPanlLmiTrapEnable_Type.__name__ = "Integer32"
_NvmFrPanlLmiTrapEnable_Object = MibScalar
nvmFrPanlLmiTrapEnable = _NvmFrPanlLmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 5),
    _NvmFrPanlLmiTrapEnable_Type()
)
nvmFrPanlLmiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPanlLmiTrapEnable.setStatus("mandatory")


class _NvmFrMsmTrapEnable_Type(Integer32):
    """Custom type nvmFrMsmTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmFrMsmTrapEnable_Type.__name__ = "Integer32"
_NvmFrMsmTrapEnable_Object = MibScalar
nvmFrMsmTrapEnable = _NvmFrMsmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 6),
    _NvmFrMsmTrapEnable_Type()
)
nvmFrMsmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrMsmTrapEnable.setStatus("mandatory")


class _NvmFrCoreTrapEnable_Type(Integer32):
    """Custom type nvmFrCoreTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmFrCoreTrapEnable_Type.__name__ = "Integer32"
_NvmFrCoreTrapEnable_Object = MibScalar
nvmFrCoreTrapEnable = _NvmFrCoreTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 7),
    _NvmFrCoreTrapEnable_Type()
)
nvmFrCoreTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrCoreTrapEnable.setStatus("mandatory")


class _NvmFrPlmTrapEnable_Type(Integer32):
    """Custom type nvmFrPlmTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmFrPlmTrapEnable_Type.__name__ = "Integer32"
_NvmFrPlmTrapEnable_Object = MibScalar
nvmFrPlmTrapEnable = _NvmFrPlmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 9, 8),
    _NvmFrPlmTrapEnable_Type()
)
nvmFrPlmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPlmTrapEnable.setStatus("mandatory")
_NvmFrPhyPortTable_Object = MibTable
nvmFrPhyPortTable = _NvmFrPhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10)
)
if mibBuilder.loadTexts:
    nvmFrPhyPortTable.setStatus("mandatory")
_NvmFrPhyPortEntry_Object = MibTableRow
nvmFrPhyPortEntry = _NvmFrPhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1)
)
nvmFrPhyPortEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrPhyPortExtIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrPhyPortEntry.setStatus("mandatory")
_NvmFrPhyPortExtIfIndex_Type = Integer32
_NvmFrPhyPortExtIfIndex_Object = MibTableColumn
nvmFrPhyPortExtIfIndex = _NvmFrPhyPortExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 1),
    _NvmFrPhyPortExtIfIndex_Type()
)
nvmFrPhyPortExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrPhyPortExtIfIndex.setStatus("mandatory")


class _NvmFrPhyPortFlowControl_Type(Integer32):
    """Custom type nvmFrPhyPortFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmFrPhyPortFlowControl_Type.__name__ = "Integer32"
_NvmFrPhyPortFlowControl_Object = MibTableColumn
nvmFrPhyPortFlowControl = _NvmFrPhyPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 2),
    _NvmFrPhyPortFlowControl_Type()
)
nvmFrPhyPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortFlowControl.setStatus("mandatory")


class _NvmFrPhyPortThroughput_Type(Integer32):
    """Custom type nvmFrPhyPortThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortThroughput_Type.__name__ = "Integer32"
_NvmFrPhyPortThroughput_Object = MibTableColumn
nvmFrPhyPortThroughput = _NvmFrPhyPortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 3),
    _NvmFrPhyPortThroughput_Type()
)
nvmFrPhyPortThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortThroughput.setStatus("deprecated")


class _NvmFrPhyPortDelta_Type(Integer32):
    """Custom type nvmFrPhyPortDelta based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NvmFrPhyPortDelta_Type.__name__ = "Integer32"
_NvmFrPhyPortDelta_Object = MibTableColumn
nvmFrPhyPortDelta = _NvmFrPhyPortDelta_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 4),
    _NvmFrPhyPortDelta_Type()
)
nvmFrPhyPortDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortDelta.setStatus("mandatory")


class _NvmFrPhyPortConsectiveFrames_Type(Integer32):
    """Custom type nvmFrPhyPortConsectiveFrames based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NvmFrPhyPortConsectiveFrames_Type.__name__ = "Integer32"
_NvmFrPhyPortConsectiveFrames_Object = MibTableColumn
nvmFrPhyPortConsectiveFrames = _NvmFrPhyPortConsectiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 5),
    _NvmFrPhyPortConsectiveFrames_Type()
)
nvmFrPhyPortConsectiveFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortConsectiveFrames.setStatus("mandatory")
_NvmFrPhyPortMtuSize_Type = Integer32
_NvmFrPhyPortMtuSize_Object = MibTableColumn
nvmFrPhyPortMtuSize = _NvmFrPhyPortMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 6),
    _NvmFrPhyPortMtuSize_Type()
)
nvmFrPhyPortMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortMtuSize.setStatus("deprecated")


class _NvmFrPhyPortTxThroughput_Type(Integer32):
    """Custom type nvmFrPhyPortTxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortTxThroughput_Type.__name__ = "Integer32"
_NvmFrPhyPortTxThroughput_Object = MibTableColumn
nvmFrPhyPortTxThroughput = _NvmFrPhyPortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 7),
    _NvmFrPhyPortTxThroughput_Type()
)
nvmFrPhyPortTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortTxThroughput.setStatus("mandatory")


class _NvmFrPhyPortRxThroughput_Type(Integer32):
    """Custom type nvmFrPhyPortRxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortRxThroughput_Type.__name__ = "Integer32"
_NvmFrPhyPortRxThroughput_Object = MibTableColumn
nvmFrPhyPortRxThroughput = _NvmFrPhyPortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 8),
    _NvmFrPhyPortRxThroughput_Type()
)
nvmFrPhyPortRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortRxThroughput.setStatus("mandatory")


class _NvmFrPhyPortTxMaxFrameSize_Type(Integer32):
    """Custom type nvmFrPhyPortTxMaxFrameSize based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NvmFrPhyPortTxMaxFrameSize_Type.__name__ = "Integer32"
_NvmFrPhyPortTxMaxFrameSize_Object = MibTableColumn
nvmFrPhyPortTxMaxFrameSize = _NvmFrPhyPortTxMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 9),
    _NvmFrPhyPortTxMaxFrameSize_Type()
)
nvmFrPhyPortTxMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortTxMaxFrameSize.setStatus("mandatory")


class _NvmFrPhyPortRxMaxFrameSize_Type(Integer32):
    """Custom type nvmFrPhyPortRxMaxFrameSize based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NvmFrPhyPortRxMaxFrameSize_Type.__name__ = "Integer32"
_NvmFrPhyPortRxMaxFrameSize_Object = MibTableColumn
nvmFrPhyPortRxMaxFrameSize = _NvmFrPhyPortRxMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 10),
    _NvmFrPhyPortRxMaxFrameSize_Type()
)
nvmFrPhyPortRxMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortRxMaxFrameSize.setStatus("mandatory")


class _NvmFrPhyPortRateEnf_Type(Integer32):
    """Custom type nvmFrPhyPortRateEnf based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmFrPhyPortRateEnf_Type.__name__ = "Integer32"
_NvmFrPhyPortRateEnf_Object = MibTableColumn
nvmFrPhyPortRateEnf = _NvmFrPhyPortRateEnf_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 11),
    _NvmFrPhyPortRateEnf_Type()
)
nvmFrPhyPortRateEnf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortRateEnf.setStatus("mandatory")


class _NvmFrPhyPortTxBc_Type(Integer32):
    """Custom type nvmFrPhyPortTxBc based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortTxBc_Type.__name__ = "Integer32"
_NvmFrPhyPortTxBc_Object = MibTableColumn
nvmFrPhyPortTxBc = _NvmFrPhyPortTxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 12),
    _NvmFrPhyPortTxBc_Type()
)
nvmFrPhyPortTxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortTxBc.setStatus("mandatory")


class _NvmFrPhyPortRxBc_Type(Integer32):
    """Custom type nvmFrPhyPortRxBc based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortRxBc_Type.__name__ = "Integer32"
_NvmFrPhyPortRxBc_Object = MibTableColumn
nvmFrPhyPortRxBc = _NvmFrPhyPortRxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 13),
    _NvmFrPhyPortRxBc_Type()
)
nvmFrPhyPortRxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortRxBc.setStatus("mandatory")


class _NvmFrPhyPortTxBe_Type(Integer32):
    """Custom type nvmFrPhyPortTxBe based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortTxBe_Type.__name__ = "Integer32"
_NvmFrPhyPortTxBe_Object = MibTableColumn
nvmFrPhyPortTxBe = _NvmFrPhyPortTxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 14),
    _NvmFrPhyPortTxBe_Type()
)
nvmFrPhyPortTxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortTxBe.setStatus("mandatory")


class _NvmFrPhyPortRxBe_Type(Integer32):
    """Custom type nvmFrPhyPortRxBe based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPhyPortRxBe_Type.__name__ = "Integer32"
_NvmFrPhyPortRxBe_Object = MibTableColumn
nvmFrPhyPortRxBe = _NvmFrPhyPortRxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 10, 1, 15),
    _NvmFrPhyPortRxBe_Type()
)
nvmFrPhyPortRxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPhyPortRxBe.setStatus("mandatory")
_NvmFrPVCPhyTable_Object = MibTable
nvmFrPVCPhyTable = _NvmFrPVCPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 11)
)
if mibBuilder.loadTexts:
    nvmFrPVCPhyTable.setStatus("mandatory")
_NvmFrPVCPhyEntry_Object = MibTableRow
nvmFrPVCPhyEntry = _NvmFrPVCPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 11, 1)
)
nvmFrPVCPhyEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrPVCPhyIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrPVCPhyEntry.setStatus("mandatory")
_NvmFrPVCPhyIfIndex_Type = Integer32
_NvmFrPVCPhyIfIndex_Object = MibTableColumn
nvmFrPVCPhyIfIndex = _NvmFrPVCPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 11, 1, 1),
    _NvmFrPVCPhyIfIndex_Type()
)
nvmFrPVCPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrPVCPhyIfIndex.setStatus("mandatory")


class _NvmFrPVCLMIMode_Type(Integer32):
    """Custom type nvmFrPVCLMIMode based on Integer32"""
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


_NvmFrPVCLMIMode_Type.__name__ = "Integer32"
_NvmFrPVCLMIMode_Object = MibTableColumn
nvmFrPVCLMIMode = _NvmFrPVCLMIMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 11, 1, 2),
    _NvmFrPVCLMIMode_Type()
)
nvmFrPVCLMIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCLMIMode.setStatus("mandatory")


class _NvmFrPVCBiDir_Type(Integer32):
    """Custom type nvmFrPVCBiDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_NvmFrPVCBiDir_Type.__name__ = "Integer32"
_NvmFrPVCBiDir_Object = MibTableColumn
nvmFrPVCBiDir = _NvmFrPVCBiDir_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 11, 1, 3),
    _NvmFrPVCBiDir_Type()
)
nvmFrPVCBiDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCBiDir.setStatus("mandatory")
_NvmFrSVCPhyTable_Object = MibTable
nvmFrSVCPhyTable = _NvmFrSVCPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12)
)
if mibBuilder.loadTexts:
    nvmFrSVCPhyTable.setStatus("mandatory")
_NvmFrSVCPhyEntry_Object = MibTableRow
nvmFrSVCPhyEntry = _NvmFrSVCPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1)
)
nvmFrSVCPhyEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrSVCPhyIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrSVCPhyEntry.setStatus("mandatory")
_NvmFrSVCPhyIfIndex_Type = Integer32
_NvmFrSVCPhyIfIndex_Object = MibTableColumn
nvmFrSVCPhyIfIndex = _NvmFrSVCPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 1),
    _NvmFrSVCPhyIfIndex_Type()
)
nvmFrSVCPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrSVCPhyIfIndex.setStatus("mandatory")


class _NvmFrSVCState_Type(Integer32):
    """Custom type nvmFrSVCState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("q933svc", 1)
    )


_NvmFrSVCState_Type.__name__ = "Integer32"
_NvmFrSVCState_Object = MibTableColumn
nvmFrSVCState = _NvmFrSVCState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 2),
    _NvmFrSVCState_Type()
)
nvmFrSVCState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCState.setStatus("mandatory")


class _NvmFrSVCT303_Type(Integer32):
    """Custom type nvmFrSVCT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrSVCT303_Type.__name__ = "Integer32"
_NvmFrSVCT303_Object = MibTableColumn
nvmFrSVCT303 = _NvmFrSVCT303_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 3),
    _NvmFrSVCT303_Type()
)
nvmFrSVCT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCT303.setStatus("mandatory")


class _NvmFrSVCT305_Type(Integer32):
    """Custom type nvmFrSVCT305 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrSVCT305_Type.__name__ = "Integer32"
_NvmFrSVCT305_Object = MibTableColumn
nvmFrSVCT305 = _NvmFrSVCT305_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 4),
    _NvmFrSVCT305_Type()
)
nvmFrSVCT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCT305.setStatus("mandatory")


class _NvmFrSVCT308_Type(Integer32):
    """Custom type nvmFrSVCT308 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrSVCT308_Type.__name__ = "Integer32"
_NvmFrSVCT308_Object = MibTableColumn
nvmFrSVCT308 = _NvmFrSVCT308_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 5),
    _NvmFrSVCT308_Type()
)
nvmFrSVCT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCT308.setStatus("mandatory")


class _NvmFrSVCT310_Type(Integer32):
    """Custom type nvmFrSVCT310 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrSVCT310_Type.__name__ = "Integer32"
_NvmFrSVCT310_Object = MibTableColumn
nvmFrSVCT310 = _NvmFrSVCT310_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 6),
    _NvmFrSVCT310_Type()
)
nvmFrSVCT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCT310.setStatus("mandatory")


class _NvmFrSVCMaxCalls_Type(Integer32):
    """Custom type nvmFrSVCMaxCalls based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrSVCMaxCalls_Type.__name__ = "Integer32"
_NvmFrSVCMaxCalls_Object = MibTableColumn
nvmFrSVCMaxCalls = _NvmFrSVCMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 7),
    _NvmFrSVCMaxCalls_Type()
)
nvmFrSVCMaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMaxCalls.setStatus("mandatory")


class _NvmFrSVCMaxTxSize_Type(Integer32):
    """Custom type nvmFrSVCMaxTxSize based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrSVCMaxTxSize_Type.__name__ = "Integer32"
_NvmFrSVCMaxTxSize_Object = MibTableColumn
nvmFrSVCMaxTxSize = _NvmFrSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 8),
    _NvmFrSVCMaxTxSize_Type()
)
nvmFrSVCMaxTxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMaxTxSize.setStatus("mandatory")


class _NvmFrSVCMaxRxSize_Type(Integer32):
    """Custom type nvmFrSVCMaxRxSize based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrSVCMaxRxSize_Type.__name__ = "Integer32"
_NvmFrSVCMaxRxSize_Object = MibTableColumn
nvmFrSVCMaxRxSize = _NvmFrSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 9),
    _NvmFrSVCMaxRxSize_Type()
)
nvmFrSVCMaxRxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMaxRxSize.setStatus("mandatory")


class _NvmFrSVCMinDLCI_Type(Integer32):
    """Custom type nvmFrSVCMinDLCI based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 991),
    )


_NvmFrSVCMinDLCI_Type.__name__ = "Integer32"
_NvmFrSVCMinDLCI_Object = MibTableColumn
nvmFrSVCMinDLCI = _NvmFrSVCMinDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 10),
    _NvmFrSVCMinDLCI_Type()
)
nvmFrSVCMinDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMinDLCI.setStatus("mandatory")


class _NvmFrSVCMaxDLCI_Type(Integer32):
    """Custom type nvmFrSVCMaxDLCI based on Integer32"""
    defaultValue = 991

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 991),
    )


_NvmFrSVCMaxDLCI_Type.__name__ = "Integer32"
_NvmFrSVCMaxDLCI_Object = MibTableColumn
nvmFrSVCMaxDLCI = _NvmFrSVCMaxDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 11),
    _NvmFrSVCMaxDLCI_Type()
)
nvmFrSVCMaxDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMaxDLCI.setStatus("mandatory")


class _NvmFrSVCMinTxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMinTxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMinTxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMinTxThroughput_Object = MibTableColumn
nvmFrSVCMinTxThroughput = _NvmFrSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 12),
    _NvmFrSVCMinTxThroughput_Type()
)
nvmFrSVCMinTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMinTxThroughput.setStatus("mandatory")


class _NvmFrSVCMinRxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMinRxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMinRxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMinRxThroughput_Object = MibTableColumn
nvmFrSVCMinRxThroughput = _NvmFrSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 13),
    _NvmFrSVCMinRxThroughput_Type()
)
nvmFrSVCMinRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMinRxThroughput.setStatus("mandatory")


class _NvmFrSVCMaxTxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMaxTxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMaxTxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMaxTxThroughput_Object = MibTableColumn
nvmFrSVCMaxTxThroughput = _NvmFrSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 14),
    _NvmFrSVCMaxTxThroughput_Type()
)
nvmFrSVCMaxTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMaxTxThroughput.setStatus("mandatory")


class _NvmFrSVCMaxRxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMaxRxThroughput based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMaxRxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMaxRxThroughput_Object = MibTableColumn
nvmFrSVCMaxRxThroughput = _NvmFrSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 15),
    _NvmFrSVCMaxRxThroughput_Type()
)
nvmFrSVCMaxRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMaxRxThroughput.setStatus("mandatory")


class _NvmFrSVCTxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCTxBurstSize based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCTxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCTxBurstSize_Object = MibTableColumn
nvmFrSVCTxBurstSize = _NvmFrSVCTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 16),
    _NvmFrSVCTxBurstSize_Type()
)
nvmFrSVCTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCTxBurstSize.setStatus("mandatory")


class _NvmFrSVCRxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCRxBurstSize based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCRxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCRxBurstSize_Object = MibTableColumn
nvmFrSVCRxBurstSize = _NvmFrSVCRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 17),
    _NvmFrSVCRxBurstSize_Type()
)
nvmFrSVCRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCRxBurstSize.setStatus("mandatory")


class _NvmFrSVCExcessTxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCExcessTxBurstSize based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCExcessTxBurstSize_Object = MibTableColumn
nvmFrSVCExcessTxBurstSize = _NvmFrSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 18),
    _NvmFrSVCExcessTxBurstSize_Type()
)
nvmFrSVCExcessTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCExcessTxBurstSize.setStatus("mandatory")


class _NvmFrSVCExcessRxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCExcessRxBurstSize based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCExcessRxBurstSize_Object = MibTableColumn
nvmFrSVCExcessRxBurstSize = _NvmFrSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 12, 1, 19),
    _NvmFrSVCExcessRxBurstSize_Type()
)
nvmFrSVCExcessRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCExcessRxBurstSize.setStatus("mandatory")
_NvmFrVirtualPortTable_Object = MibTable
nvmFrVirtualPortTable = _NvmFrVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13)
)
if mibBuilder.loadTexts:
    nvmFrVirtualPortTable.setStatus("mandatory")
_NvmFrVirtualPortEntry_Object = MibTableRow
nvmFrVirtualPortEntry = _NvmFrVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1)
)
nvmFrVirtualPortEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrVirtualPortIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrVirtualPortEntry.setStatus("mandatory")


class _NvmFrVirtualPortIfIndex_Type(Integer32):
    """Custom type nvmFrVirtualPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrVirtualPortIfIndex_Type.__name__ = "Integer32"
_NvmFrVirtualPortIfIndex_Object = MibTableColumn
nvmFrVirtualPortIfIndex = _NvmFrVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 1),
    _NvmFrVirtualPortIfIndex_Type()
)
nvmFrVirtualPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrVirtualPortIfIndex.setStatus("mandatory")


class _NvmFrVirtualPortPhyPortIfIndex_Type(Integer32):
    """Custom type nvmFrVirtualPortPhyPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrVirtualPortPhyPortIfIndex_Type.__name__ = "Integer32"
_NvmFrVirtualPortPhyPortIfIndex_Object = MibTableColumn
nvmFrVirtualPortPhyPortIfIndex = _NvmFrVirtualPortPhyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 2),
    _NvmFrVirtualPortPhyPortIfIndex_Type()
)
nvmFrVirtualPortPhyPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrVirtualPortPhyPortIfIndex.setStatus("obsolete")


class _NvmFrVirtualPortPPA_Type(Integer32):
    """Custom type nvmFrVirtualPortPPA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_NvmFrVirtualPortPPA_Type.__name__ = "Integer32"
_NvmFrVirtualPortPPA_Object = MibTableColumn
nvmFrVirtualPortPPA = _NvmFrVirtualPortPPA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 3),
    _NvmFrVirtualPortPPA_Type()
)
nvmFrVirtualPortPPA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrVirtualPortPPA.setStatus("obsolete")


class _NvmFrVirtualPortMode_Type(Integer32):
    """Custom type nvmFrVirtualPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("easyRouting", 2))
    )


_NvmFrVirtualPortMode_Type.__name__ = "Integer32"
_NvmFrVirtualPortMode_Object = MibTableColumn
nvmFrVirtualPortMode = _NvmFrVirtualPortMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 4),
    _NvmFrVirtualPortMode_Type()
)
nvmFrVirtualPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrVirtualPortMode.setStatus("mandatory")


class _NvmFrVirtualPortEntryStatus_Type(Integer32):
    """Custom type nvmFrVirtualPortEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_NvmFrVirtualPortEntryStatus_Type.__name__ = "Integer32"
_NvmFrVirtualPortEntryStatus_Object = MibTableColumn
nvmFrVirtualPortEntryStatus = _NvmFrVirtualPortEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 5),
    _NvmFrVirtualPortEntryStatus_Type()
)
nvmFrVirtualPortEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrVirtualPortEntryStatus.setStatus("mandatory")


class _NvmFrVirtualPortProtocolBinding_Type(Integer32):
    """Custom type nvmFrVirtualPortProtocolBinding based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bridge-configured", 4),
          ("ip-and-bridge-configured", 5),
          ("ip-and-ipx-and-bridge-configured", 7),
          ("ip-and-ipx-configured", 3),
          ("ip-configured", 1),
          ("ipx-and-bridge-configured", 6),
          ("ipx-configured", 2),
          ("sNA-configured", 8),
          ("x25-configured", 9))
    )


_NvmFrVirtualPortProtocolBinding_Type.__name__ = "Integer32"
_NvmFrVirtualPortProtocolBinding_Object = MibTableColumn
nvmFrVirtualPortProtocolBinding = _NvmFrVirtualPortProtocolBinding_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 6),
    _NvmFrVirtualPortProtocolBinding_Type()
)
nvmFrVirtualPortProtocolBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrVirtualPortProtocolBinding.setStatus("mandatory")


class _NvmFrVirtualPortNumber_Type(Integer32):
    """Custom type nvmFrVirtualPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_NvmFrVirtualPortNumber_Type.__name__ = "Integer32"
_NvmFrVirtualPortNumber_Object = MibTableColumn
nvmFrVirtualPortNumber = _NvmFrVirtualPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 13, 1, 7),
    _NvmFrVirtualPortNumber_Type()
)
nvmFrVirtualPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrVirtualPortNumber.setStatus("mandatory")
_NvmFrSVCMapTable_Object = MibTable
nvmFrSVCMapTable = _NvmFrSVCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14)
)
if mibBuilder.loadTexts:
    nvmFrSVCMapTable.setStatus("mandatory")
_NvmFrSVCMapEntry_Object = MibTableRow
nvmFrSVCMapEntry = _NvmFrSVCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1)
)
nvmFrSVCMapEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrSVCMapVirtualPortIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrSVCMapDNA"),
)
if mibBuilder.loadTexts:
    nvmFrSVCMapEntry.setStatus("mandatory")
_NvmFrSVCMapVirtualPortIfIndex_Type = Integer32
_NvmFrSVCMapVirtualPortIfIndex_Object = MibTableColumn
nvmFrSVCMapVirtualPortIfIndex = _NvmFrSVCMapVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 1),
    _NvmFrSVCMapVirtualPortIfIndex_Type()
)
nvmFrSVCMapVirtualPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapVirtualPortIfIndex.setStatus("mandatory")


class _NvmFrSVCMapDNA_Type(OctetString):
    """Custom type nvmFrSVCMapDNA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmFrSVCMapDNA_Type.__name__ = "OctetString"
_NvmFrSVCMapDNA_Object = MibTableColumn
nvmFrSVCMapDNA = _NvmFrSVCMapDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 2),
    _NvmFrSVCMapDNA_Type()
)
nvmFrSVCMapDNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapDNA.setStatus("mandatory")


class _NvmFrSVCMapMaxTxSize_Type(Integer32):
    """Custom type nvmFrSVCMapMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrSVCMapMaxTxSize_Type.__name__ = "Integer32"
_NvmFrSVCMapMaxTxSize_Object = MibTableColumn
nvmFrSVCMapMaxTxSize = _NvmFrSVCMapMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 3),
    _NvmFrSVCMapMaxTxSize_Type()
)
nvmFrSVCMapMaxTxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapMaxTxSize.setStatus("mandatory")


class _NvmFrSVCMapMaxRxSize_Type(Integer32):
    """Custom type nvmFrSVCMapMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrSVCMapMaxRxSize_Type.__name__ = "Integer32"
_NvmFrSVCMapMaxRxSize_Object = MibTableColumn
nvmFrSVCMapMaxRxSize = _NvmFrSVCMapMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 4),
    _NvmFrSVCMapMaxRxSize_Type()
)
nvmFrSVCMapMaxRxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapMaxRxSize.setStatus("mandatory")


class _NvmFrSVCMapMinTxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMapMinTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapMinTxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMapMinTxThroughput_Object = MibTableColumn
nvmFrSVCMapMinTxThroughput = _NvmFrSVCMapMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 5),
    _NvmFrSVCMapMinTxThroughput_Type()
)
nvmFrSVCMapMinTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapMinTxThroughput.setStatus("mandatory")


class _NvmFrSVCMapMinRxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMapMinRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapMinRxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMapMinRxThroughput_Object = MibTableColumn
nvmFrSVCMapMinRxThroughput = _NvmFrSVCMapMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 6),
    _NvmFrSVCMapMinRxThroughput_Type()
)
nvmFrSVCMapMinRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapMinRxThroughput.setStatus("mandatory")


class _NvmFrSVCMapMaxTxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMapMaxTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapMaxTxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMapMaxTxThroughput_Object = MibTableColumn
nvmFrSVCMapMaxTxThroughput = _NvmFrSVCMapMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 7),
    _NvmFrSVCMapMaxTxThroughput_Type()
)
nvmFrSVCMapMaxTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapMaxTxThroughput.setStatus("mandatory")


class _NvmFrSVCMapMaxRxThroughput_Type(Integer32):
    """Custom type nvmFrSVCMapMaxRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapMaxRxThroughput_Type.__name__ = "Integer32"
_NvmFrSVCMapMaxRxThroughput_Object = MibTableColumn
nvmFrSVCMapMaxRxThroughput = _NvmFrSVCMapMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 8),
    _NvmFrSVCMapMaxRxThroughput_Type()
)
nvmFrSVCMapMaxRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapMaxRxThroughput.setStatus("mandatory")


class _NvmFrSVCMapTxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCMapTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapTxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCMapTxBurstSize_Object = MibTableColumn
nvmFrSVCMapTxBurstSize = _NvmFrSVCMapTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 9),
    _NvmFrSVCMapTxBurstSize_Type()
)
nvmFrSVCMapTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapTxBurstSize.setStatus("mandatory")


class _NvmFrSVCMapRxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCMapRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapRxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCMapRxBurstSize_Object = MibTableColumn
nvmFrSVCMapRxBurstSize = _NvmFrSVCMapRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 10),
    _NvmFrSVCMapRxBurstSize_Type()
)
nvmFrSVCMapRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapRxBurstSize.setStatus("mandatory")


class _NvmFrSVCMapExcessTxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCMapExcessTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapExcessTxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCMapExcessTxBurstSize_Object = MibTableColumn
nvmFrSVCMapExcessTxBurstSize = _NvmFrSVCMapExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 11),
    _NvmFrSVCMapExcessTxBurstSize_Type()
)
nvmFrSVCMapExcessTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapExcessTxBurstSize.setStatus("mandatory")


class _NvmFrSVCMapExcessRxBurstSize_Type(Integer32):
    """Custom type nvmFrSVCMapExcessRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrSVCMapExcessRxBurstSize_Type.__name__ = "Integer32"
_NvmFrSVCMapExcessRxBurstSize_Object = MibTableColumn
nvmFrSVCMapExcessRxBurstSize = _NvmFrSVCMapExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 12),
    _NvmFrSVCMapExcessRxBurstSize_Type()
)
nvmFrSVCMapExcessRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapExcessRxBurstSize.setStatus("mandatory")


class _NvmFrSVCMapPriority_Type(Integer32):
    """Custom type nvmFrSVCMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NvmFrSVCMapPriority_Type.__name__ = "Integer32"
_NvmFrSVCMapPriority_Object = MibTableColumn
nvmFrSVCMapPriority = _NvmFrSVCMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 13),
    _NvmFrSVCMapPriority_Type()
)
nvmFrSVCMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapPriority.setStatus("mandatory")


class _NvmFrSVCMapEntryStatus_Type(Integer32):
    """Custom type nvmFrSVCMapEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_NvmFrSVCMapEntryStatus_Type.__name__ = "Integer32"
_NvmFrSVCMapEntryStatus_Object = MibTableColumn
nvmFrSVCMapEntryStatus = _NvmFrSVCMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 14),
    _NvmFrSVCMapEntryStatus_Type()
)
nvmFrSVCMapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapEntryStatus.setStatus("mandatory")


class _NvmFrSVCMapTransferPriority_Type(Integer32):
    """Custom type nvmFrSVCMapTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NvmFrSVCMapTransferPriority_Type.__name__ = "Integer32"
_NvmFrSVCMapTransferPriority_Object = MibTableColumn
nvmFrSVCMapTransferPriority = _NvmFrSVCMapTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 15),
    _NvmFrSVCMapTransferPriority_Type()
)
nvmFrSVCMapTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapTransferPriority.setStatus("mandatory")


class _NvmFrSVCMapRowStatus_Type(Integer32):
    """Custom type nvmFrSVCMapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_NvmFrSVCMapRowStatus_Type.__name__ = "Integer32"
_NvmFrSVCMapRowStatus_Object = MibTableColumn
nvmFrSVCMapRowStatus = _NvmFrSVCMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 16),
    _NvmFrSVCMapRowStatus_Type()
)
nvmFrSVCMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapRowStatus.setStatus("mandatory")


class _NvmFrSVCMapDiscardPriority_Type(Integer32):
    """Custom type nvmFrSVCMapDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_NvmFrSVCMapDiscardPriority_Type.__name__ = "Integer32"
_NvmFrSVCMapDiscardPriority_Object = MibTableColumn
nvmFrSVCMapDiscardPriority = _NvmFrSVCMapDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 17),
    _NvmFrSVCMapDiscardPriority_Type()
)
nvmFrSVCMapDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapDiscardPriority.setStatus("mandatory")


class _NvmFrSVCMapSetupPriority_Type(Integer32):
    """Custom type nvmFrSVCMapSetupPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmFrSVCMapSetupPriority_Type.__name__ = "Integer32"
_NvmFrSVCMapSetupPriority_Object = MibTableColumn
nvmFrSVCMapSetupPriority = _NvmFrSVCMapSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 18),
    _NvmFrSVCMapSetupPriority_Type()
)
nvmFrSVCMapSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapSetupPriority.setStatus("mandatory")


class _NvmFrSVCMapHoldingPriority_Type(Integer32):
    """Custom type nvmFrSVCMapHoldingPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmFrSVCMapHoldingPriority_Type.__name__ = "Integer32"
_NvmFrSVCMapHoldingPriority_Object = MibTableColumn
nvmFrSVCMapHoldingPriority = _NvmFrSVCMapHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 14, 1, 19),
    _NvmFrSVCMapHoldingPriority_Type()
)
nvmFrSVCMapHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrSVCMapHoldingPriority.setStatus("mandatory")
_NvmFrPVCMapTable_Object = MibTable
nvmFrPVCMapTable = _NvmFrPVCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 15)
)
if mibBuilder.loadTexts:
    nvmFrPVCMapTable.setStatus("obsolete")
_NvmFrPVCMapEntry_Object = MibTableRow
nvmFrPVCMapEntry = _NvmFrPVCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 15, 1)
)
nvmFrPVCMapEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrPVCMapVirtualPortIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrPVCMapDLCI"),
)
if mibBuilder.loadTexts:
    nvmFrPVCMapEntry.setStatus("obsolete")
_NvmFrPVCMapVirtualPortIfIndex_Type = Integer32
_NvmFrPVCMapVirtualPortIfIndex_Object = MibTableColumn
nvmFrPVCMapVirtualPortIfIndex = _NvmFrPVCMapVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 15, 1, 1),
    _NvmFrPVCMapVirtualPortIfIndex_Type()
)
nvmFrPVCMapVirtualPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCMapVirtualPortIfIndex.setStatus("obsolete")


class _NvmFrPVCMapDLCI_Type(Integer32):
    """Custom type nvmFrPVCMapDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 126975),
    )


_NvmFrPVCMapDLCI_Type.__name__ = "Integer32"
_NvmFrPVCMapDLCI_Object = MibTableColumn
nvmFrPVCMapDLCI = _NvmFrPVCMapDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 15, 1, 2),
    _NvmFrPVCMapDLCI_Type()
)
nvmFrPVCMapDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCMapDLCI.setStatus("obsolete")


class _NvmFrPVCMapEntryStatus_Type(Integer32):
    """Custom type nvmFrPVCMapEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_NvmFrPVCMapEntryStatus_Type.__name__ = "Integer32"
_NvmFrPVCMapEntryStatus_Object = MibTableColumn
nvmFrPVCMapEntryStatus = _NvmFrPVCMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 15, 1, 3),
    _NvmFrPVCMapEntryStatus_Type()
)
nvmFrPVCMapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCMapEntryStatus.setStatus("obsolete")
_NvmFrPVCMapPhysIfIndex_Type = Integer32
_NvmFrPVCMapPhysIfIndex_Object = MibTableColumn
nvmFrPVCMapPhysIfIndex = _NvmFrPVCMapPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 15, 1, 4),
    _NvmFrPVCMapPhysIfIndex_Type()
)
nvmFrPVCMapPhysIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCMapPhysIfIndex.setStatus("obsolete")
_NvmFrDlcmiTable_Object = MibTable
nvmFrDlcmiTable = _NvmFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16)
)
if mibBuilder.loadTexts:
    nvmFrDlcmiTable.setStatus("mandatory")
_NvmFrDlcmiEntry_Object = MibTableRow
nvmFrDlcmiEntry = _NvmFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1)
)
nvmFrDlcmiEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrDlcmiEntry.setStatus("mandatory")


class _NvmFrDlcmiIfIndex_Type(Integer32):
    """Custom type nvmFrDlcmiIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrDlcmiIfIndex_Type.__name__ = "Integer32"
_NvmFrDlcmiIfIndex_Object = MibTableColumn
nvmFrDlcmiIfIndex = _NvmFrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 1),
    _NvmFrDlcmiIfIndex_Type()
)
nvmFrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrDlcmiIfIndex.setStatus("mandatory")


class _NvmFrDlcmiState_Type(Integer32):
    """Custom type nvmFrDlcmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1617D1994", 6),
          ("itut933A", 5),
          ("lmi", 2),
          ("noLmiConfigured", 1))
    )


_NvmFrDlcmiState_Type.__name__ = "Integer32"
_NvmFrDlcmiState_Object = MibTableColumn
nvmFrDlcmiState = _NvmFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 2),
    _NvmFrDlcmiState_Type()
)
nvmFrDlcmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiState.setStatus("mandatory")


class _NvmFrDlcmiAddress_Type(Integer32):
    """Custom type nvmFrDlcmiAddress based on Integer32"""
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
        *(("q921", 1),
          ("q922", 4),
          ("q922March90", 2),
          ("q922November90", 3))
    )


_NvmFrDlcmiAddress_Type.__name__ = "Integer32"
_NvmFrDlcmiAddress_Object = MibTableColumn
nvmFrDlcmiAddress = _NvmFrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 3),
    _NvmFrDlcmiAddress_Type()
)
nvmFrDlcmiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiAddress.setStatus("mandatory")


class _NvmFrDlcmiAddressLen_Type(Integer32):
    """Custom type nvmFrDlcmiAddressLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("four-octets", 4),
          ("three-octets", 3),
          ("two-octets", 2))
    )


_NvmFrDlcmiAddressLen_Type.__name__ = "Integer32"
_NvmFrDlcmiAddressLen_Object = MibTableColumn
nvmFrDlcmiAddressLen = _NvmFrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 4),
    _NvmFrDlcmiAddressLen_Type()
)
nvmFrDlcmiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiAddressLen.setStatus("mandatory")


class _NvmFrDlcmiPollingInterval_Type(Integer32):
    """Custom type nvmFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_NvmFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_NvmFrDlcmiPollingInterval_Object = MibTableColumn
nvmFrDlcmiPollingInterval = _NvmFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 5),
    _NvmFrDlcmiPollingInterval_Type()
)
nvmFrDlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiPollingInterval.setStatus("mandatory")


class _NvmFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type nvmFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_NvmFrDlcmiFullEnquiryInterval_Object = MibTableColumn
nvmFrDlcmiFullEnquiryInterval = _NvmFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 6),
    _NvmFrDlcmiFullEnquiryInterval_Type()
)
nvmFrDlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiFullEnquiryInterval.setStatus("mandatory")


class _NvmFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type nvmFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NvmFrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_NvmFrDlcmiErrorThreshold_Object = MibTableColumn
nvmFrDlcmiErrorThreshold = _NvmFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 7),
    _NvmFrDlcmiErrorThreshold_Type()
)
nvmFrDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiErrorThreshold.setStatus("mandatory")


class _NvmFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type nvmFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NvmFrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_NvmFrDlcmiMonitoredEvents_Object = MibTableColumn
nvmFrDlcmiMonitoredEvents = _NvmFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 8),
    _NvmFrDlcmiMonitoredEvents_Type()
)
nvmFrDlcmiMonitoredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrDlcmiMonitoredEvents.setStatus("mandatory")
_NvmFrDlcmiMaxSupportedVCs_Type = Integer32
_NvmFrDlcmiMaxSupportedVCs_Object = MibTableColumn
nvmFrDlcmiMaxSupportedVCs = _NvmFrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 9),
    _NvmFrDlcmiMaxSupportedVCs_Type()
)
nvmFrDlcmiMaxSupportedVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiMaxSupportedVCs.setStatus("mandatory")


class _NvmFrDlcmiMulticast_Type(Integer32):
    """Custom type nvmFrDlcmiMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 1))
    )


_NvmFrDlcmiMulticast_Type.__name__ = "Integer32"
_NvmFrDlcmiMulticast_Object = MibTableColumn
nvmFrDlcmiMulticast = _NvmFrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 16, 1, 10),
    _NvmFrDlcmiMulticast_Type()
)
nvmFrDlcmiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrDlcmiMulticast.setStatus("mandatory")
_McmFrAllSVCCircuitTable_Object = MibTable
mcmFrAllSVCCircuitTable = _McmFrAllSVCCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17)
)
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitTable.setStatus("mandatory")
_McmFrAllSVCCircuitEntry_Object = MibTableRow
mcmFrAllSVCCircuitEntry = _McmFrAllSVCCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1)
)
mcmFrAllSVCCircuitEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrAllSVCCircuitIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrAllSVCCircuitDlci"),
)
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitEntry.setStatus("mandatory")


class _McmFrAllSVCCircuitIfIndex_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrAllSVCCircuitIfIndex_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitIfIndex_Object = MibTableColumn
mcmFrAllSVCCircuitIfIndex = _McmFrAllSVCCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 1),
    _McmFrAllSVCCircuitIfIndex_Type()
)
mcmFrAllSVCCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitIfIndex.setStatus("mandatory")


class _McmFrAllSVCCircuitDlci_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrAllSVCCircuitDlci_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitDlci_Object = MibTableColumn
mcmFrAllSVCCircuitDlci = _McmFrAllSVCCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 2),
    _McmFrAllSVCCircuitDlci_Type()
)
mcmFrAllSVCCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitDlci.setStatus("mandatory")


class _McmFrAllSVCCircuitType_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitType based on Integer32"""
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
        *(("rfc1490", 1),
          ("rfc1490switched", 4),
          ("switched", 3),
          ("voice", 2))
    )


_McmFrAllSVCCircuitType_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitType_Object = MibTableColumn
mcmFrAllSVCCircuitType = _McmFrAllSVCCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 3),
    _McmFrAllSVCCircuitType_Type()
)
mcmFrAllSVCCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitType.setStatus("mandatory")


class _McmFrAllSVCCircuitDNA_Type(OctetString):
    """Custom type mcmFrAllSVCCircuitDNA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrAllSVCCircuitDNA_Type.__name__ = "OctetString"
_McmFrAllSVCCircuitDNA_Object = MibTableColumn
mcmFrAllSVCCircuitDNA = _McmFrAllSVCCircuitDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 4),
    _McmFrAllSVCCircuitDNA_Type()
)
mcmFrAllSVCCircuitDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitDNA.setStatus("mandatory")


class _McmFrAllSVCCircuitState_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_McmFrAllSVCCircuitState_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitState_Object = MibTableColumn
mcmFrAllSVCCircuitState = _McmFrAllSVCCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 5),
    _McmFrAllSVCCircuitState_Type()
)
mcmFrAllSVCCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitState.setStatus("mandatory")
_McmFrAllSVCCircuitReceivedFECNs_Type = Counter32
_McmFrAllSVCCircuitReceivedFECNs_Object = MibTableColumn
mcmFrAllSVCCircuitReceivedFECNs = _McmFrAllSVCCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 6),
    _McmFrAllSVCCircuitReceivedFECNs_Type()
)
mcmFrAllSVCCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitReceivedFECNs.setStatus("mandatory")
_McmFrAllSVCCircuitReceivedBECNs_Type = Counter32
_McmFrAllSVCCircuitReceivedBECNs_Object = MibTableColumn
mcmFrAllSVCCircuitReceivedBECNs = _McmFrAllSVCCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 7),
    _McmFrAllSVCCircuitReceivedBECNs_Type()
)
mcmFrAllSVCCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitReceivedBECNs.setStatus("mandatory")
_McmFrAllSVCCircuitSentFrames_Type = Counter32
_McmFrAllSVCCircuitSentFrames_Object = MibTableColumn
mcmFrAllSVCCircuitSentFrames = _McmFrAllSVCCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 8),
    _McmFrAllSVCCircuitSentFrames_Type()
)
mcmFrAllSVCCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitSentFrames.setStatus("mandatory")
_McmFrAllSVCCircuitSentOctets_Type = Counter32
_McmFrAllSVCCircuitSentOctets_Object = MibTableColumn
mcmFrAllSVCCircuitSentOctets = _McmFrAllSVCCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 9),
    _McmFrAllSVCCircuitSentOctets_Type()
)
mcmFrAllSVCCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitSentOctets.setStatus("mandatory")
_McmFrAllSVCCircuitReceivedFrames_Type = Counter32
_McmFrAllSVCCircuitReceivedFrames_Object = MibTableColumn
mcmFrAllSVCCircuitReceivedFrames = _McmFrAllSVCCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 10),
    _McmFrAllSVCCircuitReceivedFrames_Type()
)
mcmFrAllSVCCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitReceivedFrames.setStatus("mandatory")
_McmFrAllSVCCircuitReceivedOctets_Type = Counter32
_McmFrAllSVCCircuitReceivedOctets_Object = MibTableColumn
mcmFrAllSVCCircuitReceivedOctets = _McmFrAllSVCCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 11),
    _McmFrAllSVCCircuitReceivedOctets_Type()
)
mcmFrAllSVCCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitReceivedOctets.setStatus("mandatory")
_McmFrAllSVCCircuitCreationTime_Type = TimeTicks
_McmFrAllSVCCircuitCreationTime_Object = MibTableColumn
mcmFrAllSVCCircuitCreationTime = _McmFrAllSVCCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 12),
    _McmFrAllSVCCircuitCreationTime_Type()
)
mcmFrAllSVCCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitCreationTime.setStatus("mandatory")


class _McmFrAllSVCCircuitCallOriginator_Type(OctetString):
    """Custom type mcmFrAllSVCCircuitCallOriginator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrAllSVCCircuitCallOriginator_Type.__name__ = "OctetString"
_McmFrAllSVCCircuitCallOriginator_Object = MibTableColumn
mcmFrAllSVCCircuitCallOriginator = _McmFrAllSVCCircuitCallOriginator_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 13),
    _McmFrAllSVCCircuitCallOriginator_Type()
)
mcmFrAllSVCCircuitCallOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitCallOriginator.setStatus("mandatory")
_McmFrAllSVCCircuitLastTimeChange_Type = TimeTicks
_McmFrAllSVCCircuitLastTimeChange_Object = MibTableColumn
mcmFrAllSVCCircuitLastTimeChange = _McmFrAllSVCCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 14),
    _McmFrAllSVCCircuitLastTimeChange_Type()
)
mcmFrAllSVCCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitLastTimeChange.setStatus("mandatory")


class _McmFrAllSVCCircuitCommittedBurst_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitCommittedBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitCommittedBurst_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitCommittedBurst_Object = MibTableColumn
mcmFrAllSVCCircuitCommittedBurst = _McmFrAllSVCCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 15),
    _McmFrAllSVCCircuitCommittedBurst_Type()
)
mcmFrAllSVCCircuitCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitCommittedBurst.setStatus("deprecated")


class _McmFrAllSVCCircuitExcessBurst_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitExcessBurst_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitExcessBurst_Object = MibTableColumn
mcmFrAllSVCCircuitExcessBurst = _McmFrAllSVCCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 16),
    _McmFrAllSVCCircuitExcessBurst_Type()
)
mcmFrAllSVCCircuitExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitExcessBurst.setStatus("deprecated")


class _McmFrAllSVCCircuitThroughput_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitThroughput_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitThroughput_Object = MibTableColumn
mcmFrAllSVCCircuitThroughput = _McmFrAllSVCCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 17),
    _McmFrAllSVCCircuitThroughput_Type()
)
mcmFrAllSVCCircuitThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitThroughput.setStatus("mandatory")


class _McmFrAllSVCCircuitNegMaxTxSize_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrAllSVCCircuitNegMaxTxSize_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegMaxTxSize_Object = MibTableColumn
mcmFrAllSVCCircuitNegMaxTxSize = _McmFrAllSVCCircuitNegMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 18),
    _McmFrAllSVCCircuitNegMaxTxSize_Type()
)
mcmFrAllSVCCircuitNegMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegMaxTxSize.setStatus("mandatory")


class _McmFrAllSVCCircuitNegMaxRxSize_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrAllSVCCircuitNegMaxRxSize_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegMaxRxSize_Object = MibTableColumn
mcmFrAllSVCCircuitNegMaxRxSize = _McmFrAllSVCCircuitNegMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 19),
    _McmFrAllSVCCircuitNegMaxRxSize_Type()
)
mcmFrAllSVCCircuitNegMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegMaxRxSize.setStatus("mandatory")


class _McmFrAllSVCCircuitNegTxThroughput_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitNegTxThroughput_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegTxThroughput_Object = MibTableColumn
mcmFrAllSVCCircuitNegTxThroughput = _McmFrAllSVCCircuitNegTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 20),
    _McmFrAllSVCCircuitNegTxThroughput_Type()
)
mcmFrAllSVCCircuitNegTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegTxThroughput.setStatus("mandatory")


class _McmFrAllSVCCircuitNegRxThroughput_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitNegRxThroughput_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegRxThroughput_Object = MibTableColumn
mcmFrAllSVCCircuitNegRxThroughput = _McmFrAllSVCCircuitNegRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 21),
    _McmFrAllSVCCircuitNegRxThroughput_Type()
)
mcmFrAllSVCCircuitNegRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegRxThroughput.setStatus("mandatory")


class _McmFrAllSVCCircuitNegTxBurst_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegTxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitNegTxBurst_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegTxBurst_Object = MibTableColumn
mcmFrAllSVCCircuitNegTxBurst = _McmFrAllSVCCircuitNegTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 22),
    _McmFrAllSVCCircuitNegTxBurst_Type()
)
mcmFrAllSVCCircuitNegTxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegTxBurst.setStatus("mandatory")


class _McmFrAllSVCCircuitNegRxBurst_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegRxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitNegRxBurst_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegRxBurst_Object = MibTableColumn
mcmFrAllSVCCircuitNegRxBurst = _McmFrAllSVCCircuitNegRxBurst_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 23),
    _McmFrAllSVCCircuitNegRxBurst_Type()
)
mcmFrAllSVCCircuitNegRxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegRxBurst.setStatus("mandatory")


class _McmFrAllSVCCircuitNegTxExcess_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegTxExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitNegTxExcess_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegTxExcess_Object = MibTableColumn
mcmFrAllSVCCircuitNegTxExcess = _McmFrAllSVCCircuitNegTxExcess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 24),
    _McmFrAllSVCCircuitNegTxExcess_Type()
)
mcmFrAllSVCCircuitNegTxExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegTxExcess.setStatus("mandatory")


class _McmFrAllSVCCircuitNegRxExcess_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitNegRxExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrAllSVCCircuitNegRxExcess_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitNegRxExcess_Object = MibTableColumn
mcmFrAllSVCCircuitNegRxExcess = _McmFrAllSVCCircuitNegRxExcess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 25),
    _McmFrAllSVCCircuitNegRxExcess_Type()
)
mcmFrAllSVCCircuitNegRxExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitNegRxExcess.setStatus("mandatory")
_McmFrAllSVCCircuitTxDiscardCIRPolice_Type = Counter32
_McmFrAllSVCCircuitTxDiscardCIRPolice_Object = MibTableColumn
mcmFrAllSVCCircuitTxDiscardCIRPolice = _McmFrAllSVCCircuitTxDiscardCIRPolice_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 26),
    _McmFrAllSVCCircuitTxDiscardCIRPolice_Type()
)
mcmFrAllSVCCircuitTxDiscardCIRPolice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitTxDiscardCIRPolice.setStatus("mandatory")


class _McmFrAllSVCCircuitPriority_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmFrAllSVCCircuitPriority_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitPriority_Object = MibTableColumn
mcmFrAllSVCCircuitPriority = _McmFrAllSVCCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 27),
    _McmFrAllSVCCircuitPriority_Type()
)
mcmFrAllSVCCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitPriority.setStatus("mandatory")
_McmFrAllSVCCircuitSvcIfIndex_Type = Integer32
_McmFrAllSVCCircuitSvcIfIndex_Object = MibTableColumn
mcmFrAllSVCCircuitSvcIfIndex = _McmFrAllSVCCircuitSvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 28),
    _McmFrAllSVCCircuitSvcIfIndex_Type()
)
mcmFrAllSVCCircuitSvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitSvcIfIndex.setStatus("mandatory")


class _McmFrAllSVCCircuitDiscardPriority_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_McmFrAllSVCCircuitDiscardPriority_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitDiscardPriority_Object = MibTableColumn
mcmFrAllSVCCircuitDiscardPriority = _McmFrAllSVCCircuitDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 29),
    _McmFrAllSVCCircuitDiscardPriority_Type()
)
mcmFrAllSVCCircuitDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitDiscardPriority.setStatus("mandatory")


class _McmFrAllSVCCircuitSetupPriority_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrAllSVCCircuitSetupPriority_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitSetupPriority_Object = MibTableColumn
mcmFrAllSVCCircuitSetupPriority = _McmFrAllSVCCircuitSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 30),
    _McmFrAllSVCCircuitSetupPriority_Type()
)
mcmFrAllSVCCircuitSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitSetupPriority.setStatus("mandatory")


class _McmFrAllSVCCircuitHoldingPriority_Type(Integer32):
    """Custom type mcmFrAllSVCCircuitHoldingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrAllSVCCircuitHoldingPriority_Type.__name__ = "Integer32"
_McmFrAllSVCCircuitHoldingPriority_Object = MibTableColumn
mcmFrAllSVCCircuitHoldingPriority = _McmFrAllSVCCircuitHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 17, 1, 31),
    _McmFrAllSVCCircuitHoldingPriority_Type()
)
mcmFrAllSVCCircuitHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrAllSVCCircuitHoldingPriority.setStatus("mandatory")
_McmFrLANSpvcTable_Object = MibTable
mcmFrLANSpvcTable = _McmFrLANSpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18)
)
if mibBuilder.loadTexts:
    mcmFrLANSpvcTable.setStatus("mandatory")
_McmFrLANSpvcEntry_Object = MibTableRow
mcmFrLANSpvcEntry = _McmFrLANSpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1)
)
mcmFrLANSpvcEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrLANSpvcVirtualPortIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrLANSpvcRemoteDLCI"),
)
if mibBuilder.loadTexts:
    mcmFrLANSpvcEntry.setStatus("mandatory")


class _McmFrLANSpvcVirtualPortIfIndex_Type(Integer32):
    """Custom type mcmFrLANSpvcVirtualPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrLANSpvcVirtualPortIfIndex_Type.__name__ = "Integer32"
_McmFrLANSpvcVirtualPortIfIndex_Object = MibTableColumn
mcmFrLANSpvcVirtualPortIfIndex = _McmFrLANSpvcVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 1),
    _McmFrLANSpvcVirtualPortIfIndex_Type()
)
mcmFrLANSpvcVirtualPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcVirtualPortIfIndex.setStatus("mandatory")


class _McmFrLANSpvcRemoteDLCI_Type(Integer32):
    """Custom type mcmFrLANSpvcRemoteDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrLANSpvcRemoteDLCI_Type.__name__ = "Integer32"
_McmFrLANSpvcRemoteDLCI_Object = MibTableColumn
mcmFrLANSpvcRemoteDLCI = _McmFrLANSpvcRemoteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 2),
    _McmFrLANSpvcRemoteDLCI_Type()
)
mcmFrLANSpvcRemoteDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcRemoteDLCI.setStatus("mandatory")


class _McmFrLANSpvcConnectId_Type(Integer32):
    """Custom type mcmFrLANSpvcConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmFrLANSpvcConnectId_Type.__name__ = "Integer32"
_McmFrLANSpvcConnectId_Object = MibTableColumn
mcmFrLANSpvcConnectId = _McmFrLANSpvcConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 3),
    _McmFrLANSpvcConnectId_Type()
)
mcmFrLANSpvcConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcConnectId.setStatus("mandatory")


class _McmFrLANSpvcRemoteDNA_Type(DisplayString):
    """Custom type mcmFrLANSpvcRemoteDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrLANSpvcRemoteDNA_Type.__name__ = "DisplayString"
_McmFrLANSpvcRemoteDNA_Object = MibTableColumn
mcmFrLANSpvcRemoteDNA = _McmFrLANSpvcRemoteDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 4),
    _McmFrLANSpvcRemoteDNA_Type()
)
mcmFrLANSpvcRemoteDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcRemoteDNA.setStatus("mandatory")


class _McmFrLANSpvcDLCI_Type(Integer32):
    """Custom type mcmFrLANSpvcDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrLANSpvcDLCI_Type.__name__ = "Integer32"
_McmFrLANSpvcDLCI_Object = MibTableColumn
mcmFrLANSpvcDLCI = _McmFrLANSpvcDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 5),
    _McmFrLANSpvcDLCI_Type()
)
mcmFrLANSpvcDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcDLCI.setStatus("mandatory")


class _McmFrLANSpvcIfIndex_Type(Integer32):
    """Custom type mcmFrLANSpvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrLANSpvcIfIndex_Type.__name__ = "Integer32"
_McmFrLANSpvcIfIndex_Object = MibTableColumn
mcmFrLANSpvcIfIndex = _McmFrLANSpvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 6),
    _McmFrLANSpvcIfIndex_Type()
)
mcmFrLANSpvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcIfIndex.setStatus("mandatory")


class _McmFrLANSpvcVPState_Type(Integer32):
    """Custom type mcmFrLANSpvcVPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_McmFrLANSpvcVPState_Type.__name__ = "Integer32"
_McmFrLANSpvcVPState_Object = MibTableColumn
mcmFrLANSpvcVPState = _McmFrLANSpvcVPState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 7),
    _McmFrLANSpvcVPState_Type()
)
mcmFrLANSpvcVPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcVPState.setStatus("mandatory")


class _McmFrLANSpvcSVCState_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_McmFrLANSpvcSVCState_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCState_Object = MibTableColumn
mcmFrLANSpvcSVCState = _McmFrLANSpvcSVCState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 8),
    _McmFrLANSpvcSVCState_Type()
)
mcmFrLANSpvcSVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCState.setStatus("mandatory")


class _McmFrLANSpvcConnType_Type(Integer32):
    """Custom type mcmFrLANSpvcConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_McmFrLANSpvcConnType_Type.__name__ = "Integer32"
_McmFrLANSpvcConnType_Object = MibTableColumn
mcmFrLANSpvcConnType = _McmFrLANSpvcConnType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 9),
    _McmFrLANSpvcConnType_Type()
)
mcmFrLANSpvcConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcConnType.setStatus("mandatory")
_McmFrLANSpvcLastChange_Type = TimeTicks
_McmFrLANSpvcLastChange_Object = MibTableColumn
mcmFrLANSpvcLastChange = _McmFrLANSpvcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 10),
    _McmFrLANSpvcLastChange_Type()
)
mcmFrLANSpvcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcLastChange.setStatus("mandatory")


class _McmFrLANSpvcDisconnectReason_Type(Integer32):
    """Custom type mcmFrLANSpvcDisconnectReason based on Integer32"""
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
        *(("local-SVC-LMI-is-Down", 2),
          ("local-VP-is-down", 1),
          ("remote-PVC-LMI-is-down", 3),
          ("the-SVC-connection-is-down", 4))
    )


_McmFrLANSpvcDisconnectReason_Type.__name__ = "Integer32"
_McmFrLANSpvcDisconnectReason_Object = MibTableColumn
mcmFrLANSpvcDisconnectReason = _McmFrLANSpvcDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 18, 1, 11),
    _McmFrLANSpvcDisconnectReason_Type()
)
mcmFrLANSpvcDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcDisconnectReason.setStatus("mandatory")
_McmFrLANSpvcSVCTable_Object = MibTable
mcmFrLANSpvcSVCTable = _McmFrLANSpvcSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19)
)
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCTable.setStatus("mandatory")
_McmFrLANSpvcSVCEntry_Object = MibTableRow
mcmFrLANSpvcSVCEntry = _McmFrLANSpvcSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1)
)
mcmFrLANSpvcSVCEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrLANSpvcSVCConnectId"),
)
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCEntry.setStatus("mandatory")


class _McmFrLANSpvcSVCConnectId_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmFrLANSpvcSVCConnectId_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCConnectId_Object = MibTableColumn
mcmFrLANSpvcSVCConnectId = _McmFrLANSpvcSVCConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 1),
    _McmFrLANSpvcSVCConnectId_Type()
)
mcmFrLANSpvcSVCConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCConnectId.setStatus("mandatory")


class _McmFrLANSpvcSVCIfIndex_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrLANSpvcSVCIfIndex_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCIfIndex_Object = MibTableColumn
mcmFrLANSpvcSVCIfIndex = _McmFrLANSpvcSVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 2),
    _McmFrLANSpvcSVCIfIndex_Type()
)
mcmFrLANSpvcSVCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCIfIndex.setStatus("mandatory")


class _McmFrLANSpvcSVCDNA_Type(DisplayString):
    """Custom type mcmFrLANSpvcSVCDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmFrLANSpvcSVCDNA_Type.__name__ = "DisplayString"
_McmFrLANSpvcSVCDNA_Object = MibTableColumn
mcmFrLANSpvcSVCDNA = _McmFrLANSpvcSVCDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 3),
    _McmFrLANSpvcSVCDNA_Type()
)
mcmFrLANSpvcSVCDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCDNA.setStatus("mandatory")


class _McmFrLANSpvcSVCDLCI_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrLANSpvcSVCDLCI_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCDLCI_Object = MibTableColumn
mcmFrLANSpvcSVCDLCI = _McmFrLANSpvcSVCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 4),
    _McmFrLANSpvcSVCDLCI_Type()
)
mcmFrLANSpvcSVCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCDLCI.setStatus("mandatory")


class _McmFrLANSpvcSVCMaxTxSize_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrLANSpvcSVCMaxTxSize_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMaxTxSize_Object = MibTableColumn
mcmFrLANSpvcSVCMaxTxSize = _McmFrLANSpvcSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 5),
    _McmFrLANSpvcSVCMaxTxSize_Type()
)
mcmFrLANSpvcSVCMaxTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMaxTxSize.setStatus("mandatory")


class _McmFrLANSpvcSVCMaxRxSize_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrLANSpvcSVCMaxRxSize_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMaxRxSize_Object = MibTableColumn
mcmFrLANSpvcSVCMaxRxSize = _McmFrLANSpvcSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 6),
    _McmFrLANSpvcSVCMaxRxSize_Type()
)
mcmFrLANSpvcSVCMaxRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMaxRxSize.setStatus("mandatory")


class _McmFrLANSpvcSVCMinTxThroughput_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMinTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCMinTxThroughput_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMinTxThroughput_Object = MibTableColumn
mcmFrLANSpvcSVCMinTxThroughput = _McmFrLANSpvcSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 7),
    _McmFrLANSpvcSVCMinTxThroughput_Type()
)
mcmFrLANSpvcSVCMinTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMinTxThroughput.setStatus("mandatory")


class _McmFrLANSpvcSVCMinRxThroughput_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMinRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCMinRxThroughput_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMinRxThroughput_Object = MibTableColumn
mcmFrLANSpvcSVCMinRxThroughput = _McmFrLANSpvcSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 8),
    _McmFrLANSpvcSVCMinRxThroughput_Type()
)
mcmFrLANSpvcSVCMinRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMinRxThroughput.setStatus("mandatory")


class _McmFrLANSpvcSVCMaxTxThroughput_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMaxTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCMaxTxThroughput_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMaxTxThroughput_Object = MibTableColumn
mcmFrLANSpvcSVCMaxTxThroughput = _McmFrLANSpvcSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 9),
    _McmFrLANSpvcSVCMaxTxThroughput_Type()
)
mcmFrLANSpvcSVCMaxTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMaxTxThroughput.setStatus("mandatory")


class _McmFrLANSpvcSVCMaxRxThroughput_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMaxRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCMaxRxThroughput_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMaxRxThroughput_Object = MibTableColumn
mcmFrLANSpvcSVCMaxRxThroughput = _McmFrLANSpvcSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 10),
    _McmFrLANSpvcSVCMaxRxThroughput_Type()
)
mcmFrLANSpvcSVCMaxRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMaxRxThroughput.setStatus("mandatory")


class _McmFrLANSpvcSVCMaxTxBurstSize_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMaxTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCMaxTxBurstSize_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMaxTxBurstSize_Object = MibTableColumn
mcmFrLANSpvcSVCMaxTxBurstSize = _McmFrLANSpvcSVCMaxTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 11),
    _McmFrLANSpvcSVCMaxTxBurstSize_Type()
)
mcmFrLANSpvcSVCMaxTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMaxTxBurstSize.setStatus("mandatory")


class _McmFrLANSpvcSVCMaxRxBurstSize_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCMaxRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCMaxRxBurstSize_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCMaxRxBurstSize_Object = MibTableColumn
mcmFrLANSpvcSVCMaxRxBurstSize = _McmFrLANSpvcSVCMaxRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 12),
    _McmFrLANSpvcSVCMaxRxBurstSize_Type()
)
mcmFrLANSpvcSVCMaxRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCMaxRxBurstSize.setStatus("mandatory")


class _McmFrLANSpvcSVCExcessTxBurstSize_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCExcessTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCExcessTxBurstSize_Object = MibTableColumn
mcmFrLANSpvcSVCExcessTxBurstSize = _McmFrLANSpvcSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 13),
    _McmFrLANSpvcSVCExcessTxBurstSize_Type()
)
mcmFrLANSpvcSVCExcessTxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCExcessTxBurstSize.setStatus("mandatory")


class _McmFrLANSpvcSVCExcessRxBurstSize_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCExcessRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrLANSpvcSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCExcessRxBurstSize_Object = MibTableColumn
mcmFrLANSpvcSVCExcessRxBurstSize = _McmFrLANSpvcSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 14),
    _McmFrLANSpvcSVCExcessRxBurstSize_Type()
)
mcmFrLANSpvcSVCExcessRxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCExcessRxBurstSize.setStatus("mandatory")


class _McmFrLANSpvcSVCTransferPriority_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmFrLANSpvcSVCTransferPriority_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCTransferPriority_Object = MibTableColumn
mcmFrLANSpvcSVCTransferPriority = _McmFrLANSpvcSVCTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 15),
    _McmFrLANSpvcSVCTransferPriority_Type()
)
mcmFrLANSpvcSVCTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCTransferPriority.setStatus("mandatory")


class _McmFrLANSpvcSVCReasonForDisconnect_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCReasonForDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              21,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              47,
              49,
              50,
              57,
              58,
              63,
              65,
              66,
              70,
              79,
              81,
              82,
              87,
              88,
              90,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              111,
              127,
              128)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-implemented", 65),
          ("bearer-capability-not-presently-available", 58),
          ("call-awarded-and-being-delivered-in-an-est-channel", 7),
          ("channel-type-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("destination-out-of-order", 27),
          ("element-non-existent-or-not-implemented", 99),
          ("facility-rejected", 29),
          ("identified-channel-does-not-exist", 82),
          ("incompatible-destination", 88),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-element", 100),
          ("invalid-message-for-state", 101),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network-selection", 91),
          ("message-not-compatible", 98),
          ("message-type-unknown", 97),
          ("missing-element", 96),
          ("network-out-of-order", 38),
          ("no-DLCI-available", 34),
          ("no-route-to-destination", 3),
          ("no-route-to-specified-transit-network", 2),
          ("no-user-present-in-call", 18),
          ("non-existent-CUG", 90),
          ("normal-call-clearing", 16),
          ("normal-condition", 128),
          ("normal-unspecified", 31),
          ("only-restricted-digital-capability-is-available", 70),
          ("permanent-frame-mode-connection-operational", 40),
          ("permanent-frame-mode-connection-out-of-service", 39),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-not-available", 49),
          ("remote-PVC-already-connected-ie-busy", 17),
          ("remote-PVC-down-ie-unavailable", 21),
          ("requested-facility-not-subscribed", 50),
          ("resource-unavailable", 47),
          ("response-to-status-inquiry", 30),
          ("service-or-option-not-available-unspecified", 63),
          ("service-or-option-not-implemented-unspecified", 79),
          ("specified-DLCI-unavailable", 44),
          ("switching-equipment-congestion", 42),
          ("temporary-failure", 41),
          ("the-PVC-does-not-exist-ie-unassigned", 1),
          ("timer-recovery", 102),
          ("user-not-member-of-CUG", 87))
    )


_McmFrLANSpvcSVCReasonForDisconnect_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCReasonForDisconnect_Object = MibTableColumn
mcmFrLANSpvcSVCReasonForDisconnect = _McmFrLANSpvcSVCReasonForDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 16),
    _McmFrLANSpvcSVCReasonForDisconnect_Type()
)
mcmFrLANSpvcSVCReasonForDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCReasonForDisconnect.setStatus("mandatory")


class _McmFrLANSpvcSVCDiscardPriority_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_McmFrLANSpvcSVCDiscardPriority_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCDiscardPriority_Object = MibTableColumn
mcmFrLANSpvcSVCDiscardPriority = _McmFrLANSpvcSVCDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 17),
    _McmFrLANSpvcSVCDiscardPriority_Type()
)
mcmFrLANSpvcSVCDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCDiscardPriority.setStatus("mandatory")


class _McmFrLANSpvcSVCSetupPriority_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrLANSpvcSVCSetupPriority_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCSetupPriority_Object = MibTableColumn
mcmFrLANSpvcSVCSetupPriority = _McmFrLANSpvcSVCSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 18),
    _McmFrLANSpvcSVCSetupPriority_Type()
)
mcmFrLANSpvcSVCSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCSetupPriority.setStatus("mandatory")


class _McmFrLANSpvcSVCHoldingPriority_Type(Integer32):
    """Custom type mcmFrLANSpvcSVCHoldingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrLANSpvcSVCHoldingPriority_Type.__name__ = "Integer32"
_McmFrLANSpvcSVCHoldingPriority_Object = MibTableColumn
mcmFrLANSpvcSVCHoldingPriority = _McmFrLANSpvcSVCHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 19, 1, 19),
    _McmFrLANSpvcSVCHoldingPriority_Type()
)
mcmFrLANSpvcSVCHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLANSpvcSVCHoldingPriority.setStatus("mandatory")
_NvmFrLANSpvcTable_Object = MibTable
nvmFrLANSpvcTable = _NvmFrLANSpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20)
)
if mibBuilder.loadTexts:
    nvmFrLANSpvcTable.setStatus("mandatory")
_NvmFrLANSpvcEntry_Object = MibTableRow
nvmFrLANSpvcEntry = _NvmFrLANSpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1)
)
nvmFrLANSpvcEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrLANSpvcVirtualPortIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrLANSpvcRemoteDLCI"),
)
if mibBuilder.loadTexts:
    nvmFrLANSpvcEntry.setStatus("mandatory")


class _NvmFrLANSpvcVirtualPortIfIndex_Type(Integer32):
    """Custom type nvmFrLANSpvcVirtualPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrLANSpvcVirtualPortIfIndex_Type.__name__ = "Integer32"
_NvmFrLANSpvcVirtualPortIfIndex_Object = MibTableColumn
nvmFrLANSpvcVirtualPortIfIndex = _NvmFrLANSpvcVirtualPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1, 1),
    _NvmFrLANSpvcVirtualPortIfIndex_Type()
)
nvmFrLANSpvcVirtualPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcVirtualPortIfIndex.setStatus("mandatory")


class _NvmFrLANSpvcRemoteDLCI_Type(Integer32):
    """Custom type nvmFrLANSpvcRemoteDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NvmFrLANSpvcRemoteDLCI_Type.__name__ = "Integer32"
_NvmFrLANSpvcRemoteDLCI_Object = MibTableColumn
nvmFrLANSpvcRemoteDLCI = _NvmFrLANSpvcRemoteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1, 2),
    _NvmFrLANSpvcRemoteDLCI_Type()
)
nvmFrLANSpvcRemoteDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcRemoteDLCI.setStatus("mandatory")


class _NvmFrLANSpvcConnectId_Type(Integer32):
    """Custom type nvmFrLANSpvcConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmFrLANSpvcConnectId_Type.__name__ = "Integer32"
_NvmFrLANSpvcConnectId_Object = MibTableColumn
nvmFrLANSpvcConnectId = _NvmFrLANSpvcConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1, 3),
    _NvmFrLANSpvcConnectId_Type()
)
nvmFrLANSpvcConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrLANSpvcConnectId.setStatus("mandatory")


class _NvmFrLANSpvcRemoteDNA_Type(DisplayString):
    """Custom type nvmFrLANSpvcRemoteDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmFrLANSpvcRemoteDNA_Type.__name__ = "DisplayString"
_NvmFrLANSpvcRemoteDNA_Object = MibTableColumn
nvmFrLANSpvcRemoteDNA = _NvmFrLANSpvcRemoteDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1, 4),
    _NvmFrLANSpvcRemoteDNA_Type()
)
nvmFrLANSpvcRemoteDNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcRemoteDNA.setStatus("mandatory")


class _NvmFrLANSpvcConnType_Type(Integer32):
    """Custom type nvmFrLANSpvcConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_NvmFrLANSpvcConnType_Type.__name__ = "Integer32"
_NvmFrLANSpvcConnType_Object = MibTableColumn
nvmFrLANSpvcConnType = _NvmFrLANSpvcConnType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1, 5),
    _NvmFrLANSpvcConnType_Type()
)
nvmFrLANSpvcConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcConnType.setStatus("mandatory")


class _NvmFrLANSpvcRowStatus_Type(Integer32):
    """Custom type nvmFrLANSpvcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_NvmFrLANSpvcRowStatus_Type.__name__ = "Integer32"
_NvmFrLANSpvcRowStatus_Object = MibTableColumn
nvmFrLANSpvcRowStatus = _NvmFrLANSpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 20, 1, 6),
    _NvmFrLANSpvcRowStatus_Type()
)
nvmFrLANSpvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcRowStatus.setStatus("mandatory")
_NvmFrLANSpvcSVCTable_Object = MibTable
nvmFrLANSpvcSVCTable = _NvmFrLANSpvcSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21)
)
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCTable.setStatus("mandatory")
_NvmFrLANSpvcSVCEntry_Object = MibTableRow
nvmFrLANSpvcSVCEntry = _NvmFrLANSpvcSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1)
)
nvmFrLANSpvcSVCEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrLANSpvcSVCConnectId"),
)
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCEntry.setStatus("mandatory")


class _NvmFrLANSpvcSVCConnectId_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCConnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmFrLANSpvcSVCConnectId_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCConnectId_Object = MibTableColumn
nvmFrLANSpvcSVCConnectId = _NvmFrLANSpvcSVCConnectId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 1),
    _NvmFrLANSpvcSVCConnectId_Type()
)
nvmFrLANSpvcSVCConnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCConnectId.setStatus("mandatory")


class _NvmFrLANSpvcSVCDNA_Type(DisplayString):
    """Custom type nvmFrLANSpvcSVCDNA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmFrLANSpvcSVCDNA_Type.__name__ = "DisplayString"
_NvmFrLANSpvcSVCDNA_Object = MibTableColumn
nvmFrLANSpvcSVCDNA = _NvmFrLANSpvcSVCDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 2),
    _NvmFrLANSpvcSVCDNA_Type()
)
nvmFrLANSpvcSVCDNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCDNA.setStatus("mandatory")


class _NvmFrLANSpvcSVCMaxTxSize_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMaxTxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrLANSpvcSVCMaxTxSize_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMaxTxSize_Object = MibTableColumn
nvmFrLANSpvcSVCMaxTxSize = _NvmFrLANSpvcSVCMaxTxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 3),
    _NvmFrLANSpvcSVCMaxTxSize_Type()
)
nvmFrLANSpvcSVCMaxTxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMaxTxSize.setStatus("mandatory")


class _NvmFrLANSpvcSVCMaxRxSize_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMaxRxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrLANSpvcSVCMaxRxSize_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMaxRxSize_Object = MibTableColumn
nvmFrLANSpvcSVCMaxRxSize = _NvmFrLANSpvcSVCMaxRxSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 4),
    _NvmFrLANSpvcSVCMaxRxSize_Type()
)
nvmFrLANSpvcSVCMaxRxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMaxRxSize.setStatus("mandatory")


class _NvmFrLANSpvcSVCMinTxThroughput_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMinTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCMinTxThroughput_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMinTxThroughput_Object = MibTableColumn
nvmFrLANSpvcSVCMinTxThroughput = _NvmFrLANSpvcSVCMinTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 5),
    _NvmFrLANSpvcSVCMinTxThroughput_Type()
)
nvmFrLANSpvcSVCMinTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMinTxThroughput.setStatus("mandatory")


class _NvmFrLANSpvcSVCMinRxThroughput_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMinRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCMinRxThroughput_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMinRxThroughput_Object = MibTableColumn
nvmFrLANSpvcSVCMinRxThroughput = _NvmFrLANSpvcSVCMinRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 6),
    _NvmFrLANSpvcSVCMinRxThroughput_Type()
)
nvmFrLANSpvcSVCMinRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMinRxThroughput.setStatus("mandatory")


class _NvmFrLANSpvcSVCMaxTxThroughput_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMaxTxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCMaxTxThroughput_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMaxTxThroughput_Object = MibTableColumn
nvmFrLANSpvcSVCMaxTxThroughput = _NvmFrLANSpvcSVCMaxTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 7),
    _NvmFrLANSpvcSVCMaxTxThroughput_Type()
)
nvmFrLANSpvcSVCMaxTxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMaxTxThroughput.setStatus("mandatory")


class _NvmFrLANSpvcSVCMaxRxThroughput_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMaxRxThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCMaxRxThroughput_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMaxRxThroughput_Object = MibTableColumn
nvmFrLANSpvcSVCMaxRxThroughput = _NvmFrLANSpvcSVCMaxRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 8),
    _NvmFrLANSpvcSVCMaxRxThroughput_Type()
)
nvmFrLANSpvcSVCMaxRxThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMaxRxThroughput.setStatus("mandatory")


class _NvmFrLANSpvcSVCMaxTxBurstSize_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMaxTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCMaxTxBurstSize_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMaxTxBurstSize_Object = MibTableColumn
nvmFrLANSpvcSVCMaxTxBurstSize = _NvmFrLANSpvcSVCMaxTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 9),
    _NvmFrLANSpvcSVCMaxTxBurstSize_Type()
)
nvmFrLANSpvcSVCMaxTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMaxTxBurstSize.setStatus("mandatory")


class _NvmFrLANSpvcSVCMaxRxBurstSize_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCMaxRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCMaxRxBurstSize_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCMaxRxBurstSize_Object = MibTableColumn
nvmFrLANSpvcSVCMaxRxBurstSize = _NvmFrLANSpvcSVCMaxRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 10),
    _NvmFrLANSpvcSVCMaxRxBurstSize_Type()
)
nvmFrLANSpvcSVCMaxRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCMaxRxBurstSize.setStatus("mandatory")


class _NvmFrLANSpvcSVCExcessTxBurstSize_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCExcessTxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCExcessTxBurstSize_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCExcessTxBurstSize_Object = MibTableColumn
nvmFrLANSpvcSVCExcessTxBurstSize = _NvmFrLANSpvcSVCExcessTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 11),
    _NvmFrLANSpvcSVCExcessTxBurstSize_Type()
)
nvmFrLANSpvcSVCExcessTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCExcessTxBurstSize.setStatus("mandatory")


class _NvmFrLANSpvcSVCExcessRxBurstSize_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCExcessRxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrLANSpvcSVCExcessRxBurstSize_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCExcessRxBurstSize_Object = MibTableColumn
nvmFrLANSpvcSVCExcessRxBurstSize = _NvmFrLANSpvcSVCExcessRxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 12),
    _NvmFrLANSpvcSVCExcessRxBurstSize_Type()
)
nvmFrLANSpvcSVCExcessRxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCExcessRxBurstSize.setStatus("mandatory")


class _NvmFrLANSpvcSVCTransferPriority_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCTransferPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NvmFrLANSpvcSVCTransferPriority_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCTransferPriority_Object = MibTableColumn
nvmFrLANSpvcSVCTransferPriority = _NvmFrLANSpvcSVCTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 13),
    _NvmFrLANSpvcSVCTransferPriority_Type()
)
nvmFrLANSpvcSVCTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCTransferPriority.setStatus("mandatory")


class _NvmFrLANSpvcSVCDiscardPriority_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-discard-level", 3),
          ("low-discard-level", 1),
          ("medium-discard-level", 2))
    )


_NvmFrLANSpvcSVCDiscardPriority_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCDiscardPriority_Object = MibTableColumn
nvmFrLANSpvcSVCDiscardPriority = _NvmFrLANSpvcSVCDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 14),
    _NvmFrLANSpvcSVCDiscardPriority_Type()
)
nvmFrLANSpvcSVCDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCDiscardPriority.setStatus("mandatory")


class _NvmFrLANSpvcSVCSetupPriority_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCSetupPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmFrLANSpvcSVCSetupPriority_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCSetupPriority_Object = MibTableColumn
nvmFrLANSpvcSVCSetupPriority = _NvmFrLANSpvcSVCSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 15),
    _NvmFrLANSpvcSVCSetupPriority_Type()
)
nvmFrLANSpvcSVCSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCSetupPriority.setStatus("mandatory")


class _NvmFrLANSpvcSVCHoldingPriority_Type(Integer32):
    """Custom type nvmFrLANSpvcSVCHoldingPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvmFrLANSpvcSVCHoldingPriority_Type.__name__ = "Integer32"
_NvmFrLANSpvcSVCHoldingPriority_Object = MibTableColumn
nvmFrLANSpvcSVCHoldingPriority = _NvmFrLANSpvcSVCHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 21, 1, 16),
    _NvmFrLANSpvcSVCHoldingPriority_Type()
)
nvmFrLANSpvcSVCHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLANSpvcSVCHoldingPriority.setStatus("mandatory")
_McmFrDlcmiSVCStatusTable_Object = MibTable
mcmFrDlcmiSVCStatusTable = _McmFrDlcmiSVCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22)
)
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusTable.setStatus("mandatory")
_McmFrDlcmiSVCStatusEntry_Object = MibTableRow
mcmFrDlcmiSVCStatusEntry = _McmFrDlcmiSVCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1)
)
mcmFrDlcmiSVCStatusEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrDlcmiSVCStatusIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrDlcmiSVCStatusDlci"),
)
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusEntry.setStatus("mandatory")


class _McmFrDlcmiSVCStatusIfIndex_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrDlcmiSVCStatusIfIndex_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusIfIndex_Object = MibTableColumn
mcmFrDlcmiSVCStatusIfIndex = _McmFrDlcmiSVCStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 1),
    _McmFrDlcmiSVCStatusIfIndex_Type()
)
mcmFrDlcmiSVCStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusIfIndex.setStatus("mandatory")


class _McmFrDlcmiSVCStatusDlci_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 991),
    )


_McmFrDlcmiSVCStatusDlci_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusDlci_Object = MibTableColumn
mcmFrDlcmiSVCStatusDlci = _McmFrDlcmiSVCStatusDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 2),
    _McmFrDlcmiSVCStatusDlci_Type()
)
mcmFrDlcmiSVCStatusDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusDlci.setStatus("mandatory")


class _McmFrDlcmiSVCStatusCardNumber_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrDlcmiSVCStatusCardNumber_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusCardNumber_Object = MibTableColumn
mcmFrDlcmiSVCStatusCardNumber = _McmFrDlcmiSVCStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 3),
    _McmFrDlcmiSVCStatusCardNumber_Type()
)
mcmFrDlcmiSVCStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusCardNumber.setStatus("mandatory")


class _McmFrDlcmiSVCStatusPortNumber_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_McmFrDlcmiSVCStatusPortNumber_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusPortNumber_Object = MibTableColumn
mcmFrDlcmiSVCStatusPortNumber = _McmFrDlcmiSVCStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 4),
    _McmFrDlcmiSVCStatusPortNumber_Type()
)
mcmFrDlcmiSVCStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusPortNumber.setStatus("mandatory")


class _McmFrDlcmiSVCStatusTunnelPvcDlci_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusTunnelPvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrDlcmiSVCStatusTunnelPvcDlci_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusTunnelPvcDlci_Object = MibTableColumn
mcmFrDlcmiSVCStatusTunnelPvcDlci = _McmFrDlcmiSVCStatusTunnelPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 5),
    _McmFrDlcmiSVCStatusTunnelPvcDlci_Type()
)
mcmFrDlcmiSVCStatusTunnelPvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusTunnelPvcDlci.setStatus("mandatory")


class _McmFrDlcmiSVCStatusPeerCardNumber_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusPeerCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_McmFrDlcmiSVCStatusPeerCardNumber_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusPeerCardNumber_Object = MibTableColumn
mcmFrDlcmiSVCStatusPeerCardNumber = _McmFrDlcmiSVCStatusPeerCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 6),
    _McmFrDlcmiSVCStatusPeerCardNumber_Type()
)
mcmFrDlcmiSVCStatusPeerCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusPeerCardNumber.setStatus("mandatory")


class _McmFrDlcmiSVCStatusPeerPortNumber_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusPeerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_McmFrDlcmiSVCStatusPeerPortNumber_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusPeerPortNumber_Object = MibTableColumn
mcmFrDlcmiSVCStatusPeerPortNumber = _McmFrDlcmiSVCStatusPeerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 7),
    _McmFrDlcmiSVCStatusPeerPortNumber_Type()
)
mcmFrDlcmiSVCStatusPeerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusPeerPortNumber.setStatus("mandatory")


class _McmFrDlcmiSVCStatusPeerTunPvcDlci_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusPeerTunPvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrDlcmiSVCStatusPeerTunPvcDlci_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusPeerTunPvcDlci_Object = MibTableColumn
mcmFrDlcmiSVCStatusPeerTunPvcDlci = _McmFrDlcmiSVCStatusPeerTunPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 8),
    _McmFrDlcmiSVCStatusPeerTunPvcDlci_Type()
)
mcmFrDlcmiSVCStatusPeerTunPvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusPeerTunPvcDlci.setStatus("mandatory")


class _McmFrDlcmiSVCStatusPeerSvcDlci_Type(Integer32):
    """Custom type mcmFrDlcmiSVCStatusPeerSvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 991),
    )


_McmFrDlcmiSVCStatusPeerSvcDlci_Type.__name__ = "Integer32"
_McmFrDlcmiSVCStatusPeerSvcDlci_Object = MibTableColumn
mcmFrDlcmiSVCStatusPeerSvcDlci = _McmFrDlcmiSVCStatusPeerSvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 22, 1, 9),
    _McmFrDlcmiSVCStatusPeerSvcDlci_Type()
)
mcmFrDlcmiSVCStatusPeerSvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrDlcmiSVCStatusPeerSvcDlci.setStatus("mandatory")
_McmFrTunnelPvcTable_Object = MibTable
mcmFrTunnelPvcTable = _McmFrTunnelPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23)
)
if mibBuilder.loadTexts:
    mcmFrTunnelPvcTable.setStatus("mandatory")
_McmFrTunnelPvcEntry_Object = MibTableRow
mcmFrTunnelPvcEntry = _McmFrTunnelPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1)
)
mcmFrTunnelPvcEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrTunnelPvcIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrTunnelPvcEntry.setStatus("mandatory")


class _McmFrTunnelPvcIfIndex_Type(Integer32):
    """Custom type mcmFrTunnelPvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrTunnelPvcIfIndex_Type.__name__ = "Integer32"
_McmFrTunnelPvcIfIndex_Object = MibTableColumn
mcmFrTunnelPvcIfIndex = _McmFrTunnelPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 1),
    _McmFrTunnelPvcIfIndex_Type()
)
mcmFrTunnelPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcIfIndex.setStatus("mandatory")


class _McmFrTunnelPvcDlciNumber_Type(Integer32):
    """Custom type mcmFrTunnelPvcDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrTunnelPvcDlciNumber_Type.__name__ = "Integer32"
_McmFrTunnelPvcDlciNumber_Object = MibTableColumn
mcmFrTunnelPvcDlciNumber = _McmFrTunnelPvcDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 2),
    _McmFrTunnelPvcDlciNumber_Type()
)
mcmFrTunnelPvcDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcDlciNumber.setStatus("mandatory")


class _McmFrTunnelPvcPhysicalCard_Type(Integer32):
    """Custom type mcmFrTunnelPvcPhysicalCard based on Integer32"""
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1))
    )


_McmFrTunnelPvcPhysicalCard_Type.__name__ = "Integer32"
_McmFrTunnelPvcPhysicalCard_Object = MibTableColumn
mcmFrTunnelPvcPhysicalCard = _McmFrTunnelPvcPhysicalCard_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 3),
    _McmFrTunnelPvcPhysicalCard_Type()
)
mcmFrTunnelPvcPhysicalCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcPhysicalCard.setStatus("mandatory")


class _McmFrTunnelPvcPhysicalPort_Type(Integer32):
    """Custom type mcmFrTunnelPvcPhysicalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_McmFrTunnelPvcPhysicalPort_Type.__name__ = "Integer32"
_McmFrTunnelPvcPhysicalPort_Object = MibTableColumn
mcmFrTunnelPvcPhysicalPort = _McmFrTunnelPvcPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 4),
    _McmFrTunnelPvcPhysicalPort_Type()
)
mcmFrTunnelPvcPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcPhysicalPort.setStatus("mandatory")


class _McmFrTunnelPvcType_Type(Integer32):
    """Custom type mcmFrTunnelPvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce-panl", 2),
          ("dte-panl", 1),
          ("standard", 3))
    )


_McmFrTunnelPvcType_Type.__name__ = "Integer32"
_McmFrTunnelPvcType_Object = MibTableColumn
mcmFrTunnelPvcType = _McmFrTunnelPvcType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 5),
    _McmFrTunnelPvcType_Type()
)
mcmFrTunnelPvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcType.setStatus("mandatory")


class _McmFrTunnelPvcPhysPortIfIndex_Type(Integer32):
    """Custom type mcmFrTunnelPvcPhysPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrTunnelPvcPhysPortIfIndex_Type.__name__ = "Integer32"
_McmFrTunnelPvcPhysPortIfIndex_Object = MibTableColumn
mcmFrTunnelPvcPhysPortIfIndex = _McmFrTunnelPvcPhysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 6),
    _McmFrTunnelPvcPhysPortIfIndex_Type()
)
mcmFrTunnelPvcPhysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcPhysPortIfIndex.setStatus("mandatory")


class _McmFrTunnelPvcMaxRxFrameSize_Type(Integer32):
    """Custom type mcmFrTunnelPvcMaxRxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_McmFrTunnelPvcMaxRxFrameSize_Type.__name__ = "Integer32"
_McmFrTunnelPvcMaxRxFrameSize_Object = MibTableColumn
mcmFrTunnelPvcMaxRxFrameSize = _McmFrTunnelPvcMaxRxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 7),
    _McmFrTunnelPvcMaxRxFrameSize_Type()
)
mcmFrTunnelPvcMaxRxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcMaxRxFrameSize.setStatus("mandatory")


class _McmFrTunnelPvcRxBc_Type(Integer32):
    """Custom type mcmFrTunnelPvcRxBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrTunnelPvcRxBc_Type.__name__ = "Integer32"
_McmFrTunnelPvcRxBc_Object = MibTableColumn
mcmFrTunnelPvcRxBc = _McmFrTunnelPvcRxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 8),
    _McmFrTunnelPvcRxBc_Type()
)
mcmFrTunnelPvcRxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxBc.setStatus("mandatory")


class _McmFrTunnelPvcRxBe_Type(Integer32):
    """Custom type mcmFrTunnelPvcRxBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrTunnelPvcRxBe_Type.__name__ = "Integer32"
_McmFrTunnelPvcRxBe_Object = MibTableColumn
mcmFrTunnelPvcRxBe = _McmFrTunnelPvcRxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 9),
    _McmFrTunnelPvcRxBe_Type()
)
mcmFrTunnelPvcRxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxBe.setStatus("mandatory")


class _McmFrTunnelPvcMaxRxCIR_Type(Integer32):
    """Custom type mcmFrTunnelPvcMaxRxCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_McmFrTunnelPvcMaxRxCIR_Type.__name__ = "Integer32"
_McmFrTunnelPvcMaxRxCIR_Object = MibTableColumn
mcmFrTunnelPvcMaxRxCIR = _McmFrTunnelPvcMaxRxCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 10),
    _McmFrTunnelPvcMaxRxCIR_Type()
)
mcmFrTunnelPvcMaxRxCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcMaxRxCIR.setStatus("mandatory")


class _McmFrTunnelPvcMaxTxFrameSize_Type(Integer32):
    """Custom type mcmFrTunnelPvcMaxTxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_McmFrTunnelPvcMaxTxFrameSize_Type.__name__ = "Integer32"
_McmFrTunnelPvcMaxTxFrameSize_Object = MibTableColumn
mcmFrTunnelPvcMaxTxFrameSize = _McmFrTunnelPvcMaxTxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 11),
    _McmFrTunnelPvcMaxTxFrameSize_Type()
)
mcmFrTunnelPvcMaxTxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcMaxTxFrameSize.setStatus("mandatory")


class _McmFrTunnelPvcTxBc_Type(Integer32):
    """Custom type mcmFrTunnelPvcTxBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrTunnelPvcTxBc_Type.__name__ = "Integer32"
_McmFrTunnelPvcTxBc_Object = MibTableColumn
mcmFrTunnelPvcTxBc = _McmFrTunnelPvcTxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 12),
    _McmFrTunnelPvcTxBc_Type()
)
mcmFrTunnelPvcTxBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcTxBc.setStatus("mandatory")


class _McmFrTunnelPvcTxBe_Type(Integer32):
    """Custom type mcmFrTunnelPvcTxBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrTunnelPvcTxBe_Type.__name__ = "Integer32"
_McmFrTunnelPvcTxBe_Object = MibTableColumn
mcmFrTunnelPvcTxBe = _McmFrTunnelPvcTxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 13),
    _McmFrTunnelPvcTxBe_Type()
)
mcmFrTunnelPvcTxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcTxBe.setStatus("mandatory")


class _McmFrTunnelPvcMaxTxCIR_Type(Integer32):
    """Custom type mcmFrTunnelPvcMaxTxCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_McmFrTunnelPvcMaxTxCIR_Type.__name__ = "Integer32"
_McmFrTunnelPvcMaxTxCIR_Object = MibTableColumn
mcmFrTunnelPvcMaxTxCIR = _McmFrTunnelPvcMaxTxCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 14),
    _McmFrTunnelPvcMaxTxCIR_Type()
)
mcmFrTunnelPvcMaxTxCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcMaxTxCIR.setStatus("mandatory")


class _McmFrTunnelPvcState_Type(Integer32):
    """Custom type mcmFrTunnelPvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_McmFrTunnelPvcState_Type.__name__ = "Integer32"
_McmFrTunnelPvcState_Object = MibTableColumn
mcmFrTunnelPvcState = _McmFrTunnelPvcState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 15),
    _McmFrTunnelPvcState_Type()
)
mcmFrTunnelPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcState.setStatus("mandatory")
_McmFrTunnelPvcRxFrames_Type = Counter32
_McmFrTunnelPvcRxFrames_Object = MibTableColumn
mcmFrTunnelPvcRxFrames = _McmFrTunnelPvcRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 16),
    _McmFrTunnelPvcRxFrames_Type()
)
mcmFrTunnelPvcRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxFrames.setStatus("mandatory")
_McmFrTunnelPvcTxFrames_Type = Counter32
_McmFrTunnelPvcTxFrames_Object = MibTableColumn
mcmFrTunnelPvcTxFrames = _McmFrTunnelPvcTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 17),
    _McmFrTunnelPvcTxFrames_Type()
)
mcmFrTunnelPvcTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcTxFrames.setStatus("mandatory")
_McmFrTunnelPvcRxDeFrames_Type = Counter32
_McmFrTunnelPvcRxDeFrames_Object = MibTableColumn
mcmFrTunnelPvcRxDeFrames = _McmFrTunnelPvcRxDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 18),
    _McmFrTunnelPvcRxDeFrames_Type()
)
mcmFrTunnelPvcRxDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxDeFrames.setStatus("mandatory")
_McmFrTunnelPvcRxExcessFrames_Type = Counter32
_McmFrTunnelPvcRxExcessFrames_Object = MibTableColumn
mcmFrTunnelPvcRxExcessFrames = _McmFrTunnelPvcRxExcessFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 19),
    _McmFrTunnelPvcRxExcessFrames_Type()
)
mcmFrTunnelPvcRxExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxExcessFrames.setStatus("mandatory")
_McmFrTunnelPvcTxExcessFrames_Type = Counter32
_McmFrTunnelPvcTxExcessFrames_Object = MibTableColumn
mcmFrTunnelPvcTxExcessFrames = _McmFrTunnelPvcTxExcessFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 20),
    _McmFrTunnelPvcTxExcessFrames_Type()
)
mcmFrTunnelPvcTxExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcTxExcessFrames.setStatus("mandatory")
_McmFrTunnelPvcRxDiscards_Type = Counter32
_McmFrTunnelPvcRxDiscards_Object = MibTableColumn
mcmFrTunnelPvcRxDiscards = _McmFrTunnelPvcRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 21),
    _McmFrTunnelPvcRxDiscards_Type()
)
mcmFrTunnelPvcRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxDiscards.setStatus("mandatory")
_McmFrTunnelPvcRxOctets_Type = Counter32
_McmFrTunnelPvcRxOctets_Object = MibTableColumn
mcmFrTunnelPvcRxOctets = _McmFrTunnelPvcRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 22),
    _McmFrTunnelPvcRxOctets_Type()
)
mcmFrTunnelPvcRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcRxOctets.setStatus("mandatory")
_McmFrTunnelPvcTxOctets_Type = Counter32
_McmFrTunnelPvcTxOctets_Object = MibTableColumn
mcmFrTunnelPvcTxOctets = _McmFrTunnelPvcTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 23),
    _McmFrTunnelPvcTxOctets_Type()
)
mcmFrTunnelPvcTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcTxOctets.setStatus("mandatory")


class _McmFrTunnelPvcConsecFrames_Type(Integer32):
    """Custom type mcmFrTunnelPvcConsecFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_McmFrTunnelPvcConsecFrames_Type.__name__ = "Integer32"
_McmFrTunnelPvcConsecFrames_Object = MibTableColumn
mcmFrTunnelPvcConsecFrames = _McmFrTunnelPvcConsecFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 24),
    _McmFrTunnelPvcConsecFrames_Type()
)
mcmFrTunnelPvcConsecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcConsecFrames.setStatus("mandatory")


class _McmFrTunnelPvcMinTxCIR_Type(Integer32):
    """Custom type mcmFrTunnelPvcMinTxCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_McmFrTunnelPvcMinTxCIR_Type.__name__ = "Integer32"
_McmFrTunnelPvcMinTxCIR_Object = MibTableColumn
mcmFrTunnelPvcMinTxCIR = _McmFrTunnelPvcMinTxCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 23, 1, 25),
    _McmFrTunnelPvcMinTxCIR_Type()
)
mcmFrTunnelPvcMinTxCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrTunnelPvcMinTxCIR.setStatus("mandatory")
_NvmFrTunnelPvcTable_Object = MibTable
nvmFrTunnelPvcTable = _NvmFrTunnelPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24)
)
if mibBuilder.loadTexts:
    nvmFrTunnelPvcTable.setStatus("mandatory")
_NvmFrTunnelPvcEntry_Object = MibTableRow
nvmFrTunnelPvcEntry = _NvmFrTunnelPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1)
)
nvmFrTunnelPvcEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrTunnelPvcIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrTunnelPvcEntry.setStatus("mandatory")


class _NvmFrTunnelPvcIfIndex_Type(Integer32):
    """Custom type nvmFrTunnelPvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrTunnelPvcIfIndex_Type.__name__ = "Integer32"
_NvmFrTunnelPvcIfIndex_Object = MibTableColumn
nvmFrTunnelPvcIfIndex = _NvmFrTunnelPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 1),
    _NvmFrTunnelPvcIfIndex_Type()
)
nvmFrTunnelPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcIfIndex.setStatus("mandatory")


class _NvmFrTunnelPvcDlciNumber_Type(Integer32):
    """Custom type nvmFrTunnelPvcDlciNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NvmFrTunnelPvcDlciNumber_Type.__name__ = "Integer32"
_NvmFrTunnelPvcDlciNumber_Object = MibTableColumn
nvmFrTunnelPvcDlciNumber = _NvmFrTunnelPvcDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 2),
    _NvmFrTunnelPvcDlciNumber_Type()
)
nvmFrTunnelPvcDlciNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcDlciNumber.setStatus("mandatory")


class _NvmFrTunnelPvcPhysicalCard_Type(Integer32):
    """Custom type nvmFrTunnelPvcPhysicalCard based on Integer32"""
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limA", 1))
    )


_NvmFrTunnelPvcPhysicalCard_Type.__name__ = "Integer32"
_NvmFrTunnelPvcPhysicalCard_Object = MibTableColumn
nvmFrTunnelPvcPhysicalCard = _NvmFrTunnelPvcPhysicalCard_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 3),
    _NvmFrTunnelPvcPhysicalCard_Type()
)
nvmFrTunnelPvcPhysicalCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcPhysicalCard.setStatus("mandatory")


class _NvmFrTunnelPvcPhysicalPort_Type(Integer32):
    """Custom type nvmFrTunnelPvcPhysicalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NvmFrTunnelPvcPhysicalPort_Type.__name__ = "Integer32"
_NvmFrTunnelPvcPhysicalPort_Object = MibTableColumn
nvmFrTunnelPvcPhysicalPort = _NvmFrTunnelPvcPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 4),
    _NvmFrTunnelPvcPhysicalPort_Type()
)
nvmFrTunnelPvcPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcPhysicalPort.setStatus("mandatory")


class _NvmFrTunnelPvcType_Type(Integer32):
    """Custom type nvmFrTunnelPvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce-panl", 2),
          ("dte-panl", 1),
          ("standard", 3))
    )


_NvmFrTunnelPvcType_Type.__name__ = "Integer32"
_NvmFrTunnelPvcType_Object = MibTableColumn
nvmFrTunnelPvcType = _NvmFrTunnelPvcType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 5),
    _NvmFrTunnelPvcType_Type()
)
nvmFrTunnelPvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcType.setStatus("mandatory")


class _NvmFrTunnelPvcPhysPortIfIndex_Type(Integer32):
    """Custom type nvmFrTunnelPvcPhysPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrTunnelPvcPhysPortIfIndex_Type.__name__ = "Integer32"
_NvmFrTunnelPvcPhysPortIfIndex_Object = MibTableColumn
nvmFrTunnelPvcPhysPortIfIndex = _NvmFrTunnelPvcPhysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 6),
    _NvmFrTunnelPvcPhysPortIfIndex_Type()
)
nvmFrTunnelPvcPhysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcPhysPortIfIndex.setStatus("mandatory")


class _NvmFrTunnelPvcMaxRxFrameSize_Type(Integer32):
    """Custom type nvmFrTunnelPvcMaxRxFrameSize based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NvmFrTunnelPvcMaxRxFrameSize_Type.__name__ = "Integer32"
_NvmFrTunnelPvcMaxRxFrameSize_Object = MibTableColumn
nvmFrTunnelPvcMaxRxFrameSize = _NvmFrTunnelPvcMaxRxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 7),
    _NvmFrTunnelPvcMaxRxFrameSize_Type()
)
nvmFrTunnelPvcMaxRxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcMaxRxFrameSize.setStatus("mandatory")


class _NvmFrTunnelPvcRxBc_Type(Integer32):
    """Custom type nvmFrTunnelPvcRxBc based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrTunnelPvcRxBc_Type.__name__ = "Integer32"
_NvmFrTunnelPvcRxBc_Object = MibTableColumn
nvmFrTunnelPvcRxBc = _NvmFrTunnelPvcRxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 8),
    _NvmFrTunnelPvcRxBc_Type()
)
nvmFrTunnelPvcRxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcRxBc.setStatus("mandatory")


class _NvmFrTunnelPvcRxBe_Type(Integer32):
    """Custom type nvmFrTunnelPvcRxBe based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrTunnelPvcRxBe_Type.__name__ = "Integer32"
_NvmFrTunnelPvcRxBe_Object = MibTableColumn
nvmFrTunnelPvcRxBe = _NvmFrTunnelPvcRxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 9),
    _NvmFrTunnelPvcRxBe_Type()
)
nvmFrTunnelPvcRxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcRxBe.setStatus("mandatory")


class _NvmFrTunnelPvcMaxRxCIR_Type(Integer32):
    """Custom type nvmFrTunnelPvcMaxRxCIR based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_NvmFrTunnelPvcMaxRxCIR_Type.__name__ = "Integer32"
_NvmFrTunnelPvcMaxRxCIR_Object = MibTableColumn
nvmFrTunnelPvcMaxRxCIR = _NvmFrTunnelPvcMaxRxCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 10),
    _NvmFrTunnelPvcMaxRxCIR_Type()
)
nvmFrTunnelPvcMaxRxCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcMaxRxCIR.setStatus("mandatory")


class _NvmFrTunnelPvcMaxTxFrameSize_Type(Integer32):
    """Custom type nvmFrTunnelPvcMaxTxFrameSize based on Integer32"""
    defaultValue = 1604

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NvmFrTunnelPvcMaxTxFrameSize_Type.__name__ = "Integer32"
_NvmFrTunnelPvcMaxTxFrameSize_Object = MibTableColumn
nvmFrTunnelPvcMaxTxFrameSize = _NvmFrTunnelPvcMaxTxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 11),
    _NvmFrTunnelPvcMaxTxFrameSize_Type()
)
nvmFrTunnelPvcMaxTxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcMaxTxFrameSize.setStatus("mandatory")


class _NvmFrTunnelPvcTxBc_Type(Integer32):
    """Custom type nvmFrTunnelPvcTxBc based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrTunnelPvcTxBc_Type.__name__ = "Integer32"
_NvmFrTunnelPvcTxBc_Object = MibTableColumn
nvmFrTunnelPvcTxBc = _NvmFrTunnelPvcTxBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 12),
    _NvmFrTunnelPvcTxBc_Type()
)
nvmFrTunnelPvcTxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcTxBc.setStatus("mandatory")


class _NvmFrTunnelPvcTxBe_Type(Integer32):
    """Custom type nvmFrTunnelPvcTxBe based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrTunnelPvcTxBe_Type.__name__ = "Integer32"
_NvmFrTunnelPvcTxBe_Object = MibTableColumn
nvmFrTunnelPvcTxBe = _NvmFrTunnelPvcTxBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 13),
    _NvmFrTunnelPvcTxBe_Type()
)
nvmFrTunnelPvcTxBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcTxBe.setStatus("mandatory")


class _NvmFrTunnelPvcMaxTxCIR_Type(Integer32):
    """Custom type nvmFrTunnelPvcMaxTxCIR based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_NvmFrTunnelPvcMaxTxCIR_Type.__name__ = "Integer32"
_NvmFrTunnelPvcMaxTxCIR_Object = MibTableColumn
nvmFrTunnelPvcMaxTxCIR = _NvmFrTunnelPvcMaxTxCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 14),
    _NvmFrTunnelPvcMaxTxCIR_Type()
)
nvmFrTunnelPvcMaxTxCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcMaxTxCIR.setStatus("mandatory")


class _NvmFrTunnelPvcRowStatus_Type(Integer32):
    """Custom type nvmFrTunnelPvcRowStatus based on Integer32"""
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


_NvmFrTunnelPvcRowStatus_Type.__name__ = "Integer32"
_NvmFrTunnelPvcRowStatus_Object = MibTableColumn
nvmFrTunnelPvcRowStatus = _NvmFrTunnelPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 15),
    _NvmFrTunnelPvcRowStatus_Type()
)
nvmFrTunnelPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcRowStatus.setStatus("mandatory")


class _NvmFrTunnelPvcConsecFrames_Type(Integer32):
    """Custom type nvmFrTunnelPvcConsecFrames based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NvmFrTunnelPvcConsecFrames_Type.__name__ = "Integer32"
_NvmFrTunnelPvcConsecFrames_Object = MibTableColumn
nvmFrTunnelPvcConsecFrames = _NvmFrTunnelPvcConsecFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 16),
    _NvmFrTunnelPvcConsecFrames_Type()
)
nvmFrTunnelPvcConsecFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcConsecFrames.setStatus("mandatory")


class _NvmFrTunnelPvcMinTxCIR_Type(Integer32):
    """Custom type nvmFrTunnelPvcMinTxCIR based on Integer32"""
    defaultValue = 64000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256000),
    )


_NvmFrTunnelPvcMinTxCIR_Type.__name__ = "Integer32"
_NvmFrTunnelPvcMinTxCIR_Object = MibTableColumn
nvmFrTunnelPvcMinTxCIR = _NvmFrTunnelPvcMinTxCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 24, 1, 17),
    _NvmFrTunnelPvcMinTxCIR_Type()
)
nvmFrTunnelPvcMinTxCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrTunnelPvcMinTxCIR.setStatus("mandatory")
_McmFrNetlinkMapTable_Object = MibTable
mcmFrNetlinkMapTable = _McmFrNetlinkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 25)
)
if mibBuilder.loadTexts:
    mcmFrNetlinkMapTable.setStatus("mandatory")
_McmFrNetlinkMapEntry_Object = MibTableRow
mcmFrNetlinkMapEntry = _McmFrNetlinkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 25, 1)
)
mcmFrNetlinkMapEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrNetlinkMapVPIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrNetlinkMapNetlinkIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrNetlinkMapEntry.setStatus("mandatory")


class _McmFrNetlinkMapVPIfIndex_Type(Integer32):
    """Custom type mcmFrNetlinkMapVPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrNetlinkMapVPIfIndex_Type.__name__ = "Integer32"
_McmFrNetlinkMapVPIfIndex_Object = MibTableColumn
mcmFrNetlinkMapVPIfIndex = _McmFrNetlinkMapVPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 25, 1, 1),
    _McmFrNetlinkMapVPIfIndex_Type()
)
mcmFrNetlinkMapVPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrNetlinkMapVPIfIndex.setStatus("mandatory")


class _McmFrNetlinkMapNetlinkIfIndex_Type(Integer32):
    """Custom type mcmFrNetlinkMapNetlinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrNetlinkMapNetlinkIfIndex_Type.__name__ = "Integer32"
_McmFrNetlinkMapNetlinkIfIndex_Object = MibTableColumn
mcmFrNetlinkMapNetlinkIfIndex = _McmFrNetlinkMapNetlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 25, 1, 2),
    _McmFrNetlinkMapNetlinkIfIndex_Type()
)
mcmFrNetlinkMapNetlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrNetlinkMapNetlinkIfIndex.setStatus("mandatory")


class _McmFrNetlinkMapOperStatus_Type(Integer32):
    """Custom type mcmFrNetlinkMapOperStatus based on Integer32"""
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


_McmFrNetlinkMapOperStatus_Type.__name__ = "Integer32"
_McmFrNetlinkMapOperStatus_Object = MibTableColumn
mcmFrNetlinkMapOperStatus = _McmFrNetlinkMapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 25, 1, 3),
    _McmFrNetlinkMapOperStatus_Type()
)
mcmFrNetlinkMapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrNetlinkMapOperStatus.setStatus("mandatory")
_NvmFrNetlinkMapTable_Object = MibTable
nvmFrNetlinkMapTable = _NvmFrNetlinkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 26)
)
if mibBuilder.loadTexts:
    nvmFrNetlinkMapTable.setStatus("mandatory")
_NvmFrNetlinkMapEntry_Object = MibTableRow
nvmFrNetlinkMapEntry = _NvmFrNetlinkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 26, 1)
)
nvmFrNetlinkMapEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrNetlinkMapVPIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "nvmFrNetlinkMapNetlinkIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrNetlinkMapEntry.setStatus("mandatory")


class _NvmFrNetlinkMapVPIfIndex_Type(Integer32):
    """Custom type nvmFrNetlinkMapVPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrNetlinkMapVPIfIndex_Type.__name__ = "Integer32"
_NvmFrNetlinkMapVPIfIndex_Object = MibTableColumn
nvmFrNetlinkMapVPIfIndex = _NvmFrNetlinkMapVPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 26, 1, 1),
    _NvmFrNetlinkMapVPIfIndex_Type()
)
nvmFrNetlinkMapVPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrNetlinkMapVPIfIndex.setStatus("mandatory")


class _NvmFrNetlinkMapNetlinkIfIndex_Type(Integer32):
    """Custom type nvmFrNetlinkMapNetlinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrNetlinkMapNetlinkIfIndex_Type.__name__ = "Integer32"
_NvmFrNetlinkMapNetlinkIfIndex_Object = MibTableColumn
nvmFrNetlinkMapNetlinkIfIndex = _NvmFrNetlinkMapNetlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 26, 1, 2),
    _NvmFrNetlinkMapNetlinkIfIndex_Type()
)
nvmFrNetlinkMapNetlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrNetlinkMapNetlinkIfIndex.setStatus("mandatory")


class _NvmFrNetlinkMapRowStatus_Type(Integer32):
    """Custom type nvmFrNetlinkMapRowStatus based on Integer32"""
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


_NvmFrNetlinkMapRowStatus_Type.__name__ = "Integer32"
_NvmFrNetlinkMapRowStatus_Object = MibTableColumn
nvmFrNetlinkMapRowStatus = _NvmFrNetlinkMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 1, 26, 1, 3),
    _NvmFrNetlinkMapRowStatus_Type()
)
nvmFrNetlinkMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrNetlinkMapRowStatus.setStatus("mandatory")
_Fr_control_ObjectIdentity = ObjectIdentity
fr_control = _Fr_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2)
)
_McmFrPhyPortCntrTable_Object = MibTable
mcmFrPhyPortCntrTable = _McmFrPhyPortCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mcmFrPhyPortCntrTable.setStatus("obsolete")
_McmFrPhyPortCntrEntry_Object = MibTableRow
mcmFrPhyPortCntrEntry = _McmFrPhyPortCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 1, 1)
)
mcmFrPhyPortCntrEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPhyPortCntrIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrPhyPortCntrEntry.setStatus("obsolete")
_McmFrPhyPortCntrIfIndex_Type = Integer32
_McmFrPhyPortCntrIfIndex_Object = MibTableColumn
mcmFrPhyPortCntrIfIndex = _McmFrPhyPortCntrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 1, 1, 1),
    _McmFrPhyPortCntrIfIndex_Type()
)
mcmFrPhyPortCntrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrPhyPortCntrIfIndex.setStatus("obsolete")


class _McmFrPhyPortCntrAction_Type(Integer32):
    """Custom type mcmFrPhyPortCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmFrPhyPortCntrAction_Type.__name__ = "Integer32"
_McmFrPhyPortCntrAction_Object = MibTableColumn
mcmFrPhyPortCntrAction = _McmFrPhyPortCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 1, 1, 2),
    _McmFrPhyPortCntrAction_Type()
)
mcmFrPhyPortCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrPhyPortCntrAction.setStatus("obsolete")
_McmFrVirtualPortCntrTable_Object = MibTable
mcmFrVirtualPortCntrTable = _McmFrVirtualPortCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 2)
)
if mibBuilder.loadTexts:
    mcmFrVirtualPortCntrTable.setStatus("obsolete")
_McmFrVirtualPortCntrEntry_Object = MibTableRow
mcmFrVirtualPortCntrEntry = _McmFrVirtualPortCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 2, 1)
)
mcmFrVirtualPortCntrEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrVirtualPortCntrIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrVirtualPortCntrEntry.setStatus("obsolete")
_McmFrVirtualPortCntrIfIndex_Type = Integer32
_McmFrVirtualPortCntrIfIndex_Object = MibTableColumn
mcmFrVirtualPortCntrIfIndex = _McmFrVirtualPortCntrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 2, 1, 1),
    _McmFrVirtualPortCntrIfIndex_Type()
)
mcmFrVirtualPortCntrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrVirtualPortCntrIfIndex.setStatus("obsolete")


class _McmFrVirtualPortCntrAction_Type(Integer32):
    """Custom type mcmFrVirtualPortCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmFrVirtualPortCntrAction_Type.__name__ = "Integer32"
_McmFrVirtualPortCntrAction_Object = MibTableColumn
mcmFrVirtualPortCntrAction = _McmFrVirtualPortCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 2, 1, 2),
    _McmFrVirtualPortCntrAction_Type()
)
mcmFrVirtualPortCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrVirtualPortCntrAction.setStatus("obsolete")
_McmFrPVCCntrTable_Object = MibTable
mcmFrPVCCntrTable = _McmFrPVCCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 3)
)
if mibBuilder.loadTexts:
    mcmFrPVCCntrTable.setStatus("obsolete")
_McmFrPVCCntrEntry_Object = MibTableRow
mcmFrPVCCntrEntry = _McmFrPVCCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 3, 1)
)
mcmFrPVCCntrEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPVCCntrIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrPVCCntrDLCI"),
)
if mibBuilder.loadTexts:
    mcmFrPVCCntrEntry.setStatus("obsolete")
_McmFrPVCCntrIfIndex_Type = Integer32
_McmFrPVCCntrIfIndex_Object = MibTableColumn
mcmFrPVCCntrIfIndex = _McmFrPVCCntrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 3, 1, 1),
    _McmFrPVCCntrIfIndex_Type()
)
mcmFrPVCCntrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrPVCCntrIfIndex.setStatus("obsolete")


class _McmFrPVCCntrDLCI_Type(Integer32):
    """Custom type mcmFrPVCCntrDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 126975),
    )


_McmFrPVCCntrDLCI_Type.__name__ = "Integer32"
_McmFrPVCCntrDLCI_Object = MibTableColumn
mcmFrPVCCntrDLCI = _McmFrPVCCntrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 3, 1, 2),
    _McmFrPVCCntrDLCI_Type()
)
mcmFrPVCCntrDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrPVCCntrDLCI.setStatus("obsolete")


class _McmFrPVCCntrAction_Type(Integer32):
    """Custom type mcmFrPVCCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmFrPVCCntrAction_Type.__name__ = "Integer32"
_McmFrPVCCntrAction_Object = MibTableColumn
mcmFrPVCCntrAction = _McmFrPVCCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 3, 1, 3),
    _McmFrPVCCntrAction_Type()
)
mcmFrPVCCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrPVCCntrAction.setStatus("obsolete")
_McmFrSVCCntrTable_Object = MibTable
mcmFrSVCCntrTable = _McmFrSVCCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 4)
)
if mibBuilder.loadTexts:
    mcmFrSVCCntrTable.setStatus("obsolete")
_McmFrSVCCntrEntry_Object = MibTableRow
mcmFrSVCCntrEntry = _McmFrSVCCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 4, 1)
)
mcmFrSVCCntrEntry.setIndexNames(
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCCntrIfIndex"),
    (0, "MICOM-FRAMERELAY-MIB", "mcmFrSVCCntrDNA"),
)
if mibBuilder.loadTexts:
    mcmFrSVCCntrEntry.setStatus("obsolete")
_McmFrSVCCntrIfIndex_Type = Integer32
_McmFrSVCCntrIfIndex_Object = MibTableColumn
mcmFrSVCCntrIfIndex = _McmFrSVCCntrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 4, 1, 1),
    _McmFrSVCCntrIfIndex_Type()
)
mcmFrSVCCntrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrSVCCntrIfIndex.setStatus("obsolete")


class _McmFrSVCCntrDNA_Type(OctetString):
    """Custom type mcmFrSVCCntrDNA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 30),
    )


_McmFrSVCCntrDNA_Type.__name__ = "OctetString"
_McmFrSVCCntrDNA_Object = MibTableColumn
mcmFrSVCCntrDNA = _McmFrSVCCntrDNA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 4, 1, 2),
    _McmFrSVCCntrDNA_Type()
)
mcmFrSVCCntrDNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmFrSVCCntrDNA.setStatus("obsolete")


class _McmFrSVCCntrAction_Type(Integer32):
    """Custom type mcmFrSVCCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_McmFrSVCCntrAction_Type.__name__ = "Integer32"
_McmFrSVCCntrAction_Object = MibTableColumn
mcmFrSVCCntrAction = _McmFrSVCCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 2, 4, 1, 3),
    _McmFrSVCCntrAction_Type()
)
mcmFrSVCCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrSVCCntrAction.setStatus("obsolete")

# Managed Objects groups


# Notification objects

mcmFrWanLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 0, 1)
)
mcmFrWanLinkUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-SYS-MIB", "mcmSysIfExtModule"),
        ("MICOM-SYS-MIB", "mcmSysIfExtPPA"))
)
if mibBuilder.loadTexts:
    mcmFrWanLinkUp.setStatus(
        ""
    )

mcmFrWanLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 7, 0, 2)
)
mcmFrWanLinkDown.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-SYS-MIB", "mcmSysIfExtModule"),
        ("MICOM-SYS-MIB", "mcmSysIfExtPPA"))
)
if mibBuilder.loadTexts:
    mcmFrWanLinkDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-FRAMERELAY-MIB",
    **{"Index": Index,
       "micom-frame-relay": micom_frame_relay,
       "mcmFrWanLinkUp": mcmFrWanLinkUp,
       "mcmFrWanLinkDown": mcmFrWanLinkDown,
       "fr-configuration": fr_configuration,
       "mcmFrGlobalGroup": mcmFrGlobalGroup,
       "mcmFrMaxDLCI": mcmFrMaxDLCI,
       "mcmFrMaxVirtualPorts": mcmFrMaxVirtualPorts,
       "mcmFrMaxDlciPerLine": mcmFrMaxDlciPerLine,
       "mcmFrConnectTime": mcmFrConnectTime,
       "mcmFrOctetsSent": mcmFrOctetsSent,
       "mcmFrOctetsReceived": mcmFrOctetsReceived,
       "mcmFrFramesSent": mcmFrFramesSent,
       "mcmFrFramesReceived": mcmFrFramesReceived,
       "mcmFrGlobalGroupCntrAction": mcmFrGlobalGroupCntrAction,
       "mcmFrDNANumberingPlan": mcmFrDNANumberingPlan,
       "mcmFrActivePanlDlciSVCs": mcmFrActivePanlDlciSVCs,
       "mcmFrTotalTunnelingPVCs": mcmFrTotalTunnelingPVCs,
       "mcmFrActiveTunnelingPVCs": mcmFrActiveTunnelingPVCs,
       "mcmFrPanlLmiTrapEnable": mcmFrPanlLmiTrapEnable,
       "mcmFrMsmTrapEnable": mcmFrMsmTrapEnable,
       "mcmFrCoreTrapEnable": mcmFrCoreTrapEnable,
       "mcmFrPlmTrapEnable": mcmFrPlmTrapEnable,
       "mcmFrPhyPortTable": mcmFrPhyPortTable,
       "mcmFrPhyPortEntry": mcmFrPhyPortEntry,
       "mcmFrPhyPortExtIfIndex": mcmFrPhyPortExtIfIndex,
       "mcmFrPhyPortFlowControl": mcmFrPhyPortFlowControl,
       "mcmFrPhyPortThroughput": mcmFrPhyPortThroughput,
       "mcmFrPhyPortDelta": mcmFrPhyPortDelta,
       "mcmFrPhyPortConsectiveFrames": mcmFrPhyPortConsectiveFrames,
       "mcmFrPhyPortMtuSize": mcmFrPhyPortMtuSize,
       "mcmFrPhyPortConnectTime": mcmFrPhyPortConnectTime,
       "mcmFrPhyPortLMISent": mcmFrPhyPortLMISent,
       "mcmFrPhyPortLMIReceived": mcmFrPhyPortLMIReceived,
       "mcmFrPhyPortXIDSent": mcmFrPhyPortXIDSent,
       "mcmFrPhyPortXIDReceived": mcmFrPhyPortXIDReceived,
       "mcmFrPhyPortCLLMSent": mcmFrPhyPortCLLMSent,
       "mcmFrPhyPortCLLMReceived": mcmFrPhyPortCLLMReceived,
       "mcmFrPhyPortHeaderErrors": mcmFrPhyPortHeaderErrors,
       "mcmFrPhyPortInvalidDLCI": mcmFrPhyPortInvalidDLCI,
       "mcmFrPhyPortShortFrames": mcmFrPhyPortShortFrames,
       "mcmFrPhyPortLongFrames": mcmFrPhyPortLongFrames,
       "mcmFrPhyPortIgnoredFrames": mcmFrPhyPortIgnoredFrames,
       "mcmFrPhyPortXIDExpirations": mcmFrPhyPortXIDExpirations,
       "mcmFrPhyPortTxExpirations": mcmFrPhyPortTxExpirations,
       "mcmFrPhyPortPVCLMIStatus": mcmFrPhyPortPVCLMIStatus,
       "mcmFrPhyPortSVCLMIStatus": mcmFrPhyPortSVCLMIStatus,
       "mcmFrPhyPortActivePanlDlciSVCs": mcmFrPhyPortActivePanlDlciSVCs,
       "mcmFrPhyPortRxDataFrames": mcmFrPhyPortRxDataFrames,
       "mcmFrPhyPortTxDataFrames": mcmFrPhyPortTxDataFrames,
       "mcmFrPhyPortRxActivations": mcmFrPhyPortRxActivations,
       "mcmFrPhyPortRxDeactivations": mcmFrPhyPortRxDeactivations,
       "mcmFrPhyPortRxOkAcks": mcmFrPhyPortRxOkAcks,
       "mcmFrPhyPortRxErrAcks": mcmFrPhyPortRxErrAcks,
       "mcmFrPhyPortRxUnknowns": mcmFrPhyPortRxUnknowns,
       "mcmFrPhyPortRxErrors": mcmFrPhyPortRxErrors,
       "mcmFrPhyPortRxOctets": mcmFrPhyPortRxOctets,
       "mcmFrPhyPortTxOctets": mcmFrPhyPortTxOctets,
       "mcmFrPhyPortTxThroughput": mcmFrPhyPortTxThroughput,
       "mcmFrPhyPortRxThroughput": mcmFrPhyPortRxThroughput,
       "mcmFrPhyPortTxMaxFrameSize": mcmFrPhyPortTxMaxFrameSize,
       "mcmFrPhyPortRxMaxFrameSize": mcmFrPhyPortRxMaxFrameSize,
       "mcmFrPhyPortRateEnf": mcmFrPhyPortRateEnf,
       "mcmFrPhyPortTxBc": mcmFrPhyPortTxBc,
       "mcmFrPhyPortRxBc": mcmFrPhyPortRxBc,
       "mcmFrPhyPortTxBe": mcmFrPhyPortTxBe,
       "mcmFrPhyPortRxBe": mcmFrPhyPortRxBe,
       "mcmFrPhyPortDataFrames": mcmFrPhyPortDataFrames,
       "mcmFrPVCPhyTable": mcmFrPVCPhyTable,
       "mcmFrPVCPhyEntry": mcmFrPVCPhyEntry,
       "mcmFrPVCPhyIfIndex": mcmFrPVCPhyIfIndex,
       "mcmFrPVCLMIMode": mcmFrPVCLMIMode,
       "mcmFrPVCBiDir": mcmFrPVCBiDir,
       "mcmFrSVCPhyTable": mcmFrSVCPhyTable,
       "mcmFrSVCPhyEntry": mcmFrSVCPhyEntry,
       "mcmFrSVCPhyIfIndex": mcmFrSVCPhyIfIndex,
       "mcmFrSVCState": mcmFrSVCState,
       "mcmFrSVCT303": mcmFrSVCT303,
       "mcmFrSVCT305": mcmFrSVCT305,
       "mcmFrSVCT308": mcmFrSVCT308,
       "mcmFrSVCT310": mcmFrSVCT310,
       "mcmFrSVCMaxCalls": mcmFrSVCMaxCalls,
       "mcmFrSVCMaxTxSize": mcmFrSVCMaxTxSize,
       "mcmFrSVCMaxRxSize": mcmFrSVCMaxRxSize,
       "mcmFrSVCMinDLCI": mcmFrSVCMinDLCI,
       "mcmFrSVCMaxDLCI": mcmFrSVCMaxDLCI,
       "mcmFrSVCMinTxThroughput": mcmFrSVCMinTxThroughput,
       "mcmFrSVCMinRxThroughput": mcmFrSVCMinRxThroughput,
       "mcmFrSVCMaxTxThroughput": mcmFrSVCMaxTxThroughput,
       "mcmFrSVCMaxRxThroughput": mcmFrSVCMaxRxThroughput,
       "mcmFrSVCTxBurstSize": mcmFrSVCTxBurstSize,
       "mcmFrSVCRxBurstSize": mcmFrSVCRxBurstSize,
       "mcmFrSVCExcessTxBurstSize": mcmFrSVCExcessTxBurstSize,
       "mcmFrSVCExcessRxBurstSize": mcmFrSVCExcessRxBurstSize,
       "mcmFrVirtualPortTable": mcmFrVirtualPortTable,
       "mcmFrVirtualPortEntry": mcmFrVirtualPortEntry,
       "mcmFrVirtualPortIfIndex": mcmFrVirtualPortIfIndex,
       "mcmFrVirtualPortPhyPortIfIndex": mcmFrVirtualPortPhyPortIfIndex,
       "mcmFrVirtualPortPPA": mcmFrVirtualPortPPA,
       "mcmFrVirtualPortMode": mcmFrVirtualPortMode,
       "mcmFrVirtualPortState": mcmFrVirtualPortState,
       "mcmFrVirtualPortEntryStatus": mcmFrVirtualPortEntryStatus,
       "mcmFrVirtualPortProtocolBinding": mcmFrVirtualPortProtocolBinding,
       "mcmFrVirtualPortNumber": mcmFrVirtualPortNumber,
       "mcmFrSVCMapTable": mcmFrSVCMapTable,
       "mcmFrSVCMapEntry": mcmFrSVCMapEntry,
       "mcmFrSVCMapVirtualPortIfIndex": mcmFrSVCMapVirtualPortIfIndex,
       "mcmFrSVCMapDNA": mcmFrSVCMapDNA,
       "mcmFrSVCMapDLCI": mcmFrSVCMapDLCI,
       "mcmFrSVCMapMaxTxSize": mcmFrSVCMapMaxTxSize,
       "mcmFrSVCMapMaxRxSize": mcmFrSVCMapMaxRxSize,
       "mcmFrSVCMapMinTxThroughput": mcmFrSVCMapMinTxThroughput,
       "mcmFrSVCMapMinRxThroughput": mcmFrSVCMapMinRxThroughput,
       "mcmFrSVCMapMaxTxThroughput": mcmFrSVCMapMaxTxThroughput,
       "mcmFrSVCMapMaxRxThroughput": mcmFrSVCMapMaxRxThroughput,
       "mcmFrSVCMapTxBurstSize": mcmFrSVCMapTxBurstSize,
       "mcmFrSVCMapRxBurstSize": mcmFrSVCMapRxBurstSize,
       "mcmFrSVCMapExcessTxBurstSize": mcmFrSVCMapExcessTxBurstSize,
       "mcmFrSVCMapExcessRxBurstSize": mcmFrSVCMapExcessRxBurstSize,
       "mcmFrSVCMapPriority": mcmFrSVCMapPriority,
       "mcmFrSVCMapEntryStatus": mcmFrSVCMapEntryStatus,
       "mcmFrSVCMapTransferPriority": mcmFrSVCMapTransferPriority,
       "mcmFrSVCMapDisableCause": mcmFrSVCMapDisableCause,
       "mcmFrSvcMapSvcIfIndex": mcmFrSvcMapSvcIfIndex,
       "mcmFrSVCMapDiscardPriority": mcmFrSVCMapDiscardPriority,
       "mcmFrSVCMapSetupPriority": mcmFrSVCMapSetupPriority,
       "mcmFrSVCMapHoldingPriority": mcmFrSVCMapHoldingPriority,
       "mcmFrPVCMapTable": mcmFrPVCMapTable,
       "mcmFrPVCMapEntry": mcmFrPVCMapEntry,
       "mcmFrPVCMapVirtualPortIfIndex": mcmFrPVCMapVirtualPortIfIndex,
       "mcmFrPVCMapDLCI": mcmFrPVCMapDLCI,
       "mcmFrPVCMapState": mcmFrPVCMapState,
       "mcmFrPVCMapEntryStatus": mcmFrPVCMapEntryStatus,
       "mcmFrPVCMapPhysIfIndex": mcmFrPVCMapPhysIfIndex,
       "mcmFrSVCCircuitTable": mcmFrSVCCircuitTable,
       "mcmFrSVCCircuitEntry": mcmFrSVCCircuitEntry,
       "mcmFrSVCCircuitIfIndex": mcmFrSVCCircuitIfIndex,
       "mcmFrSVCCircuitDNA": mcmFrSVCCircuitDNA,
       "mcmFrSVCCircuitDlci": mcmFrSVCCircuitDlci,
       "mcmFrSVCCircuitState": mcmFrSVCCircuitState,
       "mcmFrSVCCircuitReceivedFECNs": mcmFrSVCCircuitReceivedFECNs,
       "mcmFrSVCCircuitReceivedBECNs": mcmFrSVCCircuitReceivedBECNs,
       "mcmFrSVCCircuitSentFrames": mcmFrSVCCircuitSentFrames,
       "mcmFrSVCCircuitSentOctets": mcmFrSVCCircuitSentOctets,
       "mcmFrSVCCircuitReceivedFrames": mcmFrSVCCircuitReceivedFrames,
       "mcmFrSVCCircuitReceivedOctets": mcmFrSVCCircuitReceivedOctets,
       "mcmFrSVCCircuitCreationTime": mcmFrSVCCircuitCreationTime,
       "mcmFrSVCCircuitCallOriginator": mcmFrSVCCircuitCallOriginator,
       "mcmFrSVCCircuitLastTimeChange": mcmFrSVCCircuitLastTimeChange,
       "mcmFrSVCCircuitCommittedBurst": mcmFrSVCCircuitCommittedBurst,
       "mcmFrSVCCircuitExcessBurst": mcmFrSVCCircuitExcessBurst,
       "mcmFrSVCCircuitThroughput": mcmFrSVCCircuitThroughput,
       "mcmFrSVCCircuitNegMaxTxSize": mcmFrSVCCircuitNegMaxTxSize,
       "mcmFrSVCCircuitNegMaxRxSize": mcmFrSVCCircuitNegMaxRxSize,
       "mcmFrSVCCircuitNegTxThroughput": mcmFrSVCCircuitNegTxThroughput,
       "mcmFrSVCCircuitNegRxThroughput": mcmFrSVCCircuitNegRxThroughput,
       "mcmFrSVCCircuitNegTxBurst": mcmFrSVCCircuitNegTxBurst,
       "mcmFrSVCCircuitNegRxBurst": mcmFrSVCCircuitNegRxBurst,
       "mcmFrSVCCircuitNegTxExcess": mcmFrSVCCircuitNegTxExcess,
       "mcmFrSVCCircuitNegRxExcess": mcmFrSVCCircuitNegRxExcess,
       "mcmFrSVCCircuitTxDiscardCIRPolice": mcmFrSVCCircuitTxDiscardCIRPolice,
       "mcmFrSVCCircuitPriority": mcmFrSVCCircuitPriority,
       "mcmFrSVCCircuitSvcIfIndex": mcmFrSVCCircuitSvcIfIndex,
       "mcmFrSVCCircuitDiscardPriority": mcmFrSVCCircuitDiscardPriority,
       "mcmFrSVCCircuitSetupPriority": mcmFrSVCCircuitSetupPriority,
       "mcmFrSVCCircuitHoldingPriority": mcmFrSVCCircuitHoldingPriority,
       "nvmFrGlobalGroup": nvmFrGlobalGroup,
       "nvmFrMaxDLCI": nvmFrMaxDLCI,
       "nvmFrMaxVirtualPorts": nvmFrMaxVirtualPorts,
       "nvmFrMaxDlciPerLine": nvmFrMaxDlciPerLine,
       "nvmFrDNANumberingPlan": nvmFrDNANumberingPlan,
       "nvmFrPanlLmiTrapEnable": nvmFrPanlLmiTrapEnable,
       "nvmFrMsmTrapEnable": nvmFrMsmTrapEnable,
       "nvmFrCoreTrapEnable": nvmFrCoreTrapEnable,
       "nvmFrPlmTrapEnable": nvmFrPlmTrapEnable,
       "nvmFrPhyPortTable": nvmFrPhyPortTable,
       "nvmFrPhyPortEntry": nvmFrPhyPortEntry,
       "nvmFrPhyPortExtIfIndex": nvmFrPhyPortExtIfIndex,
       "nvmFrPhyPortFlowControl": nvmFrPhyPortFlowControl,
       "nvmFrPhyPortThroughput": nvmFrPhyPortThroughput,
       "nvmFrPhyPortDelta": nvmFrPhyPortDelta,
       "nvmFrPhyPortConsectiveFrames": nvmFrPhyPortConsectiveFrames,
       "nvmFrPhyPortMtuSize": nvmFrPhyPortMtuSize,
       "nvmFrPhyPortTxThroughput": nvmFrPhyPortTxThroughput,
       "nvmFrPhyPortRxThroughput": nvmFrPhyPortRxThroughput,
       "nvmFrPhyPortTxMaxFrameSize": nvmFrPhyPortTxMaxFrameSize,
       "nvmFrPhyPortRxMaxFrameSize": nvmFrPhyPortRxMaxFrameSize,
       "nvmFrPhyPortRateEnf": nvmFrPhyPortRateEnf,
       "nvmFrPhyPortTxBc": nvmFrPhyPortTxBc,
       "nvmFrPhyPortRxBc": nvmFrPhyPortRxBc,
       "nvmFrPhyPortTxBe": nvmFrPhyPortTxBe,
       "nvmFrPhyPortRxBe": nvmFrPhyPortRxBe,
       "nvmFrPVCPhyTable": nvmFrPVCPhyTable,
       "nvmFrPVCPhyEntry": nvmFrPVCPhyEntry,
       "nvmFrPVCPhyIfIndex": nvmFrPVCPhyIfIndex,
       "nvmFrPVCLMIMode": nvmFrPVCLMIMode,
       "nvmFrPVCBiDir": nvmFrPVCBiDir,
       "nvmFrSVCPhyTable": nvmFrSVCPhyTable,
       "nvmFrSVCPhyEntry": nvmFrSVCPhyEntry,
       "nvmFrSVCPhyIfIndex": nvmFrSVCPhyIfIndex,
       "nvmFrSVCState": nvmFrSVCState,
       "nvmFrSVCT303": nvmFrSVCT303,
       "nvmFrSVCT305": nvmFrSVCT305,
       "nvmFrSVCT308": nvmFrSVCT308,
       "nvmFrSVCT310": nvmFrSVCT310,
       "nvmFrSVCMaxCalls": nvmFrSVCMaxCalls,
       "nvmFrSVCMaxTxSize": nvmFrSVCMaxTxSize,
       "nvmFrSVCMaxRxSize": nvmFrSVCMaxRxSize,
       "nvmFrSVCMinDLCI": nvmFrSVCMinDLCI,
       "nvmFrSVCMaxDLCI": nvmFrSVCMaxDLCI,
       "nvmFrSVCMinTxThroughput": nvmFrSVCMinTxThroughput,
       "nvmFrSVCMinRxThroughput": nvmFrSVCMinRxThroughput,
       "nvmFrSVCMaxTxThroughput": nvmFrSVCMaxTxThroughput,
       "nvmFrSVCMaxRxThroughput": nvmFrSVCMaxRxThroughput,
       "nvmFrSVCTxBurstSize": nvmFrSVCTxBurstSize,
       "nvmFrSVCRxBurstSize": nvmFrSVCRxBurstSize,
       "nvmFrSVCExcessTxBurstSize": nvmFrSVCExcessTxBurstSize,
       "nvmFrSVCExcessRxBurstSize": nvmFrSVCExcessRxBurstSize,
       "nvmFrVirtualPortTable": nvmFrVirtualPortTable,
       "nvmFrVirtualPortEntry": nvmFrVirtualPortEntry,
       "nvmFrVirtualPortIfIndex": nvmFrVirtualPortIfIndex,
       "nvmFrVirtualPortPhyPortIfIndex": nvmFrVirtualPortPhyPortIfIndex,
       "nvmFrVirtualPortPPA": nvmFrVirtualPortPPA,
       "nvmFrVirtualPortMode": nvmFrVirtualPortMode,
       "nvmFrVirtualPortEntryStatus": nvmFrVirtualPortEntryStatus,
       "nvmFrVirtualPortProtocolBinding": nvmFrVirtualPortProtocolBinding,
       "nvmFrVirtualPortNumber": nvmFrVirtualPortNumber,
       "nvmFrSVCMapTable": nvmFrSVCMapTable,
       "nvmFrSVCMapEntry": nvmFrSVCMapEntry,
       "nvmFrSVCMapVirtualPortIfIndex": nvmFrSVCMapVirtualPortIfIndex,
       "nvmFrSVCMapDNA": nvmFrSVCMapDNA,
       "nvmFrSVCMapMaxTxSize": nvmFrSVCMapMaxTxSize,
       "nvmFrSVCMapMaxRxSize": nvmFrSVCMapMaxRxSize,
       "nvmFrSVCMapMinTxThroughput": nvmFrSVCMapMinTxThroughput,
       "nvmFrSVCMapMinRxThroughput": nvmFrSVCMapMinRxThroughput,
       "nvmFrSVCMapMaxTxThroughput": nvmFrSVCMapMaxTxThroughput,
       "nvmFrSVCMapMaxRxThroughput": nvmFrSVCMapMaxRxThroughput,
       "nvmFrSVCMapTxBurstSize": nvmFrSVCMapTxBurstSize,
       "nvmFrSVCMapRxBurstSize": nvmFrSVCMapRxBurstSize,
       "nvmFrSVCMapExcessTxBurstSize": nvmFrSVCMapExcessTxBurstSize,
       "nvmFrSVCMapExcessRxBurstSize": nvmFrSVCMapExcessRxBurstSize,
       "nvmFrSVCMapPriority": nvmFrSVCMapPriority,
       "nvmFrSVCMapEntryStatus": nvmFrSVCMapEntryStatus,
       "nvmFrSVCMapTransferPriority": nvmFrSVCMapTransferPriority,
       "nvmFrSVCMapRowStatus": nvmFrSVCMapRowStatus,
       "nvmFrSVCMapDiscardPriority": nvmFrSVCMapDiscardPriority,
       "nvmFrSVCMapSetupPriority": nvmFrSVCMapSetupPriority,
       "nvmFrSVCMapHoldingPriority": nvmFrSVCMapHoldingPriority,
       "nvmFrPVCMapTable": nvmFrPVCMapTable,
       "nvmFrPVCMapEntry": nvmFrPVCMapEntry,
       "nvmFrPVCMapVirtualPortIfIndex": nvmFrPVCMapVirtualPortIfIndex,
       "nvmFrPVCMapDLCI": nvmFrPVCMapDLCI,
       "nvmFrPVCMapEntryStatus": nvmFrPVCMapEntryStatus,
       "nvmFrPVCMapPhysIfIndex": nvmFrPVCMapPhysIfIndex,
       "nvmFrDlcmiTable": nvmFrDlcmiTable,
       "nvmFrDlcmiEntry": nvmFrDlcmiEntry,
       "nvmFrDlcmiIfIndex": nvmFrDlcmiIfIndex,
       "nvmFrDlcmiState": nvmFrDlcmiState,
       "nvmFrDlcmiAddress": nvmFrDlcmiAddress,
       "nvmFrDlcmiAddressLen": nvmFrDlcmiAddressLen,
       "nvmFrDlcmiPollingInterval": nvmFrDlcmiPollingInterval,
       "nvmFrDlcmiFullEnquiryInterval": nvmFrDlcmiFullEnquiryInterval,
       "nvmFrDlcmiErrorThreshold": nvmFrDlcmiErrorThreshold,
       "nvmFrDlcmiMonitoredEvents": nvmFrDlcmiMonitoredEvents,
       "nvmFrDlcmiMaxSupportedVCs": nvmFrDlcmiMaxSupportedVCs,
       "nvmFrDlcmiMulticast": nvmFrDlcmiMulticast,
       "mcmFrAllSVCCircuitTable": mcmFrAllSVCCircuitTable,
       "mcmFrAllSVCCircuitEntry": mcmFrAllSVCCircuitEntry,
       "mcmFrAllSVCCircuitIfIndex": mcmFrAllSVCCircuitIfIndex,
       "mcmFrAllSVCCircuitDlci": mcmFrAllSVCCircuitDlci,
       "mcmFrAllSVCCircuitType": mcmFrAllSVCCircuitType,
       "mcmFrAllSVCCircuitDNA": mcmFrAllSVCCircuitDNA,
       "mcmFrAllSVCCircuitState": mcmFrAllSVCCircuitState,
       "mcmFrAllSVCCircuitReceivedFECNs": mcmFrAllSVCCircuitReceivedFECNs,
       "mcmFrAllSVCCircuitReceivedBECNs": mcmFrAllSVCCircuitReceivedBECNs,
       "mcmFrAllSVCCircuitSentFrames": mcmFrAllSVCCircuitSentFrames,
       "mcmFrAllSVCCircuitSentOctets": mcmFrAllSVCCircuitSentOctets,
       "mcmFrAllSVCCircuitReceivedFrames": mcmFrAllSVCCircuitReceivedFrames,
       "mcmFrAllSVCCircuitReceivedOctets": mcmFrAllSVCCircuitReceivedOctets,
       "mcmFrAllSVCCircuitCreationTime": mcmFrAllSVCCircuitCreationTime,
       "mcmFrAllSVCCircuitCallOriginator": mcmFrAllSVCCircuitCallOriginator,
       "mcmFrAllSVCCircuitLastTimeChange": mcmFrAllSVCCircuitLastTimeChange,
       "mcmFrAllSVCCircuitCommittedBurst": mcmFrAllSVCCircuitCommittedBurst,
       "mcmFrAllSVCCircuitExcessBurst": mcmFrAllSVCCircuitExcessBurst,
       "mcmFrAllSVCCircuitThroughput": mcmFrAllSVCCircuitThroughput,
       "mcmFrAllSVCCircuitNegMaxTxSize": mcmFrAllSVCCircuitNegMaxTxSize,
       "mcmFrAllSVCCircuitNegMaxRxSize": mcmFrAllSVCCircuitNegMaxRxSize,
       "mcmFrAllSVCCircuitNegTxThroughput": mcmFrAllSVCCircuitNegTxThroughput,
       "mcmFrAllSVCCircuitNegRxThroughput": mcmFrAllSVCCircuitNegRxThroughput,
       "mcmFrAllSVCCircuitNegTxBurst": mcmFrAllSVCCircuitNegTxBurst,
       "mcmFrAllSVCCircuitNegRxBurst": mcmFrAllSVCCircuitNegRxBurst,
       "mcmFrAllSVCCircuitNegTxExcess": mcmFrAllSVCCircuitNegTxExcess,
       "mcmFrAllSVCCircuitNegRxExcess": mcmFrAllSVCCircuitNegRxExcess,
       "mcmFrAllSVCCircuitTxDiscardCIRPolice": mcmFrAllSVCCircuitTxDiscardCIRPolice,
       "mcmFrAllSVCCircuitPriority": mcmFrAllSVCCircuitPriority,
       "mcmFrAllSVCCircuitSvcIfIndex": mcmFrAllSVCCircuitSvcIfIndex,
       "mcmFrAllSVCCircuitDiscardPriority": mcmFrAllSVCCircuitDiscardPriority,
       "mcmFrAllSVCCircuitSetupPriority": mcmFrAllSVCCircuitSetupPriority,
       "mcmFrAllSVCCircuitHoldingPriority": mcmFrAllSVCCircuitHoldingPriority,
       "mcmFrLANSpvcTable": mcmFrLANSpvcTable,
       "mcmFrLANSpvcEntry": mcmFrLANSpvcEntry,
       "mcmFrLANSpvcVirtualPortIfIndex": mcmFrLANSpvcVirtualPortIfIndex,
       "mcmFrLANSpvcRemoteDLCI": mcmFrLANSpvcRemoteDLCI,
       "mcmFrLANSpvcConnectId": mcmFrLANSpvcConnectId,
       "mcmFrLANSpvcRemoteDNA": mcmFrLANSpvcRemoteDNA,
       "mcmFrLANSpvcDLCI": mcmFrLANSpvcDLCI,
       "mcmFrLANSpvcIfIndex": mcmFrLANSpvcIfIndex,
       "mcmFrLANSpvcVPState": mcmFrLANSpvcVPState,
       "mcmFrLANSpvcSVCState": mcmFrLANSpvcSVCState,
       "mcmFrLANSpvcConnType": mcmFrLANSpvcConnType,
       "mcmFrLANSpvcLastChange": mcmFrLANSpvcLastChange,
       "mcmFrLANSpvcDisconnectReason": mcmFrLANSpvcDisconnectReason,
       "mcmFrLANSpvcSVCTable": mcmFrLANSpvcSVCTable,
       "mcmFrLANSpvcSVCEntry": mcmFrLANSpvcSVCEntry,
       "mcmFrLANSpvcSVCConnectId": mcmFrLANSpvcSVCConnectId,
       "mcmFrLANSpvcSVCIfIndex": mcmFrLANSpvcSVCIfIndex,
       "mcmFrLANSpvcSVCDNA": mcmFrLANSpvcSVCDNA,
       "mcmFrLANSpvcSVCDLCI": mcmFrLANSpvcSVCDLCI,
       "mcmFrLANSpvcSVCMaxTxSize": mcmFrLANSpvcSVCMaxTxSize,
       "mcmFrLANSpvcSVCMaxRxSize": mcmFrLANSpvcSVCMaxRxSize,
       "mcmFrLANSpvcSVCMinTxThroughput": mcmFrLANSpvcSVCMinTxThroughput,
       "mcmFrLANSpvcSVCMinRxThroughput": mcmFrLANSpvcSVCMinRxThroughput,
       "mcmFrLANSpvcSVCMaxTxThroughput": mcmFrLANSpvcSVCMaxTxThroughput,
       "mcmFrLANSpvcSVCMaxRxThroughput": mcmFrLANSpvcSVCMaxRxThroughput,
       "mcmFrLANSpvcSVCMaxTxBurstSize": mcmFrLANSpvcSVCMaxTxBurstSize,
       "mcmFrLANSpvcSVCMaxRxBurstSize": mcmFrLANSpvcSVCMaxRxBurstSize,
       "mcmFrLANSpvcSVCExcessTxBurstSize": mcmFrLANSpvcSVCExcessTxBurstSize,
       "mcmFrLANSpvcSVCExcessRxBurstSize": mcmFrLANSpvcSVCExcessRxBurstSize,
       "mcmFrLANSpvcSVCTransferPriority": mcmFrLANSpvcSVCTransferPriority,
       "mcmFrLANSpvcSVCReasonForDisconnect": mcmFrLANSpvcSVCReasonForDisconnect,
       "mcmFrLANSpvcSVCDiscardPriority": mcmFrLANSpvcSVCDiscardPriority,
       "mcmFrLANSpvcSVCSetupPriority": mcmFrLANSpvcSVCSetupPriority,
       "mcmFrLANSpvcSVCHoldingPriority": mcmFrLANSpvcSVCHoldingPriority,
       "nvmFrLANSpvcTable": nvmFrLANSpvcTable,
       "nvmFrLANSpvcEntry": nvmFrLANSpvcEntry,
       "nvmFrLANSpvcVirtualPortIfIndex": nvmFrLANSpvcVirtualPortIfIndex,
       "nvmFrLANSpvcRemoteDLCI": nvmFrLANSpvcRemoteDLCI,
       "nvmFrLANSpvcConnectId": nvmFrLANSpvcConnectId,
       "nvmFrLANSpvcRemoteDNA": nvmFrLANSpvcRemoteDNA,
       "nvmFrLANSpvcConnType": nvmFrLANSpvcConnType,
       "nvmFrLANSpvcRowStatus": nvmFrLANSpvcRowStatus,
       "nvmFrLANSpvcSVCTable": nvmFrLANSpvcSVCTable,
       "nvmFrLANSpvcSVCEntry": nvmFrLANSpvcSVCEntry,
       "nvmFrLANSpvcSVCConnectId": nvmFrLANSpvcSVCConnectId,
       "nvmFrLANSpvcSVCDNA": nvmFrLANSpvcSVCDNA,
       "nvmFrLANSpvcSVCMaxTxSize": nvmFrLANSpvcSVCMaxTxSize,
       "nvmFrLANSpvcSVCMaxRxSize": nvmFrLANSpvcSVCMaxRxSize,
       "nvmFrLANSpvcSVCMinTxThroughput": nvmFrLANSpvcSVCMinTxThroughput,
       "nvmFrLANSpvcSVCMinRxThroughput": nvmFrLANSpvcSVCMinRxThroughput,
       "nvmFrLANSpvcSVCMaxTxThroughput": nvmFrLANSpvcSVCMaxTxThroughput,
       "nvmFrLANSpvcSVCMaxRxThroughput": nvmFrLANSpvcSVCMaxRxThroughput,
       "nvmFrLANSpvcSVCMaxTxBurstSize": nvmFrLANSpvcSVCMaxTxBurstSize,
       "nvmFrLANSpvcSVCMaxRxBurstSize": nvmFrLANSpvcSVCMaxRxBurstSize,
       "nvmFrLANSpvcSVCExcessTxBurstSize": nvmFrLANSpvcSVCExcessTxBurstSize,
       "nvmFrLANSpvcSVCExcessRxBurstSize": nvmFrLANSpvcSVCExcessRxBurstSize,
       "nvmFrLANSpvcSVCTransferPriority": nvmFrLANSpvcSVCTransferPriority,
       "nvmFrLANSpvcSVCDiscardPriority": nvmFrLANSpvcSVCDiscardPriority,
       "nvmFrLANSpvcSVCSetupPriority": nvmFrLANSpvcSVCSetupPriority,
       "nvmFrLANSpvcSVCHoldingPriority": nvmFrLANSpvcSVCHoldingPriority,
       "mcmFrDlcmiSVCStatusTable": mcmFrDlcmiSVCStatusTable,
       "mcmFrDlcmiSVCStatusEntry": mcmFrDlcmiSVCStatusEntry,
       "mcmFrDlcmiSVCStatusIfIndex": mcmFrDlcmiSVCStatusIfIndex,
       "mcmFrDlcmiSVCStatusDlci": mcmFrDlcmiSVCStatusDlci,
       "mcmFrDlcmiSVCStatusCardNumber": mcmFrDlcmiSVCStatusCardNumber,
       "mcmFrDlcmiSVCStatusPortNumber": mcmFrDlcmiSVCStatusPortNumber,
       "mcmFrDlcmiSVCStatusTunnelPvcDlci": mcmFrDlcmiSVCStatusTunnelPvcDlci,
       "mcmFrDlcmiSVCStatusPeerCardNumber": mcmFrDlcmiSVCStatusPeerCardNumber,
       "mcmFrDlcmiSVCStatusPeerPortNumber": mcmFrDlcmiSVCStatusPeerPortNumber,
       "mcmFrDlcmiSVCStatusPeerTunPvcDlci": mcmFrDlcmiSVCStatusPeerTunPvcDlci,
       "mcmFrDlcmiSVCStatusPeerSvcDlci": mcmFrDlcmiSVCStatusPeerSvcDlci,
       "mcmFrTunnelPvcTable": mcmFrTunnelPvcTable,
       "mcmFrTunnelPvcEntry": mcmFrTunnelPvcEntry,
       "mcmFrTunnelPvcIfIndex": mcmFrTunnelPvcIfIndex,
       "mcmFrTunnelPvcDlciNumber": mcmFrTunnelPvcDlciNumber,
       "mcmFrTunnelPvcPhysicalCard": mcmFrTunnelPvcPhysicalCard,
       "mcmFrTunnelPvcPhysicalPort": mcmFrTunnelPvcPhysicalPort,
       "mcmFrTunnelPvcType": mcmFrTunnelPvcType,
       "mcmFrTunnelPvcPhysPortIfIndex": mcmFrTunnelPvcPhysPortIfIndex,
       "mcmFrTunnelPvcMaxRxFrameSize": mcmFrTunnelPvcMaxRxFrameSize,
       "mcmFrTunnelPvcRxBc": mcmFrTunnelPvcRxBc,
       "mcmFrTunnelPvcRxBe": mcmFrTunnelPvcRxBe,
       "mcmFrTunnelPvcMaxRxCIR": mcmFrTunnelPvcMaxRxCIR,
       "mcmFrTunnelPvcMaxTxFrameSize": mcmFrTunnelPvcMaxTxFrameSize,
       "mcmFrTunnelPvcTxBc": mcmFrTunnelPvcTxBc,
       "mcmFrTunnelPvcTxBe": mcmFrTunnelPvcTxBe,
       "mcmFrTunnelPvcMaxTxCIR": mcmFrTunnelPvcMaxTxCIR,
       "mcmFrTunnelPvcState": mcmFrTunnelPvcState,
       "mcmFrTunnelPvcRxFrames": mcmFrTunnelPvcRxFrames,
       "mcmFrTunnelPvcTxFrames": mcmFrTunnelPvcTxFrames,
       "mcmFrTunnelPvcRxDeFrames": mcmFrTunnelPvcRxDeFrames,
       "mcmFrTunnelPvcRxExcessFrames": mcmFrTunnelPvcRxExcessFrames,
       "mcmFrTunnelPvcTxExcessFrames": mcmFrTunnelPvcTxExcessFrames,
       "mcmFrTunnelPvcRxDiscards": mcmFrTunnelPvcRxDiscards,
       "mcmFrTunnelPvcRxOctets": mcmFrTunnelPvcRxOctets,
       "mcmFrTunnelPvcTxOctets": mcmFrTunnelPvcTxOctets,
       "mcmFrTunnelPvcConsecFrames": mcmFrTunnelPvcConsecFrames,
       "mcmFrTunnelPvcMinTxCIR": mcmFrTunnelPvcMinTxCIR,
       "nvmFrTunnelPvcTable": nvmFrTunnelPvcTable,
       "nvmFrTunnelPvcEntry": nvmFrTunnelPvcEntry,
       "nvmFrTunnelPvcIfIndex": nvmFrTunnelPvcIfIndex,
       "nvmFrTunnelPvcDlciNumber": nvmFrTunnelPvcDlciNumber,
       "nvmFrTunnelPvcPhysicalCard": nvmFrTunnelPvcPhysicalCard,
       "nvmFrTunnelPvcPhysicalPort": nvmFrTunnelPvcPhysicalPort,
       "nvmFrTunnelPvcType": nvmFrTunnelPvcType,
       "nvmFrTunnelPvcPhysPortIfIndex": nvmFrTunnelPvcPhysPortIfIndex,
       "nvmFrTunnelPvcMaxRxFrameSize": nvmFrTunnelPvcMaxRxFrameSize,
       "nvmFrTunnelPvcRxBc": nvmFrTunnelPvcRxBc,
       "nvmFrTunnelPvcRxBe": nvmFrTunnelPvcRxBe,
       "nvmFrTunnelPvcMaxRxCIR": nvmFrTunnelPvcMaxRxCIR,
       "nvmFrTunnelPvcMaxTxFrameSize": nvmFrTunnelPvcMaxTxFrameSize,
       "nvmFrTunnelPvcTxBc": nvmFrTunnelPvcTxBc,
       "nvmFrTunnelPvcTxBe": nvmFrTunnelPvcTxBe,
       "nvmFrTunnelPvcMaxTxCIR": nvmFrTunnelPvcMaxTxCIR,
       "nvmFrTunnelPvcRowStatus": nvmFrTunnelPvcRowStatus,
       "nvmFrTunnelPvcConsecFrames": nvmFrTunnelPvcConsecFrames,
       "nvmFrTunnelPvcMinTxCIR": nvmFrTunnelPvcMinTxCIR,
       "mcmFrNetlinkMapTable": mcmFrNetlinkMapTable,
       "mcmFrNetlinkMapEntry": mcmFrNetlinkMapEntry,
       "mcmFrNetlinkMapVPIfIndex": mcmFrNetlinkMapVPIfIndex,
       "mcmFrNetlinkMapNetlinkIfIndex": mcmFrNetlinkMapNetlinkIfIndex,
       "mcmFrNetlinkMapOperStatus": mcmFrNetlinkMapOperStatus,
       "nvmFrNetlinkMapTable": nvmFrNetlinkMapTable,
       "nvmFrNetlinkMapEntry": nvmFrNetlinkMapEntry,
       "nvmFrNetlinkMapVPIfIndex": nvmFrNetlinkMapVPIfIndex,
       "nvmFrNetlinkMapNetlinkIfIndex": nvmFrNetlinkMapNetlinkIfIndex,
       "nvmFrNetlinkMapRowStatus": nvmFrNetlinkMapRowStatus,
       "fr-control": fr_control,
       "mcmFrPhyPortCntrTable": mcmFrPhyPortCntrTable,
       "mcmFrPhyPortCntrEntry": mcmFrPhyPortCntrEntry,
       "mcmFrPhyPortCntrIfIndex": mcmFrPhyPortCntrIfIndex,
       "mcmFrPhyPortCntrAction": mcmFrPhyPortCntrAction,
       "mcmFrVirtualPortCntrTable": mcmFrVirtualPortCntrTable,
       "mcmFrVirtualPortCntrEntry": mcmFrVirtualPortCntrEntry,
       "mcmFrVirtualPortCntrIfIndex": mcmFrVirtualPortCntrIfIndex,
       "mcmFrVirtualPortCntrAction": mcmFrVirtualPortCntrAction,
       "mcmFrPVCCntrTable": mcmFrPVCCntrTable,
       "mcmFrPVCCntrEntry": mcmFrPVCCntrEntry,
       "mcmFrPVCCntrIfIndex": mcmFrPVCCntrIfIndex,
       "mcmFrPVCCntrDLCI": mcmFrPVCCntrDLCI,
       "mcmFrPVCCntrAction": mcmFrPVCCntrAction,
       "mcmFrSVCCntrTable": mcmFrSVCCntrTable,
       "mcmFrSVCCntrEntry": mcmFrSVCCntrEntry,
       "mcmFrSVCCntrIfIndex": mcmFrSVCCntrIfIndex,
       "mcmFrSVCCntrDNA": mcmFrSVCCntrDNA,
       "mcmFrSVCCntrAction": mcmFrSVCCntrAction}
)
