# SNMP MIB module (CTRON-REMOTE-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-REMOTE-ACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:12 2024
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



class Index(Integer32):
    """Custom type Index based on Integer32"""




class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_Ctron_ObjectIdentity = ObjectIdentity
ctron = _Ctron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1)
)
_CtDataLink_ObjectIdentity = ObjectIdentity
ctDataLink = _CtDataLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2)
)
_CtronWan_ObjectIdentity = ObjectIdentity
ctronWan = _CtronWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7)
)
_CtRemoteAccess_ObjectIdentity = ObjectIdentity
ctRemoteAccess = _CtRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2)
)
_CtRemoteConnection_ObjectIdentity = ObjectIdentity
ctRemoteConnection = _CtRemoteConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1)
)
_CtRemNumConnections_Type = Integer32
_CtRemNumConnections_Object = MibScalar
ctRemNumConnections = _CtRemNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 1),
    _CtRemNumConnections_Type()
)
ctRemNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemNumConnections.setStatus("mandatory")
_CtRemPhysPortTable_Object = MibTable
ctRemPhysPortTable = _CtRemPhysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ctRemPhysPortTable.setStatus("mandatory")
_CtRemPhysPortEntry_Object = MibTableRow
ctRemPhysPortEntry = _CtRemPhysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1)
)
ctRemPhysPortEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctRemConnectionIndex"),
)
if mibBuilder.loadTexts:
    ctRemPhysPortEntry.setStatus("mandatory")
_CtRemConnectionIndex_Type = Integer32
_CtRemConnectionIndex_Object = MibTableColumn
ctRemConnectionIndex = _CtRemConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 1),
    _CtRemConnectionIndex_Type()
)
ctRemConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemConnectionIndex.setStatus("mandatory")


class _CtRemPhysPortType_Type(Integer32):
    """Custom type ctRemPhysPortType based on Integer32"""
    defaultValue = 1

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
        *(("dds", 5),
          ("di", 6),
          ("ds30", 9),
          ("e1", 3),
          ("hdsl", 7),
          ("isdnBRI", 8),
          ("none", 1),
          ("synchronous", 4),
          ("t1", 2),
          ("t1dds", 10))
    )


_CtRemPhysPortType_Type.__name__ = "Integer32"
_CtRemPhysPortType_Object = MibTableColumn
ctRemPhysPortType = _CtRemPhysPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 2),
    _CtRemPhysPortType_Type()
)
ctRemPhysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemPhysPortType.setStatus("mandatory")
_CtRemPhysPortSpecificMib_Type = ObjectIdentifier
_CtRemPhysPortSpecificMib_Object = MibTableColumn
ctRemPhysPortSpecificMib = _CtRemPhysPortSpecificMib_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 3),
    _CtRemPhysPortSpecificMib_Type()
)
ctRemPhysPortSpecificMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemPhysPortSpecificMib.setStatus("mandatory")


class _CtRemPhysPortProtMgrType_Type(Integer32):
    """Custom type ctRemPhysPortProtMgrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("frameRelayPvcRtr", 5),
          ("frameRelayPvcSw", 6),
          ("hdlc", 7),
          ("isdnBriPpp", 4),
          ("isdnPriPpp", 3),
          ("none", 1),
          ("pppNailedUp", 2))
    )


_CtRemPhysPortProtMgrType_Type.__name__ = "Integer32"
_CtRemPhysPortProtMgrType_Object = MibTableColumn
ctRemPhysPortProtMgrType = _CtRemPhysPortProtMgrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 4),
    _CtRemPhysPortProtMgrType_Type()
)
ctRemPhysPortProtMgrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemPhysPortProtMgrType.setStatus("mandatory")
_CtRemPhysPortProtMgrIfaceNum_Type = Integer32
_CtRemPhysPortProtMgrIfaceNum_Object = MibTableColumn
ctRemPhysPortProtMgrIfaceNum = _CtRemPhysPortProtMgrIfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 5),
    _CtRemPhysPortProtMgrIfaceNum_Type()
)
ctRemPhysPortProtMgrIfaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemPhysPortProtMgrIfaceNum.setStatus("mandatory")
_CtRemPhysPortWanIfaceNum_Type = Integer32
_CtRemPhysPortWanIfaceNum_Object = MibTableColumn
ctRemPhysPortWanIfaceNum = _CtRemPhysPortWanIfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 6),
    _CtRemPhysPortWanIfaceNum_Type()
)
ctRemPhysPortWanIfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemPhysPortWanIfaceNum.setStatus("mandatory")
_CtRemPhysPortProtMgrMaxIfos_Type = Integer32
_CtRemPhysPortProtMgrMaxIfos_Object = MibTableColumn
ctRemPhysPortProtMgrMaxIfos = _CtRemPhysPortProtMgrMaxIfos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 7),
    _CtRemPhysPortProtMgrMaxIfos_Type()
)
ctRemPhysPortProtMgrMaxIfos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemPhysPortProtMgrMaxIfos.setStatus("mandatory")
_CtRemPhysPortProtMgrIfaceList_Type = DisplayString
_CtRemPhysPortProtMgrIfaceList_Object = MibTableColumn
ctRemPhysPortProtMgrIfaceList = _CtRemPhysPortProtMgrIfaceList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 8),
    _CtRemPhysPortProtMgrIfaceList_Type()
)
ctRemPhysPortProtMgrIfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemPhysPortProtMgrIfaceList.setStatus("mandatory")
_CtRemPhysAlarmTimeOut_Type = Integer32
_CtRemPhysAlarmTimeOut_Object = MibTableColumn
ctRemPhysAlarmTimeOut = _CtRemPhysAlarmTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 9),
    _CtRemPhysAlarmTimeOut_Type()
)
ctRemPhysAlarmTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemPhysAlarmTimeOut.setStatus("mandatory")


class _CtRemPhysWpimType_Type(Integer32):
    """Custom type ctRemPhysWpimType based on Integer32"""
    defaultValue = 2


_CtRemPhysWpimType_Object = MibTableColumn
ctRemPhysWpimType = _CtRemPhysWpimType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 2, 1, 10),
    _CtRemPhysWpimType_Type()
)
ctRemPhysWpimType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemPhysWpimType.setStatus("mandatory")
_CtRemInterfaceTable_Object = MibTable
ctRemInterfaceTable = _CtRemInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ctRemInterfaceTable.setStatus("mandatory")
_CtRemInterfaceEntry_Object = MibTableRow
ctRemInterfaceEntry = _CtRemInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1)
)
ctRemInterfaceEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctRemIntEntIfIndex"),
)
if mibBuilder.loadTexts:
    ctRemInterfaceEntry.setStatus("mandatory")
_CtRemIntEntIfIndex_Type = Integer32
_CtRemIntEntIfIndex_Object = MibTableColumn
ctRemIntEntIfIndex = _CtRemIntEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 1),
    _CtRemIntEntIfIndex_Type()
)
ctRemIntEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemIntEntIfIndex.setStatus("mandatory")


class _CtRemIntEntCompression_Type(Integer32):
    """Custom type ctRemIntEntCompression based on Integer32"""
    defaultValue = 2

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


_CtRemIntEntCompression_Type.__name__ = "Integer32"
_CtRemIntEntCompression_Object = MibTableColumn
ctRemIntEntCompression = _CtRemIntEntCompression_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 2),
    _CtRemIntEntCompression_Type()
)
ctRemIntEntCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntCompression.setStatus("mandatory")
_CtRemIntEntCompRatio_Type = DisplayString
_CtRemIntEntCompRatio_Object = MibTableColumn
ctRemIntEntCompRatio = _CtRemIntEntCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 3),
    _CtRemIntEntCompRatio_Type()
)
ctRemIntEntCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemIntEntCompRatio.setStatus("mandatory")


class _CtRemIntEntCompStatus_Type(Integer32):
    """Custom type ctRemIntEntCompStatus based on Integer32"""
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


_CtRemIntEntCompStatus_Type.__name__ = "Integer32"
_CtRemIntEntCompStatus_Object = MibTableColumn
ctRemIntEntCompStatus = _CtRemIntEntCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 4),
    _CtRemIntEntCompStatus_Type()
)
ctRemIntEntCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemIntEntCompStatus.setStatus("mandatory")
_CtRemIntEntMTU_Type = Integer32
_CtRemIntEntMTU_Object = MibTableColumn
ctRemIntEntMTU = _CtRemIntEntMTU_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 5),
    _CtRemIntEntMTU_Type()
)
ctRemIntEntMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntMTU.setStatus("mandatory")


class _CtRemIntEntCongestion_Type(Integer32):
    """Custom type ctRemIntEntCongestion based on Integer32"""
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


_CtRemIntEntCongestion_Type.__name__ = "Integer32"
_CtRemIntEntCongestion_Object = MibTableColumn
ctRemIntEntCongestion = _CtRemIntEntCongestion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 6),
    _CtRemIntEntCongestion_Type()
)
ctRemIntEntCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntCongestion.setStatus("mandatory")
_CtRemIntEntMaxProfiles_Type = Integer32
_CtRemIntEntMaxProfiles_Object = MibTableColumn
ctRemIntEntMaxProfiles = _CtRemIntEntMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 7),
    _CtRemIntEntMaxProfiles_Type()
)
ctRemIntEntMaxProfiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntMaxProfiles.setStatus("mandatory")
_CtRemIntEntTxIdleTimeout_Type = Integer32
_CtRemIntEntTxIdleTimeout_Object = MibTableColumn
ctRemIntEntTxIdleTimeout = _CtRemIntEntTxIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 8),
    _CtRemIntEntTxIdleTimeout_Type()
)
ctRemIntEntTxIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntTxIdleTimeout.setStatus("mandatory")
_CtRemIntEntRxIdleTimeout_Type = Integer32
_CtRemIntEntRxIdleTimeout_Object = MibTableColumn
ctRemIntEntRxIdleTimeout = _CtRemIntEntRxIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 9),
    _CtRemIntEntRxIdleTimeout_Type()
)
ctRemIntEntRxIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntRxIdleTimeout.setStatus("mandatory")
_CtRemIntEntCircuitName_Type = DisplayString
_CtRemIntEntCircuitName_Object = MibTableColumn
ctRemIntEntCircuitName = _CtRemIntEntCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 10),
    _CtRemIntEntCircuitName_Type()
)
ctRemIntEntCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntCircuitName.setStatus("mandatory")


class _CtRemIntEntEncryption_Type(Integer32):
    """Custom type ctRemIntEntEncryption based on Integer32"""
    defaultValue = 2

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


_CtRemIntEntEncryption_Type.__name__ = "Integer32"
_CtRemIntEntEncryption_Object = MibTableColumn
ctRemIntEntEncryption = _CtRemIntEntEncryption_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 11),
    _CtRemIntEntEncryption_Type()
)
ctRemIntEntEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntEncryption.setStatus("mandatory")


class _CtRemIntEntEncryptStatus_Type(Integer32):
    """Custom type ctRemIntEntEncryptStatus based on Integer32"""
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


_CtRemIntEntEncryptStatus_Type.__name__ = "Integer32"
_CtRemIntEntEncryptStatus_Object = MibTableColumn
ctRemIntEntEncryptStatus = _CtRemIntEntEncryptStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 3, 1, 12),
    _CtRemIntEntEncryptStatus_Type()
)
ctRemIntEntEncryptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemIntEntEncryptStatus.setStatus("mandatory")
_CtRemPrimaryInterfaceTable_Object = MibTable
ctRemPrimaryInterfaceTable = _CtRemPrimaryInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ctRemPrimaryInterfaceTable.setStatus("mandatory")
_CtRemPrimaryInterfaceEntry_Object = MibTableRow
ctRemPrimaryInterfaceEntry = _CtRemPrimaryInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 4, 1)
)
ctRemPrimaryInterfaceEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctRemPriIntEntIfIndex"),
)
if mibBuilder.loadTexts:
    ctRemPrimaryInterfaceEntry.setStatus("mandatory")
_CtRemPriIntEntIfIndex_Type = Integer32
_CtRemPriIntEntIfIndex_Object = MibTableColumn
ctRemPriIntEntIfIndex = _CtRemPriIntEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 4, 1, 1),
    _CtRemPriIntEntIfIndex_Type()
)
ctRemPriIntEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemPriIntEntIfIndex.setStatus("mandatory")


class _CtRemPriIntEntConnectRetryInterval_Type(Integer32):
    """Custom type ctRemPriIntEntConnectRetryInterval based on Integer32"""
    defaultValue = 30


_CtRemPriIntEntConnectRetryInterval_Object = MibTableColumn
ctRemPriIntEntConnectRetryInterval = _CtRemPriIntEntConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 4, 1, 2),
    _CtRemPriIntEntConnectRetryInterval_Type()
)
ctRemPriIntEntConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemPriIntEntConnectRetryInterval.setStatus("mandatory")
_CtRemBackupInterfaceTable_Object = MibTable
ctRemBackupInterfaceTable = _CtRemBackupInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ctRemBackupInterfaceTable.setStatus("mandatory")
_CtRemBackupInterfaceEntry_Object = MibTableRow
ctRemBackupInterfaceEntry = _CtRemBackupInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1)
)
ctRemBackupInterfaceEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctRemIntEntBackupIfIndex"),
)
if mibBuilder.loadTexts:
    ctRemBackupInterfaceEntry.setStatus("mandatory")
_CtRemIntEntBackupIfIndex_Type = Integer32
_CtRemIntEntBackupIfIndex_Object = MibTableColumn
ctRemIntEntBackupIfIndex = _CtRemIntEntBackupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 1),
    _CtRemIntEntBackupIfIndex_Type()
)
ctRemIntEntBackupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemIntEntBackupIfIndex.setStatus("mandatory")
_CtRemIntEntBackupIfNum_Type = Integer32
_CtRemIntEntBackupIfNum_Object = MibTableColumn
ctRemIntEntBackupIfNum = _CtRemIntEntBackupIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 2),
    _CtRemIntEntBackupIfNum_Type()
)
ctRemIntEntBackupIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntBackupIfNum.setStatus("mandatory")
_CtRemIntEntBackupIfInUseCnt_Type = Integer32
_CtRemIntEntBackupIfInUseCnt_Object = MibTableColumn
ctRemIntEntBackupIfInUseCnt = _CtRemIntEntBackupIfInUseCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 3),
    _CtRemIntEntBackupIfInUseCnt_Type()
)
ctRemIntEntBackupIfInUseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemIntEntBackupIfInUseCnt.setStatus("mandatory")
_CtRemIntEntBackupIfTimeToConnect_Type = Integer32
_CtRemIntEntBackupIfTimeToConnect_Object = MibTableColumn
ctRemIntEntBackupIfTimeToConnect = _CtRemIntEntBackupIfTimeToConnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 4),
    _CtRemIntEntBackupIfTimeToConnect_Type()
)
ctRemIntEntBackupIfTimeToConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntBackupIfTimeToConnect.setStatus("mandatory")
_CtRemIntEntBackupIfTimeToDisconnect_Type = Integer32
_CtRemIntEntBackupIfTimeToDisconnect_Object = MibTableColumn
ctRemIntEntBackupIfTimeToDisconnect = _CtRemIntEntBackupIfTimeToDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 5),
    _CtRemIntEntBackupIfTimeToDisconnect_Type()
)
ctRemIntEntBackupIfTimeToDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntBackupIfTimeToDisconnect.setStatus("mandatory")


class _CtRemIntEntBackupIfOverride_Type(Integer32):
    """Custom type ctRemIntEntBackupIfOverride based on Integer32"""
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


_CtRemIntEntBackupIfOverride_Type.__name__ = "Integer32"
_CtRemIntEntBackupIfOverride_Object = MibTableColumn
ctRemIntEntBackupIfOverride = _CtRemIntEntBackupIfOverride_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 6),
    _CtRemIntEntBackupIfOverride_Type()
)
ctRemIntEntBackupIfOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntBackupIfOverride.setStatus("mandatory")
_CtRemIntEntBackupConnectRetries_Type = Integer32
_CtRemIntEntBackupConnectRetries_Object = MibTableColumn
ctRemIntEntBackupConnectRetries = _CtRemIntEntBackupConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 7),
    _CtRemIntEntBackupConnectRetries_Type()
)
ctRemIntEntBackupConnectRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntBackupConnectRetries.setStatus("mandatory")
_CtRemIntEntBackupConnectRetryInterval_Type = Integer32
_CtRemIntEntBackupConnectRetryInterval_Object = MibTableColumn
ctRemIntEntBackupConnectRetryInterval = _CtRemIntEntBackupConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 5, 1, 8),
    _CtRemIntEntBackupConnectRetryInterval_Type()
)
ctRemIntEntBackupConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemIntEntBackupConnectRetryInterval.setStatus("mandatory")
_CtRemExtPhysPortTable_Object = MibTable
ctRemExtPhysPortTable = _CtRemExtPhysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ctRemExtPhysPortTable.setStatus("mandatory")
_CtRemExtPhysPortEntry_Object = MibTableRow
ctRemExtPhysPortEntry = _CtRemExtPhysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1)
)
ctRemExtPhysPortEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctRemExtConnectionIndex"),
)
if mibBuilder.loadTexts:
    ctRemExtPhysPortEntry.setStatus("mandatory")
_CtRemExtConnectionIndex_Type = Integer32
_CtRemExtConnectionIndex_Object = MibTableColumn
ctRemExtConnectionIndex = _CtRemExtConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 1),
    _CtRemExtConnectionIndex_Type()
)
ctRemExtConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemExtConnectionIndex.setStatus("mandatory")
_CtRemExtProtMgrIndex_Type = Integer32
_CtRemExtProtMgrIndex_Object = MibTableColumn
ctRemExtProtMgrIndex = _CtRemExtProtMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 2),
    _CtRemExtProtMgrIndex_Type()
)
ctRemExtProtMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemExtProtMgrIndex.setStatus("mandatory")


class _CtRemExtPhysPortProtMgrType_Type(Integer32):
    """Custom type ctRemExtPhysPortProtMgrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("frameRelayPvcRtr", 5),
          ("frameRelayPvcSw", 6),
          ("hdlc", 7),
          ("isdnBriPpp", 4),
          ("isdnPriPpp", 3),
          ("none", 1),
          ("pppNailedUp", 2))
    )


_CtRemExtPhysPortProtMgrType_Type.__name__ = "Integer32"
_CtRemExtPhysPortProtMgrType_Object = MibTableColumn
ctRemExtPhysPortProtMgrType = _CtRemExtPhysPortProtMgrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 3),
    _CtRemExtPhysPortProtMgrType_Type()
)
ctRemExtPhysPortProtMgrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemExtPhysPortProtMgrType.setStatus("mandatory")


class _CtRemExtPhysPortProtMgrEnable_Type(Integer32):
    """Custom type ctRemExtPhysPortProtMgrEnable based on Integer32"""
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


_CtRemExtPhysPortProtMgrEnable_Type.__name__ = "Integer32"
_CtRemExtPhysPortProtMgrEnable_Object = MibTableColumn
ctRemExtPhysPortProtMgrEnable = _CtRemExtPhysPortProtMgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 4),
    _CtRemExtPhysPortProtMgrEnable_Type()
)
ctRemExtPhysPortProtMgrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemExtPhysPortProtMgrEnable.setStatus("mandatory")
_CtRemExtPhysPortProtMgrIfaceNum_Type = Integer32
_CtRemExtPhysPortProtMgrIfaceNum_Object = MibTableColumn
ctRemExtPhysPortProtMgrIfaceNum = _CtRemExtPhysPortProtMgrIfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 5),
    _CtRemExtPhysPortProtMgrIfaceNum_Type()
)
ctRemExtPhysPortProtMgrIfaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemExtPhysPortProtMgrIfaceNum.setStatus("mandatory")
_CtRemExtPhysPortProtMgrMaxIfos_Type = Integer32
_CtRemExtPhysPortProtMgrMaxIfos_Object = MibTableColumn
ctRemExtPhysPortProtMgrMaxIfos = _CtRemExtPhysPortProtMgrMaxIfos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 6),
    _CtRemExtPhysPortProtMgrMaxIfos_Type()
)
ctRemExtPhysPortProtMgrMaxIfos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRemExtPhysPortProtMgrMaxIfos.setStatus("mandatory")
_CtRemExtPhysPortProtMgrIfaceList_Type = DisplayString
_CtRemExtPhysPortProtMgrIfaceList_Object = MibTableColumn
ctRemExtPhysPortProtMgrIfaceList = _CtRemExtPhysPortProtMgrIfaceList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 7),
    _CtRemExtPhysPortProtMgrIfaceList_Type()
)
ctRemExtPhysPortProtMgrIfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemExtPhysPortProtMgrIfaceList.setStatus("mandatory")
_CtRemExtPhysPortProtMgrChannelList_Type = DisplayString
_CtRemExtPhysPortProtMgrChannelList_Object = MibTableColumn
ctRemExtPhysPortProtMgrChannelList = _CtRemExtPhysPortProtMgrChannelList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 1, 6, 1, 8),
    _CtRemExtPhysPortProtMgrChannelList_Type()
)
ctRemExtPhysPortProtMgrChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRemExtPhysPortProtMgrChannelList.setStatus("mandatory")
_CtDs1Ext_ObjectIdentity = ObjectIdentity
ctDs1Ext = _CtDs1Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2)
)
_CtDs1ExtensionsTable_Object = MibTable
ctDs1ExtensionsTable = _CtDs1ExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctDs1ExtensionsTable.setStatus("mandatory")
_CtDs1ExtensionsEntry_Object = MibTableRow
ctDs1ExtensionsEntry = _CtDs1ExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1)
)
ctDs1ExtensionsEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctDs1ExtensionsEntryIndex"),
)
if mibBuilder.loadTexts:
    ctDs1ExtensionsEntry.setStatus("mandatory")
_CtDs1ExtensionsEntryIndex_Type = Integer32
_CtDs1ExtensionsEntryIndex_Object = MibTableColumn
ctDs1ExtensionsEntryIndex = _CtDs1ExtensionsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 1),
    _CtDs1ExtensionsEntryIndex_Type()
)
ctDs1ExtensionsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs1ExtensionsEntryIndex.setStatus("mandatory")
_CtDs1ExtensionsNumInterfaces_Type = Integer32
_CtDs1ExtensionsNumInterfaces_Object = MibTableColumn
ctDs1ExtensionsNumInterfaces = _CtDs1ExtensionsNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 2),
    _CtDs1ExtensionsNumInterfaces_Type()
)
ctDs1ExtensionsNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs1ExtensionsNumInterfaces.setStatus("mandatory")


class _CtDs1ExtensionsToggleFracTable_Type(Integer32):
    """Custom type ctDs1ExtensionsToggleFracTable based on Integer32"""
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
        *(("display-new", 2),
          ("display-old", 3),
          ("restore-old", 4),
          ("update-table", 1))
    )


_CtDs1ExtensionsToggleFracTable_Type.__name__ = "Integer32"
_CtDs1ExtensionsToggleFracTable_Object = MibTableColumn
ctDs1ExtensionsToggleFracTable = _CtDs1ExtensionsToggleFracTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 3),
    _CtDs1ExtensionsToggleFracTable_Type()
)
ctDs1ExtensionsToggleFracTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs1ExtensionsToggleFracTable.setStatus("mandatory")


class _CtDs1ExtensionsLineBuildOut_Type(Integer32):
    """Custom type ctDs1ExtensionsLineBuildOut based on Integer32"""
    defaultValue = 2

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("a133to266feet", 5),
          ("a266to399feet", 6),
          ("a399to533feet", 7),
          ("a533to655feet", 8),
          ("minus-15", 4),
          ("minus-7point5", 3),
          ("unknown", 1),
          ("zero", 2))
    )


_CtDs1ExtensionsLineBuildOut_Type.__name__ = "Integer32"
_CtDs1ExtensionsLineBuildOut_Object = MibTableColumn
ctDs1ExtensionsLineBuildOut = _CtDs1ExtensionsLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 4),
    _CtDs1ExtensionsLineBuildOut_Type()
)
ctDs1ExtensionsLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs1ExtensionsLineBuildOut.setStatus("mandatory")


class _CtDs1ExtensionsCFADuration_Type(Integer32):
    """Custom type ctDs1ExtensionsCFADuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CtDs1ExtensionsCFADuration_Type.__name__ = "Integer32"
_CtDs1ExtensionsCFADuration_Object = MibTableColumn
ctDs1ExtensionsCFADuration = _CtDs1ExtensionsCFADuration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 5),
    _CtDs1ExtensionsCFADuration_Type()
)
ctDs1ExtensionsCFADuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs1ExtensionsCFADuration.setStatus("mandatory")


class _CtDs1ExtensionsDIEnable_Type(Integer32):
    """Custom type ctDs1ExtensionsDIEnable based on Integer32"""
    defaultValue = 1

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


_CtDs1ExtensionsDIEnable_Type.__name__ = "Integer32"
_CtDs1ExtensionsDIEnable_Object = MibTableColumn
ctDs1ExtensionsDIEnable = _CtDs1ExtensionsDIEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 6),
    _CtDs1ExtensionsDIEnable_Type()
)
ctDs1ExtensionsDIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs1ExtensionsDIEnable.setStatus("mandatory")
_CtDs1ExtensionsTotalValidIntervals_Type = Counter32
_CtDs1ExtensionsTotalValidIntervals_Object = MibTableColumn
ctDs1ExtensionsTotalValidIntervals = _CtDs1ExtensionsTotalValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 7),
    _CtDs1ExtensionsTotalValidIntervals_Type()
)
ctDs1ExtensionsTotalValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs1ExtensionsTotalValidIntervals.setStatus("mandatory")


class _WanDs1ExtensionsBertTestMode_Type(Integer32):
    """Custom type wanDs1ExtensionsBertTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("manual", 3),
          ("none", 1))
    )


_WanDs1ExtensionsBertTestMode_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertTestMode_Object = MibTableColumn
wanDs1ExtensionsBertTestMode = _WanDs1ExtensionsBertTestMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 8),
    _WanDs1ExtensionsBertTestMode_Type()
)
wanDs1ExtensionsBertTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertTestMode.setStatus("mandatory")


class _WanDs1ExtensionsBertRun_Type(Integer32):
    """Custom type wanDs1ExtensionsBertRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WanDs1ExtensionsBertRun_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertRun_Object = MibTableColumn
wanDs1ExtensionsBertRun = _WanDs1ExtensionsBertRun_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 9),
    _WanDs1ExtensionsBertRun_Type()
)
wanDs1ExtensionsBertRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertRun.setStatus("mandatory")
_WanDs1ExtensionsBertCurrentResults_Type = Integer32
_WanDs1ExtensionsBertCurrentResults_Object = MibTableColumn
wanDs1ExtensionsBertCurrentResults = _WanDs1ExtensionsBertCurrentResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 10),
    _WanDs1ExtensionsBertCurrentResults_Type()
)
wanDs1ExtensionsBertCurrentResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertCurrentResults.setStatus("mandatory")
_WanDs1ExtensionsBertCumulativeResults_Type = Integer32
_WanDs1ExtensionsBertCumulativeResults_Object = MibTableColumn
wanDs1ExtensionsBertCumulativeResults = _WanDs1ExtensionsBertCumulativeResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 11),
    _WanDs1ExtensionsBertCumulativeResults_Type()
)
wanDs1ExtensionsBertCumulativeResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertCumulativeResults.setStatus("mandatory")
_WanDs1ExtensionsBertPeakResults_Type = Integer32
_WanDs1ExtensionsBertPeakResults_Object = MibTableColumn
wanDs1ExtensionsBertPeakResults = _WanDs1ExtensionsBertPeakResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 12),
    _WanDs1ExtensionsBertPeakResults_Type()
)
wanDs1ExtensionsBertPeakResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertPeakResults.setStatus("mandatory")
_WanDs1ExtensionsBertAverageResult_Type = Integer32
_WanDs1ExtensionsBertAverageResult_Object = MibTableColumn
wanDs1ExtensionsBertAverageResult = _WanDs1ExtensionsBertAverageResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 13),
    _WanDs1ExtensionsBertAverageResult_Type()
)
wanDs1ExtensionsBertAverageResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertAverageResult.setStatus("mandatory")


class _WanDs1ExtensionsBertTestPattern_Type(Integer32):
    """Custom type wanDs1ExtensionsBertTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("pattern1s", 2),
          ("pattern2047", 5),
          ("pattern3in24", 6),
          ("pattern511", 4),
          ("pattern63", 3),
          ("patternOther", 1),
          ("patternQRSS", 7))
    )


_WanDs1ExtensionsBertTestPattern_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertTestPattern_Object = MibTableColumn
wanDs1ExtensionsBertTestPattern = _WanDs1ExtensionsBertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 14),
    _WanDs1ExtensionsBertTestPattern_Type()
)
wanDs1ExtensionsBertTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertTestPattern.setStatus("mandatory")
_WanDs1ExtensionsBertSamplePeriod_Type = Integer32
_WanDs1ExtensionsBertSamplePeriod_Object = MibTableColumn
wanDs1ExtensionsBertSamplePeriod = _WanDs1ExtensionsBertSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 15),
    _WanDs1ExtensionsBertSamplePeriod_Type()
)
wanDs1ExtensionsBertSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertSamplePeriod.setStatus("mandatory")
_WanDs1ExtensionsBertNumPeriods_Type = Counter32
_WanDs1ExtensionsBertNumPeriods_Object = MibTableColumn
wanDs1ExtensionsBertNumPeriods = _WanDs1ExtensionsBertNumPeriods_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 16),
    _WanDs1ExtensionsBertNumPeriods_Type()
)
wanDs1ExtensionsBertNumPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertNumPeriods.setStatus("mandatory")


class _WanDs1ExtensionsBertTestTraps_Type(Integer32):
    """Custom type wanDs1ExtensionsBertTestTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WanDs1ExtensionsBertTestTraps_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertTestTraps_Object = MibTableColumn
wanDs1ExtensionsBertTestTraps = _WanDs1ExtensionsBertTestTraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 17),
    _WanDs1ExtensionsBertTestTraps_Type()
)
wanDs1ExtensionsBertTestTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertTestTraps.setStatus("mandatory")


class _WanDs1ExtensionsBertDataStatus_Type(Integer32):
    """Custom type wanDs1ExtensionsBertDataStatus based on Integer32"""
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
        *(("idle", 1),
          ("running", 4),
          ("waitingForLink", 2),
          ("waitingForLoopback", 3))
    )


_WanDs1ExtensionsBertDataStatus_Type.__name__ = "Integer32"
_WanDs1ExtensionsBertDataStatus_Object = MibTableColumn
wanDs1ExtensionsBertDataStatus = _WanDs1ExtensionsBertDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 1, 1, 18),
    _WanDs1ExtensionsBertDataStatus_Type()
)
wanDs1ExtensionsBertDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDs1ExtensionsBertDataStatus.setStatus("mandatory")
_CtDs1WanDriverTable_Object = MibTable
ctDs1WanDriverTable = _CtDs1WanDriverTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ctDs1WanDriverTable.setStatus("mandatory")
_CtDs1WanDriverEntry_Object = MibTableRow
ctDs1WanDriverEntry = _CtDs1WanDriverEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 2, 1)
)
ctDs1WanDriverEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctDs1WanDriverEntryIndex"),
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctDs1WanDriverChannelIndex"),
)
if mibBuilder.loadTexts:
    ctDs1WanDriverEntry.setStatus("mandatory")
_CtDs1WanDriverEntryIndex_Type = Integer32
_CtDs1WanDriverEntryIndex_Object = MibTableColumn
ctDs1WanDriverEntryIndex = _CtDs1WanDriverEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 2, 1, 1),
    _CtDs1WanDriverEntryIndex_Type()
)
ctDs1WanDriverEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs1WanDriverEntryIndex.setStatus("mandatory")
_CtDs1WanDriverChannelIndex_Type = Integer32
_CtDs1WanDriverChannelIndex_Object = MibTableColumn
ctDs1WanDriverChannelIndex = _CtDs1WanDriverChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 2, 1, 2),
    _CtDs1WanDriverChannelIndex_Type()
)
ctDs1WanDriverChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs1WanDriverChannelIndex.setStatus("mandatory")


class _CtDs1WanDriverLineCode_Type(Integer32):
    """Custom type ctDs1WanDriverLineCode based on Integer32"""
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
        *(("invHDLC", 3),
          ("jBZS", 2),
          ("none", 1))
    )


_CtDs1WanDriverLineCode_Type.__name__ = "Integer32"
_CtDs1WanDriverLineCode_Object = MibTableColumn
ctDs1WanDriverLineCode = _CtDs1WanDriverLineCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 2, 1, 3),
    _CtDs1WanDriverLineCode_Type()
)
ctDs1WanDriverLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs1WanDriverLineCode.setStatus("mandatory")


class _CtDs1WanDriverCRCBits_Type(Integer32):
    """Custom type ctDs1WanDriverCRCBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_CtDs1WanDriverCRCBits_Type.__name__ = "Integer32"
_CtDs1WanDriverCRCBits_Object = MibTableColumn
ctDs1WanDriverCRCBits = _CtDs1WanDriverCRCBits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 2, 2, 1, 4),
    _CtDs1WanDriverCRCBits_Type()
)
ctDs1WanDriverCRCBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs1WanDriverCRCBits.setStatus("mandatory")
_CtRs232Ext_ObjectIdentity = ObjectIdentity
ctRs232Ext = _CtRs232Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3)
)
_CtRs232ExtensionsTable_Object = MibTable
ctRs232ExtensionsTable = _CtRs232ExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ctRs232ExtensionsTable.setStatus("mandatory")
_CtRs232ExtensionsEntry_Object = MibTableRow
ctRs232ExtensionsEntry = _CtRs232ExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1, 1)
)
ctRs232ExtensionsEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctRs232ExtensionsEntryIndex"),
)
if mibBuilder.loadTexts:
    ctRs232ExtensionsEntry.setStatus("mandatory")
_CtRs232ExtensionsEntryIndex_Type = Integer32
_CtRs232ExtensionsEntryIndex_Object = MibTableColumn
ctRs232ExtensionsEntryIndex = _CtRs232ExtensionsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1, 1, 1),
    _CtRs232ExtensionsEntryIndex_Type()
)
ctRs232ExtensionsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctRs232ExtensionsEntryIndex.setStatus("mandatory")


class _CtRs232ExtensionsCTSEnable_Type(Integer32):
    """Custom type ctRs232ExtensionsCTSEnable based on Integer32"""
    defaultValue = 2

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


_CtRs232ExtensionsCTSEnable_Type.__name__ = "Integer32"
_CtRs232ExtensionsCTSEnable_Object = MibTableColumn
ctRs232ExtensionsCTSEnable = _CtRs232ExtensionsCTSEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1, 1, 2),
    _CtRs232ExtensionsCTSEnable_Type()
)
ctRs232ExtensionsCTSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRs232ExtensionsCTSEnable.setStatus("mandatory")


class _CtRs232ExtensionsDSREnable_Type(Integer32):
    """Custom type ctRs232ExtensionsDSREnable based on Integer32"""
    defaultValue = 2

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


_CtRs232ExtensionsDSREnable_Type.__name__ = "Integer32"
_CtRs232ExtensionsDSREnable_Object = MibTableColumn
ctRs232ExtensionsDSREnable = _CtRs232ExtensionsDSREnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1, 1, 3),
    _CtRs232ExtensionsDSREnable_Type()
)
ctRs232ExtensionsDSREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRs232ExtensionsDSREnable.setStatus("mandatory")


class _CtRs232ExtensionsRTSEnable_Type(Integer32):
    """Custom type ctRs232ExtensionsRTSEnable based on Integer32"""
    defaultValue = 2

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


_CtRs232ExtensionsRTSEnable_Type.__name__ = "Integer32"
_CtRs232ExtensionsRTSEnable_Object = MibTableColumn
ctRs232ExtensionsRTSEnable = _CtRs232ExtensionsRTSEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1, 1, 4),
    _CtRs232ExtensionsRTSEnable_Type()
)
ctRs232ExtensionsRTSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRs232ExtensionsRTSEnable.setStatus("mandatory")


class _CtRs232ExtensionsDTREnable_Type(Integer32):
    """Custom type ctRs232ExtensionsDTREnable based on Integer32"""
    defaultValue = 2

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


_CtRs232ExtensionsDTREnable_Type.__name__ = "Integer32"
_CtRs232ExtensionsDTREnable_Object = MibTableColumn
ctRs232ExtensionsDTREnable = _CtRs232ExtensionsDTREnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 3, 1, 1, 5),
    _CtRs232ExtensionsDTREnable_Type()
)
ctRs232ExtensionsDTREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctRs232ExtensionsDTREnable.setStatus("mandatory")
_CtFrDcp_ObjectIdentity = ObjectIdentity
ctFrDcp = _CtFrDcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4)
)
_FrDcpCircuitTable_Object = MibTable
frDcpCircuitTable = _FrDcpCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1)
)
if mibBuilder.loadTexts:
    frDcpCircuitTable.setStatus("mandatory")
_FrDcpCircuitEntry_Object = MibTableRow
frDcpCircuitEntry = _FrDcpCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1, 1)
)
frDcpCircuitEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "frDcpCircuitIfIndex"),
    (0, "CTRON-REMOTE-ACCESS-MIB", "frDcpCircuitDlci"),
)
if mibBuilder.loadTexts:
    frDcpCircuitEntry.setStatus("mandatory")
_FrDcpCircuitIfIndex_Type = Index
_FrDcpCircuitIfIndex_Object = MibTableColumn
frDcpCircuitIfIndex = _FrDcpCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1, 1, 1),
    _FrDcpCircuitIfIndex_Type()
)
frDcpCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitIfIndex.setStatus("mandatory")
_FrDcpCircuitDlci_Type = DLCI
_FrDcpCircuitDlci_Object = MibTableColumn
frDcpCircuitDlci = _FrDcpCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1, 1, 2),
    _FrDcpCircuitDlci_Type()
)
frDcpCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitDlci.setStatus("mandatory")


class _FrDcpCircuitEnable_Type(Integer32):
    """Custom type frDcpCircuitEnable based on Integer32"""
    defaultValue = 2

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


_FrDcpCircuitEnable_Type.__name__ = "Integer32"
_FrDcpCircuitEnable_Object = MibTableColumn
frDcpCircuitEnable = _FrDcpCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1, 1, 3),
    _FrDcpCircuitEnable_Type()
)
frDcpCircuitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDcpCircuitEnable.setStatus("mandatory")


class _FrDcpCircuitStatus_Type(Integer32):
    """Custom type frDcpCircuitStatus based on Integer32"""
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


_FrDcpCircuitStatus_Type.__name__ = "Integer32"
_FrDcpCircuitStatus_Object = MibTableColumn
frDcpCircuitStatus = _FrDcpCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1, 1, 4),
    _FrDcpCircuitStatus_Type()
)
frDcpCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitStatus.setStatus("mandatory")


class _FrDcpCircuitRatio_Type(OctetString):
    """Custom type frDcpCircuitRatio based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_FrDcpCircuitRatio_Type.__name__ = "OctetString"
_FrDcpCircuitRatio_Object = MibTableColumn
frDcpCircuitRatio = _FrDcpCircuitRatio_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 4, 1, 1, 5),
    _FrDcpCircuitRatio_Type()
)
frDcpCircuitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDcpCircuitRatio.setStatus("mandatory")
_CtDDSExt_ObjectIdentity = ObjectIdentity
ctDDSExt = _CtDDSExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5)
)
_CtDDSConfigTable_Object = MibTable
ctDDSConfigTable = _CtDDSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ctDDSConfigTable.setStatus("mandatory")
_CtDDSConfigEntry_Object = MibTableRow
ctDDSConfigEntry = _CtDDSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1)
)
ctDDSConfigEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctDDSLineIndex"),
)
if mibBuilder.loadTexts:
    ctDDSConfigEntry.setStatus("mandatory")


class _CtDDSLineIndex_Type(Integer32):
    """Custom type ctDDSLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtDDSLineIndex_Type.__name__ = "Integer32"
_CtDDSLineIndex_Object = MibTableColumn
ctDDSLineIndex = _CtDDSLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 1),
    _CtDDSLineIndex_Type()
)
ctDDSLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDDSLineIndex.setStatus("mandatory")


class _CtDDSIfIndex_Type(Integer32):
    """Custom type ctDDSIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtDDSIfIndex_Type.__name__ = "Integer32"
_CtDDSIfIndex_Object = MibTableColumn
ctDDSIfIndex = _CtDDSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 2),
    _CtDDSIfIndex_Type()
)
ctDDSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDDSIfIndex.setStatus("mandatory")


class _CtDDSLineMode_Type(Integer32):
    """Custom type ctDDSLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsCc", 3),
          ("ddsPri", 1),
          ("ddsSc", 2))
    )


_CtDDSLineMode_Type.__name__ = "Integer32"
_CtDDSLineMode_Object = MibTableColumn
ctDDSLineMode = _CtDDSLineMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 3),
    _CtDDSLineMode_Type()
)
ctDDSLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDDSLineMode.setStatus("mandatory")


class _CtDDSLineCoding_Type(Integer32):
    """Custom type ctDDSLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsJBZS", 2),
          ("ddsNone", 1),
          ("otherLineCode", 3))
    )


_CtDDSLineCoding_Type.__name__ = "Integer32"
_CtDDSLineCoding_Object = MibTableColumn
ctDDSLineCoding = _CtDDSLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 4),
    _CtDDSLineCoding_Type()
)
ctDDSLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDDSLineCoding.setStatus("mandatory")


class _CtDDSLoopbackConfig_Type(Integer32):
    """Custom type ctDDSLoopbackConfig based on Integer32"""
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
        *(("ddsLineLoop", 3),
          ("ddsLocalLoop", 2),
          ("ddsNoLoop", 1),
          ("ddsOtherLoop", 4))
    )


_CtDDSLoopbackConfig_Type.__name__ = "Integer32"
_CtDDSLoopbackConfig_Object = MibTableColumn
ctDDSLoopbackConfig = _CtDDSLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 5),
    _CtDDSLoopbackConfig_Type()
)
ctDDSLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDDSLoopbackConfig.setStatus("mandatory")


class _CtDDSLineStatus_Type(Integer32):
    """Custom type ctDDSLineStatus based on Integer32"""
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
        *(("ddsLossOfSignal", 2),
          ("ddsNoAlarm", 1),
          ("ddsOutOfFrame", 4),
          ("ddsOutOfService", 3))
    )


_CtDDSLineStatus_Type.__name__ = "Integer32"
_CtDDSLineStatus_Object = MibTableColumn
ctDDSLineStatus = _CtDDSLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 6),
    _CtDDSLineStatus_Type()
)
ctDDSLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDDSLineStatus.setStatus("mandatory")


class _CtDDSTxClockSource_Type(Integer32):
    """Custom type ctDDSTxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddsLocalTiming", 2),
          ("ddsLoopTiming", 1),
          ("ddsThroughTiming", 3))
    )


_CtDDSTxClockSource_Type.__name__ = "Integer32"
_CtDDSTxClockSource_Object = MibTableColumn
ctDDSTxClockSource = _CtDDSTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 7),
    _CtDDSTxClockSource_Type()
)
ctDDSTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDDSTxClockSource.setStatus("mandatory")
_CtDDSPortInSpeed_Type = Integer32
_CtDDSPortInSpeed_Object = MibTableColumn
ctDDSPortInSpeed = _CtDDSPortInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 8),
    _CtDDSPortInSpeed_Type()
)
ctDDSPortInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDDSPortInSpeed.setStatus("mandatory")
_CtDDSPortOutSpeed_Type = Integer32
_CtDDSPortOutSpeed_Object = MibTableColumn
ctDDSPortOutSpeed = _CtDDSPortOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 5, 1, 1, 9),
    _CtDDSPortOutSpeed_Type()
)
ctDDSPortOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDDSPortOutSpeed.setStatus("mandatory")
_CtPPPExt_ObjectIdentity = ObjectIdentity
ctPPPExt = _CtPPPExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6)
)
_CtPppCountersTable_Object = MibTable
ctPppCountersTable = _CtPppCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ctPppCountersTable.setStatus("mandatory")
_CtPppCountersEntry_Object = MibTableRow
ctPppCountersEntry = _CtPppCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1, 1)
)
ctPppCountersEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctPppCountersIfIndex"),
)
if mibBuilder.loadTexts:
    ctPppCountersEntry.setStatus("mandatory")


class _CtPppCountersIfIndex_Type(Integer32):
    """Custom type ctPppCountersIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppCountersIfIndex_Type.__name__ = "Integer32"
_CtPppCountersIfIndex_Object = MibTableColumn
ctPppCountersIfIndex = _CtPppCountersIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1, 1, 1),
    _CtPppCountersIfIndex_Type()
)
ctPppCountersIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppCountersIfIndex.setStatus("mandatory")


class _CtPppCountersMaxTerminate_Type(Integer32):
    """Custom type ctPppCountersMaxTerminate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppCountersMaxTerminate_Type.__name__ = "Integer32"
_CtPppCountersMaxTerminate_Object = MibTableColumn
ctPppCountersMaxTerminate = _CtPppCountersMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1, 1, 2),
    _CtPppCountersMaxTerminate_Type()
)
ctPppCountersMaxTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppCountersMaxTerminate.setStatus("mandatory")


class _CtPppCountersMaxConfigure_Type(Integer32):
    """Custom type ctPppCountersMaxConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppCountersMaxConfigure_Type.__name__ = "Integer32"
_CtPppCountersMaxConfigure_Object = MibTableColumn
ctPppCountersMaxConfigure = _CtPppCountersMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1, 1, 3),
    _CtPppCountersMaxConfigure_Type()
)
ctPppCountersMaxConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppCountersMaxConfigure.setStatus("mandatory")


class _CtPppCountersMaxFailure_Type(Integer32):
    """Custom type ctPppCountersMaxFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppCountersMaxFailure_Type.__name__ = "Integer32"
_CtPppCountersMaxFailure_Object = MibTableColumn
ctPppCountersMaxFailure = _CtPppCountersMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1, 1, 4),
    _CtPppCountersMaxFailure_Type()
)
ctPppCountersMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppCountersMaxFailure.setStatus("mandatory")


class _CtPppCountersRestartTimer_Type(Integer32):
    """Custom type ctPppCountersRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppCountersRestartTimer_Type.__name__ = "Integer32"
_CtPppCountersRestartTimer_Object = MibTableColumn
ctPppCountersRestartTimer = _CtPppCountersRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 1, 1, 5),
    _CtPppCountersRestartTimer_Type()
)
ctPppCountersRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppCountersRestartTimer.setStatus("mandatory")
_CtPppLcpExtTable_Object = MibTable
ctPppLcpExtTable = _CtPppLcpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2)
)
if mibBuilder.loadTexts:
    ctPppLcpExtTable.setStatus("mandatory")
_CtPppLcpExtEntry_Object = MibTableRow
ctPppLcpExtEntry = _CtPppLcpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1)
)
ctPppLcpExtEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctPppLcpExtIfIndex"),
)
if mibBuilder.loadTexts:
    ctPppLcpExtEntry.setStatus("mandatory")


class _CtPppLcpExtIfIndex_Type(Integer32):
    """Custom type ctPppLcpExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppLcpExtIfIndex_Type.__name__ = "Integer32"
_CtPppLcpExtIfIndex_Object = MibTableColumn
ctPppLcpExtIfIndex = _CtPppLcpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 1),
    _CtPppLcpExtIfIndex_Type()
)
ctPppLcpExtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtIfIndex.setStatus("mandatory")


class _CtPppLcpExtAuthenticationProt_Type(Integer32):
    """Custom type ctPppLcpExtAuthenticationProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_CtPppLcpExtAuthenticationProt_Type.__name__ = "Integer32"
_CtPppLcpExtAuthenticationProt_Object = MibTableColumn
ctPppLcpExtAuthenticationProt = _CtPppLcpExtAuthenticationProt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 2),
    _CtPppLcpExtAuthenticationProt_Type()
)
ctPppLcpExtAuthenticationProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPppLcpExtAuthenticationProt.setStatus("mandatory")


class _CtPppLcpExtQualityProt_Type(Integer32):
    """Custom type ctPppLcpExtQualityProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lqr", 2),
          ("none", 1))
    )


_CtPppLcpExtQualityProt_Type.__name__ = "Integer32"
_CtPppLcpExtQualityProt_Object = MibTableColumn
ctPppLcpExtQualityProt = _CtPppLcpExtQualityProt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 3),
    _CtPppLcpExtQualityProt_Type()
)
ctPppLcpExtQualityProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtQualityProt.setStatus("mandatory")


class _CtPppLcpExtPFC_Type(Integer32):
    """Custom type ctPppLcpExtPFC based on Integer32"""
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


_CtPppLcpExtPFC_Type.__name__ = "Integer32"
_CtPppLcpExtPFC_Object = MibTableColumn
ctPppLcpExtPFC = _CtPppLcpExtPFC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 4),
    _CtPppLcpExtPFC_Type()
)
ctPppLcpExtPFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtPFC.setStatus("mandatory")


class _CtPppLcpExtACFC_Type(Integer32):
    """Custom type ctPppLcpExtACFC based on Integer32"""
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


_CtPppLcpExtACFC_Type.__name__ = "Integer32"
_CtPppLcpExtACFC_Object = MibTableColumn
ctPppLcpExtACFC = _CtPppLcpExtACFC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 5),
    _CtPppLcpExtACFC_Type()
)
ctPppLcpExtACFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtACFC.setStatus("mandatory")


class _CtPppLcpExtSelfDescribePadding_Type(Integer32):
    """Custom type ctPppLcpExtSelfDescribePadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CtPppLcpExtSelfDescribePadding_Type.__name__ = "Integer32"
_CtPppLcpExtSelfDescribePadding_Object = MibTableColumn
ctPppLcpExtSelfDescribePadding = _CtPppLcpExtSelfDescribePadding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 6),
    _CtPppLcpExtSelfDescribePadding_Type()
)
ctPppLcpExtSelfDescribePadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtSelfDescribePadding.setStatus("mandatory")


class _CtPppLcpExtCallback_Type(Integer32):
    """Custom type ctPppLcpExtCallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CtPppLcpExtCallback_Type.__name__ = "Integer32"
_CtPppLcpExtCallback_Object = MibTableColumn
ctPppLcpExtCallback = _CtPppLcpExtCallback_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 7),
    _CtPppLcpExtCallback_Type()
)
ctPppLcpExtCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtCallback.setStatus("mandatory")


class _CtPppLcpExtCompoundFrames_Type(Integer32):
    """Custom type ctPppLcpExtCompoundFrames based on Integer32"""
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


_CtPppLcpExtCompoundFrames_Type.__name__ = "Integer32"
_CtPppLcpExtCompoundFrames_Object = MibTableColumn
ctPppLcpExtCompoundFrames = _CtPppLcpExtCompoundFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 8),
    _CtPppLcpExtCompoundFrames_Type()
)
ctPppLcpExtCompoundFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtCompoundFrames.setStatus("mandatory")


class _CtPppLcpExtMru_Type(Integer32):
    """Custom type ctPppLcpExtMru based on Integer32"""
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


_CtPppLcpExtMru_Type.__name__ = "Integer32"
_CtPppLcpExtMru_Object = MibTableColumn
ctPppLcpExtMru = _CtPppLcpExtMru_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 9),
    _CtPppLcpExtMru_Type()
)
ctPppLcpExtMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMru.setStatus("mandatory")


class _CtPppLcpExtAccm_Type(Integer32):
    """Custom type ctPppLcpExtAccm based on Integer32"""
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


_CtPppLcpExtAccm_Type.__name__ = "Integer32"
_CtPppLcpExtAccm_Object = MibTableColumn
ctPppLcpExtAccm = _CtPppLcpExtAccm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 10),
    _CtPppLcpExtAccm_Type()
)
ctPppLcpExtAccm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtAccm.setStatus("mandatory")


class _CtPppLcpExtEchoRequest_Type(Integer32):
    """Custom type ctPppLcpExtEchoRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtPppLcpExtEchoRequest_Type.__name__ = "Integer32"
_CtPppLcpExtEchoRequest_Object = MibTableColumn
ctPppLcpExtEchoRequest = _CtPppLcpExtEchoRequest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 11),
    _CtPppLcpExtEchoRequest_Type()
)
ctPppLcpExtEchoRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtEchoRequest.setStatus("mandatory")


class _CtPppLcpExtReplyCounter_Type(Integer32):
    """Custom type ctPppLcpExtReplyCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtPppLcpExtReplyCounter_Type.__name__ = "Integer32"
_CtPppLcpExtReplyCounter_Object = MibTableColumn
ctPppLcpExtReplyCounter = _CtPppLcpExtReplyCounter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 12),
    _CtPppLcpExtReplyCounter_Type()
)
ctPppLcpExtReplyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPppLcpExtReplyCounter.setStatus("mandatory")


class _CtPppLcpExtMpCapable_Type(Integer32):
    """Custom type ctPppLcpExtMpCapable based on Integer32"""
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


_CtPppLcpExtMpCapable_Type.__name__ = "Integer32"
_CtPppLcpExtMpCapable_Object = MibTableColumn
ctPppLcpExtMpCapable = _CtPppLcpExtMpCapable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 2, 1, 13),
    _CtPppLcpExtMpCapable_Type()
)
ctPppLcpExtMpCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpCapable.setStatus("mandatory")
_CtPppBncpExtTable_Object = MibTable
ctPppBncpExtTable = _CtPppBncpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 3)
)
if mibBuilder.loadTexts:
    ctPppBncpExtTable.setStatus("mandatory")
_CtPppBncpExtEntry_Object = MibTableRow
ctPppBncpExtEntry = _CtPppBncpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 3, 1)
)
ctPppBncpExtEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctPppBncpExtIfIndex"),
)
if mibBuilder.loadTexts:
    ctPppBncpExtEntry.setStatus("mandatory")


class _CtPppBncpExtIfIndex_Type(Integer32):
    """Custom type ctPppBncpExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppBncpExtIfIndex_Type.__name__ = "Integer32"
_CtPppBncpExtIfIndex_Object = MibTableColumn
ctPppBncpExtIfIndex = _CtPppBncpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 3, 1, 1),
    _CtPppBncpExtIfIndex_Type()
)
ctPppBncpExtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppBncpExtIfIndex.setStatus("mandatory")


class _CtPppBncpExtCrcStatus_Type(Integer32):
    """Custom type ctPppBncpExtCrcStatus based on Integer32"""
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


_CtPppBncpExtCrcStatus_Type.__name__ = "Integer32"
_CtPppBncpExtCrcStatus_Object = MibTableColumn
ctPppBncpExtCrcStatus = _CtPppBncpExtCrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 3, 1, 2),
    _CtPppBncpExtCrcStatus_Type()
)
ctPppBncpExtCrcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppBncpExtCrcStatus.setStatus("mandatory")
_CtPppMpExtTable_Object = MibTable
ctPppMpExtTable = _CtPppMpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4)
)
if mibBuilder.loadTexts:
    ctPppMpExtTable.setStatus("mandatory")
_CtPppMpExtEntry_Object = MibTableRow
ctPppMpExtEntry = _CtPppMpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1)
)
ctPppMpExtEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctPppMpExtIfIndex"),
)
if mibBuilder.loadTexts:
    ctPppMpExtEntry.setStatus("mandatory")


class _CtPppMpExtIfIndex_Type(Integer32):
    """Custom type ctPppMpExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtPppMpExtIfIndex_Type.__name__ = "Integer32"
_CtPppMpExtIfIndex_Object = MibTableColumn
ctPppMpExtIfIndex = _CtPppMpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 1),
    _CtPppMpExtIfIndex_Type()
)
ctPppMpExtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppMpExtIfIndex.setStatus("mandatory")


class _CtPppLcpExtMpLUT_Type(Integer32):
    """Custom type ctPppLcpExtMpLUT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CtPppLcpExtMpLUT_Type.__name__ = "Integer32"
_CtPppLcpExtMpLUT_Object = MibTableColumn
ctPppLcpExtMpLUT = _CtPppLcpExtMpLUT_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 2),
    _CtPppLcpExtMpLUT_Type()
)
ctPppLcpExtMpLUT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpLUT.setStatus("mandatory")


class _CtPppLcpExtMpHistoryTime_Type(Integer32):
    """Custom type ctPppLcpExtMpHistoryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtPppLcpExtMpHistoryTime_Type.__name__ = "Integer32"
_CtPppLcpExtMpHistoryTime_Object = MibTableColumn
ctPppLcpExtMpHistoryTime = _CtPppLcpExtMpHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 3),
    _CtPppLcpExtMpHistoryTime_Type()
)
ctPppLcpExtMpHistoryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpHistoryTime.setStatus("mandatory")


class _CtPppLcpExtMpMoreBW_Type(Integer32):
    """Custom type ctPppLcpExtMpMoreBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtPppLcpExtMpMoreBW_Type.__name__ = "Integer32"
_CtPppLcpExtMpMoreBW_Object = MibTableColumn
ctPppLcpExtMpMoreBW = _CtPppLcpExtMpMoreBW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 4),
    _CtPppLcpExtMpMoreBW_Type()
)
ctPppLcpExtMpMoreBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpMoreBW.setStatus("mandatory")


class _CtPppLcpExtMpLessBW_Type(Integer32):
    """Custom type ctPppLcpExtMpLessBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtPppLcpExtMpLessBW_Type.__name__ = "Integer32"
_CtPppLcpExtMpLessBW_Object = MibTableColumn
ctPppLcpExtMpLessBW = _CtPppLcpExtMpLessBW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 5),
    _CtPppLcpExtMpLessBW_Type()
)
ctPppLcpExtMpLessBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpLessBW.setStatus("mandatory")


class _CtPppLcpExtMpMaxChannels_Type(Integer32):
    """Custom type ctPppLcpExtMpMaxChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtPppLcpExtMpMaxChannels_Type.__name__ = "Integer32"
_CtPppLcpExtMpMaxChannels_Object = MibTableColumn
ctPppLcpExtMpMaxChannels = _CtPppLcpExtMpMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 6),
    _CtPppLcpExtMpMaxChannels_Type()
)
ctPppLcpExtMpMaxChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpMaxChannels.setStatus("mandatory")


class _CtPppLcpExtMpChannelsToAdd_Type(Integer32):
    """Custom type ctPppLcpExtMpChannelsToAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtPppLcpExtMpChannelsToAdd_Type.__name__ = "Integer32"
_CtPppLcpExtMpChannelsToAdd_Object = MibTableColumn
ctPppLcpExtMpChannelsToAdd = _CtPppLcpExtMpChannelsToAdd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 7),
    _CtPppLcpExtMpChannelsToAdd_Type()
)
ctPppLcpExtMpChannelsToAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpChannelsToAdd.setStatus("mandatory")


class _CtPppLcpExtMpChannelsToRemove_Type(Integer32):
    """Custom type ctPppLcpExtMpChannelsToRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CtPppLcpExtMpChannelsToRemove_Type.__name__ = "Integer32"
_CtPppLcpExtMpChannelsToRemove_Object = MibTableColumn
ctPppLcpExtMpChannelsToRemove = _CtPppLcpExtMpChannelsToRemove_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 4, 1, 8),
    _CtPppLcpExtMpChannelsToRemove_Type()
)
ctPppLcpExtMpChannelsToRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppLcpExtMpChannelsToRemove.setStatus("mandatory")
_CtPppEcpExtTable_Object = MibTable
ctPppEcpExtTable = _CtPppEcpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 5)
)
if mibBuilder.loadTexts:
    ctPppEcpExtTable.setStatus("mandatory")
_CtPppEcpExtEntry_Object = MibTableRow
ctPppEcpExtEntry = _CtPppEcpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 5, 1)
)
ctPppEcpExtEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctPppEcpExtIfIndex"),
)
if mibBuilder.loadTexts:
    ctPppEcpExtEntry.setStatus("mandatory")


class _CtPppEcpExtIfIndex_Type(Integer32):
    """Custom type ctPppEcpExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CtPppEcpExtIfIndex_Type.__name__ = "Integer32"
_CtPppEcpExtIfIndex_Object = MibTableColumn
ctPppEcpExtIfIndex = _CtPppEcpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 5, 1, 1),
    _CtPppEcpExtIfIndex_Type()
)
ctPppEcpExtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppEcpExtIfIndex.setStatus("mandatory")


class _CtPppEcpKey_Type(DisplayString):
    """Custom type ctPppEcpKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_CtPppEcpKey_Type.__name__ = "DisplayString"
_CtPppEcpKey_Object = MibTableColumn
ctPppEcpKey = _CtPppEcpKey_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 5, 1, 2),
    _CtPppEcpKey_Type()
)
ctPppEcpKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppEcpKey.setStatus("mandatory")


class _CtPppEcpIV_Type(DisplayString):
    """Custom type ctPppEcpIV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CtPppEcpIV_Type.__name__ = "DisplayString"
_CtPppEcpIV_Object = MibTableColumn
ctPppEcpIV = _CtPppEcpIV_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 6, 5, 1, 3),
    _CtPppEcpIV_Type()
)
ctPppEcpIV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPppEcpIV.setStatus("mandatory")
_CtWanalyzer_ObjectIdentity = ObjectIdentity
ctWanalyzer = _CtWanalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7)
)
_CtWanalyzerTable_Object = MibTable
ctWanalyzerTable = _CtWanalyzerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ctWanalyzerTable.setStatus("mandatory")
_CtWanalyzerEntry_Object = MibTableRow
ctWanalyzerEntry = _CtWanalyzerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1)
)
ctWanalyzerEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctWanalyzerIfIndex"),
)
if mibBuilder.loadTexts:
    ctWanalyzerEntry.setStatus("mandatory")


class _CtWanalyzerIfIndex_Type(Integer32):
    """Custom type ctWanalyzerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtWanalyzerIfIndex_Type.__name__ = "Integer32"
_CtWanalyzerIfIndex_Object = MibTableColumn
ctWanalyzerIfIndex = _CtWanalyzerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 1),
    _CtWanalyzerIfIndex_Type()
)
ctWanalyzerIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanalyzerIfIndex.setStatus("mandatory")


class _CtWanalyzerEnabled_Type(Integer32):
    """Custom type ctWanalyzerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtWanalyzerEnabled_Type.__name__ = "Integer32"
_CtWanalyzerEnabled_Object = MibTableColumn
ctWanalyzerEnabled = _CtWanalyzerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 2),
    _CtWanalyzerEnabled_Type()
)
ctWanalyzerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanalyzerEnabled.setStatus("mandatory")
_CtWanalyzerMaxEntries_Type = Integer32
_CtWanalyzerMaxEntries_Object = MibTableColumn
ctWanalyzerMaxEntries = _CtWanalyzerMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 3),
    _CtWanalyzerMaxEntries_Type()
)
ctWanalyzerMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanalyzerMaxEntries.setStatus("mandatory")
_CtWanalyzerClearAll_Type = Integer32
_CtWanalyzerClearAll_Object = MibTableColumn
ctWanalyzerClearAll = _CtWanalyzerClearAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 4),
    _CtWanalyzerClearAll_Type()
)
ctWanalyzerClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanalyzerClearAll.setStatus("mandatory")
_CtWanalyzerClearInterface_Type = Integer32
_CtWanalyzerClearInterface_Object = MibTableColumn
ctWanalyzerClearInterface = _CtWanalyzerClearInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 5),
    _CtWanalyzerClearInterface_Type()
)
ctWanalyzerClearInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanalyzerClearInterface.setStatus("mandatory")
_CtWanalyzerDisplayInterface_Type = Integer32
_CtWanalyzerDisplayInterface_Object = MibTableColumn
ctWanalyzerDisplayInterface = _CtWanalyzerDisplayInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 6),
    _CtWanalyzerDisplayInterface_Type()
)
ctWanalyzerDisplayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctWanalyzerDisplayInterface.setStatus("mandatory")
_CtWanalyzerCurrEntries_Type = Integer32
_CtWanalyzerCurrEntries_Object = MibTableColumn
ctWanalyzerCurrEntries = _CtWanalyzerCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 1, 1, 7),
    _CtWanalyzerCurrEntries_Type()
)
ctWanalyzerCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctWanalyzerCurrEntries.setStatus("mandatory")
_WanalyzerMessageTable_Object = MibTable
wanalyzerMessageTable = _WanalyzerMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2)
)
if mibBuilder.loadTexts:
    wanalyzerMessageTable.setStatus("mandatory")
_WanalyzerEntry_Object = MibTableRow
wanalyzerEntry = _WanalyzerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2, 1)
)
wanalyzerEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "wanMessageIndex"),
)
if mibBuilder.loadTexts:
    wanalyzerEntry.setStatus("mandatory")
_WanMessageIndex_Type = Integer32
_WanMessageIndex_Object = MibTableColumn
wanMessageIndex = _WanMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2, 1, 1),
    _WanMessageIndex_Type()
)
wanMessageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanMessageIndex.setStatus("mandatory")
_WanMessageInterfaceIndex_Type = Integer32
_WanMessageInterfaceIndex_Object = MibTableColumn
wanMessageInterfaceIndex = _WanMessageInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2, 1, 2),
    _WanMessageInterfaceIndex_Type()
)
wanMessageInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanMessageInterfaceIndex.setStatus("mandatory")


class _WanMessageDate_Type(DisplayString):
    """Custom type wanMessageDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WanMessageDate_Type.__name__ = "DisplayString"
_WanMessageDate_Object = MibTableColumn
wanMessageDate = _WanMessageDate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2, 1, 3),
    _WanMessageDate_Type()
)
wanMessageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanMessageDate.setStatus("mandatory")


class _WanMessageTime_Type(DisplayString):
    """Custom type wanMessageTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WanMessageTime_Type.__name__ = "DisplayString"
_WanMessageTime_Object = MibTableColumn
wanMessageTime = _WanMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2, 1, 4),
    _WanMessageTime_Type()
)
wanMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanMessageTime.setStatus("mandatory")


class _WanMessageCode_Type(Integer32):
    """Custom type wanMessageCode based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              538,
              539,
              540,
              541,
              542,
              543,
              544,
              1000,
              1001,
              1002,
              1003,
              1500,
              1501,
              1502,
              1503,
              1504,
              1505,
              1506,
              1507,
              1508,
              1509,
              1510)
        )
    )
    namedValues = NamedValues(
        *(("frDcpDictionaryQuotaExceeded", 544),
          ("frDcpMode1ControlPacketReceived", 532),
          ("frDcpMode1DataPacketReceived", 533),
          ("frDcpMode1Disabled", 531),
          ("frDcpMode1Initializing", 530),
          ("frDcpMode1Operational", 538),
          ("frDcpMode1RequestReceived", 535),
          ("frDcpMode1RequestSent", 534),
          ("frDcpMode1ResponseReceived", 537),
          ("frDcpMode1ResponseSent", 536),
          ("frDcpMode1TimerExpired", 539),
          ("frDcpMode2ControlPacketReceived", 540),
          ("frDcpResetAckSent", 543),
          ("frDcpResetPacketSent", 541),
          ("frDcpResetTimerExpired", 542),
          ("frGotBadQ922Header", 501),
          ("frGotBadSnapPacket", 510),
          ("frGotBadUi", 509),
          ("frGotCllmPacket", 502),
          ("frGotLmiPacket", 500),
          ("frInactiveReceivedPacket", 503),
          ("frLinkDown", 512),
          ("frLinkUp", 511),
          ("frLmiAsynchronousStatus", 522),
          ("frLmiBadPvcStatusLength", 524),
          ("frLmiGotAnsiReportType", 518),
          ("frLmiGotFullStatusReport", 519),
          ("frLmiGotKeepAliveMessage", 520),
          ("frLmiGotQ933AReportType", 523),
          ("frLmiSentFullStatusEnquiry", 515),
          ("frLmiSentKeepAliveMessage", 516),
          ("frLmiStarted", 513),
          ("frLmiStatusEnquiryReceived", 529),
          ("frLmiStatusResponseReceived", 517),
          ("frLmiStopped", 514),
          ("frLmiT391PollFailed", 527),
          ("frLmiT391PollSucceeded", 528),
          ("frLmiT391TimeoutFs", 525),
          ("frLmiT391TimeoutSe", 526),
          ("frLmiUnsolicitedKeepAlive", 521),
          ("frReceivedNlpidIpPacket", 504),
          ("frReceivedXidPacket", 507),
          ("frSentXidPacket", 505),
          ("frSentXidResponse", 506),
          ("frXidTimerExpired", 508),
          ("isdnActivateConnection", 1002),
          ("isdnDeactivateConnection", 1003),
          ("isdnRemoteConnectionDown", 1001),
          ("isdnRemoteConnectionUp", 1000),
          ("multilinkMpAddBW", 1501),
          ("multilinkMpLinkUp", 1500),
          ("multilinkMpReceivedBeginningFragment", 1507),
          ("multilinkMpReceivedCompleteMessage", 1510),
          ("multilinkMpReceivedEndFragment", 1509),
          ("multilinkMpReceivedMiddleFragment", 1508),
          ("multilinkMpRemoveBW", 1502),
          ("multilinkMpSentBeginningFragment", 1503),
          ("multilinkMpSentCompleteMessage", 1506),
          ("multilinkMpSentEndFragment", 1505),
          ("multilinkMpSentMiddleFragment", 1504),
          ("pppAuthentication", 2),
          ("pppBncpAckRcvdState", 40),
          ("pppBncpAckSentState", 41),
          ("pppBncpBridgeIdRcvNak", 47),
          ("pppBncpBridgeIdRcvRej", 48),
          ("pppBncpBridgeIdRcvReq", 46),
          ("pppBncpBridgeIdXmitReq", 49),
          ("pppBncpClosedState", 35),
          ("pppBncpClosingState", 37),
          ("pppBncpEthernetMacType", 43),
          ("pppBncpFddiMacType", 45),
          ("pppBncpIllegalAction", 23),
          ("pppBncpInitialState", 33),
          ("pppBncpInitializeRestartCount", 7),
          ("pppBncpLanIdRcvNak", 59),
          ("pppBncpLanIdRcvRej", 60),
          ("pppBncpLanIdRcvReq", 58),
          ("pppBncpLanIdXmitReq", 61),
          ("pppBncpMacSelectRcvNak", 51),
          ("pppBncpMacSelectRcvRej", 52),
          ("pppBncpMacSelectRcvReq", 50),
          ("pppBncpMacSelectXmitReq", 53),
          ("pppBncpOpenedState", 42),
          ("pppBncpRcvConfReqBad", 10),
          ("pppBncpRcvConfReqGood", 9),
          ("pppBncpReceiveCodeRejectCatastrophic", 17),
          ("pppBncpReceiveCodeRejectPermitted", 16),
          ("pppBncpReceiveConfigureAck", 11),
          ("pppBncpReceiveConfigureNak", 12),
          ("pppBncpReceiveConfigureReject", 13),
          ("pppBncpReceiveDiscardRequest", 21),
          ("pppBncpReceiveEchoReply", 20),
          ("pppBncpReceiveEchoRequest", 19),
          ("pppBncpReceiveProtocolRejectPermitted", 18),
          ("pppBncpReceiveTerminateAck", 15),
          ("pppBncpReceiveTerminateRequest", 14),
          ("pppBncpReceiveUnknownCode", 22),
          ("pppBncpReqSentState", 39),
          ("pppBncpSendCodeReject", 30),
          ("pppBncpSendConfigureAck", 25),
          ("pppBncpSendConfigureNak", 26),
          ("pppBncpSendConfigureReject", 27),
          ("pppBncpSendConfigureRequest", 24),
          ("pppBncpSendEchoReply", 32),
          ("pppBncpSendProtocolReject", 31),
          ("pppBncpSendTerminateAck", 29),
          ("pppBncpSendTerminateRequest", 28),
          ("pppBncpStartingState", 34),
          ("pppBncpStoppedState", 36),
          ("pppBncpStoppingState", 38),
          ("pppBncpThisLayerDown", 6),
          ("pppBncpThisLayerFinished", 4),
          ("pppBncpThisLayerStart", 3),
          ("pppBncpThisLayerUp", 5),
          ("pppBncpTinygramRcvNak", 55),
          ("pppBncpTinygramRcvRej", 56),
          ("pppBncpTinygramRcvReq", 54),
          ("pppBncpTinygramXmitReq", 57),
          ("pppBncpTokenRingMacType", 44),
          ("pppBncpZeroRestartCount", 8),
          ("pppCcpAckRcvdState", 99),
          ("pppCcpAckSentState", 100),
          ("pppCcpBsdLzwRcvNak", 139),
          ("pppCcpBsdLzwRcvRej", 140),
          ("pppCcpBsdLzwRcvReq", 138),
          ("pppCcpBsdLzwXmitReq", 141),
          ("pppCcpClosedState", 94),
          ("pppCcpClosingState", 96),
          ("pppCcpGandalfFzaRcvNak", 131),
          ("pppCcpGandalfFzaRcvRej", 132),
          ("pppCcpGandalfFzaRcvReq", 130),
          ("pppCcpGandalfFzaXmitReq", 133),
          ("pppCcpHpPpcRcvNak", 119),
          ("pppCcpHpPpcRcvRej", 120),
          ("pppCcpHpPpcRcvReq", 118),
          ("pppCcpHpPpcXmitReq", 121),
          ("pppCcpIllegalAction", 82),
          ("pppCcpInitialState", 92),
          ("pppCcpInitializeRestartCount", 66),
          ("pppCcpMsPpcRcvNak", 127),
          ("pppCcpMsPpcRcvRej", 128),
          ("pppCcpMsPpcRcvReq", 126),
          ("pppCcpMsPpcXmitReq", 129),
          ("pppCcpOpenedState", 101),
          ("pppCcpPredictorType1RcvNak", 107),
          ("pppCcpPredictorType1RcvRej", 108),
          ("pppCcpPredictorType1RcvReq", 106),
          ("pppCcpPredictorType1XmitReq", 109),
          ("pppCcpPredictorType2RcvNak", 111),
          ("pppCcpPredictorType2RcvRej", 112),
          ("pppCcpPredictorType2RcvReq", 110),
          ("pppCcpPredictorType2XmitReq", 113),
          ("pppCcpProprietaryCompRcvNak", 103),
          ("pppCcpProprietaryCompRcvRej", 104),
          ("pppCcpProprietaryCompRcvReq", 102),
          ("pppCcpProprietaryCompXmitReq", 105),
          ("pppCcpPuddleJumperRcvNak", 115),
          ("pppCcpPuddleJumperRcvRej", 116),
          ("pppCcpPuddleJumperRcvReq", 114),
          ("pppCcpPuddleJumperXmitReq", 117),
          ("pppCcpRcvConfReqBad", 69),
          ("pppCcpRcvConfReqGood", 68),
          ("pppCcpReceiveCodeRejectCatastrophic", 76),
          ("pppCcpReceiveCodeRejectPermitted", 75),
          ("pppCcpReceiveConfigureAck", 70),
          ("pppCcpReceiveConfigureNak", 71),
          ("pppCcpReceiveConfigureReject", 72),
          ("pppCcpReceiveDiscardRequest", 80),
          ("pppCcpReceiveEchoReply", 79),
          ("pppCcpReceiveEchoRequest", 78),
          ("pppCcpReceiveProtocolRejectPermitted", 77),
          ("pppCcpReceiveTerminateAck", 74),
          ("pppCcpReceiveTerminateRequest", 73),
          ("pppCcpReceiveUnknownCode", 81),
          ("pppCcpReqSentState", 98),
          ("pppCcpSendCodeReject", 89),
          ("pppCcpSendConfigureAck", 84),
          ("pppCcpSendConfigureNak", 85),
          ("pppCcpSendConfigureReject", 86),
          ("pppCcpSendConfigureRequest", 83),
          ("pppCcpSendEchoReply", 91),
          ("pppCcpSendProtocolReject", 90),
          ("pppCcpSendTerminateAck", 88),
          ("pppCcpSendTerminateRequest", 87),
          ("pppCcpStacLzsRcvNak", 123),
          ("pppCcpStacLzsRcvRej", 124),
          ("pppCcpStacLzsRcvReq", 122),
          ("pppCcpStacLzsXmitReq", 125),
          ("pppCcpStackDcpRcvNak", 143),
          ("pppCcpStackDcpRcvRej", 144),
          ("pppCcpStackDcpRcvReq", 142),
          ("pppCcpStackDcpXmitReq", 145),
          ("pppCcpStartingState", 93),
          ("pppCcpStoppedState", 95),
          ("pppCcpStoppingState", 97),
          ("pppCcpThisLayerDown", 65),
          ("pppCcpThisLayerFinished", 63),
          ("pppCcpThisLayerStart", 62),
          ("pppCcpThisLayerUp", 64),
          ("pppCcpV42bisRcvNak", 135),
          ("pppCcpV42bisRcvRej", 136),
          ("pppCcpV42bisRcvReq", 134),
          ("pppCcpV42bisXmitReq", 137),
          ("pppCcpZeroRestartCount", 67),
          ("pppChapChallengeReceived", 146),
          ("pppChapChallengeSent", 152),
          ("pppChapFailureReceived", 149),
          ("pppChapFailureSent", 151),
          ("pppChapResponseReceived", 147),
          ("pppChapResponseSent", 153),
          ("pppChapSuccessReceived", 148),
          ("pppChapSuccessSent", 150),
          ("pppIpcpAckRcvdState", 191),
          ("pppIpcpAckSentState", 192),
          ("pppIpcpClosedState", 186),
          ("pppIpcpClosingState", 188),
          ("pppIpcpCompressionTypeRcvNak", 200),
          ("pppIpcpCompressionTypeRcvRej", 199),
          ("pppIpcpCompressionTypeRcvReq", 198),
          ("pppIpcpCompressionTypeXmitReq", 201),
          ("pppIpcpIllegalAction", 174),
          ("pppIpcpInitialState", 184),
          ("pppIpcpInitializeRestartCount", 158),
          ("pppIpcpIpAddressRcvNak", 195),
          ("pppIpcpIpAddressRcvRej", 196),
          ("pppIpcpIpAddressRcvReq", 194),
          ("pppIpcpIpAddressXmitReq", 197),
          ("pppIpcpOpenedState", 193),
          ("pppIpcpRcvConfReqBad", 161),
          ("pppIpcpRcvConfReqGood", 160),
          ("pppIpcpReceiveCodeRejectCatastrophic", 168),
          ("pppIpcpReceiveCodeRejectPermitted", 167),
          ("pppIpcpReceiveConfigureAck", 162),
          ("pppIpcpReceiveConfigureNak", 163),
          ("pppIpcpReceiveConfigureReject", 164),
          ("pppIpcpReceiveDiscardRequest", 172),
          ("pppIpcpReceiveEchoReply", 171),
          ("pppIpcpReceiveEchoRequest", 170),
          ("pppIpcpReceiveProtocolRejectPermitted", 169),
          ("pppIpcpReceiveTerminateAck", 166),
          ("pppIpcpReceiveTerminateRequest", 165),
          ("pppIpcpReceiveUnknownCode", 173),
          ("pppIpcpReqSentState", 190),
          ("pppIpcpSendCodeReject", 181),
          ("pppIpcpSendConfigureAck", 176),
          ("pppIpcpSendConfigureNak", 177),
          ("pppIpcpSendConfigureReject", 178),
          ("pppIpcpSendConfigureRequest", 175),
          ("pppIpcpSendEchoReply", 183),
          ("pppIpcpSendProtocolReject", 182),
          ("pppIpcpSendTerminateAck", 180),
          ("pppIpcpSendTerminateRequest", 179),
          ("pppIpcpStartingState", 185),
          ("pppIpcpStoppedState", 187),
          ("pppIpcpStoppingState", 189),
          ("pppIpcpThisLayerDown", 157),
          ("pppIpcpThisLayerFinished", 155),
          ("pppIpcpThisLayerStart", 154),
          ("pppIpcpThisLayerUp", 156),
          ("pppIpcpZeroRestartCount", 159),
          ("pppIpxcpAckRcvdState", 239),
          ("pppIpxcpAckSentState", 240),
          ("pppIpxcpClosedState", 234),
          ("pppIpxcpClosingState", 236),
          ("pppIpxcpCompressionProtocolRcvNak", 243),
          ("pppIpxcpCompressionProtocolRcvRej", 244),
          ("pppIpxcpCompressionProtocolRcvReq", 242),
          ("pppIpxcpCompressionProtocolXmitReq", 245),
          ("pppIpxcpConfigurationCompleteRcvNak", 263),
          ("pppIpxcpConfigurationCompleteRcvRej", 264),
          ("pppIpxcpConfigurationCompleteRcvReq", 262),
          ("pppIpxcpConfigurationCompleteXmitReq", 265),
          ("pppIpxcpIllegalAction", 222),
          ("pppIpxcpInitialState", 232),
          ("pppIpxcpInitializeRestartCount", 206),
          ("pppIpxcpNetworkNumberRcvNak", 247),
          ("pppIpxcpNetworkNumberRcvRej", 248),
          ("pppIpxcpNetworkNumberRcvReq", 246),
          ("pppIpxcpNetworkNumberXmitReq", 249),
          ("pppIpxcpNodeNumberRcvNak", 251),
          ("pppIpxcpNodeNumberRcvRej", 252),
          ("pppIpxcpNodeNumberRcvReq", 250),
          ("pppIpxcpNodeNumberXmitReq", 253),
          ("pppIpxcpOpenedState", 241),
          ("pppIpxcpRcvConfReqBad", 209),
          ("pppIpxcpRcvConfReqGood", 208),
          ("pppIpxcpReceiveCodeRejectCatastrophic", 216),
          ("pppIpxcpReceiveCodeRejectPermitted", 215),
          ("pppIpxcpReceiveConfigureAck", 210),
          ("pppIpxcpReceiveConfigureNak", 211),
          ("pppIpxcpReceiveConfigureReject", 212),
          ("pppIpxcpReceiveDiscardRequest", 220),
          ("pppIpxcpReceiveEchoReply", 219),
          ("pppIpxcpReceiveEchoRequest", 218),
          ("pppIpxcpReceiveProtocolRejectPermitted", 217),
          ("pppIpxcpReceiveTerminateAck", 214),
          ("pppIpxcpReceiveUnknownCode", 221),
          ("pppIpxcpReqSentState", 238),
          ("pppIpxcpRouterNameRcvNak", 259),
          ("pppIpxcpRouterNameRcvRej", 260),
          ("pppIpxcpRouterNameRcvReq", 258),
          ("pppIpxcpRouterNameXmitReq", 261),
          ("pppIpxcpRoutingProtocolRcvNak", 255),
          ("pppIpxcpRoutingProtocolRcvRej", 256),
          ("pppIpxcpRoutingProtocolRcvReq", 254),
          ("pppIpxcpRoutingProtocolXmitReq", 257),
          ("pppIpxcpSendCodeReject", 229),
          ("pppIpxcpSendConfigureAck", 224),
          ("pppIpxcpSendConfigureNak", 225),
          ("pppIpxcpSendConfigureReject", 226),
          ("pppIpxcpSendConfigureRequest", 223),
          ("pppIpxcpSendEchoReply", 231),
          ("pppIpxcpSendProtocolReject", 230),
          ("pppIpxcpSendTerminateAck", 228),
          ("pppIpxcpSendTerminateRequest", 227),
          ("pppIpxcpStartingState", 233),
          ("pppIpxcpStoppedState", 235),
          ("pppIpxcpStoppingState", 237),
          ("pppIpxcpThisLayerDown", 205),
          ("pppIpxcpThisLayerFinished", 203),
          ("pppIpxcpThisLayerStart", 202),
          ("pppIpxcpThisLayerUp", 204),
          ("pppIpxcpZeroRestartCount", 207),
          ("pppLcpAckRcvdState", 303),
          ("pppLcpAckSentState", 304),
          ("pppLcpAddrCompRcvNak", 331),
          ("pppLcpAddrCompRcvRej", 332),
          ("pppLcpAddrCompRcvReq", 330),
          ("pppLcpAddrCompXmitReq", 333),
          ("pppLcpAsyncCharMapRcvNak", 311),
          ("pppLcpAsyncCharMapRcvRej", 312),
          ("pppLcpAsyncCharMapRcvReq", 310),
          ("pppLcpAsyncCharMapXmitReq", 313),
          ("pppLcpAuthenticationRcvNak", 315),
          ("pppLcpAuthenticationRcvRej", 316),
          ("pppLcpAuthenticationRcvReq", 314),
          ("pppLcpAuthenticationXmitReq", 317),
          ("pppLcpCallbackRcvNak", 347),
          ("pppLcpCallbackRcvRej", 348),
          ("pppLcpCallbackRcvReq", 346),
          ("pppLcpCallbackXmitReq", 349),
          ("pppLcpClosedState", 298),
          ("pppLcpClosingState", 300),
          ("pppLcpCompoundFramesRcvNak", 343),
          ("pppLcpCompoundFramesRcvRej", 344),
          ("pppLcpCompoundFramesRcvReq", 342),
          ("pppLcpCompoundFramesXmitReq", 345),
          ("pppLcpFcs32BitRcvNak", 335),
          ("pppLcpFcs32BitRcvRej", 336),
          ("pppLcpFcs32BitRcvReq", 334),
          ("pppLcpFcs32BitXmitReq", 337),
          ("pppLcpIllegalAction", 286),
          ("pppLcpInitialState", 296),
          ("pppLcpInitializeRestartCount", 270),
          ("pppLcpLinkQualityRcvNak", 323),
          ("pppLcpLinkQualityRcvRej", 324),
          ("pppLcpLinkQualityRcvReq", 322),
          ("pppLcpLinkQualityXmitReq", 325),
          ("pppLcpMagicNumberRcvNak", 319),
          ("pppLcpMagicNumberRcvRej", 320),
          ("pppLcpMagicNumberRcvReq", 318),
          ("pppLcpMagicNumberXmitReq", 321),
          ("pppLcpMruRcvNak", 307),
          ("pppLcpMruRcvRej", 308),
          ("pppLcpMruRcvReq", 306),
          ("pppLcpMruXmitReq", 309),
          ("pppLcpOpenedState", 305),
          ("pppLcpProtCompRcvNak", 327),
          ("pppLcpProtCompRcvRej", 328),
          ("pppLcpProtCompRcvReq", 326),
          ("pppLcpProtCompXmitReq", 329),
          ("pppLcpRcvConfReqBad", 273),
          ("pppLcpRcvConfReqGood", 272),
          ("pppLcpReceiveCodeRejectCatastrophic", 280),
          ("pppLcpReceiveCodeRejectPermitted", 279),
          ("pppLcpReceiveConfigureAck", 274),
          ("pppLcpReceiveConfigureNak", 275),
          ("pppLcpReceiveConfigureReject", 276),
          ("pppLcpReceiveDiscardRequest", 284),
          ("pppLcpReceiveEchoReply", 283),
          ("pppLcpReceiveEchoRequest", 282),
          ("pppLcpReceiveProtocolReject", 281),
          ("pppLcpReceiveTerminateAck", 278),
          ("pppLcpReceiveTerminateRequest", 277),
          ("pppLcpReceiveUnknownCode", 285),
          ("pppLcpReqSentState", 302),
          ("pppLcpSelfDescPaddingRcvNak", 339),
          ("pppLcpSelfDescPaddingRcvRej", 340),
          ("pppLcpSelfDescPaddingRcvReq", 338),
          ("pppLcpSelfDescPaddingXmitReq", 341),
          ("pppLcpSendCodeReject", 293),
          ("pppLcpSendConfigureAck", 288),
          ("pppLcpSendConfigureNak", 289),
          ("pppLcpSendConfigureReject", 290),
          ("pppLcpSendConfigureRequest", 287),
          ("pppLcpSendEchoReply", 295),
          ("pppLcpSendProtocolReject", 294),
          ("pppLcpSendTerminateAck", 292),
          ("pppLcpSendTerminateRequest", 291),
          ("pppLcpStartingState", 297),
          ("pppLcpStoppedState", 299),
          ("pppLcpStoppingState", 301),
          ("pppLcpThisLayerDown", 269),
          ("pppLcpThisLayerFinished", 267),
          ("pppLcpThisLayerStart", 266),
          ("pppLcpThisLayerUp", 268),
          ("pppLcpZeroRestartCount", 271),
          ("pppLexAckRcvdState", 387),
          ("pppLexAckSentState", 388),
          ("pppLexClosedState", 382),
          ("pppLexClosingState", 384),
          ("pppLexIllegalAction", 370),
          ("pppLexInitialState", 380),
          ("pppLexInitializeRestartCount", 354),
          ("pppLexMacAddressRcvNak", 399),
          ("pppLexMacAddressRcvRej", 400),
          ("pppLexMacAddressRcvReq", 398),
          ("pppLexMacAddressXmitReq", 401),
          ("pppLexMacRelayRcvNak", 403),
          ("pppLexMacRelayRcvRej", 404),
          ("pppLexMacRelayRcvReq", 402),
          ("pppLexMacRelayXmitReq", 405),
          ("pppLexMacTypeSelectRcvNak", 391),
          ("pppLexMacTypeSelectRcvRej", 392),
          ("pppLexMacTypeSelectRcvReq", 390),
          ("pppLexMacTypeSelectXmitReq", 393),
          ("pppLexOpenedState", 389),
          ("pppLexRcvConfReqBad", 357),
          ("pppLexRcvConfReqGood", 356),
          ("pppLexReceiveCodeRejectCatastrophic", 364),
          ("pppLexReceiveCodeRejectPermitted", 363),
          ("pppLexReceiveConfigureAck", 358),
          ("pppLexReceiveConfigureNak", 359),
          ("pppLexReceiveConfigureReject", 360),
          ("pppLexReceiveDiscardRequest", 368),
          ("pppLexReceiveEchoReply", 367),
          ("pppLexReceiveEchoRequest", 366),
          ("pppLexReceiveProtocolRejectPermitted", 365),
          ("pppLexReceiveTerminateAck", 362),
          ("pppLexReceiveTerminateRequest", 361),
          ("pppLexReceiveUnknownCode", 369),
          ("pppLexReqSentState", 386),
          ("pppLexSendCodeReject", 377),
          ("pppLexSendConfigureAck", 372),
          ("pppLexSendConfigureNak", 373),
          ("pppLexSendConfigureReject", 374),
          ("pppLexSendConfigureRequest", 371),
          ("pppLexSendEchoReply", 379),
          ("pppLexSendProtocolReject", 378),
          ("pppLexSendTerminateAck", 376),
          ("pppLexSendTerminateRequest", 375),
          ("pppLexStartingState", 381),
          ("pppLexStatisticsRequestRcvReq", 406),
          ("pppLexStoppedState", 383),
          ("pppLexStoppingState", 385),
          ("pppLexThisLayerDown", 353),
          ("pppLexThisLayerFinished", 351),
          ("pppLexThisLayerStart", 350),
          ("pppLexThisLayerUp", 352),
          ("pppLexTinygramCompressRcvNak", 395),
          ("pppLexTinygramCompressRcvRej", 396),
          ("pppLexTinygramCompressRcvReq", 394),
          ("pppLexTinygramCompressXmitReq", 397),
          ("pppLexZeroRestartCount", 355),
          ("pppLinkDead", 409),
          ("pppLinkEstablishment", 410),
          ("pppLinkTermination", 411),
          ("pppLqrReceived", 408),
          ("pppLqrSent", 407),
          ("pppNetworkLayerPhase", 412),
          ("pppPapAuthenticateAckReceived", 414),
          ("pppPapAuthenticateAckSent", 417),
          ("pppPapAuthenticateNakReceived", 415),
          ("pppPapAuthenticateNakSent", 418),
          ("pppPapAuthenticateReqReceived", 413),
          ("pppPapAuthenticateReqSent", 416),
          ("wanalyzerLastMessageRepeated", 1))
    )


_WanMessageCode_Type.__name__ = "Integer32"
_WanMessageCode_Object = MibTableColumn
wanMessageCode = _WanMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 7, 2, 1, 5),
    _WanMessageCode_Type()
)
wanMessageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanMessageCode.setStatus("mandatory")
_CtDs1Alarms_ObjectIdentity = ObjectIdentity
ctDs1Alarms = _CtDs1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8)
)
_Ds1AlarmsGlobalConfigGroup_ObjectIdentity = ObjectIdentity
ds1AlarmsGlobalConfigGroup = _Ds1AlarmsGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1)
)


class _Ds1AlarmGlobalAdmin_Type(Integer32):
    """Custom type ds1AlarmGlobalAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ds1AlarmGlobalAdmin_Type.__name__ = "Integer32"
_Ds1AlarmGlobalAdmin_Object = MibScalar
ds1AlarmGlobalAdmin = _Ds1AlarmGlobalAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 1),
    _Ds1AlarmGlobalAdmin_Type()
)
ds1AlarmGlobalAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalAdmin.setStatus("mandatory")


class _Ds1AlarmGlobalAutoRecovery_Type(Integer32):
    """Custom type ds1AlarmGlobalAutoRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ds1AlarmGlobalAutoRecovery_Type.__name__ = "Integer32"
_Ds1AlarmGlobalAutoRecovery_Object = MibScalar
ds1AlarmGlobalAutoRecovery = _Ds1AlarmGlobalAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 2),
    _Ds1AlarmGlobalAutoRecovery_Type()
)
ds1AlarmGlobalAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalAutoRecovery.setStatus("mandatory")


class _Ds1AlarmGlobalTrapEnable_Type(Integer32):
    """Custom type ds1AlarmGlobalTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ds1AlarmGlobalTrapEnable_Type.__name__ = "Integer32"
_Ds1AlarmGlobalTrapEnable_Object = MibScalar
ds1AlarmGlobalTrapEnable = _Ds1AlarmGlobalTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 3),
    _Ds1AlarmGlobalTrapEnable_Type()
)
ds1AlarmGlobalTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalTrapEnable.setStatus("mandatory")


class _Ds1AlarmGlobalESCount_Type(Integer32):
    """Custom type ds1AlarmGlobalESCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Ds1AlarmGlobalESCount_Type.__name__ = "Integer32"
_Ds1AlarmGlobalESCount_Object = MibScalar
ds1AlarmGlobalESCount = _Ds1AlarmGlobalESCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 4),
    _Ds1AlarmGlobalESCount_Type()
)
ds1AlarmGlobalESCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalESCount.setStatus("mandatory")


class _Ds1AlarmGlobalESInterval_Type(Integer32):
    """Custom type ds1AlarmGlobalESInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmGlobalESInterval_Type.__name__ = "Integer32"
_Ds1AlarmGlobalESInterval_Object = MibScalar
ds1AlarmGlobalESInterval = _Ds1AlarmGlobalESInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 5),
    _Ds1AlarmGlobalESInterval_Type()
)
ds1AlarmGlobalESInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalESInterval.setStatus("mandatory")


class _Ds1AlarmGlobalBPVErrorRate_Type(Integer32):
    """Custom type ds1AlarmGlobalBPVErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_Ds1AlarmGlobalBPVErrorRate_Type.__name__ = "Integer32"
_Ds1AlarmGlobalBPVErrorRate_Object = MibScalar
ds1AlarmGlobalBPVErrorRate = _Ds1AlarmGlobalBPVErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 6),
    _Ds1AlarmGlobalBPVErrorRate_Type()
)
ds1AlarmGlobalBPVErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalBPVErrorRate.setStatus("mandatory")


class _Ds1AlarmGlobalBPVInterval_Type(Integer32):
    """Custom type ds1AlarmGlobalBPVInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmGlobalBPVInterval_Type.__name__ = "Integer32"
_Ds1AlarmGlobalBPVInterval_Object = MibScalar
ds1AlarmGlobalBPVInterval = _Ds1AlarmGlobalBPVInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 7),
    _Ds1AlarmGlobalBPVInterval_Type()
)
ds1AlarmGlobalBPVInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalBPVInterval.setStatus("mandatory")


class _Ds1AlarmGlobalManualRecovery_Type(Integer32):
    """Custom type ds1AlarmGlobalManualRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recover", 1)
    )


_Ds1AlarmGlobalManualRecovery_Type.__name__ = "Integer32"
_Ds1AlarmGlobalManualRecovery_Object = MibScalar
ds1AlarmGlobalManualRecovery = _Ds1AlarmGlobalManualRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 1, 8),
    _Ds1AlarmGlobalManualRecovery_Type()
)
ds1AlarmGlobalManualRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmGlobalManualRecovery.setStatus("mandatory")
_Ds1AlarmConfigTable_Object = MibTable
ds1AlarmConfigTable = _Ds1AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2)
)
if mibBuilder.loadTexts:
    ds1AlarmConfigTable.setStatus("mandatory")
_Ds1AlarmConfigEntry_Object = MibTableRow
ds1AlarmConfigEntry = _Ds1AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1)
)
ds1AlarmConfigEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ds1PhysNum"),
)
if mibBuilder.loadTexts:
    ds1AlarmConfigEntry.setStatus("mandatory")
_Ds1PhysNum_Type = Integer32
_Ds1PhysNum_Object = MibTableColumn
ds1PhysNum = _Ds1PhysNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 1),
    _Ds1PhysNum_Type()
)
ds1PhysNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PhysNum.setStatus("mandatory")


class _Ds1AlarmAdmin_Type(Integer32):
    """Custom type ds1AlarmAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ds1AlarmAdmin_Type.__name__ = "Integer32"
_Ds1AlarmAdmin_Object = MibTableColumn
ds1AlarmAdmin = _Ds1AlarmAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 2),
    _Ds1AlarmAdmin_Type()
)
ds1AlarmAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmAdmin.setStatus("mandatory")


class _Ds1AlarmAutoRecovery_Type(Integer32):
    """Custom type ds1AlarmAutoRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ds1AlarmAutoRecovery_Type.__name__ = "Integer32"
_Ds1AlarmAutoRecovery_Object = MibTableColumn
ds1AlarmAutoRecovery = _Ds1AlarmAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 3),
    _Ds1AlarmAutoRecovery_Type()
)
ds1AlarmAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmAutoRecovery.setStatus("mandatory")


class _Ds1AlarmTrapEnable_Type(Integer32):
    """Custom type ds1AlarmTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ds1AlarmTrapEnable_Type.__name__ = "Integer32"
_Ds1AlarmTrapEnable_Object = MibTableColumn
ds1AlarmTrapEnable = _Ds1AlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 4),
    _Ds1AlarmTrapEnable_Type()
)
ds1AlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmTrapEnable.setStatus("mandatory")


class _Ds1AlarmESCount_Type(Integer32):
    """Custom type ds1AlarmESCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Ds1AlarmESCount_Type.__name__ = "Integer32"
_Ds1AlarmESCount_Object = MibTableColumn
ds1AlarmESCount = _Ds1AlarmESCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 5),
    _Ds1AlarmESCount_Type()
)
ds1AlarmESCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmESCount.setStatus("mandatory")


class _Ds1AlarmESInterval_Type(Integer32):
    """Custom type ds1AlarmESInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmESInterval_Type.__name__ = "Integer32"
_Ds1AlarmESInterval_Object = MibTableColumn
ds1AlarmESInterval = _Ds1AlarmESInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 6),
    _Ds1AlarmESInterval_Type()
)
ds1AlarmESInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmESInterval.setStatus("mandatory")


class _Ds1AlarmBPVErrorRate_Type(Integer32):
    """Custom type ds1AlarmBPVErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_Ds1AlarmBPVErrorRate_Type.__name__ = "Integer32"
_Ds1AlarmBPVErrorRate_Object = MibTableColumn
ds1AlarmBPVErrorRate = _Ds1AlarmBPVErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 7),
    _Ds1AlarmBPVErrorRate_Type()
)
ds1AlarmBPVErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmBPVErrorRate.setStatus("mandatory")


class _Ds1AlarmBPVInterval_Type(Integer32):
    """Custom type ds1AlarmBPVInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Ds1AlarmBPVInterval_Type.__name__ = "Integer32"
_Ds1AlarmBPVInterval_Object = MibTableColumn
ds1AlarmBPVInterval = _Ds1AlarmBPVInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 8),
    _Ds1AlarmBPVInterval_Type()
)
ds1AlarmBPVInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmBPVInterval.setStatus("mandatory")


class _Ds1AlarmManualRecovery_Type(Integer32):
    """Custom type ds1AlarmManualRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recover", 1)
    )


_Ds1AlarmManualRecovery_Type.__name__ = "Integer32"
_Ds1AlarmManualRecovery_Object = MibTableColumn
ds1AlarmManualRecovery = _Ds1AlarmManualRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 8, 2, 1, 9),
    _Ds1AlarmManualRecovery_Type()
)
ds1AlarmManualRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AlarmManualRecovery.setStatus("mandatory")
_CtIPPQFilters_ObjectIdentity = ObjectIdentity
ctIPPQFilters = _CtIPPQFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9)
)
_IpPQConfigGroup_ObjectIdentity = ObjectIdentity
ipPQConfigGroup = _IpPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 1)
)


class _IpPQAdmin_Type(Integer32):
    """Custom type ipPQAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpPQAdmin_Type.__name__ = "Integer32"
_IpPQAdmin_Object = MibScalar
ipPQAdmin = _IpPQAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 1, 1),
    _IpPQAdmin_Type()
)
ipPQAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPQAdmin.setStatus("mandatory")
_IPPQMaxEntries_Type = Integer32
_IPPQMaxEntries_Object = MibScalar
iPPQMaxEntries = _IPPQMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 1, 2),
    _IPPQMaxEntries_Type()
)
iPPQMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPPQMaxEntries.setStatus("mandatory")
_IPPQNumEntries_Type = Integer32
_IPPQNumEntries_Object = MibScalar
iPPQNumEntries = _IPPQNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 1, 3),
    _IPPQNumEntries_Type()
)
iPPQNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPPQNumEntries.setStatus("mandatory")
_IPPQAddAddress_Type = IpAddress
_IPPQAddAddress_Object = MibScalar
iPPQAddAddress = _IPPQAddAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 1, 4),
    _IPPQAddAddress_Type()
)
iPPQAddAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPPQAddAddress.setStatus("mandatory")
_IPPQDelAddress_Type = IpAddress
_IPPQDelAddress_Object = MibScalar
iPPQDelAddress = _IPPQDelAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 1, 5),
    _IPPQDelAddress_Type()
)
iPPQDelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPPQDelAddress.setStatus("mandatory")
_IpPQAddressTable_Object = MibTable
ipPQAddressTable = _IpPQAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 2)
)
if mibBuilder.loadTexts:
    ipPQAddressTable.setStatus("mandatory")
_IpPQAddressEntry_Object = MibTableRow
ipPQAddressEntry = _IpPQAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 2, 1)
)
ipPQAddressEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ipPQAddressId"),
)
if mibBuilder.loadTexts:
    ipPQAddressEntry.setStatus("mandatory")


class _IpPQAddressId_Type(Integer32):
    """Custom type ipPQAddressId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpPQAddressId_Type.__name__ = "Integer32"
_IpPQAddressId_Object = MibTableColumn
ipPQAddressId = _IpPQAddressId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 2, 1, 1),
    _IpPQAddressId_Type()
)
ipPQAddressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPQAddressId.setStatus("mandatory")
_IpPQIPAddress_Type = IpAddress
_IpPQIPAddress_Object = MibTableColumn
ipPQIPAddress = _IpPQIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 9, 2, 1, 2),
    _IpPQIPAddress_Type()
)
ipPQIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPQIPAddress.setStatus("mandatory")
_CtDs3Ext_ObjectIdentity = ObjectIdentity
ctDs3Ext = _CtDs3Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 10)
)
_CtDs3ExtensionsTable_Object = MibTable
ctDs3ExtensionsTable = _CtDs3ExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 10, 1)
)
if mibBuilder.loadTexts:
    ctDs3ExtensionsTable.setStatus("mandatory")
_CtDs3ExtensionsEntry_Object = MibTableRow
ctDs3ExtensionsEntry = _CtDs3ExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 10, 1, 1)
)
ctDs3ExtensionsEntry.setIndexNames(
    (0, "CTRON-REMOTE-ACCESS-MIB", "ctDs3ExtensionsEntryIndex"),
)
if mibBuilder.loadTexts:
    ctDs3ExtensionsEntry.setStatus("mandatory")
_CtDs3ExtensionsEntryIndex_Type = Integer32
_CtDs3ExtensionsEntryIndex_Object = MibTableColumn
ctDs3ExtensionsEntryIndex = _CtDs3ExtensionsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 10, 1, 1, 1),
    _CtDs3ExtensionsEntryIndex_Type()
)
ctDs3ExtensionsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs3ExtensionsEntryIndex.setStatus("mandatory")
_CtDs3ExtensionsNumInterfaces_Type = Integer32
_CtDs3ExtensionsNumInterfaces_Object = MibTableColumn
ctDs3ExtensionsNumInterfaces = _CtDs3ExtensionsNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 10, 1, 1, 2),
    _CtDs3ExtensionsNumInterfaces_Type()
)
ctDs3ExtensionsNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDs3ExtensionsNumInterfaces.setStatus("mandatory")


class _CtDs3ExtensionsLineBuildOut_Type(Integer32):
    """Custom type ctDs3ExtensionsLineBuildOut based on Integer32"""
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
        *(("a255to450feet", 3),
          ("unknown", 1),
          ("zeroto255feet", 2))
    )


_CtDs3ExtensionsLineBuildOut_Type.__name__ = "Integer32"
_CtDs3ExtensionsLineBuildOut_Object = MibTableColumn
ctDs3ExtensionsLineBuildOut = _CtDs3ExtensionsLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2, 10, 1, 1, 3),
    _CtDs3ExtensionsLineBuildOut_Type()
)
ctDs3ExtensionsLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDs3ExtensionsLineBuildOut.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-REMOTE-ACCESS-MIB",
    **{"Index": Index,
       "DLCI": DLCI,
       "cabletron": cabletron,
       "mibs": mibs,
       "ctron": ctron,
       "ctDataLink": ctDataLink,
       "ctronWan": ctronWan,
       "ctRemoteAccess": ctRemoteAccess,
       "ctRemoteConnection": ctRemoteConnection,
       "ctRemNumConnections": ctRemNumConnections,
       "ctRemPhysPortTable": ctRemPhysPortTable,
       "ctRemPhysPortEntry": ctRemPhysPortEntry,
       "ctRemConnectionIndex": ctRemConnectionIndex,
       "ctRemPhysPortType": ctRemPhysPortType,
       "ctRemPhysPortSpecificMib": ctRemPhysPortSpecificMib,
       "ctRemPhysPortProtMgrType": ctRemPhysPortProtMgrType,
       "ctRemPhysPortProtMgrIfaceNum": ctRemPhysPortProtMgrIfaceNum,
       "ctRemPhysPortWanIfaceNum": ctRemPhysPortWanIfaceNum,
       "ctRemPhysPortProtMgrMaxIfos": ctRemPhysPortProtMgrMaxIfos,
       "ctRemPhysPortProtMgrIfaceList": ctRemPhysPortProtMgrIfaceList,
       "ctRemPhysAlarmTimeOut": ctRemPhysAlarmTimeOut,
       "ctRemPhysWpimType": ctRemPhysWpimType,
       "ctRemInterfaceTable": ctRemInterfaceTable,
       "ctRemInterfaceEntry": ctRemInterfaceEntry,
       "ctRemIntEntIfIndex": ctRemIntEntIfIndex,
       "ctRemIntEntCompression": ctRemIntEntCompression,
       "ctRemIntEntCompRatio": ctRemIntEntCompRatio,
       "ctRemIntEntCompStatus": ctRemIntEntCompStatus,
       "ctRemIntEntMTU": ctRemIntEntMTU,
       "ctRemIntEntCongestion": ctRemIntEntCongestion,
       "ctRemIntEntMaxProfiles": ctRemIntEntMaxProfiles,
       "ctRemIntEntTxIdleTimeout": ctRemIntEntTxIdleTimeout,
       "ctRemIntEntRxIdleTimeout": ctRemIntEntRxIdleTimeout,
       "ctRemIntEntCircuitName": ctRemIntEntCircuitName,
       "ctRemIntEntEncryption": ctRemIntEntEncryption,
       "ctRemIntEntEncryptStatus": ctRemIntEntEncryptStatus,
       "ctRemPrimaryInterfaceTable": ctRemPrimaryInterfaceTable,
       "ctRemPrimaryInterfaceEntry": ctRemPrimaryInterfaceEntry,
       "ctRemPriIntEntIfIndex": ctRemPriIntEntIfIndex,
       "ctRemPriIntEntConnectRetryInterval": ctRemPriIntEntConnectRetryInterval,
       "ctRemBackupInterfaceTable": ctRemBackupInterfaceTable,
       "ctRemBackupInterfaceEntry": ctRemBackupInterfaceEntry,
       "ctRemIntEntBackupIfIndex": ctRemIntEntBackupIfIndex,
       "ctRemIntEntBackupIfNum": ctRemIntEntBackupIfNum,
       "ctRemIntEntBackupIfInUseCnt": ctRemIntEntBackupIfInUseCnt,
       "ctRemIntEntBackupIfTimeToConnect": ctRemIntEntBackupIfTimeToConnect,
       "ctRemIntEntBackupIfTimeToDisconnect": ctRemIntEntBackupIfTimeToDisconnect,
       "ctRemIntEntBackupIfOverride": ctRemIntEntBackupIfOverride,
       "ctRemIntEntBackupConnectRetries": ctRemIntEntBackupConnectRetries,
       "ctRemIntEntBackupConnectRetryInterval": ctRemIntEntBackupConnectRetryInterval,
       "ctRemExtPhysPortTable": ctRemExtPhysPortTable,
       "ctRemExtPhysPortEntry": ctRemExtPhysPortEntry,
       "ctRemExtConnectionIndex": ctRemExtConnectionIndex,
       "ctRemExtProtMgrIndex": ctRemExtProtMgrIndex,
       "ctRemExtPhysPortProtMgrType": ctRemExtPhysPortProtMgrType,
       "ctRemExtPhysPortProtMgrEnable": ctRemExtPhysPortProtMgrEnable,
       "ctRemExtPhysPortProtMgrIfaceNum": ctRemExtPhysPortProtMgrIfaceNum,
       "ctRemExtPhysPortProtMgrMaxIfos": ctRemExtPhysPortProtMgrMaxIfos,
       "ctRemExtPhysPortProtMgrIfaceList": ctRemExtPhysPortProtMgrIfaceList,
       "ctRemExtPhysPortProtMgrChannelList": ctRemExtPhysPortProtMgrChannelList,
       "ctDs1Ext": ctDs1Ext,
       "ctDs1ExtensionsTable": ctDs1ExtensionsTable,
       "ctDs1ExtensionsEntry": ctDs1ExtensionsEntry,
       "ctDs1ExtensionsEntryIndex": ctDs1ExtensionsEntryIndex,
       "ctDs1ExtensionsNumInterfaces": ctDs1ExtensionsNumInterfaces,
       "ctDs1ExtensionsToggleFracTable": ctDs1ExtensionsToggleFracTable,
       "ctDs1ExtensionsLineBuildOut": ctDs1ExtensionsLineBuildOut,
       "ctDs1ExtensionsCFADuration": ctDs1ExtensionsCFADuration,
       "ctDs1ExtensionsDIEnable": ctDs1ExtensionsDIEnable,
       "ctDs1ExtensionsTotalValidIntervals": ctDs1ExtensionsTotalValidIntervals,
       "wanDs1ExtensionsBertTestMode": wanDs1ExtensionsBertTestMode,
       "wanDs1ExtensionsBertRun": wanDs1ExtensionsBertRun,
       "wanDs1ExtensionsBertCurrentResults": wanDs1ExtensionsBertCurrentResults,
       "wanDs1ExtensionsBertCumulativeResults": wanDs1ExtensionsBertCumulativeResults,
       "wanDs1ExtensionsBertPeakResults": wanDs1ExtensionsBertPeakResults,
       "wanDs1ExtensionsBertAverageResult": wanDs1ExtensionsBertAverageResult,
       "wanDs1ExtensionsBertTestPattern": wanDs1ExtensionsBertTestPattern,
       "wanDs1ExtensionsBertSamplePeriod": wanDs1ExtensionsBertSamplePeriod,
       "wanDs1ExtensionsBertNumPeriods": wanDs1ExtensionsBertNumPeriods,
       "wanDs1ExtensionsBertTestTraps": wanDs1ExtensionsBertTestTraps,
       "wanDs1ExtensionsBertDataStatus": wanDs1ExtensionsBertDataStatus,
       "ctDs1WanDriverTable": ctDs1WanDriverTable,
       "ctDs1WanDriverEntry": ctDs1WanDriverEntry,
       "ctDs1WanDriverEntryIndex": ctDs1WanDriverEntryIndex,
       "ctDs1WanDriverChannelIndex": ctDs1WanDriverChannelIndex,
       "ctDs1WanDriverLineCode": ctDs1WanDriverLineCode,
       "ctDs1WanDriverCRCBits": ctDs1WanDriverCRCBits,
       "ctRs232Ext": ctRs232Ext,
       "ctRs232ExtensionsTable": ctRs232ExtensionsTable,
       "ctRs232ExtensionsEntry": ctRs232ExtensionsEntry,
       "ctRs232ExtensionsEntryIndex": ctRs232ExtensionsEntryIndex,
       "ctRs232ExtensionsCTSEnable": ctRs232ExtensionsCTSEnable,
       "ctRs232ExtensionsDSREnable": ctRs232ExtensionsDSREnable,
       "ctRs232ExtensionsRTSEnable": ctRs232ExtensionsRTSEnable,
       "ctRs232ExtensionsDTREnable": ctRs232ExtensionsDTREnable,
       "ctFrDcp": ctFrDcp,
       "frDcpCircuitTable": frDcpCircuitTable,
       "frDcpCircuitEntry": frDcpCircuitEntry,
       "frDcpCircuitIfIndex": frDcpCircuitIfIndex,
       "frDcpCircuitDlci": frDcpCircuitDlci,
       "frDcpCircuitEnable": frDcpCircuitEnable,
       "frDcpCircuitStatus": frDcpCircuitStatus,
       "frDcpCircuitRatio": frDcpCircuitRatio,
       "ctDDSExt": ctDDSExt,
       "ctDDSConfigTable": ctDDSConfigTable,
       "ctDDSConfigEntry": ctDDSConfigEntry,
       "ctDDSLineIndex": ctDDSLineIndex,
       "ctDDSIfIndex": ctDDSIfIndex,
       "ctDDSLineMode": ctDDSLineMode,
       "ctDDSLineCoding": ctDDSLineCoding,
       "ctDDSLoopbackConfig": ctDDSLoopbackConfig,
       "ctDDSLineStatus": ctDDSLineStatus,
       "ctDDSTxClockSource": ctDDSTxClockSource,
       "ctDDSPortInSpeed": ctDDSPortInSpeed,
       "ctDDSPortOutSpeed": ctDDSPortOutSpeed,
       "ctPPPExt": ctPPPExt,
       "ctPppCountersTable": ctPppCountersTable,
       "ctPppCountersEntry": ctPppCountersEntry,
       "ctPppCountersIfIndex": ctPppCountersIfIndex,
       "ctPppCountersMaxTerminate": ctPppCountersMaxTerminate,
       "ctPppCountersMaxConfigure": ctPppCountersMaxConfigure,
       "ctPppCountersMaxFailure": ctPppCountersMaxFailure,
       "ctPppCountersRestartTimer": ctPppCountersRestartTimer,
       "ctPppLcpExtTable": ctPppLcpExtTable,
       "ctPppLcpExtEntry": ctPppLcpExtEntry,
       "ctPppLcpExtIfIndex": ctPppLcpExtIfIndex,
       "ctPppLcpExtAuthenticationProt": ctPppLcpExtAuthenticationProt,
       "ctPppLcpExtQualityProt": ctPppLcpExtQualityProt,
       "ctPppLcpExtPFC": ctPppLcpExtPFC,
       "ctPppLcpExtACFC": ctPppLcpExtACFC,
       "ctPppLcpExtSelfDescribePadding": ctPppLcpExtSelfDescribePadding,
       "ctPppLcpExtCallback": ctPppLcpExtCallback,
       "ctPppLcpExtCompoundFrames": ctPppLcpExtCompoundFrames,
       "ctPppLcpExtMru": ctPppLcpExtMru,
       "ctPppLcpExtAccm": ctPppLcpExtAccm,
       "ctPppLcpExtEchoRequest": ctPppLcpExtEchoRequest,
       "ctPppLcpExtReplyCounter": ctPppLcpExtReplyCounter,
       "ctPppLcpExtMpCapable": ctPppLcpExtMpCapable,
       "ctPppBncpExtTable": ctPppBncpExtTable,
       "ctPppBncpExtEntry": ctPppBncpExtEntry,
       "ctPppBncpExtIfIndex": ctPppBncpExtIfIndex,
       "ctPppBncpExtCrcStatus": ctPppBncpExtCrcStatus,
       "ctPppMpExtTable": ctPppMpExtTable,
       "ctPppMpExtEntry": ctPppMpExtEntry,
       "ctPppMpExtIfIndex": ctPppMpExtIfIndex,
       "ctPppLcpExtMpLUT": ctPppLcpExtMpLUT,
       "ctPppLcpExtMpHistoryTime": ctPppLcpExtMpHistoryTime,
       "ctPppLcpExtMpMoreBW": ctPppLcpExtMpMoreBW,
       "ctPppLcpExtMpLessBW": ctPppLcpExtMpLessBW,
       "ctPppLcpExtMpMaxChannels": ctPppLcpExtMpMaxChannels,
       "ctPppLcpExtMpChannelsToAdd": ctPppLcpExtMpChannelsToAdd,
       "ctPppLcpExtMpChannelsToRemove": ctPppLcpExtMpChannelsToRemove,
       "ctPppEcpExtTable": ctPppEcpExtTable,
       "ctPppEcpExtEntry": ctPppEcpExtEntry,
       "ctPppEcpExtIfIndex": ctPppEcpExtIfIndex,
       "ctPppEcpKey": ctPppEcpKey,
       "ctPppEcpIV": ctPppEcpIV,
       "ctWanalyzer": ctWanalyzer,
       "ctWanalyzerTable": ctWanalyzerTable,
       "ctWanalyzerEntry": ctWanalyzerEntry,
       "ctWanalyzerIfIndex": ctWanalyzerIfIndex,
       "ctWanalyzerEnabled": ctWanalyzerEnabled,
       "ctWanalyzerMaxEntries": ctWanalyzerMaxEntries,
       "ctWanalyzerClearAll": ctWanalyzerClearAll,
       "ctWanalyzerClearInterface": ctWanalyzerClearInterface,
       "ctWanalyzerDisplayInterface": ctWanalyzerDisplayInterface,
       "ctWanalyzerCurrEntries": ctWanalyzerCurrEntries,
       "wanalyzerMessageTable": wanalyzerMessageTable,
       "wanalyzerEntry": wanalyzerEntry,
       "wanMessageIndex": wanMessageIndex,
       "wanMessageInterfaceIndex": wanMessageInterfaceIndex,
       "wanMessageDate": wanMessageDate,
       "wanMessageTime": wanMessageTime,
       "wanMessageCode": wanMessageCode,
       "ctDs1Alarms": ctDs1Alarms,
       "ds1AlarmsGlobalConfigGroup": ds1AlarmsGlobalConfigGroup,
       "ds1AlarmGlobalAdmin": ds1AlarmGlobalAdmin,
       "ds1AlarmGlobalAutoRecovery": ds1AlarmGlobalAutoRecovery,
       "ds1AlarmGlobalTrapEnable": ds1AlarmGlobalTrapEnable,
       "ds1AlarmGlobalESCount": ds1AlarmGlobalESCount,
       "ds1AlarmGlobalESInterval": ds1AlarmGlobalESInterval,
       "ds1AlarmGlobalBPVErrorRate": ds1AlarmGlobalBPVErrorRate,
       "ds1AlarmGlobalBPVInterval": ds1AlarmGlobalBPVInterval,
       "ds1AlarmGlobalManualRecovery": ds1AlarmGlobalManualRecovery,
       "ds1AlarmConfigTable": ds1AlarmConfigTable,
       "ds1AlarmConfigEntry": ds1AlarmConfigEntry,
       "ds1PhysNum": ds1PhysNum,
       "ds1AlarmAdmin": ds1AlarmAdmin,
       "ds1AlarmAutoRecovery": ds1AlarmAutoRecovery,
       "ds1AlarmTrapEnable": ds1AlarmTrapEnable,
       "ds1AlarmESCount": ds1AlarmESCount,
       "ds1AlarmESInterval": ds1AlarmESInterval,
       "ds1AlarmBPVErrorRate": ds1AlarmBPVErrorRate,
       "ds1AlarmBPVInterval": ds1AlarmBPVInterval,
       "ds1AlarmManualRecovery": ds1AlarmManualRecovery,
       "ctIPPQFilters": ctIPPQFilters,
       "ipPQConfigGroup": ipPQConfigGroup,
       "ipPQAdmin": ipPQAdmin,
       "iPPQMaxEntries": iPPQMaxEntries,
       "iPPQNumEntries": iPPQNumEntries,
       "iPPQAddAddress": iPPQAddAddress,
       "iPPQDelAddress": iPPQDelAddress,
       "ipPQAddressTable": ipPQAddressTable,
       "ipPQAddressEntry": ipPQAddressEntry,
       "ipPQAddressId": ipPQAddressId,
       "ipPQIPAddress": ipPQIPAddress,
       "ctDs3Ext": ctDs3Ext,
       "ctDs3ExtensionsTable": ctDs3ExtensionsTable,
       "ctDs3ExtensionsEntry": ctDs3ExtensionsEntry,
       "ctDs3ExtensionsEntryIndex": ctDs3ExtensionsEntryIndex,
       "ctDs3ExtensionsNumInterfaces": ctDs3ExtensionsNumInterfaces,
       "ctDs3ExtensionsLineBuildOut": ctDs3ExtensionsLineBuildOut}
)
