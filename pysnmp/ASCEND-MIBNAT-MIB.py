# SNMP MIB module (ASCEND-MIBNAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBNAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:56 2024
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

_MibnatProfile_ObjectIdentity = ObjectIdentity
mibnatProfile = _MibnatProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 95)
)
_MibnatProfileTable_Object = MibTable
mibnatProfileTable = _MibnatProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1)
)
if mibBuilder.loadTexts:
    mibnatProfileTable.setStatus("mandatory")
_MibnatProfileEntry_Object = MibTableRow
mibnatProfileEntry = _MibnatProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1)
)
mibnatProfileEntry.setIndexNames(
    (0, "ASCEND-MIBNAT-MIB", "natProfile-NatProfile"),
)
if mibBuilder.loadTexts:
    mibnatProfileEntry.setStatus("mandatory")


class _NatProfile_NatRouting_Type(Integer32):
    """Custom type natProfile_NatRouting based on Integer32"""
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


_NatProfile_NatRouting_Type.__name__ = "Integer32"
_NatProfile_NatRouting_Object = MibScalar
natProfile_NatRouting = _NatProfile_NatRouting_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 2),
    _NatProfile_NatRouting_Type()
)
natProfile_NatRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_NatRouting.setStatus("mandatory")
_NatProfile_NatProfile_Type = DisplayString
_NatProfile_NatProfile_Object = MibScalar
natProfile_NatProfile = _NatProfile_NatProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 3),
    _NatProfile_NatProfile_Type()
)
natProfile_NatProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natProfile_NatProfile.setStatus("mandatory")


class _NatProfile_NatLan_Type(Integer32):
    """Custom type natProfile_NatLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("natlanMultiIp", 2),
          ("natlanPoolIp", 3),
          ("natlanSingleIp", 1))
    )


_NatProfile_NatLan_Type.__name__ = "Integer32"
_NatProfile_NatLan_Object = MibScalar
natProfile_NatLan = _NatProfile_NatLan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 4),
    _NatProfile_NatLan_Type()
)
natProfile_NatLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_NatLan.setStatus("mandatory")
_NatProfile_DefaultServer_Type = IpAddress
_NatProfile_DefaultServer_Object = MibScalar
natProfile_DefaultServer = _NatProfile_DefaultServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 5),
    _NatProfile_DefaultServer_Type()
)
natProfile_DefaultServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_DefaultServer.setStatus("mandatory")
_NatProfile_TunnelServer_Type = IpAddress
_NatProfile_TunnelServer_Object = MibScalar
natProfile_TunnelServer = _NatProfile_TunnelServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 6),
    _NatProfile_TunnelServer_Type()
)
natProfile_TunnelServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_TunnelServer.setStatus("mandatory")
_NatProfile_FrameRelayAddress_Type = IpAddress
_NatProfile_FrameRelayAddress_Object = MibScalar
natProfile_FrameRelayAddress = _NatProfile_FrameRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 7),
    _NatProfile_FrameRelayAddress_Type()
)
natProfile_FrameRelayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_FrameRelayAddress.setStatus("mandatory")


class _NatProfile_StickyAddress_Type(Integer32):
    """Custom type natProfile_StickyAddress based on Integer32"""
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


_NatProfile_StickyAddress_Type.__name__ = "Integer32"
_NatProfile_StickyAddress_Object = MibScalar
natProfile_StickyAddress = _NatProfile_StickyAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 8),
    _NatProfile_StickyAddress_Type()
)
natProfile_StickyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StickyAddress.setStatus("mandatory")
_NatProfile_StickyTimeout_Type = Integer32
_NatProfile_StickyTimeout_Object = MibScalar
natProfile_StickyTimeout = _NatProfile_StickyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 9),
    _NatProfile_StickyTimeout_Type()
)
natProfile_StickyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StickyTimeout.setStatus("mandatory")
_NatProfile_NoNatAddress_Type = IpAddress
_NatProfile_NoNatAddress_Object = MibScalar
natProfile_NoNatAddress = _NatProfile_NoNatAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 10),
    _NatProfile_NoNatAddress_Type()
)
natProfile_NoNatAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_NoNatAddress.setStatus("mandatory")
_NatProfile_AlternateNaptAddress_Type = IpAddress
_NatProfile_AlternateNaptAddress_Object = MibScalar
natProfile_AlternateNaptAddress = _NatProfile_AlternateNaptAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 11),
    _NatProfile_AlternateNaptAddress_Type()
)
natProfile_AlternateNaptAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_AlternateNaptAddress.setStatus("mandatory")
_NatProfile_NaptIdleTcpTimeout_Type = Integer32
_NatProfile_NaptIdleTcpTimeout_Object = MibScalar
natProfile_NaptIdleTcpTimeout = _NatProfile_NaptIdleTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 12),
    _NatProfile_NaptIdleTcpTimeout_Type()
)
natProfile_NaptIdleTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_NaptIdleTcpTimeout.setStatus("mandatory")


class _NatProfile_Action_o_Type(Integer32):
    """Custom type natProfile_Action_o based on Integer32"""
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


_NatProfile_Action_o_Type.__name__ = "Integer32"
_NatProfile_Action_o_Object = MibScalar
natProfile_Action_o = _NatProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 13),
    _NatProfile_Action_o_Type()
)
natProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_Action_o.setStatus("mandatory")
_NatProfile_NatAddrPoolNum_Type = Integer32
_NatProfile_NatAddrPoolNum_Object = MibScalar
natProfile_NatAddrPoolNum = _NatProfile_NatAddrPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 1, 1, 14),
    _NatProfile_NatAddrPoolNum_Type()
)
natProfile_NatAddrPoolNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_NatAddrPoolNum.setStatus("mandatory")
_MibnatProfile_StaticMappingsTable_Object = MibTable
mibnatProfile_StaticMappingsTable = _MibnatProfile_StaticMappingsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2)
)
if mibBuilder.loadTexts:
    mibnatProfile_StaticMappingsTable.setStatus("mandatory")
_MibnatProfile_StaticMappingsEntry_Object = MibTableRow
mibnatProfile_StaticMappingsEntry = _MibnatProfile_StaticMappingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1)
)
mibnatProfile_StaticMappingsEntry.setIndexNames(
    (0, "ASCEND-MIBNAT-MIB", "natProfile-StaticMappings-NatProfile"),
    (0, "ASCEND-MIBNAT-MIB", "natProfile-StaticMappings-Index-o"),
)
if mibBuilder.loadTexts:
    mibnatProfile_StaticMappingsEntry.setStatus("mandatory")
_NatProfile_StaticMappings_Index_o_Type = Integer32
_NatProfile_StaticMappings_Index_o_Object = MibScalar
natProfile_StaticMappings_Index_o = _NatProfile_StaticMappings_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 1),
    _NatProfile_StaticMappings_Index_o_Type()
)
natProfile_StaticMappings_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_Index_o.setStatus("mandatory")


class _NatProfile_StaticMappings_ValidEntry_Type(Integer32):
    """Custom type natProfile_StaticMappings_ValidEntry based on Integer32"""
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


_NatProfile_StaticMappings_ValidEntry_Type.__name__ = "Integer32"
_NatProfile_StaticMappings_ValidEntry_Object = MibScalar
natProfile_StaticMappings_ValidEntry = _NatProfile_StaticMappings_ValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 3),
    _NatProfile_StaticMappings_ValidEntry_Type()
)
natProfile_StaticMappings_ValidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_ValidEntry.setStatus("mandatory")
_NatProfile_StaticMappings_DestPort_Type = Integer32
_NatProfile_StaticMappings_DestPort_Object = MibScalar
natProfile_StaticMappings_DestPort = _NatProfile_StaticMappings_DestPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 4),
    _NatProfile_StaticMappings_DestPort_Type()
)
natProfile_StaticMappings_DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_DestPort.setStatus("mandatory")


class _NatProfile_StaticMappings_Protocol_Type(Integer32):
    """Custom type natProfile_StaticMappings_Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smTcp", 1),
          ("smUdp", 2))
    )


_NatProfile_StaticMappings_Protocol_Type.__name__ = "Integer32"
_NatProfile_StaticMappings_Protocol_Object = MibScalar
natProfile_StaticMappings_Protocol = _NatProfile_StaticMappings_Protocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 5),
    _NatProfile_StaticMappings_Protocol_Type()
)
natProfile_StaticMappings_Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_Protocol.setStatus("mandatory")
_NatProfile_StaticMappings_LocalPort_Type = Integer32
_NatProfile_StaticMappings_LocalPort_Object = MibScalar
natProfile_StaticMappings_LocalPort = _NatProfile_StaticMappings_LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 6),
    _NatProfile_StaticMappings_LocalPort_Type()
)
natProfile_StaticMappings_LocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_LocalPort.setStatus("mandatory")
_NatProfile_StaticMappings_LocalAddress_Type = IpAddress
_NatProfile_StaticMappings_LocalAddress_Object = MibScalar
natProfile_StaticMappings_LocalAddress = _NatProfile_StaticMappings_LocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 7),
    _NatProfile_StaticMappings_LocalAddress_Type()
)
natProfile_StaticMappings_LocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_LocalAddress.setStatus("mandatory")
_NatProfile_StaticMappings_NatProfile_Type = DisplayString
_NatProfile_StaticMappings_NatProfile_Object = MibScalar
natProfile_StaticMappings_NatProfile = _NatProfile_StaticMappings_NatProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 95, 2, 1, 8),
    _NatProfile_StaticMappings_NatProfile_Type()
)
natProfile_StaticMappings_NatProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natProfile_StaticMappings_NatProfile.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBNAT-MIB",
    **{"DisplayString": DisplayString,
       "mibnatProfile": mibnatProfile,
       "mibnatProfileTable": mibnatProfileTable,
       "mibnatProfileEntry": mibnatProfileEntry,
       "natProfile-NatRouting": natProfile_NatRouting,
       "natProfile-NatProfile": natProfile_NatProfile,
       "natProfile-NatLan": natProfile_NatLan,
       "natProfile-DefaultServer": natProfile_DefaultServer,
       "natProfile-TunnelServer": natProfile_TunnelServer,
       "natProfile-FrameRelayAddress": natProfile_FrameRelayAddress,
       "natProfile-StickyAddress": natProfile_StickyAddress,
       "natProfile-StickyTimeout": natProfile_StickyTimeout,
       "natProfile-NoNatAddress": natProfile_NoNatAddress,
       "natProfile-AlternateNaptAddress": natProfile_AlternateNaptAddress,
       "natProfile-NaptIdleTcpTimeout": natProfile_NaptIdleTcpTimeout,
       "natProfile-Action-o": natProfile_Action_o,
       "natProfile-NatAddrPoolNum": natProfile_NatAddrPoolNum,
       "mibnatProfile-StaticMappingsTable": mibnatProfile_StaticMappingsTable,
       "mibnatProfile-StaticMappingsEntry": mibnatProfile_StaticMappingsEntry,
       "natProfile-StaticMappings-Index-o": natProfile_StaticMappings_Index_o,
       "natProfile-StaticMappings-ValidEntry": natProfile_StaticMappings_ValidEntry,
       "natProfile-StaticMappings-DestPort": natProfile_StaticMappings_DestPort,
       "natProfile-StaticMappings-Protocol": natProfile_StaticMappings_Protocol,
       "natProfile-StaticMappings-LocalPort": natProfile_StaticMappings_LocalPort,
       "natProfile-StaticMappings-LocalAddress": natProfile_StaticMappings_LocalAddress,
       "natProfile-StaticMappings-NatProfile": natProfile_StaticMappings_NatProfile}
)
