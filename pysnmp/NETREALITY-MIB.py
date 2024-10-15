# SNMP MIB module (NETREALITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETREALITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:40 2024
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

(DLCI,
 Index) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "DLCI",
    "Index")

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

_Netreality_ObjectIdentity = ObjectIdentity
netreality = _Netreality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382)
)
_NrGeneral_ObjectIdentity = ObjectIdentity
nrGeneral = _NrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 1)
)
_NrManagers_ObjectIdentity = ObjectIdentity
nrManagers = _NrManagers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 1, 1)
)
_NrTrapHostsTable_Object = MibTable
nrTrapHostsTable = _NrTrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nrTrapHostsTable.setStatus("mandatory")
_NrTrapHostsEntry_Object = MibTableRow
nrTrapHostsEntry = _NrTrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 1, 1, 1)
)
nrTrapHostsEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrTrapIPaddress"),
)
if mibBuilder.loadTexts:
    nrTrapHostsEntry.setStatus("mandatory")
_NrTrapIPaddress_Type = IpAddress
_NrTrapIPaddress_Object = MibTableColumn
nrTrapIPaddress = _NrTrapIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 1, 1, 1, 1),
    _NrTrapIPaddress_Type()
)
nrTrapIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrTrapIPaddress.setStatus("mandatory")


class _NrTrapPort_Type(Integer32):
    """Custom type nrTrapPort based on Integer32"""
    defaultValue = 162


_NrTrapPort_Object = MibTableColumn
nrTrapPort = _NrTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 1, 1, 1, 2),
    _NrTrapPort_Type()
)
nrTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrTrapPort.setStatus("mandatory")
_NrSystem_ObjectIdentity = ObjectIdentity
nrSystem = _NrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 1, 2)
)


class _NrSysReset_Type(Integer32):
    """Custom type nrSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_NrSysReset_Type.__name__ = "Integer32"
_NrSysReset_Object = MibScalar
nrSysReset = _NrSysReset_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 2, 1),
    _NrSysReset_Type()
)
nrSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrSysReset.setStatus("mandatory")


class _NrSysSetDefaults_Type(Integer32):
    """Custom type nrSysSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-process", 3),
          ("off", 1),
          ("set", 2))
    )


_NrSysSetDefaults_Type.__name__ = "Integer32"
_NrSysSetDefaults_Object = MibScalar
nrSysSetDefaults = _NrSysSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 2, 2),
    _NrSysSetDefaults_Type()
)
nrSysSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrSysSetDefaults.setStatus("mandatory")
_NrSysTrapCounter_Type = Counter32
_NrSysTrapCounter_Object = MibScalar
nrSysTrapCounter = _NrSysTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 2, 3),
    _NrSysTrapCounter_Type()
)
nrSysTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrSysTrapCounter.setStatus("mandatory")


class _NrSysEventReset_Type(Integer32):
    """Custom type nrSysEventReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-process", 3),
          ("off", 1),
          ("reset", 2))
    )


_NrSysEventReset_Type.__name__ = "Integer32"
_NrSysEventReset_Object = MibScalar
nrSysEventReset = _NrSysEventReset_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 2, 4),
    _NrSysEventReset_Type()
)
nrSysEventReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrSysEventReset.setStatus("mandatory")


class _NrSysSerial_Type(DisplayString):
    """Custom type nrSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NrSysSerial_Type.__name__ = "DisplayString"
_NrSysSerial_Object = MibScalar
nrSysSerial = _NrSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 2, 5),
    _NrSysSerial_Type()
)
nrSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrSysSerial.setStatus("mandatory")
_NrTrapInfo_ObjectIdentity = ObjectIdentity
nrTrapInfo = _NrTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 1, 3)
)


class _NrTrapRSType_Type(Integer32):
    """Custom type nrTrapRSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("com1", 5),
          ("ethernet", 2),
          ("flash", 4),
          ("memory", 1),
          ("unknown", 6),
          ("wanadapter", 3))
    )


_NrTrapRSType_Type.__name__ = "Integer32"
_NrTrapRSType_Object = MibScalar
nrTrapRSType = _NrTrapRSType_Object(
    (1, 3, 6, 1, 4, 1, 2382, 1, 3, 1),
    _NrTrapRSType_Type()
)
nrTrapRSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrTrapRSType.setStatus("mandatory")
_NrProducts_ObjectIdentity = ObjectIdentity
nrProducts = _NrProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 2)
)
_NrWanwise_ObjectIdentity = ObjectIdentity
nrWanwise = _NrWanwise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 2, 1)
)
_NrFr_ObjectIdentity = ObjectIdentity
nrFr = _NrFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3)
)
_NrInterface_ObjectIdentity = ObjectIdentity
nrInterface = _NrInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1)
)
_NrIfTable_Object = MibTable
nrIfTable = _NrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nrIfTable.setStatus("mandatory")
_NrIfEntry_Object = MibTableRow
nrIfEntry = _NrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1)
)
nrIfEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrIfIndex"),
)
if mibBuilder.loadTexts:
    nrIfEntry.setStatus("mandatory")
_NrIfIndex_Type = Integer32
_NrIfIndex_Object = MibTableColumn
nrIfIndex = _NrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 1),
    _NrIfIndex_Type()
)
nrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfIndex.setStatus("mandatory")
_NrIfInUtilization_Type = Integer32
_NrIfInUtilization_Object = MibTableColumn
nrIfInUtilization = _NrIfInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 2),
    _NrIfInUtilization_Type()
)
nrIfInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfInUtilization.setStatus("mandatory")
_NrIfOutUtilization_Type = Integer32
_NrIfOutUtilization_Object = MibTableColumn
nrIfOutUtilization = _NrIfOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 3),
    _NrIfOutUtilization_Type()
)
nrIfOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfOutUtilization.setStatus("mandatory")
_NrIfInErrRatio_Type = Integer32
_NrIfInErrRatio_Object = MibTableColumn
nrIfInErrRatio = _NrIfInErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 4),
    _NrIfInErrRatio_Type()
)
nrIfInErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfInErrRatio.setStatus("mandatory")
_NrIfOutErrRatio_Type = Integer32
_NrIfOutErrRatio_Object = MibTableColumn
nrIfOutErrRatio = _NrIfOutErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 5),
    _NrIfOutErrRatio_Type()
)
nrIfOutErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfOutErrRatio.setStatus("mandatory")


class _NrIfPhysConnType_Type(Integer32):
    """Custom type nrIfPhysConnType based on Integer32"""
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
          ("other", 1),
          ("passive", 3))
    )


_NrIfPhysConnType_Type.__name__ = "Integer32"
_NrIfPhysConnType_Object = MibTableColumn
nrIfPhysConnType = _NrIfPhysConnType_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 6),
    _NrIfPhysConnType_Type()
)
nrIfPhysConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfPhysConnType.setStatus("mandatory")


class _NrIfType_Type(Integer32):
    """Custom type nrIfType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("e1", 8),
          ("eia530-rs449", 4),
          ("frame-relay", 10),
          ("frame-relay-cisco", 11),
          ("hdlc-cisco", 13),
          ("hssi", 9),
          ("other", 1),
          ("ppp", 12),
          ("ppp-bay", 14),
          ("rs232", 6),
          ("t1", 7),
          ("v35", 2),
          ("v35db", 3),
          ("x21-x24", 5))
    )


_NrIfType_Type.__name__ = "Integer32"
_NrIfType_Object = MibTableColumn
nrIfType = _NrIfType_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 7),
    _NrIfType_Type()
)
nrIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfType.setStatus("mandatory")


class _NrIfOperMode_Type(Integer32):
    """Custom type nrIfOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 2),
          ("other", 1),
          ("shaper", 3))
    )


_NrIfOperMode_Type.__name__ = "Integer32"
_NrIfOperMode_Object = MibTableColumn
nrIfOperMode = _NrIfOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 8),
    _NrIfOperMode_Type()
)
nrIfOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfOperMode.setStatus("mandatory")
_NrIfGroupNm_Type = Integer32
_NrIfGroupNm_Object = MibTableColumn
nrIfGroupNm = _NrIfGroupNm_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 1, 1, 1, 9),
    _NrIfGroupNm_Type()
)
nrIfGroupNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrIfGroupNm.setStatus("mandatory")
_NrFrame_relay_ObjectIdentity = ObjectIdentity
nrFrame_relay = _NrFrame_relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2)
)
_NrFrCircuitTable_Object = MibTable
nrFrCircuitTable = _NrFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nrFrCircuitTable.setStatus("mandatory")
_NrFrCircuitEntry_Object = MibTableRow
nrFrCircuitEntry = _NrFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1)
)
nrFrCircuitEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrFrCircuitIfIndex"),
    (0, "NETREALITY-MIB", "nrFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    nrFrCircuitEntry.setStatus("mandatory")
_NrFrCircuitIfIndex_Type = Index
_NrFrCircuitIfIndex_Object = MibTableColumn
nrFrCircuitIfIndex = _NrFrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 1),
    _NrFrCircuitIfIndex_Type()
)
nrFrCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitIfIndex.setStatus("mandatory")
_NrFrCircuitDlci_Type = DLCI
_NrFrCircuitDlci_Object = MibTableColumn
nrFrCircuitDlci = _NrFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 2),
    _NrFrCircuitDlci_Type()
)
nrFrCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitDlci.setStatus("mandatory")
_NrFrCircuitInCIRUtilization_Type = Integer32
_NrFrCircuitInCIRUtilization_Object = MibTableColumn
nrFrCircuitInCIRUtilization = _NrFrCircuitInCIRUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 3),
    _NrFrCircuitInCIRUtilization_Type()
)
nrFrCircuitInCIRUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitInCIRUtilization.setStatus("mandatory")
_NrFrCircuitOutCIRUtilization_Type = Integer32
_NrFrCircuitOutCIRUtilization_Object = MibTableColumn
nrFrCircuitOutCIRUtilization = _NrFrCircuitOutCIRUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 4),
    _NrFrCircuitOutCIRUtilization_Type()
)
nrFrCircuitOutCIRUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitOutCIRUtilization.setStatus("mandatory")
_NrFrCircuitInDiscard_Type = Counter32
_NrFrCircuitInDiscard_Object = MibTableColumn
nrFrCircuitInDiscard = _NrFrCircuitInDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 5),
    _NrFrCircuitInDiscard_Type()
)
nrFrCircuitInDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitInDiscard.setStatus("mandatory")
_NrFrCircuitOutDiscard_Type = Counter32
_NrFrCircuitOutDiscard_Object = MibTableColumn
nrFrCircuitOutDiscard = _NrFrCircuitOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 6),
    _NrFrCircuitOutDiscard_Type()
)
nrFrCircuitOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitOutDiscard.setStatus("mandatory")


class _NrFrCircuitEchoAddress_Type(IpAddress):
    """Custom type nrFrCircuitEchoAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NrFrCircuitEchoAddress_Object = MibTableColumn
nrFrCircuitEchoAddress = _NrFrCircuitEchoAddress_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 7),
    _NrFrCircuitEchoAddress_Type()
)
nrFrCircuitEchoAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrFrCircuitEchoAddress.setStatus("mandatory")


class _NrFrCircuitEchoProto_Type(Integer32):
    """Custom type nrFrCircuitEchoProto based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 2),
          ("other", 1))
    )


_NrFrCircuitEchoProto_Type.__name__ = "Integer32"
_NrFrCircuitEchoProto_Object = MibTableColumn
nrFrCircuitEchoProto = _NrFrCircuitEchoProto_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 8),
    _NrFrCircuitEchoProto_Type()
)
nrFrCircuitEchoProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrFrCircuitEchoProto.setStatus("mandatory")


class _NrFrCircuitEchoStatus_Type(Integer32):
    """Custom type nrFrCircuitEchoStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NrFrCircuitEchoStatus_Type.__name__ = "Integer32"
_NrFrCircuitEchoStatus_Object = MibTableColumn
nrFrCircuitEchoStatus = _NrFrCircuitEchoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 9),
    _NrFrCircuitEchoStatus_Type()
)
nrFrCircuitEchoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrFrCircuitEchoStatus.setStatus("mandatory")


class _NrFrCircuitLastResponseTime_Type(Integer32):
    """Custom type nrFrCircuitLastResponseTime based on Integer32"""
    defaultValue = 0


_NrFrCircuitLastResponseTime_Object = MibTableColumn
nrFrCircuitLastResponseTime = _NrFrCircuitLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 2, 2, 1, 10),
    _NrFrCircuitLastResponseTime_Type()
)
nrFrCircuitLastResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrFrCircuitLastResponseTime.setStatus("mandatory")
_NrRmon_ObjectIdentity = ObjectIdentity
nrRmon = _NrRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3)
)
_NrNlMatrix_ObjectIdentity = ObjectIdentity
nrNlMatrix = _NrNlMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1)
)
_NrNlMatrixTable_Object = MibTable
nrNlMatrixTable = _NrNlMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nrNlMatrixTable.setStatus("mandatory")
_NrNlMatrixEntry_Object = MibTableRow
nrNlMatrixEntry = _NrNlMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1)
)
nrNlMatrixEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrNlMatrixifNumber"),
    (0, "NETREALITY-MIB", "nrNlMatrixDlciNumber"),
    (0, "NETREALITY-MIB", "nrNlMatrixProtocol"),
    (0, "NETREALITY-MIB", "nrNlMatrixAddress1"),
    (0, "NETREALITY-MIB", "nrNlMatrixAddress2"),
)
if mibBuilder.loadTexts:
    nrNlMatrixEntry.setStatus("mandatory")
_NrNlMatrixifNumber_Type = Integer32
_NrNlMatrixifNumber_Object = MibTableColumn
nrNlMatrixifNumber = _NrNlMatrixifNumber_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1, 1),
    _NrNlMatrixifNumber_Type()
)
nrNlMatrixifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlMatrixifNumber.setStatus("mandatory")
_NrNlMatrixDlciNumber_Type = Integer32
_NrNlMatrixDlciNumber_Object = MibTableColumn
nrNlMatrixDlciNumber = _NrNlMatrixDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1, 2),
    _NrNlMatrixDlciNumber_Type()
)
nrNlMatrixDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlMatrixDlciNumber.setStatus("mandatory")


class _NrNlMatrixProtocol_Type(Integer32):
    """Custom type nrNlMatrixProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NrNlMatrixProtocol_Type.__name__ = "Integer32"
_NrNlMatrixProtocol_Object = MibTableColumn
nrNlMatrixProtocol = _NrNlMatrixProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1, 3),
    _NrNlMatrixProtocol_Type()
)
nrNlMatrixProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlMatrixProtocol.setStatus("mandatory")
_NrNlMatrixAddress1_Type = OctetString
_NrNlMatrixAddress1_Object = MibTableColumn
nrNlMatrixAddress1 = _NrNlMatrixAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1, 4),
    _NrNlMatrixAddress1_Type()
)
nrNlMatrixAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlMatrixAddress1.setStatus("mandatory")
_NrNlMatrixAddress2_Type = OctetString
_NrNlMatrixAddress2_Object = MibTableColumn
nrNlMatrixAddress2 = _NrNlMatrixAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1, 5),
    _NrNlMatrixAddress2_Type()
)
nrNlMatrixAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlMatrixAddress2.setStatus("mandatory")
_NrNl1to2UfromCIR_Type = Integer32
_NrNl1to2UfromCIR_Object = MibTableColumn
nrNl1to2UfromCIR = _NrNl1to2UfromCIR_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 1, 1, 1, 6),
    _NrNl1to2UfromCIR_Type()
)
nrNl1to2UfromCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNl1to2UfromCIR.setStatus("mandatory")
_NrNlHost_ObjectIdentity = ObjectIdentity
nrNlHost = _NrNlHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2)
)
_NrNlHostTable_Object = MibTable
nrNlHostTable = _NrNlHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nrNlHostTable.setStatus("mandatory")
_NrNlHostEntry_Object = MibTableRow
nrNlHostEntry = _NrNlHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1, 1)
)
nrNlHostEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrNlHostifNumber"),
    (0, "NETREALITY-MIB", "nrNlHostDlciNumber"),
    (0, "NETREALITY-MIB", "nrNlMatrixProtocol"),
    (0, "NETREALITY-MIB", "nrNlHostAddress"),
)
if mibBuilder.loadTexts:
    nrNlHostEntry.setStatus("mandatory")
_NrNlHostifNumber_Type = Integer32
_NrNlHostifNumber_Object = MibTableColumn
nrNlHostifNumber = _NrNlHostifNumber_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1, 1, 1),
    _NrNlHostifNumber_Type()
)
nrNlHostifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlHostifNumber.setStatus("mandatory")
_NrNlHostDlciNumber_Type = Integer32
_NrNlHostDlciNumber_Object = MibTableColumn
nrNlHostDlciNumber = _NrNlHostDlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1, 1, 2),
    _NrNlHostDlciNumber_Type()
)
nrNlHostDlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlHostDlciNumber.setStatus("mandatory")


class _NrNlHostProtocol_Type(Integer32):
    """Custom type nrNlHostProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NrNlHostProtocol_Type.__name__ = "Integer32"
_NrNlHostProtocol_Object = MibTableColumn
nrNlHostProtocol = _NrNlHostProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1, 1, 3),
    _NrNlHostProtocol_Type()
)
nrNlHostProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlHostProtocol.setStatus("mandatory")
_NrNlHostAddress_Type = OctetString
_NrNlHostAddress_Object = MibTableColumn
nrNlHostAddress = _NrNlHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1, 1, 4),
    _NrNlHostAddress_Type()
)
nrNlHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlHostAddress.setStatus("mandatory")
_NrNlHostUtilization_Type = Integer32
_NrNlHostUtilization_Object = MibTableColumn
nrNlHostUtilization = _NrNlHostUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 3, 2, 1, 1, 5),
    _NrNlHostUtilization_Type()
)
nrNlHostUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrNlHostUtilization.setStatus("mandatory")
_NrBulk_ObjectIdentity = ObjectIdentity
nrBulk = _NrBulk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4)
)
_NrtCtrl_ObjectIdentity = ObjectIdentity
nrtCtrl = _NrtCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1)
)


class _NrtCtrlLtermInterval_Type(Integer32):
    """Custom type nrtCtrlLtermInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_NrtCtrlLtermInterval_Type.__name__ = "Integer32"
_NrtCtrlLtermInterval_Object = MibScalar
nrtCtrlLtermInterval = _NrtCtrlLtermInterval_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 1),
    _NrtCtrlLtermInterval_Type()
)
nrtCtrlLtermInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrtCtrlLtermInterval.setStatus("mandatory")


class _NrtCtrlLtermBucketsGrant_Type(Integer32):
    """Custom type nrtCtrlLtermBucketsGrant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NrtCtrlLtermBucketsGrant_Type.__name__ = "Integer32"
_NrtCtrlLtermBucketsGrant_Object = MibScalar
nrtCtrlLtermBucketsGrant = _NrtCtrlLtermBucketsGrant_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 2),
    _NrtCtrlLtermBucketsGrant_Type()
)
nrtCtrlLtermBucketsGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtCtrlLtermBucketsGrant.setStatus("mandatory")
_NrtCtrlLtermLast_Type = Integer32
_NrtCtrlLtermLast_Object = MibScalar
nrtCtrlLtermLast = _NrtCtrlLtermLast_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 3),
    _NrtCtrlLtermLast_Type()
)
nrtCtrlLtermLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtCtrlLtermLast.setStatus("mandatory")
_NrtCtrlLtermTime_Type = Integer32
_NrtCtrlLtermTime_Object = MibScalar
nrtCtrlLtermTime = _NrtCtrlLtermTime_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 4),
    _NrtCtrlLtermTime_Type()
)
nrtCtrlLtermTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtCtrlLtermTime.setStatus("mandatory")


class _NrtCtrlStermInterval_Type(Integer32):
    """Custom type nrtCtrlStermInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_NrtCtrlStermInterval_Type.__name__ = "Integer32"
_NrtCtrlStermInterval_Object = MibScalar
nrtCtrlStermInterval = _NrtCtrlStermInterval_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 5),
    _NrtCtrlStermInterval_Type()
)
nrtCtrlStermInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nrtCtrlStermInterval.setStatus("mandatory")


class _NrtCtrlStermBucketsGrant_Type(Integer32):
    """Custom type nrtCtrlStermBucketsGrant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NrtCtrlStermBucketsGrant_Type.__name__ = "Integer32"
_NrtCtrlStermBucketsGrant_Object = MibScalar
nrtCtrlStermBucketsGrant = _NrtCtrlStermBucketsGrant_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 6),
    _NrtCtrlStermBucketsGrant_Type()
)
nrtCtrlStermBucketsGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtCtrlStermBucketsGrant.setStatus("mandatory")
_NrtCtrlStermLast_Type = Integer32
_NrtCtrlStermLast_Object = MibScalar
nrtCtrlStermLast = _NrtCtrlStermLast_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 7),
    _NrtCtrlStermLast_Type()
)
nrtCtrlStermLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtCtrlStermLast.setStatus("mandatory")
_NrtCtrlStermTime_Type = Integer32
_NrtCtrlStermTime_Object = MibScalar
nrtCtrlStermTime = _NrtCtrlStermTime_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 1, 8),
    _NrtCtrlStermTime_Type()
)
nrtCtrlStermTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtCtrlStermTime.setStatus("mandatory")
_NrShortTermData_ObjectIdentity = ObjectIdentity
nrShortTermData = _NrShortTermData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 2)
)
_NrShortTermDataTable_Object = MibTable
nrShortTermDataTable = _NrShortTermDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nrShortTermDataTable.setStatus("mandatory")
_NrShortTermDataEntry_Object = MibTableRow
nrShortTermDataEntry = _NrShortTermDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 2, 1, 1)
)
nrShortTermDataEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrShortTermBucketIndex"),
    (0, "NETREALITY-MIB", "nrShortTermDataIndex"),
)
if mibBuilder.loadTexts:
    nrShortTermDataEntry.setStatus("mandatory")
_NrShortTermBucketIndex_Type = Integer32
_NrShortTermBucketIndex_Object = MibTableColumn
nrShortTermBucketIndex = _NrShortTermBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 2, 1, 1, 1),
    _NrShortTermBucketIndex_Type()
)
nrShortTermBucketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrShortTermBucketIndex.setStatus("mandatory")
_NrShortTermDataIndex_Type = Integer32
_NrShortTermDataIndex_Object = MibTableColumn
nrShortTermDataIndex = _NrShortTermDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 2, 1, 1, 2),
    _NrShortTermDataIndex_Type()
)
nrShortTermDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrShortTermDataIndex.setStatus("mandatory")
_NrShortTermDataData_Type = OctetString
_NrShortTermDataData_Object = MibTableColumn
nrShortTermDataData = _NrShortTermDataData_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 2, 1, 1, 3),
    _NrShortTermDataData_Type()
)
nrShortTermDataData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrShortTermDataData.setStatus("mandatory")
_NrLongTermData_ObjectIdentity = ObjectIdentity
nrLongTermData = _NrLongTermData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 3)
)
_NrLongTermDataTable_Object = MibTable
nrLongTermDataTable = _NrLongTermDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    nrLongTermDataTable.setStatus("mandatory")
_NrLongTermDataEntry_Object = MibTableRow
nrLongTermDataEntry = _NrLongTermDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 3, 1, 1)
)
nrLongTermDataEntry.setIndexNames(
    (0, "NETREALITY-MIB", "nrLongTermBucketIndex"),
    (0, "NETREALITY-MIB", "nrLongTermDataIndex"),
)
if mibBuilder.loadTexts:
    nrLongTermDataEntry.setStatus("mandatory")
_NrLongTermBucketIndex_Type = Integer32
_NrLongTermBucketIndex_Object = MibTableColumn
nrLongTermBucketIndex = _NrLongTermBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 3, 1, 1, 1),
    _NrLongTermBucketIndex_Type()
)
nrLongTermBucketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrLongTermBucketIndex.setStatus("mandatory")
_NrLongTermDataIndex_Type = Integer32
_NrLongTermDataIndex_Object = MibTableColumn
nrLongTermDataIndex = _NrLongTermDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 3, 1, 1, 2),
    _NrLongTermDataIndex_Type()
)
nrLongTermDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrLongTermDataIndex.setStatus("mandatory")
_NrLongTermDataData_Type = OctetString
_NrLongTermDataData_Object = MibTableColumn
nrLongTermDataData = _NrLongTermDataData_Object(
    (1, 3, 6, 1, 4, 1, 2382, 3, 4, 3, 1, 1, 3),
    _NrLongTermDataData_Type()
)
nrLongTermDataData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrLongTermDataData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nrShortResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 2382, 0, 1)
)
nrShortResources.setObjects(
    ("NETREALITY-MIB", "nrTrapRSType")
)
if mibBuilder.loadTexts:
    nrShortResources.setStatus(
        ""
    )

nrDiagnosticFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2382, 0, 2)
)
nrDiagnosticFailure.setObjects(
    ("NETREALITY-MIB", "nrTrapRSType")
)
if mibBuilder.loadTexts:
    nrDiagnosticFailure.setStatus(
        ""
    )

nrDLCIRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2382, 0, 3)
)
nrDLCIRemove.setObjects(
      *(("NETREALITY-MIB", "nrFrCircuitIfIndex"),
        ("NETREALITY-MIB", "nrFrCircuitDlci"))
)
if mibBuilder.loadTexts:
    nrDLCIRemove.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETREALITY-MIB",
    **{"netreality": netreality,
       "nrShortResources": nrShortResources,
       "nrDiagnosticFailure": nrDiagnosticFailure,
       "nrDLCIRemove": nrDLCIRemove,
       "nrGeneral": nrGeneral,
       "nrManagers": nrManagers,
       "nrTrapHostsTable": nrTrapHostsTable,
       "nrTrapHostsEntry": nrTrapHostsEntry,
       "nrTrapIPaddress": nrTrapIPaddress,
       "nrTrapPort": nrTrapPort,
       "nrSystem": nrSystem,
       "nrSysReset": nrSysReset,
       "nrSysSetDefaults": nrSysSetDefaults,
       "nrSysTrapCounter": nrSysTrapCounter,
       "nrSysEventReset": nrSysEventReset,
       "nrSysSerial": nrSysSerial,
       "nrTrapInfo": nrTrapInfo,
       "nrTrapRSType": nrTrapRSType,
       "nrProducts": nrProducts,
       "nrWanwise": nrWanwise,
       "nrFr": nrFr,
       "nrInterface": nrInterface,
       "nrIfTable": nrIfTable,
       "nrIfEntry": nrIfEntry,
       "nrIfIndex": nrIfIndex,
       "nrIfInUtilization": nrIfInUtilization,
       "nrIfOutUtilization": nrIfOutUtilization,
       "nrIfInErrRatio": nrIfInErrRatio,
       "nrIfOutErrRatio": nrIfOutErrRatio,
       "nrIfPhysConnType": nrIfPhysConnType,
       "nrIfType": nrIfType,
       "nrIfOperMode": nrIfOperMode,
       "nrIfGroupNm": nrIfGroupNm,
       "nrFrame-relay": nrFrame_relay,
       "nrFrCircuitTable": nrFrCircuitTable,
       "nrFrCircuitEntry": nrFrCircuitEntry,
       "nrFrCircuitIfIndex": nrFrCircuitIfIndex,
       "nrFrCircuitDlci": nrFrCircuitDlci,
       "nrFrCircuitInCIRUtilization": nrFrCircuitInCIRUtilization,
       "nrFrCircuitOutCIRUtilization": nrFrCircuitOutCIRUtilization,
       "nrFrCircuitInDiscard": nrFrCircuitInDiscard,
       "nrFrCircuitOutDiscard": nrFrCircuitOutDiscard,
       "nrFrCircuitEchoAddress": nrFrCircuitEchoAddress,
       "nrFrCircuitEchoProto": nrFrCircuitEchoProto,
       "nrFrCircuitEchoStatus": nrFrCircuitEchoStatus,
       "nrFrCircuitLastResponseTime": nrFrCircuitLastResponseTime,
       "nrRmon": nrRmon,
       "nrNlMatrix": nrNlMatrix,
       "nrNlMatrixTable": nrNlMatrixTable,
       "nrNlMatrixEntry": nrNlMatrixEntry,
       "nrNlMatrixifNumber": nrNlMatrixifNumber,
       "nrNlMatrixDlciNumber": nrNlMatrixDlciNumber,
       "nrNlMatrixProtocol": nrNlMatrixProtocol,
       "nrNlMatrixAddress1": nrNlMatrixAddress1,
       "nrNlMatrixAddress2": nrNlMatrixAddress2,
       "nrNl1to2UfromCIR": nrNl1to2UfromCIR,
       "nrNlHost": nrNlHost,
       "nrNlHostTable": nrNlHostTable,
       "nrNlHostEntry": nrNlHostEntry,
       "nrNlHostifNumber": nrNlHostifNumber,
       "nrNlHostDlciNumber": nrNlHostDlciNumber,
       "nrNlHostProtocol": nrNlHostProtocol,
       "nrNlHostAddress": nrNlHostAddress,
       "nrNlHostUtilization": nrNlHostUtilization,
       "nrBulk": nrBulk,
       "nrtCtrl": nrtCtrl,
       "nrtCtrlLtermInterval": nrtCtrlLtermInterval,
       "nrtCtrlLtermBucketsGrant": nrtCtrlLtermBucketsGrant,
       "nrtCtrlLtermLast": nrtCtrlLtermLast,
       "nrtCtrlLtermTime": nrtCtrlLtermTime,
       "nrtCtrlStermInterval": nrtCtrlStermInterval,
       "nrtCtrlStermBucketsGrant": nrtCtrlStermBucketsGrant,
       "nrtCtrlStermLast": nrtCtrlStermLast,
       "nrtCtrlStermTime": nrtCtrlStermTime,
       "nrShortTermData": nrShortTermData,
       "nrShortTermDataTable": nrShortTermDataTable,
       "nrShortTermDataEntry": nrShortTermDataEntry,
       "nrShortTermBucketIndex": nrShortTermBucketIndex,
       "nrShortTermDataIndex": nrShortTermDataIndex,
       "nrShortTermDataData": nrShortTermDataData,
       "nrLongTermData": nrLongTermData,
       "nrLongTermDataTable": nrLongTermDataTable,
       "nrLongTermDataEntry": nrLongTermDataEntry,
       "nrLongTermBucketIndex": nrLongTermBucketIndex,
       "nrLongTermDataIndex": nrLongTermDataIndex,
       "nrLongTermDataData": nrLongTermDataData}
)
