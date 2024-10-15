# SNMP MIB module (CTRON-SFPS-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:26 2024
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

(sfpsMcastCnx,
 sfpsMcastCnxAPI,
 sfpsMcastConfigApi,
 sfpsMcastIPRIBApi,
 sfpsMcastIPReceiverInfoBase,
 sfpsMcastIPRouter,
 sfpsMcastIPSIBApi,
 sfpsMcastIPSenderInfoBase) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsMcastCnx",
    "sfpsMcastCnxAPI",
    "sfpsMcastConfigApi",
    "sfpsMcastIPRIBApi",
    "sfpsMcastIPReceiverInfoBase",
    "sfpsMcastIPRouter",
    "sfpsMcastIPSIBApi",
    "sfpsMcastIPSenderInfoBase")

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



class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsMcastCnxDestination_Type = SfpsAddress
_SfpsMcastCnxDestination_Object = MibScalar
sfpsMcastCnxDestination = _SfpsMcastCnxDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 1),
    _SfpsMcastCnxDestination_Type()
)
sfpsMcastCnxDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxDestination.setStatus("mandatory")
_SfpsMcastCnxSource_Type = SfpsAddress
_SfpsMcastCnxSource_Object = MibScalar
sfpsMcastCnxSource = _SfpsMcastCnxSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 2),
    _SfpsMcastCnxSource_Type()
)
sfpsMcastCnxSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxSource.setStatus("mandatory")
_SfpsMcastCnxSenderSw_Type = SfpsAddress
_SfpsMcastCnxSenderSw_Object = MibScalar
sfpsMcastCnxSenderSw = _SfpsMcastCnxSenderSw_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 3),
    _SfpsMcastCnxSenderSw_Type()
)
sfpsMcastCnxSenderSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxSenderSw.setStatus("mandatory")
_SfpsMcastCnxInPort_Type = Integer32
_SfpsMcastCnxInPort_Object = MibScalar
sfpsMcastCnxInPort = _SfpsMcastCnxInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 4),
    _SfpsMcastCnxInPort_Type()
)
sfpsMcastCnxInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxInPort.setStatus("mandatory")
_SfpsMcastCnxOutPorts_Type = DisplayString
_SfpsMcastCnxOutPorts_Object = MibScalar
sfpsMcastCnxOutPorts = _SfpsMcastCnxOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 5),
    _SfpsMcastCnxOutPorts_Type()
)
sfpsMcastCnxOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxOutPorts.setStatus("mandatory")
_SfpsMcastCnxGroup_Type = IpAddress
_SfpsMcastCnxGroup_Object = MibScalar
sfpsMcastCnxGroup = _SfpsMcastCnxGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 6),
    _SfpsMcastCnxGroup_Type()
)
sfpsMcastCnxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxGroup.setStatus("mandatory")
_SfpsMcastCnxTTL_Type = Integer32
_SfpsMcastCnxTTL_Object = MibScalar
sfpsMcastCnxTTL = _SfpsMcastCnxTTL_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 7),
    _SfpsMcastCnxTTL_Type()
)
sfpsMcastCnxTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxTTL.setStatus("deprecated")
_SfpsMcastCnxAge_Type = TimeTicks
_SfpsMcastCnxAge_Object = MibScalar
sfpsMcastCnxAge = _SfpsMcastCnxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 8),
    _SfpsMcastCnxAge_Type()
)
sfpsMcastCnxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAge.setStatus("mandatory")


class _SfpsMcastCnxStatus_Type(Integer32):
    """Custom type sfpsMcastCnxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              8,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("dying", 8),
          ("filter", 1),
          ("inActive", 2),
          ("netFilter", 5),
          ("remote", 4),
          ("static", 16),
          ("staticFilter", 17),
          ("staticInactive", 18))
    )


_SfpsMcastCnxStatus_Type.__name__ = "Integer32"
_SfpsMcastCnxStatus_Object = MibScalar
sfpsMcastCnxStatus = _SfpsMcastCnxStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 9),
    _SfpsMcastCnxStatus_Type()
)
sfpsMcastCnxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxStatus.setStatus("mandatory")
_SfpsMcastCnxNextSw_Type = SfpsAddress
_SfpsMcastCnxNextSw_Object = MibScalar
sfpsMcastCnxNextSw = _SfpsMcastCnxNextSw_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1, 10),
    _SfpsMcastCnxNextSw_Type()
)
sfpsMcastCnxNextSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxNextSw.setStatus("mandatory")
_SfpsMcastCnxAPIDestination_Type = SfpsAddress
_SfpsMcastCnxAPIDestination_Object = MibScalar
sfpsMcastCnxAPIDestination = _SfpsMcastCnxAPIDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 1),
    _SfpsMcastCnxAPIDestination_Type()
)
sfpsMcastCnxAPIDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPIDestination.setStatus("mandatory")
_SfpsMcastCnxAPISource_Type = SfpsAddress
_SfpsMcastCnxAPISource_Object = MibScalar
sfpsMcastCnxAPISource = _SfpsMcastCnxAPISource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 2),
    _SfpsMcastCnxAPISource_Type()
)
sfpsMcastCnxAPISource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPISource.setStatus("mandatory")
_SfpsMcastCnxAPISenderSw_Type = SfpsAddress
_SfpsMcastCnxAPISenderSw_Object = MibScalar
sfpsMcastCnxAPISenderSw = _SfpsMcastCnxAPISenderSw_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 3),
    _SfpsMcastCnxAPISenderSw_Type()
)
sfpsMcastCnxAPISenderSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPISenderSw.setStatus("mandatory")
_SfpsMcastCnxAPIInPort_Type = Integer32
_SfpsMcastCnxAPIInPort_Object = MibScalar
sfpsMcastCnxAPIInPort = _SfpsMcastCnxAPIInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 4),
    _SfpsMcastCnxAPIInPort_Type()
)
sfpsMcastCnxAPIInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPIInPort.setStatus("mandatory")
_SfpsMcastCnxAPIOutPort_Type = DisplayString
_SfpsMcastCnxAPIOutPort_Object = MibScalar
sfpsMcastCnxAPIOutPort = _SfpsMcastCnxAPIOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 5),
    _SfpsMcastCnxAPIOutPort_Type()
)
sfpsMcastCnxAPIOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPIOutPort.setStatus("mandatory")
_SfpsMcastCnxAPIGroup_Type = IpAddress
_SfpsMcastCnxAPIGroup_Object = MibScalar
sfpsMcastCnxAPIGroup = _SfpsMcastCnxAPIGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 6),
    _SfpsMcastCnxAPIGroup_Type()
)
sfpsMcastCnxAPIGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPIGroup.setStatus("mandatory")
_SfpsMcastCnxAPITTL_Type = Integer32
_SfpsMcastCnxAPITTL_Object = MibScalar
sfpsMcastCnxAPITTL = _SfpsMcastCnxAPITTL_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 7),
    _SfpsMcastCnxAPITTL_Type()
)
sfpsMcastCnxAPITTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPITTL.setStatus("deprecated")


class _SfpsMcastCnxAPIVerb_Type(Integer32):
    """Custom type sfpsMcastCnxAPIVerb based on Integer32"""
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
        *(("addCnx", 5),
          ("addFilter", 2),
          ("addPort", 3),
          ("delCnx", 6),
          ("delPort", 4),
          ("other", 1))
    )


_SfpsMcastCnxAPIVerb_Type.__name__ = "Integer32"
_SfpsMcastCnxAPIVerb_Object = MibScalar
sfpsMcastCnxAPIVerb = _SfpsMcastCnxAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 8),
    _SfpsMcastCnxAPIVerb_Type()
)
sfpsMcastCnxAPIVerb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPIVerb.setStatus("mandatory")
_SfpsMcastCnxAPIFilters_Type = Integer32
_SfpsMcastCnxAPIFilters_Object = MibScalar
sfpsMcastCnxAPIFilters = _SfpsMcastCnxAPIFilters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 9),
    _SfpsMcastCnxAPIFilters_Type()
)
sfpsMcastCnxAPIFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPIFilters.setStatus("mandatory")
_SfpsMcastCnxAPINonFilters_Type = Integer32
_SfpsMcastCnxAPINonFilters_Object = MibScalar
sfpsMcastCnxAPINonFilters = _SfpsMcastCnxAPINonFilters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2, 10),
    _SfpsMcastCnxAPINonFilters_Type()
)
sfpsMcastCnxAPINonFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastCnxAPINonFilters.setStatus("mandatory")
_SfpsMcastIPRouterTable_Object = MibTable
sfpsMcastIPRouterTable = _SfpsMcastIPRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsMcastIPRouterTable.setStatus("mandatory")
_SfpsMcastIPRouterEntry_Object = MibTableRow
sfpsMcastIPRouterEntry = _SfpsMcastIPRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 1, 1)
)
sfpsMcastIPRouterEntry.setIndexNames(
    (0, "CTRON-SFPS-MCAST-MIB", "sfpsMcastIPRouterIfNum"),
)
if mibBuilder.loadTexts:
    sfpsMcastIPRouterEntry.setStatus("mandatory")
_SfpsMcastIPRouterIfNum_Type = Integer32
_SfpsMcastIPRouterIfNum_Object = MibTableColumn
sfpsMcastIPRouterIfNum = _SfpsMcastIPRouterIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 1, 1, 1),
    _SfpsMcastIPRouterIfNum_Type()
)
sfpsMcastIPRouterIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterIfNum.setStatus("mandatory")
_SfpsMcastIPRouterVlanId_Type = Integer32
_SfpsMcastIPRouterVlanId_Object = MibTableColumn
sfpsMcastIPRouterVlanId = _SfpsMcastIPRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 1, 1, 2),
    _SfpsMcastIPRouterVlanId_Type()
)
sfpsMcastIPRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterVlanId.setStatus("mandatory")
_SfpsMcastIPRouterRouterIP_Type = IpAddress
_SfpsMcastIPRouterRouterIP_Object = MibTableColumn
sfpsMcastIPRouterRouterIP = _SfpsMcastIPRouterRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 1, 1, 3),
    _SfpsMcastIPRouterRouterIP_Type()
)
sfpsMcastIPRouterRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterRouterIP.setStatus("mandatory")
_SfpsMcastIPRouterTTL_Type = Integer32
_SfpsMcastIPRouterTTL_Object = MibTableColumn
sfpsMcastIPRouterTTL = _SfpsMcastIPRouterTTL_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 1, 1, 4),
    _SfpsMcastIPRouterTTL_Type()
)
sfpsMcastIPRouterTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterTTL.setStatus("deprecated")


class _SfpsMcastIPRouterAPIVerb_Type(Integer32):
    """Custom type sfpsMcastIPRouterAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("portMap", 2),
          ("portUnmap", 3))
    )


_SfpsMcastIPRouterAPIVerb_Type.__name__ = "Integer32"
_SfpsMcastIPRouterAPIVerb_Object = MibScalar
sfpsMcastIPRouterAPIVerb = _SfpsMcastIPRouterAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 2),
    _SfpsMcastIPRouterAPIVerb_Type()
)
sfpsMcastIPRouterAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterAPIVerb.setStatus("mandatory")
_SfpsMcastIPRouterAPIIFNum_Type = Integer32
_SfpsMcastIPRouterAPIIFNum_Object = MibScalar
sfpsMcastIPRouterAPIIFNum = _SfpsMcastIPRouterAPIIFNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 3),
    _SfpsMcastIPRouterAPIIFNum_Type()
)
sfpsMcastIPRouterAPIIFNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterAPIIFNum.setStatus("mandatory")
_SfpsMcastIPRouterAPIRouterIP_Type = IpAddress
_SfpsMcastIPRouterAPIRouterIP_Object = MibScalar
sfpsMcastIPRouterAPIRouterIP = _SfpsMcastIPRouterAPIRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 4),
    _SfpsMcastIPRouterAPIRouterIP_Type()
)
sfpsMcastIPRouterAPIRouterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterAPIRouterIP.setStatus("mandatory")


class _SfpsMcastIPRouterAPITTLScope_Type(Integer32):
    """Custom type sfpsMcastIPRouterAPITTLScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              16,
              64,
              128,
              192,
              255)
        )
    )
    namedValues = NamedValues(
        *(("region", 64),
          ("site", 16),
          ("subnet", 1),
          ("unrestricted", 255),
          ("vacinity", 4),
          ("world", 128),
          ("worldLimited", 192))
    )


_SfpsMcastIPRouterAPITTLScope_Type.__name__ = "Integer32"
_SfpsMcastIPRouterAPITTLScope_Object = MibScalar
sfpsMcastIPRouterAPITTLScope = _SfpsMcastIPRouterAPITTLScope_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 5),
    _SfpsMcastIPRouterAPITTLScope_Type()
)
sfpsMcastIPRouterAPITTLScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterAPITTLScope.setStatus("deprecated")
_SfpsMcastIPRouterAPIVlanId_Type = Integer32
_SfpsMcastIPRouterAPIVlanId_Object = MibScalar
sfpsMcastIPRouterAPIVlanId = _SfpsMcastIPRouterAPIVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1, 6),
    _SfpsMcastIPRouterAPIVlanId_Type()
)
sfpsMcastIPRouterAPIVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPRouterAPIVlanId.setStatus("mandatory")
_SfpsMcastIPRIBTable_Object = MibTable
sfpsMcastIPRIBTable = _SfpsMcastIPRIBTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsMcastIPRIBTable.setStatus("mandatory")
_SfpsMcastIPRIBEntry_Object = MibTableRow
sfpsMcastIPRIBEntry = _SfpsMcastIPRIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1, 1)
)
sfpsMcastIPRIBEntry.setIndexNames(
    (0, "CTRON-SFPS-MCAST-MIB", "sfpsMcastIPRIBGroup"),
)
if mibBuilder.loadTexts:
    sfpsMcastIPRIBEntry.setStatus("mandatory")
_SfpsMcastIPRIBGroup_Type = IpAddress
_SfpsMcastIPRIBGroup_Object = MibTableColumn
sfpsMcastIPRIBGroup = _SfpsMcastIPRIBGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1, 1, 1),
    _SfpsMcastIPRIBGroup_Type()
)
sfpsMcastIPRIBGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBGroup.setStatus("mandatory")


class _SfpsMcastIPRIBOrigin_Type(Integer32):
    """Custom type sfpsMcastIPRIBOrigin based on Integer32"""
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
        *(("igmp", 4),
          ("local", 2),
          ("netMgt", 5),
          ("other", 1),
          ("router", 3))
    )


_SfpsMcastIPRIBOrigin_Type.__name__ = "Integer32"
_SfpsMcastIPRIBOrigin_Object = MibTableColumn
sfpsMcastIPRIBOrigin = _SfpsMcastIPRIBOrigin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1, 1, 2),
    _SfpsMcastIPRIBOrigin_Type()
)
sfpsMcastIPRIBOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBOrigin.setStatus("mandatory")


class _SfpsMcastIPRIBInclusion_Type(Integer32):
    """Custom type sfpsMcastIPRIBInclusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_SfpsMcastIPRIBInclusion_Type.__name__ = "Integer32"
_SfpsMcastIPRIBInclusion_Object = MibTableColumn
sfpsMcastIPRIBInclusion = _SfpsMcastIPRIBInclusion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1, 1, 3),
    _SfpsMcastIPRIBInclusion_Type()
)
sfpsMcastIPRIBInclusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBInclusion.setStatus("mandatory")
_SfpsMcastIPRIBRcvPorts_Type = OctetString
_SfpsMcastIPRIBRcvPorts_Object = MibTableColumn
sfpsMcastIPRIBRcvPorts = _SfpsMcastIPRIBRcvPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1, 1, 4),
    _SfpsMcastIPRIBRcvPorts_Type()
)
sfpsMcastIPRIBRcvPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBRcvPorts.setStatus("mandatory")
_SfpsMcastIPRIBAge_Type = Integer32
_SfpsMcastIPRIBAge_Object = MibTableColumn
sfpsMcastIPRIBAge = _SfpsMcastIPRIBAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 1, 1, 5),
    _SfpsMcastIPRIBAge_Type()
)
sfpsMcastIPRIBAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBAge.setStatus("mandatory")
_SfpsMcastIPRIBApiGroup_Type = IpAddress
_SfpsMcastIPRIBApiGroup_Object = MibScalar
sfpsMcastIPRIBApiGroup = _SfpsMcastIPRIBApiGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 2, 1),
    _SfpsMcastIPRIBApiGroup_Type()
)
sfpsMcastIPRIBApiGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBApiGroup.setStatus("mandatory")
_SfpsMcastIPRIBApiPort_Type = Integer32
_SfpsMcastIPRIBApiPort_Object = MibScalar
sfpsMcastIPRIBApiPort = _SfpsMcastIPRIBApiPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 2, 2),
    _SfpsMcastIPRIBApiPort_Type()
)
sfpsMcastIPRIBApiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBApiPort.setStatus("mandatory")


class _SfpsMcastIPRIBApiVerb_Type(Integer32):
    """Custom type sfpsMcastIPRIBApiVerb based on Integer32"""
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
        *(("excludePort", 3),
          ("includePort", 1),
          ("undoExclude", 4),
          ("undoInclude", 2))
    )


_SfpsMcastIPRIBApiVerb_Type.__name__ = "Integer32"
_SfpsMcastIPRIBApiVerb_Object = MibScalar
sfpsMcastIPRIBApiVerb = _SfpsMcastIPRIBApiVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 2, 3),
    _SfpsMcastIPRIBApiVerb_Type()
)
sfpsMcastIPRIBApiVerb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPRIBApiVerb.setStatus("mandatory")
_SfpsMcastIPSIBTable_Object = MibTable
sfpsMcastIPSIBTable = _SfpsMcastIPSIBTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsMcastIPSIBTable.setStatus("mandatory")
_SfpsMcastIPSIBEntry_Object = MibTableRow
sfpsMcastIPSIBEntry = _SfpsMcastIPSIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 1, 1)
)
sfpsMcastIPSIBEntry.setIndexNames(
    (0, "CTRON-SFPS-MCAST-MIB", "sfpsMcastIPSIBGroup"),
    (0, "CTRON-SFPS-MCAST-MIB", "sfpsMcastIPSIBSender"),
)
if mibBuilder.loadTexts:
    sfpsMcastIPSIBEntry.setStatus("mandatory")
_SfpsMcastIPSIBGroup_Type = IpAddress
_SfpsMcastIPSIBGroup_Object = MibTableColumn
sfpsMcastIPSIBGroup = _SfpsMcastIPSIBGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 1, 1, 1),
    _SfpsMcastIPSIBGroup_Type()
)
sfpsMcastIPSIBGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPSIBGroup.setStatus("mandatory")
_SfpsMcastIPSIBSender_Type = OctetString
_SfpsMcastIPSIBSender_Object = MibTableColumn
sfpsMcastIPSIBSender = _SfpsMcastIPSIBSender_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 1, 1, 2),
    _SfpsMcastIPSIBSender_Type()
)
sfpsMcastIPSIBSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPSIBSender.setStatus("mandatory")


class _SfpsMcastIPSIBInclusion_Type(Integer32):
    """Custom type sfpsMcastIPSIBInclusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_SfpsMcastIPSIBInclusion_Type.__name__ = "Integer32"
_SfpsMcastIPSIBInclusion_Object = MibTableColumn
sfpsMcastIPSIBInclusion = _SfpsMcastIPSIBInclusion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 1, 1, 3),
    _SfpsMcastIPSIBInclusion_Type()
)
sfpsMcastIPSIBInclusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPSIBInclusion.setStatus("mandatory")
_SfpsMcastIPSIBAge_Type = Integer32
_SfpsMcastIPSIBAge_Object = MibTableColumn
sfpsMcastIPSIBAge = _SfpsMcastIPSIBAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 1, 1, 4),
    _SfpsMcastIPSIBAge_Type()
)
sfpsMcastIPSIBAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastIPSIBAge.setStatus("mandatory")
_SfpsMcastIPSibApiGroup_Type = IpAddress
_SfpsMcastIPSibApiGroup_Object = MibScalar
sfpsMcastIPSibApiGroup = _SfpsMcastIPSibApiGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 2, 1),
    _SfpsMcastIPSibApiGroup_Type()
)
sfpsMcastIPSibApiGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPSibApiGroup.setStatus("mandatory")
_SfpsMcastIPSibApiSender_Type = SfpsAddress
_SfpsMcastIPSibApiSender_Object = MibScalar
sfpsMcastIPSibApiSender = _SfpsMcastIPSibApiSender_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 2, 2),
    _SfpsMcastIPSibApiSender_Type()
)
sfpsMcastIPSibApiSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPSibApiSender.setStatus("mandatory")


class _SfpsMcastIPSibApiVerb_Type(Integer32):
    """Custom type sfpsMcastIPSibApiVerb based on Integer32"""
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
        *(("excludeSender", 3),
          ("includeSender", 1),
          ("reset", 5),
          ("undoExclude", 4),
          ("undoInclude", 2))
    )


_SfpsMcastIPSibApiVerb_Type.__name__ = "Integer32"
_SfpsMcastIPSibApiVerb_Object = MibScalar
sfpsMcastIPSibApiVerb = _SfpsMcastIPSibApiVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 2, 3),
    _SfpsMcastIPSibApiVerb_Type()
)
sfpsMcastIPSibApiVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMcastIPSibApiVerb.setStatus("mandatory")
_SfpsMcastConfigApiSenderTableSize_Type = Integer32
_SfpsMcastConfigApiSenderTableSize_Object = MibScalar
sfpsMcastConfigApiSenderTableSize = _SfpsMcastConfigApiSenderTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 1),
    _SfpsMcastConfigApiSenderTableSize_Type()
)
sfpsMcastConfigApiSenderTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiSenderTableSize.setStatus("mandatory")
_SfpsMcastConfigApiMaxNonFilters_Type = Integer32
_SfpsMcastConfigApiMaxNonFilters_Object = MibScalar
sfpsMcastConfigApiMaxNonFilters = _SfpsMcastConfigApiMaxNonFilters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 2),
    _SfpsMcastConfigApiMaxNonFilters_Type()
)
sfpsMcastConfigApiMaxNonFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiMaxNonFilters.setStatus("mandatory")
_SfpsMcastConfigApiRDRetryBuffs_Type = Integer32
_SfpsMcastConfigApiRDRetryBuffs_Object = MibScalar
sfpsMcastConfigApiRDRetryBuffs = _SfpsMcastConfigApiRDRetryBuffs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 3),
    _SfpsMcastConfigApiRDRetryBuffs_Type()
)
sfpsMcastConfigApiRDRetryBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiRDRetryBuffs.setStatus("mandatory")
_SfpsMcastConfigApiRDPktBuffs_Type = Integer32
_SfpsMcastConfigApiRDPktBuffs_Object = MibScalar
sfpsMcastConfigApiRDPktBuffs = _SfpsMcastConfigApiRDPktBuffs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 4),
    _SfpsMcastConfigApiRDPktBuffs_Type()
)
sfpsMcastConfigApiRDPktBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiRDPktBuffs.setStatus("mandatory")
_SfpsMcastConfigApiPendingMaps_Type = Integer32
_SfpsMcastConfigApiPendingMaps_Object = MibScalar
sfpsMcastConfigApiPendingMaps = _SfpsMcastConfigApiPendingMaps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 5),
    _SfpsMcastConfigApiPendingMaps_Type()
)
sfpsMcastConfigApiPendingMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiPendingMaps.setStatus("mandatory")
_SfpsMcastConfigApiSndrAgeOut_Type = Integer32
_SfpsMcastConfigApiSndrAgeOut_Object = MibScalar
sfpsMcastConfigApiSndrAgeOut = _SfpsMcastConfigApiSndrAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 6),
    _SfpsMcastConfigApiSndrAgeOut_Type()
)
sfpsMcastConfigApiSndrAgeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiSndrAgeOut.setStatus("mandatory")
_SfpsMcastConfigApiRefreshInterval_Type = Integer32
_SfpsMcastConfigApiRefreshInterval_Object = MibScalar
sfpsMcastConfigApiRefreshInterval = _SfpsMcastConfigApiRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 7),
    _SfpsMcastConfigApiRefreshInterval_Type()
)
sfpsMcastConfigApiRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiRefreshInterval.setStatus("mandatory")
_SfpsMcastConfigApiSndersPerAncmt_Type = Integer32
_SfpsMcastConfigApiSndersPerAncmt_Object = MibScalar
sfpsMcastConfigApiSndersPerAncmt = _SfpsMcastConfigApiSndersPerAncmt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 8),
    _SfpsMcastConfigApiSndersPerAncmt_Type()
)
sfpsMcastConfigApiSndersPerAncmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiSndersPerAncmt.setStatus("mandatory")
_SfpsMcastConfigApiDebugLog_Type = Integer32
_SfpsMcastConfigApiDebugLog_Object = MibScalar
sfpsMcastConfigApiDebugLog = _SfpsMcastConfigApiDebugLog_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 9),
    _SfpsMcastConfigApiDebugLog_Type()
)
sfpsMcastConfigApiDebugLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiDebugLog.setStatus("mandatory")
_SfpsMcastConfigApiStaticTblSize_Type = Integer32
_SfpsMcastConfigApiStaticTblSize_Object = MibScalar
sfpsMcastConfigApiStaticTblSize = _SfpsMcastConfigApiStaticTblSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 10),
    _SfpsMcastConfigApiStaticTblSize_Type()
)
sfpsMcastConfigApiStaticTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiStaticTblSize.setStatus("mandatory")
_SfpsMcastConfigApiMcribSize_Type = Integer32
_SfpsMcastConfigApiMcribSize_Object = MibScalar
sfpsMcastConfigApiMcribSize = _SfpsMcastConfigApiMcribSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 11),
    _SfpsMcastConfigApiMcribSize_Type()
)
sfpsMcastConfigApiMcribSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiMcribSize.setStatus("mandatory")


class _SfpsMcastConfigApiMcastMode_Type(Integer32):
    """Custom type sfpsMcastConfigApiMcastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkAll", 3),
          ("doNoVlanChecking", 1),
          ("doSomeVlanChecking", 2))
    )


_SfpsMcastConfigApiMcastMode_Type.__name__ = "Integer32"
_SfpsMcastConfigApiMcastMode_Object = MibScalar
sfpsMcastConfigApiMcastMode = _SfpsMcastConfigApiMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 12),
    _SfpsMcastConfigApiMcastMode_Type()
)
sfpsMcastConfigApiMcastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiMcastMode.setStatus("mandatory")
_SfpsMcastConfigApiRemapDelay_Type = Integer32
_SfpsMcastConfigApiRemapDelay_Object = MibScalar
sfpsMcastConfigApiRemapDelay = _SfpsMcastConfigApiRemapDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 13),
    _SfpsMcastConfigApiRemapDelay_Type()
)
sfpsMcastConfigApiRemapDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiRemapDelay.setStatus("mandatory")
_SfpsMcastConfigApiQHighLimit_Type = Integer32
_SfpsMcastConfigApiQHighLimit_Object = MibScalar
sfpsMcastConfigApiQHighLimit = _SfpsMcastConfigApiQHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 14),
    _SfpsMcastConfigApiQHighLimit_Type()
)
sfpsMcastConfigApiQHighLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiQHighLimit.setStatus("mandatory")
_SfpsMcastConfigApiQLowLimit_Type = Integer32
_SfpsMcastConfigApiQLowLimit_Object = MibScalar
sfpsMcastConfigApiQLowLimit = _SfpsMcastConfigApiQLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 15),
    _SfpsMcastConfigApiQLowLimit_Type()
)
sfpsMcastConfigApiQLowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiQLowLimit.setStatus("mandatory")
_SfpsMcastConfigApiDynamicQuery_Type = Integer32
_SfpsMcastConfigApiDynamicQuery_Object = MibScalar
sfpsMcastConfigApiDynamicQuery = _SfpsMcastConfigApiDynamicQuery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1, 16),
    _SfpsMcastConfigApiDynamicQuery_Type()
)
sfpsMcastConfigApiDynamicQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMcastConfigApiDynamicQuery.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-MCAST-MIB",
    **{"SfpsAddress": SfpsAddress,
       "sfpsMcastCnxDestination": sfpsMcastCnxDestination,
       "sfpsMcastCnxSource": sfpsMcastCnxSource,
       "sfpsMcastCnxSenderSw": sfpsMcastCnxSenderSw,
       "sfpsMcastCnxInPort": sfpsMcastCnxInPort,
       "sfpsMcastCnxOutPorts": sfpsMcastCnxOutPorts,
       "sfpsMcastCnxGroup": sfpsMcastCnxGroup,
       "sfpsMcastCnxTTL": sfpsMcastCnxTTL,
       "sfpsMcastCnxAge": sfpsMcastCnxAge,
       "sfpsMcastCnxStatus": sfpsMcastCnxStatus,
       "sfpsMcastCnxNextSw": sfpsMcastCnxNextSw,
       "sfpsMcastCnxAPIDestination": sfpsMcastCnxAPIDestination,
       "sfpsMcastCnxAPISource": sfpsMcastCnxAPISource,
       "sfpsMcastCnxAPISenderSw": sfpsMcastCnxAPISenderSw,
       "sfpsMcastCnxAPIInPort": sfpsMcastCnxAPIInPort,
       "sfpsMcastCnxAPIOutPort": sfpsMcastCnxAPIOutPort,
       "sfpsMcastCnxAPIGroup": sfpsMcastCnxAPIGroup,
       "sfpsMcastCnxAPITTL": sfpsMcastCnxAPITTL,
       "sfpsMcastCnxAPIVerb": sfpsMcastCnxAPIVerb,
       "sfpsMcastCnxAPIFilters": sfpsMcastCnxAPIFilters,
       "sfpsMcastCnxAPINonFilters": sfpsMcastCnxAPINonFilters,
       "sfpsMcastIPRouterTable": sfpsMcastIPRouterTable,
       "sfpsMcastIPRouterEntry": sfpsMcastIPRouterEntry,
       "sfpsMcastIPRouterIfNum": sfpsMcastIPRouterIfNum,
       "sfpsMcastIPRouterVlanId": sfpsMcastIPRouterVlanId,
       "sfpsMcastIPRouterRouterIP": sfpsMcastIPRouterRouterIP,
       "sfpsMcastIPRouterTTL": sfpsMcastIPRouterTTL,
       "sfpsMcastIPRouterAPIVerb": sfpsMcastIPRouterAPIVerb,
       "sfpsMcastIPRouterAPIIFNum": sfpsMcastIPRouterAPIIFNum,
       "sfpsMcastIPRouterAPIRouterIP": sfpsMcastIPRouterAPIRouterIP,
       "sfpsMcastIPRouterAPITTLScope": sfpsMcastIPRouterAPITTLScope,
       "sfpsMcastIPRouterAPIVlanId": sfpsMcastIPRouterAPIVlanId,
       "sfpsMcastIPRIBTable": sfpsMcastIPRIBTable,
       "sfpsMcastIPRIBEntry": sfpsMcastIPRIBEntry,
       "sfpsMcastIPRIBGroup": sfpsMcastIPRIBGroup,
       "sfpsMcastIPRIBOrigin": sfpsMcastIPRIBOrigin,
       "sfpsMcastIPRIBInclusion": sfpsMcastIPRIBInclusion,
       "sfpsMcastIPRIBRcvPorts": sfpsMcastIPRIBRcvPorts,
       "sfpsMcastIPRIBAge": sfpsMcastIPRIBAge,
       "sfpsMcastIPRIBApiGroup": sfpsMcastIPRIBApiGroup,
       "sfpsMcastIPRIBApiPort": sfpsMcastIPRIBApiPort,
       "sfpsMcastIPRIBApiVerb": sfpsMcastIPRIBApiVerb,
       "sfpsMcastIPSIBTable": sfpsMcastIPSIBTable,
       "sfpsMcastIPSIBEntry": sfpsMcastIPSIBEntry,
       "sfpsMcastIPSIBGroup": sfpsMcastIPSIBGroup,
       "sfpsMcastIPSIBSender": sfpsMcastIPSIBSender,
       "sfpsMcastIPSIBInclusion": sfpsMcastIPSIBInclusion,
       "sfpsMcastIPSIBAge": sfpsMcastIPSIBAge,
       "sfpsMcastIPSibApiGroup": sfpsMcastIPSibApiGroup,
       "sfpsMcastIPSibApiSender": sfpsMcastIPSibApiSender,
       "sfpsMcastIPSibApiVerb": sfpsMcastIPSibApiVerb,
       "sfpsMcastConfigApiSenderTableSize": sfpsMcastConfigApiSenderTableSize,
       "sfpsMcastConfigApiMaxNonFilters": sfpsMcastConfigApiMaxNonFilters,
       "sfpsMcastConfigApiRDRetryBuffs": sfpsMcastConfigApiRDRetryBuffs,
       "sfpsMcastConfigApiRDPktBuffs": sfpsMcastConfigApiRDPktBuffs,
       "sfpsMcastConfigApiPendingMaps": sfpsMcastConfigApiPendingMaps,
       "sfpsMcastConfigApiSndrAgeOut": sfpsMcastConfigApiSndrAgeOut,
       "sfpsMcastConfigApiRefreshInterval": sfpsMcastConfigApiRefreshInterval,
       "sfpsMcastConfigApiSndersPerAncmt": sfpsMcastConfigApiSndersPerAncmt,
       "sfpsMcastConfigApiDebugLog": sfpsMcastConfigApiDebugLog,
       "sfpsMcastConfigApiStaticTblSize": sfpsMcastConfigApiStaticTblSize,
       "sfpsMcastConfigApiMcribSize": sfpsMcastConfigApiMcribSize,
       "sfpsMcastConfigApiMcastMode": sfpsMcastConfigApiMcastMode,
       "sfpsMcastConfigApiRemapDelay": sfpsMcastConfigApiRemapDelay,
       "sfpsMcastConfigApiQHighLimit": sfpsMcastConfigApiQHighLimit,
       "sfpsMcastConfigApiQLowLimit": sfpsMcastConfigApiQLowLimit,
       "sfpsMcastConfigApiDynamicQuery": sfpsMcastConfigApiDynamicQuery}
)
