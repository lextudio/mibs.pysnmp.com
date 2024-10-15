# SNMP MIB module (CISCO-ATM-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:49 2024
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

(atmInterfaceConfEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceConfEntry")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoAtmIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 14)
)
ciscoAtmIfMIB.setRevisions(
        ("2002-02-13 00:00",
         "2001-08-08 00:00",
         "2001-05-21 00:00",
         "2000-04-11 00:00",
         "1999-03-11 00:00",
         "1997-11-30 00:00",
         "1997-09-10 00:00",
         "1996-11-01 00:00",
         "1996-10-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NsapAtmAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



class AtmAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )



class UpcMethod(Integer32, TextualConvention):
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
        *(("dropping", 3),
          ("passing", 1),
          ("tagging", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmIfMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoAtmIfMIBNotifications = _CiscoAtmIfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 0)
)
_CiscoAtmIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmIfMIBObjects = _CiscoAtmIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1)
)
_CiscoAtmIfTable_Object = MibTable
ciscoAtmIfTable = _CiscoAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmIfTable.setStatus("current")
_CiscoAtmIfEntry_Object = MibTableRow
ciscoAtmIfEntry = _CiscoAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmIfEntry.setStatus("current")


class _CiscoAtmIfType_Type(Integer32):
    """Custom type ciscoAtmIfType based on Integer32"""
    defaultValue = 2

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
        *(("aini", 6),
          ("iisp", 4),
          ("nniPvcOnly", 5),
          ("other", 1),
          ("pnni", 3),
          ("uni", 2))
    )


_CiscoAtmIfType_Type.__name__ = "Integer32"
_CiscoAtmIfType_Object = MibTableColumn
ciscoAtmIfType = _CiscoAtmIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 1),
    _CiscoAtmIfType_Type()
)
ciscoAtmIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfType.setStatus("current")


class _CiscoAtmIfSide_Type(Integer32):
    """Custom type ciscoAtmIfSide based on Integer32"""
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
        *(("network", 2),
          ("notApplicable", 3),
          ("user", 1))
    )


_CiscoAtmIfSide_Type.__name__ = "Integer32"
_CiscoAtmIfSide_Object = MibTableColumn
ciscoAtmIfSide = _CiscoAtmIfSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 2),
    _CiscoAtmIfSide_Type()
)
ciscoAtmIfSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSide.setStatus("current")


class _CiscoAtmIfUniType_Type(Integer32):
    """Custom type ciscoAtmIfUniType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_CiscoAtmIfUniType_Type.__name__ = "Integer32"
_CiscoAtmIfUniType_Object = MibTableColumn
ciscoAtmIfUniType = _CiscoAtmIfUniType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 3),
    _CiscoAtmIfUniType_Type()
)
ciscoAtmIfUniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfUniType.setStatus("current")


class _CiscoAtmIfPVPs_Type(Integer32):
    """Custom type ciscoAtmIfPVPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoAtmIfPVPs_Type.__name__ = "Integer32"
_CiscoAtmIfPVPs_Object = MibTableColumn
ciscoAtmIfPVPs = _CiscoAtmIfPVPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 4),
    _CiscoAtmIfPVPs_Type()
)
ciscoAtmIfPVPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPVPs.setStatus("current")


class _CiscoAtmIfPVCs_Type(Integer32):
    """Custom type ciscoAtmIfPVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmIfPVCs_Type.__name__ = "Integer32"
_CiscoAtmIfPVCs_Object = MibTableColumn
ciscoAtmIfPVCs = _CiscoAtmIfPVCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 5),
    _CiscoAtmIfPVCs_Type()
)
ciscoAtmIfPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPVCs.setStatus("current")
_CiscoAtmIfActiveSVPs_Type = Gauge32
_CiscoAtmIfActiveSVPs_Object = MibTableColumn
ciscoAtmIfActiveSVPs = _CiscoAtmIfActiveSVPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 6),
    _CiscoAtmIfActiveSVPs_Type()
)
ciscoAtmIfActiveSVPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfActiveSVPs.setStatus("current")
_CiscoAtmIfActiveSVCs_Type = Gauge32
_CiscoAtmIfActiveSVCs_Object = MibTableColumn
ciscoAtmIfActiveSVCs = _CiscoAtmIfActiveSVCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 7),
    _CiscoAtmIfActiveSVCs_Type()
)
ciscoAtmIfActiveSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfActiveSVCs.setStatus("current")
_CiscoAtmIfTotalConnections_Type = Gauge32
_CiscoAtmIfTotalConnections_Object = MibTableColumn
ciscoAtmIfTotalConnections = _CiscoAtmIfTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 8),
    _CiscoAtmIfTotalConnections_Type()
)
ciscoAtmIfTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfTotalConnections.setStatus("current")


class _CiscoAtmIfConfVplIf_Type(Integer32):
    """Custom type ciscoAtmIfConfVplIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmIfConfVplIf_Type.__name__ = "Integer32"
_CiscoAtmIfConfVplIf_Object = MibTableColumn
ciscoAtmIfConfVplIf = _CiscoAtmIfConfVplIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 9),
    _CiscoAtmIfConfVplIf_Type()
)
ciscoAtmIfConfVplIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfConfVplIf.setStatus("current")


class _CiscoAtmIfPortType_Type(Integer32):
    """Custom type ciscoAtmIfPortType based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("atm25", 25),
          ("cpu", 2),
          ("ds1", 10),
          ("ds3", 8),
          ("e1", 11),
          ("e3", 9),
          ("ethernet", 3),
          ("oc12MultiModeFiber", 18),
          ("oc12Pof", 22),
          ("oc12SingleModeFiber", 7),
          ("oc12SmIr", 19),
          ("oc12SmIrPlus", 20),
          ("oc12SmLr", 21),
          ("oc12SmLr2", 23),
          ("oc12SmLr3", 24),
          ("oc3MultiModeFiber", 6),
          ("oc3Pof", 17),
          ("oc3SingleModeFiber", 5),
          ("oc3SmIr", 14),
          ("oc3SmIrPlus", 15),
          ("oc3SmLr", 16),
          ("oc3Utp", 4),
          ("oc3Utp3", 12),
          ("oc3Utp5", 13),
          ("other", 1))
    )


_CiscoAtmIfPortType_Type.__name__ = "Integer32"
_CiscoAtmIfPortType_Object = MibTableColumn
ciscoAtmIfPortType = _CiscoAtmIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 10),
    _CiscoAtmIfPortType_Type()
)
ciscoAtmIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPortType.setStatus("current")


class _CiscoAtmIfXmitLed_Type(Integer32):
    """Custom type ciscoAtmIfXmitLed based on Integer32"""
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
        *(("flashGreen", 5),
          ("flashRed", 7),
          ("flashYellow", 6),
          ("off", 1),
          ("steadyGreen", 2),
          ("steadyRed", 4),
          ("steadyYellow", 3))
    )


_CiscoAtmIfXmitLed_Type.__name__ = "Integer32"
_CiscoAtmIfXmitLed_Object = MibTableColumn
ciscoAtmIfXmitLed = _CiscoAtmIfXmitLed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 11),
    _CiscoAtmIfXmitLed_Type()
)
ciscoAtmIfXmitLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfXmitLed.setStatus("current")


class _CiscoAtmIfRecvLed_Type(Integer32):
    """Custom type ciscoAtmIfRecvLed based on Integer32"""
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
        *(("flashGreen", 5),
          ("flashRed", 7),
          ("flashYellow", 6),
          ("off", 1),
          ("steadyGreen", 2),
          ("steadyRed", 4),
          ("steadyYellow", 3))
    )


_CiscoAtmIfRecvLed_Type.__name__ = "Integer32"
_CiscoAtmIfRecvLed_Object = MibTableColumn
ciscoAtmIfRecvLed = _CiscoAtmIfRecvLed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 12),
    _CiscoAtmIfRecvLed_Type()
)
ciscoAtmIfRecvLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfRecvLed.setStatus("current")
_CiscoAtmIfXmitCells_Type = Counter32
_CiscoAtmIfXmitCells_Object = MibTableColumn
ciscoAtmIfXmitCells = _CiscoAtmIfXmitCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 13),
    _CiscoAtmIfXmitCells_Type()
)
ciscoAtmIfXmitCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfXmitCells.setStatus("current")
_CiscoAtmIfRecvCells_Type = Counter32
_CiscoAtmIfRecvCells_Object = MibTableColumn
ciscoAtmIfRecvCells = _CiscoAtmIfRecvCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 14),
    _CiscoAtmIfRecvCells_Type()
)
ciscoAtmIfRecvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfRecvCells.setStatus("current")


class _CiscoAtmIfSvcMinVci_Type(Integer32):
    """Custom type ciscoAtmIfSvcMinVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoAtmIfSvcMinVci_Type.__name__ = "Integer32"
_CiscoAtmIfSvcMinVci_Object = MibTableColumn
ciscoAtmIfSvcMinVci = _CiscoAtmIfSvcMinVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 15),
    _CiscoAtmIfSvcMinVci_Type()
)
ciscoAtmIfSvcMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcMinVci.setStatus("deprecated")


class _CiscoAtmIfIlmiConfiguration_Type(Integer32):
    """Custom type ciscoAtmIfIlmiConfiguration based on Integer32"""
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


_CiscoAtmIfIlmiConfiguration_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiConfiguration_Object = MibTableColumn
ciscoAtmIfIlmiConfiguration = _CiscoAtmIfIlmiConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 16),
    _CiscoAtmIfIlmiConfiguration_Type()
)
ciscoAtmIfIlmiConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiConfiguration.setStatus("current")


class _CiscoAtmIfIlmiAddressRegistration_Type(Integer32):
    """Custom type ciscoAtmIfIlmiAddressRegistration based on Integer32"""
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


_CiscoAtmIfIlmiAddressRegistration_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiAddressRegistration_Object = MibTableColumn
ciscoAtmIfIlmiAddressRegistration = _CiscoAtmIfIlmiAddressRegistration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 17),
    _CiscoAtmIfIlmiAddressRegistration_Type()
)
ciscoAtmIfIlmiAddressRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiAddressRegistration.setStatus("current")


class _CiscoAtmIfIlmiAutoConfiguration_Type(Integer32):
    """Custom type ciscoAtmIfIlmiAutoConfiguration based on Integer32"""
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


_CiscoAtmIfIlmiAutoConfiguration_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiAutoConfiguration_Object = MibTableColumn
ciscoAtmIfIlmiAutoConfiguration = _CiscoAtmIfIlmiAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 18),
    _CiscoAtmIfIlmiAutoConfiguration_Type()
)
ciscoAtmIfIlmiAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiAutoConfiguration.setStatus("current")


class _CiscoAtmIfIlmiKeepAlive_Type(Integer32):
    """Custom type ciscoAtmIfIlmiKeepAlive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmIfIlmiKeepAlive_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiKeepAlive_Object = MibTableColumn
ciscoAtmIfIlmiKeepAlive = _CiscoAtmIfIlmiKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 19),
    _CiscoAtmIfIlmiKeepAlive_Type()
)
ciscoAtmIfIlmiKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiKeepAlive.setUnits("seconds")
_CiscoAtmIfSoftVcDestAddress_Type = NsapAtmAddr
_CiscoAtmIfSoftVcDestAddress_Object = MibTableColumn
ciscoAtmIfSoftVcDestAddress = _CiscoAtmIfSoftVcDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 20),
    _CiscoAtmIfSoftVcDestAddress_Type()
)
ciscoAtmIfSoftVcDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfSoftVcDestAddress.setStatus("current")


class _CiscoAtmIfUniSignallingVersion_Type(Integer32):
    """Custom type ciscoAtmIfUniSignallingVersion based on Integer32"""
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
        *(("atmfUni3Dot0", 2),
          ("atmfUni3Dot1", 3),
          ("atmfUni4Dot0", 4),
          ("notApplicable", 1))
    )


_CiscoAtmIfUniSignallingVersion_Type.__name__ = "Integer32"
_CiscoAtmIfUniSignallingVersion_Object = MibTableColumn
ciscoAtmIfUniSignallingVersion = _CiscoAtmIfUniSignallingVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 21),
    _CiscoAtmIfUniSignallingVersion_Type()
)
ciscoAtmIfUniSignallingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfUniSignallingVersion.setStatus("current")


class _CiscoAtmIfSvcUpcIntent_Type(Integer32):
    """Custom type ciscoAtmIfSvcUpcIntent based on Integer32"""
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
        *(("dropping", 3),
          ("passing", 1),
          ("tagging", 2))
    )


_CiscoAtmIfSvcUpcIntent_Type.__name__ = "Integer32"
_CiscoAtmIfSvcUpcIntent_Object = MibTableColumn
ciscoAtmIfSvcUpcIntent = _CiscoAtmIfSvcUpcIntent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 22),
    _CiscoAtmIfSvcUpcIntent_Type()
)
ciscoAtmIfSvcUpcIntent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcUpcIntent.setStatus("deprecated")


class _CiscoAtmIfAddressType_Type(Integer32):
    """Custom type ciscoAtmIfAddressType based on Integer32"""
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
        *(("e164", 3),
          ("esi", 2),
          ("nsap", 1),
          ("null", 4))
    )


_CiscoAtmIfAddressType_Type.__name__ = "Integer32"
_CiscoAtmIfAddressType_Object = MibTableColumn
ciscoAtmIfAddressType = _CiscoAtmIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 23),
    _CiscoAtmIfAddressType_Type()
)
ciscoAtmIfAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfAddressType.setStatus("obsolete")


class _CiscoAtmIfAddress_Type(OctetString):
    """Custom type ciscoAtmIfAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )


_CiscoAtmIfAddress_Type.__name__ = "OctetString"
_CiscoAtmIfAddress_Object = MibTableColumn
ciscoAtmIfAddress = _CiscoAtmIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 24),
    _CiscoAtmIfAddress_Type()
)
ciscoAtmIfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfAddress.setStatus("obsolete")


class _CiscoAtmIfWellKnownVcMode_Type(Integer32):
    """Custom type ciscoAtmIfWellKnownVcMode based on Integer32"""
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
        *(("automatic", 1),
          ("manual", 2),
          ("manualDeleteUponEntry", 3))
    )


_CiscoAtmIfWellKnownVcMode_Type.__name__ = "Integer32"
_CiscoAtmIfWellKnownVcMode_Object = MibTableColumn
ciscoAtmIfWellKnownVcMode = _CiscoAtmIfWellKnownVcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 31),
    _CiscoAtmIfWellKnownVcMode_Type()
)
ciscoAtmIfWellKnownVcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfWellKnownVcMode.setStatus("current")


class _CiscoAtmIfSignallingAdminStatus_Type(Integer32):
    """Custom type ciscoAtmIfSignallingAdminStatus based on Integer32"""
    defaultValue = 1

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


_CiscoAtmIfSignallingAdminStatus_Type.__name__ = "Integer32"
_CiscoAtmIfSignallingAdminStatus_Object = MibTableColumn
ciscoAtmIfSignallingAdminStatus = _CiscoAtmIfSignallingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 32),
    _CiscoAtmIfSignallingAdminStatus_Type()
)
ciscoAtmIfSignallingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSignallingAdminStatus.setStatus("current")


class _CiscoAtmIfCdLed_Type(Integer32):
    """Custom type ciscoAtmIfCdLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("steadyGreen", 2))
    )


_CiscoAtmIfCdLed_Type.__name__ = "Integer32"
_CiscoAtmIfCdLed_Object = MibTableColumn
ciscoAtmIfCdLed = _CiscoAtmIfCdLed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 33),
    _CiscoAtmIfCdLed_Type()
)
ciscoAtmIfCdLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfCdLed.setStatus("current")


class _CiscoAtmIfIlmiAccessFilter_Type(Integer32):
    """Custom type ciscoAtmIfIlmiAccessFilter based on Integer32"""
    defaultValue = 5

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
        *(("permitAll", 1),
          ("permitPrefix", 2),
          ("permitPrefixAndAllGroups", 4),
          ("permitPrefixAndWellknownGroups", 3),
          ("useGlobalDefaultFilter", 5))
    )


_CiscoAtmIfIlmiAccessFilter_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiAccessFilter_Object = MibTableColumn
ciscoAtmIfIlmiAccessFilter = _CiscoAtmIfIlmiAccessFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 34),
    _CiscoAtmIfIlmiAccessFilter_Type()
)
ciscoAtmIfIlmiAccessFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiAccessFilter.setStatus("current")


class _CiscoAtmIfConfigAESA_Type(OctetString):
    """Custom type ciscoAtmIfConfigAESA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
        ValueSizeConstraint(20, 20),
    )


_CiscoAtmIfConfigAESA_Type.__name__ = "OctetString"
_CiscoAtmIfConfigAESA_Object = MibTableColumn
ciscoAtmIfConfigAESA = _CiscoAtmIfConfigAESA_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 35),
    _CiscoAtmIfConfigAESA_Type()
)
ciscoAtmIfConfigAESA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfConfigAESA.setStatus("current")
_CiscoAtmIfDerivedAESA_Type = AtmAddr
_CiscoAtmIfDerivedAESA_Object = MibTableColumn
ciscoAtmIfDerivedAESA = _CiscoAtmIfDerivedAESA_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 36),
    _CiscoAtmIfDerivedAESA_Type()
)
ciscoAtmIfDerivedAESA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfDerivedAESA.setStatus("current")
_CiscoAtmIfE164Address_Type = AtmAddr
_CiscoAtmIfE164Address_Object = MibTableColumn
ciscoAtmIfE164Address = _CiscoAtmIfE164Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 37),
    _CiscoAtmIfE164Address_Type()
)
ciscoAtmIfE164Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfE164Address.setStatus("current")
_CiscoAtmIfE164AutoConversionOnly_Type = TruthValue
_CiscoAtmIfE164AutoConversionOnly_Object = MibTableColumn
ciscoAtmIfE164AutoConversionOnly = _CiscoAtmIfE164AutoConversionOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 38),
    _CiscoAtmIfE164AutoConversionOnly_Type()
)
ciscoAtmIfE164AutoConversionOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfE164AutoConversionOnly.setStatus("current")
_CiscoAtmIfRxCellUpcViolations_Type = Counter32
_CiscoAtmIfRxCellUpcViolations_Object = MibTableColumn
ciscoAtmIfRxCellUpcViolations = _CiscoAtmIfRxCellUpcViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 39),
    _CiscoAtmIfRxCellUpcViolations_Type()
)
ciscoAtmIfRxCellUpcViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfRxCellUpcViolations.setStatus("current")
_CiscoAtmIfRxCellDiscards_Type = Counter32
_CiscoAtmIfRxCellDiscards_Object = MibTableColumn
ciscoAtmIfRxCellDiscards = _CiscoAtmIfRxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 40),
    _CiscoAtmIfRxCellDiscards_Type()
)
ciscoAtmIfRxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfRxCellDiscards.setStatus("current")


class _CiscoAtmIfIlmiFSMState_Type(Integer32):
    """Custom type ciscoAtmIfIlmiFSMState based on Integer32"""
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
        *(("awaitPnniConfig", 5),
          ("awaitRestartAck", 7),
          ("deviceAndPortTypeComplete", 4),
          ("down", 1),
          ("pnniConfigComplete", 6),
          ("restarting", 2),
          ("upAndNormal", 8),
          ("waitDevType", 3))
    )


_CiscoAtmIfIlmiFSMState_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiFSMState_Object = MibTableColumn
ciscoAtmIfIlmiFSMState = _CiscoAtmIfIlmiFSMState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 41),
    _CiscoAtmIfIlmiFSMState_Type()
)
ciscoAtmIfIlmiFSMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiFSMState.setStatus("current")
_CiscoAtmIfIlmiUpDownChanges_Type = Counter32
_CiscoAtmIfIlmiUpDownChanges_Object = MibTableColumn
ciscoAtmIfIlmiUpDownChanges = _CiscoAtmIfIlmiUpDownChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 42),
    _CiscoAtmIfIlmiUpDownChanges_Type()
)
ciscoAtmIfIlmiUpDownChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiUpDownChanges.setStatus("current")


class _CiscoAtmIfSscopFSMState_Type(Integer32):
    """Custom type ciscoAtmIfSscopFSMState based on Integer32"""
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
        *(("concurrentResyncPending", 10),
          ("dataTransferReady", 4),
          ("idle", 1),
          ("incomingConnectionPending", 3),
          ("incomingRecoveryPending", 9),
          ("incomingResyncPending", 7),
          ("outgoingConnectionPending", 2),
          ("outgoingDisconnectionPending", 5),
          ("outgoingRecoveryPending", 8),
          ("outgoingResyncPending", 6))
    )


_CiscoAtmIfSscopFSMState_Type.__name__ = "Integer32"
_CiscoAtmIfSscopFSMState_Object = MibTableColumn
ciscoAtmIfSscopFSMState = _CiscoAtmIfSscopFSMState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 43),
    _CiscoAtmIfSscopFSMState_Type()
)
ciscoAtmIfSscopFSMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfSscopFSMState.setStatus("current")
_CiscoAtmIfSscopUpDownChanges_Type = Counter32
_CiscoAtmIfSscopUpDownChanges_Object = MibTableColumn
ciscoAtmIfSscopUpDownChanges = _CiscoAtmIfSscopUpDownChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 44),
    _CiscoAtmIfSscopUpDownChanges_Type()
)
ciscoAtmIfSscopUpDownChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfSscopUpDownChanges.setStatus("current")


class _CiscoAtmIfSvcUpcIntentCbr_Type(UpcMethod):
    """Custom type ciscoAtmIfSvcUpcIntentCbr based on UpcMethod"""


_CiscoAtmIfSvcUpcIntentCbr_Object = MibTableColumn
ciscoAtmIfSvcUpcIntentCbr = _CiscoAtmIfSvcUpcIntentCbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 45),
    _CiscoAtmIfSvcUpcIntentCbr_Type()
)
ciscoAtmIfSvcUpcIntentCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcUpcIntentCbr.setStatus("current")


class _CiscoAtmIfSvcUpcIntentVbrRt_Type(UpcMethod):
    """Custom type ciscoAtmIfSvcUpcIntentVbrRt based on UpcMethod"""


_CiscoAtmIfSvcUpcIntentVbrRt_Object = MibTableColumn
ciscoAtmIfSvcUpcIntentVbrRt = _CiscoAtmIfSvcUpcIntentVbrRt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 46),
    _CiscoAtmIfSvcUpcIntentVbrRt_Type()
)
ciscoAtmIfSvcUpcIntentVbrRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcUpcIntentVbrRt.setStatus("current")


class _CiscoAtmIfSvcUpcIntentVbrNrt_Type(UpcMethod):
    """Custom type ciscoAtmIfSvcUpcIntentVbrNrt based on UpcMethod"""


_CiscoAtmIfSvcUpcIntentVbrNrt_Object = MibTableColumn
ciscoAtmIfSvcUpcIntentVbrNrt = _CiscoAtmIfSvcUpcIntentVbrNrt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 47),
    _CiscoAtmIfSvcUpcIntentVbrNrt_Type()
)
ciscoAtmIfSvcUpcIntentVbrNrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcUpcIntentVbrNrt.setStatus("current")


class _CiscoAtmIfSvcUpcIntentAbr_Type(UpcMethod):
    """Custom type ciscoAtmIfSvcUpcIntentAbr based on UpcMethod"""


_CiscoAtmIfSvcUpcIntentAbr_Object = MibTableColumn
ciscoAtmIfSvcUpcIntentAbr = _CiscoAtmIfSvcUpcIntentAbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 48),
    _CiscoAtmIfSvcUpcIntentAbr_Type()
)
ciscoAtmIfSvcUpcIntentAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcUpcIntentAbr.setStatus("current")


class _CiscoAtmIfSvcUpcIntentUbr_Type(UpcMethod):
    """Custom type ciscoAtmIfSvcUpcIntentUbr based on UpcMethod"""


_CiscoAtmIfSvcUpcIntentUbr_Object = MibTableColumn
ciscoAtmIfSvcUpcIntentUbr = _CiscoAtmIfSvcUpcIntentUbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 1, 1, 49),
    _CiscoAtmIfSvcUpcIntentUbr_Type()
)
ciscoAtmIfSvcUpcIntentUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfSvcUpcIntentUbr.setStatus("current")


class _CiscoAtmIfIlmiAccessGlobalDefaultFilter_Type(Integer32):
    """Custom type ciscoAtmIfIlmiAccessGlobalDefaultFilter based on Integer32"""
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
        *(("permitAll", 1),
          ("permitPrefix", 2),
          ("permitPrefixAndAllGroups", 4),
          ("permitPrefixAndWellknownGroups", 3))
    )


_CiscoAtmIfIlmiAccessGlobalDefaultFilter_Type.__name__ = "Integer32"
_CiscoAtmIfIlmiAccessGlobalDefaultFilter_Object = MibScalar
ciscoAtmIfIlmiAccessGlobalDefaultFilter = _CiscoAtmIfIlmiAccessGlobalDefaultFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 2),
    _CiscoAtmIfIlmiAccessGlobalDefaultFilter_Type()
)
ciscoAtmIfIlmiAccessGlobalDefaultFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfIlmiAccessGlobalDefaultFilter.setStatus("current")


class _CiscoAtmIfNotifsEnabled_Type(TruthValue):
    """Custom type ciscoAtmIfNotifsEnabled based on TruthValue"""


_CiscoAtmIfNotifsEnabled_Object = MibScalar
ciscoAtmIfNotifsEnabled = _CiscoAtmIfNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 1, 3),
    _CiscoAtmIfNotifsEnabled_Type()
)
ciscoAtmIfNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfNotifsEnabled.setStatus("current")
_CiscoAtmIfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmIfMIBConformance = _CiscoAtmIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3)
)
_CiscoAtmIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmIfMIBCompliances = _CiscoAtmIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1)
)
_CiscoAtmIfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmIfMIBGroups = _CiscoAtmIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2)
)
atmInterfaceConfEntry.registerAugmentions(
    ("CISCO-ATM-IF-MIB",
     "ciscoAtmIfEntry")
)
ciscoAtmIfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())

# Managed Objects groups

ciscoAtmIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 1)
)
ciscoAtmIfMIBGroup.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSide"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfUniType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVPs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVCs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVPs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVCs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfTotalConnections"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfConfVplIf"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfPortType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitLed"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvLed"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitCells"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvCells"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcMinVci"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiConfiguration"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAddressRegistration"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAutoConfiguration"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiKeepAlive"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSoftVcDestAddress"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfCdLed"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup.setStatus("deprecated")

ciscoAtmIfMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 2)
)
ciscoAtmIfMIBGroup2.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfUniSignallingVersion"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntent"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup2.setStatus("deprecated")

ciscoAtmIfMIBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 3)
)
ciscoAtmIfMIBGroup3.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfAddressType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfAddress"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfWellKnownVcMode"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSignallingAdminStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup3.setStatus("obsolete")

ciscoAtmIfMIBGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 4)
)
ciscoAtmIfMIBGroup4.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAccessGlobalDefaultFilter"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAccessFilter"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup4.setStatus("current")

ciscoAtmIfMIBGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 5)
)
ciscoAtmIfMIBGroup5.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfConfigAESA"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfDerivedAESA"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfE164Address"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfE164AutoConversionOnly"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup5.setStatus("current")

ciscoAtmIfMIBGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 6)
)
ciscoAtmIfMIBGroup6.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfWellKnownVcMode"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSignallingAdminStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup6.setStatus("current")

ciscoAtmIfMIBGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 7)
)
ciscoAtmIfMIBGroup7.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfRxCellUpcViolations"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfRxCellDiscards"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiFSMState"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiUpDownChanges"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSscopFSMState"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSscopUpDownChanges"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup7.setStatus("current")

ciscoAtmIfMIBGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 8)
)
ciscoAtmIfMIBGroup8.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfUniSignallingVersion"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentCbr"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentVbrRt"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentVbrNrt"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentAbr"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSvcUpcIntentUbr"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup8.setStatus("current")

ciscoAtmIfMIBGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 9)
)
ciscoAtmIfMIBGroup9.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSide"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfUniType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVPs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfPVCs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVPs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfActiveSVCs"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfTotalConnections"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfConfVplIf"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfPortType"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitLed"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvLed"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfXmitCells"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfRecvCells"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiConfiguration"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAddressRegistration"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiAutoConfiguration"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiKeepAlive"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSoftVcDestAddress"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfCdLed"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup9.setStatus("current")

ciscoAtmIfMIBGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 10)
)
ciscoAtmIfMIBGroup10.setObjects(
    ("CISCO-ATM-IF-MIB", "ciscoAtmIfNotifsEnabled")
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBGroup10.setStatus("current")


# Notification objects

ciscoAtmIfEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 0, 1)
)
ciscoAtmIfEvent.setObjects(
      *(("CISCO-ATM-IF-MIB", "ciscoAtmIfIlmiFSMState"),
        ("CISCO-ATM-IF-MIB", "ciscoAtmIfSscopFSMState"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoAtmIfNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 2, 11)
)
ciscoAtmIfNotifyGroup.setObjects(
    ("CISCO-ATM-IF-MIB", "ciscoAtmIfEvent")
)
if mibBuilder.loadTexts:
    ciscoAtmIfNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoAtmIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance.setStatus(
        "obsolete"
    )

ciscoAtmIfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance2.setStatus(
        "obsolete"
    )

ciscoAtmIfMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance3.setStatus(
        "obsolete"
    )

ciscoAtmIfMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance4.setStatus(
        "obsolete"
    )

ciscoAtmIfMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance5.setStatus(
        "obsolete"
    )

ciscoAtmIfMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance6.setStatus(
        "obsolete"
    )

ciscoAtmIfMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance7.setStatus(
        "deprecated"
    )

ciscoAtmIfMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 14, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoAtmIfMIBCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-IF-MIB",
    **{"NsapAtmAddr": NsapAtmAddr,
       "AtmAddr": AtmAddr,
       "UpcMethod": UpcMethod,
       "ciscoAtmIfMIB": ciscoAtmIfMIB,
       "ciscoAtmIfMIBNotifications": ciscoAtmIfMIBNotifications,
       "ciscoAtmIfEvent": ciscoAtmIfEvent,
       "ciscoAtmIfMIBObjects": ciscoAtmIfMIBObjects,
       "ciscoAtmIfTable": ciscoAtmIfTable,
       "ciscoAtmIfEntry": ciscoAtmIfEntry,
       "ciscoAtmIfType": ciscoAtmIfType,
       "ciscoAtmIfSide": ciscoAtmIfSide,
       "ciscoAtmIfUniType": ciscoAtmIfUniType,
       "ciscoAtmIfPVPs": ciscoAtmIfPVPs,
       "ciscoAtmIfPVCs": ciscoAtmIfPVCs,
       "ciscoAtmIfActiveSVPs": ciscoAtmIfActiveSVPs,
       "ciscoAtmIfActiveSVCs": ciscoAtmIfActiveSVCs,
       "ciscoAtmIfTotalConnections": ciscoAtmIfTotalConnections,
       "ciscoAtmIfConfVplIf": ciscoAtmIfConfVplIf,
       "ciscoAtmIfPortType": ciscoAtmIfPortType,
       "ciscoAtmIfXmitLed": ciscoAtmIfXmitLed,
       "ciscoAtmIfRecvLed": ciscoAtmIfRecvLed,
       "ciscoAtmIfXmitCells": ciscoAtmIfXmitCells,
       "ciscoAtmIfRecvCells": ciscoAtmIfRecvCells,
       "ciscoAtmIfSvcMinVci": ciscoAtmIfSvcMinVci,
       "ciscoAtmIfIlmiConfiguration": ciscoAtmIfIlmiConfiguration,
       "ciscoAtmIfIlmiAddressRegistration": ciscoAtmIfIlmiAddressRegistration,
       "ciscoAtmIfIlmiAutoConfiguration": ciscoAtmIfIlmiAutoConfiguration,
       "ciscoAtmIfIlmiKeepAlive": ciscoAtmIfIlmiKeepAlive,
       "ciscoAtmIfSoftVcDestAddress": ciscoAtmIfSoftVcDestAddress,
       "ciscoAtmIfUniSignallingVersion": ciscoAtmIfUniSignallingVersion,
       "ciscoAtmIfSvcUpcIntent": ciscoAtmIfSvcUpcIntent,
       "ciscoAtmIfAddressType": ciscoAtmIfAddressType,
       "ciscoAtmIfAddress": ciscoAtmIfAddress,
       "ciscoAtmIfWellKnownVcMode": ciscoAtmIfWellKnownVcMode,
       "ciscoAtmIfSignallingAdminStatus": ciscoAtmIfSignallingAdminStatus,
       "ciscoAtmIfCdLed": ciscoAtmIfCdLed,
       "ciscoAtmIfIlmiAccessFilter": ciscoAtmIfIlmiAccessFilter,
       "ciscoAtmIfConfigAESA": ciscoAtmIfConfigAESA,
       "ciscoAtmIfDerivedAESA": ciscoAtmIfDerivedAESA,
       "ciscoAtmIfE164Address": ciscoAtmIfE164Address,
       "ciscoAtmIfE164AutoConversionOnly": ciscoAtmIfE164AutoConversionOnly,
       "ciscoAtmIfRxCellUpcViolations": ciscoAtmIfRxCellUpcViolations,
       "ciscoAtmIfRxCellDiscards": ciscoAtmIfRxCellDiscards,
       "ciscoAtmIfIlmiFSMState": ciscoAtmIfIlmiFSMState,
       "ciscoAtmIfIlmiUpDownChanges": ciscoAtmIfIlmiUpDownChanges,
       "ciscoAtmIfSscopFSMState": ciscoAtmIfSscopFSMState,
       "ciscoAtmIfSscopUpDownChanges": ciscoAtmIfSscopUpDownChanges,
       "ciscoAtmIfSvcUpcIntentCbr": ciscoAtmIfSvcUpcIntentCbr,
       "ciscoAtmIfSvcUpcIntentVbrRt": ciscoAtmIfSvcUpcIntentVbrRt,
       "ciscoAtmIfSvcUpcIntentVbrNrt": ciscoAtmIfSvcUpcIntentVbrNrt,
       "ciscoAtmIfSvcUpcIntentAbr": ciscoAtmIfSvcUpcIntentAbr,
       "ciscoAtmIfSvcUpcIntentUbr": ciscoAtmIfSvcUpcIntentUbr,
       "ciscoAtmIfIlmiAccessGlobalDefaultFilter": ciscoAtmIfIlmiAccessGlobalDefaultFilter,
       "ciscoAtmIfNotifsEnabled": ciscoAtmIfNotifsEnabled,
       "ciscoAtmIfMIBConformance": ciscoAtmIfMIBConformance,
       "ciscoAtmIfMIBCompliances": ciscoAtmIfMIBCompliances,
       "ciscoAtmIfMIBCompliance": ciscoAtmIfMIBCompliance,
       "ciscoAtmIfMIBCompliance2": ciscoAtmIfMIBCompliance2,
       "ciscoAtmIfMIBCompliance3": ciscoAtmIfMIBCompliance3,
       "ciscoAtmIfMIBCompliance4": ciscoAtmIfMIBCompliance4,
       "ciscoAtmIfMIBCompliance5": ciscoAtmIfMIBCompliance5,
       "ciscoAtmIfMIBCompliance6": ciscoAtmIfMIBCompliance6,
       "ciscoAtmIfMIBCompliance7": ciscoAtmIfMIBCompliance7,
       "ciscoAtmIfMIBCompliance8": ciscoAtmIfMIBCompliance8,
       "ciscoAtmIfMIBGroups": ciscoAtmIfMIBGroups,
       "ciscoAtmIfMIBGroup": ciscoAtmIfMIBGroup,
       "ciscoAtmIfMIBGroup2": ciscoAtmIfMIBGroup2,
       "ciscoAtmIfMIBGroup3": ciscoAtmIfMIBGroup3,
       "ciscoAtmIfMIBGroup4": ciscoAtmIfMIBGroup4,
       "ciscoAtmIfMIBGroup5": ciscoAtmIfMIBGroup5,
       "ciscoAtmIfMIBGroup6": ciscoAtmIfMIBGroup6,
       "ciscoAtmIfMIBGroup7": ciscoAtmIfMIBGroup7,
       "ciscoAtmIfMIBGroup8": ciscoAtmIfMIBGroup8,
       "ciscoAtmIfMIBGroup9": ciscoAtmIfMIBGroup9,
       "ciscoAtmIfMIBGroup10": ciscoAtmIfMIBGroup10,
       "ciscoAtmIfNotifyGroup": ciscoAtmIfNotifyGroup}
)
