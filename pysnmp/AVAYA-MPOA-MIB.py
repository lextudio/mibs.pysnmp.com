# SNMP MIB module (AVAYA-MPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-MPOA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:33 2024
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

(lsg,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "lsg")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mpoa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1)
)
mpoa.setRevisions(
        ("1901-10-10 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MpoaEnabledValue(Integer32, TextualConvention):
    status = "current"
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



class MpoaYesorNoValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )



class MpoaOperValue(Integer32, TextualConvention):
    status = "current"
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
          ("initial", 3),
          ("up", 1))
    )



class MpoaResourceId(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1012)
)
_EsrLsg_ObjectIdentity = ObjectIdentity
esrLsg = _EsrLsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1012, 44)
)
_AtmAccess_ObjectIdentity = ObjectIdentity
atmAccess = _AtmAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4)
)
_MpoaResourceMgmtGroup_ObjectIdentity = ObjectIdentity
mpoaResourceMgmtGroup = _MpoaResourceMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 1)
)
_MpoaNextLinkResourceId_Type = Integer32
_MpoaNextLinkResourceId_Object = MibScalar
mpoaNextLinkResourceId = _MpoaNextLinkResourceId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 1, 1),
    _MpoaNextLinkResourceId_Type()
)
mpoaNextLinkResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaNextLinkResourceId.setStatus("current")
_MpoaNextPvcResourceId_Type = Integer32
_MpoaNextPvcResourceId_Object = MibScalar
mpoaNextPvcResourceId = _MpoaNextPvcResourceId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 1, 2),
    _MpoaNextPvcResourceId_Type()
)
mpoaNextPvcResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaNextPvcResourceId.setStatus("current")
_MpoaVirtualSwitchPortTable_Object = MibTable
mpoaVirtualSwitchPortTable = _MpoaVirtualSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mpoaVirtualSwitchPortTable.setStatus("current")
_MpoaVirtualSwitchPortEntry_Object = MibTableRow
mpoaVirtualSwitchPortEntry = _MpoaVirtualSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1)
)
mpoaVirtualSwitchPortEntry.setIndexNames(
    (0, "AVAYA-MPOA-MIB", "mpoaVspIndex"),
)
if mibBuilder.loadTexts:
    mpoaVirtualSwitchPortEntry.setStatus("current")


class _MpoaVspIndex_Type(Integer32):
    """Custom type mpoaVspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpoaVspIndex_Type.__name__ = "Integer32"
_MpoaVspIndex_Object = MibTableColumn
mpoaVspIndex = _MpoaVspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 1),
    _MpoaVspIndex_Type()
)
mpoaVspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaVspIndex.setStatus("current")
_MpoaVspAdminStatus_Type = MpoaEnabledValue
_MpoaVspAdminStatus_Object = MibTableColumn
mpoaVspAdminStatus = _MpoaVspAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 2),
    _MpoaVspAdminStatus_Type()
)
mpoaVspAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspAdminStatus.setStatus("current")
_MpoaVspOperStatus_Type = MpoaOperValue
_MpoaVspOperStatus_Object = MibTableColumn
mpoaVspOperStatus = _MpoaVspOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 3),
    _MpoaVspOperStatus_Type()
)
mpoaVspOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaVspOperStatus.setStatus("current")


class _MpoaVspName_Type(DisplayString):
    """Custom type mpoaVspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpoaVspName_Type.__name__ = "DisplayString"
_MpoaVspName_Object = MibTableColumn
mpoaVspName = _MpoaVspName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 4),
    _MpoaVspName_Type()
)
mpoaVspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspName.setStatus("current")


class _MpoaVspEncapsulationType_Type(Integer32):
    """Custom type mpoaVspEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llcBridge", 3),
          ("routed", 1),
          ("simpleBridge", 2))
    )


_MpoaVspEncapsulationType_Type.__name__ = "Integer32"
_MpoaVspEncapsulationType_Object = MibTableColumn
mpoaVspEncapsulationType = _MpoaVspEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 5),
    _MpoaVspEncapsulationType_Type()
)
mpoaVspEncapsulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspEncapsulationType.setStatus("current")
_MpoaVspPktReplication_Type = MpoaYesorNoValue
_MpoaVspPktReplication_Object = MibTableColumn
mpoaVspPktReplication = _MpoaVspPktReplication_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 6),
    _MpoaVspPktReplication_Type()
)
mpoaVspPktReplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspPktReplication.setStatus("current")
_MpoaVspLoadShare_Type = MpoaYesorNoValue
_MpoaVspLoadShare_Object = MibTableColumn
mpoaVspLoadShare = _MpoaVspLoadShare_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 7),
    _MpoaVspLoadShare_Type()
)
mpoaVspLoadShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspLoadShare.setStatus("current")


class _MpoaVspDefaultPort_Type(Integer32):
    """Custom type mpoaVspDefaultPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MpoaVspDefaultPort_Type.__name__ = "Integer32"
_MpoaVspDefaultPort_Object = MibTableColumn
mpoaVspDefaultPort = _MpoaVspDefaultPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 8),
    _MpoaVspDefaultPort_Type()
)
mpoaVspDefaultPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspDefaultPort.setStatus("current")
_MpoaVspDefaultVc_port1_Type = MpoaResourceId
_MpoaVspDefaultVc_port1_Object = MibScalar
mpoaVspDefaultVc_port1 = _MpoaVspDefaultVc_port1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 9),
    _MpoaVspDefaultVc_port1_Type()
)
mpoaVspDefaultVc_port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspDefaultVc_port1.setStatus("current")
_MpoaVspDefaultVc_port2_Type = MpoaResourceId
_MpoaVspDefaultVc_port2_Object = MibScalar
mpoaVspDefaultVc_port2 = _MpoaVspDefaultVc_port2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 10),
    _MpoaVspDefaultVc_port2_Type()
)
mpoaVspDefaultVc_port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspDefaultVc_port2.setStatus("current")
_MpoaVspMulticastChan_port1_Type = Integer32
_MpoaVspMulticastChan_port1_Object = MibScalar
mpoaVspMulticastChan_port1 = _MpoaVspMulticastChan_port1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 11),
    _MpoaVspMulticastChan_port1_Type()
)
mpoaVspMulticastChan_port1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaVspMulticastChan_port1.setStatus("current")
_MpoaVspMulticastChan_port2_Type = Integer32
_MpoaVspMulticastChan_port2_Object = MibScalar
mpoaVspMulticastChan_port2 = _MpoaVspMulticastChan_port2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 12),
    _MpoaVspMulticastChan_port2_Type()
)
mpoaVspMulticastChan_port2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaVspMulticastChan_port2.setStatus("current")
_MpoaVspRowStatus_Type = RowStatus
_MpoaVspRowStatus_Object = MibTableColumn
mpoaVspRowStatus = _MpoaVspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 13),
    _MpoaVspRowStatus_Type()
)
mpoaVspRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaVspRowStatus.setStatus("current")
_MpoaAtmLinkTable_Object = MibTable
mpoaAtmLinkTable = _MpoaAtmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    mpoaAtmLinkTable.setStatus("current")
_MpoaAtmLinkEntry_Object = MibTableRow
mpoaAtmLinkEntry = _MpoaAtmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1)
)
mpoaAtmLinkEntry.setIndexNames(
    (0, "AVAYA-MPOA-MIB", "mpoaAtmLinkVspIndex"),
    (0, "AVAYA-MPOA-MIB", "mpoaAtmLinkIndex"),
)
if mibBuilder.loadTexts:
    mpoaAtmLinkEntry.setStatus("current")


class _MpoaAtmLinkVspIndex_Type(Integer32):
    """Custom type mpoaAtmLinkVspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpoaAtmLinkVspIndex_Type.__name__ = "Integer32"
_MpoaAtmLinkVspIndex_Object = MibTableColumn
mpoaAtmLinkVspIndex = _MpoaAtmLinkVspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 1),
    _MpoaAtmLinkVspIndex_Type()
)
mpoaAtmLinkVspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaAtmLinkVspIndex.setStatus("current")
_MpoaAtmLinkIndex_Type = MpoaResourceId
_MpoaAtmLinkIndex_Object = MibTableColumn
mpoaAtmLinkIndex = _MpoaAtmLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 2),
    _MpoaAtmLinkIndex_Type()
)
mpoaAtmLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaAtmLinkIndex.setStatus("current")
_MpoaAtmLinkAdminStatus_Type = MpoaEnabledValue
_MpoaAtmLinkAdminStatus_Object = MibTableColumn
mpoaAtmLinkAdminStatus = _MpoaAtmLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 3),
    _MpoaAtmLinkAdminStatus_Type()
)
mpoaAtmLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkAdminStatus.setStatus("current")
_MpoaAtmLinkOperStatus_Type = MpoaOperValue
_MpoaAtmLinkOperStatus_Object = MibTableColumn
mpoaAtmLinkOperStatus = _MpoaAtmLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 4),
    _MpoaAtmLinkOperStatus_Type()
)
mpoaAtmLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaAtmLinkOperStatus.setStatus("current")


class _MpoaAtmLinkName_Type(DisplayString):
    """Custom type mpoaAtmLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpoaAtmLinkName_Type.__name__ = "DisplayString"
_MpoaAtmLinkName_Object = MibTableColumn
mpoaAtmLinkName = _MpoaAtmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 5),
    _MpoaAtmLinkName_Type()
)
mpoaAtmLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkName.setStatus("current")
_MpoaAtmLinkDefaultVc_Type = MpoaResourceId
_MpoaAtmLinkDefaultVc_Object = MibTableColumn
mpoaAtmLinkDefaultVc = _MpoaAtmLinkDefaultVc_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 6),
    _MpoaAtmLinkDefaultVc_Type()
)
mpoaAtmLinkDefaultVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkDefaultVc.setStatus("current")
_MpoaAtmLinkFailOverLink_Type = MpoaResourceId
_MpoaAtmLinkFailOverLink_Object = MibTableColumn
mpoaAtmLinkFailOverLink = _MpoaAtmLinkFailOverLink_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 8),
    _MpoaAtmLinkFailOverLink_Type()
)
mpoaAtmLinkFailOverLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkFailOverLink.setStatus("current")
_MpoaAtmLinkOutPriority_0_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_0_Object = MibScalar
mpoaAtmLinkOutPriority_0 = _MpoaAtmLinkOutPriority_0_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 9),
    _MpoaAtmLinkOutPriority_0_Type()
)
mpoaAtmLinkOutPriority_0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_0.setStatus("current")
_MpoaAtmLinkOutPriority_1_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_1_Object = MibScalar
mpoaAtmLinkOutPriority_1 = _MpoaAtmLinkOutPriority_1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 10),
    _MpoaAtmLinkOutPriority_1_Type()
)
mpoaAtmLinkOutPriority_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_1.setStatus("current")
_MpoaAtmLinkOutPriority_2_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_2_Object = MibScalar
mpoaAtmLinkOutPriority_2 = _MpoaAtmLinkOutPriority_2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 11),
    _MpoaAtmLinkOutPriority_2_Type()
)
mpoaAtmLinkOutPriority_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_2.setStatus("current")
_MpoaAtmLinkOutPriority_3_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_3_Object = MibScalar
mpoaAtmLinkOutPriority_3 = _MpoaAtmLinkOutPriority_3_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 12),
    _MpoaAtmLinkOutPriority_3_Type()
)
mpoaAtmLinkOutPriority_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_3.setStatus("current")
_MpoaAtmLinkOutPriority_4_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_4_Object = MibScalar
mpoaAtmLinkOutPriority_4 = _MpoaAtmLinkOutPriority_4_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 13),
    _MpoaAtmLinkOutPriority_4_Type()
)
mpoaAtmLinkOutPriority_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_4.setStatus("current")
_MpoaAtmLinkOutPriority_5_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_5_Object = MibScalar
mpoaAtmLinkOutPriority_5 = _MpoaAtmLinkOutPriority_5_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 14),
    _MpoaAtmLinkOutPriority_5_Type()
)
mpoaAtmLinkOutPriority_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_5.setStatus("current")
_MpoaAtmLinkOutPriority_6_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_6_Object = MibScalar
mpoaAtmLinkOutPriority_6 = _MpoaAtmLinkOutPriority_6_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 15),
    _MpoaAtmLinkOutPriority_6_Type()
)
mpoaAtmLinkOutPriority_6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_6.setStatus("current")
_MpoaAtmLinkOutPriority_7_Type = MpoaResourceId
_MpoaAtmLinkOutPriority_7_Object = MibScalar
mpoaAtmLinkOutPriority_7 = _MpoaAtmLinkOutPriority_7_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 16),
    _MpoaAtmLinkOutPriority_7_Type()
)
mpoaAtmLinkOutPriority_7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkOutPriority_7.setStatus("current")
_MpoaAtmLinkRowStatus_Type = RowStatus
_MpoaAtmLinkRowStatus_Object = MibTableColumn
mpoaAtmLinkRowStatus = _MpoaAtmLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 17),
    _MpoaAtmLinkRowStatus_Type()
)
mpoaAtmLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaAtmLinkRowStatus.setStatus("current")
_MpoaPvcTable_Object = MibTable
mpoaPvcTable = _MpoaPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    mpoaPvcTable.setStatus("current")
_MpoaPvcEntry_Object = MibTableRow
mpoaPvcEntry = _MpoaPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1)
)
mpoaPvcEntry.setIndexNames(
    (0, "AVAYA-MPOA-MIB", "mpoaPvcVspIndex"),
    (0, "AVAYA-MPOA-MIB", "mpoaPvcLinkIndex"),
    (0, "AVAYA-MPOA-MIB", "mpoaPvcResIndex"),
)
if mibBuilder.loadTexts:
    mpoaPvcEntry.setStatus("current")


class _MpoaPvcVspIndex_Type(Integer32):
    """Custom type mpoaPvcVspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpoaPvcVspIndex_Type.__name__ = "Integer32"
_MpoaPvcVspIndex_Object = MibTableColumn
mpoaPvcVspIndex = _MpoaPvcVspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 1),
    _MpoaPvcVspIndex_Type()
)
mpoaPvcVspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaPvcVspIndex.setStatus("current")
_MpoaPvcLinkIndex_Type = MpoaResourceId
_MpoaPvcLinkIndex_Object = MibTableColumn
mpoaPvcLinkIndex = _MpoaPvcLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 2),
    _MpoaPvcLinkIndex_Type()
)
mpoaPvcLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaPvcLinkIndex.setStatus("current")
_MpoaPvcResIndex_Type = MpoaResourceId
_MpoaPvcResIndex_Object = MibTableColumn
mpoaPvcResIndex = _MpoaPvcResIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 3),
    _MpoaPvcResIndex_Type()
)
mpoaPvcResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpoaPvcResIndex.setStatus("current")


class _MpoaPvcPort_Type(Integer32):
    """Custom type mpoaPvcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MpoaPvcPort_Type.__name__ = "Integer32"
_MpoaPvcPort_Object = MibTableColumn
mpoaPvcPort = _MpoaPvcPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 4),
    _MpoaPvcPort_Type()
)
mpoaPvcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcPort.setStatus("current")


class _MpoaPvcVpi_Type(Integer32):
    """Custom type mpoaPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpoaPvcVpi_Type.__name__ = "Integer32"
_MpoaPvcVpi_Object = MibTableColumn
mpoaPvcVpi = _MpoaPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 5),
    _MpoaPvcVpi_Type()
)
mpoaPvcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcVpi.setStatus("current")


class _MpoaPvcVci_Type(Integer32):
    """Custom type mpoaPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_MpoaPvcVci_Type.__name__ = "Integer32"
_MpoaPvcVci_Object = MibTableColumn
mpoaPvcVci = _MpoaPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 6),
    _MpoaPvcVci_Type()
)
mpoaPvcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcVci.setStatus("current")


class _MpoaPvcInPriorityMap_Type(Integer32):
    """Custom type mpoaPvcInPriorityMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpoaPvcInPriorityMap_Type.__name__ = "Integer32"
_MpoaPvcInPriorityMap_Object = MibTableColumn
mpoaPvcInPriorityMap = _MpoaPvcInPriorityMap_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 7),
    _MpoaPvcInPriorityMap_Type()
)
mpoaPvcInPriorityMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcInPriorityMap.setStatus("current")


class _MpoaPvcTrafficClass_Type(Integer32):
    """Custom type mpoaPvcTrafficClass based on Integer32"""
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
        *(("cbr", 4),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 1))
    )


_MpoaPvcTrafficClass_Type.__name__ = "Integer32"
_MpoaPvcTrafficClass_Object = MibTableColumn
mpoaPvcTrafficClass = _MpoaPvcTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 8),
    _MpoaPvcTrafficClass_Type()
)
mpoaPvcTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcTrafficClass.setStatus("current")


class _MpoaPvcCDVT_Type(Integer32):
    """Custom type mpoaPvcCDVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MpoaPvcCDVT_Type.__name__ = "Integer32"
_MpoaPvcCDVT_Object = MibTableColumn
mpoaPvcCDVT = _MpoaPvcCDVT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 9),
    _MpoaPvcCDVT_Type()
)
mpoaPvcCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcCDVT.setStatus("current")


class _MpoaPvcPCR_Type(Integer32):
    """Custom type mpoaPvcPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1412830),
    )


_MpoaPvcPCR_Type.__name__ = "Integer32"
_MpoaPvcPCR_Object = MibTableColumn
mpoaPvcPCR = _MpoaPvcPCR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 10),
    _MpoaPvcPCR_Type()
)
mpoaPvcPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcPCR.setStatus("current")


class _MpoaPvcSCR_Type(Integer32):
    """Custom type mpoaPvcSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1412830),
    )


_MpoaPvcSCR_Type.__name__ = "Integer32"
_MpoaPvcSCR_Object = MibTableColumn
mpoaPvcSCR = _MpoaPvcSCR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 11),
    _MpoaPvcSCR_Type()
)
mpoaPvcSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcSCR.setStatus("current")


class _MpoaPvcMBS_Type(Integer32):
    """Custom type mpoaPvcMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1048576),
    )


_MpoaPvcMBS_Type.__name__ = "Integer32"
_MpoaPvcMBS_Object = MibTableColumn
mpoaPvcMBS = _MpoaPvcMBS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 12),
    _MpoaPvcMBS_Type()
)
mpoaPvcMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcMBS.setStatus("current")


class _MpoaPvcRandomEarlyDetPktId_Type(Integer32):
    """Custom type mpoaPvcRandomEarlyDetPktId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MpoaPvcRandomEarlyDetPktId_Type.__name__ = "Integer32"
_MpoaPvcRandomEarlyDetPktId_Object = MibTableColumn
mpoaPvcRandomEarlyDetPktId = _MpoaPvcRandomEarlyDetPktId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 13),
    _MpoaPvcRandomEarlyDetPktId_Type()
)
mpoaPvcRandomEarlyDetPktId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcRandomEarlyDetPktId.setStatus("current")
_MpoaPvcRowStatus_Type = RowStatus
_MpoaPvcRowStatus_Object = MibTableColumn
mpoaPvcRowStatus = _MpoaPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 14),
    _MpoaPvcRowStatus_Type()
)
mpoaPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpoaPvcRowStatus.setStatus("current")
_MpoaTraps_ObjectIdentity = ObjectIdentity
mpoaTraps = _MpoaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5)
)


class _MpoaVspId_Type(Integer32):
    """Custom type mpoaVspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpoaVspId_Type.__name__ = "Integer32"
_MpoaVspId_Object = MibScalar
mpoaVspId = _MpoaVspId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 1),
    _MpoaVspId_Type()
)
mpoaVspId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mpoaVspId.setStatus("current")
_MpoaLinkId_Type = MpoaResourceId
_MpoaLinkId_Object = MibScalar
mpoaLinkId = _MpoaLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 2),
    _MpoaLinkId_Type()
)
mpoaLinkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mpoaLinkId.setStatus("current")
_MpoaOperState_Type = MpoaOperValue
_MpoaOperState_Object = MibScalar
mpoaOperState = _MpoaOperState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 3),
    _MpoaOperState_Type()
)
mpoaOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mpoaOperState.setStatus("current")

# Managed Objects groups


# Notification objects

mpoaTrapLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 4)
)
mpoaTrapLinkChange.setObjects(
      *(("AVAYA-MPOA-MIB", "mpoaVspId"),
        ("AVAYA-MPOA-MIB", "mpoaLinkId"),
        ("AVAYA-MPOA-MIB", "mpoaOperState"))
)
if mibBuilder.loadTexts:
    mpoaTrapLinkChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-MPOA-MIB",
    **{"MpoaEnabledValue": MpoaEnabledValue,
       "MpoaYesorNoValue": MpoaYesorNoValue,
       "MpoaOperValue": MpoaOperValue,
       "MpoaResourceId": MpoaResourceId,
       "marconi": marconi,
       "esrLsg": esrLsg,
       "atmAccess": atmAccess,
       "mpoa": mpoa,
       "mpoaResourceMgmtGroup": mpoaResourceMgmtGroup,
       "mpoaNextLinkResourceId": mpoaNextLinkResourceId,
       "mpoaNextPvcResourceId": mpoaNextPvcResourceId,
       "mpoaVirtualSwitchPortTable": mpoaVirtualSwitchPortTable,
       "mpoaVirtualSwitchPortEntry": mpoaVirtualSwitchPortEntry,
       "mpoaVspIndex": mpoaVspIndex,
       "mpoaVspAdminStatus": mpoaVspAdminStatus,
       "mpoaVspOperStatus": mpoaVspOperStatus,
       "mpoaVspName": mpoaVspName,
       "mpoaVspEncapsulationType": mpoaVspEncapsulationType,
       "mpoaVspPktReplication": mpoaVspPktReplication,
       "mpoaVspLoadShare": mpoaVspLoadShare,
       "mpoaVspDefaultPort": mpoaVspDefaultPort,
       "mpoaVspDefaultVc-port1": mpoaVspDefaultVc_port1,
       "mpoaVspDefaultVc-port2": mpoaVspDefaultVc_port2,
       "mpoaVspMulticastChan-port1": mpoaVspMulticastChan_port1,
       "mpoaVspMulticastChan-port2": mpoaVspMulticastChan_port2,
       "mpoaVspRowStatus": mpoaVspRowStatus,
       "mpoaAtmLinkTable": mpoaAtmLinkTable,
       "mpoaAtmLinkEntry": mpoaAtmLinkEntry,
       "mpoaAtmLinkVspIndex": mpoaAtmLinkVspIndex,
       "mpoaAtmLinkIndex": mpoaAtmLinkIndex,
       "mpoaAtmLinkAdminStatus": mpoaAtmLinkAdminStatus,
       "mpoaAtmLinkOperStatus": mpoaAtmLinkOperStatus,
       "mpoaAtmLinkName": mpoaAtmLinkName,
       "mpoaAtmLinkDefaultVc": mpoaAtmLinkDefaultVc,
       "mpoaAtmLinkFailOverLink": mpoaAtmLinkFailOverLink,
       "mpoaAtmLinkOutPriority-0": mpoaAtmLinkOutPriority_0,
       "mpoaAtmLinkOutPriority-1": mpoaAtmLinkOutPriority_1,
       "mpoaAtmLinkOutPriority-2": mpoaAtmLinkOutPriority_2,
       "mpoaAtmLinkOutPriority-3": mpoaAtmLinkOutPriority_3,
       "mpoaAtmLinkOutPriority-4": mpoaAtmLinkOutPriority_4,
       "mpoaAtmLinkOutPriority-5": mpoaAtmLinkOutPriority_5,
       "mpoaAtmLinkOutPriority-6": mpoaAtmLinkOutPriority_6,
       "mpoaAtmLinkOutPriority-7": mpoaAtmLinkOutPriority_7,
       "mpoaAtmLinkRowStatus": mpoaAtmLinkRowStatus,
       "mpoaPvcTable": mpoaPvcTable,
       "mpoaPvcEntry": mpoaPvcEntry,
       "mpoaPvcVspIndex": mpoaPvcVspIndex,
       "mpoaPvcLinkIndex": mpoaPvcLinkIndex,
       "mpoaPvcResIndex": mpoaPvcResIndex,
       "mpoaPvcPort": mpoaPvcPort,
       "mpoaPvcVpi": mpoaPvcVpi,
       "mpoaPvcVci": mpoaPvcVci,
       "mpoaPvcInPriorityMap": mpoaPvcInPriorityMap,
       "mpoaPvcTrafficClass": mpoaPvcTrafficClass,
       "mpoaPvcCDVT": mpoaPvcCDVT,
       "mpoaPvcPCR": mpoaPvcPCR,
       "mpoaPvcSCR": mpoaPvcSCR,
       "mpoaPvcMBS": mpoaPvcMBS,
       "mpoaPvcRandomEarlyDetPktId": mpoaPvcRandomEarlyDetPktId,
       "mpoaPvcRowStatus": mpoaPvcRowStatus,
       "mpoaTraps": mpoaTraps,
       "mpoaVspId": mpoaVspId,
       "mpoaLinkId": mpoaLinkId,
       "mpoaOperState": mpoaOperState,
       "mpoaTrapLinkChange": mpoaTrapLinkChange}
)
