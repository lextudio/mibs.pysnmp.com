# SNMP MIB module (ASCEND-MIBL2TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBL2TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:49 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mibl2TunnelGlobal_ObjectIdentity = ObjectIdentity
mibl2TunnelGlobal = _Mibl2TunnelGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 90)
)
_Mibl2TunnelGlobalTable_Object = MibTable
mibl2TunnelGlobalTable = _Mibl2TunnelGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1)
)
if mibBuilder.loadTexts:
    mibl2TunnelGlobalTable.setStatus("mandatory")
_Mibl2TunnelGlobalEntry_Object = MibTableRow
mibl2TunnelGlobalEntry = _Mibl2TunnelGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1)
)
mibl2TunnelGlobalEntry.setIndexNames(
    (0, "ASCEND-MIBL2TUNNEL-MIB", "l2TunnelGlobal-Index-o"),
)
if mibBuilder.loadTexts:
    mibl2TunnelGlobalEntry.setStatus("mandatory")
_L2TunnelGlobal_Index_o_Type = Integer32
_L2TunnelGlobal_Index_o_Object = MibScalar
l2TunnelGlobal_Index_o = _L2TunnelGlobal_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 1),
    _L2TunnelGlobal_Index_o_Type()
)
l2TunnelGlobal_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TunnelGlobal_Index_o.setStatus("mandatory")


class _L2TunnelGlobal_PptpEnabled_Type(Integer32):
    """Custom type l2TunnelGlobal_PptpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_PptpEnabled_Type.__name__ = "Integer32"
_L2TunnelGlobal_PptpEnabled_Object = MibScalar
l2TunnelGlobal_PptpEnabled = _L2TunnelGlobal_PptpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 2),
    _L2TunnelGlobal_PptpEnabled_Type()
)
l2TunnelGlobal_PptpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_PptpEnabled.setStatus("mandatory")


class _L2TunnelGlobal_ServerProfileRequired_Type(Integer32):
    """Custom type l2TunnelGlobal_ServerProfileRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_ServerProfileRequired_Type.__name__ = "Integer32"
_L2TunnelGlobal_ServerProfileRequired_Object = MibScalar
l2TunnelGlobal_ServerProfileRequired = _L2TunnelGlobal_ServerProfileRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 3),
    _L2TunnelGlobal_ServerProfileRequired_Type()
)
l2TunnelGlobal_ServerProfileRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_ServerProfileRequired.setStatus("mandatory")


class _L2TunnelGlobal_L2tpMode_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpMode based on Integer32"""
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
        *(("disabled", 1),
          ("lac", 2),
          ("lacAndLns", 4),
          ("lns", 3))
    )


_L2TunnelGlobal_L2tpMode_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpMode_Object = MibScalar
l2TunnelGlobal_L2tpMode = _L2TunnelGlobal_L2tpMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 4),
    _L2TunnelGlobal_L2tpMode_Type()
)
l2TunnelGlobal_L2tpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpMode.setStatus("mandatory")


class _L2TunnelGlobal_L2tpAuthEnabled_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpAuthEnabled_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpAuthEnabled_Object = MibScalar
l2TunnelGlobal_L2tpAuthEnabled = _L2TunnelGlobal_L2tpAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 5),
    _L2TunnelGlobal_L2tpAuthEnabled_Type()
)
l2TunnelGlobal_L2tpAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpAuthEnabled.setStatus("mandatory")
_L2TunnelGlobal_L2tpRxWindow_Type = Integer32
_L2TunnelGlobal_L2tpRxWindow_Object = MibScalar
l2TunnelGlobal_L2tpRxWindow = _L2TunnelGlobal_L2tpRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 6),
    _L2TunnelGlobal_L2tpRxWindow_Type()
)
l2TunnelGlobal_L2tpRxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpRxWindow.setStatus("mandatory")
_L2TunnelGlobal_MaxLnsClients_Type = Integer32
_L2TunnelGlobal_MaxLnsClients_Object = MibScalar
l2TunnelGlobal_MaxLnsClients = _L2TunnelGlobal_MaxLnsClients_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 7),
    _L2TunnelGlobal_MaxLnsClients_Type()
)
l2TunnelGlobal_MaxLnsClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_MaxLnsClients.setStatus("mandatory")
_L2TunnelGlobal_L2tpSystemName_Type = DisplayString
_L2TunnelGlobal_L2tpSystemName_Object = MibScalar
l2TunnelGlobal_L2tpSystemName = _L2TunnelGlobal_L2tpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 8),
    _L2TunnelGlobal_L2tpSystemName_Type()
)
l2TunnelGlobal_L2tpSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpSystemName.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_FirstRetryTimer_Type = Integer32
_L2TunnelGlobal_L2tpConfig_FirstRetryTimer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_FirstRetryTimer = _L2TunnelGlobal_L2tpConfig_FirstRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 9),
    _L2TunnelGlobal_L2tpConfig_FirstRetryTimer_Type()
)
l2TunnelGlobal_L2tpConfig_FirstRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_FirstRetryTimer.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_RetryCount_Type = Integer32
_L2TunnelGlobal_L2tpConfig_RetryCount_Object = MibScalar
l2TunnelGlobal_L2tpConfig_RetryCount = _L2TunnelGlobal_L2tpConfig_RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 10),
    _L2TunnelGlobal_L2tpConfig_RetryCount_Type()
)
l2TunnelGlobal_L2tpConfig_RetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_RetryCount.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_HelloTimer_Type = Integer32
_L2TunnelGlobal_L2tpConfig_HelloTimer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_HelloTimer = _L2TunnelGlobal_L2tpConfig_HelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 11),
    _L2TunnelGlobal_L2tpConfig_HelloTimer_Type()
)
l2TunnelGlobal_L2tpConfig_HelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_HelloTimer.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer_Type = Integer32
_L2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer = _L2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 12),
    _L2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer_Type()
)
l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_LacIncomingCallTimer_Type = Integer32
_L2TunnelGlobal_L2tpConfig_LacIncomingCallTimer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer = _L2TunnelGlobal_L2tpConfig_LacIncomingCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 13),
    _L2TunnelGlobal_L2tpConfig_LacIncomingCallTimer_Type()
)
l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer_Type = Integer32
_L2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer = _L2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 14),
    _L2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer_Type()
)
l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_BaseUdpPort_Type = Integer32
_L2TunnelGlobal_L2tpConfig_BaseUdpPort_Object = MibScalar
l2TunnelGlobal_L2tpConfig_BaseUdpPort = _L2TunnelGlobal_L2tpConfig_BaseUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 15),
    _L2TunnelGlobal_L2tpConfig_BaseUdpPort_Type()
)
l2TunnelGlobal_L2tpConfig_BaseUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_BaseUdpPort.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_DialoutAuthLns_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_DialoutAuthLns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpConfig_DialoutAuthLns_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_DialoutAuthLns_Object = MibScalar
l2TunnelGlobal_L2tpConfig_DialoutAuthLns = _L2TunnelGlobal_L2tpConfig_DialoutAuthLns_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 16),
    _L2TunnelGlobal_L2tpConfig_DialoutAuthLns_Type()
)
l2TunnelGlobal_L2tpConfig_DialoutAuthLns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_DialoutAuthLns.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_DialoutSendProfileName_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_DialoutSendProfileName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpConfig_DialoutSendProfileName_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_DialoutSendProfileName_Object = MibScalar
l2TunnelGlobal_L2tpConfig_DialoutSendProfileName = _L2TunnelGlobal_L2tpConfig_DialoutSendProfileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 17),
    _L2TunnelGlobal_L2tpConfig_DialoutSendProfileName_Type()
)
l2TunnelGlobal_L2tpConfig_DialoutSendProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_DialoutSendProfileName.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decimalCallSerialNumber", 2),
          ("hexadecimalCallSerialNumber", 3),
          ("normal", 1))
    )


_L2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding_Object = MibScalar
l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding = _L2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 18),
    _L2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding_Type()
)
l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding.setStatus("mandatory")


class _L2TunnelGlobal_L2fMode_Type(Integer32):
    """Custom type l2TunnelGlobal_L2fMode based on Integer32"""
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
        *(("disabled", 1),
          ("gw", 3),
          ("nas", 2),
          ("nasAndGw", 4))
    )


_L2TunnelGlobal_L2fMode_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2fMode_Object = MibScalar
l2TunnelGlobal_L2fMode = _L2TunnelGlobal_L2fMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 20),
    _L2TunnelGlobal_L2fMode_Type()
)
l2TunnelGlobal_L2fMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2fMode.setStatus("mandatory")
_L2TunnelGlobal_L2fSystemName_Type = DisplayString
_L2TunnelGlobal_L2fSystemName_Object = MibScalar
l2TunnelGlobal_L2fSystemName = _L2TunnelGlobal_L2fSystemName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 21),
    _L2TunnelGlobal_L2fSystemName_Type()
)
l2TunnelGlobal_L2fSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2fSystemName.setStatus("mandatory")
_L2TunnelGlobal_L2fRetryCount_Type = Integer32
_L2TunnelGlobal_L2fRetryCount_Object = MibScalar
l2TunnelGlobal_L2fRetryCount = _L2TunnelGlobal_L2fRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 22),
    _L2TunnelGlobal_L2fRetryCount_Type()
)
l2TunnelGlobal_L2fRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2fRetryCount.setStatus("mandatory")
_L2TunnelGlobal_L2fRetryInterval_Type = Integer32
_L2TunnelGlobal_L2fRetryInterval_Object = MibScalar
l2TunnelGlobal_L2fRetryInterval = _L2TunnelGlobal_L2fRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 23),
    _L2TunnelGlobal_L2fRetryInterval_Type()
)
l2TunnelGlobal_L2fRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2fRetryInterval.setStatus("mandatory")


class _L2TunnelGlobal_L2fTunnelSecret_Type(Integer32):
    """Custom type l2TunnelGlobal_L2fTunnelSecret based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("distinctTunnelSecrets", 2),
          ("eitherSharedOrDistinctTunnelSecret", 3),
          ("sharedTunnelSecret", 1))
    )


_L2TunnelGlobal_L2fTunnelSecret_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2fTunnelSecret_Object = MibScalar
l2TunnelGlobal_L2fTunnelSecret = _L2TunnelGlobal_L2fTunnelSecret_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 24),
    _L2TunnelGlobal_L2fTunnelSecret_Type()
)
l2TunnelGlobal_L2fTunnelSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2fTunnelSecret.setStatus("mandatory")


class _L2TunnelGlobal_L2fIgnoreMidSequence_Type(Integer32):
    """Custom type l2TunnelGlobal_L2fIgnoreMidSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2fIgnoreMidSequence_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2fIgnoreMidSequence_Object = MibScalar
l2TunnelGlobal_L2fIgnoreMidSequence = _L2TunnelGlobal_L2fIgnoreMidSequence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 25),
    _L2TunnelGlobal_L2fIgnoreMidSequence_Type()
)
l2TunnelGlobal_L2fIgnoreMidSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2fIgnoreMidSequence.setStatus("mandatory")


class _L2TunnelGlobal_Action_o_Type(Integer32):
    """Custom type l2TunnelGlobal_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_L2TunnelGlobal_Action_o_Type.__name__ = "Integer32"
_L2TunnelGlobal_Action_o_Object = MibScalar
l2TunnelGlobal_Action_o = _L2TunnelGlobal_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 26),
    _L2TunnelGlobal_Action_o_Type()
)
l2TunnelGlobal_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_Action_o.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_VerifyRemoteHostName_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpConfig_VerifyRemoteHostName_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_VerifyRemoteHostName_Object = MibScalar
l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName = _L2TunnelGlobal_L2tpConfig_VerifyRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 27),
    _L2TunnelGlobal_L2tpConfig_VerifyRemoteHostName_Type()
)
l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_DefaultTunnelServer_Type = DisplayString
_L2TunnelGlobal_L2tpConfig_DefaultTunnelServer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_DefaultTunnelServer = _L2TunnelGlobal_L2tpConfig_DefaultTunnelServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 28),
    _L2TunnelGlobal_L2tpConfig_DefaultTunnelServer_Type()
)
l2TunnelGlobal_L2tpConfig_DefaultTunnelServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_DefaultTunnelServer.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup_Object = MibScalar
l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup = _L2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 29),
    _L2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup_Type()
)
l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator_Object = MibScalar
l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator = _L2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 30),
    _L2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator_Type()
)
l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_LnsNasPortType_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_LnsNasPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portTypeAvp", 2),
          ("virtual", 1))
    )


_L2TunnelGlobal_L2tpConfig_LnsNasPortType_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_LnsNasPortType_Object = MibScalar
l2TunnelGlobal_L2tpConfig_LnsNasPortType = _L2TunnelGlobal_L2tpConfig_LnsNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 31),
    _L2TunnelGlobal_L2tpConfig_LnsNasPortType_Type()
)
l2TunnelGlobal_L2tpConfig_LnsNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_LnsNasPortType.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("v110", 4),
          ("v120", 3))
    )


_L2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType_Object = MibScalar
l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType = _L2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 32),
    _L2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType_Type()
)
l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_RetryTimerMode_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_RetryTimerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exponential", 2),
          ("linear", 1))
    )


_L2TunnelGlobal_L2tpConfig_RetryTimerMode_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_RetryTimerMode_Object = MibScalar
l2TunnelGlobal_L2tpConfig_RetryTimerMode = _L2TunnelGlobal_L2tpConfig_RetryTimerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 33),
    _L2TunnelGlobal_L2tpConfig_RetryTimerMode_Type()
)
l2TunnelGlobal_L2tpConfig_RetryTimerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_RetryTimerMode.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_MaxRetryTimer_Type = Integer32
_L2TunnelGlobal_L2tpConfig_MaxRetryTimer_Object = MibScalar
l2TunnelGlobal_L2tpConfig_MaxRetryTimer = _L2TunnelGlobal_L2tpConfig_MaxRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 34),
    _L2TunnelGlobal_L2tpConfig_MaxRetryTimer_Type()
)
l2TunnelGlobal_L2tpConfig_MaxRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_MaxRetryTimer.setStatus("mandatory")


class _L2TunnelGlobal_L2tpConfig_DataPktUdpCksum_Type(Integer32):
    """Custom type l2TunnelGlobal_L2tpConfig_DataPktUdpCksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_L2TunnelGlobal_L2tpConfig_DataPktUdpCksum_Type.__name__ = "Integer32"
_L2TunnelGlobal_L2tpConfig_DataPktUdpCksum_Object = MibScalar
l2TunnelGlobal_L2tpConfig_DataPktUdpCksum = _L2TunnelGlobal_L2tpConfig_DataPktUdpCksum_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 35),
    _L2TunnelGlobal_L2tpConfig_DataPktUdpCksum_Type()
)
l2TunnelGlobal_L2tpConfig_DataPktUdpCksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_DataPktUdpCksum.setStatus("mandatory")
_L2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel_Type = Integer32
_L2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel_Object = MibScalar
l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel = _L2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 36),
    _L2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel_Type()
)
l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel.setStatus("mandatory")
_MibtunnelServer_ObjectIdentity = ObjectIdentity
mibtunnelServer = _MibtunnelServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 91)
)
_MibtunnelServerTable_Object = MibTable
mibtunnelServerTable = _MibtunnelServerTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1)
)
if mibBuilder.loadTexts:
    mibtunnelServerTable.setStatus("mandatory")
_MibtunnelServerEntry_Object = MibTableRow
mibtunnelServerEntry = _MibtunnelServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1)
)
mibtunnelServerEntry.setIndexNames(
    (0, "ASCEND-MIBL2TUNNEL-MIB", "tunnelServer-ServerEndpoint"),
)
if mibBuilder.loadTexts:
    mibtunnelServerEntry.setStatus("mandatory")
_TunnelServer_ServerEndpoint_Type = DisplayString
_TunnelServer_ServerEndpoint_Object = MibScalar
tunnelServer_ServerEndpoint = _TunnelServer_ServerEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 1),
    _TunnelServer_ServerEndpoint_Type()
)
tunnelServer_ServerEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServer_ServerEndpoint.setStatus("mandatory")


class _TunnelServer_Enabled_Type(Integer32):
    """Custom type tunnelServer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TunnelServer_Enabled_Type.__name__ = "Integer32"
_TunnelServer_Enabled_Object = MibScalar
tunnelServer_Enabled = _TunnelServer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 2),
    _TunnelServer_Enabled_Type()
)
tunnelServer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_Enabled.setStatus("mandatory")
_TunnelServer_SharedSecret_Type = DisplayString
_TunnelServer_SharedSecret_Object = MibScalar
tunnelServer_SharedSecret = _TunnelServer_SharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 3),
    _TunnelServer_SharedSecret_Type()
)
tunnelServer_SharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_SharedSecret.setStatus("mandatory")
_TunnelServer_MaxClients_Type = Integer32
_TunnelServer_MaxClients_Object = MibScalar
tunnelServer_MaxClients = _TunnelServer_MaxClients_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 4),
    _TunnelServer_MaxClients_Type()
)
tunnelServer_MaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_MaxClients.setStatus("mandatory")


class _TunnelServer_ValidCallTypes_Type(Integer32):
    """Custom type tunnelServer_ValidCallTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allCalls", 1),
          ("analogCalls", 2),
          ("digitalCalls", 3))
    )


_TunnelServer_ValidCallTypes_Type.__name__ = "Integer32"
_TunnelServer_ValidCallTypes_Object = MibScalar
tunnelServer_ValidCallTypes = _TunnelServer_ValidCallTypes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 5),
    _TunnelServer_ValidCallTypes_Type()
)
tunnelServer_ValidCallTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_ValidCallTypes.setStatus("mandatory")
_TunnelServer_IpsecProfile_Type = DisplayString
_TunnelServer_IpsecProfile_Object = MibScalar
tunnelServer_IpsecProfile = _TunnelServer_IpsecProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 6),
    _TunnelServer_IpsecProfile_Type()
)
tunnelServer_IpsecProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_IpsecProfile.setStatus("mandatory")
_TunnelServer_ClientAuthId_Type = DisplayString
_TunnelServer_ClientAuthId_Object = MibScalar
tunnelServer_ClientAuthId = _TunnelServer_ClientAuthId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 7),
    _TunnelServer_ClientAuthId_Type()
)
tunnelServer_ClientAuthId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_ClientAuthId.setStatus("mandatory")
_TunnelServer_ServerAuthId_Type = DisplayString
_TunnelServer_ServerAuthId_Object = MibScalar
tunnelServer_ServerAuthId = _TunnelServer_ServerAuthId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 8),
    _TunnelServer_ServerAuthId_Type()
)
tunnelServer_ServerAuthId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_ServerAuthId.setStatus("mandatory")


class _TunnelServer_DialoutOptions_Enabled_Type(Integer32):
    """Custom type tunnelServer_DialoutOptions_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TunnelServer_DialoutOptions_Enabled_Type.__name__ = "Integer32"
_TunnelServer_DialoutOptions_Enabled_Object = MibScalar
tunnelServer_DialoutOptions_Enabled = _TunnelServer_DialoutOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 9),
    _TunnelServer_DialoutOptions_Enabled_Type()
)
tunnelServer_DialoutOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_Enabled.setStatus("mandatory")


class _TunnelServer_Action_o_Type(Integer32):
    """Custom type tunnelServer_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_TunnelServer_Action_o_Type.__name__ = "Integer32"
_TunnelServer_Action_o_Object = MibScalar
tunnelServer_Action_o = _TunnelServer_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 16),
    _TunnelServer_Action_o_Type()
)
tunnelServer_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_Action_o.setStatus("mandatory")


class _TunnelServer_DialoutOptions_DialNumberLookup_Type(Integer32):
    """Custom type tunnelServer_DialoutOptions_DialNumberLookup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TunnelServer_DialoutOptions_DialNumberLookup_Type.__name__ = "Integer32"
_TunnelServer_DialoutOptions_DialNumberLookup_Object = MibScalar
tunnelServer_DialoutOptions_DialNumberLookup = _TunnelServer_DialoutOptions_DialNumberLookup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 17),
    _TunnelServer_DialoutOptions_DialNumberLookup_Type()
)
tunnelServer_DialoutOptions_DialNumberLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DialNumberLookup.setStatus("mandatory")
_TunnelServer_DialoutOptions_LookupPrefix_Type = DisplayString
_TunnelServer_DialoutOptions_LookupPrefix_Object = MibScalar
tunnelServer_DialoutOptions_LookupPrefix = _TunnelServer_DialoutOptions_LookupPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 18),
    _TunnelServer_DialoutOptions_LookupPrefix_Type()
)
tunnelServer_DialoutOptions_LookupPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_LookupPrefix.setStatus("mandatory")
_TunnelServer_DialoutOptions_DialNumberPrefix_Type = DisplayString
_TunnelServer_DialoutOptions_DialNumberPrefix_Object = MibScalar
tunnelServer_DialoutOptions_DialNumberPrefix = _TunnelServer_DialoutOptions_DialNumberPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 19),
    _TunnelServer_DialoutOptions_DialNumberPrefix_Type()
)
tunnelServer_DialoutOptions_DialNumberPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DialNumberPrefix.setStatus("mandatory")
_MibtunnelServer_DialoutOptions_DefaultCallMappingTable_Object = MibTable
mibtunnelServer_DialoutOptions_DefaultCallMappingTable = _MibtunnelServer_DialoutOptions_DefaultCallMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2)
)
if mibBuilder.loadTexts:
    mibtunnelServer_DialoutOptions_DefaultCallMappingTable.setStatus("mandatory")
_MibtunnelServer_DialoutOptions_DefaultCallMappingEntry_Object = MibTableRow
mibtunnelServer_DialoutOptions_DefaultCallMappingEntry = _MibtunnelServer_DialoutOptions_DefaultCallMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1)
)
mibtunnelServer_DialoutOptions_DefaultCallMappingEntry.setIndexNames(
    (0, "ASCEND-MIBL2TUNNEL-MIB", "tunnelServer-DialoutOptions-DefaultCallMapping-ServerEndpoint"),
    (0, "ASCEND-MIBL2TUNNEL-MIB", "tunnelServer-DialoutOptions-DefaultCallMapping-Index-o"),
)
if mibBuilder.loadTexts:
    mibtunnelServer_DialoutOptions_DefaultCallMappingEntry.setStatus("mandatory")
_TunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint_Type = DisplayString
_TunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint_Object = MibScalar
tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint = _TunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 1),
    _TunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint_Type()
)
tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint.setStatus("mandatory")
_TunnelServer_DialoutOptions_DefaultCallMapping_Index_o_Type = Integer32
_TunnelServer_DialoutOptions_DefaultCallMapping_Index_o_Object = MibScalar
tunnelServer_DialoutOptions_DefaultCallMapping_Index_o = _TunnelServer_DialoutOptions_DefaultCallMapping_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 2),
    _TunnelServer_DialoutOptions_DefaultCallMapping_Index_o_Type()
)
tunnelServer_DialoutOptions_DefaultCallMapping_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DefaultCallMapping_Index_o.setStatus("mandatory")


class _TunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry_Type(Integer32):
    """Custom type tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry_Type.__name__ = "Integer32"
_TunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry_Object = MibScalar
tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry = _TunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 3),
    _TunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry_Type()
)
tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry.setStatus("mandatory")


class _TunnelServer_DialoutOptions_DefaultCallMapping_BearerType_Type(Integer32):
    """Custom type tunnelServer_DialoutOptions_DefaultCallMapping_BearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("any", 4),
          ("digital", 2))
    )


_TunnelServer_DialoutOptions_DefaultCallMapping_BearerType_Type.__name__ = "Integer32"
_TunnelServer_DialoutOptions_DefaultCallMapping_BearerType_Object = MibScalar
tunnelServer_DialoutOptions_DefaultCallMapping_BearerType = _TunnelServer_DialoutOptions_DefaultCallMapping_BearerType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 4),
    _TunnelServer_DialoutOptions_DefaultCallMapping_BearerType_Type()
)
tunnelServer_DialoutOptions_DefaultCallMapping_BearerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DefaultCallMapping_BearerType.setStatus("mandatory")


class _TunnelServer_DialoutOptions_DefaultCallMapping_FramingType_Type(Integer32):
    """Custom type tunnelServer_DialoutOptions_DefaultCallMapping_FramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 4),
          ("async", 3),
          ("sync", 2))
    )


_TunnelServer_DialoutOptions_DefaultCallMapping_FramingType_Type.__name__ = "Integer32"
_TunnelServer_DialoutOptions_DefaultCallMapping_FramingType_Object = MibScalar
tunnelServer_DialoutOptions_DefaultCallMapping_FramingType = _TunnelServer_DialoutOptions_DefaultCallMapping_FramingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 5),
    _TunnelServer_DialoutOptions_DefaultCallMapping_FramingType_Type()
)
tunnelServer_DialoutOptions_DefaultCallMapping_FramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DefaultCallMapping_FramingType.setStatus("mandatory")


class _TunnelServer_DialoutOptions_DefaultCallMapping_DataService_Type(Integer32):
    """Custom type tunnelServer_DialoutOptions_DefaultCallMapping_DataService based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
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
              255,
              263)
        )
    )
    namedValues = NamedValues(
        *(("atmSvc", 70),
          ("atmodem", 44),
          ("dws384Clear", 14),
          ("frameRelaySvc", 71),
          ("iptoip", 263),
          ("modem", 43),
          ("modem31khzAudio", 82),
          ("n-1024Clear", 24),
          ("n-1088Clear", 25),
          ("n-1152Clear", 26),
          ("n-1216Clear", 27),
          ("n-1280Clear", 28),
          ("n-128kClear", 10),
          ("n-1344Clear", 29),
          ("n-1408Clear", 30),
          ("n-14456kV110", 74),
          ("n-14456krV110", 76),
          ("n-14464kV110", 78),
          ("n-14464krV110", 80),
          ("n-144kClear", 255),
          ("n-1472Clear", 31),
          ("n-1536kClear", 8),
          ("n-1536kRestricted", 9),
          ("n-1600Clear", 32),
          ("n-1664Clear", 33),
          ("n-1728Clear", 34),
          ("n-1792Clear", 35),
          ("n-1856Clear", 36),
          ("n-1920Clear", 37),
          ("n-19256kV110", 49),
          ("n-19256krV110", 54),
          ("n-19264kV110", 59),
          ("n-19264krV110", 64),
          ("n-192kClear", 11),
          ("n-2456kV110", 46),
          ("n-2456krV110", 51),
          ("n-2464kV110", 56),
          ("n-2464krV110", 61),
          ("n-256kClear", 12),
          ("n-28856kV110", 75),
          ("n-28856krV110", 77),
          ("n-28864kV110", 79),
          ("n-28864krV110", 81),
          ("n-320kClear", 13),
          ("n-38456kV110", 50),
          ("n-38456krV110", 55),
          ("n-38464kV110", 60),
          ("n-38464krV110", 65),
          ("n-384kClear", 7),
          ("n-384kRestricted", 6),
          ("n-448Clear", 15),
          ("n-4856kV110", 47),
          ("n-4856krV110", 52),
          ("n-4864kV110", 57),
          ("n-4864krV110", 62),
          ("n-512Clear", 16),
          ("n-56kClear", 5),
          ("n-56kRestricted", 2),
          ("n-56kV110Clear", 42),
          ("n-576Clear", 17),
          ("n-640Clear", 18),
          ("n-64kClear", 3),
          ("n-64kRestricted", 4),
          ("n-64kX30Restricted", 41),
          ("n-704Clear", 19),
          ("n-768Clear", 20),
          ("n-832Clear", 21),
          ("n-896Clear", 22),
          ("n-960Clear", 23),
          ("n-9656kV110", 48),
          ("n-9656krV110", 53),
          ("n-9664kV110", 58),
          ("n-9664krV110", 63),
          ("phs64k", 67),
          ("v110ClearBearer", 40),
          ("v32", 66),
          ("voice", 1),
          ("voiceOverIp", 68),
          ("vpnTunnel", 72),
          ("wormarq", 73),
          ("x25Svc", 83),
          ("x30RestrictedBearer", 39))
    )


_TunnelServer_DialoutOptions_DefaultCallMapping_DataService_Type.__name__ = "Integer32"
_TunnelServer_DialoutOptions_DefaultCallMapping_DataService_Object = MibScalar
tunnelServer_DialoutOptions_DefaultCallMapping_DataService = _TunnelServer_DialoutOptions_DefaultCallMapping_DataService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 6),
    _TunnelServer_DialoutOptions_DefaultCallMapping_DataService_Type()
)
tunnelServer_DialoutOptions_DefaultCallMapping_DataService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelServer_DialoutOptions_DefaultCallMapping_DataService.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBL2TUNNEL-MIB",
    **{"DisplayString": DisplayString,
       "mibl2TunnelGlobal": mibl2TunnelGlobal,
       "mibl2TunnelGlobalTable": mibl2TunnelGlobalTable,
       "mibl2TunnelGlobalEntry": mibl2TunnelGlobalEntry,
       "l2TunnelGlobal-Index-o": l2TunnelGlobal_Index_o,
       "l2TunnelGlobal-PptpEnabled": l2TunnelGlobal_PptpEnabled,
       "l2TunnelGlobal-ServerProfileRequired": l2TunnelGlobal_ServerProfileRequired,
       "l2TunnelGlobal-L2tpMode": l2TunnelGlobal_L2tpMode,
       "l2TunnelGlobal-L2tpAuthEnabled": l2TunnelGlobal_L2tpAuthEnabled,
       "l2TunnelGlobal-L2tpRxWindow": l2TunnelGlobal_L2tpRxWindow,
       "l2TunnelGlobal-MaxLnsClients": l2TunnelGlobal_MaxLnsClients,
       "l2TunnelGlobal-L2tpSystemName": l2TunnelGlobal_L2tpSystemName,
       "l2TunnelGlobal-L2tpConfig-FirstRetryTimer": l2TunnelGlobal_L2tpConfig_FirstRetryTimer,
       "l2TunnelGlobal-L2tpConfig-RetryCount": l2TunnelGlobal_L2tpConfig_RetryCount,
       "l2TunnelGlobal-L2tpConfig-HelloTimer": l2TunnelGlobal_L2tpConfig_HelloTimer,
       "l2TunnelGlobal-L2tpConfig-ControlConnectEstablishTimer": l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer,
       "l2TunnelGlobal-L2tpConfig-LacIncomingCallTimer": l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer,
       "l2TunnelGlobal-L2tpConfig-LnsIncomingCallTimer": l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer,
       "l2TunnelGlobal-L2tpConfig-BaseUdpPort": l2TunnelGlobal_L2tpConfig_BaseUdpPort,
       "l2TunnelGlobal-L2tpConfig-DialoutAuthLns": l2TunnelGlobal_L2tpConfig_DialoutAuthLns,
       "l2TunnelGlobal-L2tpConfig-DialoutSendProfileName": l2TunnelGlobal_L2tpConfig_DialoutSendProfileName,
       "l2TunnelGlobal-L2tpConfig-AcctTunnelConnectionEncoding": l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding,
       "l2TunnelGlobal-L2fMode": l2TunnelGlobal_L2fMode,
       "l2TunnelGlobal-L2fSystemName": l2TunnelGlobal_L2fSystemName,
       "l2TunnelGlobal-L2fRetryCount": l2TunnelGlobal_L2fRetryCount,
       "l2TunnelGlobal-L2fRetryInterval": l2TunnelGlobal_L2fRetryInterval,
       "l2TunnelGlobal-L2fTunnelSecret": l2TunnelGlobal_L2fTunnelSecret,
       "l2TunnelGlobal-L2fIgnoreMidSequence": l2TunnelGlobal_L2fIgnoreMidSequence,
       "l2TunnelGlobal-Action-o": l2TunnelGlobal_Action_o,
       "l2TunnelGlobal-L2tpConfig-VerifyRemoteHostName": l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName,
       "l2TunnelGlobal-L2tpConfig-DefaultTunnelServer": l2TunnelGlobal_L2tpConfig_DefaultTunnelServer,
       "l2TunnelGlobal-L2tpConfig-TunnelServerPreSccrqLookup": l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup,
       "l2TunnelGlobal-L2tpConfig-SuppressEndpointDiscriminator": l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator,
       "l2TunnelGlobal-L2tpConfig-LnsNasPortType": l2TunnelGlobal_L2tpConfig_LnsNasPortType,
       "l2TunnelGlobal-L2tpConfig-DigitalAsyncNasPortType": l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType,
       "l2TunnelGlobal-L2tpConfig-RetryTimerMode": l2TunnelGlobal_L2tpConfig_RetryTimerMode,
       "l2TunnelGlobal-L2tpConfig-MaxRetryTimer": l2TunnelGlobal_L2tpConfig_MaxRetryTimer,
       "l2TunnelGlobal-L2tpConfig-DataPktUdpCksum": l2TunnelGlobal_L2tpConfig_DataPktUdpCksum,
       "l2TunnelGlobal-L2tpConfig-MaxCallsPerTunnel": l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel,
       "mibtunnelServer": mibtunnelServer,
       "mibtunnelServerTable": mibtunnelServerTable,
       "mibtunnelServerEntry": mibtunnelServerEntry,
       "tunnelServer-ServerEndpoint": tunnelServer_ServerEndpoint,
       "tunnelServer-Enabled": tunnelServer_Enabled,
       "tunnelServer-SharedSecret": tunnelServer_SharedSecret,
       "tunnelServer-MaxClients": tunnelServer_MaxClients,
       "tunnelServer-ValidCallTypes": tunnelServer_ValidCallTypes,
       "tunnelServer-IpsecProfile": tunnelServer_IpsecProfile,
       "tunnelServer-ClientAuthId": tunnelServer_ClientAuthId,
       "tunnelServer-ServerAuthId": tunnelServer_ServerAuthId,
       "tunnelServer-DialoutOptions-Enabled": tunnelServer_DialoutOptions_Enabled,
       "tunnelServer-Action-o": tunnelServer_Action_o,
       "tunnelServer-DialoutOptions-DialNumberLookup": tunnelServer_DialoutOptions_DialNumberLookup,
       "tunnelServer-DialoutOptions-LookupPrefix": tunnelServer_DialoutOptions_LookupPrefix,
       "tunnelServer-DialoutOptions-DialNumberPrefix": tunnelServer_DialoutOptions_DialNumberPrefix,
       "mibtunnelServer-DialoutOptions-DefaultCallMappingTable": mibtunnelServer_DialoutOptions_DefaultCallMappingTable,
       "mibtunnelServer-DialoutOptions-DefaultCallMappingEntry": mibtunnelServer_DialoutOptions_DefaultCallMappingEntry,
       "tunnelServer-DialoutOptions-DefaultCallMapping-ServerEndpoint": tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint,
       "tunnelServer-DialoutOptions-DefaultCallMapping-Index-o": tunnelServer_DialoutOptions_DefaultCallMapping_Index_o,
       "tunnelServer-DialoutOptions-DefaultCallMapping-ValidEntry": tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry,
       "tunnelServer-DialoutOptions-DefaultCallMapping-BearerType": tunnelServer_DialoutOptions_DefaultCallMapping_BearerType,
       "tunnelServer-DialoutOptions-DefaultCallMapping-FramingType": tunnelServer_DialoutOptions_DefaultCallMapping_FramingType,
       "tunnelServer-DialoutOptions-DefaultCallMapping-DataService": tunnelServer_DialoutOptions_DefaultCallMapping_DataService}
)
